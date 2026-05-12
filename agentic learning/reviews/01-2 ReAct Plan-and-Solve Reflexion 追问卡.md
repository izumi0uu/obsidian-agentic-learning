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
- 不先看底部的“答后校准区”；答完后再对照。
- 每题尽量用 3-6 句话说清，不追求长。
- 答完后由 Codex 补反馈、勾选掌握情况，并决定是否写回 [[02 问题池]]、[[05 Query 写回队列]] 或概念卡。

## 当前掌握状态

已基本掌握：

- [[ReAct]] 的 loop controller 在框架 / [[Agent Harness]]，不是 LLM 自己后台循环。
- [[Observation]]、context、[[Agent State]]、[[Memory]] 的基础边界。
- [[Plan-and-Solve Prompting]] 不是完整 Agent loop，因为没有外部 action / observation。
- [[Reflexion]] 的主链路：`Trajectory -> Evaluator -> Self-reflection -> Experience -> Actor`。

本轮回答后仍需校准：

- [[ReAct]] 原地打转时，你已经答到“最大步数 / 错误次数 / 退出”；已由 Codex 校准后写回“重复 action 检测 -> 改路 -> 升级”的 harness 边界。
- `plan 文本`、`Agent State 里的 task list`、`context 投影` 已由 Codex 校准后写回 [[Agent State]]；重点是 state 是系统事实，context 是本轮模型可见切片。
- [[Plan-and-Solve Prompting]]、[[ReAct]]、[[Reflexion]] 的执行时序已经能大体复述；[[Reflexion]] 需要把 `self-reflection -> Experience -> next Actor` 顺序说得更稳。
- Experience 与长期记忆的边界已经基本掌握：不是所有有用经验都永久保存。

---

## 追问卡 1：ReAct 原地打转怎么止损？

### 问题

如果一个 ReAct Agent 连续两轮调用同一个工具、同一组参数，并得到相似的 [[Observation]]，框架应该怎么判断和处理？

### 回答区

我的回答：

这种情况属于agent内部错误，可能是上下文限制导致的问题，模型幻觉问题。Agent framework可以设置最大步数（最多loop多少次），错误次数，最终确认答案（llm没有再输出action calls），代码测试结果，框架让其退出。

### 反馈区

Codex 反馈：

部分掌握。你已经答到“最大步数、错误次数、没有 action 时退出”，这些属于停止机制；还需要补上本题的关键触发条件：框架要检测 `同一 action + 同一参数 + 相似 observation` 是否没有带来新信息。

更完整的处理链路是：先停止当前重复路径，再尝试参数修正、换工具、query rewrite 或 replan；如果仍然没有新信息，就进入 evaluator、ask user、human approval 或 handoff。边界上，这不一定只是“agent 内部错误”，也可能是工具返回信息不足、context 投影丢了关键条件、模型卡在局部策略，框架真正要判断的是“这轮 observation 是否改变了下一步决策”。

---

## 追问卡 2：一次性 tool calling 和 ReAct 的最小区别

### 问题

请用一句话区分“一次性 tool calling”和 ReAct，必须出现 `Observation`。

### 回答区

我的回答：

对于一次性 tool calling，Observation是在tool call之后的结果（无论怎样都不会进入下一轮loop），而对于ReAct，Observation是由action call 外部工具/环境反馈的结果，是可以让agent驱动LLM是否进行下一步判断（final answer or call 外部工具）

### 反馈区

Codex 反馈：

掌握。你抓住了最小区别：一次性 tool calling 的 observation 通常只用于生成最终回答，而 ReAct 会把 [[Observation]] 回填到下一轮决策里，让模型判断继续 action 还是 final answer。

小边界：区别不在“工具调用次数一定更多”，而在 observation 是否成为循环控制信号。一次性工具调用也可以有工具结果，但它通常不是一个 `observe -> decide -> act` 的持续循环。

---

## 追问卡 3：plan 文本、task list、context 投影

### 问题

用一句话区分 `plan 文本`、`Agent State 里的 task list`、`context 投影`。

### 回答区

我的回答：

plan文本是让LLM在思考的的时候plan出一系列tasks，方便LLM根据tasks去逐步做出推理，`Agent State 里的 task list`是由agent 框架调控的task list，来源也是LLM plan出来的tasks，由Agent state控制。`context 投影`是把原始上下文处理为LLM易于理解的形式，常见于多模态场景。

### 反馈区

Codex 反馈：

基本掌握，但 `context 投影` 的范围说窄了。`plan 文本` 是模型输出的可读计划草稿；`Agent State 里的 task list` 是 runtime 可更新、可检查、可持久化的任务状态；`context 投影` 是框架从 state、memory、trace、文件、工具结果里挑出本轮要给 LLM 看的信息。

关键边界：state 是系统持有的事实和进度，context 是这一次模型调用能看到的切片。多模态只是 context 投影的一种场景，不是它的定义。

---

## 追问卡 4：代码任务为什么越过 prompt-only Plan-and-Solve？

### 问题

如果一个代码 Agent 的 plan 是“修改函数 -> 跑测试 -> 修复失败”，测试失败后为什么这已经不是 prompt-only [[Plan-and-Solve Prompting]]？

### 回答区

我的回答：

修改函数，已经是LLM输出了"action" 由agent框架识别指令并调用某个修改工具修改文件，跑测试同样也是，修复失败是observation。

### 反馈区

Codex 反馈：

掌握。你已经抓到文件修改和跑测试都是 runtime action，测试失败是外部环境返回的 [[Observation]]，而后续修复会被这个 observation 改写。

小修正：`修复失败` 本身不是 observation；测试日志、报错、diff、lint 输出才是 observation，基于这些结果做下一步修改才是 action。分界线不是“有没有 plan”，而是外部反馈是否改变后续执行。

---

## 追问卡 5：plan 错了怎么补救？

### 问题

plan 一开始错了时，为什么 workflow 的补救不等于“让人插一句新 prompt”？

### 回答区

我的回答：

因为这样并不是唯一解，它可以被evaluator自动检测plan质量，如果明显偏离目标，或者plan不明确，可以继续追问user，执行过程中发现现有工具，测试出错，observation无法解决问题，回滚task，把失败写入agent state等等解决方法。让人插一句新 prompt属于human in the loop，是解决方法的一种。

### 反馈区

Codex 反馈：

掌握。你答出了 evaluator、ask user、工具 / 测试 observation、回滚 task、把失败写进 [[Agent State]]，这已经越过了“人补一句 prompt”的单点补救。

边界再压实一点：workflow 的核心补救是可观察、可记录、可分支的控制点，例如失败位置、失败证据、replan 节点、重试预算和升级路径；human-in-the-loop 只是升级路径之一，不是 workflow 的默认补救机制。

---

## 追问卡 6：Reflexion 的 Experience 是否等于长期记忆？

### 问题

为什么说 [[Reflexion]] 里的 Experience 不自动等于 [[Long-term Memory]]？

### 回答区

我的回答：

Experience可以是用于下轮对话，例如一次任务中意识到某个测试用例的更好的写法，那么下轮对话中则可以继续用这条Experience，但是它局限性比较强，所以不会存入长期记忆。如果它是用户的个人习惯，比如用户习惯用中英文输出，那么agent可以拿这条Experience存入长期记忆。

### 反馈区

Codex 反馈：

掌握。你用“当前任务里的测试写法经验”和“用户长期偏好”把边界切开了：Experience 先是下一轮 Actor 可读的反思经验，不自动进入 [[Long-term Memory]]。

可以再补一个筛选条件：只有可靠、可验证、可泛化、不含敏感泄露、不会污染未来任务的 experience，才适合沉淀为长期记忆。一次性 repo 状态、临时工具参数、偶然失败，更适合留在当前 context、trace 或短期任务记忆里。

---

## 追问卡 7：三者执行时序对比

### 问题

用一个最小流程图对比 [[Plan-and-Solve Prompting]]、[[ReAct]]、[[Reflexion]] 分别把 plan、action、observation、evaluation、reflection 放在哪里。

### 回答区

我的回答：

Plan-and-Solve Prompting: Prompt -> LLM -> plan -> tasks -> action(resolve and output)，一般没有observation、evaluation、reflection。
ReAct: LLM -> action -> observation -> LLM -> action(output or action)
Reflexion: LLM -> action -> trajectory -> evaluator (-> LLM -> action)-> experience -> LLM -> action

### 反馈区

Codex 反馈：

基本掌握。[[Plan-and-Solve Prompting]] 你说对了：它主要是 `Prompt -> Plan -> Solve -> Answer`，通常没有外部 observation、evaluation、reflection。[[ReAct]] 也说对了：`Action -> Observation -> Next Decision` 是核心循环。

[[Reflexion]] 的顺序再校准一下：更稳的骨架是 `Actor -> Trajectory -> Evaluator -> Self-reflection -> Experience -> Next Actor`。Experience 不是 evaluator 直接产生下一次 action，而是把失败评价转成下一轮 actor 可读的经验。

---

## 本卡收束标准

当我能不用看卡片解释这句话时，本卡收束：

> Plan-and-Solve 解决“先拆再想”的推理结构；ReAct 解决“根据观察继续行动”的执行循环；Reflexion 解决“把评价反馈转成下一轮经验”的失败学习。

## 写回候选

- [x] 追问卡 1 已写回 [[Agent Harness]]：重复 action + 相似 observation 应触发停止、纠错或升级，而不是继续原地打转。
- [x] 追问卡 3 已写回 [[Agent State]]：`plan 文本 / task list / context 投影` 的边界是 plan 草稿、runtime 状态、当前模型输入切片。
- [x] 追问卡 5 已写回 [[Agent Workflow]]：workflow 的 plan 补救不是“人补一句 prompt”，而是 state、observation、evaluator、replan 和 human-in-the-loop 的组合控制点。
- [x] 追问卡 6 已写回 [[Long-term Memory]] / [[Memory Reflection]]：Experience 写入长期记忆需要可靠、可验证、可泛化、安全、低污染风险。
- [x] 追问卡 7 已写回 [[ReAct Plan-and-Solve Reflexion 对比]]：三者对比可沉淀为执行时序边界，尤其是 plan / observation / evaluation / reflection 的介入位置。

## 本轮收束结论

第二轮追问已收束，不继续加新问题。卡 1、3、5、6、7 的稳定边界均已写回；其中卡 1、3 是由 Codex 依据反馈区校准后写回，不代表原回答当时已经完全掌握。后续复习重点仍是：能自然说出“重复检测 -> 改路 -> 升级”和“state 与 context 投影的区别”。

## 答后校准区

答完对应追问卡后，再看这里对照。这里不是答题前提示。

### 追问卡 1 校准

回答里至少出现 3 类机制：

- 停止：最大步数、重复 action 检测、预算、超时。
- 纠错：参数修正、换工具、query rewrite、replan。
- 升级：evaluator、ask user、human approval、handoff。

边界提醒：多加工具不是止损机制。关键是判断这一步有没有带来新信息；没有新信息时要停、改路或升级。

### 追问卡 2 校准

标准句应该接近：

> 一次性 tool calling 通常是工具返回后汇总答案；ReAct 会把 [[Observation]] 回填进上下文或 state，让模型基于 observation 决定下一步 action 或 final answer。

边界提醒：区别不在于“工具调用次数一定更多”，而在于 observation 是否驱动下一轮决策。

### 追问卡 3 校准

需要切开三层：

- `plan 文本`：模型输出的一段推理草稿或任务草稿。
- `Agent State 里的 task list`：runtime 可读、可更新、可检查的任务状态。
- `context 投影`：框架从 state / memory / trace 中挑出来，放进本轮模型输入的信息。

边界提醒：把 plan 放进 [[Agent State]] 不等于“塞回上下文”。State 是系统事实；context 是给模型看的当前投影。

### 追问卡 4 校准

回答里要出现：

- 测试失败是外部环境返回的 observation。
- observation 会改变下一步执行或触发 replan。
- plan 已经进入 runtime / workflow，而不只是一次回答里的推理脚手架。

边界提醒：有没有 plan 不是关键；有没有外部 feedback 改变后续执行，才是 prompt-only 和 [[Agent Workflow]] 的分界。

### 追问卡 5 校准

需要说出 workflow 的补救控制点：

- [[Agent State]] 记录失败位置。
- 工具结果、测试、检索或 evaluator 给出 evidence。
- replan 节点根据失败原因改计划。
- 必要时才 ask user / human approval / handoff。

边界提醒：human-in-the-loop 是升级路径，不是唯一补救机制。更核心的是 state、observation、evaluator、replan。

### 追问卡 6 校准

回答里要包含：

- Experience 先是下一轮 Actor 可读的反思经验。
- 只有可靠、可验证、可泛化、不泄露敏感信息、不污染未来任务时，才适合沉淀为长期记忆。
- 局部工具参数、偶然失败、当前 repo 状态更适合留在当前上下文或 trace。

边界提醒：长期记忆不是“所有有用信息都永久保存”。长期记忆是一种带筛选和治理的复用机制。

### 追问卡 7 校准

参考骨架：

```text
Plan-and-Solve:
Prompt -> Plan -> Solve -> Answer

ReAct:
Thought/Decision -> Action -> Observation -> Next Decision -> ... -> Answer

Reflexion:
Trajectory -> Evaluator -> Self-reflection -> Experience -> Next Actor
```

边界提醒：三者不是互斥技术栈。现代 Agent 可能同时使用 plan-first、ReAct-style action loop 和 Reflexion-style failure learning；区别在于它们介入任务时序的不同位置。
