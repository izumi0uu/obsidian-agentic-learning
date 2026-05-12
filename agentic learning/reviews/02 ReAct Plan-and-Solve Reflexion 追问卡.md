---
type: review
topic:
  - agent
  - review
  - feynman
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[01 概念触发式复习]]"
  - "[[ReAct]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[Reflexion]]"
related:
  - "[[reviews/复习记录索引]]"
  - "[[Agent Loop]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Observation]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory]]"
  - "[[Memory Reflection]]"
  - "[[Long-term Memory]]"
---

# 02 ReAct Plan-and-Solve Reflexion 追问卡

日期：2026-05-12

## 来源

这张追问卡基于 [[01 概念触发式复习]] 生成，只追问已经暴露出来的边界，不开新战线。

## 使用规则

- 每次只答一张卡。
- 回答时先用自己的话说，不翻概念卡。
- 每题尽量用 3-6 句话说清，不追求长。
- 答完后由 Codex 补反馈、勾选掌握情况，并决定是否写回 [[02 问题池]]、[[05 Query 写回队列]] 或概念卡。

## 当前掌握状态

已基本掌握：

- [[ReAct]] 的 loop controller 在框架 / [[Agent Harness]]，不是 LLM 自己后台循环。
- [[Observation]]、context、[[Agent State]]、[[Memory]] 的基础边界。
- [[Plan-and-Solve Prompting]] 不是完整 Agent loop，因为没有外部 action / observation。
- [[Reflexion]] 的主链路：`Trajectory -> Evaluator -> Self-reflection -> Experience -> Actor`。

仍需追问：

- ReAct 原地打转时，框架层如何停止、纠错、评估和升级。
- `plan 文本`、`Agent State 里的 task list`、`context 投影` 的边界。
- Plan-and-Solve、ReAct、Reflexion 在执行时序里的位置差异。
- Experience 什么时候只是当前任务经验，什么时候才能进入长期记忆。

---

## 追问卡 1：ReAct 原地打转怎么止损？

### 问题

如果一个 ReAct Agent 连续两轮调用同一个工具、同一组参数，并得到相似的 [[Observation]]，框架应该怎么判断和处理？

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

回答里至少出现 3 类机制：

- 停止：最大步数、重复 action 检测、预算、超时。
- 纠错：参数修正、换工具、query rewrite、replan。
- 升级：evaluator、ask user、human approval、handoff。

### 边界提醒

“多加工具”不是止损机制。关键是判断这一步有没有带来新信息；没有新信息时要停、改路或升级。

---

## 追问卡 2：一次性 tool calling 和 ReAct 的最小区别

### 问题

请用一句话区分“一次性 tool calling”和 ReAct，必须出现 `Observation`。

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

标准句应该接近：

> 一次性 tool calling 通常是工具返回后汇总答案；ReAct 会把 [[Observation]] 回填进上下文或 state，让模型基于 observation 决定下一步 action 或 final answer。

### 边界提醒

区别不在于“工具调用次数一定更多”，而在于 observation 是否驱动下一轮决策。

---

## 追问卡 3：plan 文本、task list、context 投影

### 问题

用一句话区分 `plan 文本`、`Agent State 里的 task list`、`context 投影`。

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

需要切开三层：

- `plan 文本`：模型输出的一段推理草稿或任务草稿。
- `Agent State 里的 task list`：runtime 可读、可更新、可检查的任务状态。
- `context 投影`：框架从 state / memory / trace 中挑出来，放进本轮模型输入的信息。

### 边界提醒

把 plan 放进 [[Agent State]] 不等于“塞回上下文”。State 是系统事实；context 是给模型看的当前投影。

---

## 追问卡 4：代码任务为什么越过 prompt-only Plan-and-Solve？

### 问题

如果一个代码 Agent 的 plan 是“修改函数 -> 跑测试 -> 修复失败”，测试失败后为什么这已经不是 prompt-only [[Plan-and-Solve Prompting]]？

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

回答里要出现：

- 测试失败是外部环境返回的 observation。
- observation 会改变下一步执行或触发 replan。
- plan 已经进入 runtime / workflow，而不只是一次回答里的推理脚手架。

### 边界提醒

有没有 plan 不是关键；有没有外部 feedback 改变后续执行，才是 prompt-only 和 [[Agent Workflow]] 的分界。

---

## 追问卡 5：plan 错了怎么补救？

### 问题

plan 一开始错了时，为什么 workflow 的补救不等于“让人插一句新 prompt”？

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

需要说出 workflow 的补救控制点：

- [[Agent State]] 记录失败位置。
- 工具结果、测试、检索或 evaluator 给出 evidence。
- replan 节点根据失败原因改计划。
- 必要时才 ask user / human approval / handoff。

### 边界提醒

human-in-the-loop 是升级路径，不是唯一补救机制。更核心的是 state、observation、evaluator、replan。

---

## 追问卡 6：Reflexion 的 Experience 是否等于长期记忆？

### 问题

为什么说 [[Reflexion]] 里的 Experience 不自动等于 [[Long-term Memory]]？

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

回答里要包含：

- Experience 先是下一轮 Actor 可读的反思经验。
- 只有可靠、可验证、可泛化、不泄露敏感信息、不污染未来任务时，才适合沉淀为长期记忆。
- 局部工具参数、偶然失败、当前 repo 状态更适合留在当前上下文或 trace。

### 边界提醒

长期记忆不是“所有有用信息都永久保存”。长期记忆是一种带筛选和治理的复用机制。

---

## 追问卡 7：三者执行时序对比

### 问题

用一个最小流程图对比 [[Plan-and-Solve Prompting]]、[[ReAct]]、[[Reflexion]] 分别把 plan、action、observation、evaluation、reflection 放在哪里。

### 回答区

我的回答：

### 反馈区

Codex 反馈：

### 掌握标准

参考骨架：

```text
Plan-and-Solve:
Prompt -> Plan -> Solve -> Answer

ReAct:
Thought/Decision -> Action -> Observation -> Next Decision -> ... -> Answer

Reflexion:
Trajectory -> Evaluator -> Self-reflection -> Experience -> Next Actor
```

### 边界提醒

三者不是互斥技术栈。现代 Agent 可能同时使用 plan-first、ReAct-style action loop 和 Reflexion-style failure learning；区别在于它们介入任务时序的不同位置。

---

## 本卡收束标准

当我能不用看卡片解释这句话时，本卡收束：

> Plan-and-Solve 解决“先拆再想”的推理结构；ReAct 解决“根据观察继续行动”的执行循环；Reflexion 解决“把评价反馈转成下一轮经验”的失败学习。

## 写回候选

- [ ] 如果追问卡 1 回答清楚，把 ReAct 止损机制写回 [[Agent Harness]] 或 [[Agent Framework]]。
- [ ] 如果追问卡 3 回答清楚，把 `plan 文本 / task list / context 投影` 写回 [[Agent State]] 或 [[Agent Workflow]]。
- [ ] 如果追问卡 6 回答清楚，把 Experience 写入长期记忆的筛选条件写回 [[Long-term Memory]] / [[Memory Reflection]]。
- [ ] 如果追问卡 7 回答清楚，把三者对比沉淀到 [[ReAct Plan-and-Solve Reflexion 对比]]。
