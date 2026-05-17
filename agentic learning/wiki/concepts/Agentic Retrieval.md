---
type: concept
topic:
  - rag
  - retrieval
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-16
up:
  - "[[Retriever]]"
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Azure AI Search Agentic Retrieval]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Azure AI Search Agentic Retrieval#为什么收]]"
  - "[[Azure AI Search Agentic Retrieval#一句话]]"
  - "[[Azure AI Search Agentic Retrieval#边界提醒]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[Agentic RAG]]"
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Evaluation]]"
---

# Agentic Retrieval

## 一句话

Agentic Retrieval 是让检索层具备 query planning、子问题分解、多源选择、并行检索和结果合并能力。

## 概念详解

Agentic Retrieval 出现的原因是：复杂问题很少只对应一个 query。用户可能要求比较多个框架、跨多个数据源找证据、按时间过滤、同时检索文档和知识库，或者先拆出几个子问题再回答。普通 retriever 把原问题直接送进 top-k，容易漏掉维度或把不同来源混在一起。

Azure AI Search 的 source note 把 agentic retrieval 描述成面向复杂问题和 agent workflow 的多查询检索管线：LLM 做 query planning，把问题拆成多个子查询，面向 knowledge source / knowledge base 执行 retrieve action，再把 grounding data 返回给下游 chat 或 Agent 应用。这说明它更偏检索层的规划和执行，而不是完整 Agent 行动系统。

和 [[Agentic RAG]] 的边界：Agentic Retrieval 负责“怎么查”，Agentic RAG 还包括是否查、查完是否重试、如何生成、是否调用工具、如何引用、何时停止等完整流程。和 [[Retriever]] 的边界：普通 retriever 可以是单次 query；agentic retrieval 把 query planning、多源检索、并行子查询和结果合并显式化。

它的现代性是 frontier/watch：作为模式已经进入官方文档和框架实践，但具体产品能力、preview 状态、价格、可用区域、query planner 行为和 API 名称会变化。学习时要保留可迁移抽象：复杂问题的检索规划；不要把 Azure 的具体字段写成通用定义。

## 它解决什么问题

普通 RAG 常常把用户问题当成一个 query，然后取 top-k 文档。复杂问题会失败，因为它可能包含多个子问题、隐含上下文、不同数据源和需要合并的证据。

Agentic Retrieval 让检索不再只是“搜索一次”，而是先判断信息需求，再生成多个子查询，执行检索、排序、合并 grounding data。

## 它不是什么

它不是完整 Agent。

它也不等于 [[Agentic RAG]]。Agentic Retrieval 更偏检索层；Agentic RAG 更偏整个回答系统，包括是否检索、检索后是否重试、如何生成和引用。

## 最小例子

用户问：“比较 LangGraph 和 OpenAI Agents SDK 在 memory、tracing、human-in-the-loop 上的差别。”

Agentic Retrieval 会拆成：LangGraph memory/tracing/HITL；OpenAI Agents SDK memory/tracing/HITL；对比维度和边界。然后并行检索、rerank，并把引用来源和 query plan 返回给回答层。

## 常见误解 / 风险

- 更复杂不一定更好：它会增加延迟和成本。
- query plan 错了，后面检索再强也会偏。
- 检索结果仍然需要引用、评分和失败复现。
- 对简单事实问题，普通 hybrid search 可能已经足够。

## 边界细节

Agentic Retrieval 的核心是检索层的 planning，不是所有 Agent 行动。

和 [[Hybrid Search]] 的边界：hybrid search 合并语义和关键词信号；agentic retrieval 先规划多个信息需求，再选择检索动作。

和 [[Self-RAG]] 的边界：Self-RAG 关注模型是否检索和证据批判的训练/控制信号；agentic retrieval 关注检索产品或系统层的 query planning。

## 现代性状态

- 判定：frontier / current-practice。
- 稳定部分：复杂问题需要 query planning、子查询和多源 grounding。
- 易变部分：Azure AI Search 等产品的 API、preview 状态、价格、query planner 行为和集成方式。
- freshness: watch。
- last_checked: 2026-05-10。
- 复查点：产品文档变化时更新 source note；概念卡只保留检索层规划的稳定边界。

## 现代系统怎么吸收 Agentic Retrieval 的价值

现代系统会把 agentic retrieval 的 plan、子查询、候选结果和合并结果写入 trace。这样回答错时能定位：是问题拆错、知识源选错、检索漏召回、rerank 排错，还是 generator 误读证据。

## 证据锚点

- Source: [[Azure AI Search Agentic Retrieval]]
- Anchor: [[Azure AI Search Agentic Retrieval#为什么收]]
- Anchor: [[Azure AI Search Agentic Retrieval#一句话]]
- Anchor: [[Azure AI Search Agentic Retrieval#边界提醒]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: official docs source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: Azure source supports one official product framing; broader agentic retrieval as a transferable pattern is engineering synthesis and must be separated from Azure-specific implementation details.

## 复习触发

- Agentic Retrieval 和 Agentic RAG 的边界是什么？
- query plan 错误会怎样影响后续 RAG？
- 简单事实问题为什么未必需要 Agentic Retrieval？

## 相关链接

- [[Agentic RAG]]
- [[RAG]]
- [[Retriever]]
- [[Trace]]
- [[Observability]]
