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

# Positional Encoding

## 一句话

Positional Encoding 是给 Transformer 输入注入位置信息的机制。

## 它解决什么问题

Transformer 去掉了 recurrence 和 convolution，所以模型本身不会天然知道 token 的顺序。Positional Encoding 把位置相关信息加到输入表示中，让模型能区分“我喜欢你”和“你喜欢我”这种顺序差异。

## 它不是什么

Positional Encoding 不是上下文窗口。

它也不是长期记忆。它只帮助模型在当前序列中感知位置。

## 最小例子

如果一句话有 10 个 token，模型需要知道第 1 个 token 和第 8 个 token 不是同一个位置。Positional Encoding 给每个位置加入可区分的位置信号。

## 常见误解

- 有位置信息不等于能无限处理长文本。
- 原始 Transformer 的正弦/余弦位置编码不是现代所有 LLM 的唯一做法。

## 边界细节

位置编码和长上下文能力相关，但不是同一个概念。长上下文还涉及训练长度、注意力实现、位置外推、检索和上下文工程。

## 证据锚点

- Source: [[Attention Is All You Need]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Transformer]]
- [[Self-Attention]]
- [[LLM]]
- [[Attention Is All You Need]]
