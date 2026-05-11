---
type: source
source_type: paper
title: "Scaling Laws for Neural Language Models"
url: "https://arxiv.org/abs/2001.08361"
pdf: "https://arxiv.org/pdf/2001.08361"
author:
  - Kaplan et al.
site: arXiv
topic:
  - llm
  - training
created: 2026-05-09
updated: 2026-05-11
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: seed
source:
related:
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
---

# Scaling Laws for Neural Language Models

## 为什么收

这篇论文帮助理解现代 LLM 为什么会沿着参数、数据和算力规模化路线变强。

## 一句话

Scaling laws 描述模型性能如何随模型规模、数据规模和训练计算量变化。


## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 语言模型 loss 与模型规模、数据规模、计算量之间存在经验 scaling 关系。 | arXiv abstract | high | scaling law |
| 固定训练计算下，三种资源的瓶颈会共同影响最优表现。 | arXiv abstract | medium | compute scaling |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。


## 现代性 / 前沿性初判

- foundation：scaling law 是理解 LLM 训练规模化的地基。
- 稳定部分：规模对预训练 loss 的趋势影响仍重要。
- 被修正部分：Chinchilla 等后续工作修正了 compute-optimal 数据/参数分配。
- freshness：stable。

## 需要我读的内容

目标：理解 scaling laws 是规模、数据、算力与 loss 的经验关系，不是“越大越好”的口号。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / loss 的 power-law 关系

- 位置：arXiv abstract / 2001.08361 / last checked 2026-05-11
- 为什么必读：这里支撑 scaling law 的基本定义：性能与模型/数据/算力规模存在可拟合趋势。
- 原文短摘：
  > The loss scales as a power-law with model size, dataset size, and the amount of compute used for training
- 中文概括：
  - 论文研究语言模型 loss 如何随参数量、数据量和计算量变化。
  - 它强调 scale 的影响大于许多具体架构形状细节。
- 我需要理解的机制：
  1. power-law scaling
  2. model size
  3. dataset size
  4. compute budget
- 支撑概念：
  - [[LLM Training Pipeline]]
  - scaling law
- 证据边界：
  - 这段说明预训练 loss 的规模趋势；不能推出产品质量、安全性或 Agent 能力只由参数规模决定。

#### 必读块 2：Abstract / compute budget allocation

- 位置：arXiv abstract / 2001.08361 / last checked 2026-05-11
- 为什么必读：这里解释为什么 scaling law 会影响训练策略：固定算力下要分配参数和数据。
- 原文短摘：
  > determine the optimal allocation of a fixed compute budget
- 中文概括：
  - 模型、数据和计算三者任一成为瓶颈都会限制 loss 改善。
  - 这为后续 Chinchilla/compute-optimal 论文提供了问题背景。
- 我需要理解的机制：
  1. compute allocation
  2. bottleneck analysis
  3. scaling tradeoff
- 支撑概念：
  - compute scaling
  - [[LLM Training Pipeline]]
- 证据边界：
  - 这不是部署成本最优，也不是后训练/对齐/工具使用的解释框架。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- Scaling law 解释的是 loss 还是真实产品可用性？
- 为什么后续 Chinchilla 会挑战早期“多堆参数”的训练直觉？

### 读完要更新

- [[LLM Training Pipeline]]
- scaling law
- compute scaling

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- scaling law
- compute scaling

## 我的疑问

- Scaling law 解释的是 loss 还是真实产品可用性？
- 为什么后续 Chinchilla 会挑战早期“多堆参数”的训练直觉？

## 边界提醒

Scaling 解释的是能力随规模增长的趋势，不等于数据质量、对齐、工具使用或产品 Agent 能力。
