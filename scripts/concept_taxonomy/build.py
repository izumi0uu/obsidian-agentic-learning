#!/usr/bin/env python3
"""Build a temporary concept-card relationship map for the Obsidian vault.

This writes project report artifacts by default. It does not edit concept cards.
"""
from __future__ import annotations

import paths
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import yaml

ROOT = paths.ROOT
CONCEPT_DIR = paths.CONCEPT_DIR
OUT_DIR = paths.OUT_DIR
JSON_OUT = OUT_DIR / "concept-relations-temp.json"
MD_OUT = OUT_DIR / "concept-relations-temp.md"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
H2_RE = re.compile(r"^##\s+(.+)$", re.M)

TOPIC_FAMILY_RULES = [
    ({"evaluation"}, "Evaluation", "topic family: evaluation"),
    ({"observability"}, "Observability", "topic family: observability"),
    ({"memory"}, "Memory", "topic family: memory"),
    ({"framework"}, "Agent Framework", "topic family: framework"),
    ({"workflow"}, "Agent Workflow", "topic family: workflow"),
    ({"rag"}, "RAG", "topic family: rag"),
    ({"retrieval", "search"}, "Retriever", "topic family: retrieval/search"),
    ({"tool-use", "tools"}, "Tool Use", "topic family: tool-use/tools"),
    ({"planning"}, "Planning", "topic family: planning"),
]

TITLE_PARENT_RULES = [
    (re.compile(r".+\bBenchmark$"), "Benchmark", "title suffix Benchmark"),
    (re.compile(r".+\bEvaluation$"), "Evaluation", "title suffix Evaluation"),
    (re.compile(r".+\bMemory$"), "Memory", "title suffix Memory"),
    (re.compile(r".+\bRAG$|^GraphRAG$|^RAGGraph$"), "RAG", "RAG method/title family"),
    (re.compile(r".+\bRetrieval$|.+\bSearch$|^Top-K$"), "Retriever", "retrieval/search title family"),
    (re.compile(r".+\bFramework$|^(AutoGen|CAMEL|LangGraph|AgentScope|LangChain DeepAgents)$"), "Agent Framework", "framework title or known framework"),
    (re.compile(r".+\bWorkflow$|^State Graph Runtime$|^Crew Orchestration$|^Multi-agent Orchestration$|^Durable Execution$|^Handoff$|^Human-in-the-loop$"), "Agent Workflow", "workflow/runtime title family"),
    (re.compile(r".+\bTrace$|^OpenTelemetry GenAI$|^Audit Log$"), "Observability", "trace/observability title family"),
    (re.compile(r"^Tool .+|^Tool Calling$|^Tool Permissioning$|^Computer Use$"), "Tool Use", "tool-use title family"),
]

RELATION_ORDER = {"taxonomy": 0, "typed_relation": 1, "related_link": 2, "body_link": 3}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, "", text
    raw = m.group(1)
    try:
        data = yaml.safe_load(raw) or {}
    except Exception as exc:
        data = {"_yaml_error": str(exc)}
    body = text[m.end():]
    return data, raw, body


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_link(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, dict):
        return None
    s = str(value).strip().strip('"').strip("'")
    if not s:
        return None
    m = WIKILINK_RE.search(s)
    if m:
        s = m.group(1)
    elif s.startswith("[[") and s.endswith("]]')"):
        s = s[2:-2]
    s = s.split("|")[0].split("#")[0].strip()
    if not s:
        return None
    if "/" in s:
        s = Path(s).stem
    return s


def extract_body_links(body: str) -> list[str]:
    return sorted({m.group(1).split("/")[-1].strip() for m in WIKILINK_RE.finditer(body)})


def title_from(path: Path, body: str) -> str:
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return path.stem


def section_text(body: str, heading: str) -> str:
    marker = f"## {heading}"
    idx = body.find(marker)
    if idx == -1:
        return ""
    rest = body[idx + len(marker):]
    nxt = re.search(r"\n##\s+", rest)
    return (rest[:nxt.start()] if nxt else rest).strip()


def status_of_path(path: Path) -> str:
    rel = str(path.relative_to(ROOT))
    res = subprocess.run(["git", "status", "--porcelain", "--", rel], cwd=ROOT, text=True, capture_output=True)
    return res.stdout.strip()


@dataclass
class Edge:
    source: str
    target: str
    kind: str
    relation_type: str
    confidence: str
    status: str
    evidence: str
    note: str = ""


def add_edge(edges: list[Edge], node_ids: set[str], source: str, target: str | None, kind: str, relation_type: str, evidence: str, note: str = "", confidence: str = "existing") -> None:
    if not target or target == source:
        return
    status = "internal" if target in node_ids else "external_or_missing"
    edges.append(Edge(source, target, kind, relation_type, confidence, status, evidence, note))


def infer_candidates(nodes: dict[str, dict[str, Any]], edges: list[Edge]) -> list[dict[str, Any]]:
    node_ids = set(nodes)
    has_up = defaultdict(bool)
    related_targets = defaultdict(set)
    body_targets = defaultdict(set)
    typed_targets = defaultdict(list)
    for e in edges:
        if e.kind == "taxonomy" and e.status == "internal":
            has_up[e.source] = True
        if e.kind == "related_link" and e.status == "internal":
            related_targets[e.source].add(e.target)
        if e.kind == "body_link" and e.status == "internal":
            body_targets[e.source].add(e.target)
        if e.kind == "typed_relation" and e.status == "internal":
            typed_targets[e.source].append(e)

    candidates: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    def propose(source: str, target: str, confidence: str, rationale: str, candidate_type: str = "taxonomy_candidate") -> None:
        if source == target or target not in node_ids or has_up[source]:
            return
        key = (source, target, candidate_type)
        if key in seen:
            return
        seen.add(key)
        support = []
        if target in related_targets[source]:
            support.append("frontmatter.related")
        if target in body_targets[source]:
            support.append("body wikilink")
        for rel in typed_targets[source]:
            if rel.target == target:
                support.append(f"relations:{rel.relation_type}")
        candidates.append({
            "source": source,
            "target": target,
            "candidate_type": candidate_type,
            "confidence": confidence,
            "status": "needs_review",
            "rationale": rationale,
            "support": sorted(set(support)) or ["title/topic heuristic"],
        })

    for node_id, node in nodes.items():
        if has_up[node_id]:
            continue
        title = node["title"]
        topic_set = set(node.get("topics") or [])
        one_line = node.get("one_line", "")

        for pattern, parent, why in TITLE_PARENT_RULES:
            if parent in node_ids and parent != node_id and pattern.search(title):
                conf = "medium" if parent in related_targets[node_id] or parent in body_targets[node_id] else "low"
                propose(node_id, parent, conf, why, "taxonomy_candidate")

        # Topic overlap is useful for review batching, but topic is not taxonomy.
        # Keep it as a low-confidence family signal so future agents do not bulk-write it into `up`.
        for required_topics, parent, why in TOPIC_FAMILY_RULES:
            if parent in node_ids and parent != node_id and topic_set & required_topics:
                if parent in related_targets[node_id] or parent in body_targets[node_id]:
                    propose(node_id, parent, "low", why, "topic_family_review")

        for rel in typed_targets[node_id]:
            if rel.relation_type == "representative_of":
                propose(node_id, rel.target, "medium", "representative_of may indicate a member-of taxonomy, but must be checked", "typed_relation_taxonomy_candidate")

    return sorted(candidates, key=lambda c: ({"medium": 0, "low": 1}.get(c["confidence"], 2), c["source"], c["target"]))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = sorted(CONCEPT_DIR.glob("*.md"))
    raw_cards: dict[str, dict[str, Any]] = {}
    all_titles: set[str] = set()

    for path in paths:
        text = read_text(path)
        fm, raw_fm, body = split_frontmatter(text)
        if fm.get("type") != "concept":
            continue
        title = title_from(path, body)
        node_id = path.stem
        topics = [str(x) for x in as_list(fm.get("topic")) if str(x)]
        related = [clean_link(x) for x in as_list(fm.get("related"))]
        up = [clean_link(x) for x in as_list(fm.get("up"))]
        one_line = section_text(body, "一句话")[:900]
        raw_cards[node_id] = {
            "id": node_id,
            "title": title,
            "file": str(path.relative_to(ROOT)),
            "topics": topics,
            "status": str(fm.get("status") or ""),
            "freshness": str(fm.get("freshness") or ""),
            "aliases": [str(x) for x in as_list(fm.get("aliases")) if str(x)],
            "source_count": len(as_list(fm.get("source"))),
            "evidence_count": len(as_list(fm.get("evidence"))),
            "up": [x for x in up if x],
            "related": [x for x in related if x],
            "relations_raw": fm.get("relations") or [],
            "body_links": extract_body_links(body),
            "one_line": one_line.replace("\n", " ").strip(),
        }
        all_titles.add(node_id)

    edges: list[Edge] = []
    node_ids = set(raw_cards)
    dangling = []

    for source, node in raw_cards.items():
        for target in node["up"]:
            add_edge(edges, node_ids, source, target, "taxonomy", "up", "frontmatter.up")
        for rel in as_list(node["relations_raw"]):
            if isinstance(rel, dict):
                target = clean_link(rel.get("target"))
                relation_type = str(rel.get("type") or "typed_relation")
                note = str(rel.get("note") or "")
                add_edge(edges, node_ids, source, target, "typed_relation", relation_type, "frontmatter.relations", note)
        for target in node["related"]:
            add_edge(edges, node_ids, source, target, "related_link", "related", "frontmatter.related")
        existing_core = {(e.target, e.kind) for e in edges if e.source == source and e.kind in {"taxonomy", "typed_relation", "related_link"}}
        for target in node["body_links"]:
            if target in node_ids and target != source and (target, "related_link") not in existing_core:
                add_edge(edges, node_ids, source, target, "body_link", "body_wikilink", "body wikilink", confidence="observed")

    for e in edges:
        if e.status == "external_or_missing" and e.kind in {"taxonomy", "typed_relation", "related_link"}:
            dangling.append(asdict(e))

    candidates = infer_candidates(raw_cards, edges)

    edge_counter = Counter(e.kind for e in edges)
    relation_counter = Counter(e.relation_type for e in edges if e.kind == "typed_relation")
    incoming_core = Counter()
    outgoing_core = Counter()
    incoming_tax = Counter()
    for e in edges:
        if e.status == "internal" and e.kind in {"taxonomy", "typed_relation", "related_link"}:
            outgoing_core[e.source] += 1
            incoming_core[e.target] += 1
        if e.status == "internal" and e.kind == "taxonomy":
            incoming_tax[e.target] += 1

    no_up = sorted([n for n, node in raw_cards.items() if not node["up"]])
    no_core = sorted([n for n in raw_cards if incoming_core[n] == 0 and outgoing_core[n] == 0])
    weak = sorted([n for n in raw_cards if incoming_core[n] + outgoing_core[n] <= 1])
    top_tax_parents = incoming_tax.most_common(30)

    data = {
        "schema_version": 1,
        "artifact_type": "temporary_concept_relationship_map",
        "generated_at": subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip(),
        "scope": {
            "concept_dir": str(CONCEPT_DIR.relative_to(ROOT)),
            "temporary": True,
            "write_policy": "Do not write these candidates into concept cards without a separate review task.",
        },
        "summary": {
            "total_concepts": len(raw_cards),
            "edge_counts": dict(edge_counter),
            "typed_relation_counts": dict(relation_counter),
            "concepts_without_up": len(no_up),
            "core_orphans": len(no_core),
            "weakly_connected_concepts": len(weak),
            "dangling_core_targets": len(dangling),
            "candidate_edges": len(candidates),
            "taxonomy_candidates": sum(1 for c in candidates if c["candidate_type"] == "taxonomy_candidate"),
            "topic_family_review_signals": sum(1 for c in candidates if c["candidate_type"] == "topic_family_review"),
        },
        "nodes": [
            {k: v for k, v in node.items() if k not in {"relations_raw", "body_links", "one_line"}}
            for node in sorted(raw_cards.values(), key=lambda x: x["id"])
        ],
        "edges": [asdict(e) for e in sorted(edges, key=lambda e: (e.source, RELATION_ORDER.get(e.kind, 9), e.relation_type, e.target))],
        "candidate_edges": candidates,
        "audits": {
            "concepts_without_up": no_up,
            "core_orphans": no_core,
            "weakly_connected_concepts": weak,
            "top_taxonomy_parents": top_tax_parents,
            "dangling_core_targets": dangling,
        },
    }

    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def edge_table(kind: str, limit: int | None = None) -> list[str]:
        rows = []
        selected = [e for e in data["edges"] if e["kind"] == kind and e["status"] == "internal"]
        if limit:
            selected = selected[:limit]
        for e in selected:
            rows.append(f"| [[{e['source']}]] | {e['relation_type']} | [[{e['target']}]] | {e['evidence']} | {e.get('note','')} |")
        return rows

    candidate_rows = []
    for c in candidates[:120]:
        candidate_rows.append(
            f"| [[{c['source']}]] | [[{c['target']}]] | {c['candidate_type']} | {c['confidence']} | {', '.join(c['support'])} | {c['rationale']} |"
        )

    md = []
    md.append("# Temporary Concept Relationship Map")
    md.append("")
    md.append(f"Generated: `{data['generated_at']}`")
    md.append("")
    md.append("> 临时文件：用于后续概念层级开发评估。不要把候选边自动写回概念卡；每条 candidate 都需要单独人工/LLM 复核。")
    md.append("")
    md.append("## Summary")
    md.append("")
    for key, value in data["summary"].items():
        md.append(f"- {key}: {value}")
    md.append("")
    md.append("## Existing taxonomy edges (`up`)")
    md.append("")
    md.append("| Source | relation | Target | Evidence | Note |")
    md.append("|---|---|---|---|---|")
    md.extend(edge_table("taxonomy"))
    md.append("")
    md.append("## Existing typed relations")
    md.append("")
    md.append("| Source | relation | Target | Evidence | Note |")
    md.append("|---|---|---|---|---|")
    md.extend(edge_table("typed_relation"))
    md.append("")
    md.append("## Candidate edges for review")
    md.append("")
    md.append("Candidate type boundary: `taxonomy_candidate` is a possible `up` edge for human review; `topic_family_review` is only a batching / neighborhood signal and must not be bulk-written into `up`.")
    md.append("")
    md.append("Retrieval boundary: representation/feature concepts such as TF-IDF, route families such as Sparse Retrieval, and orchestration strategies such as Multi-Route Retrieval live on different semantic layers. A feature or route may support a strategy through `relations`, but that does not make it a taxonomy child for `up`.")
    md.append("")
    md.append("| Source | Candidate target | Candidate type | Confidence | Support | Rationale |")
    md.append("|---|---|---|---|---|---|")
    md.extend(candidate_rows or ["| _none_ |  |  |  |  |  |"])
    md.append("")
    md.append("## Concepts without `up`")
    md.append("")
    md.extend([f"- [[{n}]]" for n in no_up] or ["- none"])
    md.append("")
    md.append("## Weakly connected concepts")
    md.append("")
    md.extend([f"- [[{n}]]" for n in weak] or ["- none"])
    md.append("")
    md.append("## Dangling core targets")
    md.append("")
    if dangling:
        md.append("| Source | relation | Missing/external target | Kind |")
        md.append("|---|---|---|---|")
        for e in dangling:
            md.append(f"| [[{e['source']}]] | {e['relation_type']} | {e['target']} | {e['kind']} |")
    else:
        md.append("- none")
    md.append("")
    md.append("## Recommended next stages")
    md.append("")
    md.append("1. Run `decide.py` to create a per-candidate decision ledger before any writeback.")
    md.append("2. Run `writeback.py --dry-run` and inspect the planned `up` additions.")
    md.append("3. Apply only a small reviewed batch with `writeback.py --apply --limit N`; never bulk-apply `topic_family_review` signals.")
    md.append("4. For each accepted taxonomy edge, update only the child card `up`; explain non-taxonomy relationships in `relations` only when needed.")
    md.append("5. Keep `related` as ordinary adjacency; do not treat it as hierarchy.")
    md.append("6. If Breadcrumbs visualization later needs non-taxonomy edges, add mirror fields only after the relation type is stable.")
    md.append("")
    md.append("## Validation commands")
    md.append("")
    md.append("```bash")
    md.append("python3 scripts/concept_taxonomy/build.py")
    md.append("python3 scripts/concept_taxonomy/decide.py")
    md.append("python3 scripts/concept_taxonomy/writeback.py --dry-run")
    md.append("python3 scripts/concept_taxonomy/writeback.py --apply --limit 12")
    md.append("python3 scripts/concept_taxonomy/validate.py")
    md.append("git diff --check")
    md.append("```")
    md.append("")

    MD_OUT.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({"ok": True, "json": str(JSON_OUT.relative_to(ROOT)), "markdown": str(MD_OUT.relative_to(ROOT)), "summary": data["summary"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
