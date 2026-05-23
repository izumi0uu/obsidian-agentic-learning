---
type: source
source_type: article
title: "AI Engineering From Scratch - Prompt Engineering"
url: https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/01-prompt-engineering
author: Rohit G.
site: aiengineeringfromscratch.com
topic:
  - llm
  - prompting
  - prompt-engineering
created: 2026-05-22
updated: 2026-05-22
last_checked: 2026-05-22
freshness: watch
status: seed
source:
related:
  - "[[Prompt Engineering]]"
  - "[[Prompt]]"
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[Context Engineering]]"
---

# AI Engineering From Scratch - Prompt Engineering

## 为什么收

这篇 lesson 对 [[Prompt Engineering]] 的学习价值在于：它用 vague prompt 与 engineered prompt 的对比说明，prompt 的具体程度会改变模型生成时被约束到的语义和格式空间。

这条来源适合作为一个边界提醒：文章里的“激活训练数据中的窄切片”可以作为工程直觉，但不应被理解成模型真的在推理时访问外部训练样本库。

## 一句话

细化后的 prompt 会把模型从宽泛的生成空间推向更窄、更相关、更可评估的条件分布；但这不是数据库检索，而是基于当前上下文的概率生成。

## 关键事实

- 文章用营销邮件例子区分 vague prompt 和 engineered prompt：后者增加角色、产品、受众、语气、长度、指标和 CTA 等约束。
- 文章把 role prompting 解释为让模型更偏向某类专业文本模式；角色描述越精确，候选输出分布越窄，但过度收窄或证据稀薄时会诱发幻觉。
- 文章把 instruction clarity 的核心问题说成减少歧义：每个模糊点都是模型需要猜测的分支。
- 从 [[LLM]] / [[Transformer]] 机制看，更精确的说法是：提示词细化改变 `P(next token | context)` 的条件上下文，让 self-attention 处理到更多任务、受众、格式和排除条件，而不是在权重外部打开一个训练样本库。
- 这条边界同时连接 [[Context Engineering]]：prompt 只是上下文窗口里的一部分，真正的生产质量还取决于放入窗口的信息是否有信号、可验证、可治理。

## 机制拆解（工程综合）

- 条件增加：更具体的 prompt 本质上给自回归生成增加上下文条件，使模型每一步预测下一个 token 时面对的条件更完整。
- 上下文参与：角色、领域、受众、格式、包含项和排除项都会作为 token 进入上下文，参与 Transformer 层内的表示计算与 attention 交互。
- 语义邻域偏移：专业词、场景词和受众词会把生成更偏向模型已学到的相关统计模式；这不是推理时检索训练样本，而是表示空间和概率分布的条件化。
- 输出空间约束：JSON、bullet 数量、字数、语气和禁止项会让很多候选 token 序列变得低概率、不合规或不符合任务。
- few-shot 与 role 提示：示例和角色描述可以在推理时形成临时任务定义；它们改变上下文，不更新模型参数，也不保证事实正确。
- 风险边界：当条件过窄、互相冲突、缺少真实证据，或指向模型缺乏可靠模式的专业身份时，细化 prompt 可能提升形式一致性，却降低事实可靠性。

## 可以拆成概念卡

- [[Prompt Engineering]]
- [[Prompt]]
- [[Context Engineering]]

## 我的疑问

- 什么时候提示词细化会变成过拟合 prompt、冲突约束或诱发幻觉？
- 提示词细化和 few-shot 示例选择之间，哪个更像在推理时定义任务分布？
- 在 Agent 场景里，哪些约束应该留在 prompt，哪些应该下沉到 tool schema、policy、eval harness 或 runtime？

## 边界提醒

本 note 不把提示词细化写成训练数据检索机制。更稳的表达是：prompt 通过增加条件，改变模型下一 token 的概率分布，并收窄合法输出空间。

这篇文章是教学材料，不是 Transformer 论文或模型内部机制论文。解释底层机制时仍应回到 [[LLM]]、[[Transformer]]、[[Attention Is All You Need]] 和相关模型原理论文。

## 外部链接

- Lesson: <https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/01-prompt-engineering>
- Source markdown: <https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/phases/11-llm-engineering/01-prompt-engineering/docs/en.md>
