---
type: map
topic:
  - agent
  - comparison
status: active
created: 2026-05-10
updated: 2026-05-10
source:
  - "[[Observation]]"
  - "[[ReAct]]"
  - "[[Agent Loop]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning]]"
related:
  - "[[Agent 主题]]"
  - "[[ReAct]]"
  - "[[Agent Loop]]"
  - "[[Observation]]"
  - "[[Agent State]]"
  - "[[Trace]]"
---

# Environment Observation 类型对比

这页专门回答：ReAct / Reflexion 图里的 Environment 和 Observation 是不是一回事。

核心边界：Environment 是动作发生的外部世界、工具系统或任务环境；Observation 是 Agent 执行动作后，从这个环境返回的反馈结果。

## 一张表先抓住

| 类型 | 核心含义 | 在 loop 里的位置 | 主要解决什么问题 | 它不是什么 |
|---|---|---|---|---|
| Environment | 动作发生的外部世界、工具系统、网页、文件系统、测试环境或游戏环境 | Action 被执行的地方 | 给 Agent 提供可被作用、会变化、会返回结果的外部对象 | 不是单次返回结果，也不是模型自己的上下文 |
| [[Observation]] | Action 执行后返回给 Agent 的反馈、结果或新状态 | Action 之后，下一轮 Thought 之前 | 让模型知道刚才动作产生了什么结果 | 不是 Environment 本身，也不是 Action |
| Action | Agent 请求执行的动作和参数 | Thought 之后，Environment 之前 | 把模型意图交给外部执行 | 不是执行结果 |
| [[Agent State]] | 框架保存的当前任务运行状态 | 每轮都可能读写 | 保存目标、进度、中间结果、最近 observation | 不是外部环境本身 |
| [[Trace]] | 对每一步输入、动作、observation、状态变化的记录 | 贯穿整个执行过程 | 调试、复盘、评测、重放 | 不是 Environment，也不是 Observation 本身 |

## 生活类比

把 ReAct 想成“你去图书馆找一本书”：

| Agent 概念 | 生活中的对应物 | 为什么这样类比 |
|---|---|---|
| Environment | 图书馆：书架、馆员、借阅系统、自习区 | 这是你行动发生的外部世界，它会根据你的动作给出反馈 |
| Action | 你问馆员：“请帮我查《ReAct》这本书在哪里” | 这是你发出的动作请求 |
| [[Observation]] | 馆员回答：“在三楼 A 区，索书号 005.1” | 这是环境对这次动作返回的结果 |
| [[Agent State]] | 你手里的便签：目标是找书，已知道三楼 A 区，下一步去三楼 | 这是当前任务进度，不等于图书馆本身 |
| [[Trace]] | 你事后的行程记录：几点进馆、问了谁、得到什么回答、去了哪里 | 这是对过程的记录 |

这个类比里最关键的一刀是：图书馆是 environment；馆员给你的回答是 observation。你不能说“图书馆等于馆员回答”，同样也不能说 “Environment 等于 Observation”。

## ReAct 里的位置

经典 ReAct 可以这样理解：

```text
Thought -> Action -> Environment 执行动作 -> Observation -> Thought -> ...
```

举例：

```text
Thought: 我需要查论文作者。
Action: Search["ReAct paper authors"]
Environment: 搜索引擎 / 浏览器 / 网页集合
Observation: 搜索结果显示作者包括 Yao 等人。
```

Environment 是被调用或被作用的外部系统；Observation 是这次调用之后返回给 Agent runtime 的结果。

## 按问题选型

### 我问“Agent 在哪里行动？”

看 Environment。

它可能是搜索引擎、浏览器、文件系统、数据库、终端、网页、游戏环境、机器人所在物理世界，或者测试环境。

### 我问“刚才行动后发生了什么？”

看 [[Observation]]。

它可能是搜索结果、网页内容、命令输出、测试失败日志、传感器读数、用户确认、审批结果或环境新状态。

### 我问“这次任务现在走到哪了？”

看 [[Agent State]]。

state 会保存最近 observation，但 state 不等于 observation；state 是框架组织当前任务进度的结构。

### 我问“整个过程怎么复盘？”

看 [[Trace]]。

trace 会把 action、observation、状态变化和模型输出都记录下来。

## 最容易混淆的边界

- Environment vs [[Observation]]：Environment 是外部世界；Observation 是外部世界对某次动作的返回。
- [[Observation]] vs Action：Action 是请求；Observation 是请求后的结果。
- Environment vs [[Agent State]]：Environment 在外部；State 是框架保存的当前任务内部状态。
- [[Observation]] vs [[Trace]]：Observation 是单步反馈；Trace 是多步过程记录。
- Environment vs Tool：Tool 常常是接入 environment 的接口；environment 可以比 tool 更大，例如整个网页世界、文件系统或游戏状态。

## 对我的学习建议

当前阶段可以这样背：

1. Environment 是“我行动的地方”。
2. Action 是“我做了什么请求”。
3. Observation 是“外部世界回了什么”。
4. State 是“当前任务记住了什么”。
5. Trace 是“事后能查到什么记录”。

## 相关链接

- [[Agent 主题]]
- [[ReAct]]
- [[Agent Loop]]
- [[Observation]]
- [[Agent State]]
- [[Trace]]
- [[Trajectory]]
