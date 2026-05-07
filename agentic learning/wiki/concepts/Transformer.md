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
  - "[[LLM]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Positional Encoding]]"
---

# Transformer

## 一句话

Transformer 是一种主要基于 attention 的序列建模架构，是现代 LLM 的重要架构地基。

## 它解决什么问题

在 Transformer 之前，很多序列模型依赖 RNN 或 CNN。RNN 按时间步顺序处理，训练时难以充分并行；CNN 需要多层堆叠才能连接远距离位置。

Transformer 用 self-attention 让序列中不同位置可以直接建立联系，并且更适合并行训练。

## 它不是什么

Transformer 不是 Agent。

Transformer 也不是完整的 LLM 产品。它是模型架构层面的东西，不包含工具调用、记忆、RAG、评估或人类确认。

## 最小例子

一句话中，“it” 指代前面哪个名词，需要模型理解远距离依赖。Transformer 可以通过 attention 让当前位置直接关注其他相关位置。

## 常见误解

- Transformer 不等于 ChatGPT。
- Attention 权重不一定能直接解释模型的全部推理原因。
- Transformer 解决的是序列建模架构问题，不直接解决事实可靠性问题。

## 边界细节

对 Agent 学习来说，Transformer 只回答“LLM 为什么能成为强大的语言生成底座”。它不回答“系统如何行动”。

## 证据锚点

- Source: [[Attention Is All You Need]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- [[Attention Is All You Need]]
