---
type: concept
topic:
  - rag
  - retrieval
  - evaluation
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
  - "[[RAG Evaluation]]"
---

# Reranking

## 一句话

Reranking 是在初步检索后，用更精细的模型或规则重新排序候选上下文。

## 它解决什么问题

向量库返回的 top-k 不一定是最能回答问题的片段。Reranker 可以在较小候选集上做更精细的 query-document 相关性判断。

## 它不是什么

Reranking 不是扩大召回。

如果初检没有找回正确材料，reranker 只能在错误候选里重新排序。

## 最小例子

```text
retrieve top 50 -> rerank top 8 -> LLM answer
```

## 常见误解和风险

- reranker 会增加延迟和成本。
- reranker 指标好，不等于最终答案忠实。
- 多语言、代码、表格场景要单独评估。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[RAG 类型对比]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Retriever]]
- [[Hybrid Search]]
- [[RAG Evaluation]]
