---
type: concept
topic:
  - rag
  - retrieval
  - query
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - Multi-Query
  - 多 Query 扩展
  - 多 Query 扩展召回
  - 多查询检索
  - 多查询召回
  - multi-query retrieval
source:
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法四：多 Query 扩展]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第三路：多 Query 扩展召回]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第二层：查询优化]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
up:
  - "[[Query Rewrite]]"
relations:
  - type: composes_with
    target: "[[Multi-Route Retrieval]]"
    note: "Multi-Query Retrieval 可以作为多路召回中的 query route，用多个问题变体扩大覆盖。"
  - type: contrasts_with
    target: "[[Query Planning]]"
    note: "Multi-query 是生成多个检索 query；query planning 更强调任务/子问题/知识源的规划。"
related:
  - "[[Query Rewrite]]"
  - "[[Retriever]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Dense Retrieval]]"
  - "[[Hybrid Search]]"
  - "[[RAG Evaluation]]"
---

# Multi-Query Retrieval

## 一句话

Multi-Query Retrieval（多查询检索 / 多 Query 扩展）是让 LLM 或规则从原始问题生成多个检索 query，分别检索后合并结果，以提高覆盖率。

## 概念详解

用户问题和知识库文档之间不只存在同义词差异，还存在“提问角度”差异。用户问“产品多久能送到”，文档可能写“配送时效说明”；单个 query 的向量相似度或关键词命中都可能不够。Multi-Query Retrieval 的策略是把一个问题扩展成 3～5 个不同角度的问法，每个 query 单独检索，再把结果合并去重。

它和 [[Query Rewrite]] 有重叠，但边界不同。Query Rewrite 是更大的检索前处理家族，可以做口语改写、补全上下文、HyDE、step-back、多 query 等；Multi-Query Retrieval 特指“保留同一用户意图，但生成多个查询视角并并行检索”的策略。它也常作为 [[Multi-Route Retrieval]] 的一路：dense route、BM25 route、多 query route 分别补不同盲区。

关键工程边界是：原始问题通常要保留在检索列表里。因为 LLM 改写可能丢掉产品型号、时间限制、否定词或用户原始细节；如果只用改写版本，可能提高覆盖同时引入偏题。多 query 的收益也不是免费的：更多 LLM 调用、更多检索请求、更多重复候选和更复杂的融合/评估。

Multi-Query Retrieval 的动机是：一个用户问题可能只有一种表达，但相关资料可能用不同术语、粒度或视角表达。系统让模型或规则生成多个 query，从不同表述切入检索，再合并候选。它可以提高召回，尤其适合模糊问题、同义词多、跨领域术语不一致的知识库；但 query 数量越多，噪音、成本和融合复杂度也会上升，因此常要配合去重、RRF、rerank 和上下文预算控制。
## 它解决什么问题

它解决单一 query 角度太窄的问题：当文档描述角度、用户表达风格或信息需求维度不一致时，多 query 可以扩大候选覆盖。

## 它不是什么

Multi-Query Retrieval 不是简单改写成一个更规范问题。它是多个 query 变体并行或批量检索。

它也不是 [[Query Planning]]。Query planning 通常会拆子问题、选择知识源、决定检索顺序；multi-query 可以只是同一问题的多种表述。

它不是 [[Multi-Route Retrieval]] 的全部。多路召回还可以包括 dense、sparse、graph、metadata filter、多索引等路线。

## 最小例子

```text
原始问题：怎么退货？
queries:
  1. 怎么退货？
  2. 申请售后流程是什么？
  3. 退款退货政策在哪里？
  4. 商品不满意如何办理退回？
每个 query 分别 retrieve -> 合并去重 -> rerank
```

## 常见误解 / 风险

- 只用改写 query，不保留原始 query，导致细节丢失。
- 生成太多 query，带来重复、噪音、成本和延迟。
- 没有融合策略，多个 query 的结果只是机械拼接。
- 把 multi-query 的覆盖提升误认为最终答案一定更忠实。

## 边界细节

和 [[Query Rewrite]] 的边界：Multi-Query Retrieval 是 query rewrite 家族里的一种扩展策略。

和 [[Dense Retrieval]] 的边界：多 query 可以分别走 dense retrieval，也可以走 sparse/hybrid route；它不是向量检索本身。

和 [[Reciprocal Rank Fusion]] 的边界：multi-query 产生多组候选；RRF 可用于融合这些候选排序。

## 现代性状态

- 判定：current-practice。
- 稳定部分：多 query 扩展是 RAG 检索优化常见策略。
- 易变部分：query 生成方式、数量、过滤、融合和成本控制需要按线上分布评估。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法四：多 Query 扩展]]
- [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第三路：多 Query 扩展召回]]
- [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第二层：查询优化]]
- [[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]

- Evidence type: RAG retrieval optimization notes + multi-route retrieval synthesis.
- Boundary: Multi-Query Retrieval 是多 query 变体召回，不等于 hybrid search、query planning、reranking 或简单把 top-k 调大。
## 复习触发

1. Multi-Query Retrieval 和单次 Query Rewrite 有什么区别？
2. 为什么原始 query 通常要保留？
3. 多 query 结果应该怎样合并和评估？

## 相关链接

- [[Query Rewrite]]
- [[Multi-Route Retrieval]]
- [[Retriever]]
- [[Reciprocal Rank Fusion]]
- [[Reranking]]

