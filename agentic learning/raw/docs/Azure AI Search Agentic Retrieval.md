---
type: source
source_type: docs
title: "Agentic retrieval in Azure AI Search"
url: "https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview"
author: Microsoft
site: learn.microsoft.com
topic:
  - rag
  - retrieval
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Agentic Retrieval]]"
  - "[[Agentic RAG]]"
  - "[[Retriever]]"
---

# Azure AI Search Agentic Retrieval

## 为什么收

这是 [[Agentic Retrieval]] 的高质量主源之一。它把检索从“单次 query -> top-k 文档”推进到“由 LLM 做 query planning，再并行执行多个子查询、排序、合并 grounding data”的模式。

## 一句话

Azure AI Search 的 agentic retrieval 是面向复杂问题和 agent workflow 的多查询检索管线。

## 先读什么

- Overview：理解 query planning、knowledge source、knowledge base、retrieve action。
- Query a knowledge base：看它如何作为下游 Agent 或 Chat 应用的知识层。
- Pricing / availability：注意它目前带有 preview 和成本边界。

## 可以拆成概念卡

- [[Agentic Retrieval]]
- [[Agentic RAG]]
- [[Retriever]]

## 我的疑问

- Agentic retrieval 是搜索产品能力，还是一种可迁移的 RAG 架构模式？
- query plan 应该暴露给用户、开发者，还是只留给 observability？

## 边界提醒

它不是“所有 RAG 都应该这样做”。复杂问题、多轮上下文、多源检索时更值得用；简单事实查询可能会被额外 planning 成本拖慢。
