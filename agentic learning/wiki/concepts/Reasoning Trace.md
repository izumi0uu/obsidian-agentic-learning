---
type: concept
topic:
  - agent
  - evaluation
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
related:
  - "[[ReAct]]"
  - "[[Agent Loop]]"
  - "[[Trajectory Trace 类型对比]]"
  - "[[Trace]]"
  - "[[Trajectory]]"
---

# Reasoning Trace

## 一句话

Reasoning Trace 是模型在解决任务过程中显式留下的推理文字或推理步骤记录。

## 概念详解

Reasoning Trace 最早容易从 ReAct 这类范式理解：模型一边写 `Thought`，一边选择 `Action`，再读取 `Observation`。这里的 reasoning trace 是显式文本，帮助人类或系统看到模型“声称自己如何推理”。它可以让调试更容易：为什么选择这个工具、为什么换搜索词、为什么认为观察结果足够。

但现代系统对它更谨慎。模型写出的推理文字不一定等于真实内部机制，也可能包含错误解释、过度自信、敏感信息或可被 prompt injection 操纵的内容。因此很多产品不会暴露完整 chain-of-thought，而是保存结构化 trace、摘要、理由标签、工具调用依据或可审计的简短 rationale。

对 evaluation 来说，Reasoning Trace 是过程证据的一部分，但不是完整过程。真正的 [[Trajectory]] 还包括动作、观察、环境状态、工具结果、错误、成本和最终输出；[[Trace]] 则是系统把这些过程保存成可观察记录。评估时要避免只给推理文字打分，而忽略工具是否真的安全有效。


Reasoning Trace 的学习价值主要在“可解释入口”，不是“真相保证”。它能帮助人类发现模型显式写下的假设：比如它以为某个工具能联网、以为观察结果已经足够、以为用户授权了高风险动作。但这些假设必须拿工具结果、状态、权限记录和最终 checker 交叉验证。否则评估者可能被一段流畅推理说服，却忽略实际 trajectory 已经失败。

因此现代 harness 更常把 reasoning trace 降级成诊断材料：可以保存摘要、标签、计划步骤或工具选择理由，但最终质量判断仍要回到可观察动作和结果。

## 它解决什么问题

推理轨迹能帮助跟踪计划、解释中间决策、发现错误传播，也能让人更容易理解 Agent 为什么采取某个动作。

它还帮助学习者理解 ReAct、Plan-and-Solve、Reflexion 等方法为什么会把“想法/行动/观察”拆开。

## 它不是什么

Reasoning Trace 不一定等于模型真实内部原因。

它也不一定应该暴露给用户。生产系统可能只保留结构化 trace 或摘要，而不展示完整推理文本。

Reasoning Trace 也不等于 [[Trajectory]]。Trajectory 是一次任务的完整行动路径；Reasoning Trace 只是这条路径里模型显式推理文字的部分。

## 最小例子

ReAct 里的 `Thought` 字段就是一种 reasoning trace。

```text
Thought: I need current weather before recommending clothing.
Action: weather.lookup(city="Shanghai")
Observation: 18°C and raining.
```

这里 `Thought` 是 reasoning trace；`Action` 和 `Observation` 属于更完整的 trajectory/trace。

## 常见误解 / 风险

- 把 reasoning trace 当成模型真实内心：它只是生成出来的解释性文本。
- 只评估推理文字流畅度：文字好看不代表工具调用正确。
- 把完整 chain-of-thought 暴露给终端用户：可能带来隐私、安全或产品体验风险。
- 忽略结构化 trace：没有工具结果和状态变化，推理文字很难验证。

## 边界细节

Reasoning Trace 偏“推理文字”；[[Trace]] 更广，包括输入、输出、工具调用、工具结果、状态变化和成本延迟等执行记录；[[Trajectory]] 则偏任务实际走过的路径本身。

在 evaluation harness 中，可以把 reasoning trace 当成诊断材料，而不是唯一评分对象：

- 可用于定位错误计划或错误假设。
- 可用于生成失败摘要或人工 review 提示。
- 不应单独证明任务成功、安全或合规。
- 高风险场景更应依赖工具结果、权限记录、audit log 和最终 checker。

## 现代性状态

- 判定：transitional / current-practice boundary。
- 为什么：显式 reasoning trace 是 ReAct 等论文范式的重要学习入口；现代产品通常把完整推理文本收敛为结构化 trace、摘要 rationale 或内部诊断信号。
- 稳定部分：过程解释有助于调试和学习。
- 易变部分：不同模型/平台如何暴露、隐藏、摘要或审计推理内容会持续变化。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: [[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]
- Evidence type: paper source note + modern Agent safety/observability synthesis.
- Confidence: medium
- Boundary: ReAct 的 `Thought` 是概念入口；现代系统是否保留或展示完整推理文本取决于产品、安全和平台策略。

## 复习触发

- 为什么 Reasoning Trace 不是 [[Trajectory]]？
- 一个工具调用失败时，推理文字能告诉你什么，不能告诉你什么？
- 为什么现代系统可能只展示推理摘要而不是完整 chain-of-thought？

## 相关链接

- [[ReAct]]
- [[Trajectory Trace 类型对比]]
- [[Trace]]
- [[Trajectory]]
- [[Agent Loop]]
