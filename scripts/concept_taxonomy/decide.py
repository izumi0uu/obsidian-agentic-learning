#!/usr/bin/env python3
"""Create a reviewed decision ledger for temporary concept-card relation candidates.

The ledger is intentionally conservative: it does not edit concept cards. It turns
candidate edges from ``build.py`` into explicit decisions that can be audited before
any writeback.
"""
from __future__ import annotations

import paths
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from boundary_policy import NON_TAXONOMY_BOUNDARIES, policy_rows

ROOT = paths.ROOT
CONCEPT_DIR = paths.CONCEPT_DIR
OUT_DIR = paths.OUT_DIR
MAP_JSON = OUT_DIR / "concept-relations-temp.json"
LEDGER_JSON = OUT_DIR / "relation-decision-ledger.json"
LEDGER_MD = OUT_DIR / "relation-decision-ledger.md"
PRE_MAP_JSON = OUT_DIR / "concept-relations-pre-writeback.json"
PRE_MAP_MD = OUT_DIR / "concept-relations-pre-writeback.md"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")

# Accepted strict taxonomy candidates. These are not simply topic neighbors: the
# child card's one-line/body describes a member/subtype/instance of the parent
# family, and the parent is already a stable concept card.
ACCEPT_TAXONOMY: dict[tuple[str, str], str] = {
    ("AgentScope", "Agent Framework"): "AgentScope is an engineering platform/framework in the Agent Framework family.",
    ("Agentic RAG", "RAG"): "Agentic RAG is a RAG mode where an agent controls retrieval decisions.",
    ("Agentic Retrieval", "Retriever"): "Agentic Retrieval is a retrieval-layer pattern; Retriever is the broader retrieval component family.",
    ("Audit Log", "Observability"): "Audit logs are durable observability/compliance records for agent actions.",
    ("AutoGen", "Agent Framework"): "AutoGen is a Microsoft multi-agent orchestration framework.",
    ("CAMEL", "Agent Framework"): "CAMEL-AI is described as a modular multi-agent framework.",
    ("Corrective RAG", "RAG"): "Corrective RAG is a RAG mode that evaluates and repairs retrieval evidence.",
    ("Crew Orchestration", "Agent Workflow"): "Crew orchestration is a workflow/coordination pattern for role-based multi-agent work.",
    ("Episodic Memory", "Memory"): "Episodic memory is a subtype of memory for past events and trajectories.",
    ("GraphRAG", "RAG"): "GraphRAG is a graph-augmented RAG method family.",
    ("LangChain DeepAgents", "Agent Framework"): "LangChain DeepAgents is a LangGraph/LangChain framework harness.",
    ("LangGraph", "Agent Framework"): "LangGraph is a low-level agent orchestration framework/runtime in the LangChain ecosystem.",
    ("Long-term Memory", "Memory"): "Long-term memory is the broader cross-session memory capability.",
    ("Microsoft Agent Framework", "Agent Framework"): "Microsoft Agent Framework is a named agent SDK/framework route.",
    ("Non-Parametric Memory", "Memory"): "Non-parametric memory is external retrievable memory outside model weights.",
    ("Parametric Memory", "Memory"): "Parametric memory is memory encoded inside model parameters.",
    ("RAG Evaluation", "Evaluation"): "RAG Evaluation is a subtype of evaluation focused on retrieval/context/citation/answer quality.",
    ("Self-RAG", "RAG"): "Self-RAG is a RAG method family with adaptive retrieval/generation/critique.",
    ("Semantic Memory", "Memory"): "Semantic memory is a subtype of memory for stable facts/preferences/concepts.",
    ("Tool Calling", "Tool Use"): "Tool Calling is a structured form of tool use.",
    ("Trajectory Evaluation", "Evaluation"): "Trajectory Evaluation is evaluation of an agent's action process rather than only final output.",
    # Lower-confidence title-only candidates accepted by semantic boundary, but
    # kept outside the default first small writeback batch unless the limit is raised.
    ("Computer Use", "Tool Use"): "Computer Use is a tool-use mode where the agent operates browser/desktop/terminal surfaces.",
    ("Data-first Agent Framework", "Agent Framework"): "Data-first Agent Framework is explicitly a framework route centered on data/RAG primitives.",
    ("Graph Construction Evaluation", "Evaluation"): "Graph Construction Evaluation is a subtype of evaluation for graph/RAG construction quality.",
    ("Multi-agent Orchestration", "Agent Workflow"): "Multi-agent orchestration is a workflow/coordination pattern for multiple agents.",
}

REJECT_TAXONOMY: dict[tuple[str, str], str] = {
    ("Top-K", "Retriever"): "Top-K is a ranking/selection rule used by retrievers and decoders; it is not itself a retriever subtype.",
    ("Reasoning Trace", "Observability"): "Reasoning Trace is a kind of trace/trajectory artifact; Observability is too broad as a direct parent here.",
    ("Tool Permissioning", "Tool Use"): "Tool Permissioning constrains and governs tools; it is not a tool-use subtype.",
    ("Tool Poisoning", "Tool Use"): "Tool Poisoning is a threat/failure mode against tools; it is not a tool-use subtype.",
    ("Tool Registry", "Tool Use"): "Tool Registry is infrastructure/catalog metadata for tools; it is not a tool-use subtype.",
    ("Durable Execution", "Agent Workflow"): "Durable Execution is a runtime capability used by workflows, not a workflow subtype.",
    ("Handoff", "Agent Workflow"): "Handoff is a transfer mechanism inside workflows, not a workflow subtype.",
    ("Human-in-the-loop", "Agent Workflow"): "Human-in-the-loop is an intervention/approval pattern inside workflows, not a workflow subtype.",
    ("OpenTelemetry GenAI", "Observability"): "OpenTelemetry GenAI is a semantic-convention/standardization layer that supports observability; it is not itself an observability capability subtype.",
    ("RAGGraph", "RAG"): "RAGGraph is an unstable ambiguity/reminder card for workflow graph vs GraphRAG confusion; it remains related to RAG but is not a stable RAG subtype.",
    ("State Graph Runtime", "Agent Workflow"): "State Graph Runtime executes and persists workflows; runtime infrastructure is adjacent to Agent Workflow, not a workflow subtype.",
}

DEFER_TAXONOMY: dict[tuple[str, str], str] = {
}


def resolution_status(decision: dict[str, Any]) -> str:
    """Classify whether a ledger row is still actionable after review."""
    if decision.get("writeback_action") == "add_up":
        return "open_writeback"
    if decision.get("decision") in {"needs_review", "defer_taxonomy"}:
        return "open_review"
    if decision.get("writeback_action") == "already_present":
        return "terminal_already_present"
    return "terminal_non_writeback"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, "", text
    raw = m.group(1)
    return yaml.safe_load(raw) or {}, raw, text[m.end():]


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def clean_link(value: Any) -> str | None:
    if value is None or isinstance(value, dict):
        return None
    s = str(value).strip().strip('"').strip("'")
    m = WIKILINK_RE.search(s)
    if m:
        s = m.group(1)
    s = s.split("|")[0].split("#")[0].strip()
    if "/" in s:
        s = Path(s).stem
    return s or None


def section_text(body: str, heading: str) -> str:
    marker = f"## {heading}"
    idx = body.find(marker)
    if idx == -1:
        return ""
    rest = body[idx + len(marker):]
    nxt = re.search(r"\n##\s+", rest)
    return (rest[:nxt.start()] if nxt else rest).strip()


def load_cards() -> dict[str, dict[str, Any]]:
    cards: dict[str, dict[str, Any]] = {}
    for path in sorted(CONCEPT_DIR.glob("*.md")):
        text = read_text(path)
        fm, _raw, body = split_frontmatter(text)
        if fm.get("type") != "concept":
            continue
        cards[path.stem] = {
            "file": str(path.relative_to(ROOT)),
            "frontmatter": fm,
            "one_line": section_text(body, "一句话").replace("\n", " ").strip(),
            "not_what": section_text(body, "它不是什么").replace("\n", " ").strip(),
            "boundary": section_text(body, "边界细节").replace("\n", " ").strip(),
        }
    return cards


def existing_up(card: dict[str, Any]) -> list[str]:
    return [x for x in (clean_link(v) for v in as_list(card["frontmatter"].get("up"))) if x]


def existing_related(card: dict[str, Any]) -> list[str]:
    return [x for x in (clean_link(v) for v in as_list(card["frontmatter"].get("related"))) if x]


def decide_candidate(candidate: dict[str, Any], cards: dict[str, dict[str, Any]], accepted_pairs: set[tuple[str, str]]) -> dict[str, Any]:
    pair = (candidate["source"], candidate["target"])
    source_card = cards.get(candidate["source"], {})
    one_line = source_card.get("one_line", "")
    source_up = existing_up(source_card) if source_card else []
    source_related = existing_related(source_card) if source_card else []
    result: dict[str, Any] = {
        **candidate,
        "source_file": source_card.get("file", ""),
        "source_one_line": one_line,
        "existing_up": source_up,
        "decision": "needs_review",
        "writeback_action": "none",
        "proposed_field": None,
        "judge_confidence": "low",
        "llm_judgment_basis": "card frontmatter + one-line/boundary snippets + relation-field rules; not source-level re-reading",
        "decision_rationale": "Not classified by the conservative review rules.",
        "guardrail": "Do not write to concept cards without an explicit accepted decision and dry-run.",
    }

    if pair in NON_TAXONOMY_BOUNDARIES:
        boundary = NON_TAXONOMY_BOUNDARIES[pair]
        is_taxonomy_candidate = candidate["candidate_type"].endswith("taxonomy_candidate")
        result.update({
            "decision": "reject_taxonomy" if is_taxonomy_candidate else "adjacency_only",
            "writeback_action": "none",
            "proposed_field": "relations or related, never up",
            "judge_confidence": "high",
            "boundary_guardrail_applied": True,
            "boundary_kind": boundary["kind"],
            "safe_relation": boundary["safe_relation"],
            "decision_rationale": boundary["rationale"],
            "guardrail": "Do not write this pair to up. Keep representation/algorithm/route/strategy boundaries separate.",
        })
        return result

    if candidate["candidate_type"] == "topic_family_review":
        if pair in accepted_pairs:
            result.update({
                "decision": "duplicate_signal",
                "judge_confidence": "high",
                "decision_rationale": "This low-confidence topic-family signal duplicates an accepted strict taxonomy candidate for the same source/target.",
                "guardrail": "Use the accepted taxonomy row, not this topic-family signal, for any writeback.",
            })
        else:
            result.update({
                "decision": "adjacency_only",
                "judge_confidence": "medium",
                "proposed_field": "related/body context only",
                "decision_rationale": "Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge.",
                "guardrail": "Never bulk-write topic_family_review into up.",
            })
        return result

    if pair in ACCEPT_TAXONOMY:
        if source_up and candidate["target"] not in source_up:
            result.update({
                "decision": "defer_taxonomy",
                "judge_confidence": "medium",
                "decision_rationale": f"Semantic parent is plausible, but the card already has up={source_up}; avoid creating multi-parent taxonomy without separate review.",
                "guardrail": "Review multi-parent taxonomy manually before writeback.",
            })
        else:
            result.update({
                "decision": "accept_taxonomy",
                "writeback_action": "add_up" if candidate["target"] not in source_up else "already_present",
                "proposed_field": "up",
                "judge_confidence": "high" if "frontmatter.related" in candidate.get("support", []) else "medium",
                "decision_rationale": ACCEPT_TAXONOMY[pair],
                "guardrail": "Write only child up; do not add down/children or Breadcrumbs mirror fields.",
            })
        return result

    if pair in REJECT_TAXONOMY:
        result.update({
            "decision": "reject_taxonomy",
            "judge_confidence": "high",
            "proposed_field": "related or relations, not up",
            "decision_rationale": REJECT_TAXONOMY[pair],
            "guardrail": "Do not write this candidate to up; preserve as adjacency or explain with typed relation only if needed.",
        })
        return result

    if pair in DEFER_TAXONOMY:
        result.update({
            "decision": "defer_taxonomy",
            "judge_confidence": "high",
            "decision_rationale": DEFER_TAXONOMY[pair],
            "guardrail": "Stabilize the concept boundary before adding a parent.",
        })
        return result

    # Fallback for unlisted taxonomy candidates: keep them reviewable but do not
    # write. This prevents title heuristics from silently hardening into taxonomy.
    if candidate["candidate_type"].endswith("taxonomy_candidate"):
        result.update({
            "decision": "defer_taxonomy",
            "judge_confidence": "medium" if candidate.get("confidence") == "medium" else "low",
            "decision_rationale": "Taxonomy direction is plausible but not accepted by the conservative first-pass ledger.",
            "guardrail": "Require source-level or body-boundary review before writeback.",
        })
    return result


def markdown_table(rows: list[dict[str, Any]]) -> list[str]:
    out = ["| Source | Target | Candidate type | Decision | Writeback | Judge confidence | Rationale |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        rationale = str(r["decision_rationale"]).replace("|", "/")
        out.append(
            f"| [[{r['source']}]] | [[{r['target']}]] | {r['candidate_type']} | {r['decision']} | {r['writeback_action']} `{r.get('proposed_field') or ''}` | {r['judge_confidence']} | {rationale} |"
        )
    return out


def main() -> None:
    if not MAP_JSON.exists():
        raise SystemExit(f"missing {MAP_JSON}; run build.py first")
    data = json.loads(MAP_JSON.read_text(encoding="utf-8"))
    # Preserve the exact candidate source used by this ledger. A later apply stage
    # may regenerate concept-relations-temp.* from the changed cards, so the
    # ledger must remain tied to the pre-writeback candidate snapshot.
    PRE_MAP_JSON.write_text(MAP_JSON.read_text(encoding="utf-8"), encoding="utf-8")
    if (OUT_DIR / "concept-relations-temp.md").exists():
        PRE_MAP_MD.write_text((OUT_DIR / "concept-relations-temp.md").read_text(encoding="utf-8"), encoding="utf-8")
    cards = load_cards()
    accepted_pairs = {pair for pair in ACCEPT_TAXONOMY if pair[0] in cards and pair[1] in cards}
    decisions = [decide_candidate(c, cards, accepted_pairs) for c in data.get("candidate_edges", [])]
    for decision in decisions:
        decision["resolution_status"] = resolution_status(decision)
    counts = Counter(d["decision"] for d in decisions)
    writebacks = [d for d in decisions if d["writeback_action"] == "add_up"]
    open_review = [d for d in decisions if d["resolution_status"] == "open_review"]
    open_writeback = [d for d in decisions if d["resolution_status"] == "open_writeback"]
    terminal_non_writeback = [d for d in decisions if d["resolution_status"] == "terminal_non_writeback"]
    summary = {
        "candidate_edges": len(decisions),
        "decision_counts": dict(counts),
        "writeback_candidates": len(writebacks),
        "open_writeback_items": len(open_writeback),
        "open_review_items": len(open_review),
        "relation_tail_open_items": len(open_review) + len(open_writeback),
        "relation_tail_status": "closed" if not open_review and not open_writeback else "open",
        "terminal_non_writeback_decisions": len(terminal_non_writeback),
        "already_applied_or_present_taxonomy": sum(1 for d in decisions if d["decision"] == "accept_taxonomy" and d.get("writeback_action") == "already_present"),
        "remaining_writeback_candidates": len(writebacks),
        "accepted_taxonomy": counts.get("accept_taxonomy", 0),
        "rejected_taxonomy": counts.get("reject_taxonomy", 0),
        "deferred_taxonomy": counts.get("defer_taxonomy", 0),
        "adjacency_only": counts.get("adjacency_only", 0),
        "duplicate_signals": counts.get("duplicate_signal", 0),
        "non_taxonomy_boundary_guardrails": sum(1 for d in decisions if d.get("boundary_guardrail_applied")),
        "write_policy": "Only decisions with writeback_action=add_up may be applied, and only through dry-run/apply small batches.",
    }
    payload = {
        "schema_version": 1,
        "artifact_type": "concept_relation_decision_ledger",
        "generated_at": subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip(),
        "input_map": str(PRE_MAP_JSON.relative_to(ROOT)),
        "current_map_at_decision_time": str(MAP_JSON.relative_to(ROOT)),
        "summary": summary,
        "non_taxonomy_boundary_policy": policy_rows(),
        "decisions": decisions,
    }
    LEDGER_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md: list[str] = []
    md.append("# Concept Relation Decision Ledger")
    md.append("")
    md.append(f"Generated: `{payload['generated_at']}`")
    md.append("")
    md.append("> 逐条判定台账：把临时图候选边分成 accepted taxonomy、rejected taxonomy、adjacency only、duplicate signal 和 deferred。只有 `writeback_action=add_up` 的行可以进入后续写回；`already_present` 表示本轮小批量已落地或卡片已有该 `up`；`topic_family_review` 永远不能直接写入 `up`。")
    md.append("")
    md.append("## Summary")
    md.append("")
    for k, v in summary.items():
        md.append(f"- {k}: {v}")
    md.append("")
    md.append("## Tail closure summary")
    md.append("")
    md.append("- `open_writeback_items`: accepted taxonomy rows still needing a limited apply.")
    md.append("- `open_review_items`: `needs_review` or `defer_taxonomy` rows still lacking a terminal decision.")
    md.append("- `terminal_non_writeback_decisions`: reviewed rows that are deliberately **not** written to `up` (`reject_taxonomy`, `adjacency_only`, or `duplicate_signal`). These are closed decisions, not backlog.")
    md.append("")
    if open_review or open_writeback:
        md.append("| Source | Target | Resolution status | Decision | Writeback | Rationale |")
        md.append("|---|---|---|---|---|---|")
        for d in open_review + open_writeback:
            rationale = str(d["decision_rationale"]).replace("|", "/")
            md.append(f"| [[{d['source']}]] | [[{d['target']}]] | {d['resolution_status']} | {d['decision']} | {d['writeback_action']} | {rationale} |")
    else:
        md.append("- relation tail status: **closed**")
        md.append("- open rows: none")
    md.append("")
    md.append("## Accepted taxonomy writeback candidates")
    md.append("")
    md.extend(markdown_table([d for d in decisions if d["decision"] == "accept_taxonomy"]))
    md.append("")
    md.append("## Rejected or deferred taxonomy candidates")
    md.append("")
    md.extend(markdown_table([d for d in decisions if d["decision"] in {"reject_taxonomy", "defer_taxonomy"}]))
    md.append("")
    md.append("## Topic-family / adjacency signals")
    md.append("")
    md.extend(markdown_table([d for d in decisions if d["candidate_type"] == "topic_family_review"]))
    md.append("")
    boundary_rows = [d for d in decisions if d.get("boundary_guardrail_applied")]
    md.append("## Non-taxonomy boundary guardrails")
    md.append("")
    if boundary_rows:
        md.append("| Source | Target | Boundary kind | Safe relation | Decision | Rationale |")
        md.append("|---|---|---|---|---|---|")
        for d in boundary_rows:
            rationale = str(d["decision_rationale"]).replace("|", "/")
            md.append(
                f"| [[{d['source']}]] | [[{d['target']}]] | {d.get('boundary_kind','')} | {d.get('safe_relation','')} | {d['decision']} | {rationale} |"
            )
    else:
        md.append("- none")
    md.append("")
    md.append("## Non-taxonomy boundary policy catalog")
    md.append("")
    md.append("> 这些 pair 即使当前没有出现在 candidate_edges，也属于 forbidden-as-up 防线；若未来启发式生成它们，必须落到 `relations` / `related` / reject，而不是 `up`。")
    md.append("")
    md.append("| Source | Target | Boundary kind | Safe relation | Rationale |")
    md.append("|---|---|---|---|---|")
    for p in payload["non_taxonomy_boundary_policy"]:
        rationale = str(p["rationale"]).replace("|", "/")
        md.append(f"| [[{p['source']}]] | [[{p['target']}]] | {p['boundary_kind']} | {p['safe_relation']} | {rationale} |")
    md.append("")
    md.append("## Writeback gate")
    md.append("")
    md.append("1. Run `python3 scripts/concept_taxonomy/writeback.py --dry-run` first.")
    md.append("2. Apply only a small batch with `--apply --limit N`; the default verifier rejects topic-family writes.")
    md.append("3. After applying, run `python3 scripts/concept_taxonomy/validate.py` and `git diff --check`.")
    md.append("4. Breadcrumbs / Abstract Folder validation is structural: top-level `up` YAML only; no `down`, no `children`, no Juggl mirror fields.")
    md.append("")
    LEDGER_MD.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({"ok": True, "ledger": str(LEDGER_JSON.relative_to(ROOT)), "markdown": str(LEDGER_MD.relative_to(ROOT)), "summary": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
