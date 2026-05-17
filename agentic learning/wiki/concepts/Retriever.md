---
type: concept
topic:
  - rag
  - retrieval
status: growing
created: 2026-05-05
updated: 2026-05-16
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
  - "[[Azure AI Search Agentic Retrieval]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#Ingest 摘要]]"
  - "[[Azure AI Search Agentic Retrieval#一句话]]"
related:
  - "[[RAG]]"
  - "[[Non-Parametric Memory]]"
  - "[[Evaluation]]"
  - "[[Agentic Retrieval]]"
  - "[[Dense Retrieval]]"
  - "[[Sparse Retrieval]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Reranking]]"
aliases:
  - 检索器
  - 召回器
---

# Retriever

## 一句话

Retriever 是根据输入问题从外部知识库中找出相关资料的组件。

## 概念详解

Retriever 是 RAG 里的“找证据”组件。经典 RAG 论文把它放在生成模型前面：输入问题先进入 retriever，retriever 从外部文档索引里找出 top-k passages，然后 generator 基于这些 passages 生成答案。这个组件让模型不只依赖参数里的 [[Parametric Memory]]，而能访问外部 [[Non-Parametric Memory]]。

现代 retriever 不一定只是一个向量相似度函数。它可能包含 query rewrite、metadata filter、[[Dense Retrieval|向量检索]]、关键词/全文检索、[[Hybrid Search]]、权限过滤、[[Reranking]]、去重、上下文压缩和引用组织。更复杂的 [[Agentic Retrieval]] 还会先做 query planning，把复杂问题拆成多个子查询，对多个知识源并行检索，再合并 grounding data。

Retriever 的质量直接决定 RAG 的上限。生成模型写得再流畅，如果 retriever 没找到关键证据，答案可能缺事实；如果 retriever 找到相似但无关的片段，模型会被错误上下文误导；如果权限过滤错了，系统可能泄露资料；如果排序错误，正确证据可能在上下文预算外被丢掉。

它的证据边界要分清：经典论文支持 retriever-generator 的基本组合和 dense retrieval 的原始边界；Azure source note 支持现代 agentic retrieval 里的 query planning、多查询和知识源组织。把所有检索决策都叫“Agent”会过度泛化；只有当检索层会规划、分解、重查或选择知识源时，才接近 agentic retrieval。

## 它解决什么问题

生成模型不能可靠知道所有事实，也不能自然引用来源。Retriever 负责把可能相关的外部证据找出来，供后续生成或判断使用。

## 它不是什么

Retriever 不是答案生成器。

检索到相关资料也不等于回答正确。检索可能漏掉关键证据，也可能找出相似但无关的资料。

## 最小例子

用户问一个事实问题，Retriever 从文档索引里找出 top-k passages，然后生成模型基于这些 passages 回答。

```text
question -> query embedding / keyword query -> top-k chunks -> rerank -> context
```

## 常见误解 / 风险

- 误解：Retriever 返回 top-k 就说明证据足够。
- 误解：只要换更强 LLM，就能修复检索漏召回。
- 风险：query rewrite 错误会让检索偏离原问题。
- 风险：权限过滤晚于召回或合并时，可能暴露不该进入上下文的资料。

## 边界细节

RAG 失败常常不是模型“不会写”，而是 Retriever 没找到对的证据，或把错误证据放进上下文。

和 [[Reranking]] 的边界：retriever 常负责召回候选；reranking 负责在候选里精排。很多系统把 reranking 包进 retrieval pipeline，但排查时要分开看。

和 [[Agentic Retrieval]] 的边界：普通 retriever 可以是单次 query；agentic retrieval 会做 query planning、子问题分解、多源检索和合并。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：RAG 需要 retriever 从外部索引取证据。
- 易变部分：dense retriever、hybrid search、agentic retrieval、reranker 和检索产品能力持续变化。
- 复查点：学习新 RAG 架构时，要问它改变的是 retriever、reranker、generator，还是 agent workflow。

## 现代系统怎么吸收 Retriever 的价值

现代系统会把 retriever 做成可观察组件：记录 query、过滤条件、候选列表、分数、被丢弃的文档、rerank 后结果和最终引用。这样 RAG Evaluation 才能判断失败来自检索、排序还是生成。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#Ingest 摘要]]
- Source: [[Azure AI Search Agentic Retrieval]]
- Anchor: [[Azure AI Search Agentic Retrieval#一句话]]
- Evidence type: paper source note + official docs source note + engineering synthesis.
- Confidence: medium
- Boundary: RAG 论文支持 retriever-generator 基础边界；agentic query planning 来自 Azure source note，属于现代检索层扩展，不应反写成经典 RAG 定义。

## 复习触发

- Retriever、reranker、generator 分别错了时，症状有什么不同？
- 为什么检索到“相似资料”不等于检索到“可回答证据”？
- Agentic Retrieval 比普通 Retriever 多了哪些决策？

## 相关链接

- [[RAG]]
- [[Non-Parametric Memory]]
- [[Evaluation]]
- [[Agentic Retrieval]]
