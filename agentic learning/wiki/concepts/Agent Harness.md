---
type: concept
topic:
  - agent
  - frontier
  - evaluation
status: seed
created: 2026-05-05
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[SWE-bench]]"
  - "[[LangSmith Evaluation and Observability]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[SWE-bench#为什么收]]"
  - "[[LangSmith Evaluation and Observability#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Evaluation]]"
  - "[[Agent Loop]]"
  - "[[Patch Validation]]"
  - "[[Repo Context]]"
  - "[[Eval Harness]]"
---

# Agent Harness

## 一句话

Agent Harness 是包住模型、工具、状态、权限、运行环境、trace 和评测逻辑的执行外壳。

## 它解决什么问题

单个 Agent 定义通常只描述“谁在决策”。但真实系统还需要回答：在哪里运行、能调用哪些工具、如何保存状态、如何复现失败、如何评分、如何限制权限。

Harness 负责把这些东西组织成一个可运行、可调试、可评估的系统。

## 它不是什么

Agent Harness 不是模型。

Agent Harness 也不是 Agent 本身。它更像 Agent 的实验台或运行壳。

## 最小例子

代码 Agent 的 harness 可能包括：

- checkout 一个 GitHub repo。
- 给 Agent issue 描述。
- 允许它读写文件和运行测试。
- 收集 patch、日志和测试结果。
- 判断任务是否完成。

[[SWE-bench]] 是一个很好的例子：它提供 issue、repo snapshot、patch 应用和测试运行机制，因此不只是 benchmark，也是代码 Agent 评测 harness 的典型形态。

## 边界细节

Agent Harness 偏运行系统；Eval Harness 偏评测系统。两者经常重叠。

更细一点：如果它回答“Agent 怎么跑起来”，偏 [[Agent Harness]]；如果它回答“怎么重复测试并判断好坏”，偏 [[Eval Harness]]。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[SWE-bench]]
- Source: [[LangSmith Evaluation and Observability]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Evaluation]]
- [[Agent Loop]]
- [[SWE-bench]]
- [[Patch Validation]]
- [[Repo Context]]
- [[Eval Harness]]
