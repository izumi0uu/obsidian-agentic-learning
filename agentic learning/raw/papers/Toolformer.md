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
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: growing
source: "https://arxiv.org/abs/2302.04761"
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

目标：理解 Toolformer 把工具调用视为可训练的模型能力，同时仍不同于完整 Agent。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / 模型自教工具使用

- 位置：Extracted Markdown `Toolformer.extracted.md` / Page 1 / Abstract
- 为什么必读：这里支撑 Toolformer 的核心贡献：工具调用可以被构造成自监督训练数据。
- 原文短摘：
  > LMs can teach themselves to use external tools via simple APIs
- 中文概括：
  - Toolformer 从少量 API 示例出发，让模型生成、执行、筛选 API call，再用保留下来的调用微调模型。
  - 这把工具使用从纯工程接口推进为模型可学习的行为模式。
- 我需要理解的机制：
  1. self-supervised API call generation
  2. tool execution
  3. API-call filtering
- 支撑概念：
  - [[Tool Use]]
  - [[Tool Calling]]
  - [[LLM]]
- 证据边界：
  - 这段证明工具调用可训练；不能推出模型可以绕过权限或自主完成任意端到端任务。

#### 必读块 2：Abstract / 何时、如何调用 API

- 位置：Extracted Markdown `Toolformer.extracted.md` / Page 1 / Abstract
- 为什么必读：这里说明 Toolformer 不只是“能调用 API”，还学习调用时机、参数和结果整合。
- 原文短摘：
  > trained to decide which APIs to call
- 中文概括：
  - 工具使用能力包含三层判断：选哪个工具、何时调用、传什么参数。
  - 工具返回结果还需要被纳入后续 token prediction，而不是单独作为外部动作记录。
- 我需要理解的机制：
  1. tool selection
  2. argument generation
  3. result incorporation
- 支撑概念：
  - [[Tool Calling]]
  - [[Agent]]
- 证据边界：
  - 会选择和调用 API 不等于具备计划、状态、观察、权限、人类确认和恢复机制；这些仍属于 Agent harness。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- Toolformer 和 ReAct 都用工具，为什么一个偏训练、一个偏交互循环？
- 为什么“会调用工具”仍不等于 [[Agent]]？

### 读完要更新

- [[Tool Use]]
- [[Tool Calling]]
- [[LLM]]
- [[Agent]]

## 一句话

Toolformer 探索让语言模型学习何时、如何调用外部工具来增强自身能力。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Toolformer 用自监督方式训练模型使用外部工具。 | Page 1 / Abstract | high | [[Tool Use]] |
| 工具调用能力包括工具选择、调用时机、参数和结果整合。 | Page 1 / Abstract | high | [[Tool Calling]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- foundation / transitional：Toolformer 是工具使用可训练化的重要基础；现代 API tool calling 多由模型能力和外部 runtime 共同完成。
- 稳定部分：模型需要判断何时使用工具和如何整合结果。
- 已被吸收部分：现代 SDK 用 tool schema、function calling、sandbox、approval、trace 管理工具执行。
- freshness：stable。

## 已提取文件

- PDF：`assets/Toolformer.pdf`
- Extracted Markdown：`extracted/Toolformer.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

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
