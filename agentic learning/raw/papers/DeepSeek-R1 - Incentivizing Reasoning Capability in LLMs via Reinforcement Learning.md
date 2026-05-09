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
updated: 2026-05-09
last_checked: 2026-05-09
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[LLM Training Pipeline]]"
  - "[[Reasoning Trace]]"
  - "[[Evaluation]]"
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
