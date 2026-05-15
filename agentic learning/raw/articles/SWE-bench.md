---
type: source
source_type: paper
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
url: "https://arxiv.org/abs/2310.06770"
pdf: "../papers/assets/SWE-bench.pdf"
extracted: "../papers/extracted/SWE-bench.extracted.md"
author:
  - Jimenez et al.
site: arXiv
topic:
  - agent
  - coding-agent
  - evaluation
created: 2026-05-05
updated: 2026-05-15
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: growing
source: "https://arxiv.org/abs/2310.06770"
related:
  - "[[Evaluation]]"
  - "[[Agent]]"
  - "[[Coding Agent]]"
  - "[[Patch Validation]]"
  - "[[Repo Context]]"
---

# SWE-bench

## 为什么收

SWE-bench 是理解代码 Agent 评估的重要资料。它从真实 GitHub issue 出发，检查模型是否能修改代码并通过测试。

## 先读什么

- Abstract
- Task setup
- Evaluation

## 需要我读的内容

目标：理解 [[Coding Agent]] 的评测为什么必须包含真实 repo、issue、patch 和测试。

### 必读

- Abstract：抓住真实 GitHub issue、codebase、patch、tests。
- 1 Introduction：理解为什么传统代码生成 benchmark 不够真实。
- 2 SWE-bench：看任务定义。
- 2.1 Benchmark Construction：理解 issue/PR/test 如何构成任务。
- 2.2 Task Formulation：重点看 input、patch output、evaluation metrics。
- 2.3 Features：理解 real-world software engineering、long inputs、robust evaluation。
- Conclusion / Limitations：看 benchmark 的边界。

### 选读

- Figure 1：看 issue -> codebase -> generated PR -> tests 的流程。
- SWE-bench Lite：理解为什么需要轻量版本。
- Retrieval 设置：看 repo context 怎么被提供。

### 可以先跳过

- 所有仓库分布统计表。
- 大量 appendix 示例 patch。
- 具体模型分数细节。

### 读完要能回答

- [[Coding Agent]] 和代码补全有什么区别？
- [[Repo Context]] 为什么不是把整个代码库塞进上下文？
- [[Patch Validation]] 为什么比“代码看起来对”更重要？
- SWE-bench 为什么天然需要 [[Agent Harness]]？
- 测试通过率和真实软件质量之间还有什么差距？

### 读完要更新

- [[Coding Agent]]
- [[Repo Context]]
- [[Patch Validation]]
- [[Agent Harness]]
- [[Evaluation]]

## 一句话

SWE-bench 用真实软件工程问题评估模型或 Agent 修改代码解决 issue 的能力。

## 已提取文件

- PDF：`../papers/assets/SWE-bench.pdf`
- Extracted Markdown：`../papers/extracted/SWE-bench.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

这篇论文对当前学习的价值，是把代码 Agent 的评估边界讲清楚：不是生成一个函数，而是在真实 repo 中理解 issue、修改代码、应用 patch、运行测试。

核心主张：

- SWE-bench 从真实 GitHub issue 和 PR 构造任务。
- 输入包括 issue 描述和完整代码库快照。
- 输出是 patch。
- 评估依赖测试是否通过，特别是 fail-to-pass 测试。
- 这类评估需要 [[Repo Context]]、[[Patch Validation]] 和执行环境，因此天然接近 [[Agent Harness]]。

## 可以拆成概念卡

- [[Evaluation]]
- [[Coding Agent]]
- [[Benchmark]]
- regression test
- real-world task
- [[Patch Validation]]
- [[Repo Context]]

## 我的疑问

- 代码 Agent 的能力应该看 patch 质量、测试通过率，还是问题理解能力？
- SWE-bench 和日常开发中的 Agent 体验差在哪里？

## 边界提醒

代码 Agent benchmark 的分数不能直接等于真实项目中的可靠性。
