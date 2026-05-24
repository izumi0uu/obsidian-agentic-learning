---
type: concept
topic:
  - rag
  - retrieval
  - vector-search
  - infrastructure
status: growing
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: stable
conflicts: []
aliases:
  - vector search algorithms
  - vector search method
  - vector index algorithm
  - 向量搜索算法
  - 向量索引算法
source:
  - "[[AI Engineering From Scratch - Embeddings]]"
  - "[[Approximate Nearest Neighbor Search]]"
  - "[[HNSW]]"
evidence:
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[AI Engineering From Scratch - Embeddings#概念拆分]]"
  - "[[Approximate Nearest Neighbor Search#概念详解]]"
  - "[[HNSW#概念详解]]"
related:
  - "[[Embedding]]"
  - "[[Vector Similarity Metrics]]"
  - "[[Approximate Nearest Neighbor Search]]"
  - "[[HNSW]]"
  - "[[Vector Database]]"
---

# Vector Search Algorithm

## 一句话

Vector Search Algorithm 是在向量空间中查找相近向量的方法族，负责把“按相似度找候选”这件事变成可计算、可索引、可调参的检索过程。

## 概念详解

Embedding 把文本或其他对象变成向量以后，系统还要解决两个问题：什么叫“近”，以及怎样在大量向量里快速找到近邻。前者由 [[Vector Similarity Metrics]] 定义，后者就是 Vector Search Algorithm 的边界。

在小数据量里，最简单的向量搜索算法是 exact / brute-force search：把 query vector 和每个 document vector 都算一遍相似度，再按分数排序。这种方法直观、准确，也适合作为评估基线；但在百万、千万级向量上，逐条扫描会把延迟、CPU/GPU、内存带宽和成本推高。

因此工程系统会引入索引和近似搜索。[[Approximate Nearest Neighbor Search]] 是向量搜索算法的重要方法族：它不总是返回数学上绝对精确的最近邻，而是通过图结构、聚类、量化或其他索引策略快速缩小候选范围。[[HNSW]] 则是 ANN 里非常常见的图索引代表。

学习这个父概念时，最重要的是把搜索算法看成“候选生成的计算路径”，而不是最终答案质量本身。算法通常暴露一些可调参数，例如搜索宽度、图连接密度、聚类中心数量或候选池大小；这些参数改变的是 recall、latency、内存、构建时间和更新成本之间的曲线。它们必须和 embedding 模型、向量维度、normalization、metric、metadata filter 和 reranker 一起评估。

这个父概念的作用是把“向量库产品”和“具体算法”分开。[[Vector Database]] 是存储、查询、过滤、更新、服务 API 和运维产品层；Vector Search Algorithm 是里面负责近邻搜索的算法层。一个向量库可以支持多种算法，一个算法也可以被多个系统实现。

## 它解决什么问题

它解决的是“有了向量以后，怎样按相似度找到候选”的算法问题，尤其是在数据量变大时怎样避免每个 query 都全量扫描。

## 它不是什么

它不是 [[Embedding]]。Embedding 生成向量；Vector Search Algorithm 搜索向量。

它不是 [[Vector Similarity Metrics]]。metric 定义相似度；search algorithm 决定如何用这个定义找到候选。

它也不是 [[Vector Database]]。向量数据库可能实现这些算法，但还承担存储、过滤、更新、权限和运维责任。

## 最小例子

```text
query -> embedding -> vector search algorithm -> candidate vectors

exact search: compare with every vector
ANN / HNSW: use index structure to search a smaller neighborhood
```

## 常见误解 / 风险

- 把向量搜索算法等同于向量数据库产品：产品层和算法层不是一回事。
- 把速度优化当成质量提升：算法更快不代表候选更正确。
- 忽略 metric / normalization：索引算法必须和相似度定义一致。
- 只看平均延迟，不看 recall、filter、更新、删除和重建成本。

## 边界细节

和 [[Approximate Nearest Neighbor Search]] 的边界：Vector Search Algorithm 是更宽的方法族；ANN 是其中以近似换速度的子族。

和 [[HNSW]] 的边界：HNSW 是 ANN 的具体图索引代表，不是所有向量搜索算法。

和 [[Vector Similarity Metrics]] 的边界：metric 回答“近是什么意思”；algorithm 回答“怎样找到近的向量”。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：向量检索需要搜索算法和索引结构，exact search 与 ANN 的质量/速度取舍稳定。
- 易变部分：具体算法实现、参数默认值、硬件优化和向量库支持。
- 复查点：选型时看业务语料、向量维度、filter、QPS、更新频率和 recall/latency 曲线。

## 现代系统怎么吸收 Vector Search Algorithm 的价值

现代 RAG 系统通常不会在应用代码里手写算法，而是通过向量库、搜索引擎或本地索引库配置算法类型、metric 和参数。应用层需要保留检索 trace、索引版本和失败样本，才能区分是 embedding 质量差、metric 配置错，还是搜索算法漏召回。

## 证据锚点

- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchors: [[AI Engineering From Scratch - Embeddings#关键事实]], [[AI Engineering From Scratch - Embeddings#概念拆分]]
- Supporting cards: [[Approximate Nearest Neighbor Search#概念详解]], [[HNSW#概念详解]]
- Evidence type: course source note + existing concept-card synthesis.
- Confidence: medium-high.
- Boundary: 本卡是算法父类，不替代向量数据库、embedding 模型或 RAG 质量评估。

## 复习触发

1. Vector Search Algorithm 和 Vector Similarity Metrics 分别回答什么问题？
2. 为什么 exact search 适合作为 ANN 的评估基线？
3. 为什么向量数据库支持 HNSW，不等于 HNSW 是向量数据库本身？

## 相关链接

- [[Embedding]]
- [[Vector Similarity Metrics]]
- [[Approximate Nearest Neighbor Search]]
- [[HNSW]]
- [[Vector Database]]
