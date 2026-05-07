---
type: source
source_type: paper
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
url: "https://arxiv.org/abs/2302.04761"
pdf: "assets/Toolformer.pdf"
extracted: "extracted/Toolformer.extracted.md"
author:
  - Schick et al.
site: arXiv
topic:
  - llm
  - tool-use
created: 2026-05-05
updated: 2026-05-07
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: growing
source:
related:
  - "[[Tool Calling]]"
  - "[[LLM]]"
  - "[[Tool Use]]"
---

# Toolformer

## 为什么收

Toolformer 帮我理解“模型调用工具”不是简单拼 prompt，而是可以被训练和评估的一种能力。

## 先读什么

- Abstract
- Introduction
- Tool Use Examples

## 需要我读的内容

目标：理解 [[Tool Use]] 如何从“外部工程接口”变成一种模型可学习的能力。

### 必读

- Abstract：抓住模型可以学习调用工具的主张。
- 1 Introduction：理解普通 LLM 的限制：计算、实时信息、外部交互。
- Figure 1：看工具调用在文本中如何出现。
- 2 Approach：只理解候选 API call 生成、执行、筛选、微调这条链路。
- Tools/API 列表：看它使用了哪些工具类型。
- Limitations / Conclusion：看 Toolformer 没有解决什么。

### 选读

- Tool use examples：看模型什么时候调用 calculator、search、calendar 等工具。
- Ablation：看禁用 API call 后性能变化。

### 可以先跳过

- 具体训练数据过滤公式。
- 所有实验表格。
- 多语言 QA 细节。

### 读完要能回答

- [[Tool Use]] 和 [[Tool Calling]] 的区别是什么？
- 模型为什么需要学会“什么时候不用工具”？
- 会调用 API 为什么不等于 [[Agent]]？
- 工具调用结果为什么需要权限和验证？
- Toolformer 和 ReAct 的工具使用方式有什么不同？

### 读完要更新

- [[Tool Use]]
- [[Tool Calling]]
- [[LLM]]
- [[Agent]]

## 一句话

Toolformer 探索让语言模型学习何时、如何调用外部工具来增强自身能力。

## 已提取文件

- PDF：`assets/Toolformer.pdf`
- 抽取正文：`extracted/Toolformer.extracted.md`

## Ingest 摘要

这篇论文对当前学习的价值，是把 [[Tool Calling]] 从“工程接口”推进到“模型能力”：模型需要学会什么时候调用工具、传什么参数、如何使用工具结果。

核心主张：

- 工具调用可以被表示为文本中的 API call。
- 模型可以从少量示例生成候选调用，再通过筛选构造训练数据。
- 工具使用能增强问答、计算、翻译、日历等能力。
- 会用工具不等于具备完整 [[Agent]] 能力。

## 可以拆成概念卡

- [[Tool Calling]]
- [[Tool Use]]
- API call
- self-supervised learning

## 我的疑问

- Tool use 能力和 Agent 自主性之间是什么关系？
- 哪些工具应该由模型自由调用，哪些必须人类确认？

## 边界提醒

会使用工具不等于能可靠完成端到端任务。
