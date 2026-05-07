---
type: concept
topic:
  - agent
  - planning
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
evidence: []
related:
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Evaluation]]"
---

# Planning

## 一句话

Planning 是把目标拆成步骤，并在执行中根据反馈调整步骤。

## 它解决什么问题

复杂任务通常不能一步完成。Planning 帮 Agent 决定先做什么、后做什么、什么时候检查、什么时候停止。

## 它不是什么

Planning 不等于一次性列计划。真正有用的 planning 会随着执行结果变化。

Planning 也不总是越复杂越好。简单任务用固定流程可能更可靠。

## 最小例子

目标：学习 Agent。

一个计划可以是：

1. 先理解 LLM。
2. 再理解 Agent 和 LLM 的区别。
3. 学工具调用。
4. 学记忆和 RAG。
5. 做一个最小问答实验。

如果第 2 步发现概念混乱，就应该回到术语表，而不是硬往前冲。

## 证据锚点

- Source: 待补
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Agent Loop]]
- [[Evaluation]]
