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
  - "[[Multi-Head Attention]]"
  - "[[LLM]]"
---

# Self-Attention

## 一句话

Self-Attention 是让同一个序列中的不同位置互相“看见”并计算关系的机制。

## 它解决什么问题

语言里很多依赖不是相邻的。一个词可能需要参考前面很远的词。Self-Attention 让每个位置可以关注同一序列中的其他位置，从而建模长距离依赖。

## 它不是什么

Self-Attention 不是人类注意力。

它也不是模型的长期记忆。它只在当前输入序列和当前计算中建立位置之间的关系。

## 最小例子

在句子“那个学生交了作业，因为他很认真”中，“他”需要和“那个学生”建立关系。Self-Attention 提供了一种让这些位置直接交互的方式。

## 常见误解

- attention 权重看起来像解释，但不一定等于真实因果解释。
- Self-Attention 能处理序列内部关系，但不能替代外部知识库。

## 边界细节

Self-Attention 是 Transformer 的核心机制之一。它和 [[Memory]] 的区别很关键：attention 处理当前上下文，memory 处理跨上下文的保存和检索。

## 证据锚点

- Source: [[Attention Is All You Need]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Transformer]]
- [[Multi-Head Attention]]
- [[LLM]]
- [[Attention Is All You Need]]
