---
type: concept
topic:
  - rag
  - retrieval
  - embedding
  - math
status: growing
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: stable
conflicts: []
aliases:
  - vector similarity metrics
  - vector distance metrics
  - 向量相似度度量
  - 向量距离度量
  - cosine similarity
  - 余弦相似度
  - dot product
  - inner product
  - 点积
  - 内积
  - Euclidean distance
  - L2 distance
  - 欧氏距离
  - L2 距离
source:
  - "[[AI Engineering From Scratch - Embeddings]]"
  - "[[L2 Normalization]]"
evidence:
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[AI Engineering From Scratch - Embeddings#概念拆分]]"
  - "[[L2 Normalization#概念详解]]"
related:
  - "[[Embedding]]"
  - "[[Dense Retrieval]]"
  - "[[L2 Normalization]]"
  - "[[Vector Database]]"
  - "[[Top-K]]"
  - "[[Reranking]]"
---

# Vector Similarity Metrics

## 一句话

Vector Similarity Metrics 是比较两个 embedding 向量“有多接近”的数学度量，常见包括 cosine similarity、dot product / inner product 和 Euclidean / L2 distance。

## 概念详解

Embedding 只把文本变成向量，还没有回答“两个向量怎么算相似”。[[Dense Retrieval]]、[[Vector Database]] 和 semantic search 必须选一种度量来排序候选：query vector 和 chunk vector 越相似，候选越可能被召回到 top-k。

Cosine similarity 看两个向量夹角的余弦，关注方向是否相近。它常用于文本检索，因为两段文本长度不同、语气不同或信息量不同，向量长度不一定应该影响语义相似判断。它的直觉是：两个向量从原点看过去是否指向相似方向。

Dot product / inner product 是逐维相乘再求和。它计算快，也常被向量库支持；但如果向量没有归一化，它会同时受到方向和长度影响。若 query 和 document embedding 都经过 [[L2 Normalization]] 变成单位向量，dot product 的排序就可以按 cosine similarity 理解。

Euclidean / L2 distance 是向量空间里的直线距离，距离越小越近。它在某些聚类或空间近邻问题里自然，但在文本 embedding 检索里要小心：如果向量长度差异没有被控制，L2 distance 可能把尺度差异当成语义差异。

这些度量不是答案正确性的证明。它们只负责“候选向量按什么几何规则靠前”。候选是否真的回答问题，还要看 chunk 质量、metadata、权限、reranking、引用和 RAG evaluation。

工程上，metric choice 也是索引契约的一部分：文档向量建索引时选择的 metric、query 侧计算时的 metric、以及是否做 normalization，需要一起记录。否则同一批 embedding 在不同配置下会产生不同排序，排查时很容易误以为是模型质量或 prompt 问题。

## 它解决什么问题

它解决的是“embedding 生成后，系统如何把 query 和候选 chunk 排序”的问题。没有明确的相似度度量，向量检索无法定义 top-k。

## 它不是什么

它不是 [[Embedding]] 模型本身。Embedding 生成向量；similarity metric 比较向量。

它也不是 [[Reranking]]。Reranking 可以用 cross-encoder、LLM judge 或业务规则做更细判断；vector similarity 通常是更早、更便宜的候选召回或初排信号。

它更不是 [[RAG Evaluation]] 指标。相似度高不等于答案忠实，也不等于引用支持结论。

## 最小例子

```text
query_vec = embed("如何重置密码")
chunk_vec = embed("忘记密码时点击账户设置中的重置链接")

score = cosine_similarity(query_vec, chunk_vec)
```

如果 score 排名前几，这个 chunk 会进入候选集；但它是否进入最终上下文，还可能经过 filter、dedupe 和 rerank。

## 常见误解 / 风险

- 把 cosine、dot product 和 L2 distance 当成完全可互换：只有在向量归一化等条件满足时，部分排序才会等价。
- 忽略向量库 metric 配置：索引时用一种 metric，查询或评估时按另一种理解，会让排序难解释。
- 把相似度分数当置信度：相似度是几何分数，不是事实正确概率。
- 直接比较不同 embedding 模型的相似度分数：不同模型的向量空间和分数分布通常不可直接比较。

## 边界细节

和 [[L2 Normalization]] 的边界：L2 normalization 是把向量缩放到单位长度；Vector Similarity Metrics 是比较向量的规则。归一化会改变 dot product / cosine / L2 distance 的等价关系。

和 [[Top-K]] 的边界：similarity metric 产生排序分数；Top-K 是只保留前 K 个候选的预算控制。

和 [[Hybrid Search]] 的边界：hybrid search 要合并向量相似度、BM25 等不同量纲信号；这时通常不能直接把原始分数相加，可能需要 RRF、归一化或 reranking。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：cosine、dot product、Euclidean / L2 distance 的数学定义和归一化关系稳定。
- 易变部分：不同 embedding provider 是否默认归一化、向量库 metric 名称、ANN 索引对 metric 的支持和性能优化。
- 复查点：换 embedding 模型或向量库时，要确认文档侧和 query 侧的 metric / normalization 一致。

## 现代系统怎么吸收 Vector Similarity Metrics 的价值

现代 RAG 系统通常把相似度度量封装在 vector index 或 retriever 配置里，但排错时必须显式知道它。若正确 chunk 分数低，可能是 embedding 模型不适配、chunk 过长、query 表述偏移、metric 配置不一致或 normalization 不一致，而不是 LLM 生成阶段的问题。

## 证据锚点

- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchors: [[AI Engineering From Scratch - Embeddings#关键事实]], [[AI Engineering From Scratch - Embeddings#概念拆分]]
- Supporting card: [[L2 Normalization#概念详解]]
- Evidence type: course source note + existing mathematical concept card + engineering synthesis.
- Confidence: high for mathematical definitions; medium for provider-specific defaults.
- Boundary: 本卡记录向量比较规则，不证明检索结果事实正确，也不替代 reranker 或 RAG evaluation。

## 复习触发

1. 为什么 normalized dot product 可以按 cosine similarity 理解？
2. 如果两个 embedding 模型不同，为什么不能直接比较它们的相似度分数？
3. 在 hybrid search 中，为什么 BM25 分数和 cosine 分数不能直接相加？

## 相关链接

- [[Embedding]]
- [[Dense Retrieval]]
- [[L2 Normalization]]
- [[Vector Database]]
- [[Top-K]]
- [[Reranking]]
