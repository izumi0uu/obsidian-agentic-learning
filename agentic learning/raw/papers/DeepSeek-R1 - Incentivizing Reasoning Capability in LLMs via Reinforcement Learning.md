---
type: source
source_type: paper
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
url: "https://arxiv.org/abs/2501.12948"
pdf: "https://arxiv.org/pdf/2501.12948"
author:
  - DeepSeek-AI
site: arXiv
topic:
  - llm
  - reasoning
  - training
created: 2026-05-09
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[LLM Training Pipeline]]"
  - "[[Reasoning Trace]]"
  - "[[Evaluation]]"
  - "[[Zero-shot CoT]]"
---

# DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

## 为什么收

这篇适合理解现代 reasoning model 为什么不只是“会补全文本”，还会通过强化学习和可验证任务信号训练更长的推理、检查和修正行为。

## 一句话

DeepSeek-R1 探索用强化学习激发 LLM 的推理能力，尤其是数学、代码和可验证问题上的多步推理。

## 需要我读的内容

- Abstract
- RL 如何作用于 reasoning
- cold start / distilled models / evaluation 部分

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- reasoning reinforcement learning
- verifiable reward

## 边界提醒

推理强化能增强多步问题能力，但不等于 Agent runtime。模型仍需要工具、状态、权限和 trace 才能可靠行动。

## R1-Lite-Preview 时间线补充

DeepSeek 官方 API Docs 记录：DeepSeek-R1-Lite-Preview 在 2024-11-20 发布，定位为 o1-preview 级别的 reasoning model，强调 AIME / MATH benchmark 表现、实时透明 thought process，以及 “Longer Reasoning, Better Performance” 的 inference scaling 现象。

边界：R1-Lite-Preview 从用户视角很像“模型自己在写很长的 CoT”，但这不等于经典 [[Zero-shot CoT]] prompting。Zero-shot CoT 是用户在 prompt 里加“让我们一步步思考”来触发推理文本；R1 / R1-Lite 这类 reasoning model 则更接近把长推理、验证、反思和策略调整训练进模型行为，再在推理时用更多 token 展开。

## R1 正式版补充

DeepSeek-R1 在 2025-01-20 正式发布；官方 release note 强调 large-scale RL in post-training、minimal labeled data 和 math/code/reasoning tasks on par with OpenAI-o1。arXiv 论文摘要也把重点放在通过强化学习激发 reasoning patterns，例如 self-reflection、verification 和 dynamic strategy adaptation。

## 与 CoT 论文脉络的关系

DeepSeek-R1 属于 CoT / reasoning research 的后续工程化和训练化路线，而不是简单的 Zero-shot CoT prompt 复用。

- CoT / Zero-shot CoT 提供了“显式中间推理有助于复杂问题”的基础观察。
- R1-Zero / R1 关注的是如何通过 RL 和多阶段训练，让模型自然产生更长、更可验证、带自我检查的 reasoning behavior。

所以在复习时可以说：R1 参考并继承了 CoT 这条研究脉络，但它的关键贡献是训练方法，不是 prompt 模板。
