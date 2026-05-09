---
type: source
source_type: paper
title: "Training Compute-Optimal Large Language Models"
url: "https://arxiv.org/abs/2203.15556"
pdf: "https://arxiv.org/pdf/2203.15556"
author:
  - Hoffmann et al.
site: arXiv
topic:
  - llm
  - training
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
---

# Training Compute-Optimal Large Language Models

## 为什么收

这篇通常被称为 Chinchilla，适合理解“只堆参数不够，数据 token 也要按计算预算匹配”的训练边界。

## 一句话

在固定训练计算量下，模型参数量和训练 token 数需要更平衡，模型才更 compute-optimal。

## 需要我读的内容

- Abstract
- compute-optimal training 的结论
- 对“大模型少数据”和“小模型多数据”的比较

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- compute-optimal training
- data scaling

## 边界提醒

Compute-optimal 不等于产品最优。真实系统还要看延迟、成本、上下文长度、工具能力和部署约束。
