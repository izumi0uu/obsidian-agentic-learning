---
type: source
source_type: docs
title: "Neo4j GraphRAG Developer Guide"
url: "https://neo4j.com/developer/genai-ecosystem/"
author: Neo4j
site: neo4j.com
topic:
  - rag
  - graph
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[GraphRAG]]"
  - "[[Neo4j]]"
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[RAG 类型对比]]"
---

# Neo4j GraphRAG 官方文档

## 为什么收

Neo4j 是 GraphRAG / Knowledge Graph RAG 方向的重要工程主源之一。它不是一个新的 RAG “概念名”，而是图数据库、知识图谱构建、向量索引、全文搜索、Cypher 查询和图遍历结合起来的实现生态。

补收它是为了修正当前前沿来源里的缺口：之前只收了 Microsoft GraphRAG 和 Azure Agentic Retrieval，少了 Neo4j 这条图数据库实践线。

## 一句话

Neo4j GraphRAG 关注如何用 Neo4j 知识图谱、向量搜索、全文搜索和图遍历增强 RAG 的检索层。

## 先读什么

- GraphRAG Developer Guide：看 Neo4j 对 GraphRAG 的整体定位。
- Neo4j GraphRAG Python Package：看如何在 Python 里构建 GraphRAG 应用，文档入口是 <https://neo4j.com/docs/neo4j-graphrag-python/current/>。
- LLM Knowledge Graph Builder：看如何从 PDF、网页、文档等非结构文本抽取实体、关系和 chunk，仓库是 <https://github.com/neo4j-labs/llm-graph-builder>。
- Vector index / fulltext / hybrid search：理解图检索不只是图遍历，也可以和向量、关键词检索组合。

## 可以拆成概念卡

已建 [[Neo4j]] 概念卡。这个 source note 继续作为 [[GraphRAG]] 和 [[RAG 类型对比]] 的工程主源。

- [[GraphRAG]]
- [[Neo4j]]
- [[RAG]]
- [[Retriever]]
- [[RAG 类型对比]]

## 我的疑问

- 什么时候值得用 Neo4j 做 GraphRAG，而不是普通向量数据库 + reranker？
- 文档抽取成图时，schema 应该预先设计，还是让 LLM 自动抽？
- 图遍历、vector search、fulltext search 和 Text2Cypher 应该如何组合？
- Neo4j GraphRAG 对中文文档、表格、PDF 图表的效果如何？

## 边界提醒

Neo4j 是 GraphRAG 的重要实现工具，不等于 GraphRAG 本身。

GraphRAG 的关键问题不是“用了 Neo4j 就高级”，而是：

- 图里的实体和关系是否可靠。
- 图 schema 是否适合任务。
- 检索时是否真的利用了关系结构。
- 构图成本和查询延迟是否值得。
