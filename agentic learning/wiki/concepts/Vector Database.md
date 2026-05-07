---
type: concept
topic:
  - rag
  - infrastructure
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Embedding]]"
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
---

# Vector Database

## 一句话

Vector Database 是为 embedding 向量检索设计的数据库或索引系统，常用于 RAG 从大量文档片段中找语义相似内容。

## 它解决什么问题

RAG 需要从外部知识库里快速找相关材料。普通数据库擅长精确查询，向量数据库擅长近似语义搜索、metadata filter、top-k 召回和大规模索引管理。

代表生态包括 Pinecone、Weaviate、Qdrant、Milvus，以及云厂商搜索/数据库里的 vector index。

## 它不是什么

Vector Database 不是 RAG 本身。

它也不是唯一检索方式。生产系统经常需要 [[Hybrid Search]]、reranking、图检索、权限过滤和引用校验。

## 最小例子

```text
文档 -> chunk -> embedding -> vector database -> top-k chunks -> LLM answer
```

## 常见误解和风险

- 误解：向量相似就等于答案正确。
- 误解：换一个向量库就能解决 RAG 质量问题。
- 风险：metadata filter、权限、删除和更新没有设计好，会泄露或召回旧资料。
- 风险：chunk 太差时，向量库只能更快地找出差上下文。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Embedding]]
- [[Chunking]]
- [[Retriever]]
- [[Hybrid Search]]
