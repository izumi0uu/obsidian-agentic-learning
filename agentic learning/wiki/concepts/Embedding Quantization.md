---
type: concept
topic:
  - rag
  - embedding
  - retrieval
  - optimization
status: growing
created: 2026-05-24
updated: 2026-05-24

up:
  - "[[Embedding Optimization]]"

last_checked: 2026-05-24
freshness: watch
conflicts: []
aliases:
  - embedding quantization
  - vector quantization for embeddings
  - Binary Quantization
  - binary quantization
  - embedding binary quantization
  - 向量量化
  - embedding 量化
  - 二值量化
source:
  - "[[AI Engineering From Scratch - Embeddings]]"
evidence:
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[AI Engineering From Scratch - Embeddings#概念拆分]]"
related:
  - "[[Embedding Optimization]]"
  - "[[Embedding]]"
  - "[[Vector Database]]"
  - "[[Approximate Nearest Neighbor Search]]"
  - "[[HNSW]]"
  - "[[Matryoshka Embeddings]]"
  - "[[Vector Similarity Metrics]]"
---

# Embedding Quantization

## 一句话

Embedding Quantization 是把 embedding 向量用更低精度或更少 bit 表示，以降低存储、内存带宽和检索成本；binary quantization 是其中极端的一种，把每个维度压成 0/1。

## 概念详解

大规模 semantic search 的成本不只来自模型调用，也来自向量本身。一个 1536 维 float32 embedding 需要保存 1536 个 4 字节浮点数；当文档数量达到百万、千万，向量存储、索引内存和相似度计算都会变成工程问题。

Embedding Quantization 的思路是降低每个维度的表示精度。比如从 float32 降到 int8、float16，或者在 binary quantization 中只保留符号 / 阈值信息，把正值记为 1、负值记为 0。这样可以显著减少存储和内存访问，并让第一阶段候选搜索更快。

代价是召回质量可能下降。量化后的向量不再保留完整浮点信息，相似度排序会发生变化。因此常见生产模式是二阶段：先用量化向量在大规模库里快速找候选，再用全精度向量、[[Reranking]] 或业务规则对较小候选集重新排序。

需要特别区分：embedding quantization 不是 LLM 权重量化。LLM 权重量化压缩的是生成模型参数；embedding quantization 压缩的是已经生成的向量索引。它也不是 [[Matryoshka Embeddings]]，后者减少维度数，量化减少每个维度的存储精度。

可靠做法是把量化索引当成可回滚的检索版本，而不是覆盖掉唯一表示。保留全精度向量或可重建来源，可以支持二阶段 rescore、抽样审计和失败样本复盘；否则一旦压缩导致长尾 query 漏召回，很难判断是模型、chunk、量化还是 ANN 参数的问题。

## 它解决什么问题

它解决的是大规模 embedding 存储、内存和检索速度问题，让向量检索在更低资源预算下可运行。

## 它不是什么

Embedding Quantization 不是提升语义质量的方法。它通常是成本优化，可能带来召回损失。

它不是 LLM model quantization，不压缩生成模型权重。

它也不是 [[L2 Normalization]]。归一化处理向量长度；量化处理向量数值精度 / bit 表示。

## 最小例子

```text
float32 vector:
  [0.12, -0.04, 0.88, ...]

binary quantized vector:
  [1, 0, 1, ...]

first pass: binary search top-1000
second pass: full-precision rescore / rerank top-1000
```

## 常见误解 / 风险

- 只看压缩倍率，不看 recall 损失。
- 把量化后的候选直接作为最终上下文，不做重排或抽样评估。
- 把 embedding quantization 和 LLM 权重量化混在一起。
- 在变更量化策略后不重建索引或不记录索引版本。

## 边界细节

和 [[Matryoshka Embeddings]] 的边界：Matryoshka 截短维度；quantization 降低每维精度。两者都服务成本控制，但机制不同。

和 [[Approximate Nearest Neighbor Search]] 的边界：ANN 用索引结构近似搜索；quantization 用更低精度表示向量。某些向量索引会把二者组合。

和 [[Vector Similarity Metrics]] 的边界：量化会改变相似度近似方式，可能不再等同于全精度 cosine / dot product 排序。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：大规模向量检索常需要压缩向量存储和计算。
- 易变部分：具体量化方案、向量库支持、硬件优化、质量损失和参数。
- 复查点：上线前用业务 retrieval eval 比较 full precision、截短维度、量化和二阶段 rescore 的差异。

## 现代系统怎么吸收 Embedding Quantization 的价值

生产系统通常把 embedding quantization 放在“第一阶段大规模召回”的成本优化里，而不是最终质量层。它应该和索引版本、检索 trace、全精度重排、RAG evaluation 一起使用，避免压缩后的召回损失静悄悄进入线上答案。

## 证据锚点

- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchors: [[AI Engineering From Scratch - Embeddings#关键事实]], [[AI Engineering From Scratch - Embeddings#概念拆分]]
- Evidence type: course source note + engineering synthesis.
- Confidence: medium.
- Boundary: 本卡记录 embedding 向量压缩，不记录 LLM 权重量化方法，也不把具体压缩倍率 / 损失写成永久事实。

## 复习触发

1. Embedding quantization 和 LLM 权重量化有什么不同？
2. 为什么 binary quantization 常需要二阶段 full-precision rescore？
3. 它和 Matryoshka 降维分别减少了什么成本？

## 相关链接

- [[Embedding]]
- [[Embedding Optimization]]
- [[Vector Database]]
- [[Approximate Nearest Neighbor Search]]
- [[HNSW]]
- [[Matryoshka Embeddings]]
- [[Vector Similarity Metrics]]
