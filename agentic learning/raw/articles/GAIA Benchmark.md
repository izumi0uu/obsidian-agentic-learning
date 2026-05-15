---
type: source
source_type: paper
title: "GAIA: a benchmark for General AI Assistants"
url: "https://arxiv.org/abs/2311.12983"
pdf: "../papers/assets/GAIA Benchmark.pdf"
extracted: "../papers/extracted/GAIA Benchmark.extracted.md"
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
source: "https://arxiv.org/abs/2311.12983"
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

- Abstract：抓住 GAIA 关注真实世界问题和 general AI assistant。
- 1 Introduction：理解为什么已有 LLM benchmark 容易饱和或不够真实。
- 3 GAIA：看 GAIA 是什么、怎么评分、问题怎么设计。
- 3.2 Evaluation：理解为什么短答案让自动评分更容易。
- 3.3 Composition：看任务需要哪些能力，例如 reasoning、multimodality、web browsing、tool use。
- 5 Discussion / Limitations：看 GAIA 不评估 trace 的边界。

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
