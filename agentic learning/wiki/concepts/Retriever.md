---
type: concept
topic:
  - rag
  - retrieval
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Non-Parametric Memory]]"
  - "[[Evaluation]]"
---

# Retriever

## 一句话

Retriever 是根据输入问题从外部知识库中找出相关资料的组件。

## 它解决什么问题

生成模型不能可靠知道所有事实，也不能自然引用来源。Retriever 负责把可能相关的外部证据找出来，供后续生成或判断使用。

## 它不是什么

Retriever 不是答案生成器。

检索到相关资料也不等于回答正确。检索可能漏掉关键证据，也可能找出相似但无关的资料。

## 最小例子

用户问一个事实问题，Retriever 从文档索引里找出 top-K passages，然后生成模型基于这些 passages 回答。

## 边界细节

RAG 失败常常不是模型“不会写”，而是 Retriever 没找到对的证据，或把错误证据放进上下文。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Non-Parametric Memory]]
- [[Evaluation]]
