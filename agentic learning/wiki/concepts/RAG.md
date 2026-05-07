---
type: concept
topic:
  - rag
  - knowledge-base
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
  - "[[Memory]]"
  - "[[Evaluation]]"
  - "[[Retriever]]"
  - "[[Parametric Memory]]"
  - "[[Non-Parametric Memory]]"
---

# RAG

## 一句话

RAG 是 Retrieval-Augmented Generation：先从外部知识库检索相关内容，再让模型基于这些内容生成回答。

## 它解决什么问题

RAG 让系统可以使用模型参数以外的知识，例如公司的文档、个人笔记、最新资料或领域数据库。

经典 RAG 论文把模型参数里的知识称为 [[Parametric Memory]]，把外部可检索知识称为 [[Non-Parametric Memory]]。RAG 的关键就是让生成模型通过 [[Retriever]] 使用外部知识。

## 它不是什么

RAG 不是长期记忆的全部。

RAG 不能保证回答一定正确。检索可能漏掉资料，资料本身可能过期，模型也可能误读检索结果。

## 最小流程

```text
用户问题 -> 检索相关笔记 -> 拼入上下文 -> LLM 生成回答 -> 引用来源或链接
```

## 经典论文边界

[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]] 里的 RAG 强调“生成模型 + 检索器 + 外部索引”。它不是简单把资料复制进 prompt，而是把检索作为生成过程的一部分。

## Obsidian 场景

如果把 Obsidian 笔记接入 LLM，好的笔记切分会很重要：

- 一张概念卡只讲一个概念。
- 标题要清楚。
- 每张卡写出“它不是什么”。
- 关键概念之间用双链连接。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[Memory]]
- [[Evaluation]]
- [[Retriever]]
- [[Parametric Memory]]
- [[Non-Parametric Memory]]
