---
type: concept
topic:
  - rag
  - retrieval
  - search
  - embedding
status: growing
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: stable
conflicts: []
aliases:
  - semantic search
  - 语义搜索
  - semantic retrieval
  - 语义检索
source:
  - "[[AI Engineering From Scratch - Embeddings]]"
  - "[[Embedding]]"
  - "[[Dense Retrieval]]"
evidence:
  - "[[AI Engineering From Scratch - Embeddings#为什么收]]"
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[Embedding#概念详解]]"
  - "[[Dense Retrieval#概念详解]]"
related:
  - "[[Embedding]]"
  - "[[Dense Retrieval]]"
  - "[[Sparse Retrieval]]"
  - "[[Hybrid Search]]"
  - "[[Vector Database]]"
  - "[[Retriever]]"
  - "[[RAG]]"
---

# Semantic Search

## 一句话

Semantic Search 是按语义相似而不是只按关键词重叠来找资料的检索方式，常通过 [[Embedding]] 和 [[Dense Retrieval]] 实现。

## 概念详解

Semantic Search 出现的核心原因是 vocabulary mismatch：用户说法和文档说法可能完全不同，但表达的是同一件事。用户说“付款没成功”，历史工单可能写“transaction failed”“charge was declined”“billing error”。关键词检索如果只看词面重叠，会漏掉许多语义等价或相近的材料。

Embedding 提供了 semantic search 的常见表示层：把 query 和 document chunk 都映射到同一个向量空间，再用 [[Vector Similarity Metrics]] 找相近候选。这样系统不需要 query 和文档拥有完全相同的词，也能按语义方向召回候选。

但 semantic search 不是“理解一切”。它擅长找语义相似，可能不擅长精确实体、错误码、产品型号、函数名、表字段、时间范围和权限条件。因此生产 RAG 常把 semantic search 与 [[Sparse Retrieval]] / [[BM25]] 组成 [[Hybrid Search]]，再用 [[Reranking]] 重新排序候选。

和 [[RAG]] 的关系是：semantic search 可以是 RAG 的 retrieval 实现之一，但 RAG 还包括文档 ingestion、chunking、metadata、权限、上下文组装、答案生成、引用和评估。一个系统可以有 semantic search 但没有完整 RAG，也可以做 RAG 时混用关键词、SQL、图检索和人工规则。

从实现角度看，它要求 query 和 document 被放进可比较的表示空间。最常见做法是离线把文档 chunk 编成向量并建索引，在线把用户 query 编成向量后检索近邻；但很多系统还会保留原始关键词路径，因为用户有时输入的是 ID、报错串或专有名词，这些信号不应被语义表示稀释掉。

## 它解决什么问题

它解决用户 query 和知识库文字“表达不同但意思相近”的召回问题。它让搜索从词面匹配扩展到语义匹配。

## 它不是什么

Semantic Search 不是 [[RAG]] 本身。它只是找资料的方式之一。

它也不是 [[Embedding]] 本身。Embedding 生成语义向量；semantic search 是用这些向量或其他语义表示来检索。

它更不是事实校验。语义相近的资料仍可能过期、无权限、不能回答问题或引用不支持结论。

## 最小例子

```text
query: "我的付款没成功"
semantic hit: "交易被拒绝时请检查银行卡状态"
keyword miss: 文档没有出现“付款”“没成功”
```

## 常见误解 / 风险

- 以为语义搜索总比关键词搜索高级：在错误码、法规条款、产品型号和代码符号场景，关键词/全文检索可能更稳。
- 以为相似度高就能回答问题：相似可能只是主题接近，不代表包含答案。
- 忽略 query rewrite：用户表达和文档表达角度差太远时，semantic search 也可能漏召回。
- 忽略权限和 freshness：semantic search 会找到“相似资料”，但不自动判断是否可用。

## 边界细节

和 [[Dense Retrieval]] 的边界：Dense Retrieval 是 semantic search 的常见向量召回路线；semantic search 是更宽的任务/体验目标。

和 [[Sparse Retrieval]] 的边界：sparse retrieval 看词项、倒排和精确匹配；semantic search 看语义相似。生产系统常把二者组合。

和 [[Retriever]] 的边界：retriever 是组件或流程，可能包含 semantic search、keyword search、metadata filter、query rewrite、rerank 和权限过滤。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：用语义表示弥补词汇不匹配，是现代搜索和 RAG 的核心能力之一。
- 易变部分：embedding 模型、向量库、hybrid search、reranker 和产品实现。
- 复查点：语义搜索是否有效，要用业务 query 和标注资料评估，不只看 demo。

## 现代系统怎么吸收 Semantic Search 的价值

现代 RAG 通常把 semantic search 作为初召回路线之一，并用 sparse route、filter、rerank 和 evaluation 约束它。真正的工程目标不是“只用向量”，而是让正确证据更稳定地进入上下文预算。

## 证据锚点

- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchors: [[AI Engineering From Scratch - Embeddings#为什么收]], [[AI Engineering From Scratch - Embeddings#关键事实]]
- Existing cards: [[Embedding#概念详解]], [[Dense Retrieval#概念详解]]
- Evidence type: course source note + existing concept-card synthesis + engineering synthesis.
- Confidence: medium-high.
- Boundary: 本卡记录语义检索任务边界，不把 semantic search 等同于 RAG、vector database 或事实正确性。

## 复习触发

1. Semantic search 解决的 vocabulary mismatch 是什么？
2. 为什么 semantic search 仍然需要 BM25 / sparse retrieval？
3. Semantic search 和 RAG 的最小区别是什么？

## 相关链接

- [[Embedding]]
- [[Dense Retrieval]]
- [[Sparse Retrieval]]
- [[Hybrid Search]]
- [[Vector Database]]
- [[Retriever]]
- [[RAG]]
