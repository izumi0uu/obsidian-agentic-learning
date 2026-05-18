# Concept Relation Decision Ledger

Generated: `2026-05-18T09:14:09Z`

> 逐条判定台账：把临时图候选边分成 accepted taxonomy、rejected taxonomy、adjacency only、duplicate signal 和 deferred。只有 `writeback_action=add_up` 的行可以进入后续写回；`already_present` 表示本轮小批量已落地或卡片已有该 `up`；`topic_family_review` 永远不能直接写入 `up`。

## Summary

- candidate_edges: 76
- decision_counts: {'reject_taxonomy': 11, 'adjacency_only': 65}
- writeback_candidates: 0
- open_writeback_items: 0
- open_review_items: 0
- relation_tail_open_items: 0
- relation_tail_status: closed
- terminal_non_writeback_decisions: 76
- already_applied_or_present_taxonomy: 0
- remaining_writeback_candidates: 0
- accepted_taxonomy: 0
- rejected_taxonomy: 11
- deferred_taxonomy: 0
- adjacency_only: 65
- duplicate_signals: 0
- non_taxonomy_boundary_guardrails: 2
- write_policy: Only decisions with writeback_action=add_up may be applied, and only through dry-run/apply small batches.

## Tail closure summary

- `open_writeback_items`: accepted taxonomy rows still needing a limited apply.
- `open_review_items`: `needs_review` or `defer_taxonomy` rows still lacking a terminal decision.
- `terminal_non_writeback_decisions`: reviewed rows that are deliberately **not** written to `up` (`reject_taxonomy`, `adjacency_only`, or `duplicate_signal`). These are closed decisions, not backlog.

- relation tail status: **closed**
- open rows: none

## Accepted taxonomy writeback candidates

| Source | Target | Candidate type | Decision | Writeback | Judge confidence | Rationale |
|---|---|---|---|---|---|---|

## Rejected or deferred taxonomy candidates

| Source | Target | Candidate type | Decision | Writeback | Judge confidence | Rationale |
|---|---|---|---|---|---|---|
| [[OpenTelemetry GenAI]] | [[Observability]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | OpenTelemetry GenAI is a semantic-convention/standardization layer that supports observability; it is not itself an observability capability subtype. |
| [[RAGGraph]] | [[RAG]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | RAGGraph is an unstable ambiguity/reminder card for workflow graph vs GraphRAG confusion; it remains related to RAG but is not a stable RAG subtype. |
| [[State Graph Runtime]] | [[Agent Workflow]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | State Graph Runtime executes and persists workflows; runtime infrastructure is adjacent to Agent Workflow, not a workflow subtype. |
| [[Top-K]] | [[Retriever]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Top-K is a ranking/selection rule used by retrievers and decoders; it is not itself a retriever subtype. |
| [[Durable Execution]] | [[Agent Workflow]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Durable Execution is a runtime capability used by workflows, not a workflow subtype. |
| [[Handoff]] | [[Agent Workflow]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Handoff is a transfer mechanism inside workflows, not a workflow subtype. |
| [[Human-in-the-loop]] | [[Agent Workflow]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Human-in-the-loop is an intervention/approval pattern inside workflows, not a workflow subtype. |
| [[Reasoning Trace]] | [[Observability]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Reasoning Trace is a kind of trace/trajectory artifact; Observability is too broad as a direct parent here. |
| [[Tool Permissioning]] | [[Tool Use]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Tool Permissioning constrains and governs tools; it is not a tool-use subtype. |
| [[Tool Poisoning]] | [[Tool Use]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Tool Poisoning is a threat/failure mode against tools; it is not a tool-use subtype. |
| [[Tool Registry]] | [[Tool Use]] | taxonomy_candidate | reject_taxonomy | none `related or relations, not up` | high | Tool Registry is infrastructure/catalog metadata for tools; it is not a tool-use subtype. |

## Topic-family / adjacency signals

| Source | Target | Candidate type | Decision | Writeback | Judge confidence | Rationale |
|---|---|---|---|---|---|---|
| [[Agent Control Plane]] | [[Observability]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Framework]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Harness]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Lifecycle Hook]] | [[Observability]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Loop]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Robustness]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent State]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent State]] | [[Memory]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Workflow Static Verification]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Agent Workflow Static Verification]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Benchmark]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Chunking]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Context Engineering]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[DeerFlow]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Document Ingestion]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Embedding]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Eval Harness]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Frontend-first AI Toolkit]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Guardrails]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Hallucination]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Hermes Agent]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[HyDE]] | [[Retriever]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Indirect Prompt Injection]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Knowledge Graph]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[LLM Gateway]] | [[Observability]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[LLM Training Pipeline]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[LLM-as-Judge]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Neo4j]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[OMX $ 指令]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Observability]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[OpenTelemetry GenAI]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[OpenTelemetry GenAI]] | [[Observability]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Patch Validation]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Plan-and-Solve Prompting]] | [[Planning]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Progressive Disclosure]] | [[Tool Use]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Prompt Engineering]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Provider-first Agent SDK]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Query Planning]] | [[Retriever]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Query Rewrite]] | [[Retriever]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[RAG Access Control]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[RAG Citation Faithfulness]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[RAGFlow]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[RAGFlow]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[RAGGraph]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Reflexion]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Replay]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Replay]] | [[Observability]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Repo Context]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Reranking]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Reranking]] | [[Retriever]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Retriever]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Role-playing Agent]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[State Graph Runtime]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[TF-IDF]] | [[RAG]] | topic_family_review | adjacency_only | none `relations or related, never up` | high | TF-IDF is a sparse lexical weighting/representation used in retrieval contexts; it is not a RAG subtype. |
| [[TF-IDF]] | [[Retriever]] | topic_family_review | adjacency_only | none `relations or related, never up` | high | TF-IDF can supply sparse lexical scoring intuition, but it is not a retriever component subtype. |
| [[TTL]] | [[Memory]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[TTL]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Task Success Rate]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Top-K]] | [[Retriever]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Trace]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Trace]] | [[Observability]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Type-safe Agent SDK]] | [[Agent Framework]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Type-safe Agent SDK]] | [[Evaluation]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Vector Database]] | [[RAG]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |
| [[Workflow Guardrails]] | [[Agent Workflow]] | topic_family_review | adjacency_only | none `related/body context only` | medium | Topic-family overlap is useful for review batching, but it does not prove a strict parent/child taxonomy edge. |

## Non-taxonomy boundary guardrails

| Source | Target | Boundary kind | Safe relation | Decision | Rationale |
|---|---|---|---|---|---|
| [[TF-IDF]] | [[RAG]] | representation_vs_application | related_to | adjacency_only | TF-IDF is a sparse lexical weighting/representation used in retrieval contexts; it is not a RAG subtype. |
| [[TF-IDF]] | [[Retriever]] | feature_vs_component | foundational_for -> Sparse Retrieval | adjacency_only | TF-IDF can supply sparse lexical scoring intuition, but it is not a retriever component subtype. |

## Non-taxonomy boundary policy catalog

> 这些 pair 即使当前没有出现在 candidate_edges，也属于 forbidden-as-up 防线；若未来启发式生成它们，必须落到 `relations` / `related` / reject，而不是 `up`。

| Source | Target | Boundary kind | Safe relation | Rationale |
|---|---|---|---|---|
| [[BM25]] | [[Multi-Route Retrieval]] | algorithm_vs_strategy | composed_into via Sparse Retrieval | BM25 is a sparse retrieval scoring function/representative route signal, not a multi-route retrieval subtype. |
| [[Dense Retrieval]] | [[Multi-Route Retrieval]] | route_vs_strategy | composed_into | Dense Retrieval can be one route inside Multi-Route Retrieval, but a route/component is not a child taxonomy of the orchestration strategy. |
| [[Hybrid Search]] | [[Dense Retrieval]] | composition_vs_component | composes_with | Hybrid Search composes a dense retrieval side; it is not a Dense Retrieval subtype. |
| [[Hybrid Search]] | [[Sparse Retrieval]] | composition_vs_component | composes_with | Hybrid Search composes a sparse retrieval side; it is not a Sparse Retrieval subtype. |
| [[Multi-Route Retrieval]] | [[BM25]] | strategy_vs_algorithm | composes_with -> Sparse Retrieval/BM25 route | Multi-Route Retrieval may include a BM25 sparse route; the strategy is not a BM25 subtype. |
| [[Multi-Route Retrieval]] | [[Hybrid Search]] | strategy_vs_common_shape | related_to | Hybrid Search is a common dense+sparse shape inside the wider multi-route retrieval design space; this should be explained as relation, not forced into up. |
| [[Multi-Route Retrieval]] | [[Sparse Retrieval]] | strategy_vs_route | composes_with | Multi-Route Retrieval may compose Sparse Retrieval as one route; the strategy is not a child of the route. |
| [[Reranking]] | [[Multi-Route Retrieval]] | stage_vs_strategy | composes_with | Reranking is a downstream ordering stage over candidates; it is not a recall route or subtype of Multi-Route Retrieval. |
| [[Sparse Retrieval]] | [[Multi-Route Retrieval]] | route_vs_strategy | composed_into | Sparse Retrieval can be one route inside Multi-Route Retrieval, but a route/component is not a child taxonomy of the orchestration strategy. |
| [[TF-IDF]] | [[Multi-Route Retrieval]] | feature_vs_strategy | foundational_for -> Sparse Retrieval; Sparse Retrieval composed_into -> Multi-Route Retrieval | TF-IDF itself is not a multi-route retrieval route or strategy; a sparse retrieval route may use TF-IDF/BM25-style signals inside multi-route retrieval. |
| [[TF-IDF]] | [[RAG]] | representation_vs_application | related_to | TF-IDF is a sparse lexical weighting/representation used in retrieval contexts; it is not a RAG subtype. |
| [[TF-IDF]] | [[Retriever]] | feature_vs_component | foundational_for -> Sparse Retrieval | TF-IDF can supply sparse lexical scoring intuition, but it is not a retriever component subtype. |
| [[TF-IDF]] | [[Sparse Retrieval]] | foundation_vs_family | foundational_for | TF-IDF is a foundational sparse lexical weighting method; Sparse Retrieval is the broader retrieval family. |
| [[Top-K]] | [[Multi-Route Retrieval]] | selection_rule_vs_strategy | related_to | Top-K is a candidate selection/ranking cutoff, not a multi-route retrieval subtype. |

## Writeback gate

1. Run `python3 scripts/concept_taxonomy/writeback.py --dry-run` first.
2. Apply only a small batch with `--apply --limit N`; the default verifier rejects topic-family writes.
3. After applying, run `python3 scripts/concept_taxonomy/validate.py` and `git diff --check`.
4. Breadcrumbs / Abstract Folder validation is structural: top-level `up` YAML only; no `down`, no `children`, no Juggl mirror fields.
