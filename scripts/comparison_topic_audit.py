#!/usr/bin/env python3
"""Audit comparison topic pages against the vault's boundary-map standard.

This script is intentionally read-only. It inspects
`agentic learning/wiki/topics/*对比*.md` pages and checks the structural
constraints that make comparison pages useful as learning boundary maps:

- required comparison sections from `LLM Wiki 工作流`
- frontmatter basics for map/topic pages
- evidence-boundary markers in `## 证据锚点`
- explicit non-evidence labeling for analogies
- lightweight weak-page heuristics, such as too few table rows or links

Usage:
  python3 scripts/comparison_topic_audit.py
  python3 scripts/comparison_topic_audit.py --format json --output reports/comparison-topic-audit.json
  python3 scripts/comparison_topic_audit.py --team-plan --format markdown
  python3 scripts/comparison_topic_audit.py --strict
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
TOPIC_DIR = ROOT / "agentic learning" / "wiki" / "topics"

REQUIRED_FRONTMATTER = ["type", "topic", "status", "created", "updated", "source", "evidence", "related"]

REQUIRED_SECTIONS = [
    "## 一句话总览",
    "## 为什么这组值得对比",
    "## 共同问题域",
    "## 核心区别表",
    "## 最容易混淆的边界",
    "## 执行时序 / 机制差异",
    "## 学习类比（非证据）",
    "## 现代系统如何吸收或限制",
    "## 什么时候用哪个判断",
    "## 它们共同不是什么",
    "## 证据锚点",
    "## 复习触发",
    "## 相关链接",
]

EVIDENCE_MARKERS = ["Evidence type:", "Confidence:", "Boundary:"]
ANALOGY_BOUNDARY_RE = re.compile(r"(learning analogy|非证据|不是论文|不是.+官方文档|类比边界)", re.I)
MODERN_BOUNDARY_RE = re.compile(r"(来源支持|Source|工程综合\s*/\s*inference|inference|外推)", re.I)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

LANE_RULES: list[tuple[str, set[str], list[str]]] = [
    (
        "comparison-1-agent-runtime",
        {"agent", "framework", "workflow", "memory", "infrastructure"},
        ["Agent", "Memory", "Handoff", "Coding", "Browser", "Computer Use", "工程", "执行栈"],
    ),
    (
        "comparison-2-tools-security-protocol",
        {"tools", "tool-use", "security", "protocol", "frontier"},
        ["Tool", "MCP", "安全", "Protocol", "Permission", "Registry"],
    ),
    (
        "comparison-3-evaluation-observability",
        {"evaluation", "observability"},
        ["Evaluation", "Observability", "Audit", "Trace", "Trajectory"],
    ),
    (
        "comparison-4-rag-llm-retrieval",
        {"rag", "retrieval", "llm", "reasoning", "planning"},
        ["RAG", "Retrieval", "LLM", "ReAct", "Plan", "Reflexion", "Context"],
    ),
]


@dataclass
class ComparisonAudit:
    file: str
    title: str
    topics: list[str]
    status: str
    assigned_lane: str
    source_count: int
    evidence_count: int
    related_count: int
    link_count: int
    table_rows: int
    compared_link_count: int
    body_chars: int
    missing_frontmatter: list[str]
    missing_sections: list[str]
    has_learning_analogy_boundary: bool
    has_modern_absorption_boundary: bool
    has_evidence_type: bool
    has_confidence: bool
    has_boundary: bool
    quality_flags: list[str]
    action: str


def parse_frontmatter(text: str) -> dict[str, object]:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}

    fm: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if key_match:
            key, value = key_match.groups()
            current_key = key
            value = value.strip()
            if value in {"", "[]"}:
                fm[key] = []
            else:
                fm[key] = value.strip('"')
            continue
        item_match = re.match(r"^\s*-\s*(.*)$", line)
        if item_match and current_key:
            fm.setdefault(current_key, [])
            if not isinstance(fm[current_key], list):
                fm[current_key] = [fm[current_key]]
            item = item_match.group(1).strip().strip('"')
            if item:
                fm[current_key].append(item)
    return fm


def list_value(fm: dict[str, object], key: str) -> list[str]:
    value = fm.get(key, [])
    if isinstance(value, list):
        return [str(v) for v in value if str(v)]
    if value:
        return [str(value)]
    return []


def scalar_value(fm: dict[str, object], key: str) -> str:
    value = fm.get(key, "")
    if isinstance(value, list):
        return ",".join(str(v) for v in value)
    return str(value or "")


def section_body(text: str, heading: str) -> str:
    match = re.search(rf"(?m)^{re.escape(heading)}\s*$", text)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"(?m)^## ", rest)
    if next_heading:
        return rest[: next_heading.start()].strip()
    return rest.strip()


def count_core_table_rows(core_section: str) -> int:
    table_lines = [line for line in core_section.splitlines() if line.startswith("|")]
    data_rows = []
    for line in table_lines:
        stripped = line.strip()
        if re.match(r"^\|\s*:?-{3,}", stripped):
            continue
        data_rows.append(line)
    # The first non-separator row is usually the header.
    return max(0, len(data_rows) - 1)


def assign_lane(path: Path, topics: list[str]) -> str:
    name = path.stem
    topic_set = set(topics)
    scores: dict[str, int] = {}
    for lane, lane_topics, keywords in LANE_RULES:
        score = len(topic_set & lane_topics) * 3
        score += sum(1 for kw in keywords if kw.lower() in name.lower())
        scores[lane] = score
    lane, score = max(scores.items(), key=lambda kv: (kv[1], kv[0]))
    return lane if score > 0 else "comparison-1-agent-runtime"


def audit_page(path: Path, *, min_page_chars: int) -> ComparisonAudit:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    topics = list_value(fm, "topic")
    status = scalar_value(fm, "status")
    source = list_value(fm, "source")
    evidence = list_value(fm, "evidence")
    related = list_value(fm, "related")
    lane = assign_lane(path, topics)

    missing_frontmatter = [key for key in REQUIRED_FRONTMATTER if key not in fm]
    missing_sections = [
        section for section in REQUIRED_SECTIONS if not re.search(rf"(?m)^{re.escape(section)}\s*$", text)
    ]

    core_section = section_body(text, "## 核心区别表")
    analogy_section = section_body(text, "## 学习类比（非证据）")
    modern_section = section_body(text, "## 现代系统如何吸收或限制")
    evidence_section = section_body(text, "## 证据锚点")

    link_count = len(WIKI_LINK_RE.findall(text))
    compared_links = sorted(set(WIKI_LINK_RE.findall(core_section)))
    table_rows = count_core_table_rows(core_section)

    has_analogy_boundary = bool(ANALOGY_BOUNDARY_RE.search(analogy_section))
    has_modern_boundary = bool(MODERN_BOUNDARY_RE.search(modern_section))
    has_evidence_type = "Evidence type:" in evidence_section
    has_confidence = "Confidence:" in evidence_section
    has_boundary = "Boundary:" in evidence_section

    flags: list[str] = []
    if missing_frontmatter:
        flags.append("frontmatter fields missing")
    if scalar_value(fm, "type") != "map":
        flags.append("frontmatter type is not map")
    if "comparison" not in topics:
        flags.append("frontmatter topic missing comparison")
    if not source:
        flags.append("frontmatter source empty")
    if not evidence:
        flags.append("frontmatter evidence empty")
    if not related:
        flags.append("frontmatter related empty")
    if missing_sections:
        flags.append("required sections missing")
    if table_rows < 2:
        flags.append("core difference table has fewer than 2 data rows")
    if len(compared_links) < 2:
        flags.append("core difference table links fewer than 2 comparable anchors")
    if link_count < 6:
        flags.append("too few wiki links for a comparison boundary map")
    if len(text) < min_page_chars:
        flags.append(f"page too short for comparison topic (<{min_page_chars} chars)")
    if "## 学习类比（非证据）" in text and not has_analogy_boundary:
        flags.append("learning analogy boundary not explicit")
    if "## 现代系统如何吸收或限制" in text and not has_modern_boundary:
        flags.append("modern absorption lacks source/inference boundary marker")
    missing_evidence_markers = [marker for marker in EVIDENCE_MARKERS if marker not in evidence_section]
    if missing_evidence_markers:
        flags.append("evidence type/confidence/boundary markers missing")

    if not flags:
        action = "ok"
    elif "required sections missing" in flags or "evidence type/confidence/boundary markers missing" in flags:
        action = "repair comparison template/evidence boundary"
    elif "core difference table has fewer than 2 data rows" in flags or "page too short" in "; ".join(flags):
        action = "strengthen or move weak comparison back to queue"
    else:
        action = "repair metadata or shallow boundary markers"

    return ComparisonAudit(
        file=str(path.relative_to(ROOT)),
        title=path.stem,
        topics=topics,
        status=status,
        assigned_lane=lane,
        source_count=len(source),
        evidence_count=len(evidence),
        related_count=len(related),
        link_count=link_count,
        table_rows=table_rows,
        compared_link_count=len(compared_links),
        body_chars=len(text),
        missing_frontmatter=missing_frontmatter,
        missing_sections=missing_sections,
        has_learning_analogy_boundary=has_analogy_boundary,
        has_modern_absorption_boundary=has_modern_boundary,
        has_evidence_type=has_evidence_type,
        has_confidence=has_confidence,
        has_boundary=has_boundary,
        quality_flags=flags,
        action=action,
    )


def audit_all(topic_dir: Path, *, min_page_chars: int) -> list[ComparisonAudit]:
    return [
        audit_page(path, min_page_chars=min_page_chars)
        for path in sorted(topic_dir.glob("*对比*.md"))
        if path.is_file()
    ]


def to_json(pages: list[ComparisonAudit]) -> str:
    lane_counts = Counter(page.assigned_lane for page in pages)
    flag_counts = Counter(flag for page in pages for flag in page.quality_flags)
    payload = {
        "summary": {
            "total": len(pages),
            "needs_action": sum(1 for page in pages if page.action != "ok"),
            "lane_counts": dict(sorted(lane_counts.items())),
            "flag_counts": dict(sorted(flag_counts.items())),
        },
        "pages": [asdict(page) for page in pages],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def md_table(rows: Iterable[list[str]]) -> str:
    rows = list(rows)
    return "\n".join("| " + " | ".join(cell.replace("\n", "<br>") for cell in row) + " |" for row in rows)


def to_markdown(pages: list[ComparisonAudit], *, team_plan: bool = False) -> str:
    lane_groups: dict[str, list[ComparisonAudit]] = defaultdict(list)
    for page in pages:
        lane_groups[page.assigned_lane].append(page)

    flag_counts = Counter(flag for page in pages for flag in page.quality_flags)
    needs_action = [page for page in pages if page.action != "ok"]

    lines: list[str] = []
    lines.append("# Comparison Topic Audit")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total comparison topic pages: {len(pages)}")
    lines.append(f"- Needs action: {len(needs_action)}")
    if flag_counts:
        lines.append("- Top flags: " + ", ".join(f"{k}={v}" for k, v in flag_counts.most_common(10)))
    else:
        lines.append("- Top flags: none")
    lines.append("")

    if team_plan:
        lines.append("## 4-lane team assignment")
        lines.append("")
        lines.append("- Each lane edits only its assigned comparison topic pages.")
        lines.append("- Keep `raw/` source notes immutable; repair evidence by linking existing anchors, not inventing claims.")
        lines.append("- Final verifier should run this script with `--strict` and spot-check that explanation depth is real, not heading-only.")
        lines.append("")
        for lane, _, _ in LANE_RULES:
            lane_pages = sorted(lane_groups.get(lane, []), key=lambda page: page.title)
            lines.append(f"### {lane}")
            lines.append("")
            rows = [["File", "Rows", "Links", "Action", "Flags"]]
            rows.append(["---", "---", "---", "---", "---"])
            for page in lane_pages:
                flags = "; ".join(page.quality_flags[:4]) or "ok"
                rows.append([page.file, str(page.table_rows), str(page.link_count), page.action, flags])
            lines.append(md_table(rows))
            lines.append("")
    else:
        lines.append("## Pages needing action")
        lines.append("")
        if not needs_action:
            lines.append("_No comparison topic pages need action._")
            lines.append("")
        else:
            rows = [["File", "Lane", "Rows", "Links", "Action", "Flags"]]
            rows.append(["---", "---", "---", "---", "---", "---"])
            for page in needs_action:
                flags = "; ".join(page.quality_flags[:5]) or ", ".join(page.missing_sections[:5])
                rows.append([page.file, page.assigned_lane, str(page.table_rows), str(page.link_count), page.action, flags])
            lines.append(md_table(rows))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit comparison topic pages against the LLM wiki comparison-page standard."
    )
    parser.add_argument("--topic-dir", type=Path, default=TOPIC_DIR, help="Directory containing topic pages.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", type=Path, help="Write output to this path instead of stdout.")
    parser.add_argument("--team-plan", action="store_true", help="Include 4-lane comparison repair assignment tables.")
    parser.add_argument(
        "--min-page-chars",
        type=int,
        default=2500,
        help="Weak-page heuristic: minimum characters expected for a durable comparison page.",
    )
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any page needs action.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    topic_dir = args.topic_dir
    if not topic_dir.is_absolute():
        topic_dir = ROOT / topic_dir

    pages = audit_all(topic_dir, min_page_chars=args.min_page_chars)
    output = to_json(pages) if args.format == "json" else to_markdown(pages, team_plan=args.team_plan)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")

    if args.strict and any(page.action != "ok" for page in pages):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
