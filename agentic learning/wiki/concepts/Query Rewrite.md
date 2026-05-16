---
type: concept
topic:
  - rag
  - retrieval
status: growing
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: watch
source:
  - "[[Retriever]]"
  - "[[Azure AI Search Agentic Retrieval]]"
  - "[[RAG 类型对比]]"
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
evidence:
  - "[[Retriever#概念详解]]"
  - "[[Azure AI Search Agentic Retrieval#一句话]]"
  - "[[Azure AI Search Agentic Retrieval#边界提醒]]"
  - "[[RAG 类型对比#核心区别表]]"
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法二：HyDE（Hypothetical Document Embeddings）]]"
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法三：Step-back Prompting（后退提问）]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第二层：查询优化]]"
related:
  - "[[Retriever]]"
  - "[[Query Planning]]"
  - "[[Agentic Retrieval]]"
  - "[[Hybrid Search]]"
  - "[[Multi-Query Retrieval]]"
aliases:
  - "Query Rewriting"
  - "查询改写"
  - "问题改写"
---

# Query Rewrite

## 一句话

Query Rewrite 是把用户原始问题改写成更适合检索系统的查询表达，以提高召回、精确匹配或上下文对齐。

## 概念详解

用户提问通常是面向人类的自然语言，而检索系统需要更明确的关键词、实体、同义词、过滤条件或子表达。Query Rewrite 介于用户问题和 [[Retriever]] 之间：它不改变用户真正想问的任务，而是把问题变成更容易被向量检索、关键词检索、hybrid search 或结构化过滤命中的形式。

最简单的 rewrite 是补全省略词、替换同义词、展开缩写、提取关键词或生成多种检索 query（[[Multi-Query Retrieval]]）。例如用户问“那个框架支持可恢复执行吗？”系统可能结合上下文改写成“LangGraph durable execution checkpoint human-in-the-loop”。复杂一点的 rewrite 会保留原问题，同时生成多个候选查询并合并结果。

常见子策略里，HyDE（Hypothetical Document Embeddings）先让模型生成一个“像文档的假设答案”，再用这个假设答案去检索；Step-back Prompting 则把具体问题往上抽象一层，先查背景知识再回答具体问题。HyDE 更适合“问题和文档文体差异大”的场景，Step-back 更适合“问题太具体、需要背景原理”的场景。它们都属于 rewrite family，而不是 [[Query Planning]]：rewrite 主要改“怎么问”，planning 主要改“先问什么、再问什么”。

证据边界：[[Retriever]] 卡已经把 query rewrite 放在现代 retriever 的组成部分；[[Azure AI Search Agentic Retrieval]] 支持复杂检索中 query planning、多查询和 knowledge source 的现代方向；xiaolinnote source note 支持 HyDE、Step-back 和多 Query 作为 query rewrite 子策略。本卡只沉淀 rewrite 这个最小动作，不把它等同于完整 agentic retrieval。

## 它解决什么问题

它解决“用户语言和索引语言不匹配”的问题：用户说法含糊、缺实体、用了代词、用了业务昵称或跨语言表达时，直接检索可能漏掉关键文档。

## 它不是什么

Query Rewrite 不是 [[Query Planning]]。Rewrite 主要改写表达；planning 还会拆子问题、安排检索顺序和选择知识源。

Query Rewrite 也不是答案生成。它只改变检索请求，不直接回答用户问题。

## 最小例子

```text
原问题：它支持人工审批吗？
对话上下文：正在比较 LangGraph
rewrite：LangGraph human-in-the-loop approval interrupt checkpoint
```

## 常见误解 / 风险

- 误解：rewrite 总会提高检索。改写错会偏离原问题。
- 误解：只要 LLM 改写就比原 query 好。专有名词、代码符号和编号可能应保留原文。
- 风险：rewrite 把用户限制条件丢掉，例如时间、权限、否定词或产品版本。
- 风险：rewrite 过程被 prompt injection 影响，把恶意指令变成检索目标。

## 边界细节

和 [[Hybrid Search]] 的边界：rewrite 改查询表达，hybrid search 改召回信号；两者可以结合。

和 [[Reranking]] 的边界：rewrite 影响候选集合，reranking 只重排已有候选。

和 [[Agentic Retrieval]] 的边界：agentic retrieval 可能包含 rewrite，但还包括 query planning、多源检索、并行子查询和 grounding data 合并。

## 现代性状态

- 判定：current-practice。
- 稳定部分：检索前改写 query 是 RAG / search 系统常见质量层。
- 易变部分：LLM rewrite prompt、multi-query 策略、产品 API 和自动评估方式会变化。
- 复查点：rewrite 上线前要跑 retrieval eval，比较原 query 与 rewrite 后的 recall / precision。

## 现代系统怎么吸收 Query Rewrite 的价值 / 局限

现代系统通常会保留原 query 与 rewritten query，并在 trace 里记录 rewrite 理由、检索结果和最终采用的 evidence。这样 rewrite 出错时能回放。更稳的系统会同时检索原 query 和 rewrite query，避免改写丢失关键限制。

局限是 rewrite 会引入一个新的 LLM 决策点：它可能过度解释用户意图、丢掉否定条件或暴露隐私。高风险任务需要可观察、可评估和可回退。

## 证据锚点

- Concept anchor: [[Retriever#概念详解]]
- Source anchor: [[Azure AI Search Agentic Retrieval#一句话]]
- Source anchor: [[Azure AI Search Agentic Retrieval#边界提醒]]
- Topic anchor: [[RAG 类型对比#核心区别表]]
- Evidence type: existing retriever concept + official source note + engineering synthesis.

- Boundary: Query Rewrite 改善检索输入表达，不改变用户真实意图；它不同于 Query Planning 的子任务规划，也不同于 Reranking 的候选排序。
## 复习触发

1. Query Rewrite 和 Query Planning 的最小区别是什么？
2. 为什么 rewrite 后仍应保留原始 query？
3. rewrite 会怎样破坏否定词、版本号或权限限制？

## 相关链接

- [[Retriever]]
- [[Query Planning]]
- [[Agentic Retrieval]]
- [[Query Rewrite Query Planning Agentic Retrieval 对比]]
- [[Hybrid Search]]
