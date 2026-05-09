---
type: source
source_type: paper
title: "Training Language Models to Follow Instructions with Human Feedback"
url: "https://arxiv.org/abs/2203.02155"
pdf: "https://arxiv.org/pdf/2203.02155"
author:
  - Ouyang et al.
site: arXiv
topic:
  - llm
  - training
  - alignment
created: 2026-05-09
updated: 2026-05-09
last_checked: 2026-05-09
freshness: stable
conflicts: []
status: seed
source:
related:
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[Evaluation]]"
---

# Training Language Models to Follow Instructions with Human Feedback

## 为什么收

这篇 InstructGPT 论文适合理解为什么基础模型还需要 instruction tuning、reward model 和 RLHF，才能更像可用助手。

## 一句话

InstructGPT 用人类示范和偏好反馈训练模型更好地遵循用户指令。

## 需要我读的内容

- Abstract
- supervised fine-tuning
- reward model
- reinforcement learning from human feedback

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- instruction tuning
- RLHF
- reward model

## 边界提醒

RLHF 改善有用性和偏好一致性，但不自动保证事实正确、推理最优或工具调用安全。
