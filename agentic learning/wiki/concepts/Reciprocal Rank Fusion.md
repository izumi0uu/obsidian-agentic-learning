---
type: concept
topic:
  - rag
  - retrieval
  - ranking
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - RRF
  - RRF 算法
  - 倒数排名融合
  - 互倒排名融合
  - reciprocal rank fusion
source:
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#混合检索：两者结合]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#结果融合：RRF 算法]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第三层：召回优化]]"
up:
  - "[[Multi-Route Retrieval]]"
relations:
  - type: used_by
    target: "[[Hybrid Search]]"
    note: "Hybrid Search 常用 RRF 把 dense/vector 与 sparse/BM25 两路排序融合。"
  - type: precedes
    target: "[[Reranking]]"
    note: "RRF 是候选融合/粗排；reranking 是融合后对较小候选集做精排。"
related:
  - "[[Multi-Route Retrieval]]"
  - "[[Hybrid Search]]"
  - "[[Dense Retrieval]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Reranking]]"
---

# Reciprocal Rank Fusion

## 一句话

Reciprocal Rank Fusion（RRF，倒数排名融合）是一种把多路检索结果按“排名倒数”合成统一排序的方法，常用于 hybrid search 和多路召回。

## 概念详解

多路召回会带来一个直接问题：不同检索器的分数尺度不可比。[[Dense Retrieval]] 可能输出余弦相似度，[[BM25]] 可能输出没有固定上界的词项打分，图检索或业务规则又可能有自己的分数。如果直接把这些原始分数相加，常常会被量纲和分布差异误导。

RRF 的思路是绕开原始分数，只看每一路内部排名。一个文档在某一路排第 1，就给它较高的倒数排名分；排第 10，就给较低的分。多路分数相加后，多个检索器都排得靠前的文档会被提升，只有一路命中的文档也不会被完全丢掉。xiaolinnote 的多路召回 source note 把它放在 dense、BM25、多 Query 三路召回之后，用来合成统一候选列表。

RRF 的学习价值在于它把“召回融合”从模型能力问题变成一个稳定工程模式：先让不同路线覆盖不同失败模式，再用排名层面的融合降低分数不可比的风险。它通常发生在 [[Reranking]] 之前；RRF 先把候选集合并成粗排序，reranker 再对更小候选集做深度相关性判断。

RRF 的价值在于简单、稳健、少依赖分数校准。它把每一路的内部排名转换成可加的倒数排名分，因此适合把 BM25、dense retrieval、multi-query 或其他候选列表合在一起。它不能理解文档内容，只是在候选层做 rank fusion；如果每一路召回都错，RRF 也救不了。实践中常把 RRF 后的候选再交给 reranker 或 context selection，避免只靠排名融合决定最终上下文。

所以它适合做融合基线，再交给后续精排和证据筛选。

它回答的是“多路排名如何先公平合并”。
## 它解决什么问题

它解决多路检索分数不可比的问题：向量相似度、BM25 分数、图检索权重和多 query route 的排序结果不能直接加权时，可以先用每一路排名做融合。

## 它不是什么

RRF 不是 [[Reranking]]。RRF 主要融合多个排序列表；reranking 重新判断 query-document 相关性。

RRF 也不是 [[Hybrid Search]] 本身。Hybrid Search 是 dense + sparse 等检索信号的组合；RRF 是其中一种常见融合算法。

它也不是保证答案正确的评估指标。融合后的候选仍然需要 citation、faithfulness 和 RAG evaluation。

## 最小例子

```text
score(doc) = Σ 1 / (k + rank_i(doc))
```

如果 `doc_a` 在向量检索排第 1，在 BM25 排第 4；`doc_b` 只在 BM25 排第 1，RRF 会给两者都保留机会，但更偏向多路都靠前的候选。

## 常见误解 / 风险

- 误以为 RRF 能修复完全没召回到的证据；它只能融合已有候选。
- 忽略去重：同一 chunk 或同一文档不同片段需要合理合并。
- 不记录 route trace，导致无法解释候选为什么排前。
- 把 RRF 和 MRR 混淆：RRF 是融合算法；MRR 是评估排名质量的指标。

## 边界细节

和 [[Multi-Route Retrieval]] 的边界：multi-route 是组织多条召回路线；RRF 是路线结果的融合方式之一。

和 [[Hybrid Search]] 的边界：hybrid search 常用 RRF，但也可以用权重归一化、学习排序或产品内置融合。

和 [[Reranking]] 的边界：RRF 是粗融合；reranking 是更深的 query-document 相关性判断。

## 现代性状态

- 判定：current-practice。
- 稳定部分：rank-based fusion 是多路检索里常见、易落地的融合方式。
- 易变部分：具体 `k` 值、去重策略、路由权重、是否再接学习排序，需要按数据评估。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#结果融合：RRF 算法]]
- [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#混合检索：两者结合]]
- [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第三层：召回优化]]

- Evidence type: RAG interview notes + multi-route retrieval/ranking synthesis.
- Boundary: RRF 是排名融合算法，不是检索器、embedding 模型、reranker，也不是 hybrid search 的全部。
## 复习触发

1. 为什么多路检索不能直接把 dense 分数和 BM25 分数相加？
2. RRF 和 [[Reranking]] 的边界是什么？
3. RRF 为什么仍然需要 trace 和 evaluation？

## 相关链接

- [[Multi-Route Retrieval]]
- [[Hybrid Search]]
- [[Dense Retrieval]]
- [[Sparse Retrieval]]
- [[BM25]]
- [[Reranking]]

