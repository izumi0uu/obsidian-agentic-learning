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

up:
  - "[[Vector Search Algorithm]]"

last_checked: 2026-05-24
freshness: stable
conflicts: []
aliases:
  - ANN
  - ANN Search
  - Approximate Nearest Neighbor
  - Approximate Nearest Neighbor Search
  - approximate nearest neighbor search
  - 近似最近邻搜索
  - 近似最近邻
  - ANN 搜索
source:
  - "[[AI Engineering From Scratch - Embeddings]]"
  - "[[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？]]"
  - "[[raw/repos/xiaolinnote/questions/041 ai rag 8. 什么是向量数据库？有没有做过向量数据库的对比选型？]]"
related:
  - "[[Vector Search Algorithm]]"
  - "[[Vector Database]]"
  - "[[Dense Retrieval]]"
  - "[[HNSW]]"
  - "[[Top-K]]"
  - "[[Vector Similarity Metrics]]"
  - "[[Embedding]]"
evidence:
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[AI Engineering From Scratch - Embeddings#概念拆分]]"
  - "[[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？#第三步：向量检索（ANN 搜索）+ 多路召回]]"
  - "[[raw/repos/xiaolinnote/questions/041 ai rag 8. 什么是向量数据库？有没有做过向量数据库的对比选型？#核心索引算法：HNSW 和 IVF]]"
---

# Approximate Nearest Neighbor Search

## 一句话

Approximate Nearest Neighbor Search（ANN）是在大量向量中快速找“足够接近”的近邻，用少量召回精度损失换取远低于暴力全量比较的查询延迟。

## 概念详解

在小数据集里，系统可以把 query embedding 和每个 document embedding 都算一遍相似度，再取 [[Top-K]]。但当向量数量到百万、千万甚至更高时，暴力搜索会变成昂贵的 O(n) 全量扫描：每个 query 都要和所有向量逐维比较。

ANN 的核心取舍是：不保证每次都返回数学意义上绝对精确的最近邻，而是通过索引结构快速缩小候选范围，返回高概率接近真实 top-k 的结果。生产 RAG 往往接受这种取舍，因为从秒级或更慢降到毫秒级，会直接影响在线体验、并发和成本。

ANN 不是一种单一算法，而是一类向量搜索加速方法。常见家族包括图结构、量化、聚类 / inverted file 等。[[HNSW]] 是当前工程中非常常见的图结构 ANN 索引：把向量组织成多层小世界图，从稀疏高层开始跳转，再在低层细化近邻。

在 RAG pipeline 中，ANN 位于 [[Vector Database]] / vector index 内部。上游 [[Embedding]] 决定向量空间质量，[[Vector Similarity Metrics]] 决定比较规则，ANN 决定如何在这个空间里快速找候选。ANN 找回的是候选，不是最终证据；后面仍可能经过 metadata filter、hybrid merge、[[Reranking]] 和 citation check。

评估 ANN 时通常要把“精确暴力搜索”当作小规模基线：先看近似索引相对 exact search 漏掉了多少 relevant neighbors，再看换来的 latency、内存和更新成本。这样能把“embedding 本身找不到答案”和“ANN 近似导致漏召回”分开定位。

## 它解决什么问题

它解决的是大规模向量检索的延迟和吞吐问题：如果每个 query 都扫全库，向量搜索很难支撑生产 RAG 或 semantic search。

## 它不是什么

ANN 不是 [[Embedding]] 模型，也不是 [[RAG]] 本身。

它也不是“准确率提升算法”。ANN 主要用近似换速度；如果 embedding 模型或 chunking 质量差，ANN 只会更快地找到质量受限的候选。

它更不是 [[HNSW]] 的同义词。HNSW 是 ANN 的常见算法之一。

## 最小例子

```text
离线：chunk embeddings -> build ANN index
在线：query embedding -> ANN search top-k candidates -> rerank/context
```

如果资料库只有 100 条向量，可以直接暴力比较；如果有 1000 万条向量，就通常要考虑 ANN 索引。

## 常见误解 / 风险

- 以为 ANN 返回的一定是精确最近邻：ANN 本来就是近似搜索，需要用 recall / latency 取舍来评估。
- 忽略 metadata filter：先 ANN 后过滤可能导致 top-k 名额被不满足权限或条件的候选占掉。
- 只看查询延迟，不看构建索引、增量更新、删除、内存和重建成本。
- 把 ANN 问题当成 LLM 问题：检索候选都没找对时，生成模型很难补救。

## 边界细节

和 [[HNSW]] 的边界：ANN 是问题和方法家族；HNSW 是一种具体图索引实现思路。

和 [[Vector Database]] 的边界：Vector Database 是产品 / 基础设施层；ANN 是其中常见的索引和查询算法边界。

和 [[Top-K]] 的边界：ANN 负责快速找候选；Top-K 是返回数量预算。ANN 的 top-k 可能是近似 top-k，不一定等于暴力精确搜索的 top-k。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：大规模向量检索需要用索引和近似搜索避免全量扫描。
- 易变部分：具体 ANN 算法、参数、向量库实现、filter 支持、硬件优化和 benchmark。
- 复查点：项目选型时要用自己的语料、query、filter 和延迟目标评估 ANN recall / latency，而不是只看产品宣传。

## 现代系统怎么吸收 ANN 的价值

现代向量数据库通常把 ANN 作为默认搜索能力之一，并把索引参数、metric、filter、payload、压缩和更新策略做成配置。对应用层来说，关键不是记住算法名字，而是能问：召回损失多少、延迟降多少、过滤如何生效、索引如何更新、失败样本怎么回归。

## 证据锚点

- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchors: [[AI Engineering From Scratch - Embeddings#关键事实]], [[AI Engineering From Scratch - Embeddings#概念拆分]]
- Interview source anchors: [[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？#第三步：向量检索（ANN 搜索）+ 多路召回]], [[raw/repos/xiaolinnote/questions/041 ai rag 8. 什么是向量数据库？有没有做过向量数据库的对比选型？#核心索引算法：HNSW 和 IVF]]
- Evidence type: course source note + RAG interview source notes + engineering synthesis.
- Confidence: medium-high.
- Boundary: 本卡记录向量搜索加速方法族，不把某个 ANN 算法或向量数据库产品写成永久最优。

## 复习触发

1. 为什么大规模向量搜索不能总是暴力扫全库？
2. ANN 的“approximate”牺牲了什么，换来了什么？
3. 为什么 ANN 找得快，不等于 RAG 答得准？

## 相关链接

- [[Vector Database]]
- [[Vector Search Algorithm]]
- [[Dense Retrieval]]
- [[HNSW]]
- [[Top-K]]
- [[Vector Similarity Metrics]]
- [[Embedding]]
