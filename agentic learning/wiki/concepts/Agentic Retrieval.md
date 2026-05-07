---
type: concept
topic:
  - rag
  - retrieval
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Azure AI Search Agentic Retrieval]]"
evidence:
  - "[[Azure AI Search Agentic Retrieval#为什么收]]"
related:
  - "[[Agentic RAG]]"
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Evaluation]]"
---

# Agentic Retrieval

## 一句话

Agentic Retrieval 是让检索层具备 query planning、子问题分解、多源选择、并行检索和结果合并能力。

## 它解决什么问题

普通 RAG 常常把用户问题当成一个 query，然后取 top-k 文档。复杂问题会失败，因为它可能包含多个子问题、隐含上下文、不同数据源和需要合并的证据。

Agentic Retrieval 让检索不再只是“搜索一次”，而是先判断信息需求，再生成多个子查询，执行检索、排序、合并 grounding data。

## 它不是什么

它不是完整 Agent。

它也不等于 [[Agentic RAG]]。Agentic Retrieval 更偏检索层；Agentic RAG 更偏整个回答系统，包括是否检索、检索后是否重试、如何生成和引用。

## 最小例子

用户问：“比较 LangGraph 和 OpenAI Agents SDK 在 memory、tracing、human-in-the-loop 上的差别。”

Agentic Retrieval 会拆成：

- LangGraph memory/tracing/HITL。
- OpenAI Agents SDK memory/tracing/HITL。
- 对比维度和边界。

然后并行检索、rerank，并把引用来源和 query plan 返回给回答层。

## 常见误解 / 风险 / 边界细节

- 更复杂不一定更好：它会增加延迟和成本。
- query plan 错了，后面检索再强也会偏。
- 检索结果仍然需要引用、评分和失败复现。
- 对简单事实问题，普通 hybrid search 可能已经足够。

## 证据锚点

- Source: [[Azure AI Search Agentic Retrieval]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agentic RAG]]
- [[RAG]]
- [[Retriever]]
- [[Trace]]
- [[Observability]]
