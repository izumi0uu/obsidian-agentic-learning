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

## 常见误解 / 风险

- 只看总分会掩盖失败模式。
- 只做 benchmark 不等于完成 evaluation。
- 没有回归集时，改动后很难知道是变好还是变坏。

## 边界细节

- Evaluation 负责“看系统稳不稳”，不只是给一个分数。
- 对 Agent 来说，最好同时评 task success、过程质量、失败原因和安全边界。
- 真正可用的 evaluation 往往要把人工样例、自动指标和回归测试放在一起。

## 现代性状态

- 基础地基：evaluation 来自测试、实验设计和质量控制。
- 当前工程实践：Agent 评估通常会组合 benchmark、业务样例、回归集、judge 和人工审查。
- 前沿 / 易变：具体数据集、指标和平台会变化，尤其是围绕 agentic workflows 的评测方式。

## 现代系统怎么吸收它的价值

- 把 evaluation 接到 CI / 发布门禁里。
- 用回归集追踪变更影响。
- 把失败样本和原因沉淀到可复查的知识库里。

- [[GAIA Benchmark]] 偏通用助手任务，关注真实世界问题、工具使用和短答案验证。
- [[SWE-bench]] 偏代码 Agent，关注真实 GitHub issue、patch 和测试验证。
- [[Task Success Rate]] 是重要指标，但不能解释为什么失败，也不能保证过程安全。

## 证据锚点

- Source: [[GAIA Benchmark]]
- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 复习触发

- 为什么单个 benchmark 分数不足以代表 evaluation？
- 过程质量、任务完成和安全边界分别怎么评？
- 哪些失败需要进入回归集？

## 相关链接

- [[Agent]]
- [[LLM Training Pipeline]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[RAG]]
- [[Memory]]
- [[Benchmark]]
- [[Task Success Rate]]
