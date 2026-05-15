---
type: source
source_type: paper
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
url: "https://arxiv.org/abs/2501.12948"
pdf: "assets/DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.pdf"
extracted: "extracted/DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.extracted.md"
author:
  - DeepSeek-AI
site: arXiv
topic:
  - llm
  - reasoning
  - training
created: 2026-05-09
updated: 2026-05-15
last_checked: 2026-05-11
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2501.12948"
related:
  - "[[LLM Training Pipeline]]"
  - "[[Reasoning Trace]]"
  - "[[Evaluation]]"
  - "[[Zero-shot CoT]]"
---

# DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

## 为什么收

这篇适合理解现代 reasoning model 为什么不只是“会补全文本”，还会通过强化学习和可验证任务信号训练更长的推理、检查和修正行为。

## 一句话

DeepSeek-R1 探索用强化学习激发 LLM 的推理能力，尤其是数学、代码和可验证问题上的多步推理。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| R1 路线强调用强化学习激发 LLM reasoning capability。 | arXiv abstract | high | [[LLM Training Pipeline]] |
| 论文观察到 self-reflection、verification、long CoT 等 reasoning pattern。 | arXiv abstract | medium | [[Reasoning Trace]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- frontier / volatile：R1 属于 2025 reasoning model/post-training 路线，工程实现仍快速变化。
- 稳定部分：可验证奖励和强化学习能塑造某些推理行为。
- 易变部分：具体训练配方、模型透明 thought process、benchmark 领先性会被新模型快速刷新。
- freshness：watch；需要和最新 reasoning model/评测分开追踪。

## 需要我读的内容

目标：理解 R1 的贡献是训练/强化学习路线，而不是一个普通 CoT prompt 模板。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / pure RL 激发 reasoning

- 位置：arXiv abstract / 2501.12948 / last checked 2026-05-11
- 为什么必读：这里支撑 R1-Zero / R1 的核心 claim：reasoning 能力可以通过 RL 被显著激发。
- 原文短摘：
  > reasoning abilities of LLMs can be incentivized through pure reinforcement learning
- 中文概括：
  - 论文把重点放在 post-training/RL，而不是 prompt 中手写 “think step by step”。
  - R1-Zero 展示了在没有冷启动 SFT 的情况下，RL 也能诱发较强 reasoning pattern。
- 我需要理解的机制：
  1. reinforcement learning for reasoning
  2. R1-Zero
  3. post-training
- 支撑概念：
  - [[LLM Training Pipeline]]
  - [[Reasoning Trace]]
  - verifiable reward
- 证据边界：
  - 这段证明的是训练信号对 reasoning behavior 的影响；不能推出所有任务都适合纯 RL，也不能等同于 Agent runtime。

#### 必读块 2：Abstract / 自我反思、验证与策略调整

- 位置：arXiv abstract / 2501.12948 / last checked 2026-05-11
- 为什么必读：这里连接 R1 与 CoT/Reflexion 脉络：模型行为中出现更长的检查和调整。
- 原文短摘：
  > self-reflection, verification, and dynamic strategy adaptation
- 中文概括：
  - R1 的 reasoning 不只是答案前多写几步，而是包含验证、反思和动态策略调整等行为模式。
  - 正式 R1 又通过冷启动、多阶段训练和蒸馏改善可读性与性能。
- 我需要理解的机制：
  1. self-reflection
  2. verification
  3. distillation of reasoning behavior
- 支撑概念：
  - [[Reasoning Trace]]
  - [[Zero-shot CoT]]
  - [[Evaluation]]
- 证据边界：
  - 论文中的 reasoning trace 是训练/推理行为证据；产品是否展示完整思维链还受安全、隐私和用户体验约束。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- 为什么 R1 不是 Zero-shot CoT prompt 的简单升级？
- 可验证 reward 能覆盖哪些任务，又覆盖不了哪些开放式任务？

### 读完要更新

- [[LLM Training Pipeline]]
- [[Reasoning Trace]]
- verifiable reward
- [[Zero-shot CoT]]
- [[Evaluation]]

## 已提取文件

- PDF：`assets/DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.pdf`
- Extracted Markdown：`extracted/DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[LLM Training Pipeline]]
- reasoning reinforcement learning
- verifiable reward

## 我的疑问

- 为什么 R1 不是 Zero-shot CoT prompt 的简单升级？
- 可验证 reward 能覆盖哪些任务，又覆盖不了哪些开放式任务？

## 边界提醒

推理强化能增强多步问题能力，但不等于 Agent runtime。模型仍需要工具、状态、权限和 trace 才能可靠行动。

## R1-Lite-Preview 时间线补充

DeepSeek 官方 API Docs 记录：DeepSeek-R1-Lite-Preview 在 2024-11-20 发布，定位为 o1-preview 级别的 reasoning model，强调 AIME / MATH benchmark 表现、实时透明 thought process，以及 “Longer Reasoning, Better Performance” 的 inference scaling 现象。

边界：R1-Lite-Preview 从用户视角很像“模型自己在写很长的 CoT”，但这不等于经典 [[Zero-shot CoT]] prompting。Zero-shot CoT 是用户在 prompt 里加“让我们一步步思考”来触发推理文本；R1 / R1-Lite 这类 reasoning model 则更接近把长推理、验证、反思和策略调整训练进模型行为，再在推理时用更多 token 展开。

## R1 正式版补充

DeepSeek-R1 在 2025-01-20 正式发布；官方 release note 强调 large-scale RL in post-training、minimal labeled data 和 math/code/reasoning tasks on par with OpenAI-o1。arXiv 论文摘要也把重点放在通过强化学习激发 reasoning patterns，例如 self-reflection、verification 和 dynamic strategy adaptation。

## 与 CoT 论文脉络的关系

DeepSeek-R1 属于 CoT / reasoning research 的后续工程化和训练化路线，而不是简单的 Zero-shot CoT prompt 复用。

- CoT / Zero-shot CoT 提供了“显式中间推理有助于复杂问题”的基础观察。
- R1-Zero / R1 关注的是如何通过 RL 和多阶段训练，让模型自然产生更长、更可验证、带自我检查的 reasoning behavior。

所以在复习时可以说：R1 参考并继承了 CoT 这条研究脉络，但它的关键贡献是训练方法，不是 prompt 模板。
