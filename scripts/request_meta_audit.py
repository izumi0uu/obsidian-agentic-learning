#!/usr/bin/env python3
"""Audit durable vault pages for leaked request/session metadata.

This check is intentionally narrower than a privacy scanner. It looks for
conversation wrappers, Codex/OMX hook text, and request-side intake wording that
should stay in the current reply or local runtime logs instead of becoming wiki
knowledge.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SCAN_TARGETS = [
    Path("agentic learning/wiki"),
    Path("agentic learning/raw"),
    Path("agentic learning/maps"),
    Path("agentic learning/reviews"),
    Path("agentic learning/log.md"),
]

IGNORED_PARTS = {
    ".git",
    ".omx",
    ".codex",
    ".obsidian",
    "__pycache__",
    "node_modules",
}

RULE_EXPLANATION_FILES = {
    Path("agentic learning/maps/LLM Wiki 工作流.md"),
}


@dataclass(frozen=True)
class PatternRule:
    code: str
    pattern: str
    severity: str
    category: str
    note: str
    hints: tuple[str, ...]
    allow_rule_files: bool = False


@dataclass(frozen=True)
class Hit:
    path: str
    line: int
    column: int
    code: str
    severity: str
    category: str
    note: str
    match: str
    excerpt: str


RULES = [
    PatternRule(
        "codex_ide_context",
        r"(?:^|\s)#?\s*Context from my IDE setup:",
        "error",
        "conversation_transcript",
        "Codex IDE wrapper text should not be persisted in durable notes.",
        ("context from my ide setup",),
    ),
    PatternRule(
        "codex_request_header",
        r"(?:^|\s)##\s*My request for Codex:",
        "error",
        "conversation_transcript",
        "Codex prompt wrapper should remain in the active chat only.",
        ("my request for codex",),
    ),
    PatternRule(
        "codex_open_tabs",
        r"(?:^|\s)##\s*Open tabs:",
        "error",
        "conversation_transcript",
        "IDE open-tab context is runtime metadata.",
        ("open tabs",),
    ),
    PatternRule(
        "codex_active_file",
        r"(?:^|\s)##\s*Active file:",
        "error",
        "conversation_transcript",
        "IDE active-file context is runtime metadata.",
        ("active file",),
    ),
    PatternRule(
        "handoff_summary",
        r"Another language model started to solve this problem",
        "error",
        "conversation_transcript",
        "Model handoff summaries must not become wiki content.",
        ("another language model started to solve this problem",),
    ),
    PatternRule(
        "hook_prompt_xml",
        r"<hook_prompt\b|hook_run_id=",
        "error",
        "runtime_hook",
        "Hook payloads belong to local runtime state, not vault pages.",
        ("<hook_prompt", "hook_run_id="),
    ),
    PatternRule(
        "autoresearch_goal_hook",
        r"OMX autoresearch-goal requires get_goal snapshot reconciliation",
        "error",
        "runtime_hook",
        "Autoresearch stop-hook obligations must stay in .omx/runtime handling.",
        ("omx autoresearch-goal requires get_goal snapshot reconciliation",),
    ),
    PatternRule(
        "goal_snapshot_placeholder",
        r"<get_goal JSON or path>|call get_goal and pass --codex-goal-json",
        "error",
        "runtime_hook",
        "Goal reconciliation command text is runtime metadata.",
        ("<get_goal json or path>", "call get_goal and pass --codex-goal-json"),
    ),
    PatternRule(
        "stop_hook_id",
        r"\bstop:\d+:[^\s>]+",
        "error",
        "runtime_hook",
        "Stop-hook identifiers should not be written into durable pages.",
        ("stop:",),
    ),
    PatternRule(
        "write_this_back_instruction",
        r"写回到\s*(?:\[\[|Tool|Agent|Evaluation|RAG|wiki|topic|concept)",
        "error",
        "request_meta",
        "Writeback routing instructions are operation context, not knowledge content.",
        ("写回到",),
    ),
    PatternRule(
        "worth_recording_prompt",
        r"(?:这个知识点)?值得录入(?:吗|么|\?)?",
        "error",
        "request_meta",
        "Recording-worthiness questions should be neutralized before persistence.",
        ("值得录入",),
    ),
    PatternRule(
        "help_me_record",
        r"帮我(?:录入|写入|写回|沉淀)",
        "error",
        "request_meta",
        "User execution requests should not appear as durable knowledge.",
        ("帮我录入", "帮我写入", "帮我写回", "帮我沉淀"),
    ),
    PatternRule(
        "intake_batch_provenance",
        r"本页来自\s*2026-|批次索引见|前沿判断见|先录到哪|为什么先收|为什么先读",
        "error",
        "request_meta",
        "Intake/batch/provenance scaffolding should be removed or neutralized.",
        ("本页来自", "批次索引见", "前沿判断见", "先录到哪", "为什么先收", "为什么先读"),
        allow_rule_files=True,
    ),
    PatternRule(
        "agent_process_meta",
        r"本轮\s*agent(?:\s*执行过程)?|本轮判断|这个问题可保留",
        "error",
        "request_meta",
        "Agent process narration should not be promoted into wiki knowledge.",
        ("本轮 agent", "本轮判断", "这个问题可保留"),
        allow_rule_files=True,
    ),
    PatternRule(
        "user_supplied_project_meta",
        r"用户提供的\s+Hermes",
        "error",
        "request_meta",
        "Project/intake provenance should be neutralized unless it is the source topic.",
        ("用户提供的 hermes",),
    ),
]

COMPILED_RULES = [(rule, re.compile(rule.pattern, flags=re.IGNORECASE)) for rule in RULES]


def rel(path: Path) -> Path:
    try:
        return path.resolve().relative_to(ROOT)
    except ValueError:
        return path


def iter_markdown_files(targets: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for target in targets:
        path = target if target.is_absolute() else ROOT / target
        if not path.exists():
            continue
        if path.is_file():
            if path.suffix.lower() in {".md", ".markdown"}:
                files.append(path)
            continue
        for candidate in path.rglob("*"):
            if any(part in IGNORED_PARTS for part in candidate.parts):
                continue
            if candidate.is_file() and candidate.suffix.lower() in {".md", ".markdown"}:
                files.append(candidate)
    return sorted(set(files), key=lambda p: str(rel(p)))


def should_skip(rule: PatternRule, path: Path) -> bool:
    relative = rel(path)
    if rule.allow_rule_files and relative in RULE_EXPLANATION_FILES:
        return True
    return False


def excerpt_for(line: str, start: int, end: int, radius: int = 80) -> str:
    left = max(0, start - radius)
    right = min(len(line), end + radius)
    prefix = "..." if left > 0 else ""
    suffix = "..." if right < len(line) else ""
    return prefix + line[left:right].strip() + suffix


def scan_file(path: Path) -> list[Hit]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    text_lower = text.lower()
    active_rules = [
        (rule, regex)
        for rule, regex in COMPILED_RULES
        if any(hint in text_lower for hint in rule.hints)
    ]
    if not active_rules:
        return []

    hits: list[Hit] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        line_lower = line.lower()
        for rule, regex in active_rules:
            if should_skip(rule, path):
                continue
            if not any(hint in line_lower for hint in rule.hints):
                continue
            for match in regex.finditer(line):
                hits.append(
                    Hit(
                        path=str(rel(path)),
                        line=line_number,
                        column=match.start() + 1,
                        code=rule.code,
                        severity=rule.severity,
                        category=rule.category,
                        note=rule.note,
                        match=match.group(0),
                        excerpt=excerpt_for(line, match.start(), match.end()),
                    )
                )
    return hits


def audit(paths: list[Path]) -> dict[str, object]:
    files = iter_markdown_files(paths)
    hits = [hit for path in files for hit in scan_file(path)]
    errors = [hit for hit in hits if hit.severity == "error"]
    return {
        "ok": not errors,
        "scanned_files": len(files),
        "error_count": len(errors),
        "hit_count": len(hits),
        "hits": [asdict(hit) for hit in hits],
    }


def render_markdown(result: dict[str, object]) -> str:
    lines = [
        "# Request Meta Audit",
        "",
        f"- Status: {'PASS' if result['ok'] else 'FAIL'}",
        f"- Scanned files: {result['scanned_files']}",
        f"- Error count: {result['error_count']}",
        f"- Hit count: {result['hit_count']}",
        "",
    ]
    hits = result["hits"]
    if not hits:
        lines.append("_No request/session metadata hits._")
        return "\n".join(lines) + "\n"

    def table_cell(value: object) -> str:
        return str(value).replace("|", "\\|")

    lines.extend(["| File | Line | Code | Match |", "|---|---:|---|---|"])
    for hit in hits:  # type: ignore[assignment]
        lines.append(
            f"| `{table_cell(hit['path'])}` | {hit['line']} | `{table_cell(hit['code'])}` | {table_cell(hit['excerpt'])} |"
        )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit vault notes for request/session metadata leakage.")
    parser.add_argument("paths", nargs="*", help="Optional files or directories to scan.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--output", type=Path, help="Optional report output path.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    paths = [Path(p) for p in args.paths] if args.paths else DEFAULT_SCAN_TARGETS
    result = audit(paths)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.format == "markdown":
        output = render_markdown(result)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
