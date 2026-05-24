---
type: concept
topic:
  - rag
  - retrieval
  - embedding
status: growing
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: stable
conflicts: []
aliases:
  - L2 normalization
  - L2 归一化
  - L2范数归一化
  - L2 范数归一化
  - 单位向量归一化
  - unit vector normalization
  - vector normalization
source:
  - "[[AI Engineering From Scratch - Embeddings]]"
  - "[[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？]]"
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]"
  - "[[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？]]"
  - "[[raw/repos/agent_java_offer/questions/066 01_AI 03_RAG 一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。]]"
evidence:
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？#第三步：向量检索（ANN 搜索）+ 多路召回]]"
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#向量检索：语义匹配，靠 Embedding]]"
  - "[[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？#第三代：句子级对比学习 Embedding（SBERT / SimCSE / BGE）]]"
  - "[[raw/repos/agent_java_offer/questions/066 01_AI 03_RAG 一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。#3. 子问题：一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。]]"
related:
  - "[[Embedding]]"
  - "[[Dense Retrieval]]"
  - "[[Vector Database]]"
  - "[[Vector Similarity Metrics]]"
  - "[[Hybrid Search]]"
  - "[[Reciprocal Rank Fusion]]"
---

# L2 Normalization

## 一句话

L2 Normalization 是把一个向量除以自己的 L2 范数，让它变成长度为 1 的单位向量；在 embedding 检索里，它常用来让相似度比较更关注向量方向，而不是向量长度。

## 概念详解

L2 范数是向量长度：

```text
||x||_2 = sqrt(x1^2 + x2^2 + ... + xn^2)
```

L2 normalization 的操作是：

```text
x_normalized = x / ||x||_2
```

如果 `x = [3, 4]`，那么 `||x||_2 = 5`，归一化后就是 `[0.6, 0.8]`。新向量的方向不变，但长度变成 1。

在 [[Embedding]] / [[Dense Retrieval]] 语境里，这个细节很重要。向量检索通常关心“query 和 chunk 的语义方向是否接近”。如果不归一化，dot product 会同时受方向和向量长度影响；如果 query 向量和文档向量都已经 L2 normalize，那么它们的 dot product 就等价于 cosine similarity。对单位向量来说，L2 distance 的排序也和 cosine similarity 有固定换算关系：

```text
u dot v = cos(theta)
||u - v||_2^2 = 2 - 2 cos(theta)
```

这解释了为什么有些向量库或检索实现会在 cosine、inner product / dot product、L2 distance 之间做工程选择：当向量已经单位化时，这些度量之间可能只是计算形式不同；当向量没有单位化时，它们表达的排序偏好就不一样。

学习时可以把它想成把所有 embedding 都放到同一个单位球面上。原始向量离原点有多远不再重要，重要的是两个点从原点看过去夹角有多小。这个处理不会改变向量维度，也不会改变 query 和 chunk 是否来自同一个 embedding 模型；它只是在同一向量空间内固定长度尺度。因此它必须在索引侧和查询侧保持一致，否则同一条检索链路里的相似度分数会混入不同尺度假设。相似度度量的完整边界见 [[Vector Similarity Metrics]]；本卡只解释单位化这个前处理。

## 它解决什么问题

它解决的是向量相似度计算里的尺度问题：让比较重点落在方向相似，而不是某个向量因为长度更大就在 dot product 里天然占优。

## 它不是什么

L2 Normalization 不是 [[Embedding]] 本身。Embedding 负责把文本变成向量；L2 normalization 只是在向量生成后做长度处理。

它也不是 L2 regularization。L2 regularization 是训练模型时惩罚权重过大；L2 normalization 是把某个向量缩放到单位长度。

它更不是 [[Hybrid Search]] 或 [[Reciprocal Rank Fusion]] 里的分数归一化。后者处理不同检索器输出分数的量纲；L2 normalization 处理单个向量的长度。

## 最小例子

```text
query_vec = [3, 4]
norm = sqrt(3^2 + 4^2) = 5

normalized_query_vec = [3/5, 4/5]
                     = [0.6, 0.8]

sqrt(0.6^2 + 0.8^2) = 1
```

归一化后，向量仍然指向原来的方向，只是被投影到单位圆 / 单位球面上。

## 常见误解 / 风险

- 以为所有 embedding API 都已经自动归一化：不同模型和库的默认行为不一定相同，索引和查询两侧要保持一致。
- 把 normalized dot product 和普通 dot product 混用：前者等价于 cosine，后者会受向量长度影响。
- 忽略零向量：零向量的 L2 范数是 0，不能直接做 L2 normalization。
- 以为归一化能修复语义质量：它只能处理尺度，不会让差的 embedding 模型突然理解领域术语。

## 边界细节

和 [[Embedding]] 的边界：embedding 是语义表示；L2 normalization 是对表示结果的几何处理。

和 [[Dense Retrieval]] 的边界：dense retrieval 是用稠密向量召回候选的检索路线；L2 normalization 是这条路线里可能出现的相似度计算前处理。

和 [[Vector Database]] 的边界：vector database 负责存储和搜索向量；是否需要预先 L2 normalize、使用 cosine / dot product / L2 metric，是索引和检索配置的一部分。

和 [[Vector Similarity Metrics]] 的边界：相似度度量定义“近”的数学规则；L2 normalization 改变向量长度，从而影响 dot product / cosine / L2 distance 的排序关系。

和 [[Reciprocal Rank Fusion]] 的边界：RRF 绕开不同检索器分数不可比的问题，用排名融合；L2 normalization 不融合多路结果，只处理单路向量的长度。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：L2 范数、单位向量、cosine 与 dot product 在单位向量上的等价关系是稳定数学基础。
- 易变部分：具体 embedding 模型是否默认归一化、向量库 metric 名称、索引实现和性能优化属于实现细节。
- 复查点：换 embedding 模型或向量库 metric 时，要确认索引侧和查询侧是否使用同一归一化策略。

## 现代系统怎么吸收 L2 Normalization 的价值

生产 RAG 系统通常不会把 L2 normalization 当成独立能力，而是把它放在 embedding pipeline 或 vector search 配置里。关键工程要求是“一致”：离线写入 chunk embedding 时怎么处理，在线生成 query embedding 时也要怎么处理；如果一侧 normalized、一侧没有，排序会变得难以解释。

更细的判断是：如果系统使用 cosine similarity，很多库会内部处理归一化；如果系统用 inner product / dot product 近似 cosine，就更需要确认向量是否已经单位化。

## 证据锚点

- [[AI Engineering From Scratch - Embeddings#关键事实]]
- [[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？#第三步：向量检索（ANN 搜索）+ 多路召回]]
- [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#向量检索：语义匹配，靠 Embedding]]
- [[raw/repos/xiaolinnote/questions/040 ai rag 7. Embedding 有哪几种算法你了解过吗？#第三代：句子级对比学习 Embedding（SBERT / SimCSE / BGE）]]
- [[raw/repos/agent_java_offer/questions/066 01_AI 03_RAG 一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。#3. 子问题：一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。]]

- Evidence type: RAG source notes support the cosine / dot product vector-retrieval context; the L2 norm formula is stable mathematical definition.
- Confidence: high for mathematical boundary, medium for provider-specific defaults.
- Boundary: 本卡记录向量尺度处理，不把它提升成新的 retrieval strategy，也不把它和 hybrid search 的分数归一化混为一谈。

## 复习触发

1. 为什么两个向量都 L2 normalize 后，dot product 可以当作 cosine similarity？
2. 如果 embedding 没有归一化，dot product 会比 cosine 多受什么影响？
3. 为什么 L2 normalization 不能修复检索结果“语义相关但事实不支持”的问题？

## 相关链接

- [[Embedding]]
- [[Dense Retrieval]]
- [[Vector Database]]
- [[Vector Similarity Metrics]]
- [[Hybrid Search]]
- [[Reciprocal Rank Fusion]]
