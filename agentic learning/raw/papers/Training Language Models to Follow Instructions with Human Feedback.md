---
type: source
source_type: paper
title: Training Language Models to Follow Instructions with Human Feedback
url: https://arxiv.org/abs/2203.02155
pdf: assets/Training Language Models to Follow Instructions with Human Feedback.pdf
extracted: extracted/Training Language Models to Follow Instructions with Human Feedback.extracted.md
author:
  - Ouyang et al.
site: arXiv
topic:
  - llm
  - training
  - alignment
created: 2026-05-09
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: seed
source: https://arxiv.org/abs/2203.02155
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

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 模型变大不自动让它更好地遵循用户意图。 | arXiv abstract | high | RLHF |
| InstructGPT 使用示范数据、偏好排序/reward model 和 PPO/RLHF。 | arXiv abstract | high | [[LLM Training Pipeline]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- foundation：RLHF 是现代助手模型后训练的重要基础。
- 稳定部分：示范、偏好、奖励模型是理解 instruction following 的核心语言。
- 局限部分：RLHF 可改善偏好一致性，但不能单独保证事实正确、透明推理或工具安全。
- freshness：stable。

## 需要我读的内容

目标：理解 InstructGPT/RLHF 如何把基础模型调整成更符合用户指令和偏好的助手。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / bigger is not enough

- 位置：arXiv abstract / 2203.02155 / last checked 2026-05-11
- 为什么必读：这里支撑 RLHF 的问题背景：扩大模型不自动等于更会遵循用户意图。
- 原文短摘：
  > Making language models bigger does not inherently make them better at following a user's intent.
- 中文概括：
  - 基础语言模型优化的是预测文本，不直接优化用户满意度、指令遵循或偏好一致。
  - InstructGPT 通过人类反馈把模型行为向 helpfulness、truthfulness、harmlessness 调整。
- 我需要理解的机制：
  1. instruction following gap
  2. human feedback
  3. assistant behavior alignment
- 支撑概念：
  - RLHF
  - instruction tuning
  - [[LLM Training Pipeline]]
- 证据边界：
  - 这段不说明 RLHF 能解决事实性、数学推理或工具安全的全部问题。

#### 必读块 2：Method / demonstrations + rankings + PPO

- 位置：arXiv abstract / 2203.02155 / last checked 2026-05-11
- 为什么必读：这里给出 RLHF 的经典三段式：SFT、reward model、强化学习。
- 原文短摘：
  > collect a dataset of labeler demonstrations of the desired model behavior
- 中文概括：
  - 先用标注者示范做 supervised fine-tuning。
  - 再收集模型输出排序训练 reward model，最后用 PPO 优化策略模型。
- 我需要理解的机制：
  1. supervised fine-tuning
  2. reward model
  3. PPO / RLHF
- 支撑概念：
  - reward model
  - RLHF
  - [[Evaluation]]
- 证据边界：
  - 标注者偏好不是绝对真理；reward model 可能被利用，且 RLHF 不等于完整安全系统。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- 为什么基础 LM 的 next-token objective 与“遵循指令”不是同一个目标？
- RLHF 的 reward model 可能带来哪些偏差或 reward hacking 风险？

### 读完要更新

- RLHF
- instruction tuning
- [[LLM Training Pipeline]]
- reward model
- [[Evaluation]]

## 已提取文件

- PDF：`assets/Training Language Models to Follow Instructions with Human Feedback.pdf`
- Extracted Markdown：`extracted/Training Language Models to Follow Instructions with Human Feedback.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- instruction tuning
- RLHF
- reward model

## 我的疑问

- 为什么基础 LM 的 next-token objective 与“遵循指令”不是同一个目标？
- RLHF 的 reward model 可能带来哪些偏差或 reward hacking 风险？

## 边界提醒

RLHF 改善有用性和偏好一致性，但不自动保证事实正确、推理最优或工具调用安全。
