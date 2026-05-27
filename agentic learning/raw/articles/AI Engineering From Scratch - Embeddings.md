---
type: source
source_type: article
title: "AI Engineering From Scratch - Embeddings & Vector Representations"
url: https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/04-embeddings
author: Rohit G.
site: aiengineeringfromscratch.com
topic:
  - llm
  - rag
  - embedding
  - retrieval
created: 2026-05-24
updated: 2026-05-25
last_checked: 2026-05-24
freshness: watch
status: seed
source:
related:
  - "[[Embedding]]"
  - "[[Bi-Encoder]]"
  - "[[Semantic Search]]"
  - "[[Vector Similarity Metrics]]"
  - "[[Approximate Nearest Neighbor Search]]"
  - "[[HNSW]]"
  - "[[Matryoshka Embeddings]]"
  - "[[Embedding Quantization]]"
  - "[[MTEB]]"
---

# AI Engineering From Scratch - Embeddings

## 为什么收

这篇 lesson 补的是 embedding 进入 production semantic search / RAG 检索链路后的工程边界：为什么要从关键词走向语义表示、向量相似度怎么比较、向量库为什么需要 ANN / HNSW、chunking 和 bi-encoder / cross-encoder 在链路里各自负责什么，以及维度截断、量化和 benchmark 为什么是成本 / 质量判断的一部分。

已有 [[Embedding]]、[[Bi-Encoder]]、[[Dense Retrieval]]、[[Vector Database]]、[[Chunking]]、[[Reranking]] 和 [[Cross-Encoder]] 分别覆盖了局部组件；本 note 用来承接“embedding 不是一个孤立模型调用，而是一条可评估、可压缩、可索引的检索系统链路”。

## 一句话

Embedding 把离散文本放进连续向量空间；生产系统真正要掌握的是向量表示、相似度度量、近似最近邻索引、chunk 粒度、二阶段排序和模型评估如何共同决定 semantic search / RAG 的召回质量。

## 关键事实

- 课程把 embedding 的核心问题定义为 vocabulary mismatch：用户 query 和文档表达语义相近但词面不同，关键词检索可能漏掉。
- Embedding 是 dense vector，每个维度通常都有非零信息；这和 [[TF-IDF]] / bag-of-words 这类 sparse representation 不同。
- 现代 text embedding 常见维度从几百到几千不等；维度数量是向量长度，不是 token 数，也不是可人工命名的语义标签数。
- Word2Vec 的历史价值在于证明“语义关系可以在向量几何中表现出来”，但单词级、静态一词一向量的方式不足以处理句子和上下文。
- 句子 / 文档级 embedding 从 averaging、CLS token、contrastive learning 到 instruction-tuned embeddings 逐步演化；生产 RAG 通常关心句子、段落或 chunk embedding，而不是单词 embedding。
- 常用相似度度量包括 cosine similarity、dot product / inner product 和 Euclidean / L2 distance；归一化后 dot product 与 cosine 的排序边界需要和 [[L2 Normalization]] 一起理解。
- 向量库不能对每个 query 暴力比较所有向量；生产系统通常用 ANN 算法，用少量召回损失换取毫秒级检索。
- HNSW 是常见 ANN 图索引思路：多层图、上层稀疏长跳、下层稠密近邻，查询从上向下逐步逼近近邻。
- Matryoshka embeddings 让模型在训练时把重要信息放在前 N 维，使截短维度后仍能保留可用检索质量。
- Binary quantization 等 embedding quantization 用更少 bit 存储向量，常作为大规模第一阶段检索，再用全精度向量或 reranker 重排。
- MTEB 是 embedding model 的通用 benchmark 入口，但课程也提醒必须用自己的 query / corpus / task 做业务评测，不能只看榜单。

## 概念拆分

- [[Embedding]]：文本 / 对象到 dense vector representation 的表示层。
- [[Bi-Encoder]]：query 和 chunk 分开编码成向量、再用相似度比较的检索模型结构。
- [[Semantic Search]]：用语义相似而不是只用词面匹配来检索资料的任务模式。
- [[Vector Similarity Metrics]]：cosine、dot product、Euclidean / L2 distance 等向量比较方式。
- [[Approximate Nearest Neighbor Search]]：不用暴力全量比较，而用近似索引加速向量近邻检索。
- [[HNSW]]：ANN 的常见图索引算法。
- [[Matryoshka Embeddings]]：可截短维度的 embedding 训练 / 使用模式。
- [[Embedding Quantization]]：用低精度或二值化压缩 embedding 存储与检索成本。
- [[MTEB]]：embedding model 通用 benchmark，作为选型参考而不是业务评测替代品。

## 边界提醒

这篇 source 支持的稳定知识是机制链路，不是某个模型在 2026 年的永久排名。具体模型名称、MTEB 分数、价格、上下文长度和 API 参数会变化，适合保留在 source note 和选型复查中，不适合写死进稳定概念定义。

Embedding 也不等于 RAG。Embedding / vector search 是 RAG 的常见检索路线；可靠 RAG 还需要 ingestion、chunking、metadata、权限、hybrid search、reranking、citation faithfulness 和 evaluation。

## 不直接写成稳定事实

- 具体 embedding model 的分数排名、价格和上下文长度。
- 某个向量数据库的最大规模或性能数字。
- “维度越高一定越好”的单向判断。
- “MTEB 第一就适合业务”的选型结论。
- “HNSW 一定优于其他索引”的绝对结论。

## 外部链接

- Lesson: <https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/04-embeddings>
- Source markdown: <https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/phases/11-llm-engineering/04-embeddings/docs/en.md>
