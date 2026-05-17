---
type: concept
topic:
  - rag
  - retrieval
  - agent
status: growing
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: watch
source:
  - "[[Azure AI Search Agentic Retrieval]]"
  - "[[Agentic Retrieval]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Azure AI Search Agentic Retrieval#为什么收]]"
  - "[[Azure AI Search Agentic Retrieval#一句话]]"
  - "[[Azure AI Search Agentic Retrieval#边界提醒]]"
  - "[[Agentic Retrieval#证据锚点]]"
related:
  - "[[Query Rewrite]]"
  - "[[Multi-Query Retrieval]]"
  - "[[Step-back Prompting]]"
  - "[[Agentic Retrieval]]"
  - "[[Agentic RAG]]"
  - "[[Retriever]]"
---

# Query Planning

## 一句话

Query Planning 是在检索前把复杂问题拆成检索步骤、子查询和知识源选择的过程；它比 query rewrite 更像检索层的轻量计划。

## 概念详解

当用户问题简单时，一个 query 就够了；但复杂问题可能包含多个实体、时间范围、比较维度或隐含依赖。Query Planning 会先判断需要查哪些子问题、每个子问题去哪类知识源查、是否并行检索、如何合并 grounding data，再把结果交给回答生成或 Agent workflow。

[[Azure AI Search Agentic Retrieval]] 的 source note 把 agentic retrieval 概括为由 LLM 做 query planning、并行执行多个子查询、排序并合并 grounding data。这说明 query planning 是现代检索从单次 top-k 向多步检索演化的关键动作。它仍然属于 retrieval layer，不必等同于完整 [[Agentic RAG]]：有些系统只把 planning 用在搜索内部，不让 Agent 自主行动。

工程综合：Query Planning 的学习价值在于切开“改写一个 query”和“设计一组检索动作”。前者解决表达问题，后者解决任务结构问题。

Query Planning 比 Query Rewrite 更接近任务分解：它不只是把一句话换个说法，而是决定要查几个子问题、它们之间是否有依赖、是否需要不同索引或工具、哪些结果先回来才能继续下一步。现代 agentic retrieval 会把计划、执行、检查和合并连成 loop。风险是计划过度复杂：如果每个简单问题都拆成很多查询，会增加延迟、成本和噪音。
## 它解决什么问题

它解决复杂问题一次检索不够的问题，例如跨多个文档比较、需要查定义再查实现、需要分别查政策和例外条款，或者需要从多个知识源收集证据。

## 它不是什么

Query Planning 不是完整任务规划。它只规划检索步骤，不负责工具副作用、写文件、发邮件或长期执行。

它也不是 [[Query Rewrite]]。Rewrite 是改表达；planning 是拆任务、选知识源和安排检索顺序。

## 最小例子

```text
问题：LangGraph 和 CrewAI 在 human-in-the-loop 上有什么不同？
plan:
  1. 查 LangGraph human-in-the-loop / interrupt / checkpoint
  2. 查 CrewAI guardrails / human input / flows
  3. 对比 runtime state vs crew/flow 边界
```

## 常见误解 / 风险

- 误解：多拆几个子查询一定更好。过度拆解会增加延迟和噪音。
- 误解：Query Planning 就是 Agent。它可能只是搜索服务内部能力。
- 风险：计划阶段丢掉用户原始意图，后续检索全偏。
- 风险：选择错误知识源，导致看似系统性但实际遗漏关键证据。

## 边界细节

和 [[Agentic Retrieval]] 的边界：Query Planning 是 agentic retrieval 的核心动作之一；Agentic Retrieval 还包括多源检索、排序、合并和返回 grounding data。

和 [[Agentic RAG]] 的边界：Agentic RAG 可能围绕任务目标多轮查证、评价和重查；Query Planning 只负责检索计划。

和 [[RAG Evaluation]] 的边界：query plan 应被 trace 和 eval 检查，否则计划看起来合理但召回失败无法定位。

和 [[Multi-Query Retrieval]] / [[Step-back Prompting]] 的边界：multi-query 和 step-back 可以是 query plan 里的具体动作，但它们本身不等于 plan。planning 要决定是否需要这些动作、以什么顺序执行、结果如何合并。

## 现代性状态

- 判定：current-practice / frontier-watch。
- 稳定部分：复杂问题需要子查询和知识源选择。
- 易变部分：各搜索产品的 query planning API、计划可解释性、并行检索和计费模型会变化。
- 复查点：不要把某个供应商的 agentic retrieval preview 能力写成通用事实。

## 现代系统怎么吸收 Query Planning 的价值 / 局限

现代系统会把 query plan 记录到 trace：原始问题、子查询、知识源、召回结果、合并策略和最终答案。这样可以评估每一步是否有必要、是否命中期望证据、是否增加不必要成本。

局限是 planning 本身由模型生成时会带来不确定性；简单事实查询不应该因为“agentic”而被强行拆解。

## 证据锚点

- Source anchor: [[Azure AI Search Agentic Retrieval#为什么收]]
- Source anchor: [[Azure AI Search Agentic Retrieval#一句话]]
- Source anchor: [[Azure AI Search Agentic Retrieval#边界提醒]]
- Concept anchor: [[Agentic Retrieval#证据锚点]]
- Evidence type: official source note + existing concept synthesis + engineering inference.

- Boundary: Query Planning 是检索任务规划，不等于 Query Rewrite、Multi-Query Retrieval、Reranking 或最终答案规划。
## 复习触发

1. Query Planning 为什么不等于完整 Agent planning？
2. 什么时候一个问题值得拆成多个检索子查询？
3. query plan 进入 trace 后，RAG Evaluation 可以检查什么？

## 相关链接

- [[Query Rewrite]]
- [[Multi-Query Retrieval]]
- [[Step-back Prompting]]
- [[Agentic Retrieval]]
- [[Agentic RAG]]
- [[Retriever]]
- [[Query Rewrite Query Planning Agentic Retrieval 对比]]
