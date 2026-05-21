# Concept Hierarchy Placement Candidates — Conservative candidate generation

Generated: `2026-05-21T04:49:18Z`

> Conservative candidate taxonomy only. These rows are **not** accepted taxonomy and must go through Candidate adjudication before any dry-run/writeback.

## Summary

- deferred_rows_considered: 27
- approved_parent_count: 16
- generated_candidates: 2
- suppressed_signals: 25
- candidate_targets: `{"Agent Workflow": 2}`
- adjudication_items: 2
- open_writeback: 0
- dry_run_planned: 0

## Policy

- candidate_scope: Only Initial triage/3 deferred rows are considered in Conservative candidate generation.
- allowed_targets:
  - Agent Evaluation Benchmark
  - Agent Framework
  - Agent Workflow
  - Benchmark
  - Chunking
  - Evaluation
  - Memory
  - Multi-Route Retrieval
  - Observability
  - Query Rewrite
  - RAG
  - RAG Evaluation
  - Reranking
  - Retriever
  - Sparse Retrieval
  - Tool Use
- forbidden_inputs:
  - topic overlap alone
  - body wikilink once
  - same raw source
  - title similarity without approved parent
  - component-of / supports / standardizes / executes / protects relations
  - proposed anchors that Parent-whitelist review did not approve
  - missing phantom parents such as Prompting or Retrieval
- write_policy: No writeback in Conservative candidate generation. Candidates feed Candidate adjudication only.

## Candidates for Candidate adjudication review

| Source | Candidate parent | Confidence | Support | Rationale |
|---|---|---|---|---|
| [[Approval Gate]] | [[Agent Workflow]] | low | definition_control_point_before_high_risk_action, parent_possible_parent_is_approved, parent_route_precheck_workflow_candidate | Conservative Conservative candidate generation candidate from Parent-whitelist review route precheck plus card text/title signals. This is not accepted taxonomy until Candidate adjudication. |
| [[ReAct]] | [[Agent Workflow]] | low | body_distinguishes_agent_loop_from_workflow, body_plain_count:2, body_wikilink_count:2, parent_possible_parent_is_approved, parent_route_precheck_workflow_candidate | Conservative Conservative candidate generation candidate from Parent-whitelist review route precheck plus card text/title signals. This is not accepted taxonomy until Candidate adjudication. |

## Suppressed signals

| Source | Suppressed target | Signal | Reason |
|---|---|---|---|
| [[A2A]] | [[Agent]] | broad_anchor_not_approved | A2A is a protocol/ecosystem card. `Agent` is intentionally not an auto-approved parent, and no approved protocol parent exists. |
| [[ACP]] | [[Agent]] | broad_anchor_not_approved | ACP is a protocol/ecosystem card. `Agent` is intentionally not an auto-approved parent, and no approved protocol parent exists. |
| [[Agent Skills]] |  | no_conservative_approved_parent_signal | No conservative signal points to a Parent-whitelist review approved stable parent. |
| [[Browser Agent]] | [[Agent]] | broad_anchor_not_approved | The title suggests a kind of Agent, but `Agent` is too broad for automatic parent generation. |
| [[Code Execution Sandbox]] | [[Tool Use]] | security_runtime_not_tool_behavior | A sandbox supports safe tool/code execution, but support/infrastructure is not a kind of Tool Use. |
| [[Data Exfiltration]] | [[Prompt]] | security_risk_not_prompt | Data exfiltration can occur through prompts/tools/retrieval, but it is a risk class, not a kind of Prompt. |
| [[Entity Resolution]] | [[Knowledge Graph]] | supports_graph_not_graph | Entity resolution can support knowledge graphs, but support/use is not strict taxonomy; Knowledge Graph is also not auto-approved. |
| [[GUI Grounding]] | [[Agent]] | capability_not_broad_agent_parent | GUI grounding is a capability used by computer-use agents, not automatically a kind of Agent. |
| [[KV Cache]] |  | no_conservative_approved_parent_signal | No conservative signal points to a Parent-whitelist review approved stable parent. |
| [[Least Privilege Tools]] | [[Tool Use]] | policy_principle_not_tool_behavior | Least-privilege tooling constrains Tool Use, but the policy principle itself is not automatically a Tool Use subtype. |
| [[MCP]] | [[Tool Use]] | protocol_not_tool_behavior | MCP standardizes tool/context connection; protocol/support is not a kind of Tool Use. |
| [[MCP Registry]] | [[MCP]] | unapproved_parent | MCP Registry likely belongs near MCP, but MCP is not an approved parent in Conservative candidate generation. |
| [[MCP Transport]] |  | no_conservative_approved_parent_signal | No conservative signal points to a Parent-whitelist review approved stable parent. |
| [[Multi-Head Attention]] | [[Transformer]] | component_of_not_kind_of | Multi-Head Attention is a Transformer mechanism/component, not a kind of Transformer. |
| [[NLP]] |  | no_conservative_approved_parent_signal | No conservative signal points to a Parent-whitelist review approved stable parent. |
| [[Observation]] | [[Agent Workflow]] | loop_signal_not_workflow | Observation is an agent-loop feedback signal; being used inside workflows is not strict taxonomy. |
| [[Obsidian + LLM Wiki]] | [[RAG]] | local_system_not_rag_subtype | The local wiki may use retrieval-like ideas, but the project/workflow artifact is not a kind of RAG. |
| [[Oh My Codex (OMX)]] | [[Agent Framework]] | product_runtime_not_framework_subtype_without_review | OMX is a concrete Codex orchestration/runtime ecosystem; candidate generation must not classify it as Agent Framework without product-boundary review. |
| [[Policy Engine]] | [[Tool Use]] | policy_layer_not_tool_behavior | A policy engine constrains tools/actions; constraint layer is not a kind of Tool Use. |
| [[Positional Encoding]] | [[Transformer]] | component_of_not_kind_of | Positional Encoding is a Transformer mechanism/component, not a kind of Transformer. |
| [[Prompt Injection]] | [[Prompt]] | attack_class_not_prompt | Prompt Injection manipulates prompts but is an attack class, not a kind of Prompt. |
| [[Sandbox Workspace]] | [[Tool Use]] | workspace_runtime_not_tool_behavior | A sandbox workspace hosts actions/tools; hosting infrastructure is not a Tool Use subtype. |
| [[Self-Attention]] | [[Transformer]] | component_of_not_kind_of | Self-Attention is a Transformer mechanism/component, not a kind of Transformer. |
| [[Step-back Prompting]] |  | no_conservative_approved_parent_signal | No conservative signal points to a Parent-whitelist review approved stable parent. |
| [[Trajectory]] | [[Evaluation]] | evaluated_object_not_evaluation_method | Trajectory can be evaluated or observed, but the path/object being evaluated is not itself Evaluation. |

## Next command

```bash
python3 scripts/concept_taxonomy/taxonomy_placement_review.py --check
# then Candidate adjudication: LLM adjudication of these candidates; do not write cards yet
```

