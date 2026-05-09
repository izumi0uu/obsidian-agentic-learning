---
type: source
source_type: paper
title: "The Llama 3 Herd of Models"
url: "https://arxiv.org/abs/2407.21783"
pdf: "https://arxiv.org/pdf/2407.21783"
author:
  - Dubey et al.
site: arXiv
topic:
  - llm
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
  - "[[LLM]]"
  - "[[Evaluation]]"
---

# The Llama 3 Herd of Models

## 为什么收

这篇适合作为现代开源 LLM 训练流水线的综合案例：预训练、数据清洗、后训练、安全、工具使用、多模态和评测都在同一系统里出现。

## 一句话

Llama 3 把大规模预训练、数据治理、指令调优、偏好优化、安全训练和多任务评测组合成完整模型家族训练流程。

## 需要我读的内容

- Training overview
- pre-training data and filtering
- post-training
- safety and evaluations
- tool use / coding / multilingual / multimodal 相关部分

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- data curation
- post-training
- synthetic data

## 边界提醒

模型训练流水线和产品 Agent runtime 仍是两层。训练能提升模型适配框架的能力，但不能替代工具执行、权限和审计。
