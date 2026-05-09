---
type: concept
topic:
  - llm
status: growing
created: 2026-05-05
updated: 2026-05-09
last_checked: 2026-05-09
freshness: stable
conflicts: []
source:
  - "[[Attention Is All You Need]]"
evidence:
  - "[[Attention Is All You Need#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Transformer]]"
  - "[[LLM Training Pipeline]]"
  - "[[Tool Calling]]"
  - "[[RAG]]"
  - "[[Memory]]"
---

# LLM

## 一句话

LLM 是大语言模型，擅长根据上下文生成可能合理的文本。

## 它解决什么问题

LLM 可以理解和生成自然语言，帮助人类完成解释、总结、翻译、改写、代码生成、问答和推理辅助。

现代 LLM 的一个重要架构地基是 [[Transformer]]。Transformer 让模型可以用 [[Self-Attention]] 在当前上下文中建模 token 之间的关系，并通过 [[Multi-Head Attention]] 同时关注不同类型的信息。

## 它不是什么

LLM 不是数据库。它可能说出看起来很确定但实际错误的内容。

LLM 不是长期记忆。对话上下文以外的信息需要外部系统保存。

LLM 不是行动系统。它本身不会真正打开网页、读文件、调用 API 或修改代码，除非被接入工具和运行环境。

LLM 也不等于 Transformer。Transformer 是架构地基，LLM 还涉及预训练数据、tokenization、规模化训练、对齐、推理策略、工具接入和产品系统。

LLM 也不等于训练流水线。[[LLM Training Pipeline]] 解释模型怎样通过预训练、后训练、偏好优化、推理强化、工具能力和评测闭环变强。

## 最小例子

我问：“用一句话解释 Agent。”

LLM 可以生成解释。但如果我要它“检查我的仓库并创建笔记”，就需要工具、权限和执行循环。

## 边界细节

LLM 的输出是基于上下文的生成，不是事实本身。Agent 系统经常要用检索、工具调用、测试和人工确认来补足这个边界。

Transformer 解释的是“模型如何在序列中建模关系”，不解释“系统如何可靠行动”。这正是 [[LLM]] 和 [[Agent]] 的重要分界。

## 证据锚点

- Source: [[Attention Is All You Need]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Transformer]]
- [[LLM Training Pipeline]]
- [[Self-Attention]]
- [[Tool Calling]]
- [[RAG]]
- [[Memory]]
