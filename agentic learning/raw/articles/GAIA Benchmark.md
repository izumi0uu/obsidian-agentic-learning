---
type: source
source_type: paper
title: "GAIA: a benchmark for General AI Assistants"
url: https://arxiv.org/abs/2311.12983
pdf: ../papers/assets/GAIA Benchmark.pdf
extracted: ../papers/extracted/GAIA Benchmark.extracted.md
author:
  - Mialon et al.
site: arXiv
topic:
  - agent
  - evaluation
  - benchmark
created: 2026-05-05
updated: 2026-05-15
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: growing
source: https://arxiv.org/abs/2311.12983
related:
  - "[[Evaluation]]"
  - "[[Agent]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
---

# GAIA Benchmark

## 为什么收

GAIA 是评估通用 AI assistant/agent 能力的重要 benchmark。它能帮助我理解“看起来会回答”和“能完成真实复杂任务”的差别。

## 先读什么

- Abstract
- Introduction
- Benchmark design
- Error analysis

## 需要我读的内容

目标：理解通用 AI assistant 的 [[Evaluation]] 为什么不能只测静态问答，而要测真实任务完成。

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / benchmark 定位

- 位置：extracted Page 1 / Abstract
- 为什么必读：确认 GAIA 评估的是 general AI assistant 的真实任务能力，而不是单纯语言流畅度。
- 原文短摘：
  > We introduce GAIA, a benchmark for General AI Assistants that, if solved, would represent a milestone in AI research.
- 中文概括：
  - GAIA 的入口 claim 是“通用 AI 助手 benchmark”，学习重点是 assistant system 能不能完成任务。
  - 这条证据只支撑 benchmark 目标定位；不能外推为 GAIA 已覆盖所有 Agent 能力。
- 我需要理解的机制：
  1. benchmark 评估对象是 assistant system 还是单体模型。
  2. “solved” 在 GAIA 中如何转化为可评分答案。
  3. 它和静态问答 benchmark 的边界差异。
- 支撑概念:
  - [[Evaluation]]
  - [[Benchmark]]
  - [[Task Success Rate]]
- 证据边界：
  - 这条短摘只证明作者的 benchmark 定位；具体任务构成、评分和局限还要读正文。

#### 必读块 2：Abstract / 能力组合

- 位置：extracted Page 1 / Abstract
- 为什么必读：GAIA 的学习价值在于把 reasoning、multimodality、web browsing 和 tool use 放进同一真实任务评估。
- 原文短摘：
  > GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency.
- 中文概括：
  - GAIA 不是只测知识回忆，而是要求多能力组合完成真实问题。
  - 对 Agent 学习来说，它支撑“工具使用 + 多步推理 + 真实环境”这一评估边界。
- 我需要理解的机制：
  1. 这些能力如何在单个任务中组合。
  2. 是否需要外部工具或网页环境。
  3. 最终答案如何避免变成开放式主观评分。
- 支撑概念:
  - [[Tool Use]]
  - [[Multimodal Agent]]
  - [[Task Success Rate]]
- 证据边界：
  - 这条短摘不证明 GAIA 评估 trace 质量；它只说明任务需要的能力类型。

#### 必读块 3：Abstract / 人类-模型差距

- 位置：extracted Page 1 / Abstract
- 为什么必读：理解为什么“对人简单、对 AI 难”是 GAIA 的核心设计哲学。
- 原文短摘：
  > GAIA questions are conceptually simple for humans yet challenging for most advanced AIs: we show that human respondents obtain 92% vs. 15% for GPT-4 equipped with plugins.
- 中文概括：
  - 这条数字说明 GAIA 的任务不是难倒人，而是暴露当前 AI assistant 在真实组合任务上的脆弱性。
  - 写入概念卡前必须回正文核对实验设置、插件条件、样本和评分方式。
- 我需要理解的机制：
  1. 为什么任务对人简单但对 AI 难。
  2. GPT-4 equipped with plugins 的设置边界。
  3. 这个差距能否代表通用 Agent 能力差距。
- 支撑概念:
  - [[Benchmark]]
  - [[Evaluation]]
  - [[Task Success Rate]]
- 证据边界：
  - 92% vs. 15% 是论文摘要中的实验结果线索；不能脱离版本、工具和数据集设置引用。

#### 必读块 4：Abstract / 466 questions 与 leaderboard

- 位置：extracted Page 1 / Abstract
- 为什么必读：看 GAIA 如何把真实任务压缩成可发布、可评分的 benchmark。
- 原文短摘：
  > Using GAIA’s methodology, we devise 466 questions and their answer.
- 中文概括：
  - 这条证据说明 GAIA 的 artifact 是一组带答案的问题，而不是开放式聊天评审。
  - 需要继续读 3 GAIA / Evaluation 才能判断题目构造、答案保留和 leaderboard 机制。
- 我需要理解的机制：
  1. 题目如何构造并避免训练集直查。
  2. 答案如何短化、标准化和自动评分。
  3. leaderboard 保留答案的边界。
- 支撑概念:
  - [[Benchmark]]
  - [[Evaluation]]
- 证据边界：
  - 这条只证明数据规模和发布形态；不能替代 benchmark design section。

### 选读

- Sample questions：挑 2-3 个感受任务形态。
- LLM results：只看人类和模型差距，不追具体分数。

### 可以先跳过

- 全部附录问题示例。
- 数据集构建细节。
- 每个模型的完整结果表。

### 读完要能回答

- [[GAIA Benchmark]] 评估的是模型，还是 assistant system？
- [[Task Success Rate]] 为什么比“回答流畅”更重要？
- 为什么 GAIA 对人简单、对 AI 难？
- 不评估 [[Trace]] 会漏掉什么？
- 我自己的学习 Agent 可以借鉴 GAIA 的哪些设计？

### 读完要更新

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Trace]]
- [[Agent Harness]]

## 一句话

GAIA 用需要推理、工具使用和多步处理的问题来评估通用 AI 助手能力。

## 已提取文件

- PDF：`../papers/assets/GAIA Benchmark.pdf`
- Extracted Markdown：`../papers/extracted/GAIA Benchmark.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

这篇论文对当前学习的价值，是把 [[Evaluation]] 从“问答正确率”推进到“真实助手任务能不能完成”。

核心主张：

- GAIA 设计真实世界问题，常需要推理、多步处理、网页浏览、文件处理或工具使用。
- 问题对人类相对简单，但对 AI assistant 很难。
- 它更关注最终短答案是否正确，而不是只测模型知识。
- 它也有边界：论文中提到当前 GAIA 不直接评估推理轨迹质量。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| GAIA 把 general AI assistant benchmark 定位为真实问题完成，而不是静态问答。 | extracted Page 1 / Abstract | high | [[Benchmark]] |
| GAIA 任务需要 reasoning、multimodality、web browsing 和 tool use 等能力组合。 | extracted Page 1 / Abstract | high | [[Evaluation]] |
| 摘要报告人类 92% vs GPT-4 with plugins 15%，用于说明任务对人简单但对 AI 难。 | extracted Page 1 / Abstract | medium | [[Task Success Rate]] |

边界：这些 claim 来自 Abstract / Page 1；具体评分、题目构造和不评估 trace 的边界需要回正文核对。

## 方法 / 机制

- 核心方法：用真实世界问题构造 assistant benchmark，并让答案尽量唯一、短、可验证。
- 输入 / 输出：输入是需要多步推理/工具/网页/多模态处理的问题；输出是可评分的短答案。
- 关键步骤：
  1. 设计概念上对人简单、但需要复杂行动序列的问题。
  2. 保留 ground-truth answer 以支持 leaderboard。
  3. 用任务成功而不是生成流畅度评价 assistant。
- 和相邻方法的差别：GAIA 更接近真实助手任务完成评估；它不是 trace-quality benchmark，也不是只测代码修复的 SWE benchmark。

## 实验 / 证据

- 数据集 / benchmark：466 questions and their answer；部分答案保留用于 leaderboard。
- 指标：最终答案正确性；正文需要进一步核对自动评分和 human/model evaluation 设置。
- 关键结果：摘要报告 human respondents 92% vs GPT-4 equipped with plugins 15%。
- 作者给出的局限：本页先记录 Abstract/Page 1；trace 质量、工具调用过程和任务覆盖范围要读 Discussion / Limitations。

## 现代性 / 前沿性初判

- 判定：current-practice / stable benchmark reference。
- 今天仍然稳定的部分：真实任务完成、短答案评分、多能力组合仍是 Agent evaluation 的重要设计边界。
- 已被现代系统吸收或替代的部分：现代 Agent benchmark 会进一步记录 trace、工具调用、成本和失败过程。
- 需要 freshness 复查的部分：leaderboard、数据版本、是否出现 GAIA 变体或污染讨论。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor。

## 可以拆成概念卡

- [[Evaluation]]
- [[Benchmark]]
- tool use evaluation
- real-world tasks
- [[Task Success Rate]]

## 我的疑问

- GAIA 评估的是模型能力，还是完整 Agent 系统能力？
- benchmark 和我自己的学习 Agent 测试集有什么区别？

## 边界提醒

benchmark 不是万能标准，它只代表一组任务设计。
