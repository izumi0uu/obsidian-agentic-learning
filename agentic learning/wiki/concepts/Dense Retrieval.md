---
type: concept
topic:
  - rag
  - retrieval
  - search
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - 向量检索
  - 密集检索
  - vector retrieval
  - dense vector retrieval
source:
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#向量检索：语义匹配，靠 Embedding]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第一路：向量检索（Dense Retrieval）]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
up:
  - "[[Retriever]]"
relations:
  - type: contrasts_with
    target: "[[Sparse Retrieval]]"
    note: "Dense Retrieval 用稠密语义向量找相似内容；Sparse Retrieval / BM25 用词项、倒排和词面信号找精确匹配。"
  - type: composes_with
    target: "[[Hybrid Search]]"
    note: "Hybrid Search 常把 dense retrieval 和 sparse/BM25 route 组合起来互补。"
  - type: uses
    target: "[[Embedding]]"
    note: "Dense Retrieval 依赖文档和 query 的 embedding 表示。"
related:
  - "[[Retriever]]"
  - "[[Embedding]]"
  - "[[Vector Database]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Hybrid Search]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Reranking]]"
---

# Dense Retrieval

## 一句话

Dense Retrieval（向量检索 / 密集检索）是把 query 和文档 chunk 转成稠密 embedding 向量，再按向量相似度召回候选证据的检索方式。

## 概念详解

Dense Retrieval 出现的核心原因是：用户的问题和知识库原文经常不用同一组词。用户说“手机截图”，文档可能写“iPhone 截屏教程”；如果只靠词面重叠，[[BM25]] 可能看不到相关性。Dense Retrieval 通过 [[Embedding]] 把 query 和 chunk 放进同一个语义向量空间，再用近似最近邻或向量相似度找 top-k 候选，让系统能跨越同义词、近义词和不同表达方式。

在 RAG pipeline 中，Dense Retrieval 通常分两步：入库时对 chunk 生成向量并存入 [[Vector Database]] 或向量索引；查询时对用户问题或改写后的 query 生成向量，找最近的候选 chunk。它常被中文资料直接叫“向量检索”，但为了避免把“检索器”整体和“向量检索这一条路线”混在一起，本卡用 `Dense Retrieval` 作为 canonical name。

Dense Retrieval 的盲区也很稳定：它对产品型号、错误码、函数名、数字、表字段、缩写等精确词面信号不一定敏感。source note 里反复用 `M4 Pro`、`RTX 4090` 这类例子说明：向量空间里“语义接近”不等于“包含精确实体”。因此生产 RAG 常把 dense route 与 [[Sparse Retrieval]] / [[BM25]] 组合成 [[Hybrid Search]]，或作为 [[Multi-Route Retrieval]] 的一路，再用 [[Reciprocal Rank Fusion]]、去重和 [[Reranking]] 控制最终候选。

## 它解决什么问题

它解决“同义表达、口语化表达、跨表述角度导致关键词匹配漏召回”的问题。尤其当用户问题和文档描述语义相近但词面不同，dense retrieval 往往比纯关键词检索更容易找到候选。

## 它不是什么

Dense Retrieval 不是整个 [[Retriever]]。Retriever 是组件或流程，可以包含 dense、sparse、metadata filter、query rewrite、权限过滤、reranking 等步骤。

它也不是 [[Embedding]] 本身。Embedding 是表示方法；Dense Retrieval 是用这个表示做在线召回。

它更不是“高级所以总比 BM25 好”。在精确实体、编号和代码符号场景，[[BM25]] / [[Sparse Retrieval]] 可能更可靠。

## 最小例子

```text
入库：chunk -> embedding -> vector index
查询：question -> query embedding -> nearest neighbors top-k -> candidate chunks
```

如果 query 是“怎么退货”，文档写“申请售后流程”，dense route 可能找到；如果 query 是“ERR_CONNECTION_RESET”，dense route 可能不如 BM25 稳。

## 常见误解 / 风险

- 误把“向量检索”链接到 [[Retriever]]，导致路线和组件混淆。
- 以为换更强 embedding 模型就能解决所有检索问题。
- 忽略向量索引、chunking、metadata filter 和权限过滤对结果的影响。
- 只看相似度分数，不检查候选是否真的回答问题。

## 边界细节

和 [[Sparse Retrieval]] 的边界：dense 关注语义相似，sparse 关注词项/倒排/精确匹配。

和 [[Hybrid Search]] 的边界：hybrid search 通常把 dense route 与 sparse/BM25 route 合并；dense retrieval 只是其中一路。

和 [[Multi-Route Retrieval]] 的边界：multi-route 可以包含 dense、BM25、多 query、图检索、metadata filter 等多条路线；dense retrieval 是其中最常见的语义路线。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：RAG 常用稠密向量召回语义相似 chunk。
- 易变部分：embedding 模型、向量索引、ANN 算法、reranker 组合和产品能力变化快。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#向量检索：语义匹配，靠 Embedding]]
- [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第一路：向量检索（Dense Retrieval）]]
- [[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]

## 复习触发

1. 为什么“向量检索”不应该默认等同于 [[Retriever]]？
2. Dense Retrieval 在哪些场景不如 [[BM25]]？
3. Dense Retrieval、[[Embedding]]、[[Vector Database]] 三者边界是什么？

## 相关链接

- [[Retriever]]
- [[Embedding]]
- [[Vector Database]]
- [[Sparse Retrieval]]
- [[BM25]]
- [[Hybrid Search]]
- [[Multi-Route Retrieval]]

