---
type: concept
topic:
  - agent
  - planning
status: growing
created: 2026-05-05
updated: 2026-05-08
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
evidence: []
related:
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Evaluation]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[ReAct]]"
---

# Planning

## 一句话

Planning 是把目标拆成步骤，并在执行中根据反馈调整步骤。

## 它解决什么问题

复杂任务通常不能一步完成。Planning 帮 Agent 决定先做什么、后做什么、什么时候检查、什么时候停止。

## 它不是什么

Planning 不等于一次性列计划。真正有用的 planning 会随着执行结果变化。

Planning 也不总是越复杂越好。简单任务用固定流程可能更可靠。

Planning 也不一定意味着 Agent 已经开始行动。[[Plan-and-Solve Prompting]] 里的 planning 只是提示模型先写计划再求解；[[ReAct]] 或生产 Agent 里的 planning 才可能和工具调用、观察反馈、状态保存、重试、停止条件绑定。

用户提供的 Planning Phase / Solving Phase 图可以看成工程版 planning：User 触发 Plan，Plan 生成任务列表，Task Agent 执行任务，Replan 根据执行结果更新计划。这说明 planning 在 Agent 里通常不是静态清单，而是会和执行反馈相互拉扯。

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

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#为什么收]]
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Agent Loop]]
- [[Evaluation]]
- [[Plan-and-Solve Prompting]]
- [[ReAct]]
