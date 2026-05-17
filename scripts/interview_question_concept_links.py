#!/usr/bin/env python3
"""Conservative inline concept-link auditor/applier for interview question pages.

This helper is intentionally narrow: it only scans the two approved imported
interview-question roots, extracts candidates from each page's `## 相关知识 wiki`
section, links only existing vault targets, and protects source/provenance,
code, URL, and existing-link spans.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Iterable

QUESTION_ROOTS = {
    "xiaolinnote": Path("agentic learning/raw/repos/xiaolinnote/questions"),
    "agent_java_offer": Path("agentic learning/raw/repos/agent_java_offer/questions"),
}
DEFAULT_ALIAS_PATH = Path("scripts/interview_question_concept_aliases.json")
DEFAULT_REPORT_JSON = Path("reports/interview-question-concept-card-links-report.json")
DEFAULT_REPORT_MD = Path("reports/interview-question-concept-card-links-report.md")
DEFAULT_BACKLOG_PATH = Path("agentic learning/maps/08 面试题概念卡待补充.md")
BACKLOG_TEMPLATE_PATH = Path("agentic learning/templates/面试题概念卡待补充.md")

WIKI_LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]")
RELATED_HEADING_RE = re.compile(r"^## 相关知识 wiki\s*$", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^##\s+", re.MULTILINE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
URL_RE = re.compile(r"(?:https?://|www\.)[^\s<>)\]]+|<https?://[^>]+>")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\([^\)\n]+\)")
OBSIDIAN_LINK_RE = re.compile(r"\[\[[^\]]+\]\]")

SOURCE_META_PREFIXES = (
    "原始链接：",
    "原始仓库：",
    "原始文件：",
    "提交：",
    "分类：",
    "条目类型：",
    "许可证：",
    "抓取范围：",
    "source:",
    "url:",
    "source_path:",
    "commit:",
    "license:",
    "父级题组：",
    "出现位置：",
    "来源：",
    "**来源**：",
)

# Hard skip aliases that are too broad even when a page's related section gates a target.
FORBIDDEN_ALIASES = {
    "Memory",
    "memory",
    "工具",
    "模型",
    "系统",
    "服务",
    "任务",
    "能力",
    "流程",
    "状态",
    "数据",
    "方法",
    "问题",
    "代码",
    "表",
    "库",
    "图",
    "节点",
    # Too ambiguous in Chinese interview pages:
    # - "观察/观测" often means human inspection or monitoring rather than
    #   ReAct Observation.
    # - "重排" also means JVM/CPU instruction reordering, not only RAG reranking.
    "观察",
    "观测",
    "重排",
    # "成功率" is too broad: in interview answers it may describe tool calls,
    # service availability, business conversion, or task success. Keep the
    # precise "任务成功率" alias instead.
    "成功率",
}

REQUEST_META_PHRASES = (
    "本页来自 2026-",
    "批次索引见",
    "前沿判断见",
    "用户提供的 Hermes",
    "worker-",
)


@dataclass(frozen=True)
class Span:
    start: int
    end: int
    kind: str


@dataclass
class LinkProposal:
    target: str
    alias: str
    start: int
    end: int
    replacement: str
    line: int
    context: str


@dataclass
class PageReport:
    path: str
    root: str
    has_related_section: bool
    related_targets: list[str] = field(default_factory=list)
    existing_targets: list[str] = field(default_factory=list)
    missing_targets: list[str] = field(default_factory=list)
    already_linked_targets: list[str] = field(default_factory=list)
    proposed_links: list[dict] = field(default_factory=list)
    applied_links: int = 0
    unsafe_region_skips: int = 0
    unmatched_existing_targets: list[str] = field(default_factory=list)
    request_meta_hits: list[str] = field(default_factory=list)
    no_match_reason: str | None = None


def normalize_target(target: str) -> str:
    target = target.strip()
    target = target.split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target


class VaultResolver:
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.by_rel: dict[str, Path] = {}
        self.by_stem: defaultdict[str, list[Path]] = defaultdict(list)
        for p in vault_root.rglob("*.md"):
            rel = p.relative_to(vault_root).with_suffix("").as_posix()
            self.by_rel[rel] = p
            self.by_stem[p.stem].append(p)

    def resolve(self, target: str) -> Path | None:
        target = normalize_target(target)
        if not target:
            return None
        if "/" in target:
            if target in self.by_rel:
                return self.by_rel[target]
            direct = self.vault_root / f"{target}.md"
            if direct.exists():
                return direct
        matches = self.by_stem.get(target)
        if matches:
            return matches[0]
        return None


class SpanProtector:
    def __init__(self, text: str):
        self.text = text
        self.spans: list[Span] = []
        self._collect()
        self.mask = self._build_mask(self.spans)
        self.related_spans = [s for s in self.spans if s.kind == "related-section"]
        self.related_mask = self._build_mask(self.related_spans)

    def _add(self, start: int, end: int, kind: str) -> None:
        if 0 <= start < end <= len(self.text):
            self.spans.append(Span(start, end, kind))

    def _collect(self) -> None:
        text = self.text
        # YAML frontmatter at file start.
        if text.startswith("---\n"):
            m = re.search(r"\n---\s*(?:\n|$)", text[4:])
            if m:
                end = 4 + m.end()
                self._add(0, end, "frontmatter")

        # Fenced code blocks.
        in_fence = False
        fence_start = 0
        fence_marker = None
        pos = 0
        for line in text.splitlines(keepends=True):
            m = FENCE_RE.match(line)
            if m:
                marker = m.group(1)
                if not in_fence:
                    in_fence = True
                    fence_start = pos
                    fence_marker = marker
                elif marker == fence_marker:
                    self._add(fence_start, pos + len(line), "fenced-code")
                    in_fence = False
                    fence_marker = None
            pos += len(line)
        if in_fence:
            self._add(fence_start, len(text), "fenced-code")

        # Related wiki section.
        m = RELATED_HEADING_RE.search(text)
        if m:
            after = m.end()
            nxt = NEXT_H2_RE.search(text, after)
            end = nxt.start() if nxt else len(text)
            self._add(m.start(), end, "related-section")

        # Source metadata lines.
        pos = 0
        for line in text.splitlines(keepends=True):
            stripped = line.strip()
            if any(stripped.startswith(prefix) for prefix in SOURCE_META_PREFIXES):
                self._add(pos, pos + len(line), "source-metadata")
            pos += len(line)

        # Inline code, URLs, existing markdown/Obsidian links.
        for kind, rx in (
            ("inline-code", INLINE_CODE_RE),
            ("url", URL_RE),
            ("markdown-link", MARKDOWN_LINK_RE),
            ("obsidian-link", OBSIDIAN_LINK_RE),
        ):
            for match in rx.finditer(text):
                self._add(match.start(), match.end(), kind)

    def _build_mask(self, spans: Iterable[Span]) -> list[bool]:
        mask = [False] * len(self.text)
        for span in spans:
            for i in range(span.start, span.end):
                mask[i] = True
        return mask

    def protected(self, start: int, end: int) -> bool:
        return any(self.mask[start:end])

    def in_related(self, start: int, end: int) -> bool:
        return any(self.related_mask[start:end])


def extract_related_targets(text: str) -> tuple[bool, list[str]]:
    m = RELATED_HEADING_RE.search(text)
    if not m:
        return False, []
    after = m.end()
    nxt = NEXT_H2_RE.search(text, after)
    section = text[after : nxt.start() if nxt else len(text)]
    targets: list[str] = []
    seen: set[str] = set()
    for raw_target in WIKI_LINK_RE.findall(section):
        target = normalize_target(raw_target)
        if target and target not in seen:
            targets.append(target)
            seen.add(target)
    return True, targets


def load_alias_map(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    aliases: dict[str, list[str]] = {}
    for target, value in data.items():
        if isinstance(value, dict):
            raw = value.get("aliases", [])
        else:
            raw = value
        if isinstance(raw, str):
            raw = [raw]
        if isinstance(raw, list):
            aliases[target] = [str(x).strip() for x in raw if str(x).strip()]
    return aliases


def alias_candidates(target: str, alias_map: dict[str, list[str]]) -> list[str]:
    raw_aliases = [target]
    raw_aliases.extend(alias_map.get(target, []))
    dedup: list[str] = []
    seen: set[str] = set()
    for alias in raw_aliases:
        alias = alias.strip()
        if not alias or alias in seen:
            continue
        if alias in FORBIDDEN_ALIASES:
            continue
        # Avoid one-character CJK or ASCII aliases and punctuation-like aliases.
        if len(alias) < 2:
            continue
        if re.fullmatch(r"[\W_]+", alias, flags=re.UNICODE):
            continue
        dedup.append(alias)
        seen.add(alias)
    # Longest alias wins when starts are equal; English exact names remain available.
    dedup.sort(key=lambda x: (-len(x), x.lower()))
    return dedup


def is_ascii_word_char(ch: str) -> bool:
    return ch.isascii() and (ch.isalnum() or ch in "_-")


def boundary_ok(text: str, start: int, end: int, alias: str) -> bool:
    # ASCII / mixed aliases should not be embedded in larger identifiers.
    if re.search(r"[A-Za-z0-9]", alias):
        prev = text[start - 1] if start > 0 else ""
        nxt = text[end] if end < len(text) else ""
        if prev and is_ascii_word_char(prev):
            return False
        if nxt and is_ascii_word_char(nxt):
            return False
    # A few Chinese aliases are meaningful as terms but become false positives
    # inside longer everyday words. "工作流" can be a valid Agent Workflow
    # alias, but "工作流程" is usually just "process / procedure" and should
    # stay plain text unless a future concept explicitly covers that term.
    nxt = text[end] if end < len(text) else ""
    if alias == "工作流" and nxt == "程":
        return False
    return True


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def context_snippet(text: str, start: int, end: int, radius: int = 28) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    return text[left:right].replace("\n", " ").strip()


def overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return not (a_end <= b_start or a_start >= b_end)


def parse_body_wikilinks(text: str, protector: SpanProtector) -> set[str]:
    linked: set[str] = set()
    for m in WIKI_LINK_RE.finditer(text):
        start, end = m.span()
        if protector.in_related(start, end):
            continue
        # The link span itself is protected, but links inside frontmatter/code/URL/source
        # metadata should not count as existing body concept links.
        non_link_protected = any(
            span.kind not in {"obsidian-link", "markdown-link"}
            and overlaps(start, end, span.start, span.end)
            for span in protector.spans
        )
        if non_link_protected:
            continue
        target = normalize_target(m.group(1))
        if target:
            linked.add(target)
    return linked


def choose_proposal_for_target(
    text: str,
    protector: SpanProtector,
    target: str,
    aliases: list[str],
    occupied: list[tuple[int, int]],
    longer_alias_spans: list[tuple[int, int, str, str]],
) -> tuple[LinkProposal | None, int]:
    protected_hits = 0
    matches: list[tuple[int, int, str]] = []
    for alias in aliases:
        for m in re.finditer(re.escape(alias), text):
            start, end = m.span()
            if not boundary_ok(text, start, end, alias):
                continue
            if protector.protected(start, end):
                protected_hits += 1
                continue
            # Avoid linking a short alias inside another candidate concept's longer
            # alias, e.g. `Prompt` inside `Prompt Injection` or `观测` inside
            # `可观测性`. This keeps candidate-gated linking conservative when a
            # related section contains neighboring concepts.
            if any(
                other_target != target
                and (other_end - other_start) > (end - start)
                and overlaps(start, end, other_start, other_end)
                for other_start, other_end, other_target, _other_alias in longer_alias_spans
            ):
                continue
            if any(not (end <= a or start >= b) for a, b in occupied):
                continue
            matches.append((start, end, alias))
    if not matches:
        return None, protected_hits
    # Earliest safe occurrence; if tied, longest alias wins.
    matches.sort(key=lambda item: (item[0], -(item[1] - item[0]), item[2].lower()))
    start, end, alias = matches[0]
    replacement = f"[[{target}]]" if alias == target else f"[[{target}|{alias}]]"
    return (
        LinkProposal(
            target=target,
            alias=alias,
            start=start,
            end=end,
            replacement=replacement,
            line=line_number(text, start),
            context=context_snippet(text, start, end),
        ),
        protected_hits,
    )


def apply_proposals(text: str, proposals: list[LinkProposal]) -> str:
    for p in sorted(proposals, key=lambda item: item.start, reverse=True):
        text = text[: p.start] + p.replacement + text[p.end :]
    return text


def process_page(
    path: Path,
    rel_path: str,
    root_name: str,
    resolver: VaultResolver,
    alias_map: dict[str, list[str]],
    apply: bool,
) -> tuple[PageReport, str | None]:
    text = path.read_text(encoding="utf-8")
    has_related, related_targets = extract_related_targets(text)
    protector = SpanProtector(text)
    report = PageReport(path=rel_path, root=root_name, has_related_section=has_related, related_targets=related_targets)
    if not has_related:
        report.no_match_reason = "missing related section"
        return report, None

    existing_targets = [t for t in related_targets if resolver.resolve(t)]
    missing_targets = [t for t in related_targets if not resolver.resolve(t)]
    report.existing_targets = existing_targets
    report.missing_targets = missing_targets

    body_links = parse_body_wikilinks(text, protector)
    already = [t for t in existing_targets if t in body_links]
    report.already_linked_targets = already

    longer_alias_spans: list[tuple[int, int, str, str]] = []
    for target in existing_targets:
        for alias in alias_candidates(target, alias_map):
            for m in re.finditer(re.escape(alias), text):
                start, end = m.span()
                if not boundary_ok(text, start, end, alias):
                    continue
                if protector.protected(start, end):
                    continue
                longer_alias_spans.append((start, end, target, alias))

    proposals: list[LinkProposal] = []
    occupied: list[tuple[int, int]] = []
    unsafe_hits = 0
    unmatched: list[str] = []
    for target in existing_targets:
        if target in body_links:
            continue
        aliases = alias_candidates(target, alias_map)
        proposal, protected_hits = choose_proposal_for_target(
            text,
            protector,
            target,
            aliases,
            occupied,
            longer_alias_spans,
        )
        unsafe_hits += protected_hits
        if proposal:
            proposals.append(proposal)
            occupied.append((proposal.start, proposal.end))
        else:
            unmatched.append(target)

    report.unsafe_region_skips = unsafe_hits
    report.unmatched_existing_targets = unmatched
    report.proposed_links = [asdict(p) for p in proposals]
    report.request_meta_hits = [phrase for phrase in REQUEST_META_PHRASES if phrase in text]

    if not proposals and not already:
        if missing_targets and not existing_targets:
            report.no_match_reason = "all related targets are missing"
        elif unmatched:
            report.no_match_reason = "no safe alias match"
        else:
            report.no_match_reason = "no body concept links found"

    if apply and proposals:
        new_text = apply_proposals(text, proposals)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            report.applied_links = len(proposals)
            return report, new_text
    return report, None


def question_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.md"), key=lambda p: p.as_posix())


def markdown_link_to_file(rel_path: str) -> str:
    display = Path(rel_path).stem
    target = rel_path[:-3] if rel_path.endswith(".md") else rel_path
    if target.startswith("agentic learning/"):
        target = target[len("agentic learning/") :]
    return f"[[{target}|{display}]]"


def select_samples(page_reports: list[PageReport]) -> list[str]:
    samples: list[str] = []
    preferred = [
        "agentic learning/raw/repos/xiaolinnote/questions/010 ai agent 3. Workflow，Agent，Tools 这三个的概念和区别介绍一下？.md",
        "agentic learning/raw/repos/xiaolinnote/questions/045 ai tools 10. MCP 和 Agent Skill 的区别是什么？.md",
        "agentic learning/raw/repos/xiaolinnote/questions/052 ai tools 1. 什么是 Function Calling ？原理是什么？.md",
        "agentic learning/raw/repos/xiaolinnote/questions/078 home 首页.md",
        "agentic learning/raw/repos/agent_java_offer/questions/106 01_AI 03_RAG 4 向量检索.md",
        "agentic learning/raw/repos/agent_java_offer/questions/228 01_AI 08_框架协议与工程化 追问：LCEL 和手写 if else 调用代码相比，工程收益在哪？.md",
        "agentic learning/raw/repos/agent_java_offer/questions/301 02_后端 04_并发与异步任务 `CompletableFuture` 常见坑？.md",
        "agentic learning/raw/repos/agent_java_offer/questions/407 02_后端 10_网络I_O与发布治理 Netty 如何体现 Reactor 模型？.md",
        "agentic learning/raw/repos/agent_java_offer/questions/471 04_系统设计 02_高并发系统设计 高并发系统的“削峰填谷”怎么做？.md",
        "agentic learning/raw/repos/agent_java_offer/questions/637 06_算法与数据结构 02_常见算法题 你怎么系统准备算法题？.md",
    ]
    existing = {r.path for r in page_reports}
    for item in preferred:
        if item in existing and item not in samples:
            samples.append(item)
    # Fill with modified/proposed, already-linked, and no-match pages.
    pools = [
        [r.path for r in page_reports if r.proposed_links],
        [r.path for r in page_reports if r.already_linked_targets],
        [r.path for r in page_reports if r.no_match_reason],
    ]
    for pool in pools:
        for item in pool:
            if item not in samples:
                samples.append(item)
            if len(samples) >= 12:
                break
        if len(samples) >= 12:
            break
    return samples[:12]


def build_summary(page_reports: list[PageReport], mode: str) -> dict:
    root_breakdown: dict[str, dict] = {}
    for name in QUESTION_ROOTS:
        scoped = [r for r in page_reports if r.root == name]
        root_breakdown[name] = {
            "total": len(scoped),
            "with_related_section": sum(r.has_related_section for r in scoped),
            "would_modify_pages": sum(bool(r.proposed_links) for r in scoped),
            "modified_pages": sum(r.applied_links > 0 for r in scoped),
            "proposed_inline_links": sum(len(r.proposed_links) for r in scoped),
            "applied_inline_links": sum(r.applied_links for r in scoped),
            "already_linked_pages": sum(bool(r.already_linked_targets) for r in scoped),
            "skipped_no_match_pages": sum(bool(r.no_match_reason) for r in scoped),
        }
    missing_entries = [(r.path, target) for r in page_reports for target in r.missing_targets]
    missing_counter = Counter(target for _, target in missing_entries)
    samples = select_samples(page_reports)
    return {
        "schema_version": "1.0",
        "mode": mode,
        "total_question_pages_scanned": len(page_reports),
        "total_pages_scanned": len(page_reports),
        "pages_with_related_section": sum(r.has_related_section for r in page_reports),
        "would_modify_pages": sum(bool(r.proposed_links) for r in page_reports),
        "modified_pages": sum(r.applied_links > 0 for r in page_reports),
        "inline_links_inserted": sum(r.applied_links for r in page_reports) if mode == "apply" else sum(len(r.proposed_links) for r in page_reports),
        "proposed_inline_links": sum(len(r.proposed_links) for r in page_reports),
        "applied_inline_links": sum(r.applied_links for r in page_reports),
        "already_linked_pages": sum(bool(r.already_linked_targets) for r in page_reports),
        "already_linked_targets": sum(len(r.already_linked_targets) for r in page_reports),
        "skipped_no_match_pages": sum(bool(r.no_match_reason) for r in page_reports),
        "unsafe_region_skips": sum(r.unsafe_region_skips for r in page_reports),
        "protected_region_violations": 0,
        "request_meta_page_hits": [r.path for r in page_reports if r.request_meta_hits],
        "missing_concept_candidates": len(missing_entries),
        "missing_concept_unique_candidates": len(missing_counter),
        "duplicate_missing_candidates": sum(max(0, n - 1) for n in missing_counter.values()),
        "roots": root_breakdown,
        "sample_files_selected": samples,
        "missing_targets": dict(sorted(missing_counter.items())),
    }


def write_json_report(path: Path, summary: dict, page_reports: list[PageReport]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        **summary,
        "pages": [asdict(r) for r in page_reports],
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md_report(path: Path, summary: dict, page_reports: list[PageReport]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 面试题概念卡内联链接审计报告",
        "",
        f"- 模式：`{summary['mode']}`",
        f"- 扫描题页：{summary['total_question_pages_scanned']}",
        f"- 含 `## 相关知识 wiki`：{summary['pages_with_related_section']}",
        f"- 已有正文概念链接页：{summary['already_linked_pages']}",
        f"- 本次可新增/已新增链接：{summary['inline_links_inserted']}",
        f"- would modify pages：{summary['would_modify_pages']}",
        f"- skipped/no-match pages：{summary['skipped_no_match_pages']}",
        f"- unsafe-region skips：{summary['unsafe_region_skips']}",
        f"- missing concept candidates：{summary['missing_concept_candidates']}（unique {summary['missing_concept_unique_candidates']}）",
        f"- protected-region violations：{summary['protected_region_violations']}",
        "",
        "## Per-root breakdown",
        "",
        "| root | total | related | already-linked pages | would-modify pages | proposed links | skipped/no-match |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for root, data in summary["roots"].items():
        lines.append(
            f"| {root} | {data['total']} | {data['with_related_section']} | {data['already_linked_pages']} | {data['would_modify_pages']} | {data['proposed_inline_links']} | {data['skipped_no_match_pages']} |"
        )
    lines.extend(["", "## Sample files selected", ""])
    for sample in summary["sample_files_selected"]:
        lines.append(f"- {sample}")
    lines.extend(["", "## Missing targets", ""])
    if summary["missing_targets"]:
        for target, count in summary["missing_targets"].items():
            lines.append(f"- `{target}` — {count}")
    else:
        lines.append("- None: all related targets resolved to an existing vault Markdown page.")
    lines.extend(["", "## No-match pages（前 80 条）", ""])
    no_match = [r for r in page_reports if r.no_match_reason]
    if no_match:
        for r in no_match[:80]:
            lines.append(f"- {r.path} — {r.no_match_reason}")
        if len(no_match) > 80:
            lines.append(f"- ... 其余 {len(no_match)-80} 条见 JSON 报告。")
    else:
        lines.append("- None")
    lines.extend(["", "## Proposed/applied links（前 80 条）", ""])
    emitted = 0
    for r in page_reports:
        for p in r.proposed_links:
            lines.append(f"- {r.path}:{p['line']} — `{p['alias']}` -> `[[{p['target']}]]`")
            emitted += 1
            if emitted >= 80:
                break
        if emitted >= 80:
            break
    if emitted == 0:
        lines.append("- None")
    elif summary["proposed_inline_links"] > emitted:
        lines.append(f"- ... 其余 {summary['proposed_inline_links']-emitted} 条见 JSON 报告。")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_backlog_page(path: Path, root: Path, page_reports: list[PageReport]) -> None:
    full_path = root / path
    if full_path.exists():
        text = full_path.read_text(encoding="utf-8")
    else:
        template = root / BACKLOG_TEMPLATE_PATH
        if template.exists():
            text = template.read_text(encoding="utf-8")
        else:
            today = date.today().isoformat()
            text = f"""---\ntype: map\ntopic:\n  - interview\n  - concepts\n  - wiki-maintenance\nstatus: active\ncreated: {today}\nupdated: {today}\nrelated:\n  - \"[[资料收集索引]]\"\n  - \"[[04 页面目录]]\"\n  - \"[[05 Query 写回队列]]\"\n---\n\n# 08 面试题概念卡待补充\n\n## 使用规则\n\n- 后续 team workers 可以追加候选；重复允许，后续统一合并。\n- 只记录候选，不在本页写完整解释。\n\n## 候选表\n\n| 候选词 | 建议 canonical name | 来源题页 | 出现/证据 | Worker 备注 | 状态 |\n|---|---|---|---|---|---|\n"""
        full_path.parent.mkdir(parents=True, exist_ok=True)

    # Refresh updated date conservatively.
    today = date.today().isoformat()
    text = re.sub(r"^updated:\s*\d{4}-\d{2}-\d{2}\s*$", f"updated: {today}", text, flags=re.MULTILINE)

    if "## 候选表" not in text:
        text += "\n## 候选表\n\n| 候选词 | 建议 canonical name | 来源题页 | 出现/证据 | Worker 备注 | 状态 |\n|---|---|---|---|---|---|\n"
    if "| 候选词 | 建议 canonical name | 来源题页 | 出现/证据 | Worker 备注 | 状态 |" not in text:
        text += "\n| 候选词 | 建议 canonical name | 来源题页 | 出现/证据 | Worker 备注 | 状态 |\n|---|---|---|---|---|---|\n"

    existing_lines = set(text.splitlines())
    rows: list[str] = []
    by_target: dict[str, list[str]] = defaultdict(list)
    for r in page_reports:
        for target in r.missing_targets:
            by_target[target].append(r.path)
    for target, pages in sorted(by_target.items()):
        first = pages[0]
        source_link = markdown_link_to_file(first)
        evidence = f"related section; {len(pages)} page(s)"
        row = f"| {target} | {target} | {source_link} | {evidence} | script audit: missing target; do not create weak card automatically | pending |"
        if row not in existing_lines:
            rows.append(row)
    if rows:
        # Append rows directly after candidate table separator, preserving existing content.
        lines = text.splitlines()
        insert_at = None
        for i, line in enumerate(lines):
            if line.startswith("|---") and i > 0 and "候选词" in lines[i - 1]:
                insert_at = i + 1
                break
        if insert_at is None:
            text = text.rstrip() + "\n" + "\n".join(rows) + "\n"
        else:
            lines[insert_at:insert_at] = rows
            text = "\n".join(lines) + "\n"
    # If no missing rows, keep the placeholder from template; no full explanations are added.
    full_path.write_text(text, encoding="utf-8")


def run(root: Path, alias_path: Path, report_json: Path, report_md: Path, backlog_path: Path, apply: bool) -> dict:
    resolver = VaultResolver(root / "agentic learning")
    alias_map = load_alias_map(root / alias_path)
    page_reports: list[PageReport] = []
    for root_name, rel_root in QUESTION_ROOTS.items():
        abs_root = root / rel_root
        for path in question_files(abs_root):
            rel_path = path.relative_to(root).as_posix()
            report, _ = process_page(path, rel_path, root_name, resolver, alias_map, apply=apply)
            page_reports.append(report)
    mode = "apply" if apply else "dry-run"
    summary = build_summary(page_reports, mode)
    ensure_backlog_page(backlog_path, root, page_reports)
    write_json_report(root / report_json, summary, page_reports)
    write_md_report(root / report_md, summary, page_reports)
    return {"summary": summary, "page_reports": page_reports}


def run_self_tests() -> None:
    sample = """---\ntitle: Agent\n---\n\n## 相关知识 wiki\n\n- [[Agent]]\n- [[Tool Calling|工具调用]]\n- [[RAG#某节]]\n\n## 页面正文\n\n原始链接：https://example.com/Agent/Tool\n正文 Agent 和 工具调用 可链接。`Agent` 不可链接。\n\n```python\n# Agent should not link here\n```\n"""
    has_related, targets = extract_related_targets(sample)
    assert has_related and targets == ["Agent", "Tool Calling", "RAG"], targets
    protector = SpanProtector(sample)
    assert protector.protected(sample.index("title"), sample.index("title") + 5)
    assert protector.protected(sample.index("https://"), sample.index("https://") + 8)
    assert protector.protected(sample.index("`Agent`"), sample.index("`Agent`") + 7)
    assert protector.protected(sample.rindex("# Agent"), sample.rindex("# Agent") + 7)
    alias_map = {"Agent": ["Agent"], "Tool Calling": ["工具调用"], "RAG": ["RAG"]}
    # Fake resolver by monkeypatching a minimal object.
    class FakeResolver:
        def resolve(self, target: str):
            return (
                Path(target + ".md")
                if target in {
                    "Agent",
                    "Tool Calling",
                    "RAG",
                    "ReAct",
                    "Agent Workflow",
                    "Task Success Rate",
                    "Prompt",
                    "Prompt Injection",
                    "Observation",
                    "Observability",
                }
                else None
            )
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "sample.md"
        p.write_text(sample, encoding="utf-8")
        report, new_text = process_page(p, "sample.md", "test", FakeResolver(), alias_map, apply=True)
        assert report.applied_links == 2, report
        out = p.read_text(encoding="utf-8")
        assert "[[Agent]] 和 [[Tool Calling|工具调用]]" in out
        assert "https://example.com/Agent/Tool" in out
        assert "`Agent`" in out
        assert "# Agent should not link here" in out
    # Longest alias / ASCII boundary: ReAct should not link Reactor.
    text = "## 相关知识 wiki\n\n- [[ReAct]]\n\n## 页面正文\n\nReactor 不是 ReAct。\n"
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "react.md"
        p.write_text(text, encoding="utf-8")
        report, _ = process_page(p, "react.md", "test", FakeResolver(), {"ReAct": ["ReAct"]}, apply=True)
        out = p.read_text(encoding="utf-8")
        assert "Reactor 不是 [[ReAct]]" in out
        assert report.applied_links == 1
    # Chinese alias boundary: "工作流程" is not the Agent Workflow concept.
    text = "## 相关知识 wiki\n\n- [[Agent Workflow]]\n\n## 页面正文\n\n普通工作流程不是智能体工作流。\n"
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "workflow.md"
        p.write_text(text, encoding="utf-8")
        report, _ = process_page(
            p,
            "workflow.md",
            "test",
            FakeResolver(),
            {"Agent Workflow": ["工作流", "智能体工作流"]},
            apply=True,
        )
        out = p.read_text(encoding="utf-8")
        assert "普通工作流程" in out
        assert "[[Agent Workflow|工作流]]程" not in out
        assert "[[Agent Workflow|智能体工作流]]" in out
        assert report.applied_links == 1
    # Broad metric word "成功率" is not precise enough for Task Success Rate.
    text = "## 相关知识 wiki\n\n- [[Task Success Rate]]\n\n## 页面正文\n\n工具调用成功率要和任务成功率分开看。\n"
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "success-rate.md"
        p.write_text(text, encoding="utf-8")
        report, _ = process_page(
            p,
            "success-rate.md",
            "test",
            FakeResolver(),
            {"Task Success Rate": ["成功率", "任务成功率"]},
            apply=True,
        )
        out = p.read_text(encoding="utf-8")
        assert "工具调用成功率" in out
        assert "[[Task Success Rate|成功率]]" not in out
        assert "[[Task Success Rate|任务成功率]]" in out
        assert report.applied_links == 1
    # Short alias must not be linked inside another page candidate's longer alias.
    text = "## 相关知识 wiki\n\n- [[Prompt]]\n- [[Prompt Injection]]\n- [[Observation]]\n- [[Observability]]\n\n## 页面正文\n\n提示注入（Prompt Injection）和可观测性不是普通 Observation。\n"
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "overlap.md"
        p.write_text(text, encoding="utf-8")
        aliases = {
            "Prompt": ["提示", "Prompt"],
            "Prompt Injection": ["提示注入", "Prompt Injection"],
            "Observation": ["观察", "观测"],
            "Observability": ["可观测性"],
        }
        report, _ = process_page(p, "overlap.md", "test", FakeResolver(), aliases, apply=True)
        out = p.read_text(encoding="utf-8")
        assert "[[Prompt Injection|提示注入]]（Prompt Injection）" in out
        assert "和[[Observability|可观测性]]不是普通 [[Observation]]" in out
        assert "[[Prompt|Prompt]] Injection" not in out
        assert "可[[Observation|观测]]性" not in out
        assert report.applied_links == 3


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit/apply conservative inline concept links in interview question pages.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Do not edit question pages; emit reports only.")
    mode.add_argument("--apply", action="store_true", help="Apply proposed inline links and emit reports.")
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--alias-map", default=str(DEFAULT_ALIAS_PATH), help="Alias JSON path relative to root.")
    parser.add_argument("--report-json", default=str(DEFAULT_REPORT_JSON), help="JSON report path relative to root.")
    parser.add_argument("--report-md", default=str(DEFAULT_REPORT_MD), help="Markdown report path relative to root.")
    parser.add_argument("--backlog-path", default=str(DEFAULT_BACKLOG_PATH), help="Backlog page path relative to root.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in parser/protection tests and exit.")
    args = parser.parse_args(argv)

    if args.self_test:
        run_self_tests()
        print("self-test: PASS")
        return 0
    if not (args.dry_run or args.apply):
        parser.error("choose --dry-run or --apply")

    root = Path(args.root).resolve()
    result = run(
        root=root,
        alias_path=Path(args.alias_map),
        report_json=Path(args.report_json),
        report_md=Path(args.report_md),
        backlog_path=Path(args.backlog_path),
        apply=args.apply,
    )
    summary = result["summary"]
    print(json.dumps({k: summary[k] for k in (
        "mode",
        "total_question_pages_scanned",
        "pages_with_related_section",
        "would_modify_pages",
        "modified_pages",
        "inline_links_inserted",
        "skipped_no_match_pages",
        "missing_concept_candidates",
        "protected_region_violations",
    )}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
