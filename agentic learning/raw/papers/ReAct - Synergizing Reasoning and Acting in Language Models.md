---
type: source
source_type: paper
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
url: "https://arxiv.org/abs/2210.03629"
pdf: "assets/ReAct - Synergizing Reasoning and Acting in Language Models.pdf"
extracted: "extracted/ReAct - Synergizing Reasoning and Acting in Language Models.extracted.md"
author:
  - Yao et al.
site: arXiv
topic:
  - agent
  - tool-use
  - reasoning
created: 2026-05-05
updated: 2026-05-07
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: growing
source:
related:
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[ReAct]]"
  - "[[Reasoning Trace]]"
  - "[[Observation]]"
---

# ReAct - Synergizing Reasoning and Acting in Language Models

## 为什么收

ReAct 是理解 Agent Loop 的关键论文之一。它把 reasoning traces 和 actions 放在同一个循环里，是很多工具型 Agent 的思想来源。

## 先读什么

- Abstract
- Introduction
- ReAct Prompting

## 需要我读的内容

目标：理解 [[Agent Loop]] 为什么要把 reasoning、action、[[Observation]] 放在一个循环里。

### 必读

- Abstract：抓住 interleaved reasoning and acting。
- 1 Introduction：理解人类任务中“想”和“做”为什么会交替出现。
- ReAct 方法段落：只看 Thought / Action / Observation 的结构。
- QA / fact verification 示例：看工具反馈如何减少 hallucination 和 error propagation。
- Interactive decision making 示例：看环境反馈如何改变后续行动。
- Conclusion：看 ReAct 的边界和适用场景。

### 选读

- HotpotQA / FEVER：偏知识问答，帮助理解工具查询。
- ALFWorld / WebShop：偏环境交互，帮助理解 Agent Loop。

### 可以先跳过

- ReAct 抽取文本里的图例页，因为这份 PDF 抽取有大量 `(cid:)` 噪声。
- 具体 benchmark 分数和表格。
- prompt 细节模板。

### 读完要能回答

- [[ReAct]] 和 [[Agent Loop]] 的关系是什么？
- [[Reasoning Trace]] 解决什么问题，又有什么风险？
- [[Observation]] 为什么会改变下一步行动？
- ReAct 为什么不是完整生产级 Agent？
- 真实产品里是否应该展示完整 reasoning trace？

### 读完要更新

- [[Agent Loop]]
- [[ReAct]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Trace]]
- [[Tool Calling]]

## 一句话

ReAct 让模型交替进行推理和行动，通过外部环境反馈修正后续步骤。

## 已提取文件

- PDF：`assets/ReAct - Synergizing Reasoning and Acting in Language Models.pdf`
- 抽取正文：`extracted/ReAct - Synergizing Reasoning and Acting in Language Models.extracted.md`

## 抽取质量提醒

这份 PDF 的字体编码导致抽取正文出现大量 `(cid:)` 噪声。概念 ingest 只依赖可读的 Abstract、Introduction 和高层结构，不依赖抽取文本中的图例或细节表格。

## Ingest 摘要

这篇论文对当前学习的价值，是把 [[Agent Loop]] 里的“想”和“做”连起来：模型不是先完整想完再行动，而是在 [[Reasoning Trace]]、Action 和 [[Observation]] 之间循环。

核心主张：

- 只推理容易幻觉和错误传播。
- 只行动缺少可解释的计划和状态跟踪。
- [[ReAct]] 让 reasoning 和 acting 交替出现。
- 外部环境或工具返回的 observation 会改变后续推理。

## 可以拆成概念卡

- [[Agent Loop]]
- [[Tool Calling]]
- [[ReAct]]
- [[Reasoning Trace]]
- acting
- [[Observation]]

## 我的疑问

- ReAct 的推理过程什么时候应该暴露，什么时候应该隐藏？
- 真实产品里的 Agent 是否还直接使用 ReAct 形式？

## 边界提醒

ReAct 是一种行动-反馈范式，不等于完整的生产级 Agent 系统。
