---
type: concept
topic:
  - llm
  - transformer
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Attention Is All You Need]]"
evidence:
  - "[[Attention Is All You Need#为什么收]]"
related:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[LLM]]"
---

# Multi-Head Attention

## 一句话

Multi-Head Attention 是并行运行多个 attention head，让模型从不同表示子空间关注不同关系的机制。

## 它解决什么问题

单个 attention 可能把不同关系平均在一起。多个 head 可以让模型在不同子空间里同时关注不同类型的信息，例如语法关系、指代关系或位置关系。

## 它不是什么

Multi-Head Attention 不是多个 Agent。

它也不是多模型协作。它是单个 Transformer 层内部的计算结构。

## 最小例子

一个 head 可能更关注主语和动词的关系，另一个 head 可能更关注代词和指代对象的关系。最终这些 head 的结果会被拼接和投影。

## 常见误解

- head 数越多不一定越好。
- attention head 的可视化不能直接等同于模型解释。

## 边界细节

对 Agent 学习来说，Multi-Head Attention 说明 LLM 内部可以同时建模多种文本关系，但这仍然不是工具调用、规划或行动。

## 证据锚点

- Source: [[Attention Is All You Need]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Transformer]]
- [[Self-Attention]]
- [[LLM]]
- [[Attention Is All You Need]]
