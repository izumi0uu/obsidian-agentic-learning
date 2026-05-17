#!/usr/bin/env python3
"""Audit Obsidian concept cards and generate 7-worker team assignments.

This script is intentionally read-only by default. It inspects
`agentic learning/wiki/concepts/*.md`, reports structural/depth gaps,
and groups files into writer/auditor/verifier lanes for the LLM wiki
concept-card standard.

Usage:
  python scripts/concept_card_audit.py
  python scripts/concept_card_audit.py --format markdown
  python scripts/concept_card_audit.py --format json --output reports/concept-card-audit.json
  python scripts/concept_card_audit.py --team-plan --format markdown
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CONCEPT_DIR = ROOT / "agentic learning" / "wiki" / "concepts"

REQUIRED_SECTIONS = [
    "## 一句话",
    "## 它解决什么问题",
    "## 它不是什么",
    "## 最小例子",
    "## 边界细节",
    "## 现代性状态",
    "## 证据锚点",
    "## 复习触发",
    "## 相关链接",
]
DEEP_SECTION = "## 概念详解"
RISK_SECTION_RE = re.compile(r"^## (常见误解|风险|常见误解 / 风险|常见误解和风险|常见误解 / 风险 / 边界细节)\b", re.M)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
HEADING_RE = re.compile(r"^## .+$", re.M)

MIN_DETAIL_CHARS = {
    "seed-lite": 0,
    "volatile": 650,
    "qualified": 700,
    "anchor": 900,
}

ANCHOR_NAMES = {
    "Agent.md",
    "Agent Loop.md",
    "Agent Framework.md",
    "Agent State.md",
    "Agent Workflow.md",
    "Agent Harness.md",
    "Evaluation.md",
    "Eval Harness.md",
    "LLM-as-Judge.md",
    "RAG.md",
    "RAG Evaluation.md",
    "Trace.md",
    "Observability.md",
    "Trajectory Evaluation.md",
    "Tool Calling.md",
    "Memory.md",
    "Planning.md",
    "ReAct.md",
    "Plan-and-Solve Prompting.md",
    "MCP.md",
    "Guardrails.md",
    "Prompt Injection.md",
}

VOLATILE_TOPICS = {"frontier", "protocol", "sdk", "security", "tools", "observability"}
CURRENT_PRACTICE_TOPICS = {
    "agent",
    "workflow",
    "evaluation",
    "rag",
    "memory",
    "framework",
    "tool-use",
    "infrastructure",
    "observability",
}
SEED_LITE_NAMES = {"AGENTS.md.md"}

GROUP_RULES: list[tuple[str, set[str], list[str]]] = [
    (
        "writer-1-agent-foundations",
        {"agent", "reasoning", "planning", "tool-use"},
        ["Agent", "Loop", "Planning", "Tool", "ReAct", "Observation", "Reasoning", "Prompt"],
    ),
    (
        "writer-2-framework-runtime",
        {"framework", "workflow", "memory", "infrastructure"},
        ["Framework", "Harness", "State", "Workflow", "Durable", "Memory", "Sandbox", "Gateway", "Hook"],
    ),
    (
        "writer-3-evaluation-observability",
        {"evaluation", "observability"},
        ["Evaluation", "Eval", "Trace", "Trajectory", "Judge", "Benchmark", "Observability", "Replay", "Success"],
    ),
    (
        "writer-4-rag-retrieval",
        {"rag", "retrieval"},
        ["RAG", "Retrieval", "Retriever", "Vector", "Embedding", "Chunking", "Reranking", "Search", "GraphRAG", "Neo4j"],
    ),
    (
        "writer-5-security-protocol-frontier",
        {"security", "protocol", "frontier", "tools"},
        ["MCP", "A2A", "ACP", "Guardrails", "Permission", "Injection", "Poisoning", "Exfiltration", "Registry", "Computer Use", "Browser"],
    ),
]


@dataclass
class CardAudit:
    file: str
    title: str
    topics: list[str]
    status: str
    freshness: str
    depth: str
    assigned_lane: str
    missing_sections: list[str]
    has_risk_section: bool
    has_detail: bool
    detail_chars: int
    has_evidence_type: bool
    has_boundary: bool
    has_source: bool
    has_evidence: bool
    outdated_frontmatter: list[str]
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
            if value == "":
                fm[key] = []
            elif value == "[]":
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
    idx = text.find(heading)
    if idx == -1:
        return ""
    rest = text[idx + len(heading) :]
    next_heading = re.search(r"\n## ", rest)
    if next_heading:
        return rest[: next_heading.start()].strip()
    return rest.strip()


def classify_depth(path: Path, topics: list[str], status: str, freshness: str) -> str:
    """Assign a repair depth without turning every card into an anchor.

    Anchor is reserved for map-level concepts and style exemplars. Volatile means
    the card needs freshness discipline because it describes a fast-moving API,
    protocol, product, security surface, or frontier ecosystem. Most cards should
    be qualified, not encyclopedic longform.
    """
    name = path.name
    topic_set = set(topics)
    if name in SEED_LITE_NAMES or topic_set <= {"obsidian", "workflow", "llm-wiki"}:
        return "seed-lite"
    if name in ANCHOR_NAMES:
        return "anchor"
    if freshness in {"volatile", "stale"}:
        return "volatile"
    if freshness == "watch" or topic_set & VOLATILE_TOPICS:
        return "volatile"
    return "qualified"


def assign_lane(path: Path, topics: list[str]) -> str:
    name = path.stem
    topic_set = set(topics)
    scores: dict[str, int] = {}
    for lane, lane_topics, keywords in GROUP_RULES:
        score = len(topic_set & lane_topics) * 3
        score += sum(1 for kw in keywords if kw.lower() in name.lower())
        scores[lane] = score
    lane, score = max(scores.items(), key=lambda kv: (kv[1], kv[0]))
    return lane if score > 0 else "writer-5-security-protocol-frontier"


def audit_card(path: Path) -> CardAudit:
    text = path.read_text()
    fm = parse_frontmatter(text)
    topics = list_value(fm, "topic")
    status = scalar_value(fm, "status")
    freshness = scalar_value(fm, "freshness")
    depth = classify_depth(path, topics, status, freshness)
    lane = assign_lane(path, topics)

    missing = [section for section in REQUIRED_SECTIONS if section not in text]
    has_risk = bool(RISK_SECTION_RE.search(text))
    has_detail = DEEP_SECTION in text
    detail_chars = len(section_body(text, DEEP_SECTION)) if has_detail else 0
    has_evidence_type = "Evidence type:" in text
    has_boundary = "Boundary:" in text
    has_source = bool(list_value(fm, "source"))
    has_evidence = bool(list_value(fm, "evidence"))

    outdated: list[str] = []
    if (depth in {"anchor", "qualified", "volatile"}) and not scalar_value(fm, "updated"):
        outdated.append("missing updated")
    if (freshness in {"watch", "volatile", "stale"} or depth == "volatile") and not scalar_value(fm, "last_checked"):
        outdated.append("missing last_checked")
    if (freshness in {"watch", "volatile", "stale"} or depth == "volatile") and not freshness:
        outdated.append("missing freshness")

    flags: list[str] = []
    if not has_source:
        flags.append("frontmatter source missing")
    if not has_evidence:
        flags.append("frontmatter evidence missing")
    if not has_risk:
        flags.append("risk/misunderstanding section missing")
    if depth in {"anchor", "qualified", "volatile"} and not has_detail:
        flags.append("detail section missing")
    min_detail = MIN_DETAIL_CHARS.get(depth, 700)
    if depth in {"anchor", "qualified", "volatile"} and has_detail and detail_chars < min_detail:
        flags.append(f"detail too short for depth (<{min_detail})")
    if depth in {"anchor", "qualified", "volatile"} and not (has_evidence_type and has_boundary):
        flags.append("evidence type/boundary missing")
    if depth in {"anchor", "volatile"} and "## 现代性状态" not in text:
        flags.append("modernity status missing")
    if depth != "seed-lite" and "## 复习触发" not in text:
        flags.append("review trigger missing")

    if not flags and not missing:
        action = "ok"
    elif depth == "seed-lite":
        action = "mark gaps or upgrade only if concept is worth keeping"
    elif "detail section missing" in flags or "detail too short for depth" in flags:
        action = "add/strengthen concept detail with evidence boundary"
    else:
        action = "repair sections/evidence without broad rewrite"

    return CardAudit(
        file=str(path.relative_to(ROOT)),
        title=path.stem,
        topics=topics,
        status=status,
        freshness=freshness,
        depth=depth,
        assigned_lane=lane,
        missing_sections=missing,
        has_risk_section=has_risk,
        has_detail=has_detail,
        detail_chars=detail_chars,
        has_evidence_type=has_evidence_type,
        has_boundary=has_boundary,
        has_source=has_source,
        has_evidence=has_evidence,
        outdated_frontmatter=outdated,
        quality_flags=flags,
        action=action,
    )


def audit_all() -> list[CardAudit]:
    return [audit_card(path) for path in sorted(CONCEPT_DIR.glob("*.md"))]


def to_json(cards: list[CardAudit]) -> str:
    counts = Counter(card.depth for card in cards)
    lane_counts = Counter(card.assigned_lane for card in cards)
    flag_counts = Counter(flag for card in cards for flag in card.quality_flags)
    payload = {
        "summary": {
            "total": len(cards),
            "depth_counts": dict(sorted(counts.items())),
            "lane_counts": dict(sorted(lane_counts.items())),
            "flag_counts": dict(sorted(flag_counts.items())),
            "needs_action": sum(1 for c in cards if c.action != "ok"),
        },
        "cards": [asdict(card) for card in cards],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def md_table(rows: Iterable[list[str]]) -> str:
    rows = list(rows)
    return "\n".join("| " + " | ".join(cell.replace("\n", "<br>") for cell in row) + " |" for row in rows)


def to_markdown(cards: list[CardAudit], *, team_plan: bool = False) -> str:
    counts = Counter(card.depth for card in cards)
    lane_groups: dict[str, list[CardAudit]] = defaultdict(list)
    for card in cards:
        lane_groups[card.assigned_lane].append(card)
    flag_counts = Counter(flag for card in cards for flag in card.quality_flags)

    lines: list[str] = []
    lines.append("# Concept Card Audit")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total concept cards: {len(cards)}")
    lines.append(f"- Needs action: {sum(1 for c in cards if c.action != 'ok')}")
    lines.append("- Depth counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if flag_counts:
        lines.append("- Top flags: " + ", ".join(f"{k}={v}" for k, v in flag_counts.most_common(10)))
    lines.append("")

    if team_plan:
        lines.append("## 7-process team assignment")
        lines.append("")
        lines.append("- writer-1..5 edit only their assigned concept files.")
        lines.append("- worker-6 is evidence auditor: read-only by default; may only report missing/weak evidence.")
        lines.append("- worker-7 is verifier/lint: read-only by default; checks quality after writers finish.")
        lines.append("")
        for lane in [rule[0] for rule in GROUP_RULES]:
            lane_cards = sorted(lane_groups.get(lane, []), key=lambda c: (c.depth, c.title))
            lines.append(f"### {lane}")
            lines.append("")
            rows = [["File", "Depth", "Action", "Flags"]]
            rows.append(["---", "---", "---", "---"])
            for card in lane_cards:
                flags = "; ".join(card.quality_flags[:4]) or "ok"
                rows.append([card.file, card.depth, card.action, flags])
            lines.append(md_table(rows))
            lines.append("")
        lines.append("### worker-6-evidence-auditor")
        lines.append("")
        lines.append("Read all writer diffs and report cards where source/evidence anchors do not support the new detail section, or where engineering synthesis is not labeled as such. Do not rewrite body text unless leader explicitly asks.")
        lines.append("")
        lines.append("### worker-7-final-verifier")
        lines.append("")
        lines.append("Run the audit script, inspect changed cards, and fail cards that only have headings without real conceptual explanation. Do not accept section-completeness as quality-completeness.")
        lines.append("")
    else:
        lines.append("## Cards needing action")
        lines.append("")
        rows = [["File", "Lane", "Depth", "Detail", "Action", "Flags"]]
        rows.append(["---", "---", "---", "---", "---", "---"])
        for card in cards:
            if card.action == "ok":
                continue
            flags = "; ".join(card.quality_flags[:5]) or ", ".join(card.missing_sections[:5])
            rows.append([card.file, card.assigned_lane, card.depth, str(card.detail_chars), card.action, flags])
        lines.append(md_table(rows))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit concept cards against the LLM wiki concept-card standard.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", type=Path, help="Write output to this path instead of stdout.")
    parser.add_argument("--team-plan", action="store_true", help="Include 7-worker assignment tables.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cards = audit_all()
    output = to_json(cards) if args.format == "json" else to_markdown(cards, team_plan=args.team_plan)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
