---
type: concept
topic:
  - llm
  - rag
  - memory
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
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[Non-Parametric Memory]]"
---

# Parametric Memory

## 一句话

Parametric Memory 是模型参数中隐含保存的知识。

## 它解决什么问题

预训练模型通过大量数据学习语言和事实模式，这些知识被压缩进参数里。它让模型不需要每次查询外部数据库也能回答很多问题。

## 它不是什么

Parametric Memory 不是可直接编辑的数据库。

它也不能稳定提供来源引用。模型说出的事实可能来自训练数据，也可能是生成错误。

## 最小例子

LLM 知道“巴黎是法国首都”可能来自参数中的知识，而不是现场检索。

## 边界细节

RAG 的核心动机之一，就是参数化知识难更新、难引用、难检查，所以引入 [[Non-Parametric Memory]]。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[RAG]]
- [[Non-Parametric Memory]]
