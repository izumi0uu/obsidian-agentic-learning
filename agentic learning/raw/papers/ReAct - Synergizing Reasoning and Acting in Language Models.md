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
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: growing
source: "https://arxiv.org/abs/2210.03629"
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

目标：理解 ReAct 的核心是 interleaved reasoning/action/observation，而不是“把思维链展示出来”。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / reasoning traces 与 actions 交错生成

- 位置：Extracted Markdown `ReAct - Synergizing Reasoning and Acting in Language Models.extracted.md` / Page 1 / Abstract
- 为什么必读：这里是 ReAct 的核心定义：reasoning 和 acting 不是两个独立模块，而是交错发生。
- 原文短摘：
  > generate both reasoning traces and task-specific actions in an interleaved manner
- 中文概括：
  - ReAct 把语言推理轨迹和具体动作放进同一个循环。
  - 推理用于跟踪计划、处理异常、更新行动；动作让模型从外部工具或环境获得信息。
- 我需要理解的机制：
  1. Thought / Action / Observation loop
  2. reasoning trace
  3. task-specific action
- 支撑概念：
  - [[ReAct]]
  - [[Agent Loop]]
  - [[Reasoning Trace]]
- 证据边界：
  - 这段证明 ReAct 的范式；不能推出生产系统应该展示完整 reasoning trace。

#### 必读块 2：Abstract / 外部信息和 hallucination

- 位置：Extracted Markdown `ReAct - Synergizing Reasoning and Acting in Language Models.extracted.md` / Page 1 / Abstract
- 为什么必读：这里说明 action 的价值：不仅是执行动作，也能通过外部信息减少错误传播。
- 原文短摘：
  > actions allow it to interface with and gather additional information from external sources
- 中文概括：
  - 在 QA/fact verification 中，ReAct 可通过 Wikipedia API 查询事实。
  - Observation 进入后续上下文，使模型能根据外部结果修正后续推理或行动。
- 我需要理解的机制：
  1. external source access
  2. observation feedback
  3. error propagation control
- 支撑概念：
  - [[Observation]]
  - [[Tool Calling]]
  - [[Trace]]
- 证据边界：
  - 论文中的简单 API/环境反馈不等于现代工具权限系统；真实系统还需要 schema、auth、sandbox、trace 和 human-in-the-loop。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- ReAct 与 Toolformer 的工具使用边界是什么？
- Observation 为什么必须写回上下文或状态？

### 读完要更新

- [[ReAct]]
- [[Agent Loop]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Tool Calling]]
- [[Trace]]

## 一句话

ReAct 让模型交替进行推理和行动，通过外部环境反馈修正后续步骤。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| ReAct 让模型交错生成 reasoning traces 和 task-specific actions。 | Page 1 / Abstract | high | [[ReAct]] |
| 外部 actions 可帮助模型获取额外信息并缓解 hallucination/error propagation。 | Page 1 / Abstract | high | [[Observation]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- foundation / transitional：ReAct 是 Agent loop 语言和工具交互思想的地基；裸 ReAct prompt loop 在现代系统中常被框架吸收。
- 稳定部分：reasoning/action/observation 交替仍是理解工具型 Agent 的核心。
- 已被吸收部分：现代框架把 action execution、tool schema、state、trace、guardrails 外置。
- freshness：stable。

## 已提取文件

- PDF：`assets/ReAct - Synergizing Reasoning and Acting in Language Models.pdf`
- Extracted Markdown：`extracted/ReAct - Synergizing Reasoning and Acting in Language Models.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 抽取质量提醒

这份 PDF 的字体编码导致抽取正文出现大量 `(cid:)` 噪声。概念 ingest 只依赖可读的 Abstract、Introduction 和高层结构，不依赖抽取文本中的图例或细节表格。

## Ingest 摘要

这篇论文对当前学习的价值，是把 [[Agent Loop]] 里的“想”和“做”连起来：模型不是先完整想完再行动，而是在 [[Reasoning Trace]]、Action 和 [[Observation]] 之间循环。

核心主张：

- 只推理容易幻觉和错误传播。
- 只行动缺少可解释的计划和状态跟踪。
- [[ReAct]] 让 reasoning 和 acting 交替出现。
- 外部环境或工具返回的 observation 会改变后续推理。

## 图片录入：ReAct Tools / LLM / Environment

来源：用户提供截图，2026-05-10。原始图片保存为 `agentic learning/raw/assets/reAct.png`。由于原图是透明背景 PNG，已生成白底可见版本：`agentic learning/raw/assets/reAct-white-bg.png`。

为了让 LLM 和 Obsidian 更容易理解图中工程含义，已按 [[Reflexion]] 图的风格重绘为本地 SVG：`agentic learning/raw/assets/react-agent-loop.svg`。

![[react-agent-loop.svg]]

### 图中元素

- Tools：Agent 可以调用的外部能力，例如搜索、数据库、代码执行、浏览器或业务 API。
- LLM：根据上下文、工具结果和任务目标生成下一步 reasoning / action。
- Environment：动作发生的外部世界，例如网页、文件系统、测试环境、用户或业务系统。
- Agent Harness / Runtime：不在原始三盒图里，但是真正负责循环控制、工具执行、状态写回和停止条件的工程层。
- Action：模型提出的下一步动作，通常会被结构化为 tool call 或环境操作。
- Observation：工具或环境返回的结果，会进入上下文、[[Agent State]] 或 [[Trace]]。
- Trajectory / Trace：记录这次任务路径，便于调试、评估和重放。

### 图中流程

```text
LLM -> Action -> Tools / Environment -> Observation -> Context / State -> LLM
```

### 边界理解

这张图不是 ReAct 论文原图，而是用户截图的工程化重绘。它强调：ReAct 的 loop 不是 LLM 自己在内部完成的，而是由外部 runtime 执行 action、接收 observation、再把 observation 写回下一轮上下文。

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
