---
type: source
source_type: paper
title: "Constitutional AI: Harmlessness from AI Feedback"
url: "https://arxiv.org/abs/2212.08073"
pdf: "https://arxiv.org/pdf/2212.08073"
author:
  - Bai et al.
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
  - "[[Guardrails]]"
---

# Constitutional AI - Harmlessness from AI Feedback

## 为什么收

这篇适合理解 RLAIF / AI feedback 如何参与模型对齐：不只靠人类逐条标注，也可以用原则和 AI 反馈生成改进信号。

## 一句话

Constitutional AI 用一组原则引导模型自我修改回答，并用 AI feedback 训练更无害的助手行为。

## 需要我读的内容

- Abstract
- supervised learning from AI feedback
- reinforcement learning from AI feedback
- constitution / principles 的角色

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- RLAIF
- AI feedback
- alignment

## 边界提醒

Constitutional AI 是训练/对齐方法，不等于运行时 [[Guardrails]]。训练可以塑造倾向，运行时仍需要权限、审计和策略。
