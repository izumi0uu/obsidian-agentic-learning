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

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / real-world software engineering testbed

- 位置：extracted Page 1 / Abstract
- 为什么必读：确认 SWE-bench 的评估对象是现实软件工程任务，而不是孤立函数补全。
- 原文短摘：
  > We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models.
- 中文概括：
  - SWE-bench 把代码模型评估移到真实软件工程问题上。
  - 学习重点是 repo、issue、patch、tests 共同构成的任务环境。
- 我需要理解的机制：
  1. 为什么真实 repo 比 toy coding benchmark 更难。
  2. 任务是否要求执行环境和上下文检索。
  3. 它评估的是代码生成、coding agent，还是完整 harness。
- 支撑概念:
  - [[Coding Agent]]
  - [[Evaluation]]
  - [[Repo Context]]
- 证据边界：
  - 这条短摘只证明作者的 benchmark 目标；真实工程可靠性仍不能直接由分数替代。

#### 必读块 2：Abstract / 2294 GitHub issues and PRs

- 位置：extracted Page 1 / Abstract
- 为什么必读：看任务实例来自真实 GitHub issues 和 PR，而不是人工合成的单函数题。
- 原文短摘：
  > SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories.
- 中文概括：
  - 这条证据支撑 SWE-bench 的数据来源和规模。
  - 后续引用具体数量时要注明版本和 repository 范围。
- 我需要理解的机制：
  1. issue / PR 如何连接成一个任务。
  2. 12 个 Python repository 是否代表所有软件工程场景。
  3. benchmark construction 如何过滤噪音。
- 支撑概念:
  - [[Benchmark]]
  - [[Repo Context]]
  - [[Patch Validation]]
- 证据边界：
  - 这条短摘不证明 benchmark 没有数据噪音；construction 和 filtering 要读正文。

#### 必读块 3：Abstract / codebase + issue -> patch

- 位置：extracted Page 1 / Abstract
- 为什么必读：这是 [[Coding Agent]] 任务形式的最小定义。
- 原文短摘：
  > Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue.
- 中文概括：
  - SWE-bench 的输出不是一句解释，而是对代码库的 patch。
  - 这支撑 [[Patch Validation]] 和 [[Repo Context]] 的概念边界。
- 我需要理解的机制：
  1. 输入中 issue 描述和代码库快照如何提供。
  2. patch 输出如何被应用。
  3. 测试如何判断 issue 是否真的解决。
- 支撑概念:
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Repo Context]]
- 证据边界：
  - 这条短摘定义任务形态；不说明 agent 的过程质量、搜索策略或 trace 是否可靠。

#### 必读块 4：Abstract / early model performance boundary

- 位置：extracted Page 1 / Abstract
- 为什么必读：理解为什么 SWE-bench 曾经暴露出 frontier coding model 的巨大缺口。
- 原文短摘：
  > The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues.
- 中文概括：
  - 这条结果说明当时模型在真实软件工程任务上只能解决很小比例的问题。
  - 今天引用时必须加历史版本边界，不能把 1.96% 当成当前模型水平。
- 我需要理解的机制：
  1. 结果依赖模型版本、检索上下文和评估设置。
  2. 为什么通过率是任务成功信号但不是过程质量信号。
  3. 后续 SWE-bench Verified / AgentLens 等工作如何补充边界。
- 支撑概念:
  - [[Task Success Rate]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 1.96% 是 ICLR 2024 论文摘要中的历史结果；不能代表当前 coding agents。

### 选读

- Figure 1：看 issue -> codebase -> generated PR -> tests 的流程。
- SWE-bench Lite / Verified：理解为什么需要轻量版和更严格子集。
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

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| SWE-bench 用真实软件工程作为下一代语言模型评估 testbed。 | extracted Page 1 / Abstract | high | [[Coding Agent]] |
| SWE-bench 由 2,294 个真实 GitHub issue / PR 构成，覆盖 12 个 Python repo。 | extracted Page 1 / Abstract | high | [[Benchmark]] |
| 任务输入是 codebase + issue description，输出是修改代码库的 patch。 | extracted Page 1 / Abstract | high | [[Patch Validation]] |
| Claude 2 在论文设置下解决 1.96% issues，说明当时真实 repo 修复仍很难。 | extracted Page 1 / Abstract | medium | [[Task Success Rate]] |

边界：这些 claim 来自 ICLR 2024 论文 Abstract；当前模型水平、SWE-bench Verified 子集和过程质量评估需要看后续资料。

## 方法 / 机制

- 核心方法：从真实 GitHub issues 和对应 PR 构造可执行评估任务，让模型生成 patch 并用测试验证。
- 输入 / 输出：输入是 issue 描述与代码库快照；输出是可应用到 repo 的 patch。
- 关键步骤：
  1. 收集 issue / PR / tests 并过滤任务。
  2. 给模型提供 issue 与 repo context。
  3. 应用生成 patch，并用 repository tests 判断是否解决。
- 和相邻方法的差别：SWE-bench 不是函数级代码生成 benchmark；它更接近 coding agent / harness 评估，但仍主要看最终 patch 是否通过测试。

## 实验 / 证据

- 数据集 / benchmark：2,294 problems, 12 popular Python repositories；后续还有 SWE-bench Lite / Verified 等变体。
- 指标：最终 patch 是否通过与 issue 相关的测试；具体 fail-to-pass / pass-to-pass 设置要读正文。
- 关键结果：论文摘要报告 Claude 2 solve 1.96% issues，这是历史设置下的能力缺口证据。
- 作者给出的局限：测试通过不等于过程可靠；需要结合后续 [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation]] 等过程评估资料。

## 现代性 / 前沿性初判

- 判定：current-practice / foundation benchmark for coding agents。
- 今天仍然稳定的部分：真实 repo + issue + patch + tests 仍是 coding agent 评估的核心范式。
- 已被现代系统吸收或替代的部分：现代评估会使用 SWE-bench Verified、过程 trace、成本、重试和人工复核等附加信号。
- 需要 freshness 复查的部分：leaderboard、Verified 子集、是否有数据污染或 benchmark gaming 讨论。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor。

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
