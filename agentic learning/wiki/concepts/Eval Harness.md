---
type: concept
topic:
  - evaluation
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[SWE-bench]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Agent Harness]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Trace]]"
  - "[[Task Success Rate]]"
---

# Eval Harness

## 一句话

Eval Harness 是自动运行任务、记录过程、收集输出、打分并复现失败的评测外壳。

## 它解决什么问题

Agent demo 成功一次不代表系统可靠。Eval Harness 让同一批任务能被重复运行，帮助比较不同模型、prompt、工具、检索策略和代码版本。

它通常包括数据集、执行器、工具环境、评分器、trace、结果存储和报告。

## 它不是什么

Eval Harness 不是单个 benchmark。

Benchmark 是任务集合或分数标准；Eval Harness 是把任务跑起来并能复现、比较、分析失败的系统。

## 现代性状态

Eval Harness 属于 current-practice。

现代 agent 系统通常把它做成 CI 里的评测流水线：固定数据集、固定版本的模型/提示词/工具环境、可回放 trace、可版本化评分器和失败归因。概念本身稳定，具体实现会随平台与工作流变化。

## 最小例子

代码 Agent 的 eval harness：

- 给定一个 GitHub issue 和 repo snapshot。
- 让 Agent 修改代码。
- 应用 patch。
- 跑测试。
- 保存 trace、diff、日志、回放所需状态和最终评分。

## 常见误解 / 风险

- 只看最终分数会丢掉失败原因。
- 只用 LLM-as-judge 评分会引入裁判偏差。
- 测试集太少会让 prompt 过拟合。
- 评测环境和生产环境差太远时，分数会虚高。

## 边界细节

- Eval Harness 负责“跑、记、比、复现”，不只是出一个分数。
- Benchmark 负责定义任务和标准；Harness 负责执行、记录和回放。
- 对 agent 任务，最好同时保存数据集版本、工具版本、种子、trace、patch、judge 输出和失败归因。
- 只保存最终得分，通常不足以定位回归。

## 现代系统怎么吸收它的价值

- 把 eval 绑进 CI/CD 或模型发布门禁。
- 对失败样本做 replay 和 regression tracking。
- 用版本化 judge prompt / rubric 降低评分漂移。
- 将 harness 输出接到 observability 面板里，而不是只看排行榜。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[OpenAI Agents SDK 文档]]
- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent Harness]]
- [[Evaluation]]
- [[Trace]]
- [[Replay]]
- [[Trajectory Evaluation]]
