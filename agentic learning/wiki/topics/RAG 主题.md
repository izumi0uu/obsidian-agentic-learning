---
type: map
topic:
  - rag
status: active
created: 2026-05-05
updated: 2026-05-12
related:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[RAG 类型对比]]"
  - "[[Context RAG Memory 对比]]"
  - "[[Retrieval 组件对比]]"
  - "[[Obsidian + LLM Wiki]]"
---

# RAG 主题

这个主题页聚合所有 `topic` 包含 `rag` 的笔记。

## 先看这个

- [[RAG 类型对比]]：不同 RAG 类型的横向对比。
- [[Context RAG Memory 对比]]：区分 context engineering、RAG、memory 和 repo context 的上下文供给边界。
- [[Retrieval 组件对比]]：区分 ingestion、embedding、vector database、retriever、hybrid search 和 reranking 的 pipeline 位置。
- [[Neo4j GraphRAG 官方文档]]：GraphRAG / Knowledge Graph RAG 的重要工程主源之一。
- [[Neo4j]]：GraphRAG 的重要工程实现生态，不是一个独立 RAG 方法名。

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "rag")
SORT file.name ASC
```

## 下一批概念

- [x] [[Retriever]]
- [x] [[Parametric Memory]]
- [x] [[Non-Parametric Memory]]
- [x] [[RAG 类型对比]]
- [ ] embedding
- [ ] vector database
- [ ] chunking
- [ ] retrieval
- [ ] reranking
- [x] [[Neo4j]]
- [ ] Knowledge Graph
- [ ] Hybrid Search

## 关键边界

RAG 能让 LLM 使用外部资料，但不能保证资料完整、检索正确或模型解释无误。

另一个重要边界：[[Neo4j]] 是 GraphRAG 的工程工具和图数据库生态，不是和 [[Self-RAG]]、[[Corrective RAG]] 平级的方法名。
