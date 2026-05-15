---
type: source
source_type: paper
title: "Constitutional AI: Harmlessness from AI Feedback"
url: "https://arxiv.org/abs/2212.08073"
pdf: "assets/Constitutional AI - Harmlessness from AI Feedback.pdf"
extracted: "extracted/Constitutional AI - Harmlessness from AI Feedback.extracted.md"
author:
  - Bai et al.
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
source: "https://arxiv.org/abs/2212.08073"
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

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Constitutional AI 用原则替代大量逐条 harmlessness 人类标注。 | arXiv abstract | high | RLAIF |
| 方法包含监督学习阶段和强化学习阶段。 | arXiv abstract | high | [[LLM Training Pipeline]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- current-practice / foundation for alignment：RLAIF 已成为理解 AI feedback 对齐路线的重要基础。
- 稳定部分：原则、AI critique、偏好反馈可以减少某些人工标注依赖。
- 局限部分：原则集合、偏好模型和 RL 目标仍可能遗漏真实部署风险。
- freshness：stable；如跟踪 Anthropic 具体产品策略则另列 volatile source。

## 需要我读的内容

目标：理解 Constitutional AI 如何把原则、模型自评和 AI feedback 组合成训练/对齐流程。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / 监督式 AI feedback

- 位置：arXiv abstract / 2212.08073 / last checked 2026-05-11
- 为什么必读：这里支撑 Constitutional AI 的第一阶段：模型根据原则批评并修改自己的回答。
- 原文短摘：
  > The only human oversight is provided through a list of rules or principles, and so we refer to the method as Constitutional AI.
- 中文概括：
  - 论文强调人类不再逐条提供 harmlessness 标注，而是提供一组 constitution/principles。
  - 模型先生成回答，再按原则对回答做 critique/revision，形成可用于监督学习的数据。
- 我需要理解的机制：
  1. constitution / principles
  2. self-critique and revision
  3. supervised learning from AI feedback
- 支撑概念：
  - [[LLM Training Pipeline]]
  - RLAIF
  - AI feedback
- 证据边界：
  - 这段只说明训练数据生成和监督阶段的人工介入方式；不能推出系统上线后不需要人工审计或运行时 guardrails。

#### 必读块 2：Abstract / RLAIF 阶段

- 位置：arXiv abstract / 2212.08073 / last checked 2026-05-11
- 为什么必读：这里说明论文不只做自我修订，还用 AI preference feedback 进入 RL 阶段。
- 原文短摘：
  > The process involves both a supervised learning and a reinforcement learning phase.
- 中文概括：
  - Constitutional AI 把 AI 反馈扩展到偏好比较：模型按照原则判断两个回答哪个更符合 harmlessness。
  - 这些偏好可以训练 preference model，再用于 RL 训练助手。
- 我需要理解的机制：
  1. AI preference feedback
  2. preference model
  3. reinforcement learning from AI feedback
- 支撑概念：
  - RLAIF
  - alignment
  - [[LLM Training Pipeline]]
- 证据边界：
  - RLAIF 是训练层对齐方法，不等同于运行时 [[Guardrails]]；训练倾向不能替代权限边界和实时拦截。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- Constitutional AI 和 RLHF 的相同点与差别是什么？
- 为什么训练层 harmlessness 不等于运行时安全边界？

### 读完要更新

- [[LLM Training Pipeline]]
- RLAIF
- AI feedback
- alignment

## 已提取文件

- PDF：`assets/Constitutional AI - Harmlessness from AI Feedback.pdf`
- Extracted Markdown：`extracted/Constitutional AI - Harmlessness from AI Feedback.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- RLAIF
- AI feedback
- alignment

## 我的疑问

- Constitutional AI 和 RLHF 的相同点与差别是什么？
- 为什么训练层 harmlessness 不等于运行时安全边界？

## 边界提醒

Constitutional AI 是训练/对齐方法，不等于运行时 [[Guardrails]]。训练可以塑造倾向，运行时仍需要权限、审计和策略。
