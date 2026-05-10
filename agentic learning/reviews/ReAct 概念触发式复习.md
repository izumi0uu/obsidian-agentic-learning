---
type: review
topic:
  - agent
  - review
  - feynman
status: active
created: 2026-05-10
updated: 2026-05-10
source:
  - "[[ReAct]]"
related:
  - "[[reviews/复习记录索引]]"
  - "[[ReAct]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Observation]]"
  - "[[Agent Harness]]"
  - "[[02 问题池]]"
  - "[[05 Query 写回队列]]"
---

# ReAct 概念触发式复习

日期：2026-05-10

## 目标

用费曼方式检查我是否真的理解 [[ReAct]]：不是背定义，而是能说清它的执行分工、循环边界和现代工程落点。

## 我的原始解释

> ReAct，我会解释它是什么，它是 LLM 的一种 Agent loop 范式，LLM 每轮输出下一步想法/动作，外部框架负责执行动作（tool calling），拿到 observation（tool 返回结果），塞到上下文，然后 LLM 再输出想法或动作，直到想法已经觉得解决了问题。

## 校准版

ReAct 是 Reasoning + Acting 的 [[Agent Loop]] 范式。模型每轮根据上下文输出下一步推理意图和动作请求；外部框架解析或接收这个 action，通过 [[Tool Calling]] 执行真实工具，拿到 [[Observation]]，再把 observation 写回上下文或显式 state。模型基于新的 observation 继续决定下一步，直到输出 final answer，或者运行框架因为成功条件、最大步数、错误策略、预算上限或人工接管而停止。

## 我已经说对的点

- 抓住了“LLM 每轮只输出下一步”。
- 抓住了“外部框架负责执行工具和驱动循环”。
- 抓住了 “observation 回填上下文后再进入下一轮”。

## 需要更精确的点

- ReAct 不是 LLM 自己在后台循环，loop controller 在框架或 [[Agent Harness]] 里。
- `Action` 可以用现代 [[Tool Calling]] 接管，不一定继续依赖纯文本 `Action: ...` 格式。
- [[Observation]] 不只等于 tool 返回值，也可以是环境状态、网页状态、代码执行结果、测试反馈或用户反馈。
- 停止条件不只由“模型觉得解决了”决定，还可以由框架的成功条件、最大步数、预算、错误策略或人工审批决定。

## 第一轮追问

1. 如果 LLM 每轮只输出文本，为什么说 ReAct 的循环不是 LLM 自己跑起来的？
2. ReAct 和普通一次性 tool calling 的最小区别是什么？
3. Observation 和上下文、Agent State、Memory 的边界分别是什么？
4. 为什么生产系统通常不会只靠裸 `Thought -> Action -> Observation` prompt 跑 ReAct？
5. 如果 ReAct 陷入原地打转，你会从框架层加哪些停止或纠错机制？

## 我的费曼回答区

### Q1：如果 LLM 每轮只输出文本，为什么说 ReAct 的循环不是 LLM 自己跑起来的？

我的回答：

反馈：

写回：

### Q2：ReAct 和普通一次性 tool calling 的最小区别是什么？

我的回答：

反馈：

写回：

### Q3：Observation 和上下文、Agent State、Memory 的边界分别是什么？

我的回答：

反馈：

写回：

### Q4：为什么生产系统通常不会只靠裸 `Thought -> Action -> Observation` prompt 跑 ReAct？

我的回答：

反馈：

写回：

### Q5：如果 ReAct 陷入原地打转，你会从框架层加哪些停止或纠错机制？

我的回答：

反馈：

写回：

## 写回候选

- [ ] 如果能清楚解释 Q1，把“loop controller 在框架里”补进 [[ReAct]] 或 [[Agent Loop]]。
- [ ] 如果 Q3 仍然卡住，把 “Observation / Agent State / Memory 的边界” 加入 [[02 问题池]]。
- [ ] 如果 Q5 能回答完整，把停止条件和纠错机制补进 [[Agent Harness]] 或 [[Agent Framework]]。

## 下一次复习触发

当我能不用看卡片解释这句话时，再推进下一轮：

> ReAct 的核心不是固定的 prompt 格式，而是“模型提出下一步，框架执行动作并回填观察，再让模型基于观察继续决策”的行动循环分工。
