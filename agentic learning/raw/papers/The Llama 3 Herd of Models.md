---
type: source
source_type: paper
title: "The Llama 3 Herd of Models"
url: "https://arxiv.org/abs/2407.21783"
pdf: "assets/The Llama 3 Herd of Models.pdf"
extracted: "extracted/The Llama 3 Herd of Models.extracted.md"
author:
  - Dubey et al.
site: arXiv
topic:
  - llm
  - training
created: 2026-05-09
updated: 2026-05-15
last_checked: 2026-05-11
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2407.21783"
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


## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Llama 3 把多语言、代码、推理和工具使用纳入模型家族能力目标。 | arXiv abstract | high | [[LLM Training Pipeline]] |
| 论文覆盖 405B 模型的预训练和后训练版本。 | arXiv abstract | high | post-training |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。


## 现代性 / 前沿性初判

- current-practice / watch：Llama 3 是现代开放权重模型训练流水线案例，但具体模型已可能被后续版本替代。
- 稳定部分：数据治理、后训练、安全和评测是现代模型交付的基本组成。
- 易变部分：benchmark 排名、具体模型能力和许可/产品生态会更新。
- freshness：watch。

## 需要我读的内容

目标：理解 Llama 3 是现代开放模型训练流水线案例，而不是单一算法论文。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / model family capability scope

- 位置：arXiv abstract / 2407.21783 / last checked 2026-05-11
- 为什么必读：这里说明 Llama 3 覆盖的能力范围：多语言、代码、推理和工具使用都进入模型家族目标。
- 原文短摘：
  > natively support multilinguality, coding, reasoning, and tool usage.
- 中文概括：
  - Llama 3 不是只报告一个预训练 loss，而是描述一个覆盖多任务能力的模型家族。
  - 这适合作为 [[LLM Training Pipeline]] 从数据、训练、后训练到评测的综合案例。
- 我需要理解的机制：
  1. model family
  2. capability coverage
  3. tool-use post-training
- 支撑概念：
  - [[LLM Training Pipeline]]
  - [[Evaluation]]
  - [[Tool Use]]
- 证据边界：
  - 模型“支持工具使用”不等于有完整 Agent runtime；工具执行、权限和 trace 仍在系统层。

#### 必读块 2：Paper overview / pre-training 与 post-training

- 位置：arXiv abstract / 2407.21783 / last checked 2026-05-11
- 为什么必读：这里帮助把 Llama 3 放进训练流水线，而不是只看 benchmark 分数。
- 原文短摘：
  > pre-trained and post-trained versions of the 405B parameter language model
- 中文概括：
  - 论文同时描述预训练版本和后训练版本，说明现代 LLM 不是一次训练结束。
  - 数据治理、安全、指令跟随、工具使用和评测都属于模型家族交付的一部分。
- 我需要理解的机制：
  1. pre-training
  2. post-training
  3. safety/evaluation pipeline
- 支撑概念：
  - post-training
  - synthetic data
  - [[Evaluation]]
- 证据边界：
  - Llama 3 是具体模型家族报告，结论受 Meta 数据、算力、模型尺寸和开放策略限制。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- 为什么模型家族报告比单一算法论文更适合看训练流水线？
- 训练出 tool-use 能力和产品 Agent 使用工具之间差了哪些 runtime 层？

### 读完要更新

- [[LLM Training Pipeline]]
- [[Evaluation]]
- [[Tool Use]]
- post-training
- synthetic data

## 已提取文件

- PDF：`assets/The Llama 3 Herd of Models.pdf`
- Extracted Markdown：`extracted/The Llama 3 Herd of Models.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- data curation
- post-training
- synthetic data

## 我的疑问

- 为什么模型家族报告比单一算法论文更适合看训练流水线？
- 训练出 tool-use 能力和产品 Agent 使用工具之间差了哪些 runtime 层？

## 边界提醒

模型训练流水线和产品 Agent runtime 仍是两层。训练能提升模型适配框架的能力，但不能替代工具执行、权限和审计。
