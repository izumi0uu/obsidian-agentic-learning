---
type: concept
topic:
  - evaluation
  - agent
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
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
  - "[[Benchmark]]"
  - "[[Agent Harness]]"
---

# Task Success Rate

## 一句话

Task Success Rate 是任务端到端成功完成的比例。

## 它解决什么问题

Agent 的输出可能看起来合理，但任务没有完成。Task Success Rate 直接问：目标有没有达成？

## 它不是什么

Task Success Rate 不解释失败原因。

它也不保证过程安全。一个 Agent 可能完成任务但用了高风险路径。

## 最小例子

在 SWE-bench 中，如果生成 patch 后测试通过，就算该任务成功；成功任务数除以总任务数就是 success rate。

## 边界细节

Task Success Rate 常需要 harness 支持，因为必须自动运行任务、检查结果和复现失败。

## 证据锚点

- Source: [[GAIA Benchmark]]
- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Evaluation]]
- [[Benchmark]]
- [[Agent Harness]]
