#!/usr/bin/env python3
"""Build/apply the concept hierarchy audit concept-hierarchy-placement review ledger.

Read-only audit stages write only project report artifacts by default and do not edit concept cards.
Limited apply is the only write path: it requires an explicit ``--apply-reviewed`` plus
``--limit`` and may only apply rows already proven by Writeback dry-run. The goal
is to keep "concepts without up" as an auditable placement question rather than
a blind field-completion target.
"""
from __future__ import annotations

import paths
import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from boundary_policy import FORBIDDEN_UP_PAIRS, NON_TAXONOMY_BOUNDARIES

ROOT = paths.ROOT
OUT_DIR = paths.OUT_DIR
MAP_JSON = OUT_DIR / "concept-relations-temp.json"
LEDGER_JSON = OUT_DIR / "relation-decision-ledger.json"
REVIEW_JSON = OUT_DIR / "concept-hierarchy-placement-review.json"
REVIEW_MD = OUT_DIR / "concept-hierarchy-placement-review.md"
CANDIDATES_JSON = OUT_DIR / "concept-hierarchy-placement-candidates.json"
CANDIDATES_MD = OUT_DIR / "concept-hierarchy-placement-candidates.md"
ADJUDICATION_JSON = OUT_DIR / "concept-hierarchy-placement-candidate-adjudication.json"
ADJUDICATION_MD = OUT_DIR / "concept-hierarchy-placement-candidate-adjudication.md"
WRITEBACK_DRY_RUN_JSON = OUT_DIR / "concept-hierarchy-placement-writeback-dry-run.json"
WRITEBACK_DRY_RUN_MD = OUT_DIR / "concept-hierarchy-placement-writeback-dry-run.md"
LIMITED_APPLY_JSON = OUT_DIR / "concept-hierarchy-placement-apply-report.json"
LIMITED_APPLY_MD = OUT_DIR / "concept-hierarchy-placement-apply-report.md"
AUDIT_CLOSURE_JSON = OUT_DIR / "concept-hierarchy-placement-closure.json"
AUDIT_CLOSURE_MD = OUT_DIR / "concept-hierarchy-placement-closure.md"
PLUGIN_JSON = OUT_DIR / "plugin-compat-validation.json"
BUILD_SCRIPT = paths.SCRIPT_DIR / "build.py"

AUDIT_BACKLOG_HOME = "agentic learning/maps/06 Wiki 健康检查.md#2026-05-17 概念层级审计边界队列"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
TOP_LEVEL_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*:\s*")

DECISIONS = {
    "unreviewed",
    "already_has_up_reviewed",
    "accept_taxonomy",
    "reject_taxonomy",
    "root_or_anchor_no_up",
    "relation_only_terminal",
    "weak_or_backlog_terminal",
    "defer_boundary_review",
}

REVIEW_STATUSES = {
    "open",
    "terminal_non_writeback",
    "ready_for_writeback",
    "written_back",
    "deferred_with_backlog",
}

STABLE_PARENT_WHITELIST = [
    "Agent Framework",
    "Agent Workflow",
    "Benchmark",
    "Agent Evaluation Benchmark",
    "Tool Use",
    "Observability",
    "RAG",
    "Retriever",
    "Sparse Retrieval",
    "RAG Evaluation",
    "Evaluation",
    "Memory",
    "Reranking",
    "Query Rewrite",
    "Chunking",
    "Multi-Route Retrieval",
]

PROPOSED_PARENT_ANCHORS = [
    "Planning",
    "Prompting",
    "Knowledge Graph",
    "Retrieval",
    "Agent",
]

ROOT_ANCHOR_NO_UP = {
    *STABLE_PARENT_WHITELIST,
    *PROPOSED_PARENT_ANCHORS,
    "LLM",
    "Prompt",
    "Transformer",
    "Token",
    "Context Window",
}

STABLE_PARENT_WHITELIST_REVIEW = {
    "Agent Framework": {
        "role": "agent_engineering_parent",
        "reason": "Explains reusable engineering abstractions for building/running Agents; safe parent only for frameworks/SDK/toolkits that are themselves framework abstractions.",
        "guard": "Do not classify products, runtimes, protocols, or infra support layers under Agent Framework merely because they help build agents.",
    },
    "Agent Workflow": {
        "role": "agent_execution_structure_parent",
        "reason": "Explains controllable stages, branches, loops, approvals, and handoffs; safe parent for workflow patterns/structures, not for runtime implementations.",
        "guard": "Do not classify runtime engines or observability standards under Agent Workflow; use relations when something executes or supports a workflow.",
    },
    "Benchmark": {
        "role": "evaluation_task_protocol_parent",
        "reason": "Explains fixed task sets, environments, scoring rules, and reporting protocols; safe parent for benchmark families, not metrics/evaluators/loaders.",
        "guard": "Do not classify LLM judges, win-rate metrics, dataset loaders, reports, or trace objects under Benchmark merely because benchmark reports use them.",
    },
    "Agent Evaluation Benchmark": {
        "role": "agent_evaluation_benchmark_parent",
        "reason": "Explains benchmark families whose tasks/protocols evaluate agent or assistant action capability: tool use, environment interaction, multi-step tasks, computer use, or collaboration.",
        "guard": "Do not classify metrics, checkers, evaluator models, dataset loaders, or generic math/QA datasets under Agent Evaluation Benchmark unless the card itself is a benchmark/task protocol for Agent action capability.",
    },
    "Tool Use": {
        "role": "tool_behavior_parent",
        "reason": "Explains the broad behavior of using external capabilities; safe parent only for direct tool-use behavior/pattern cards after evidence review.",
        "guard": "Do not classify tool safety policies, permissioning rules, or protocols as Tool Use unless the card says they are a type of tool-use behavior.",
    },
    "Observability": {
        "role": "system_visibility_parent",
        "reason": "Explains visibility/debug/trace/monitoring responsibility; safe parent for observability methods/objects, not for standards that merely support it.",
        "guard": "Do not classify semantic conventions, instrumentation libraries, or audit records as Observability just because they support visibility.",
    },
    "RAG": {
        "role": "rag_system_parent",
        "reason": "Stable retrieval-augmented generation system concept; safe parent for RAG variants whose definition is a kind of RAG.",
        "guard": "Do not classify components such as retrievers, rerankers, chunking, or graph databases as RAG; they compose with or support RAG.",
    },
    "Retriever": {
        "role": "retrieval_component_parent",
        "reason": "Stable component parent for systems/strategies that retrieve candidate evidence from external stores.",
        "guard": "Do not classify query planning, reranking, chunking, or generation-time answer synthesis as Retriever unless the card defines a retrieval component.",
    },
    "Sparse Retrieval": {
        "role": "retrieval_family_parent",
        "reason": "Already reviewed under Retriever and describes the sparse/lexical retrieval family; safe parent for BM25/TF-IDF-style retrieval methods.",
        "guard": "Do not classify multi-route orchestration under Sparse Retrieval; sparse retrieval is one route/family, not the routing strategy.",
    },
    "RAG Evaluation": {
        "role": "evaluation_subdomain_parent",
        "reason": "Already reviewed under Evaluation and describes evaluation methods specific to RAG retrieval/context/faithfulness/citation quality.",
        "guard": "Do not classify generic evaluation harnesses or observability traces as RAG Evaluation unless the card evaluates RAG-specific behavior.",
    },
    "Evaluation": {
        "role": "quality_judgment_parent",
        "reason": "Stable parent for methods/processes that judge system quality, correctness, safety, or regressions.",
        "guard": "Do not classify artifacts being evaluated, traces, or datasets as Evaluation merely because evaluators consume them.",
    },
    "Memory": {
        "role": "agent_information_persistence_parent",
        "reason": "Stable parent for mechanisms that save/retrieve/update information across task or session time.",
        "guard": "Do not classify RAG, context windows, or runtime state as Memory unless the card's own boundary says it is a memory mechanism.",
    },
    "Reranking": {
        "role": "retrieval_quality_stage_parent",
        "reason": "Stable parent for second-stage candidate ordering methods after initial retrieval.",
        "guard": "Do not classify retrieval expansion, query rewrite, or route fusion as Reranking; reranking reorders candidates already recalled.",
    },
    "Query Rewrite": {
        "role": "retrieval_query_transformation_parent",
        "reason": "Stable parent for techniques that transform the user's query before retrieval.",
        "guard": "Do not classify query planning or multi-source orchestration as Query Rewrite unless the core action is rewriting the query expression.",
    },
    "Chunking": {
        "role": "ingestion_segmentation_parent",
        "reason": "Stable parent for document segmentation strategies that create retrievable/contextual units.",
        "guard": "Do not classify retrieval, embedding, or ingestion tooling as Chunking unless the card is specifically a chunking strategy.",
    },
    "Multi-Route Retrieval": {
        "role": "retrieval_orchestration_parent",
        "reason": "Already reviewed under Retriever and describes multi-route candidate recall/fusion; safe parent for retrieval strategies whose defining feature is multiple routes.",
        "guard": "Do not classify BM25/TF-IDF under Multi-Route Retrieval; they can be routes/signals, not the route orchestration strategy.",
    },
}

PROPOSED_PARENT_ANCHOR_REVIEW = {
    "Planning": {
        "decision": "not_auto_approved",
        "reason": "Broad and useful anchor, but it mixes prompt-time reasoning, workflow planning, replanning, and task control; Candidate adjudication must prove any child is a kind of planning rather than a technique that uses planning.",
    },
    "Prompting": {
        "decision": "missing_card_not_approved",
        "reason": "No canonical concept card exists; current vault has [[Prompt]] and specific prompting-pattern cards. Do not create or use a phantom parent during this audit.",
    },
    "Knowledge Graph": {
        "decision": "not_auto_approved",
        "reason": "Stable concept card, but many nearby cards are graph databases, GraphRAG systems, entity techniques, or relation-supporting infrastructure rather than kinds of Knowledge Graph.",
    },
    "Retrieval": {
        "decision": "missing_card_not_approved",
        "reason": "No canonical concept card exists; use reviewed parents such as [[Retriever]], [[Sparse Retrieval]], [[Query Rewrite]], [[Reranking]], or [[Multi-Route Retrieval]] when strict taxonomy is proven.",
    },
    "Agent": {
        "decision": "not_auto_approved",
        "reason": "Root learning anchor with seed status; too broad for automatic parent generation. Specific children should usually use narrower parents such as Agent Workflow, Agent Framework, Tool Use, Memory, Evaluation, or Observability.",
    },
}

ROOT_ANCHOR_EXTRA_REVIEW = {
    "LLM": "Foundation/root concept for model systems; keep as anchor, not a default parent for architecture components without strict-is-a proof.",
    "Prompt": "Foundation/root concept for input organization; keep as anchor, not an automatic parent for every prompting/security pattern.",
    "Transformer": "Foundation/root architecture card; components such as attention/position encoding are usually component-of, not kinds-of Transformer.",
    "Token": "Foundation unit card; keep as anchor for context/tokenization reasoning, not as a broad parent for unrelated LLM system cards.",
    "Context Window": "Foundation capacity-boundary card; keep as anchor rather than parent for RAG/memory/context-engineering mechanisms.",
}

DEFERRED_PARENT_ROUTE_PRECHECK = {
    "A2A": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Protocol/ecosystem card; no approved protocol parent exists and Agent is intentionally not auto-approved.",
    },
    "ACP": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Protocol/ecosystem card; no approved protocol parent exists and Agent is intentionally not auto-approved.",
    },
    "Approval Gate": {
        "route": "candidate_adjudication",
        "possible_parent": "Agent Workflow",
        "reason": "May be a workflow control pattern, but must be adjudicated from card text before writing `up`.",
    },
    "Browser Agent": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Could be a kind of Agent, but Agent is not auto-approved and no narrower reviewed parent exists.",
    },
    "Code Execution Sandbox": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Sandbox/security runtime boundary; no approved sandbox/security parent exists.",
    },
    "Data Exfiltration": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Security risk card; no approved security-risk parent exists and Prompt is not a safe parent.",
    },
    "Entity Resolution": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "May support Knowledge Graph or retrieval, but support/use is not strict taxonomy.",
    },
    "GUI Grounding": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Computer-use/grounding capability; no approved grounding or computer-use parent exists.",
    },
    "Least Privilege Tools": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Tool safety/policy principle; related to Tool Use but not automatically a kind of Tool Use.",
    },
    "MCP": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Protocol/root ecosystem card; no approved protocol parent exists.",
    },
    "MCP Registry": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Registry/ecosystem component likely belongs near MCP, but MCP is not yet an approved parent.",
    },
    "Memory Reflection": {
        "route": "candidate_adjudication",
        "possible_parent": "Memory",
        "reason": "May be a memory mechanism, but must be proven from the card boundary before writing `up`.",
    },
    "Multi-Head Attention": {
        "route": "likely_relation_only",
        "possible_parent": None,
        "reason": "Architecture mechanism/component; do not auto-place under Transformer because component-of is not kind-of.",
    },
    "Observation": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Agent loop/runtime signal; no approved Agent Loop parent exists.",
    },
    "Obsidian + LLM Wiki": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Project/workflow artifact card; no approved parent should absorb local wiki tooling by similarity.",
    },
    "Oh My Codex (OMX)": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Concrete runtime/product/workflow ecosystem; do not classify as Agent Framework without product-boundary review.",
    },
    "Policy Engine": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Policy/safety runtime component; no approved policy/guardrail parent exists.",
    },
    "Positional Encoding": {
        "route": "likely_relation_only",
        "possible_parent": None,
        "reason": "Architecture mechanism/component; do not auto-place under Transformer because component-of is not kind-of.",
    },
    "Prompt Injection": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Security risk/attack class; Prompt is related context but not a strict parent.",
    },
    "ReAct": {
        "route": "candidate_adjudication",
        "possible_parent": "Agent Workflow",
        "reason": "May be an agent workflow/pattern, but its prompting/loop boundary needs Candidate adjudication.",
    },
    "Sandbox Workspace": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Workspace/sandbox runtime boundary; no approved sandbox/workspace parent exists.",
    },
    "Self-Attention": {
        "route": "likely_relation_only",
        "possible_parent": None,
        "reason": "Architecture mechanism/component; do not auto-place under Transformer because component-of is not kind-of.",
    },
    "Trajectory": {
        "route": "remain_deferred",
        "possible_parent": None,
        "reason": "Trace/evaluation object; may be evaluated or observed, but it is not automatically Evaluation or Observability.",
    },
}

SUPPRESSED_DEFERRED_SIGNALS = {
    "A2A": {
        "suppressed_target": "Agent",
        "signal_type": "broad_anchor_not_approved",
        "reason": "A2A is a protocol/ecosystem card. `Agent` is intentionally not an auto-approved parent, and no approved protocol parent exists.",
    },
    "ACP": {
        "suppressed_target": "Agent",
        "signal_type": "broad_anchor_not_approved",
        "reason": "ACP is a protocol/ecosystem card. `Agent` is intentionally not an auto-approved parent, and no approved protocol parent exists.",
    },
    "Browser Agent": {
        "suppressed_target": "Agent",
        "signal_type": "broad_anchor_not_approved",
        "reason": "The title suggests a kind of Agent, but `Agent` is too broad for automatic parent generation.",
    },
    "Code Execution Sandbox": {
        "suppressed_target": "Tool Use",
        "signal_type": "security_runtime_not_tool_behavior",
        "reason": "A sandbox supports safe tool/code execution, but support/infrastructure is not a kind of Tool Use.",
    },
    "Data Exfiltration": {
        "suppressed_target": "Prompt",
        "signal_type": "security_risk_not_prompt",
        "reason": "Data exfiltration can occur through prompts/tools/retrieval, but it is a risk class, not a kind of Prompt.",
    },
    "Entity Resolution": {
        "suppressed_target": "Knowledge Graph",
        "signal_type": "supports_graph_not_graph",
        "reason": "Entity resolution can support knowledge graphs, but support/use is not strict taxonomy; Knowledge Graph is also not auto-approved.",
    },
    "GUI Grounding": {
        "suppressed_target": "Agent",
        "signal_type": "capability_not_broad_agent_parent",
        "reason": "GUI grounding is a capability used by computer-use agents, not automatically a kind of Agent.",
    },
    "Least Privilege Tools": {
        "suppressed_target": "Tool Use",
        "signal_type": "policy_principle_not_tool_behavior",
        "reason": "Least-privilege tooling constrains Tool Use, but the policy principle itself is not automatically a Tool Use subtype.",
    },
    "MCP": {
        "suppressed_target": "Tool Use",
        "signal_type": "protocol_not_tool_behavior",
        "reason": "MCP standardizes tool/context connection; protocol/support is not a kind of Tool Use.",
    },
    "MCP Registry": {
        "suppressed_target": "MCP",
        "signal_type": "unapproved_parent",
        "reason": "MCP Registry likely belongs near MCP, but MCP is not an approved parent in Conservative candidate generation.",
    },
    "Multi-Head Attention": {
        "suppressed_target": "Transformer",
        "signal_type": "component_of_not_kind_of",
        "reason": "Multi-Head Attention is a Transformer mechanism/component, not a kind of Transformer.",
    },
    "Observation": {
        "suppressed_target": "Agent Workflow",
        "signal_type": "loop_signal_not_workflow",
        "reason": "Observation is an agent-loop feedback signal; being used inside workflows is not strict taxonomy.",
    },
    "Obsidian + LLM Wiki": {
        "suppressed_target": "RAG",
        "signal_type": "local_system_not_rag_subtype",
        "reason": "The local wiki may use retrieval-like ideas, but the project/workflow artifact is not a kind of RAG.",
    },
    "Oh My Codex (OMX)": {
        "suppressed_target": "Agent Framework",
        "signal_type": "product_runtime_not_framework_subtype_without_review",
        "reason": "OMX is a concrete Codex orchestration/runtime ecosystem; candidate generation must not classify it as Agent Framework without product-boundary review.",
    },
    "Policy Engine": {
        "suppressed_target": "Tool Use",
        "signal_type": "policy_layer_not_tool_behavior",
        "reason": "A policy engine constrains tools/actions; constraint layer is not a kind of Tool Use.",
    },
    "Positional Encoding": {
        "suppressed_target": "Transformer",
        "signal_type": "component_of_not_kind_of",
        "reason": "Positional Encoding is a Transformer mechanism/component, not a kind of Transformer.",
    },
    "Prompt Injection": {
        "suppressed_target": "Prompt",
        "signal_type": "attack_class_not_prompt",
        "reason": "Prompt Injection manipulates prompts but is an attack class, not a kind of Prompt.",
    },
    "Sandbox Workspace": {
        "suppressed_target": "Tool Use",
        "signal_type": "workspace_runtime_not_tool_behavior",
        "reason": "A sandbox workspace hosts actions/tools; hosting infrastructure is not a Tool Use subtype.",
    },
    "Self-Attention": {
        "suppressed_target": "Transformer",
        "signal_type": "component_of_not_kind_of",
        "reason": "Self-Attention is a Transformer mechanism/component, not a kind of Transformer.",
    },
    "Trajectory": {
        "suppressed_target": "Evaluation",
        "signal_type": "evaluated_object_not_evaluation_method",
        "reason": "Trajectory can be evaluated or observed, but the path/object being evaluated is not itself Evaluation.",
    },
}

CANDIDATE_ADJUDICATIONS = {
    ("Approval Gate", "Agent Workflow"): {
        "decision": "reject_taxonomy",
        "review_status": "terminal_non_writeback",
        "writeback_action": "none",
        "strict_taxonomy_test": "fails: Approval Gate is a workflow control point / approval node used inside a workflow, not a workflow structure or workflow pattern itself.",
        "decision_reason": (
            "Reject `up: [[Agent Workflow]]`: the child card defines Approval Gate as an execution-before-control point for high-risk actions. "
            "The parent card allows workflows to contain approval gates, but containment/composition is not strict taxonomy."
        ),
        "source_evidence_needles": ["控制点", "执行前的准入点", "Approval Gate 应放在不可逆"],
        "target_evidence_needles": ["步骤、分支、循环、审批和交接", "workflow 会把任务拆成节点、边、条件、循环、并行分支、handoff 和 approval gate"],
        "drift_guard": [
            "Do not classify Approval Gate under Agent Workflow merely because workflow definitions can contain approval nodes; node/control-point-in is not kind-of.",
            "If this relationship is written later, prefer a typed relation such as `control_point_in` / `composes_with`, not `up`.",
        ],
    },
    ("Memory Reflection", "Memory"): {
        "decision": "accept_taxonomy",
        "review_status": "ready_for_writeback",
        "writeback_action": "add_up",
        "strict_taxonomy_test": "passes: Memory Reflection is a memory-maintenance mechanism that saves, filters, updates, and governs long-term memory.",
        "decision_reason": (
            "Accept `up: [[Memory]]`: the child card repeatedly defines Memory Reflection as a process for summarizing, filtering, updating, and governing long-term memory. "
            "The parent Memory card defines memory as mechanisms for saving, retrieving, updating, and using information across time, so this is a strict subtype/mechanism relation."
        ),
        "source_evidence_needles": ["记忆维护流程", "长期记忆", "Reflection 通常以"],
        "target_evidence_needles": ["保存、检索、更新并使用信息", "写入、存储、检索、冲突解决、过期和权限"],
        "drift_guard": [
            "Do not merge Memory Reflection with Reflexion: Reflexion may provide candidate experience, but Memory Reflection is the governed memory-maintenance process.",
            "Only keep `up: [[Memory]]` while the card remains about memory write/update/governance; task reflection or generic self-critique belongs elsewhere.",
        ],
    },
    ("ReAct", "Agent Workflow"): {
        "decision": "reject_taxonomy",
        "review_status": "terminal_non_writeback",
        "writeback_action": "none",
        "strict_taxonomy_test": "fails: ReAct is a reasoning/action/observation Agent Loop pattern; workflows may absorb or wrap parts of it, but it is not a workflow subtype.",
        "decision_reason": (
            "Reject `up: [[Agent Workflow]]`: the ReAct card explicitly frames ReAct as an Agent Loop / reasoning-action-observation pattern and warns it is not a production workflow template. "
            "The card says modern systems often put stable paths into workflows and keep dynamic parts in an agent loop, so the relation is boundary/adjacency rather than strict taxonomy."
        ),
        "source_evidence_needles": ["理解 Agent Loop 的地基卡", "不是完整的生产级 Agent 平台", "很多生产系统会把稳定路径写成 [[Agent Workflow]]"],
        "target_evidence_needles": ["Agent Workflow 不是 [[Agent Loop]] 的同义词", "真实系统常混合"],
        "drift_guard": [
            "Do not classify ReAct under Agent Workflow from a mere workflow mention; ReAct is primarily an Agent Loop pattern.",
            "If [[Agent Loop]] becomes an approved parent later, review ReAct against that narrower parent instead of using Agent Workflow as a proxy.",
        ],
    },
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def section_text(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].split("\n## ", 1)[0].strip()


def compact_excerpt(text: str, needle: str, max_len: int = 180) -> str:
    clean = " ".join(text.split())
    if not needle:
        return clean[:max_len]
    index = clean.lower().find(needle.lower())
    if index < 0:
        return clean[:max_len]
    start = max(index - 50, 0)
    end = min(index + len(needle) + 90, len(clean))
    prefix = "…" if start > 0 else ""
    suffix = "…" if end < len(clean) else ""
    return f"{prefix}{clean[start:end]}{suffix}"


def format_md_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return f"`{json.dumps(value, ensure_ascii=False)}`"
    return str(value)


def run_build() -> None:
    subprocess.run([sys.executable, str(BUILD_SCRIPT)], cwd=ROOT, check=True)


def load_ledger_decisions() -> dict[str, list[dict[str, Any]]]:
    if not LEDGER_JSON.exists():
        return {}
    ledger = load_json(LEDGER_JSON)
    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for decision in ledger.get("decisions", []):
        source = str(decision.get("source") or "")
        if source:
            by_source[source].append(decision)
    return by_source


def edge_indexes(edges: list[dict[str, Any]]) -> dict[str, dict[str, list[dict[str, Any]]]]:
    by_source: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for edge in edges:
        source = str(edge.get("source") or "")
        if not source:
            continue
        by_source[source][str(edge.get("kind") or "")].append(edge)
    return by_source


def candidate_indexes(candidates: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        source = str(candidate.get("source") or "")
        if source:
            by_source[source].append(candidate)
    for rows in by_source.values():
        rows.sort(key=lambda c: (c.get("candidate_type", ""), c.get("confidence", ""), c.get("target", "")))
    return by_source


def candidate_basis_for(concept: str, candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    basis = []
    for candidate in candidates:
        target = str(candidate.get("target") or "")
        pair = (concept, target)
        forbidden = pair in FORBIDDEN_UP_PAIRS or pair in NON_TAXONOMY_BOUNDARIES
        basis.append(
            {
                "target": target,
                "candidate_type": candidate.get("candidate_type"),
                "confidence": candidate.get("confidence"),
                "support": candidate.get("support") or [],
                "rationale": candidate.get("rationale") or "",
                "candidate_status": candidate.get("status") or "",
                "known_forbidden_as_up": forbidden,
            }
        )
    return basis


def drift_guards_for(concept: str, basis: list[dict[str, Any]]) -> list[str]:
    guards: list[str] = []
    for item in basis:
        target = str(item.get("target") or "")
        pair = (concept, target)
        policy = NON_TAXONOMY_BOUNDARIES.get(pair)
        if policy:
            guards.append(
                f"Do not write {concept} up [[{target}]]: {policy.get('rationale', 'known non-taxonomy boundary')}"
            )
        elif pair in FORBIDDEN_UP_PAIRS:
            guards.append(f"Do not write {concept} up [[{target}]]: forbidden non-taxonomy boundary.")
        elif item.get("candidate_type") == "topic_family_review":
            guards.append(
                f"Do not bulk-write {concept} up [[{target}]] from topic_family_review; topic overlap is only a review signal."
            )
    return sorted(set(guards))


def choose_candidate_parent(basis: list[dict[str, Any]]) -> str | None:
    taxonomy = [
        item
        for item in basis
        if item.get("candidate_type") in {"taxonomy_candidate", "typed_relation_taxonomy_candidate"}
        and not item.get("known_forbidden_as_up")
    ]
    if len(taxonomy) == 1:
        return str(taxonomy[0].get("target") or "") or None
    return None


def classify_initial_triage(row: dict[str, Any], ledger_decisions: list[dict[str, Any]], reviewed_at: str) -> None:
    """Apply the concept hierarchy audit Initial triage to one full-card ledger row.

    This is not the Candidate adjudication LLM/adjudicator pass and it never schedules writeback.
    It only replaces ``unreviewed`` with one coarse routing decision so every card
    has an explicit next state.
    """
    concept = row["concept"]
    row["reviewed_at"] = reviewed_at
    row["reviewer"] = "rule:concept-hierarchy-audit-initial-triage"
    row["writeback_action"] = "none"

    if row["current_up"]:
        row["decision"] = "already_has_up_reviewed"
        row["decision_reason"] = "Existing top-level `up` was produced by the prior guarded relation pipeline; Initial triage records that concept hierarchy placement is already present and does not schedule another writeback."
        row["review_status"] = "terminal_non_writeback"
        return

    if concept in ROOT_ANCHOR_NO_UP:
        row["decision"] = "root_or_anchor_no_up"
        row["decision_reason"] = "This concept is a stable parent/root/anchor candidate for this vault's learning taxonomy; no parent is forced merely to reduce the no-up count."
        row["review_status"] = "terminal_non_writeback"
        return

    if ledger_decisions:
        row["decision"] = "relation_only_terminal"
        row["decision_reason"] = "Existing candidate-edge ledger decisions for this concept are terminal non-writeback signals (reject_taxonomy or adjacency_only); keep them as related/relations/body context rather than `up`."
        row["review_status"] = "terminal_non_writeback"
        for decision in ledger_decisions:
            guardrail = decision.get("guardrail")
            rationale = decision.get("decision_rationale")
            target = decision.get("target")
            if guardrail or rationale:
                row["drift_guard"].append(
                    f"Ledger: {concept} -> {target}: {rationale or guardrail}"
                )
        row["drift_guard"] = sorted(set(row["drift_guard"]))
        return

    if row["candidate_parent"]:
        row["decision"] = "accept_taxonomy"
        row["decision_reason"] = "Initial triage found a single non-forbidden taxonomy candidate; this is only a Initial triage candidate and still requires later adjudication before dry-run/writeback."
        row["review_status"] = "open"
        return

    if row["current_relations_count"] > 0:
        row["decision"] = "relation_only_terminal"
        row["decision_reason"] = "The card already carries typed relation evidence, but no strict parent candidate; keep the value in `relations` rather than inventing a taxonomy parent."
        row["review_status"] = "terminal_non_writeback"
        return

    if row["card_status"] in {"seed", "review"}:
        row["decision"] = "weak_or_backlog_terminal"
        row["decision_reason"] = "The card is seed/review state with no current `up` and no safe taxonomy candidate; keep it parentless until its boundary matures or it enters a later backlog review."
        row["review_status"] = "terminal_non_writeback"
        return

    row["decision"] = "defer_boundary_review"
    row["decision_reason"] = "No safe parent, existing `up`, typed relation, or terminal weak/backlog signal was found; this requires concept-card evidence review in a later stage."
    row["review_status"] = "open"


def apply_initial_triage(review: dict[str, Any]) -> None:
    ledger_by_source = load_ledger_decisions()
    reviewed_at = utc_now()
    for row in review["rows"]:
        classify_initial_triage(row, ledger_by_source.get(row["concept"], []), reviewed_at)
    review["classification_stage"] = "initial_triage"
    review["generated_at"] = reviewed_at
    review["scope"]["write_policy"] = "Initial triage only. Do not edit concept cards or write up from this artifact without later adjudication + dry-run."
    recompute_summary(review)
    validate_review(review, load_json(MAP_JSON))


def apply_parent_whitelist_review(review: dict[str, Any]) -> None:
    """Attach the concept hierarchy audit Parent-whitelist audit.

    Parent-whitelist review fixes the candidate-generation boundary. It intentionally does not
    change row decisions or schedule writeback; the 23 deferred rows stay open
    until Candidate adjudication adjudicates them or sends them to backlog.
    """
    if any(row.get("decision") == "unreviewed" for row in review["rows"]):
        apply_initial_triage(review)

    reviewed_at = utc_now()
    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    node_ids = set(rows_by_concept)

    approved_parents: list[dict[str, Any]] = []
    for parent in STABLE_PARENT_WHITELIST:
        if parent not in node_ids:
            continue
        row = rows_by_concept[parent]
        meta = STABLE_PARENT_WHITELIST_REVIEW[parent]
        approved_parents.append(
            {
                "concept": parent,
                "path": row["path"],
                "card_status": row.get("card_status") or "",
                "current_up": row.get("current_up") or [],
                "role": meta["role"],
                "decision": "approved_for_candidate_generation",
                "reason": meta["reason"],
                "drift_guard": meta["guard"],
            }
        )

    proposed_existing: list[dict[str, Any]] = []
    proposed_missing: list[dict[str, Any]] = []
    for anchor in PROPOSED_PARENT_ANCHORS:
        meta = PROPOSED_PARENT_ANCHOR_REVIEW[anchor]
        item = {
            "concept": anchor,
            "decision": meta["decision"],
            "reason": meta["reason"],
        }
        if anchor in node_ids:
            row = rows_by_concept[anchor]
            item.update({"path": row["path"], "card_status": row.get("card_status") or ""})
            proposed_existing.append(item)
        else:
            item.update({"path": None, "card_status": None})
            proposed_missing.append(item)

    extra_root_anchors: list[dict[str, Any]] = []
    for anchor, reason in ROOT_ANCHOR_EXTRA_REVIEW.items():
        if anchor not in node_ids:
            continue
        row = rows_by_concept[anchor]
        extra_root_anchors.append(
            {
                "concept": anchor,
                "path": row["path"],
                "card_status": row.get("card_status") or "",
                "decision": "root_anchor_not_parent_whitelist",
                "reason": reason,
            }
        )

    deferred_precheck: list[dict[str, Any]] = []
    for concept in sorted(review["audit_sets"].get("by_decision", {}).get("defer_boundary_review", [])):
        row = rows_by_concept[concept]
        meta = DEFERRED_PARENT_ROUTE_PRECHECK.get(concept, {})
        possible_parent = meta.get("possible_parent")
        deferred_precheck.append(
            {
                "concept": concept,
                "path": row["path"],
                "route": meta.get("route", "remain_deferred"),
                "possible_parent": possible_parent,
                "possible_parent_is_approved": bool(possible_parent and possible_parent in {p["concept"] for p in approved_parents}),
                "reason": meta.get("reason", "No Parent-whitelist review route precheck rule; keep deferred until Candidate adjudication."),
                "writeback_action": "none",
            }
        )

    review["classification_stage"] = "parent_whitelist_review"
    review["generated_at"] = reviewed_at
    review["scope"]["write_policy"] = (
        "Parent-whitelist audit only. Approved parents may seed later candidate generation, "
        "but no concept-card writeback is scheduled before Candidate adjudication and dry-run."
    )
    review["parent_whitelist_review"] = {
        "reviewed_at": reviewed_at,
        "reviewer": "llm-adjudicator:concept-hierarchy-audit-parent-whitelist",
        "rules": [
            "`up` remains strict taxonomy / belongs-to only.",
            "Approved parent whitelist controls candidate generation; it is not permission to bulk-write `up`.",
            "Proposed anchors are not auto-approved; missing anchors must not be used as phantom parents.",
            "Component-of, supports, standardizes, executes, protects, or is-adjacent-to remains in `relations`, `related`, or body boundaries.",
        ],
        "approved_parents": approved_parents,
        "proposed_anchors_not_auto_approved": proposed_existing,
        "proposed_anchors_missing_not_approved": proposed_missing,
        "root_anchors_not_parent_whitelist": extra_root_anchors,
        "deferred_parent_route_precheck": deferred_precheck,
    }

    recompute_summary(review)
    review["summary"].update(
        {
            "write_policy": review["scope"]["write_policy"],
            "parent_whitelist_reviewed": True,
            "stable_parent_whitelist_approved": len(approved_parents),
            "proposed_parent_anchors_not_auto_approved": len(proposed_existing),
            "missing_proposed_parent_anchors": len(proposed_missing),
            "root_anchors_not_parent_whitelist": len(extra_root_anchors),
            "deferred_rows_parent_prechecked": len(deferred_precheck),
            "candidate_adjudication_needed": sum(
                1 for item in deferred_precheck if item["route"] == "candidate_adjudication"
            ),
        }
    )
    validate_review(review, load_json(MAP_JSON))


def approved_parent_names(review: dict[str, Any]) -> set[str]:
    parent_review = review.get("parent_whitelist_review") or {}
    approved = parent_review.get("approved_parents") or []
    return {str(item.get("concept") or "") for item in approved if item.get("concept")}


def parent_precheck_by_concept(review: dict[str, Any]) -> dict[str, dict[str, Any]]:
    parent_review = review.get("parent_whitelist_review") or {}
    return {
        str(item.get("concept")): item
        for item in parent_review.get("deferred_parent_route_precheck") or []
        if item.get("concept")
    }


def candidate_support_from_card(row: dict[str, Any], target: str) -> tuple[list[str], list[str]]:
    """Collect conservative, human-readable support signals from the card text."""
    path = ROOT / str(row["path"])
    text = strip_frontmatter(load_text(path)) if path.exists() else ""
    one = section_text(text, "一句话")
    detail = section_text(text, "概念详解")
    boundary = section_text(text, "边界细节")
    support: list[str] = []
    excerpts: list[str] = []

    if target and target in row["concept"]:
        support.append("title_contains_approved_parent")
        excerpts.append(row["concept"])
    if target == "Memory" and row["concept"].startswith("Memory "):
        support.append("title_prefix_memory_family")
    if target == "Agent Workflow" and row["concept"] in {"Approval Gate", "ReAct"}:
        support.append("parent_route_precheck_workflow_candidate")

    link_count = text.count(f"[[{target}]]")
    plain_count = text.lower().count(target.lower()) if target else 0
    if link_count >= 1:
        support.append(f"body_wikilink_count:{link_count}")
        excerpts.append(compact_excerpt(text, f"[[{target}]]"))
    if plain_count >= 2:
        support.append(f"body_plain_count:{plain_count}")
        excerpts.append(compact_excerpt(text, target))

    for section_name, section in (("一句话", one), ("概念详解", detail), ("边界细节", boundary)):
        if target and target.lower() in section.lower():
            support.append(f"section_mentions:{section_name}")
            excerpts.append(compact_excerpt(section, target))

    if target == "Memory" and "长期记忆" in text:
        support.append("body_mentions_long_term_memory")
        excerpts.append(compact_excerpt(text, "长期记忆"))
    if target == "Agent Workflow" and row["concept"] == "Approval Gate":
        support.append("definition_control_point_before_high_risk_action")
        excerpts.append(compact_excerpt(one or detail, "控制点"))
    if target == "Agent Workflow" and row["concept"] == "ReAct":
        support.append("body_distinguishes_agent_loop_from_workflow")

    return sorted(set(support)), list(dict.fromkeys(excerpts))[:3]


def evidence_for_needles(path_text: str, path: str, needles: list[str]) -> list[dict[str, str]]:
    evidence: list[dict[str, str]] = []
    for needle in needles:
        excerpt = compact_excerpt(path_text, needle, max_len=240)
        if excerpt:
            evidence.append({"path": path, "needle": needle, "excerpt": excerpt})
    return evidence


def build_candidate_evidence(row: dict[str, Any], target_row: dict[str, Any], spec: dict[str, Any]) -> list[dict[str, str]]:
    source_path = ROOT / str(row["path"])
    target_path = ROOT / str(target_row["path"])
    source_text = strip_frontmatter(load_text(source_path)) if source_path.exists() else ""
    target_text = strip_frontmatter(load_text(target_path)) if target_path.exists() else ""
    evidence = []
    evidence.extend(evidence_for_needles(source_text, row["path"], spec.get("source_evidence_needles", [])))
    evidence.extend(evidence_for_needles(target_text, target_row["path"], spec.get("target_evidence_needles", [])))
    return evidence[:6]


def build_conservative_candidates(review: dict[str, Any]) -> dict[str, Any]:
    approved = approved_parent_names(review)
    precheck = parent_precheck_by_concept(review)
    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    deferred = review.get("audit_sets", {}).get("by_decision", {}).get("defer_boundary_review", [])

    candidates: list[dict[str, Any]] = []
    suppressed: list[dict[str, Any]] = []
    generated_at = utc_now()

    for concept in sorted(deferred):
        row = rows_by_concept[concept]
        pre = precheck.get(concept) or {}
        target = pre.get("possible_parent")
        if (
            pre.get("route") == "candidate_adjudication"
            and target in approved
            and (concept, target) not in FORBIDDEN_UP_PAIRS
            and (concept, target) not in NON_TAXONOMY_BOUNDARIES
        ):
            support, excerpts = candidate_support_from_card(row, str(target))
            support.append("parent_possible_parent_is_approved")
            candidate = {
                "source": concept,
                "source_path": row["path"],
                "target": target,
                "target_is_approved_stable_parent": True,
                "candidate_type": "conservative_taxonomy_candidate",
                "confidence": "low" if concept in {"Approval Gate", "ReAct"} else "medium",
                "status": "candidate_for_adjudication",
                "writeback_action": "none",
                "must_review_before_writeback": True,
                "support": sorted(set(support)),
                "evidence_excerpt": excerpts,
                "rationale": (
                    "Conservative Conservative candidate generation candidate from Parent-whitelist review route precheck plus card text/title signals. "
                    "This is not accepted taxonomy until Candidate adjudication."
                ),
                "drift_guard": [
                    f"Do not write {concept} up [[{target}]] until Candidate adjudication records an explicit strict-taxonomy decision.",
                    "Do not use related/body-link/topic overlap alone as hierarchy evidence.",
                ],
            }
            candidates.append(candidate)
            continue

        suppressed_meta = SUPPRESSED_DEFERRED_SIGNALS.get(concept)
        if suppressed_meta:
            suppressed.append(
                {
                    "source": concept,
                    "source_path": row["path"],
                    "target": suppressed_meta["suppressed_target"],
                    "signal_type": suppressed_meta["signal_type"],
                    "status": "suppressed_not_candidate",
                    "reason": suppressed_meta["reason"],
                    "writeback_action": "none",
                }
            )
        else:
            suppressed.append(
                {
                    "source": concept,
                    "source_path": row["path"],
                    "target": None,
                    "signal_type": "no_conservative_approved_parent_signal",
                    "status": "suppressed_not_candidate",
                    "reason": "No conservative signal points to a Parent-whitelist review approved stable parent.",
                    "writeback_action": "none",
                }
            )

    target_counts = Counter(candidate["target"] for candidate in candidates)
    return {
        "schema_version": 1,
        "artifact_type": "taxonomy_placement_candidates",
        "generated_at": generated_at,
        "input_review": rel(REVIEW_JSON),
        "classification_stage": "conservative_candidates",
        "policy": {
            "candidate_scope": "Only Initial triage/3 deferred rows are considered in Conservative candidate generation.",
            "allowed_targets": sorted(approved),
            "forbidden_inputs": [
                "topic overlap alone",
                "body wikilink once",
                "same raw source",
                "title similarity without approved parent",
                "component-of / supports / standardizes / executes / protects relations",
                "proposed anchors that Parent-whitelist review did not approve",
                "missing phantom parents such as Prompting or Retrieval",
            ],
            "write_policy": "No writeback in Conservative candidate generation. Candidates feed Candidate adjudication only.",
        },
        "summary": {
            "deferred_rows_considered": len(deferred),
            "approved_parent_count": len(approved),
            "generated_candidates": len(candidates),
            "suppressed_signals": len(suppressed),
            "candidate_targets": dict(sorted(target_counts.items())),
            "adjudication_items": len(candidates),
            "open_writeback": 0,
            "dry_run_planned": 0,
        },
        "candidates": candidates,
        "suppressed_signals": suppressed,
    }


def apply_conservative_candidates(review: dict[str, Any]) -> dict[str, Any]:
    if review.get("classification_stage") != "parent_whitelist_review":
        apply_parent_whitelist_review(review)

    generated_at = utc_now()
    candidates = build_conservative_candidates(review)
    candidates["generated_at"] = generated_at
    review["classification_stage"] = "conservative_candidates"
    review["generated_at"] = generated_at
    review["scope"]["write_policy"] = (
        "Conservative candidate generation conservative candidate generation only. Generated candidates feed Candidate adjudication; "
        "no concept-card writeback is scheduled before accept_taxonomy + dry-run."
    )
    review["conservative_candidates"] = {
        "generated_at": generated_at,
        "candidate_artifact_json": rel(CANDIDATES_JSON),
        "candidate_artifact_md": rel(CANDIDATES_MD),
        "summary": candidates["summary"],
        "candidate_sources": [item["source"] for item in candidates["candidates"]],
        "suppressed_sources": [item["source"] for item in candidates["suppressed_signals"]],
    }

    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    for candidate in candidates["candidates"]:
        row = rows_by_concept[candidate["source"]]
        row.setdefault("candidate_generation_taxonomy", []).append(
            {
                "target": candidate["target"],
                "candidate_type": candidate["candidate_type"],
                "confidence": candidate["confidence"],
                "status": candidate["status"],
                "support": candidate["support"],
                "writeback_action": "none",
            }
        )

    recompute_summary(review)
    review["summary"].update(
        {
            "write_policy": review["scope"]["write_policy"],
            "conservative_candidates_generated": candidates["summary"]["generated_candidates"],
            "candidate_generation_suppressed_signals": candidates["summary"]["suppressed_signals"],
            "adjudication_items": candidates["summary"]["adjudication_items"],
            "open_writeback": 0,
            "dry_run_planned": 0,
        }
    )
    validate_review(review, load_json(MAP_JSON))
    return candidates


def build_candidate_adjudication(review: dict[str, Any], candidates: dict[str, Any]) -> dict[str, Any]:
    """Adjudicate Conservative candidate generation candidates without editing concept cards.

    Candidate adjudication records the LLM/semantic decision and dry-run eligibility. It does
    not set top-level row.writeback_action, because the review ledger itself is
    still a report artifact; Writeback dry-run consumes the explicit adjudication
    artifact rows whose decision is accept_taxonomy + writeback_action add_up.
    """
    generated_at = utc_now()
    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    approved = approved_parent_names(review)
    records: list[dict[str, Any]] = []

    for candidate in candidates.get("candidates", []):
        source = str(candidate.get("source") or "")
        target = str(candidate.get("target") or "")
        key = (source, target)
        if key not in CANDIDATE_ADJUDICATIONS:
            raise ValueError(f"missing Candidate adjudication rule for {key}")
        if source not in rows_by_concept:
            raise ValueError(f"Candidate adjudication source row missing from review: {source}")
        if target not in rows_by_concept:
            raise ValueError(f"Candidate adjudication target row missing from review: {target}")
        if target not in approved:
            raise ValueError(f"Candidate adjudication target outside approved parent whitelist: {source} -> {target}")

        spec = CANDIDATE_ADJUDICATIONS[key]
        row = rows_by_concept[source]
        target_row = rows_by_concept[target]
        decision = spec["decision"]
        writeback_action = spec["writeback_action"]
        review_status = spec["review_status"]
        record = {
            "source": source,
            "source_path": row["path"],
            "target": target,
            "target_path": target_row["path"],
            "candidate_type": candidate.get("candidate_type"),
            "candidate_status_before_adjudication": candidate.get("status"),
            "candidate_basis": {
                "support": candidate.get("support") or [],
                "evidence_excerpt": candidate.get("evidence_excerpt") or [],
                "rationale": candidate.get("rationale") or "",
                "confidence_before_adjudication": candidate.get("confidence") or "",
            },
            "decision": decision,
            "decision_reason": spec["decision_reason"],
            "strict_taxonomy_test": spec["strict_taxonomy_test"],
            "writeback_action": writeback_action,
            "proposed_field": "up" if writeback_action == "add_up" else None,
            "review_status": review_status,
            "dry_run_eligible": decision == "accept_taxonomy" and writeback_action == "add_up",
            "concept_card_writes_in_adjudication": 0,
            "reviewed_at": generated_at,
            "reviewer": "llm-adjudicator:concept-hierarchy-audit-candidate-adjudication",
            "evidence": build_candidate_evidence(row, target_row, spec),
            "drift_guard": spec["drift_guard"],
        }
        records.append(record)

        row["decision"] = decision
        row["decision_reason"] = spec["decision_reason"]
        row["review_status"] = review_status
        row["reviewed_at"] = generated_at
        row["reviewer"] = "llm-adjudicator:concept-hierarchy-audit-candidate-adjudication"
        row["writeback_action"] = "none"
        row["drift_guard"] = sorted(set((row.get("drift_guard") or []) + spec["drift_guard"]))
        row["candidate_taxonomy"] = [
            {
                "target": target,
                "decision": decision,
                "decision_reason": spec["decision_reason"],
                "strict_taxonomy_test": spec["strict_taxonomy_test"],
                "writeback_action": writeback_action,
                "review_status": review_status,
                "dry_run_eligible": record["dry_run_eligible"],
                "reviewed_at": generated_at,
            }
        ]
        for candidate_generation_candidate in row.get("candidate_generation_taxonomy", []):
            if candidate_generation_candidate.get("target") == target:
                candidate_generation_candidate["adjudication_decision"] = decision
                candidate_generation_candidate["adjudication_review_status"] = review_status
                candidate_generation_candidate["adjudication_writeback_action"] = writeback_action

    decision_counts = Counter(record["decision"] for record in records)
    action_counts = Counter(record["writeback_action"] for record in records)
    return {
        "schema_version": 1,
        "artifact_type": "taxonomy_placement_candidate_adjudication",
        "generated_at": generated_at,
        "input_review": rel(REVIEW_JSON),
        "input_candidates": rel(CANDIDATES_JSON),
        "classification_stage": "candidate_adjudication",
        "policy": {
            "batch_scope": "Adjudicate the Conservative candidate generation conservative candidates only; do not reopen all parentless cards.",
            "strict_taxonomy_rule": "`up` means kind-of / belongs-to only; component, control-point-in, supports, standardizes, executes, protects, or adjacency remains non-taxonomy.",
            "write_policy": "No concept cards are edited in Candidate adjudication. Accepted rows become dry-run eligible for Writeback dry-run only.",
            "dry_run_gate": "Only decision=accept_taxonomy and writeback_action=add_up may enter Writeback dry-run.",
        },
        "summary": {
            "input_candidates": len(candidates.get("candidates", [])),
            "adjudicated_candidates": len(records),
            "accept_taxonomy": decision_counts.get("accept_taxonomy", 0),
            "reject_taxonomy": decision_counts.get("reject_taxonomy", 0),
            "defer_boundary_review": decision_counts.get("defer_boundary_review", 0),
            "ready_for_dry_run": sum(1 for record in records if record["dry_run_eligible"]),
            "terminal_non_writeback": sum(1 for record in records if record["review_status"] == "terminal_non_writeback"),
            "writeback_actions": dict(sorted(action_counts.items())),
            "concept_card_writes": 0,
            "dry_run_planned": 0,
        },
        "decisions": records,
    }


def apply_candidate_adjudication(review: dict[str, Any]) -> dict[str, Any]:
    if review.get("classification_stage") != "conservative_candidates":
        apply_conservative_candidates(review)

    candidates = build_conservative_candidates(review)
    adjudication = build_candidate_adjudication(review, candidates)
    generated_at = adjudication["generated_at"]
    review["classification_stage"] = "candidate_adjudication"
    review["generated_at"] = generated_at
    review["scope"]["write_policy"] = (
        "Candidate adjudication only. Accepted rows are dry-run eligible, but concept cards still must not be edited "
        "until Writeback dry-run and a later limited apply."
    )
    review["candidate_adjudication"] = {
        "generated_at": generated_at,
        "adjudication_artifact_json": rel(ADJUDICATION_JSON),
        "adjudication_artifact_md": rel(ADJUDICATION_MD),
        "summary": adjudication["summary"],
        "accepted_for_dry_run": [
            {"source": r["source"], "target": r["target"]}
            for r in adjudication["decisions"]
            if r["dry_run_eligible"]
        ],
        "rejected_as_non_taxonomy": [
            {"source": r["source"], "target": r["target"], "reason": r["decision_reason"]}
            for r in adjudication["decisions"]
            if r["decision"] == "reject_taxonomy"
        ],
    }
    recompute_summary(review)
    review["summary"].update(
        {
            "write_policy": review["scope"]["write_policy"],
            "adjudicated_candidates": adjudication["summary"]["adjudicated_candidates"],
            "adjudication_accept_taxonomy": adjudication["summary"]["accept_taxonomy"],
            "adjudication_reject_taxonomy": adjudication["summary"]["reject_taxonomy"],
            "adjudication_defer_boundary_review": adjudication["summary"]["defer_boundary_review"],
            "adjudication_ready_for_dry_run": adjudication["summary"]["ready_for_dry_run"],
            "adjudication_concept_card_writes": 0,
            "open_writeback": 0,
            "dry_run_planned": 0,
        }
    )
    review["audit_sets"]["adjudication_accepted_for_dry_run"] = [
        r["source"] for r in adjudication["decisions"] if r["dry_run_eligible"]
    ]
    review["audit_sets"]["adjudication_rejected_non_taxonomy"] = [
        r["source"] for r in adjudication["decisions"] if r["decision"] == "reject_taxonomy"
    ]
    validate_review(review, load_json(MAP_JSON))
    return adjudication


def taxonomy_link(title: str) -> str:
    return f"[[{title}]]"


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def clean_frontmatter_link(value: Any) -> str | None:
    if value is None or isinstance(value, dict):
        return None
    text = str(value).strip().strip('"').strip("'")
    match = WIKILINK_RE.search(text)
    if match:
        text = match.group(1)
    text = text.split("|")[0].split("#")[0].strip()
    if "/" in text:
        text = Path(text).stem
    return text or None


def load_frontmatter(path: Path) -> tuple[dict[str, Any], str, str]:
    text = path.read_text(encoding="utf-8")
    match = FM_RE.match(text)
    if not match:
        raise ValueError(f"{rel(path)} has no YAML frontmatter")
    raw = match.group(1)
    return yaml.safe_load(raw) or {}, raw, text[match.end():]


def current_up_from_file(path: Path) -> list[str]:
    fm, _raw, _body = load_frontmatter(path)
    return [x for x in (clean_frontmatter_link(v) for v in as_list(fm.get("up"))) if x]


def frontmatter_block_end(lines: list[str], start: int) -> int:
    index = start + 1
    while index < len(lines) and (not lines[index].strip() or not TOP_LEVEL_RE.match(lines[index])):
        index += 1
    return index


def frontmatter_insert_index(lines: list[str]) -> int:
    preferred_after = ["related", "evidence", "source", "freshness", "last_checked", "updated"]
    last: int | None = None
    for field in preferred_after:
        for index, line in enumerate(lines):
            if line.startswith(f"{field}:"):
                last = frontmatter_block_end(lines, index)
    if last is not None:
        return last
    return len(lines)


def set_frontmatter_updated(lines: list[str]) -> list[str]:
    current = today()
    for index, line in enumerate(lines):
        if line.startswith("updated:"):
            lines[index] = f"updated: {current}"
            return lines
    for index, line in enumerate(lines):
        if line.startswith("created:"):
            lines.insert(index + 1, f"updated: {current}")
            return lines
    lines.insert(0, f"updated: {current}")
    return lines


def add_up_to_concept_file(path: Path, target: str) -> str:
    fm, raw, body = load_frontmatter(path)
    current_up = [x for x in (clean_frontmatter_link(v) for v in as_list(fm.get("up"))) if x]
    if target in current_up:
        return "already_present"
    if current_up:
        raise ValueError(f"{rel(path)} already has up={current_up}; refusing to create a multi-parent edge")

    lines = set_frontmatter_updated(raw.splitlines())
    insert_at = frontmatter_insert_index(lines)
    block = ["up:", f"  - \"[[{target}]]\""]
    if insert_at > 0 and lines[insert_at - 1].strip():
        block = [""] + block
    if insert_at < len(lines) and lines[insert_at].strip():
        block = block + [""]
    lines[insert_at:insert_at] = block
    path.write_text("---\n" + "\n".join(lines).rstrip() + "\n---\n" + body, encoding="utf-8")
    return "applied"


def build_writeback_dry_run(review: dict[str, Any], adjudication: dict[str, Any]) -> dict[str, Any]:
    """Create the concept hierarchy audit Writeback dry-run taxonomy writeback dry-run artifact.

    Writeback dry-run is deliberately still report-only: it proves which Candidate adjudication accepted
    rows would be written later, but it never edits concept-card files.
    """
    generated_at = utc_now()
    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    approved = approved_parent_names(review)
    planned: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []

    for decision in adjudication.get("decisions", []):
        source = str(decision.get("source") or "")
        target = str(decision.get("target") or "")
        eligible = (
            decision.get("decision") == "accept_taxonomy"
            and decision.get("writeback_action") == "add_up"
            and decision.get("dry_run_eligible") is True
            and decision.get("proposed_field") == "up"
        )
        if not eligible:
            excluded.append(
                {
                    "source": source,
                    "target": target,
                    "decision": decision.get("decision"),
                    "writeback_action": decision.get("writeback_action"),
                    "review_status": decision.get("review_status"),
                    "reason": "Excluded from Writeback dry-run because it is not accept_taxonomy + add_up + proposed_field=up.",
                }
            )
            continue

        if target not in approved:
            raise ValueError(f"Writeback dry-run target outside approved stable parent whitelist: {source} -> {target}")
        if source not in rows_by_concept:
            raise ValueError(f"Writeback dry-run source row missing from review: {source}")
        if target not in rows_by_concept:
            raise ValueError(f"Writeback dry-run target row missing from review: {target}")

        row = rows_by_concept[source]
        target_row = rows_by_concept[target]
        source_file = ROOT / str(row.get("path") or "")
        target_file = ROOT / str(target_row.get("path") or "")
        if not source_file.exists():
            raise ValueError(f"Writeback dry-run source concept file missing: {source_file}")
        if not target_file.exists():
            raise ValueError(f"Writeback dry-run target concept file missing: {target_file}")

        current_up = [str(x) for x in row.get("current_up") or [] if str(x)]
        if current_up:
            raise ValueError(
                f"Writeback dry-run refuses to plan an add_up for {source}: current_up already exists {current_up}"
            )

        planned.append(
            {
                "source": source,
                "target": target,
                "source_file": rel(source_file),
                "target_file": rel(target_file),
                "decision": decision.get("decision"),
                "writeback_action": decision.get("writeback_action"),
                "proposed_field": decision.get("proposed_field"),
                "status": "ready",
                "current_up": current_up,
                "proposed_write": {"up": [taxonomy_link(target)]},
                "decision_reason": decision.get("decision_reason"),
                "strict_taxonomy_test": decision.get("strict_taxonomy_test"),
                "evidence": decision.get("evidence") or [],
                "drift_guard": decision.get("drift_guard") or [],
                "concept_card_writes_in_writeback_dry_run": 0,
            }
        )

    ready = sum(1 for item in planned if item.get("status") == "ready")
    excluded_rejected = sum(1 for item in excluded if item.get("decision") == "reject_taxonomy")
    return {
        "schema_version": 1,
        "artifact_type": "taxonomy_placement_writeback_dry_run",
        "generated_at": generated_at,
        "input_review": rel(REVIEW_JSON),
        "input_adjudication": rel(ADJUDICATION_JSON),
        "classification_stage": "writeback_dry_run",
        "policy": {
            "dry_run_only": True,
            "allowed_input": "Only Candidate adjudication decisions with decision=accept_taxonomy, writeback_action=add_up, dry_run_eligible=true, and proposed_field=up.",
            "write_policy": "No concept cards are edited in Writeback dry-run. This artifact only proves the later limited apply set.",
            "field_policy": "Only child-card top-level `up` may be planned; never add `down`, `children`, Juggl fields, or Breadcrumbs mirror fields.",
            "non_taxonomy_policy": "Rejected/control-point/support/execute/standardize/component/adjacency rows remain excluded even if they are conceptually important.",
        },
        "summary": {
            "input_adjudicated": len(adjudication.get("decisions", [])),
            "accepted_add_up_candidates": len(planned),
            "planned": len(planned),
            "ready": ready,
            "blocked": len(planned) - ready,
            "excluded_candidates": len(excluded),
            "excluded_rejected_candidates": excluded_rejected,
            "excluded_non_writeback_candidates": len(excluded) - excluded_rejected,
            "concept_card_writes": 0,
            "applied": 0,
        },
        "planned": planned,
        "excluded": excluded,
        "applied": [],
    }


def validate_writeback_dry_run(dry_run: dict[str, Any], review: dict[str, Any], adjudication: dict[str, Any]) -> None:
    if dry_run.get("artifact_type") != "taxonomy_placement_writeback_dry_run":
        raise ValueError("Writeback dry-run artifact_type mismatch")
    if dry_run.get("classification_stage") != "writeback_dry_run":
        raise ValueError("Writeback dry-run classification_stage mismatch")
    summary = dry_run.get("summary") or {}
    if summary.get("concept_card_writes") != 0 or dry_run.get("applied"):
        raise ValueError("Writeback dry-run must not edit or apply concept cards")

    rows_by_concept = {row["concept"]: row for row in review.get("rows", [])}
    approved = approved_parent_names(review)
    eligible = {
        (item.get("source"), item.get("target"))
        for item in adjudication.get("decisions", [])
        if item.get("decision") == "accept_taxonomy"
        and item.get("writeback_action") == "add_up"
        and item.get("dry_run_eligible") is True
        and item.get("proposed_field") == "up"
    }
    rejected = {
        (item.get("source"), item.get("target"))
        for item in adjudication.get("decisions", [])
        if item.get("decision") == "reject_taxonomy"
    }
    planned = {(item.get("source"), item.get("target")) for item in dry_run.get("planned", [])}
    if planned != eligible:
        raise ValueError(f"Writeback dry-run planned rows mismatch eligible={sorted(eligible)} planned={sorted(planned)}")
    if planned & rejected:
        raise ValueError(f"Writeback dry-run planned rejected rows: {sorted(planned & rejected)}")
    if summary.get("planned") != len(planned) or summary.get("ready") != len(planned):
        raise ValueError("Writeback dry-run planned/ready summary mismatch")
    if summary.get("excluded_rejected_candidates") != len(rejected):
        raise ValueError("Writeback dry-run excluded rejected-candidate summary mismatch")

    for item in dry_run.get("planned", []):
        source = str(item.get("source") or "")
        target = str(item.get("target") or "")
        if target not in approved:
            raise ValueError(f"Writeback dry-run planned target outside approved whitelist: {source} -> {target}")
        if source not in rows_by_concept:
            raise ValueError(f"Writeback dry-run planned source missing from review: {source}")
        if rows_by_concept[source].get("current_up"):
            raise ValueError(f"Writeback dry-run planned source already has current_up: {source}")
        if item.get("decision") != "accept_taxonomy":
            raise ValueError(f"Writeback dry-run planned non-accepted row: {source} -> {target}")
        if item.get("writeback_action") != "add_up" or item.get("proposed_field") != "up":
            raise ValueError(f"Writeback dry-run planned row has invalid writeback target: {source} -> {target}")
        if item.get("status") != "ready":
            raise ValueError(f"Writeback dry-run planned row is not ready: {source} -> {target}")
        if item.get("proposed_write") != {"up": [taxonomy_link(target)]}:
            raise ValueError(f"Writeback dry-run proposed_write mismatch: {source} -> {target}")
        for key in ("source_file", "target_file"):
            file_path = ROOT / str(item.get(key) or "")
            if not file_path.exists():
                raise ValueError(f"Writeback dry-run planned {key} missing: {file_path}")


def apply_writeback_dry_run(review: dict[str, Any], adjudication: dict[str, Any] | None = None) -> dict[str, Any]:
    if review.get("classification_stage") != "candidate_adjudication":
        adjudication = apply_candidate_adjudication(review)
    if adjudication is None:
        if not ADJUDICATION_JSON.exists():
            raise ValueError("Writeback dry-run requires Candidate adjudication artifact")
        adjudication = load_json(ADJUDICATION_JSON)

    dry_run = build_writeback_dry_run(review, adjudication)
    generated_at = dry_run["generated_at"]
    review["classification_stage"] = "writeback_dry_run"
    review["generated_at"] = generated_at
    review["scope"]["write_policy"] = (
        "Writeback dry-run only. Only Candidate adjudication accept_taxonomy + add_up rows are planned; "
        "concept cards still must not be edited until a later limited apply."
    )
    review["writeback_dry_run"] = {
        "generated_at": generated_at,
        "dry_run_artifact_json": rel(WRITEBACK_DRY_RUN_JSON),
        "dry_run_artifact_md": rel(WRITEBACK_DRY_RUN_MD),
        "summary": dry_run["summary"],
        "planned_up": [
            {"source": item["source"], "target": item["target"], "status": item["status"]}
            for item in dry_run["planned"]
        ],
        "excluded_non_writeback": [
            {"source": item["source"], "target": item["target"], "decision": item["decision"]}
            for item in dry_run["excluded"]
        ],
    }

    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    for item in dry_run["planned"]:
        row = rows_by_concept[item["source"]]
        row["writeback_dry_run"] = {
            "target": item["target"],
            "status": item["status"],
            "proposed_write": item["proposed_write"],
            "dry_run_artifact_json": rel(WRITEBACK_DRY_RUN_JSON),
            "concept_card_writes_in_writeback_dry_run": 0,
        }

    recompute_summary(review)
    review["summary"].update(
        {
            "write_policy": review["scope"]["write_policy"],
            "writeback_dry_run_planned": dry_run["summary"]["planned"],
            "writeback_dry_run_ready": dry_run["summary"]["ready"],
            "writeback_dry_run_rejected_rows_excluded": dry_run["summary"]["excluded_rejected_candidates"],
            "writeback_dry_run_non_writeback_rows_excluded": dry_run["summary"]["excluded_non_writeback_candidates"],
            "writeback_dry_run_concept_card_writes": 0,
            "open_writeback": 0,
            "dry_run_planned": dry_run["summary"]["planned"],
        }
    )
    review["audit_sets"]["writeback_dry_run_planned"] = [item["source"] for item in dry_run["planned"]]
    review["audit_sets"]["writeback_dry_run_excluded_non_writeback"] = [item["source"] for item in dry_run["excluded"]]
    validate_writeback_dry_run(dry_run, review, adjudication)
    return dry_run


def build_limited_apply_report(dry_run: dict[str, Any], limit: int) -> dict[str, Any]:
    if limit <= 0:
        raise ValueError("Limited apply requires --limit greater than 0")
    if dry_run.get("artifact_type") != "taxonomy_placement_writeback_dry_run":
        raise ValueError("Limited apply input must be concept-hierarchy-placement Writeback dry-run")

    generated_at = utc_now()
    planned = [item for item in dry_run.get("planned", []) if item.get("status") == "ready"]
    selected = planned[:limit]
    unselected = planned[limit:]
    applied_rows: list[dict[str, Any]] = []
    skipped_rows: list[dict[str, Any]] = []

    for item in selected:
        source = str(item.get("source") or "")
        target = str(item.get("target") or "")
        if not source or not target:
            raise ValueError(f"Limited apply selected row missing source/target: {item}")
        if item.get("decision") != "accept_taxonomy" or item.get("writeback_action") != "add_up":
            raise ValueError(f"Limited apply selected row is not accepted add_up: {source} -> {target}")
        if item.get("proposed_field") != "up":
            raise ValueError(f"Limited apply selected row targets non-up field: {source} -> {target}")
        if (source, target) in FORBIDDEN_UP_PAIRS or (source, target) in NON_TAXONOMY_BOUNDARIES:
            raise ValueError(f"Limited apply refuses forbidden/non-taxonomy up pair: {source} -> {target}")

        source_file = ROOT / str(item.get("source_file") or "")
        target_file = ROOT / str(item.get("target_file") or "")
        if not source_file.exists():
            raise ValueError(f"Limited apply source file missing: {source_file}")
        if not target_file.exists():
            raise ValueError(f"Limited apply target file missing: {target_file}")

        current_up = current_up_from_file(source_file)
        if current_up and target not in current_up:
            raise ValueError(
                f"Limited apply refuses to create multi-parent up for {source}: current_up={current_up}, target={target}"
            )
        result = add_up_to_concept_file(source_file, target)
        row = {
            **item,
            "result": result,
            "current_up_before_apply": current_up,
            "current_up_after_apply": current_up_from_file(source_file),
            "applied_at": generated_at,
        }
        if result in {"applied", "already_present"}:
            applied_rows.append(row)
        else:
            skipped_rows.append(row)

    return {
        "schema_version": 1,
        "artifact_type": "taxonomy_placement_apply_report",
        "generated_at": generated_at,
        "classification_stage": "limited_apply",
        "input_dry_run": rel(WRITEBACK_DRY_RUN_JSON),
        "policy": {
            "limited_apply_only": True,
            "limit": limit,
            "allowed_input": "Only Writeback dry-run rows with status=ready and Candidate adjudication accept_taxonomy/add_up may be applied.",
            "field_policy": "Write only child-card top-level `up`; do not write `down`, `children`, Juggl fields, or Breadcrumbs mirror fields.",
            "post_apply_policy": "Rebuild relation map and regenerate concept hierarchy placement review after apply; post-apply dry-run may be 0 planned when all accepted rows landed.",
        },
        "summary": {
            "input_dry_run_planned": len(dry_run.get("planned", [])),
            "input_dry_run_ready": len(planned),
            "selected": len(selected),
            "unselected_due_to_limit": len(unselected),
            "applied": sum(1 for item in applied_rows if item.get("result") == "applied"),
            "already_present": sum(1 for item in applied_rows if item.get("result") == "already_present"),
            "skipped": len(skipped_rows),
            "concept_card_writes": sum(1 for item in applied_rows if item.get("result") == "applied"),
            "limit": limit,
            "post_apply_dry_run_planned": None,
            "post_apply_dry_run_ready": None,
        },
        "planned": selected,
        "applied": applied_rows,
        "skipped": skipped_rows,
        "unselected_due_to_limit": unselected,
        "excluded_from_input_dry_run": dry_run.get("excluded", []),
    }




def neutralize_process_terms(value: Any) -> Any:
    """Remove ad-hoc process labels from existing report text/keys."""
    process_stage_re = re.compile(r"\b[Ss]tep\s*\d+\b")
    if isinstance(value, str):
        value = process_stage_re.sub("guarded review stage", value)
        value = value.replace("guarded review stage dry-run", "writeback dry-run")
        value = value.replace("guarded review stage apply", "limited apply")
        return value
    if isinstance(value, list):
        return [neutralize_process_terms(item) for item in value]
    if isinstance(value, dict):
        return {str(key): neutralize_process_terms(item) for key, item in value.items()}
    return value

def normalize_existing_apply_report(report: dict[str, Any]) -> dict[str, Any]:
    """Return a project-neutral apply report while preserving existing proof rows."""
    if report.get("artifact_type") != "taxonomy_placement_apply_report":
        return report
    report["classification_stage"] = "limited_apply"
    if isinstance(report.get("input_dry_run"), str):
        report["input_dry_run"] = rel(WRITEBACK_DRY_RUN_JSON)
    policy = report.setdefault("policy", {})
    if "allowed_input" in policy:
        policy["allowed_input"] = (
            "Only writeback dry-run rows with status=ready and candidate-adjudication "
            "accept_taxonomy/add_up may be applied."
        )
    if "post_apply_policy" in policy:
        policy["post_apply_policy"] = (
            "Rebuild the relation map and regenerate the concept hierarchy review after apply; "
            "post-apply dry-run may be 0 planned when all accepted rows landed."
        )
    legacy_report_prefix = "/".join(["legacy-runtime", "reports", "concept-card-relation-map"]) + "/"
    process_stage_re = re.compile(r"\b[Ss]tep\s*\d+\b")
    process_key_re = re.compile(r"concept_card_writes_in_" + r"s" + r"tep\d+")
    for section in ("planned", "applied", "skipped", "unselected_due_to_limit", "excluded_from_input_dry_run"):
        report[section] = neutralize_process_terms(report.get(section, []) or [])
        for row in report.get(section, []) or []:
            for key in list(row):
                if process_key_re.fullmatch(str(key)):
                    row.pop(key, None)
            if row.get("decision_reason"):
                reason = process_stage_re.sub("the guarded review stage", str(row["decision_reason"]))
                row["decision_reason"] = reason.replace("the guarded review stage dry-run", "writeback dry-run")
            for key in ("source_file", "target_file"):
                if isinstance(row.get(key), str):
                    row[key] = row[key].replace(legacy_report_prefix, "reports/concept-card-relation-map/")
    notes = report.get("notes")
    if isinstance(notes, list):
        report["notes"] = neutralize_process_terms(notes)
    return report


def load_existing_apply_report() -> dict[str, Any] | None:
    """Find an existing limited-apply proof, preferring the project-native path."""
    candidates = [LIMITED_APPLY_JSON, *sorted(OUT_DIR.glob("*-apply-report.json"))]
    seen: set[Path] = set()
    for path in candidates:
        if path in seen or not path.exists():
            continue
        seen.add(path)
        report = normalize_existing_apply_report(load_json(path))
        if report.get("artifact_type") == "taxonomy_placement_apply_report":
            return report
    return None

def attach_limited_apply(review: dict[str, Any], apply_report: dict[str, Any]) -> None:
    generated_at = utc_now()
    dry_run_review_summary = (review.get("writeback_dry_run") or {}).get("summary") or {}
    apply_report["summary"]["post_apply_dry_run_planned"] = dry_run_review_summary.get("planned")
    apply_report["summary"]["post_apply_dry_run_ready"] = dry_run_review_summary.get("ready")
    apply_report["post_apply_review"] = {
        "review_artifact_json": rel(REVIEW_JSON),
        "review_artifact_md": rel(REVIEW_MD),
        "classification_stage": "limited_apply",
        "concepts_with_up": review.get("summary", {}).get("concepts_with_up"),
        "concepts_without_up": review.get("summary", {}).get("concepts_without_up"),
        "post_apply_dry_run_planned": dry_run_review_summary.get("planned"),
        "post_apply_dry_run_ready": dry_run_review_summary.get("ready"),
    }

    review["classification_stage"] = "limited_apply"
    review["generated_at"] = generated_at
    review["scope"]["write_policy"] = (
        "Limited apply complete. Applied rows must be listed in concept-hierarchy-placement-apply-report; "
        "post-apply dry-run should be empty for rows already written."
    )
    review["limited_apply"] = {
        "generated_at": generated_at,
        "apply_artifact_json": rel(LIMITED_APPLY_JSON),
        "apply_artifact_md": rel(LIMITED_APPLY_MD),
        "summary": apply_report["summary"],
        "applied_up": [
            {
                "source": item["source"],
                "target": item["target"],
                "result": item["result"],
                "current_up_after_apply": item.get("current_up_after_apply") or [],
            }
            for item in apply_report.get("applied", [])
        ],
        "excluded_non_writeback": [
            {"source": item.get("source"), "target": item.get("target"), "decision": item.get("decision")}
            for item in apply_report.get("excluded_from_input_dry_run", [])
        ],
    }

    rows_by_concept = {row["concept"]: row for row in review["rows"]}
    for item in apply_report.get("applied", []):
        row = rows_by_concept.get(item.get("source"))
        if not row:
            continue
        row["limited_apply_applied_up"] = {
            "target": item.get("target"),
            "result": item.get("result"),
            "apply_artifact_json": rel(LIMITED_APPLY_JSON),
            "applied_at": item.get("applied_at"),
        }

    review["summary"].update(
        {
            "write_policy": review["scope"]["write_policy"],
            "limited_apply_input_dry_run_planned": apply_report["summary"]["input_dry_run_planned"],
            "limited_apply_selected": apply_report["summary"]["selected"],
            "limited_apply_applied": apply_report["summary"]["applied"],
            "limited_apply_already_present": apply_report["summary"]["already_present"],
            "limited_apply_skipped": apply_report["summary"]["skipped"],
            "limited_apply_concept_card_writes": apply_report["summary"]["concept_card_writes"],
            "limited_apply_post_apply_dry_run_planned": dry_run_review_summary.get("planned"),
            "limited_apply_post_apply_dry_run_ready": dry_run_review_summary.get("ready"),
            "open_writeback": 0,
            "dry_run_planned": dry_run_review_summary.get("planned", 0),
        }
    )
    review["audit_sets"]["limited_apply_applied_up"] = [item["source"] for item in apply_report.get("applied", [])]


def validate_limited_apply_report(apply_report: dict[str, Any], review: dict[str, Any]) -> None:
    if apply_report.get("artifact_type") != "taxonomy_placement_apply_report":
        raise ValueError("Limited apply artifact_type mismatch")
    if apply_report.get("classification_stage") != "limited_apply":
        raise ValueError("Limited apply classification_stage mismatch")
    summary = apply_report.get("summary") or {}
    applied = apply_report.get("applied") or []
    if summary.get("selected") != len(apply_report.get("planned") or []):
        raise ValueError("Limited apply selected/planned count mismatch")
    if summary.get("concept_card_writes") != sum(1 for item in applied if item.get("result") == "applied"):
        raise ValueError("Limited apply concept_card_writes mismatch")
    if summary.get("skipped") != len(apply_report.get("skipped") or []):
        raise ValueError("Limited apply skipped count mismatch")
    if review.get("summary", {}).get("limited_apply_post_apply_dry_run_planned") != summary.get("post_apply_dry_run_planned"):
        raise ValueError("Limited apply post-apply dry-run summary mismatch")

    for item in applied:
        source = str(item.get("source") or "")
        target = str(item.get("target") or "")
        if not source or not target:
            raise ValueError(f"Limited apply applied row missing source/target: {item}")
        if (source, target) in FORBIDDEN_UP_PAIRS or (source, target) in NON_TAXONOMY_BOUNDARIES:
            raise ValueError(f"Limited apply applied forbidden/non-taxonomy pair: {source} -> {target}")
        source_file = ROOT / str(item.get("source_file") or "")
        if not source_file.exists():
            raise ValueError(f"Limited apply applied source file missing: {source_file}")
        current_up = current_up_from_file(source_file)
        if target not in current_up:
            raise ValueError(f"Limited apply applied target missing from source up: {source} -> {target}")
        fm, _raw, _body = load_frontmatter(source_file)
        if "down" in fm:
            raise ValueError(f"Limited apply source has manual down field: {source}")
        if "children" in fm:
            raise ValueError(f"Limited apply source has manual children field: {source}")


def audit_closure_completion_checks(review: dict[str, Any], plugin_summary: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return the Audit closure whole-audit completion checks.

    ``defer_boundary_review`` may remain as the semantic decision, but every
    such row must have ``review_status=deferred_with_backlog`` so it is no
    longer an open tail or a hidden request to invent a parent.
    """
    summary = review.get("summary") or {}
    rows = review.get("rows") or []
    deferred_rows = [row for row in rows if row.get("decision") == "defer_boundary_review"]
    checks: dict[str, Any] = {
        "all_concepts_reviewed": summary.get("reviewed_concepts") == summary.get("total_concepts"),
        "taxonomy_placement_unreviewed_zero": summary.get("taxonomy_placement_unreviewed") == 0,
        "open_unclassified_zero": summary.get("open_unclassified") == 0,
        "open_review_zero": summary.get("open_review") == 0,
        "open_writeback_zero": summary.get("open_writeback") == 0,
        "deferred_rows_have_backlog": summary.get("defer_boundary_review") == 0
        or all(row.get("review_status") == "deferred_with_backlog" for row in deferred_rows),
        "dry_run_planned_zero": summary.get("dry_run_planned") == 0,
    }
    if plugin_summary is not None:
        checks["plugin_problems_zero"] = plugin_summary.get("problems") == 0
        checks["forbidden_up_edges_zero"] = plugin_summary.get("forbidden_up_edges") == 0
    return {
        "checks": checks,
        "met": all(value is True for value in checks.values()),
    }


def apply_audit_closure(review: dict[str, Any]) -> dict[str, Any]:
    """Close remaining concept-hierarchy-placement open reviews into backlog-backed defers.

    Audit closure is intentionally not another parent-generation stage. It records
    that the remaining parentless cards have been considered and that each
    unresolved boundary now has a durable backlog/health-check home.
    """
    if review.get("classification_stage") != "limited_apply":
        raise ValueError("Audit closure requires a Limited apply post-apply review state")

    generated_at = utc_now()
    closure_records: list[dict[str, Any]] = []
    for row in sorted(review.get("rows", []), key=lambda item: str(item.get("concept") or "")):
        if row.get("decision") != "defer_boundary_review":
            continue
        concept = str(row.get("concept") or "")
        precheck = DEFERRED_PARENT_ROUTE_PRECHECK.get(concept, {})
        suppressed = SUPPRESSED_DEFERRED_SIGNALS.get(concept, {})
        backlog_record = {
            "status": "deferred_with_backlog",
            "backlog_home": AUDIT_BACKLOG_HOME,
            "reason": precheck.get(
                "reason",
                "No approved strict parent exists in the current concept hierarchy placement pass.",
            ),
            "suppressed_target": suppressed.get("suppressed_target"),
            "suppressed_signal_type": suppressed.get("signal_type"),
            "suppressed_reason": suppressed.get("reason"),
            "writeback_action": "none",
            "reopen_triggers": [
                "A narrower canonical parent concept card is created and added to the approved parent whitelist.",
                "The concept card's own definition/evidence changes enough to prove a strict kind-of relation.",
                "A future user request explicitly starts a new candidate/adjudication/dry-run/limited-apply cycle for this boundary.",
            ],
        }
        row["review_status"] = "deferred_with_backlog"
        row["reviewed_at"] = generated_at
        row["reviewer"] = "llm-adjudicator:concept-hierarchy-audit-closure"
        row["writeback_action"] = "none"
        row["audit_closure_deferred_backlog"] = backlog_record
        row["decision_reason"] = (
            f"{row.get('decision_reason') or 'No safe strict parent was proven.'} "
            "Audit closure keeps the card parentless for now and routes the unresolved boundary to the health-check backlog instead of forcing `up`."
        )
        guard_items = [
            "Audit closure is not permission to write a fallback parent later; reopen through candidate/adjudication/dry-run/limited-apply.",
            f"Backlog home: {AUDIT_BACKLOG_HOME}",
        ]
        if suppressed.get("reason"):
            guard_items.append(str(suppressed["reason"]))
        row["drift_guard"] = sorted(set((row.get("drift_guard") or []) + guard_items))
        closure_records.append(
            {
                "concept": concept,
                "path": row.get("path"),
                **backlog_record,
            }
        )

    plugin_summary = load_json(PLUGIN_JSON).get("summary", {}) if PLUGIN_JSON.exists() else None
    review["classification_stage"] = "audit_closure"
    review["generated_at"] = generated_at
    review["scope"]["write_policy"] = (
        "Audit closure only. Remaining defer_boundary_review rows are closed as "
        "deferred_with_backlog and no concept-card fields are written."
    )
    recompute_summary(review)
    completion = audit_closure_completion_checks(review, plugin_summary)
    closure = {
        "schema_version": 1,
        "artifact_type": "taxonomy_placement_audit_closure",
        "generated_at": generated_at,
        "input_review": rel(REVIEW_JSON),
        "classification_stage": "audit_closure",
        "backlog_home": AUDIT_BACKLOG_HOME,
        "policy": {
            "completion_target": "Close open review tails without forcing parents.",
            "strict_taxonomy_rule": "`up` remains strict kind-of / belongs-to only.",
            "deferred_status_rule": "A remaining defer_boundary_review row is closed only when review_status=deferred_with_backlog and a backlog home is recorded.",
            "write_policy": "No concept cards are edited in Audit closure.",
        },
        "summary": {
            "total_concepts": review["summary"].get("total_concepts"),
            "reviewed_concepts": review["summary"].get("reviewed_concepts"),
            "taxonomy_placement_unreviewed": review["summary"].get("taxonomy_placement_unreviewed"),
            "open_unclassified": review["summary"].get("open_unclassified"),
            "open_review_after_closure": review["summary"].get("open_review"),
            "open_writeback": review["summary"].get("open_writeback"),
            "dry_run_planned": review["summary"].get("dry_run_planned"),
            "defer_boundary_review": review["summary"].get("defer_boundary_review"),
            "deferred_with_backlog": len(closure_records),
            "concept_card_writes": 0,
            "plugin_problems": None if plugin_summary is None else plugin_summary.get("problems"),
            "forbidden_up_edges": None if plugin_summary is None else plugin_summary.get("forbidden_up_edges"),
            "completion_definition_met": completion["met"],
        },
        "completion_definition": completion,
        "deferred_with_backlog": closure_records,
    }
    review["audit_closure"] = {
        "generated_at": generated_at,
        "closure_artifact_json": rel(AUDIT_CLOSURE_JSON),
        "closure_artifact_md": rel(AUDIT_CLOSURE_MD),
        "backlog_home": AUDIT_BACKLOG_HOME,
        "summary": closure["summary"],
        "deferred_with_backlog": [
            {
                "concept": item["concept"],
                "suppressed_target": item.get("suppressed_target"),
                "suppressed_signal_type": item.get("suppressed_signal_type"),
                "reason": item.get("reason"),
            }
            for item in closure_records
        ],
    }
    review["summary"].update(
        {
            "write_policy": review["scope"]["write_policy"],
            "deferred_with_backlog": len(closure_records),
            "audit_closure_concept_card_writes": 0,
            "completion_definition_met": completion["met"],
            "open_writeback": 0,
            "dry_run_planned": 0,
        }
    )
    review["audit_sets"]["deferred_with_backlog"] = [item["concept"] for item in closure_records]
    validate_audit_closure(closure, review)
    return closure


def validate_audit_closure(closure: dict[str, Any], review: dict[str, Any]) -> None:
    if closure.get("artifact_type") != "taxonomy_placement_audit_closure":
        raise ValueError("Audit closure artifact_type mismatch")
    if closure.get("classification_stage") != "audit_closure":
        raise ValueError("Audit closure classification_stage mismatch")
    if review.get("classification_stage") != "audit_closure":
        raise ValueError("Audit closure review classification_stage mismatch")
    rows = review.get("rows", [])
    deferred_rows = [row for row in rows if row.get("decision") == "defer_boundary_review"]
    backlog_rows = [row for row in deferred_rows if row.get("review_status") == "deferred_with_backlog"]
    if len(backlog_rows) != len(deferred_rows):
        raise ValueError("Audit closure deferred rows must all have review_status=deferred_with_backlog")
    for row in backlog_rows:
        backlog = row.get("audit_closure_deferred_backlog")
        if not isinstance(backlog, dict) or backlog.get("backlog_home") != AUDIT_BACKLOG_HOME:
            raise ValueError(f"Audit closure deferred row missing backlog home: {row.get('concept')}")
        if row.get("writeback_action") != "none":
            raise ValueError(f"Audit closure deferred row scheduled writeback: {row.get('concept')}")
    summary = closure.get("summary") or {}
    review_summary = review.get("summary") or {}
    if summary.get("deferred_with_backlog") != len(backlog_rows):
        raise ValueError("Audit closure deferred_with_backlog summary mismatch")
    if summary.get("open_review_after_closure") != 0 or review_summary.get("open_review") != 0:
        raise ValueError("Audit closure must leave open_review at 0")
    if summary.get("open_writeback") != 0 or review_summary.get("open_writeback") != 0:
        raise ValueError("Audit closure must leave open_writeback at 0")
    if summary.get("dry_run_planned") != 0 or review_summary.get("dry_run_planned") != 0:
        raise ValueError("Audit closure must leave dry_run_planned at 0")
    if summary.get("concept_card_writes") != 0 or review_summary.get("audit_closure_concept_card_writes") != 0:
        raise ValueError("Audit closure must not edit concept cards")
    completion = closure.get("completion_definition") or {}
    checks = completion.get("checks") or {}
    if not completion.get("met") or not all(value is True for value in checks.values()):
        raise ValueError(f"Audit closure completion definition not met: {checks}")


def recompute_summary(review: dict[str, Any]) -> None:
    rows = review["rows"]
    decision_counts = Counter(row["decision"] for row in rows)
    review_status_counts = Counter(row["review_status"] for row in rows)
    with_up = [row for row in rows if row["current_up"]]
    without_up = [row for row in rows if not row["current_up"]]
    with_candidates = [row for row in rows if row["candidate_basis"]]
    forbidden_candidate_pairs = [
        {"source": row["concept"], "target": item["target"], "candidate_type": item["candidate_type"]}
        for row in rows
        for item in row["candidate_basis"]
        if item.get("known_forbidden_as_up")
    ]

    review["summary"].update(
        {
            "reviewed_concepts": sum(1 for row in rows if row["decision"] != "unreviewed"),
            "taxonomy_placement_unreviewed": decision_counts.get("unreviewed", 0),
            "concepts_with_up": len(with_up),
            "concepts_without_up": len(without_up),
            "concepts_with_candidate_basis": len(with_candidates),
            "candidate_basis_rows": sum(len(row["candidate_basis"]) for row in rows),
            "known_forbidden_candidate_pairs": len(forbidden_candidate_pairs),
            "decision_counts": dict(sorted(decision_counts.items())),
            "review_status_counts": dict(sorted(review_status_counts.items())),
            "accepted_taxonomy": decision_counts.get("accept_taxonomy", 0),
            "root_or_anchor_no_up": decision_counts.get("root_or_anchor_no_up", 0),
            "relation_only_terminal": decision_counts.get("relation_only_terminal", 0),
            "weak_or_backlog_terminal": decision_counts.get("weak_or_backlog_terminal", 0),
            "defer_boundary_review": decision_counts.get("defer_boundary_review", 0),
            "open_unclassified": decision_counts.get("unreviewed", 0),
            "open_review": review_status_counts.get("open", 0),
            "open_writeback": sum(1 for row in rows if row["writeback_action"] != "none"),
            "dry_run_planned": 0,
            "write_policy": "No writeback in Initial triage; decisions only route cards for later whitelist/candidate/adjudication work.",
        }
    )
    review["audit_sets"].update(
        {
            "concepts_with_up": [row["concept"] for row in with_up],
            "concepts_without_up": [row["concept"] for row in without_up],
            "concepts_with_candidate_basis": [row["concept"] for row in with_candidates],
            "known_forbidden_candidate_pairs": forbidden_candidate_pairs,
            "by_decision": {
                decision: [row["concept"] for row in rows if row["decision"] == decision]
                for decision in sorted(decision_counts)
            },
        }
    )


def build_review(map_data: dict[str, Any], classify_initial_triage_rows: bool = False) -> dict[str, Any]:
    nodes = sorted(map_data.get("nodes", []), key=lambda n: str(n.get("id") or n.get("title") or ""))
    edges = map_data.get("edges", [])
    candidates = map_data.get("candidate_edges", [])
    by_source_edges = edge_indexes(edges)
    by_source_candidates = candidate_indexes(candidates)
    node_ids = {str(node.get("id")) for node in nodes}

    rows: list[dict[str, Any]] = []
    for node in nodes:
        concept = str(node.get("id") or node.get("title") or "")
        current_up = [str(x) for x in (node.get("up") or []) if str(x)]
        typed_edges = by_source_edges[concept].get("typed_relation", [])
        related_edges = by_source_edges[concept].get("related_link", [])
        body_edges = by_source_edges[concept].get("body_link", [])
        basis = candidate_basis_for(concept, by_source_candidates.get(concept, []))
        row = {
            "concept": concept,
            "title": node.get("title") or concept,
            "path": node.get("file") or f"agentic learning/wiki/concepts/{concept}.md",
            "topics": node.get("topics") or [],
            "card_status": node.get("status") or "",
            "current_up": current_up,
            "current_relations_count": len(typed_edges),
            "current_relations": [
                {
                    "type": edge.get("relation_type"),
                    "target": edge.get("target"),
                    "note": edge.get("note") or "",
                }
                for edge in typed_edges
            ],
            "current_related_count": len(related_edges),
            "body_link_count": len(body_edges),
            "candidate_parent": choose_candidate_parent(basis),
            "candidate_basis": basis,
            "decision": "unreviewed",
            "decision_reason": "",
            "writeback_action": "none",
            "review_status": "open",
            "reviewed_at": None,
            "reviewer": "unassigned",
            "drift_guard": drift_guards_for(concept, basis),
        }
        rows.append(row)

    decision_counts = Counter(row["decision"] for row in rows)
    review_status_counts = Counter(row["review_status"] for row in rows)
    with_up = [row for row in rows if row["current_up"]]
    without_up = [row for row in rows if not row["current_up"]]
    with_candidates = [row for row in rows if row["candidate_basis"]]
    forbidden_candidate_pairs = [
        {"source": row["concept"], "target": item["target"], "candidate_type": item["candidate_type"]}
        for row in rows
        for item in row["candidate_basis"]
        if item.get("known_forbidden_as_up")
    ]

    review = {
        "schema_version": 1,
        "artifact_type": "taxonomy_placement_review",
        "generated_at": utc_now(),
        "classification_stage": "inventory",
        "input_map": rel(MAP_JSON),
        "scope": {
            "concept_dir": map_data.get("scope", {}).get("concept_dir", "agentic learning/wiki/concepts"),
            "temporary": True,
            "write_policy": "Inventory only. Do not edit concept cards or write up from this artifact without later adjudication + dry-run.",
            "accepted_name": "层级归属待审计概念卡",
        },
        "decision_vocabulary": sorted(DECISIONS),
        "review_status_vocabulary": sorted(REVIEW_STATUSES),
        "stable_parent_whitelist": [p for p in STABLE_PARENT_WHITELIST if p in node_ids],
        "proposed_parent_anchors_not_auto_approved": [p for p in PROPOSED_PARENT_ANCHORS if p in node_ids],
        "summary": {
            "total_concepts": len(rows),
            "reviewed_concepts": sum(1 for row in rows if row["decision"] != "unreviewed"),
            "taxonomy_placement_unreviewed": sum(1 for row in rows if row["decision"] == "unreviewed"),
            "concepts_with_up": len(with_up),
            "concepts_without_up": len(without_up),
            "concepts_with_candidate_basis": len(with_candidates),
            "candidate_basis_rows": sum(len(row["candidate_basis"]) for row in rows),
            "known_forbidden_candidate_pairs": len(forbidden_candidate_pairs),
            "accepted_taxonomy": decision_counts.get("accept_taxonomy", 0),
            "root_or_anchor_no_up": decision_counts.get("root_or_anchor_no_up", 0),
            "relation_only_terminal": decision_counts.get("relation_only_terminal", 0),
            "weak_or_backlog_terminal": decision_counts.get("weak_or_backlog_terminal", 0),
            "defer_boundary_review": decision_counts.get("defer_boundary_review", 0),
            "open_unclassified": decision_counts.get("unreviewed", 0),
            "open_review": review_status_counts.get("open", 0),
            "open_writeback": sum(1 for row in rows if row["writeback_action"] != "none"),
            "dry_run_planned": 0,
            "write_policy": "No writeback in inventory; concepts_without_up may remain > 0 after final closure if terminal reasons are recorded.",
        },
        "audit_sets": {
            "concepts_with_up": [row["concept"] for row in with_up],
            "concepts_without_up": [row["concept"] for row in without_up],
            "concepts_with_candidate_basis": [row["concept"] for row in with_candidates],
            "known_forbidden_candidate_pairs": forbidden_candidate_pairs,
        },
        "rows": rows,
    }
    if classify_initial_triage_rows:
        apply_initial_triage(review)
    validate_review(review, map_data)
    return review


def validate_review(review: dict[str, Any], map_data: dict[str, Any]) -> None:
    rows = review.get("rows", [])
    nodes = map_data.get("nodes", [])
    if len(rows) != len(nodes):
        raise ValueError(f"review row count {len(rows)} != map node count {len(nodes)}")
    concepts = [row.get("concept") for row in rows]
    if len(set(concepts)) != len(concepts):
        raise ValueError("duplicate concept rows in concept hierarchy placement review")
    node_ids = {node.get("id") for node in nodes}
    missing = node_ids - set(concepts)
    extra = set(concepts) - node_ids
    if missing or extra:
        raise ValueError(f"row/node mismatch missing={sorted(missing)} extra={sorted(extra)}")
    invalid_decisions = sorted({row.get("decision") for row in rows} - DECISIONS)
    if invalid_decisions:
        raise ValueError(f"invalid decision(s): {invalid_decisions}")
    invalid_statuses = sorted({row.get("review_status") for row in rows} - REVIEW_STATUSES)
    if invalid_statuses:
        raise ValueError(f"invalid review_status value(s): {invalid_statuses}")
    if any(row.get("writeback_action") != "none" for row in rows):
        raise ValueError("concept hierarchy placement review artifact must not schedule writeback before dry-run")
    summary = review.get("summary", {})
    if summary.get("total_concepts") != len(rows):
        raise ValueError("summary.total_concepts mismatch")
    if summary.get("taxonomy_placement_unreviewed") != sum(1 for row in rows if row.get("decision") == "unreviewed"):
        raise ValueError("summary.taxonomy_placement_unreviewed mismatch")
    if summary.get("concepts_without_up") != sum(1 for row in rows if not row.get("current_up")):
        raise ValueError("summary.concepts_without_up mismatch")
    if review.get("classification_stage") in {
        "initial_triage",
        "parent_whitelist_review",
        "conservative_candidates",
        "candidate_adjudication",
        "writeback_dry_run",
        "limited_apply",
        "audit_closure",
    }:
        if any(row.get("decision") == "unreviewed" for row in rows):
            raise ValueError("Initial triage+ classification must not leave unreviewed rows")
        if summary.get("open_unclassified") != 0:
            raise ValueError("Initial triage+ summary.open_unclassified must be 0")
    if review.get("classification_stage") in {
        "parent_whitelist_review",
        "conservative_candidates",
        "candidate_adjudication",
        "writeback_dry_run",
        "limited_apply",
        "audit_closure",
    }:
        parent_review = review.get("parent_whitelist_review")
        if not isinstance(parent_review, dict):
            raise ValueError("Parent-whitelist review+ review missing parent_whitelist_review object")
        approved = parent_review.get("approved_parents") or []
        approved_names = {item.get("concept") for item in approved}
        expected = set(review.get("stable_parent_whitelist") or [])
        if approved_names != expected:
            raise ValueError(
                f"Parent-whitelist review approved parent mismatch expected={sorted(expected)} approved={sorted(approved_names)}"
            )
        if any(item.get("decision") != "approved_for_candidate_generation" for item in approved):
            raise ValueError("Parent-whitelist review approved parent has invalid decision")
        if any(item.get("writeback_action") != "none" for item in parent_review.get("deferred_parent_route_precheck") or []):
            raise ValueError("Parent-whitelist review deferred precheck must not schedule writeback")
    if review.get("classification_stage") in {
        "conservative_candidates",
        "candidate_adjudication",
        "writeback_dry_run",
        "limited_apply",
        "audit_closure",
    }:
        candidate_generation = review.get("conservative_candidates")
        if not isinstance(candidate_generation, dict):
            raise ValueError("Conservative candidate generation review missing conservative_candidates object")
        candidates = [
            item
            for row in rows
            for item in row.get("candidate_generation_taxonomy", [])
        ]
        approved = set(review.get("stable_parent_whitelist") or [])
        if len(candidates) != candidate_generation.get("summary", {}).get("generated_candidates"):
            raise ValueError("Conservative candidate generation row candidate count mismatch")
        if any(item.get("target") not in approved for item in candidates):
            raise ValueError("Conservative candidate generation candidate target outside approved parent whitelist")
        if any(item.get("writeback_action") != "none" for item in candidates):
            raise ValueError("Conservative candidate generation candidates must not schedule writeback")
        if review.get("classification_stage") == "conservative_candidates":
            if summary.get("open_writeback") != 0 or summary.get("dry_run_planned") != 0:
                raise ValueError("Conservative candidate generation must not create open writeback or dry-run plans")
    if review.get("classification_stage") in {"candidate_adjudication", "writeback_dry_run", "limited_apply", "audit_closure"}:
        adjudication = review.get("candidate_adjudication")
        if not isinstance(adjudication, dict):
            raise ValueError("Candidate adjudication review missing candidate_adjudication object")
        adjudication_summary = adjudication.get("summary") or {}
        row_decisions = [
            item
            for row in rows
            for item in row.get("candidate_taxonomy", [])
        ]
        if len(row_decisions) != adjudication_summary.get("adjudicated_candidates"):
            raise ValueError("Candidate adjudication row adjudication count mismatch")
        if adjudication_summary.get("concept_card_writes") != 0:
            raise ValueError("Candidate adjudication must not edit concept cards")
        if summary.get("open_writeback") != 0:
            raise ValueError("Candidate adjudication+ review ledger must not create top-level open writeback")
        if review.get("classification_stage") == "candidate_adjudication" and summary.get("dry_run_planned") != 0:
            raise ValueError("Candidate adjudication review ledger must not create top-level dry-run plans")
        approved = set(review.get("stable_parent_whitelist") or [])
        for item in row_decisions:
            target = item.get("target")
            decision = item.get("decision")
            action = item.get("writeback_action")
            if target not in approved:
                raise ValueError(f"Candidate adjudication target outside approved parent whitelist: {target}")
            if action == "add_up" and decision != "accept_taxonomy":
                raise ValueError("Candidate adjudication add_up action requires accept_taxonomy")
            if decision == "accept_taxonomy" and action != "add_up":
                raise ValueError("Candidate adjudication accepted taxonomy must declare add_up for Writeback dry-run eligibility")
            if decision != "accept_taxonomy" and action != "none":
                raise ValueError("Candidate adjudication non-accepted candidates must not declare writeback")
        ready = sum(1 for item in row_decisions if item.get("writeback_action") == "add_up")
        if adjudication_summary.get("ready_for_dry_run") != ready:
            raise ValueError("Candidate adjudication ready_for_dry_run summary mismatch")
    if review.get("classification_stage") in {"writeback_dry_run", "limited_apply", "audit_closure"}:
        dry_run_review = review.get("writeback_dry_run")
        if not isinstance(dry_run_review, dict):
            raise ValueError("Writeback dry-run review missing writeback_dry_run object")
        dry_run_review_summary = dry_run_review.get("summary") or {}
        if dry_run_review_summary.get("concept_card_writes") != 0 or summary.get("writeback_dry_run_concept_card_writes") != 0:
            raise ValueError("Writeback dry-run must not edit concept cards")
        if summary.get("dry_run_planned") != dry_run_review_summary.get("planned"):
            raise ValueError("Writeback dry-run review summary dry_run_planned mismatch")
        if summary.get("writeback_dry_run_ready") != dry_run_review_summary.get("ready"):
            raise ValueError("Writeback dry-run ready summary mismatch")
        if dry_run_review_summary.get("planned") != len(dry_run_review.get("planned_up") or []):
            raise ValueError("Writeback dry-run planned_up count mismatch")
        if not WRITEBACK_DRY_RUN_JSON.exists():
            raise ValueError(f"Writeback dry-run artifact missing: {rel(WRITEBACK_DRY_RUN_JSON)}")
        if not ADJUDICATION_JSON.exists():
            raise ValueError(f"Candidate adjudication artifact missing: {rel(ADJUDICATION_JSON)}")
        validate_writeback_dry_run(load_json(WRITEBACK_DRY_RUN_JSON), review, load_json(ADJUDICATION_JSON))
    if review.get("classification_stage") in {"limited_apply", "audit_closure"}:
        limited_apply_review = review.get("limited_apply")
        if not isinstance(limited_apply_review, dict):
            raise ValueError("Limited apply review missing limited_apply object")
        if not LIMITED_APPLY_JSON.exists():
            raise ValueError(f"Limited apply artifact missing: {rel(LIMITED_APPLY_JSON)}")
        apply_report = load_json(LIMITED_APPLY_JSON)
        validate_limited_apply_report(apply_report, review)
        limited_apply_review_summary = limited_apply_review.get("summary") or {}
        if summary.get("limited_apply_applied") != limited_apply_review_summary.get("applied"):
            raise ValueError("Limited apply applied summary mismatch")
        if summary.get("open_writeback") != 0:
            raise ValueError("Limited apply must leave open_writeback at 0")
    if review.get("classification_stage") == "audit_closure":
        closure_review = review.get("audit_closure")
        if not isinstance(closure_review, dict):
            raise ValueError("Audit closure review missing audit_closure object")
        if not AUDIT_CLOSURE_JSON.exists():
            raise ValueError(f"Audit closure artifact missing: {rel(AUDIT_CLOSURE_JSON)}")
        validate_audit_closure(load_json(AUDIT_CLOSURE_JSON), review)


def write_markdown(review: dict[str, Any], path: Path) -> None:
    summary = review["summary"]
    rows = review["rows"]
    with_up = [row for row in rows if row["current_up"]]
    without_up = [row for row in rows if not row["current_up"]]
    candidate_rows = [row for row in rows if row["candidate_basis"]]
    forbidden_pairs = review["audit_sets"].get("known_forbidden_candidate_pairs", [])

    lines: list[str] = []
    lines.append("# Concept Hierarchy Placement Review — 层级归属待审计概念卡")
    lines.append("")
    lines.append(f"Generated: `{review['generated_at']}`")
    lines.append(f"Classification stage: `{review.get('classification_stage', 'unknown')}`")
    lines.append("")
    stage = review.get("classification_stage", "unknown")
    if stage == "audit_closure":
        lines.append("> Audit closure: remaining `defer_boundary_review` rows are closed as `deferred_with_backlog`; no concept cards are edited and no fallback parents are invented.")
    elif stage == "limited_apply":
        lines.append("> Limited apply complete: the reviewed dry-run row has been written to the child concept card, and post-apply dry-run is now the next proof state.")
    elif stage == "writeback_dry_run":
        lines.append("> Writeback dry-run complete: only Candidate adjudication `accept_taxonomy` + `add_up` rows are planned; this report still does not edit concept cards.")
    elif stage == "candidate_adjudication":
        lines.append("> Candidate adjudication LLM adjudication complete: accepted rows are dry-run eligible, but this report still does not edit concept cards.")
    elif stage == "conservative_candidates":
        lines.append("> Conservative candidate generation conservative candidate generation only: candidates feed Candidate adjudication; this report still does not write concept cards.")
    elif stage == "parent_whitelist_review":
        lines.append("> Parent-whitelist audit only: this report fixes which stable parents may seed later candidate generation, but it still does not write concept cards.")
    elif stage == "initial_triage":
        lines.append("> Initial triage only: this report classifies every concept card into one routing bucket, but it still does not write concept cards.")
    else:
        lines.append("> Inventory only: this report does not write concept cards. It turns `concepts_without_up` into an auditable concept-hierarchy-placement queue.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, value in summary.items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    if stage in {
        "initial_triage",
        "parent_whitelist_review",
        "conservative_candidates",
        "candidate_adjudication",
        "writeback_dry_run",
        "limited_apply",
        "audit_closure",
    }:
        lines.append("## Initial triage by decision")
        lines.append("")
        for decision, concepts in review.get("audit_sets", {}).get("by_decision", {}).items():
            lines.append(f"### {decision} ({len(concepts)})")
            lines.append("")
            lines.extend([f"- [[{concept}]]" for concept in concepts] or ["- none"])
            lines.append("")
    lines.append("## Naming boundary")
    lines.append("")
    lines.append("Use **层级归属待审计概念卡** instead of `no-up 卡`. Missing `up` is only a signal; the real task is to prove whether each concept has a valid concept hierarchy placement or a terminal reason for staying parentless.")
    lines.append("")
    lines.append("## Stable parent whitelist used for review")
    lines.append("")
    lines.extend([f"- [[{parent}]]" for parent in review.get("stable_parent_whitelist", [])] or ["- none"])
    lines.append("")
    lines.append("## Proposed anchors not auto-approved")
    lines.append("")
    lines.extend([f"- [[{parent}]]" for parent in review.get("proposed_parent_anchors_not_auto_approved", [])] or ["- none"])
    lines.append("")
    if stage in {
        "parent_whitelist_review",
        "conservative_candidates",
        "candidate_adjudication",
        "writeback_dry_run",
        "limited_apply",
        "audit_closure",
    }:
        parent_review = review.get("parent_whitelist_review", {})
        lines.append("## Parent-whitelist review parent whitelist review")
        lines.append("")
        lines.append("Parent-whitelist review fixes the candidate-generation boundary. An approved parent can be used as a later candidate target, but it is not permission to bulk-write `up` without Candidate adjudication and dry-run.")
        lines.append("")
        lines.append("### Approved stable parents")
        lines.append("")
        lines.append("| Parent | Role | Current up | Reason | Drift guard |")
        lines.append("|---|---|---|---|---|")
        for item in parent_review.get("approved_parents", []):
            current_up = ", ".join(f"[[{x}]]" for x in item.get("current_up", [])) or ""
            lines.append(
                f"| [[{item['concept']}]] | {item.get('role','')} | {current_up} | {item.get('reason','')} | {item.get('drift_guard','')} |"
            )
        lines.append("")
        lines.append("### Proposed anchors not auto-approved")
        lines.append("")
        lines.append("| Anchor | Decision | Reason |")
        lines.append("|---|---|---|")
        for item in parent_review.get("proposed_anchors_not_auto_approved", []):
            lines.append(f"| [[{item['concept']}]] | {item.get('decision','')} | {item.get('reason','')} |")
        for item in parent_review.get("proposed_anchors_missing_not_approved", []):
            lines.append(f"| {item['concept']} | {item.get('decision','')} | {item.get('reason','')} |")
        lines.append("")
        lines.append("### Root anchors that are not parent whitelist entries")
        lines.append("")
        lines.append("| Anchor | Decision | Reason |")
        lines.append("|---|---|---|")
        for item in parent_review.get("root_anchors_not_parent_whitelist", []):
            lines.append(f"| [[{item['concept']}]] | {item.get('decision','')} | {item.get('reason','')} |")
        lines.append("")
        lines.append("### Deferred row parent-route precheck")
        lines.append("")
        lines.append("| Concept | Route | Possible approved parent | Reason |")
        lines.append("|---|---|---|---|")
        for item in parent_review.get("deferred_parent_route_precheck", []):
            parent = item.get("possible_parent")
            parent_cell = f"[[{parent}]]" if parent else ""
            lines.append(f"| [[{item['concept']}]] | {item.get('route','')} | {parent_cell} | {item.get('reason','')} |")
        lines.append("")
    if stage in {"conservative_candidates", "candidate_adjudication", "writeback_dry_run", "limited_apply", "audit_closure"}:
        candidate_generation = review.get("conservative_candidates", {})
        lines.append("## Conservative candidate generation conservative taxonomy candidates")
        lines.append("")
        lines.append("Conservative candidate generation generates conservative candidates only from Parent-whitelist review approved parents. These candidates are **not** accepted taxonomy and cannot enter writeback until Candidate adjudication.")
        lines.append("")
        for key, value in (candidate_generation.get("summary") or {}).items():
            lines.append(f"- {key}: {format_md_value(value)}")
        lines.append("")
        lines.append("Candidate artifact:")
        lines.append("")
        lines.append(f"- JSON: `{candidate_generation.get('candidate_artifact_json', rel(CANDIDATES_JSON))}`")
        lines.append(f"- Markdown: `{candidate_generation.get('candidate_artifact_md', rel(CANDIDATES_MD))}`")
        lines.append("")
        lines.append("| Concept | Candidate parent | Confidence | Support |")
        lines.append("|---|---|---|---|")
        candidate_count = 0
        for row in rows:
            for item in row.get("candidate_generation_taxonomy", []):
                candidate_count += 1
                support = ", ".join(item.get("support", []))
                lines.append(f"| [[{row['concept']}]] | [[{item.get('target','')}]] | {item.get('confidence','')} | {support} |")
        if candidate_count == 0:
            lines.append("| _none_ |  |  |  |")
        lines.append("")
    if stage in {"candidate_adjudication", "writeback_dry_run", "limited_apply", "audit_closure"}:
        adjudication = review.get("candidate_adjudication", {})
        lines.append("## Candidate adjudication LLM adjudication")
        lines.append("")
        lines.append("Candidate adjudication judges the conservative candidates against strict taxonomy. It records dry-run eligibility but still does **not** edit concept cards.")
        lines.append("")
        for key, value in (adjudication.get("summary") or {}).items():
            lines.append(f"- {key}: {format_md_value(value)}")
        lines.append("")
        lines.append("Adjudication artifact:")
        lines.append("")
        lines.append(f"- JSON: `{adjudication.get('adjudication_artifact_json', rel(ADJUDICATION_JSON))}`")
        lines.append(f"- Markdown: `{adjudication.get('adjudication_artifact_md', rel(ADJUDICATION_MD))}`")
        lines.append("")
        lines.append("| Concept | Candidate parent | Decision | Writeback action | Status | Reason |")
        lines.append("|---|---|---|---|---|---|")
        row_count = 0
        for row in rows:
            for item in row.get("candidate_taxonomy", []):
                row_count += 1
                lines.append(
                    f"| [[{row['concept']}]] | [[{item.get('target','')}]] | {item.get('decision','')} | {item.get('writeback_action','')} | {item.get('review_status','')} | {item.get('decision_reason','')} |"
                )
        if row_count == 0:
            lines.append("| _none_ |  |  |  |  |  |")
        lines.append("")
    if stage in {"writeback_dry_run", "limited_apply", "audit_closure"}:
        dry_run_review = review.get("writeback_dry_run", {})
        lines.append("## Writeback dry-run")
        lines.append("")
        lines.append("Writeback dry-run creates a writeback preview only. It consumes **only** Candidate adjudication accepted taxonomy rows with `writeback_action: add_up`; rejected/control-point/adjacency rows stay excluded.")
        lines.append("")
        for key, value in (dry_run_review.get("summary") or {}).items():
            lines.append(f"- {key}: {format_md_value(value)}")
        lines.append("")
        lines.append("Dry-run artifact:")
        lines.append("")
        lines.append(f"- JSON: `{dry_run_review.get('dry_run_artifact_json', rel(WRITEBACK_DRY_RUN_JSON))}`")
        lines.append(f"- Markdown: `{dry_run_review.get('dry_run_artifact_md', rel(WRITEBACK_DRY_RUN_MD))}`")
        lines.append("")
        lines.append("| Concept | Parent | Status |")
        lines.append("|---|---|---|")
        for item in dry_run_review.get("planned_up", []):
            lines.append(f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('status','')} |")
        if not dry_run_review.get("planned_up"):
            lines.append("| _none_ |  |  |")
        lines.append("")
        lines.append("Excluded non-writeback rows:")
        lines.append("")
        lines.append("| Concept | Candidate parent | Decision |")
        lines.append("|---|---|---|")
        for item in dry_run_review.get("excluded_non_writeback", []):
            lines.append(f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('decision','')} |")
        if not dry_run_review.get("excluded_non_writeback"):
            lines.append("| _none_ |  |  |")
        lines.append("")
    if stage in {"limited_apply", "audit_closure"}:
        limited_apply_review = review.get("limited_apply", {})
        lines.append("## Limited apply")
        lines.append("")
        lines.append("Limited apply applies only rows that were already present in the Writeback dry-run ready set, then rebuilds the map and leaves a post-apply dry-run proof.")
        lines.append("")
        for key, value in (limited_apply_review.get("summary") or {}).items():
            lines.append(f"- {key}: {format_md_value(value)}")
        lines.append("")
        lines.append("Apply artifact:")
        lines.append("")
        lines.append(f"- JSON: `{limited_apply_review.get('apply_artifact_json', rel(LIMITED_APPLY_JSON))}`")
        lines.append(f"- Markdown: `{limited_apply_review.get('apply_artifact_md', rel(LIMITED_APPLY_MD))}`")
        lines.append("")
        lines.append("| Concept | Parent | Result | Current up after apply |")
        lines.append("|---|---|---|---|")
        for item in limited_apply_review.get("applied_up", []):
            current_up = ", ".join(f"[[{x}]]" for x in item.get("current_up_after_apply", []))
            lines.append(
                f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('result','')} | {current_up} |"
            )
        if not limited_apply_review.get("applied_up"):
            lines.append("| _none_ |  |  |  |")
        lines.append("")
    if stage == "audit_closure":
        closure_review = review.get("audit_closure", {})
        lines.append("## Audit closure")
        lines.append("")
        lines.append("Audit closure closes the whole concept hierarchy placement audit by routing every remaining deferred row to a durable backlog home. It does not add `up`; future changes must reopen a new candidate/adjudication/dry-run/limited-apply cycle.")
        lines.append("")
        for key, value in (closure_review.get("summary") or {}).items():
            lines.append(f"- {key}: {format_md_value(value)}")
        lines.append("")
        lines.append("Closure artifact:")
        lines.append("")
        lines.append(f"- JSON: `{closure_review.get('closure_artifact_json', rel(AUDIT_CLOSURE_JSON))}`")
        lines.append(f"- Markdown: `{closure_review.get('closure_artifact_md', rel(AUDIT_CLOSURE_MD))}`")
        lines.append(f"- Backlog home: `{closure_review.get('backlog_home', AUDIT_BACKLOG_HOME)}`")
        lines.append("")
        lines.append("| Concept | Suppressed target | Signal | Reason |")
        lines.append("|---|---|---|---|")
        for item in closure_review.get("deferred_with_backlog", []):
            target = item.get("suppressed_target")
            target_cell = f"[[{target}]]" if target else ""
            lines.append(
                f"| [[{item.get('concept','')}]] | {target_cell} | {item.get('suppressed_signal_type','')} | {item.get('reason','')} |"
            )
        if not closure_review.get("deferred_with_backlog"):
            lines.append("| _none_ |  |  |  |")
        lines.append("")
    lines.append("## Concepts with existing `up`")
    lines.append("")
    lines.append("| Concept | Current up | Typed relations | Candidate basis rows |")
    lines.append("|---|---:|---:|---:|")
    for row in with_up:
        current_up = ", ".join(f"[[{x}]]" for x in row["current_up"])
        lines.append(f"| [[{row['concept']}]] | {current_up} | {row['current_relations_count']} | {len(row['candidate_basis'])} |")
    lines.append("")
    lines.append("## Concepts without `up` — review queue")
    lines.append("")
    lines.append("| Concept | Decision | Candidate parent | Candidate basis rows | Drift guards |")
    lines.append("|---|---|---|---:|---:|")
    for row in without_up:
        candidate_parent = f"[[{row['candidate_parent']}]]" if row.get("candidate_parent") else ""
        lines.append(f"| [[{row['concept']}]] | {row['decision']} | {candidate_parent} | {len(row['candidate_basis'])} | {len(row['drift_guard'])} |")
    lines.append("")
    lines.append("## Candidate-bearing concepts")
    lines.append("")
    lines.append("Candidate basis is evidence for later adjudication, not an accepted parent.")
    lines.append("")
    lines.append("| Concept | Candidate target | Type | Confidence | Support | Forbidden as up |")
    lines.append("|---|---|---|---|---|---|")
    if candidate_rows:
        for row in candidate_rows:
            for item in row["candidate_basis"]:
                support = ", ".join(str(x) for x in item.get("support", []))
                forbidden = "yes" if item.get("known_forbidden_as_up") else "no"
                lines.append(
                    f"| [[{row['concept']}]] | [[{item['target']}]] | {item.get('candidate_type','')} | {item.get('confidence','')} | {support} | {forbidden} |"
                )
    else:
        lines.append("| _none_ |  |  |  |  |  |")
    lines.append("")
    lines.append("## Known forbidden candidate pairs")
    lines.append("")
    if forbidden_pairs:
        lines.append("| Source | Target | Candidate type |")
        lines.append("|---|---|---|")
        for pair in forbidden_pairs:
            lines.append(f"| [[{pair['source']}]] | [[{pair['target']}]] | {pair['candidate_type']} |")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Next command")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 scripts/concept_taxonomy/taxonomy_placement_review.py --check")
    if stage == "audit_closure":
        lines.append("# Audit closure is closed; future taxonomy changes must begin a new candidate/adjudication/dry-run/limited-apply cycle")
    elif stage == "limited_apply":
        lines.append("# Limited apply applied the ready row; continue to plugin-contract verification rebuild/plugin verification or review post-apply dry-run if needed")
    elif stage == "writeback_dry_run":
        lines.append("# then continue to Limited apply: limited apply only after reviewing this dry-run artifact")
    elif stage == "candidate_adjudication":
        lines.append("# then continue to Writeback dry-run: dry-run only rows accepted in Candidate adjudication with writeback_action=add_up")
    elif stage == "conservative_candidates":
        lines.append("# then continue to Candidate adjudication: adjudicate the conservative candidates before any dry-run/writeback")
    elif stage == "parent_whitelist_review":
        lines.append("# then continue to Conservative candidate generation: conservatively generate candidate taxonomy using only approved stable parents")
    elif stage == "initial_triage":
        lines.append("# then continue to Parent-whitelist review: confirm/adjust the stable parent whitelist before generating stronger candidates")
    else:
        lines.append("# then continue to Initial triage: classify rows without writing concept cards")
    lines.append("```")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_candidates_markdown(candidates: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Concept Hierarchy Placement Candidates — Conservative candidate generation")
    lines.append("")
    lines.append(f"Generated: `{candidates['generated_at']}`")
    lines.append("")
    lines.append("> Conservative candidate taxonomy only. These rows are **not** accepted taxonomy and must go through Candidate adjudication before any dry-run/writeback.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, value in candidates.get("summary", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Policy")
    lines.append("")
    policy = candidates.get("policy", {})
    for key, value in policy.items():
        if isinstance(value, list):
            lines.append(f"- {key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Candidates for Candidate adjudication review")
    lines.append("")
    lines.append("| Source | Candidate parent | Confidence | Support | Rationale |")
    lines.append("|---|---|---|---|---|")
    for item in candidates.get("candidates", []):
        support = ", ".join(item.get("support", []))
        lines.append(
            f"| [[{item['source']}]] | [[{item['target']}]] | {item.get('confidence','')} | {support} | {item.get('rationale','')} |"
        )
    if not candidates.get("candidates"):
        lines.append("| _none_ |  |  |  |  |")
    lines.append("")
    lines.append("## Suppressed signals")
    lines.append("")
    lines.append("| Source | Suppressed target | Signal | Reason |")
    lines.append("|---|---|---|---|")
    for item in candidates.get("suppressed_signals", []):
        target = item.get("target")
        target_cell = f"[[{target}]]" if target else ""
        lines.append(f"| [[{item['source']}]] | {target_cell} | {item.get('signal_type','')} | {item.get('reason','')} |")
    if not candidates.get("suppressed_signals"):
        lines.append("| _none_ |  |  |  |")
    lines.append("")
    lines.append("## Next command")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 scripts/concept_taxonomy/taxonomy_placement_review.py --check")
    lines.append("# then Candidate adjudication: LLM adjudication of these candidates; do not write cards yet")
    lines.append("```")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_adjudication_markdown(adjudication: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Concept Hierarchy Placement Candidate adjudication Adjudication — LLM 逐条判定")
    lines.append("")
    lines.append(f"Generated: `{adjudication['generated_at']}`")
    lines.append("")
    lines.append("> Candidate adjudication only adjudicates candidate semantics. It does not edit concept cards; accepted rows must still pass Writeback dry-run before any limited apply.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, value in adjudication.get("summary", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Policy")
    lines.append("")
    for key, value in adjudication.get("policy", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Decisions")
    lines.append("")
    lines.append("| Source | Candidate parent | Decision | Writeback action | Dry-run eligible | Strict taxonomy test |")
    lines.append("|---|---|---|---|---:|---|")
    for item in adjudication.get("decisions", []):
        lines.append(
            f"| [[{item['source']}]] | [[{item['target']}]] | {item.get('decision','')} | {item.get('writeback_action','')} | {str(item.get('dry_run_eligible', False)).lower()} | {item.get('strict_taxonomy_test','')} |"
        )
    if not adjudication.get("decisions"):
        lines.append("| _none_ |  |  |  |  |  |")
    lines.append("")
    lines.append("## Decision details")
    lines.append("")
    for item in adjudication.get("decisions", []):
        lines.append(f"### [[{item['source']}]] → [[{item['target']}]]")
        lines.append("")
        lines.append(f"- decision: `{item.get('decision','')}`")
        lines.append(f"- review_status: `{item.get('review_status','')}`")
        lines.append(f"- writeback_action: `{item.get('writeback_action','')}`")
        lines.append(f"- reason: {item.get('decision_reason','')}")
        lines.append("")
        lines.append("Evidence:")
        for evidence in item.get("evidence", []):
            lines.append(f"- `{evidence.get('path','')}` / `{evidence.get('needle','')}`: {evidence.get('excerpt','')}")
        if not item.get("evidence"):
            lines.append("- none")
        lines.append("")
        lines.append("Drift guards:")
        lines.extend(f"- {guard}" for guard in item.get("drift_guard", []))
        lines.append("")
    lines.append("## Next command")
    lines.append("")
    lines.append("```bash")
    lines.append("# Writeback dry-run should consume only accept_taxonomy + writeback_action=add_up rows from this adjudication artifact.")
    lines.append("python3 scripts/concept_taxonomy/taxonomy_placement_review.py --dry-run-reviewed --check")
    lines.append("```")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_writeback_dry_run_markdown(dry_run: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Concept Hierarchy Placement Writeback dry-run — Dry-run 写回预览")
    lines.append("")
    lines.append(f"Generated: `{dry_run['generated_at']}`")
    lines.append("")
    lines.append("> Writeback dry-run is dry-run only. It plans no concept-card edits and only previews later limited `up` writeback rows.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, value in dry_run.get("summary", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Policy")
    lines.append("")
    for key, value in dry_run.get("policy", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Planned `up` rows")
    lines.append("")
    lines.append("| Source | Target parent | Status | Current up | Proposed write |")
    lines.append("|---|---|---|---|---|")
    for item in dry_run.get("planned", []):
        current_up = ", ".join(item.get("current_up") or [])
        proposed = json.dumps(item.get("proposed_write") or {}, ensure_ascii=False)
        lines.append(
            f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('status','')} | {current_up} | `{proposed}` |"
        )
    if not dry_run.get("planned"):
        lines.append("| _none_ |  |  |  |  |")
    lines.append("")
    lines.append("## Planned-row evidence")
    lines.append("")
    for item in dry_run.get("planned", []):
        lines.append(f"### [[{item.get('source','')}]] → [[{item.get('target','')}]]")
        lines.append("")
        lines.append(f"- decision: `{item.get('decision','')}`")
        lines.append(f"- writeback_action: `{item.get('writeback_action','')}`")
        lines.append(f"- strict_taxonomy_test: {item.get('strict_taxonomy_test','')}")
        lines.append(f"- reason: {item.get('decision_reason','')}")
        lines.append("")
        lines.append("Evidence:")
        for evidence in item.get("evidence", []):
            lines.append(f"- `{evidence.get('path','')}` / `{evidence.get('needle','')}`: {evidence.get('excerpt','')}")
        if not item.get("evidence"):
            lines.append("- none")
        lines.append("")
        lines.append("Drift guards:")
        lines.extend(f"- {guard}" for guard in item.get("drift_guard", []))
        lines.append("")
    lines.append("## Excluded rows")
    lines.append("")
    lines.append("| Source | Candidate parent | Decision | Writeback action | Reason |")
    lines.append("|---|---|---|---|---|")
    for item in dry_run.get("excluded", []):
        lines.append(
            f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('decision','')} | {item.get('writeback_action','')} | {item.get('reason','')} |"
        )
    if not dry_run.get("excluded"):
        lines.append("| _none_ |  |  |  |  |")
    lines.append("")
    lines.append("## Next command")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 scripts/concept_taxonomy/taxonomy_placement_review.py --check")
    lines.append("# If still accepted after manual review, Limited apply can perform a limited apply; do not use unbounded full-batch apply.")
    lines.append("```")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_limited_apply_markdown(apply_report: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Concept Hierarchy Placement Limited apply — Limited Apply Report")
    lines.append("")
    lines.append(f"Generated: `{apply_report['generated_at']}`")
    lines.append("")
    lines.append("> Limited apply applies only reviewed Writeback dry-run ready rows. It writes child-card `up` only and then requires a rebuilt post-apply review.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, value in apply_report.get("summary", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Policy")
    lines.append("")
    for key, value in apply_report.get("policy", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Applied rows")
    lines.append("")
    lines.append("| Source | Target parent | Result | Current up after apply |")
    lines.append("|---|---|---|---|")
    for item in apply_report.get("applied", []):
        current_up = ", ".join(f"[[{x}]]" for x in item.get("current_up_after_apply", []))
        lines.append(
            f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('result','')} | {current_up} |"
        )
    if not apply_report.get("applied"):
        lines.append("| _none_ |  |  |  |")
    lines.append("")
    lines.append("## Selected rows")
    lines.append("")
    lines.append("| Source | Target parent | Strict taxonomy test |")
    lines.append("|---|---|---|")
    for item in apply_report.get("planned", []):
        lines.append(f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('strict_taxonomy_test','')} |")
    if not apply_report.get("planned"):
        lines.append("| _none_ |  |  |")
    lines.append("")
    lines.append("## Excluded from input dry-run")
    lines.append("")
    lines.append("| Source | Candidate parent | Decision |")
    lines.append("|---|---|---|")
    for item in apply_report.get("excluded_from_input_dry_run", []):
        lines.append(f"| [[{item.get('source','')}]] | [[{item.get('target','')}]] | {item.get('decision','')} |")
    if not apply_report.get("excluded_from_input_dry_run"):
        lines.append("| _none_ |  |  |")
    lines.append("")
    lines.append("## Post-apply review")
    lines.append("")
    for key, value in (apply_report.get("post_apply_review") or {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_audit_closure_markdown(closure: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Concept Hierarchy Placement Audit closure — Completion Closure")
    lines.append("")
    lines.append(f"Generated: `{closure['generated_at']}`")
    lines.append("")
    lines.append("> Audit closure closes remaining concept-hierarchy-placement open reviews as backlog-backed defers. It does not write concept cards or create fallback parents.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key, value in closure.get("summary", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Completion definition")
    lines.append("")
    for key, value in (closure.get("completion_definition", {}).get("checks") or {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Policy")
    lines.append("")
    for key, value in closure.get("policy", {}).items():
        lines.append(f"- {key}: {format_md_value(value)}")
    lines.append("")
    lines.append("## Deferred with backlog")
    lines.append("")
    lines.append(f"Backlog home: `{closure.get('backlog_home', AUDIT_BACKLOG_HOME)}`")
    lines.append("")
    lines.append("| Concept | Suppressed target | Signal | Reason | Reopen triggers |")
    lines.append("|---|---|---|---|---|")
    for item in closure.get("deferred_with_backlog", []):
        target = item.get("suppressed_target")
        target_cell = f"[[{target}]]" if target else ""
        triggers = "<br>".join(item.get("reopen_triggers") or [])
        lines.append(
            f"| [[{item.get('concept','')}]] | {target_cell} | {item.get('suppressed_signal_type','')} | {item.get('reason','')} | {triggers} |"
        )
    if not closure.get("deferred_with_backlog"):
        lines.append("| _none_ |  |  |  |  |")
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.append("- `defer_boundary_review` remains a semantic decision, but it is no longer an open task when paired with `review_status: deferred_with_backlog` and a backlog home.")
    lines.append("- Future concept cards may use this closed ledger as baseline; if they touch a deferred boundary, they must reopen through a new candidate/adjudication/dry-run/limited-apply cycle.")
    lines.append("- `concepts_without_up` may remain greater than 0; the failure condition is an unreviewed or hidden-open boundary, not a missing field.")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build/check concept hierarchy placement review artifacts.")
    parser.add_argument("--build", action="store_true", help="Generate concept-hierarchy-placement-review.json/md from the current relation map.")
    parser.add_argument("--initial-triage", action="store_true", help="Apply the concept hierarchy audit Initial triage while generating the review artifact.")
    parser.add_argument("--review-parent-whitelist", action="store_true", help="Apply the concept hierarchy audit Parent-whitelist review stable-parent whitelist review while generating the review artifact.")
    parser.add_argument("--generate-candidates", action="store_true", help="Apply the concept hierarchy audit Conservative candidate generation conservative taxonomy candidate generation.")
    parser.add_argument("--adjudicate-candidates", action="store_true", help="Apply the concept hierarchy audit Candidate adjudication LLM adjudication over Conservative candidate generation candidates without editing concept cards.")
    parser.add_argument("--dry-run-reviewed", action="store_true", help="Apply the concept hierarchy audit Writeback dry-run preview over Candidate adjudication accepted add_up rows without editing concept cards.")
    parser.add_argument("--apply-reviewed", action="store_true", help="Apply the concept hierarchy audit Limited apply limited writeback from the Writeback dry-run ready set.")
    parser.add_argument("--close-audit", action="store_true", help="Apply the concept hierarchy audit Audit closure: mark remaining deferred rows as deferred_with_backlog without concept-card edits.")
    parser.add_argument("--limit", type=int, default=None, help="Maximum Limited apply rows to apply. Required with --apply-reviewed to prevent unbounded writeback.")
    parser.add_argument("--check", action="store_true", help="Validate concept-hierarchy-placement-review.json against the current relation map.")
    parser.add_argument("--refresh-map", action="store_true", help="Run build.py before generating or checking.")
    args = parser.parse_args()

    if args.close_audit:
        args.dry_run_reviewed = True
    if args.apply_reviewed:
        if args.limit is None:
            raise SystemExit("Refusing unbounded Limited apply. Pass --limit N.")
        if args.limit <= 0:
            raise SystemExit("Refusing Limited apply with non-positive --limit.")
        args.dry_run_reviewed = True
    if args.dry_run_reviewed:
        args.adjudicate_candidates = True
    if args.adjudicate_candidates:
        args.generate_candidates = True
    if args.generate_candidates:
        args.review_parent_whitelist = True
    if args.review_parent_whitelist:
        args.classify_initial_triage = True
    if args.classify_initial_triage:
        args.build = True
    if not args.build and not args.check:
        args.build = True
    if args.refresh_map:
        run_build()
    if not MAP_JSON.exists():
        run_build()
    map_data = load_json(MAP_JSON)

    if args.build and args.close_audit:
        review = build_review(map_data, classify_initial_triage_rows=True)
        apply_parent_whitelist_review(review)
        candidates = apply_conservative_candidates(review)
        adjudication = apply_candidate_adjudication(review)
        dry_run = apply_writeback_dry_run(review, adjudication)
        apply_report = load_existing_apply_report()
        if not apply_report:
            raise ValueError("Audit closure requires existing Limited apply report proof")
        if apply_report.get("classification_stage") != "limited_apply":
            raise ValueError(f"Existing {rel(LIMITED_APPLY_JSON)} is not a Limited apply report")
        attach_limited_apply(review, apply_report)
        closure = apply_audit_closure(review)

        write_json(CANDIDATES_JSON, candidates)
        write_candidates_markdown(candidates, CANDIDATES_MD)
        write_json(ADJUDICATION_JSON, adjudication)
        write_adjudication_markdown(adjudication, ADJUDICATION_MD)
        write_json(WRITEBACK_DRY_RUN_JSON, dry_run)
        write_writeback_dry_run_markdown(dry_run, WRITEBACK_DRY_RUN_MD)
        write_json(LIMITED_APPLY_JSON, apply_report)
        write_limited_apply_markdown(apply_report, LIMITED_APPLY_MD)
        write_json(AUDIT_CLOSURE_JSON, closure)
        write_audit_closure_markdown(closure, AUDIT_CLOSURE_MD)
        write_json(REVIEW_JSON, review)
        write_markdown(review, REVIEW_MD)
        validate_review(review, map_data)
        print(
            json.dumps(
                {
                    "ok": True,
                    "json": rel(REVIEW_JSON),
                    "markdown": rel(REVIEW_MD),
                    "closure_report": rel(AUDIT_CLOSURE_JSON),
                    "summary": review["summary"],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif args.build and args.apply_reviewed:
        pre_review = build_review(map_data, classify_initial_triage_rows=True)
        apply_parent_whitelist_review(pre_review)
        pre_candidates = apply_conservative_candidates(pre_review)
        pre_adjudication = apply_candidate_adjudication(pre_review)
        pre_dry_run = apply_writeback_dry_run(pre_review, pre_adjudication)
        if pre_dry_run.get("planned"):
            apply_report = build_limited_apply_report(pre_dry_run, args.limit)
        elif LIMITED_APPLY_JSON.exists():
            apply_report = load_existing_apply_report()
            if not apply_report:
                raise ValueError("Existing limited-apply proof could not be loaded")
            if apply_report.get("classification_stage") != "limited_apply":
                raise ValueError(f"Existing {rel(LIMITED_APPLY_JSON)} is not a Limited apply report")
            apply_report["idempotent_recheck_at"] = utc_now()
            apply_report.setdefault("notes", []).append(
                "Limited apply was re-run after the accepted row was already written; "
                "the existing apply report was preserved and post-apply artifacts were rebuilt."
            )
        else:
            raise ValueError(
                "Limited apply has no ready dry-run rows to apply and no existing apply report to preserve."
            )

        # Refresh the temporary relation map after the only allowed concept-card
        # write path. The final persisted Writeback dry-run is post-apply proof.
        run_build()
        map_data = load_json(MAP_JSON)
        review = build_review(map_data, classify_initial_triage_rows=True)
        apply_parent_whitelist_review(review)
        candidates = apply_conservative_candidates(review)
        adjudication = apply_candidate_adjudication(review)
        dry_run = apply_writeback_dry_run(review, adjudication)
        attach_limited_apply(review, apply_report)

        write_json(CANDIDATES_JSON, candidates)
        write_candidates_markdown(candidates, CANDIDATES_MD)
        write_json(ADJUDICATION_JSON, adjudication)
        write_adjudication_markdown(adjudication, ADJUDICATION_MD)
        write_json(WRITEBACK_DRY_RUN_JSON, dry_run)
        write_writeback_dry_run_markdown(dry_run, WRITEBACK_DRY_RUN_MD)
        write_json(LIMITED_APPLY_JSON, apply_report)
        write_limited_apply_markdown(apply_report, LIMITED_APPLY_MD)
        write_json(REVIEW_JSON, review)
        write_markdown(review, REVIEW_MD)
        validate_review(review, map_data)
        print(
            json.dumps(
                {
                    "ok": True,
                    "json": rel(REVIEW_JSON),
                    "markdown": rel(REVIEW_MD),
                    "apply_report": rel(LIMITED_APPLY_JSON),
                    "summary": review["summary"],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif args.build:
        review = build_review(map_data, classify_initial_triage_rows=args.classify_initial_triage)
        candidates = None
        adjudication = None
        dry_run = None
        if args.review_parent_whitelist:
            apply_parent_whitelist_review(review)
        if args.generate_candidates:
            candidates = apply_conservative_candidates(review)
        if args.adjudicate_candidates:
            adjudication = apply_candidate_adjudication(review)
        if args.dry_run_reviewed:
            dry_run = apply_writeback_dry_run(review, adjudication)
        write_json(REVIEW_JSON, review)
        write_markdown(review, REVIEW_MD)
        if candidates is not None:
            write_json(CANDIDATES_JSON, candidates)
            write_candidates_markdown(candidates, CANDIDATES_MD)
        if adjudication is not None:
            write_json(ADJUDICATION_JSON, adjudication)
            write_adjudication_markdown(adjudication, ADJUDICATION_MD)
        if dry_run is not None:
            write_json(WRITEBACK_DRY_RUN_JSON, dry_run)
            write_writeback_dry_run_markdown(dry_run, WRITEBACK_DRY_RUN_MD)
            validate_review(review, map_data)
        print(json.dumps({"ok": True, "json": rel(REVIEW_JSON), "markdown": rel(REVIEW_MD), "summary": review["summary"]}, ensure_ascii=False, indent=2))

    if args.check:
        if not REVIEW_JSON.exists():
            raise SystemExit(f"missing {rel(REVIEW_JSON)}")
        review = load_json(REVIEW_JSON)
        validate_review(review, map_data)
        print(json.dumps({"ok": True, "checked": rel(REVIEW_JSON), "rows": len(review.get("rows", [])), "summary": review.get("summary", {})}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
