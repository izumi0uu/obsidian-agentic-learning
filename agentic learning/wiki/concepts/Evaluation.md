---
type: concept
topic:
  - agent
  - evaluation
status: growing
created: 2026-05-05
updated: 2026-05-09
last_checked: 2026-05-09
freshness: stable
conflicts: []
source:
  - "[[GAIA Benchmark]]"
  - "[[SWE-bench]]"
evidence:
  - "[[GAIA Benchmark#为什么收]]"
  - "[[SWE-bench#为什么收]]"
related:
  - "[[LLM Training Pipeline]]"
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
---

# Evaluation

## 一句话

Evaluation 是用任务、样例、指标和人工判断来检查 Agent 是否稳定有效。

## 它解决什么问题

Agent 很容易在 demo 中看起来聪明，但在真实任务中不稳定。Evaluation 让我们发现失败模式，而不是只被一次成功吸引。

[[GAIA Benchmark]] 和 [[SWE-bench]] 都提醒我：Agent 评估应该尽量看任务是否端到端完成，而不是只看回答是否流畅。

## 它不是什么

Evaluation 不只是问模型“你觉得自己做得好吗”。

Evaluation 也不只是跑一个 benchmark。真实系统还需要业务样例、边界场景、回归测试和人工审查。

对 [[LLM Training Pipeline]] 来说，evaluation 不是训练结束后的展示环节，而是数据筛选、后训练、红队、安全策略、回归测试和产品迭代的闭环信号。

## 最小例子

如果我要评估一个 Obsidian 学习 Agent，可以准备这些测试：

- 它能否把新概念放进正确目录？
- 它能否给概念卡补充“它不是什么”？
- 它能否避免重复创建同义笔记？
- 它能否指出回答依据来自哪篇笔记？
- 它能否在不确定时提出问题？

## Benchmark 视角

- [[GAIA Benchmark]] 偏通用助手任务，关注真实世界问题、工具使用和短答案验证。
- [[SWE-bench]] 偏代码 Agent，关注真实 GitHub issue、patch 和测试验证。
- [[Task Success Rate]] 是重要指标，但不能解释为什么失败，也不能保证过程安全。

## 证据锚点

- Source: [[GAIA Benchmark]]
- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[LLM Training Pipeline]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[RAG]]
- [[Memory]]
- [[Benchmark]]
- [[Task Success Rate]]
