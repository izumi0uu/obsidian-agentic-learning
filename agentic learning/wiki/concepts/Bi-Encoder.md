---
type: concept
topic:
  - rag
  - retrieval
  - embedding
  - model-architecture
status: growing
created: 2026-05-25
updated: 2026-05-25
last_checked: 2026-05-25
freshness: stable
conflicts: []
aliases:
  - Bi-encoder
  - bi-encoder
  - Dual Encoder
  - dual encoder
  - dual-encoder
  - 双编码器
  - 双塔结构
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
  - "[[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？]]"
  - "[[AI Engineering From Scratch - Embeddings]]"
  - "[[Dense Retrieval]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#选读块 1：Section 2.2 / Retriever: DPR]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第四层：重排序]]"
  - "[[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？#第三代：句子级对比学习 Embedding（SBERT / SimCSE / BGE）]]"
  - "[[AI Engineering From Scratch - Embeddings#为什么收]]"
  - "[[Dense Retrieval#概念详解]]"
relations:
  - type: used_by
    target: "[[Dense Retrieval]]"
    note: Dense retrieval 常用 bi-encoder / dual-encoder 把 query 和 chunk 分开编码成向量，再用相似度做召回。
  - type: contrasts_with
    target: "[[Cross-Encoder]]"
    note: Bi-Encoder 牺牲 query-chunk token 级交互换速度和可预计算；Cross-Encoder 把二者联合输入，适合小候选集精排。
  - type: enables
    target: "[[Vector Database]]"
    note: 文档侧 embedding 可离线预计算并写入向量库，是大规模向量检索能在线工作的关键前提。
related:
  - "[[Embedding]]"
  - "[[Dense Retrieval]]"
  - "[[Semantic Search]]"
  - "[[Vector Similarity Metrics]]"
  - "[[Vector Database]]"
  - "[[Approximate Nearest Neighbor Search]]"
  - "[[Reranking]]"
  - "[[Cross-Encoder]]"
  - "[[Retriever]]"
---

# Bi-Encoder

## 一句话

Bi-Encoder 是一种把 query 和 document / chunk 分别编码成向量、再用相似度比较的双编码器结构，常用于 RAG 的快速召回阶段。

## 概念详解

RAG 检索面对的第一个工程压力是规模：知识库里可能有成千上万、百万甚至更多 chunk。如果每次用户提问都把 query 和每个 chunk 拼在一起跑模型，在线延迟会不可接受。Bi-Encoder 的做法是把两边拆开：query 经过 query encoder 变成 query vector，chunk 经过 document encoder 变成 chunk vector，再用 cosine similarity、dot product 或其他 [[Vector Similarity Metrics]] 比较。

这个结构的关键价值是可预计算。文档侧 chunk embedding 可以在入库时离线生成，写入 [[Vector Database]] 或向量索引；在线查询时只需要计算一次 query embedding，再用 [[Approximate Nearest Neighbor Search]] / [[HNSW]] 等索引快速找 top-k 候选。因此它是 [[Dense Retrieval]] 能用于生产 RAG 的常见模型结构。

它的代价也很清楚：query 和 chunk 在编码阶段互相看不见。模型只能在两个整体向量之间算相似度，不能像 [[Cross-Encoder]] 那样让 query token 和 chunk token 在同一次前向传播里细粒度交互。所以 Bi-Encoder 适合大范围召回，不适合承担最终相关性判断。常见系统会先用 Bi-Encoder / BM25 / hybrid route 找 top-20 或 top-50，再用 Cross-Encoder 或其他 [[Reranking]] 方法精排。

Bi-Encoder 不一定意味着两个完全不同的模型。有些实现让 query encoder 和 document encoder 共享权重，有些实现分开训练两侧 encoder。稳定边界不是“有两份模型”，而是“query 和 candidate 独立编码，之后用向量相似度比较”。

证据边界：RAG 经典论文 source note 支持 DPR / bi-encoder retriever 和 MIPS 的原始架构线索；xiaolinnote 的 RAG 检索优化和 Embedding 算法 source note 支持 Bi-Encoder 与 Cross-Encoder 的速度 / 精度取舍；AI Engineering Embeddings source note 支持把 bi-encoder / cross-encoder 放在 production semantic search / RAG 检索链路中理解；本卡把这些证据沉淀为模型结构边界。

## 它解决什么问题

Bi-Encoder 解决的是大规模语义召回的在线成本问题。

它让系统可以提前计算文档向量，查询时只算 query 向量并做向量搜索，从而把“每个 query 都和全库逐对深度比较”的问题，改造成“向量索引中找近邻”的问题。

## 它不是什么

Bi-Encoder 不是 [[Dense Retrieval]] 本身。Dense Retrieval 是检索路线，Bi-Encoder 是这条路线常见的模型结构。

Bi-Encoder 也不是 [[Cross-Encoder]]。前者分开编码、速度快、可预计算；后者联合编码、判断细、适合小候选集精排。

它也不是 [[Vector Database]]。向量库保存和搜索 embedding；Bi-Encoder 负责生成可比较的 query / chunk 向量。

## 最小例子

```text
离线：
chunk -> document encoder -> chunk vector -> vector database

在线：
query -> query encoder -> query vector
query vector vs chunk vectors -> top-k chunks
```

代码直觉：

```python
query_vec = encoder("苹果手机怎么截图")
doc_vec = encoder("iPhone 截屏方法")
score = cosine_similarity(query_vec, doc_vec)
```

## 常见误解 / 风险

- 把 Bi-Encoder 当成“更弱的 Cross-Encoder”：它不是低配精排器，而是为大规模召回设计的结构。
- 以为它一定有两个不同模型：共享权重和非共享权重都可能成立，关键是两边独立编码。
- 忽略无交互代价：query 和 chunk 没有 token 级联合注意力，所以细粒度否定、实体关系、条件匹配可能排错。
- 只靠 Bi-Encoder 做最终上下文选择：生产 RAG 通常还需要 hybrid search、去重、reranking 和 citation check。
- 把“双塔结构”泛化到所有两个模块系统：本卡只记录检索语境中 query / candidate 独立编码再比较的结构。

## 边界细节

和 [[Embedding]] 的边界：Embedding 是向量表示结果或模型能力；Bi-Encoder 是为了检索把 query 和 candidate 分开编码的结构。

和 [[Dense Retrieval]] 的边界：Dense Retrieval 定义“用 dense embedding 召回”；Bi-Encoder 是它常用的实现结构之一。

和 [[Cross-Encoder]] 的边界：Bi-Encoder 优先速度、可索引和可预计算；Cross-Encoder 优先精细相关性判断。

和 [[Reranking]] 的边界：Bi-Encoder 常在 rerank 之前负责初召回；reranker 只能重排它和其他路线已经召回的候选。

和 [[Vector Database]] 的边界：Bi-Encoder 生成可搜索向量；向量库负责保存、索引、过滤和 top-k 查询。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：query / document 独立编码、向量相似度比较、文档向量可离线预计算，是现代 RAG 召回的基础结构。
- 易变部分：具体 embedding 模型、query/document encoder 是否共享权重、训练数据、损失函数、维度、归一化和供应商 API。
- 复查点：换 embedding model 或 reranker 时，要用业务 query / corpus 评估召回和精排，而不是只看模型宣传。

## 现代系统怎么吸收 Bi-Encoder 的价值

现代 RAG 通常把 Bi-Encoder 放在第一阶段召回：它快速给出候选池，但不单独决定最终上下文。一个可调试系统应该记录 query embedding 模型、document embedding 模型、相似度 metric、ANN 参数、召回 top-k、是否接 BM25 / hybrid route，以及 reranker 前后的排序变化。

## 证据锚点

- Source: [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]
- Anchor: [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第四层：重排序]]
- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#选读块 1：Section 2.2 / Retriever: DPR]]
- Source: [[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？]]
- Anchor: [[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？#第三代：句子级对比学习 Embedding（SBERT / SimCSE / BGE）]]
- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchor: [[AI Engineering From Scratch - Embeddings#为什么收]]
- Supporting card: [[Dense Retrieval#概念详解]]
- Evidence type: RAG interview source notes + embedding engineering source note + existing concept-card synthesis.
- Confidence: medium-high.
- Boundary: 本卡记录检索模型结构，不把 Bi-Encoder 写成整个 dense retrieval、vector database、reranking 或答案生成流程。

## 复习触发

1. 为什么 Bi-Encoder 能让文档向量离线预计算？
2. 为什么 Bi-Encoder 适合召回，而 Cross-Encoder 适合 rerank？
3. 如果初召回漏掉正确 chunk，后面的 Cross-Encoder 为什么通常救不了？

## 相关链接

- [[Embedding]]
- [[Dense Retrieval]]
- [[Semantic Search]]
- [[Vector Similarity Metrics]]
- [[Vector Database]]
- [[Approximate Nearest Neighbor Search]]
- [[Reranking]]
- [[Cross-Encoder]]
- [[Retriever]]
