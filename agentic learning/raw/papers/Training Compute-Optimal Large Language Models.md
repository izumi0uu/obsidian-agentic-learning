---
type: source
source_type: paper
title: Training Compute-Optimal Large Language Models
url: https://arxiv.org/abs/2203.15556
pdf: assets/Training Compute-Optimal Large Language Models.pdf
extracted: extracted/Training Compute-Optimal Large Language Models.extracted.md
author:
  - Hoffmann et al.
site: arXiv
topic:
  - llm
  - training
created: 2026-05-09
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: seed
source: https://arxiv.org/abs/2203.15556
related:
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
---

# Training Compute-Optimal Large Language Models

## 为什么收

这篇通常被称为 Chinchilla，适合理解“只堆参数不够，数据 token 也要按计算预算匹配”的训练边界。

## 一句话

在固定训练计算量下，模型参数量和训练 token 数需要更平衡，模型才更 compute-optimal。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Chinchilla 强调训练 token 数和模型大小同等重要。 | arXiv abstract | high | compute-optimal training |
| 固定计算预算下，参数和 token 应共同扩展。 | arXiv abstract | high | data scaling |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- foundation：compute-optimal training 是理解现代 LLM 训练资源分配的基础。
- 稳定部分：数据量和质量不能被参数规模完全替代。
- 后续变化：不同数据质量、重复训练、多阶段训练和推理时计算会改变工程最优点。
- freshness：stable。

## 需要我读的内容

目标：理解 Chinchilla 如何修正早期 scaling 直觉：固定算力下参数和 token 要平衡。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / compute-optimal 问题

- 位置：arXiv abstract / 2203.15556 / last checked 2026-05-11
- 为什么必读：这里支撑 Chinchilla 的核心问题：给定训练计算预算时，模型多大、数据多少才合适。
- 原文短摘：
  > the optimal model size and number of tokens for training a transformer language model
- 中文概括：
  - 论文指出不能只扩大参数，训练 token 数同样重要。
  - 在固定 FLOPs 下，参数量和 token 数需要共同优化。
- 我需要理解的机制：
  1. compute budget
  2. training tokens
  3. model size
- 支撑概念：
  - compute-optimal training
  - data scaling
  - [[LLM Training Pipeline]]
- 证据边界：
  - 这段关注训练计算最优；不等于推理成本、服务延迟或产品收益最优。

#### 必读块 2：Abstract / Chinchilla 结论

- 位置：arXiv abstract / 2203.15556 / last checked 2026-05-11
- 为什么必读：这里解释为什么 Chinchilla 常被用来纠正“大模型少数据”的路线。
- 原文短摘：
  > model size and the number of training tokens should be scaled equally
- 中文概括：
  - Chinchilla 结论把资源分配从“主要堆参数”转向“参数和数据一起扩”。
  - 这影响后续大模型训练对高质量 token、数据去重和数据治理的重视。
- 我需要理解的机制：
  1. equal scaling
  2. data/parameter tradeoff
  3. compute-optimal frontier
- 支撑概念：
  - [[LLM Training Pipeline]]
  - scaling law
- 证据边界：
  - 等比例 scaling 是论文拟合条件下的训练建议；真实组织还会受数据版权、质量、推理成本和硬件限制。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- Chinchilla 为什么会让“多训练 token”变得和“堆参数”一样重要？
- compute-optimal 和产品部署最优为什么不是同一个目标？

### 读完要更新

- compute-optimal training
- data scaling
- [[LLM Training Pipeline]]
- scaling law

## 已提取文件

- PDF：`assets/Training Compute-Optimal Large Language Models.pdf`
- Extracted Markdown：`extracted/Training Compute-Optimal Large Language Models.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- compute-optimal training
- data scaling

## 我的疑问

- Chinchilla 为什么会让“多训练 token”变得和“堆参数”一样重要？
- compute-optimal 和产品部署最优为什么不是同一个目标？

## 边界提醒

Compute-optimal 不等于产品最优。真实系统还要看延迟、成本、上下文长度、工具能力和部署约束。
