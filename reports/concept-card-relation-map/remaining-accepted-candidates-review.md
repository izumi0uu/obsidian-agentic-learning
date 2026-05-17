# Remaining Accepted Candidates Review

Generated: `2026-05-16T09:07:43Z`

> 本报告审查上一轮 dry-run 中剩余 15 条 accepted candidates；本轮只审查和重判，不执行第二批 apply。

## Summary

- reviewed_original_remaining_accepted: 15
- keep_accept_taxonomy: 13
- reclassified_reject_taxonomy: 2
- ready_after_review: 13
- apply_performed: False
- policy: Accepted is not auto-apply; every remaining accepted row must survive a second semantic review before small-batch writeback.

## Reviewed rows

| Source | Target | Verdict | Writeback | Rationale | Review note |
|---|---|---|---|---|---|
| [[Long-term Memory]] | [[Memory]] | keep_accept_taxonomy | add_up `up` | Long-term memory is the broader cross-session memory capability. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Microsoft Agent Framework]] | [[Agent Framework]] | keep_accept_taxonomy | add_up `up` | Microsoft Agent Framework is a named agent SDK/framework route. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Non-Parametric Memory]] | [[Memory]] | keep_accept_taxonomy | add_up `up` | Non-parametric memory is external retrievable memory outside model weights. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[OpenTelemetry GenAI]] | [[Observability]] | reclassified_reject_taxonomy | none `related or relations, not up` | OpenTelemetry GenAI is a semantic-convention/standardization layer that supports observability; it is not itself an observability capability subtype. | 降级：它是 GenAI/Agent 事件的 OpenTelemetry 语义约定/标准层，支撑 Observability，但不是 observability capability 的一种。 |
| [[RAG Evaluation]] | [[Evaluation]] | keep_accept_taxonomy | add_up `up` | RAG Evaluation is a subtype of evaluation focused on retrieval/context/citation/answer quality. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Self-RAG]] | [[RAG]] | keep_accept_taxonomy | add_up `up` | Self-RAG is a RAG method family with adaptive retrieval/generation/critique. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Semantic Memory]] | [[Memory]] | keep_accept_taxonomy | add_up `up` | Semantic memory is a subtype of memory for stable facts/preferences/concepts. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[State Graph Runtime]] | [[Agent Workflow]] | reclassified_reject_taxonomy | none `related or relations, not up` | State Graph Runtime executes and persists workflows; runtime infrastructure is adjacent to Agent Workflow, not a workflow subtype. | 降级：它是执行/持久化 workflow 的 runtime infrastructure；Agent Workflow 是流程结构，runtime 不是流程的子类。 |
| [[Tool Calling]] | [[Tool Use]] | keep_accept_taxonomy | add_up `up` | Tool Calling is a structured form of tool use. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Trajectory Evaluation]] | [[Evaluation]] | keep_accept_taxonomy | add_up `up` | Trajectory Evaluation is evaluation of an agent's action process rather than only final output. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Computer Use]] | [[Tool Use]] | keep_accept_taxonomy | add_up `up` | Computer Use is a tool-use mode where the agent operates browser/desktop/terminal surfaces. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Data-first Agent Framework]] | [[Agent Framework]] | keep_accept_taxonomy | add_up `up` | Data-first Agent Framework is explicitly a framework route centered on data/RAG primitives. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Graph Construction Evaluation]] | [[Evaluation]] | keep_accept_taxonomy | add_up `up` | Graph Construction Evaluation is a subtype of evaluation for graph/RAG construction quality. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Multi-agent Orchestration]] | [[Agent Workflow]] | keep_accept_taxonomy | add_up `up` | Multi-agent orchestration is a workflow/coordination pattern for multiple agents. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |
| [[Parametric Memory]] | [[Memory]] | keep_accept_taxonomy | add_up `up` | Parametric memory is memory encoded inside model parameters. | 保留：子卡一句话/边界支持“X 是 Y 的一种/成员/子方向”，且不是支撑、执行、标准化或组合关系。 |

## Reclassified out of accepted

### [[OpenTelemetry GenAI]] -> [[Observability]]

- Decision: `reject_taxonomy` / writeback `none`
- Why: 降级：它是 GenAI/Agent 事件的 OpenTelemetry 语义约定/标准层，支撑 Observability，但不是 observability capability 的一种。
- Source one-line: OpenTelemetry GenAI 是 OpenTelemetry 为生成式 AI 调用、token、模型、工具和 Agent 事件定义的观测语义约定方向。
- Boundary excerpt: OpenTelemetry GenAI 和相邻概念的边界： - [[Trace]]：一条具体执行记录；OTel GenAI 规定这类记录的语义字段怎么表达。 - [[Observability]]：围绕 trace/metrics/logs 的平台能力；OTel 是数据标准和传输生态的一部分。 - [[Replay]]：用保存的输入、工具结果或环境快照重放；OTel trace 能提供线索，但未必包含 replay 所需的全部可复现状态。 - [[Evaluation]]：判断质量；OTel 只是提供可供 evaluator 使用的过程证据。 当概念卡或工程设计提到 OTel 时，要问清楚：是在讨论语义约定、传输协议、collector、平台集成，还是评测数据消费？这些层不要混成一个词。

### [[State Graph Runtime]] -> [[Agent Workflow]]

- Decision: `reject_taxonomy` / writeback `none`
- Why: 降级：它是执行/持久化 workflow 的 runtime infrastructure；Agent Workflow 是流程结构，runtime 不是流程的子类。
- Source one-line: State Graph Runtime 是把 Agent / workflow 的执行过程显式建模为“状态 + 节点 + 边 + 路由 + checkpoint”的运行时，让长任务可以循环、分支、暂停、恢复和审计。
- Boundary excerpt: State Graph Runtime 最适合需要循环、分支、恢复、审批、长任务和审计的场景。它和 [[Agent Workflow]] 的关系是：workflow 是路径/任务结构，runtime 是执行和恢复这条路径的软件层；它和 [[Agent State]] 的关系是：state 是数据，runtime 负责何时读取、更新、保存和投影这些数据。 与 provider SDK 的差异：OpenAI Agents SDK 等可以封装 Agent、tools 和 handoffs，但不一定要求你显式画状态图；State Graph Runtime 更强调控制流和状态恢复。


## Ready candidates after review

- [[Long-term Memory]] -> [[Memory]] (high): Long-term memory is the broader cross-session memory capability.
- [[Microsoft Agent Framework]] -> [[Agent Framework]] (high): Microsoft Agent Framework is a named agent SDK/framework route.
- [[Non-Parametric Memory]] -> [[Memory]] (high): Non-parametric memory is external retrievable memory outside model weights.
- [[RAG Evaluation]] -> [[Evaluation]] (high): RAG Evaluation is a subtype of evaluation focused on retrieval/context/citation/answer quality.
- [[Self-RAG]] -> [[RAG]] (high): Self-RAG is a RAG method family with adaptive retrieval/generation/critique.
- [[Semantic Memory]] -> [[Memory]] (high): Semantic memory is a subtype of memory for stable facts/preferences/concepts.
- [[Tool Calling]] -> [[Tool Use]] (high): Tool Calling is a structured form of tool use.
- [[Trajectory Evaluation]] -> [[Evaluation]] (high): Trajectory Evaluation is evaluation of an agent's action process rather than only final output.
- [[Computer Use]] -> [[Tool Use]] (medium): Computer Use is a tool-use mode where the agent operates browser/desktop/terminal surfaces.
- [[Data-first Agent Framework]] -> [[Agent Framework]] (medium): Data-first Agent Framework is explicitly a framework route centered on data/RAG primitives.
- [[Graph Construction Evaluation]] -> [[Evaluation]] (medium): Graph Construction Evaluation is a subtype of evaluation for graph/RAG construction quality.
- [[Multi-agent Orchestration]] -> [[Agent Workflow]] (medium): Multi-agent orchestration is a workflow/coordination pattern for multiple agents.
- [[Parametric Memory]] -> [[Memory]] (medium): Parametric memory is memory encoded inside model parameters.
