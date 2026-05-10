---
type: concept
topic:
  - evaluation
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[GAIA Benchmark]]"
  - "[[SWE-bench]]"
evidence:
  - "[[GAIA Benchmark#为什么收]]"
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Task Success Rate]]"
---

# Benchmark

## 一句话

Benchmark 是用一组固定任务、运行协议和评分方式来比较系统能力的评测集合。

## 概念详解

Benchmark 解决的是“不要只相信演示”的问题。一个 demo 可能只展示最顺利的路径；benchmark 则把系统放到一组预先定义的任务里，用相对一致的输入、约束、评分规则和报告方式来比较能力。对 Agent 来说，benchmark 不应该只问答案像不像，还要尽量覆盖工具使用、检索、代码修改、环境交互和最终任务完成。

一个 benchmark 至少包含四层：任务集、运行环境、评分规则和报告口径。任务集决定测什么；运行环境决定模型或 Agent 能用哪些工具；评分规则决定怎么算成功；报告口径决定结果是否能和别人比较。[[GAIA Benchmark]] 更偏通用 assistant 复杂任务，[[SWE-bench]] 更偏真实 GitHub issue 的代码修复任务，两者都提醒我们：Agent 能力需要放进具体任务协议里看。

它与 evaluation harness 的关系是：benchmark 提供任务和指标，harness 负责批量运行、收集 trace、执行 checker、汇总分数和保存失败样本。没有 harness，benchmark 很容易停留在“读题打分”；没有 benchmark，harness 又缺少稳定的比较对象。


Agent benchmark 还要特别注意“环境协议”。同一个题目，如果一个系统允许联网、工具调用、长上下文、多人提示、人工修正或多次重试，另一个系统不允许，分数就不能直接比较。学习 benchmark 时，不能只记住榜单名字，而要追问任务分布、工具边界、评分 checker、污染风险和失败样本是否公开。

因此 benchmark 的学习重点不是背分数，而是学会读协议：任务来自哪里、是否接近真实需求、checker 是否可靠、运行预算是否公平、失败样本是否能解释。

## 它解决什么问题

没有 benchmark，Agent 很容易只靠 demo 给人“看起来很强”的感觉。Benchmark 让不同模型或系统可以在同一任务集上比较。

它还帮助团队发现能力边界：是工具调用弱、长任务规划弱、代码 patch 弱，还是只在某类任务上强。

## 它不是什么

Benchmark 不是现实世界能力的完整证明。

一个系统在 benchmark 上高分，不等于在你的真实任务中可靠。Benchmark 也可能被污染、被刷榜、过时或覆盖面不足。

Benchmark 也不是 [[Evaluation]] 的全部。Evaluation 还包括线上监控、回归测试、人工复盘、红队、安全评测、trajectory evaluation 和业务指标。

## 最小例子

GAIA 用真实助手问题评估通用 AI assistant；SWE-bench 用真实 GitHub issue 评估代码修改能力。

```text
benchmark = tasks + allowed tools/environment + scoring rule + report metric
```

如果一个 coding agent 在 100 个 issue 中修好 30 个，并且每个修复都通过对应测试，那么这组 benchmark 上的 task success rate 是 30%。

## 常见误解 / 风险

- 把榜单分数当成真实产品可靠性：真实任务分布、权限、数据和失败成本可能完全不同。
- 只看平均分：少数高风险失败可能比多数普通成功更重要。
- 忽略数据污染：模型可能在训练中见过 benchmark 题目或相似答案。
- 忽略运行协议：同一模型在不同工具、上下文、重试次数和人工帮助下分数不可直接比较。

## 边界细节

Agent benchmark 应该尽量评估任务完成，而不仅是文本答案好不好看。

边界可以分成三层：

1. Benchmark：固定任务和评分协议。
2. [[Eval Harness]]：运行 benchmark、收集 trace、执行 checker 和保存结果的工程系统。
3. [[Observability]] / [[Trace]]：帮助解释为什么某些任务失败，但不直接等于 benchmark 分数。

当 benchmark 用于复习时，要问：它测的是最终答案、任务完成、工具路径、安全性，还是过程质量？不同 benchmark 的答案不能混为一谈。

## 现代性状态

- 判定：foundation / current-practice。
- 为什么：固定任务集和统一评分是机器学习评测的基础方法；在 Agent 时代，它被扩展到工具使用、代码修改、浏览器操作和 trajectory 质量。
- 稳定部分：任务集、评分规则和可复现报告是 benchmark 的核心。
- 易变部分：具体榜单、数据集污染情况、工具协议、leaderboard 口径和模型排名会持续变化。

## 证据锚点

- Source: [[GAIA Benchmark]]
- Source: [[SWE-bench]]
- Anchor: [[GAIA Benchmark#为什么收]] / [[SWE-bench#为什么收]]
- Evidence type: benchmark source notes + evaluation engineering synthesis.
- Confidence: medium
- Boundary: 本卡沉淀 benchmark 的通用边界；具体榜单分数和最新 SOTA 需要按 source freshness 另行复查。

## 复习触发

- 为什么 benchmark 高分不等于真实任务可靠？
- Benchmark、[[Eval Harness]]、[[Task Success Rate]] 三者分别回答什么问题？
- 设计一个 Browser Agent benchmark 时，你会固定哪些变量？

## 相关链接

- [[Evaluation]]
- [[Task Success Rate]]
- [[GAIA Benchmark]]
- [[SWE-bench]]
