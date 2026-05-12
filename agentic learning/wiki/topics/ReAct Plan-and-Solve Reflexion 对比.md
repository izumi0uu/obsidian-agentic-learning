---
type: map
topic:
  - agent
  - reasoning
  - planning
  - evaluation
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[ReAct]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[Reflexion]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#必读块 1：Abstract / reasoning traces 与 actions 交错生成]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#必读块 2：Method / Plan then Solve]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#必读块 1：Abstract / linguistic feedback 而非权重更新]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#必读块 2：Abstract / episodic memory buffer]]"
related:
  - "[[Agent Loop]]"
  - "[[Planning]]"
  - "[[Reasoning Trace]]"
  - "[[Observation]]"
  - "[[Trajectory Evaluation]]"
  - "[[Memory Reflection]]"
  - "[[Agent Workflow]]"
---

# ReAct Plan-and-Solve Reflexion 对比

## 一句话总览

这三者都在改善“模型怎样把复杂任务做得更可靠”，但介入点不同：[[Plan-and-Solve Prompting]] 在回答前先拆任务，[[ReAct]] 在执行中用 Action / [[Observation]] 交替校正，[[Reflexion]] 在一次尝试后把评价反馈写成经验，影响下一轮。

最小边界：Plan-and-Solve 是 **pre-solve planning**；ReAct 是 **in-the-loop acting and observing**；Reflexion 是 **post-trajectory feedback-to-experience**。

## 为什么这组值得对比

- 混淆风险高：三者都会出现“推理、计划、行动、反思”这些词，容易被统称为“Agent 会自己思考”。
- 共同问题域相近：都试图减少复杂任务中的盲目生成、漏步骤、外部事实缺失或重复失败。
- 介入点不同：一个在求解前，一个在执行中，一个在执行后。
- 证据足够：三张概念卡和三篇 paper source note 都已有定义、机制和边界锚点。
- 现代工程价值明显：它们分别对应现代系统里的 plan artifact、tool/action loop、evaluation + memory / retry policy。

边界：这页不是把三者强行归成一个家族；它们只是都帮助理解“复杂任务可靠性”的不同切面。

## 共同问题域

共同问题可以概括为：LLM 直接生成答案时，可能漏步骤、缺外部反馈、失败后重复犯错。三者都在给“直接生成”加结构，但加的位置不同。

- Plan-and-Solve 认为问题可能出在一开始没有显式拆解，所以先生成 plan，再 solve。
- ReAct 认为问题可能出在封闭推理缺少外部校准，所以把 reasoning、action、observation 放进同一条执行轨迹。
- Reflexion 认为问题可能出在失败经验没有回流，所以用 evaluator feedback 生成反思文本，写入 experience / memory 供下一轮使用。

这也是它们最适合一起学习的原因：它们像把同一条任务时间线切成三个位置——行动前、行动中、行动后。

## 核心区别表

| 概念 | 主要介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Plan-and-Solve Prompting]] | 求解前的 prompt-level planning | `Question -> Plan -> Solve -> Answer` | 单个问题、提示词 | 计划文本、推理过程、答案 | [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#必读块 2：Method / Plan then Solve]] |
| [[ReAct]] | 执行中的 reasoning/action/observation 交替 | `Thought -> Action -> Observation -> Thought -> ...` | 任务目标、上下文、工具/环境反馈 | 行动轨迹、观察反馈、最终答案 | [[ReAct - Synergizing Reasoning and Acting in Language Models#必读块 1：Abstract / reasoning traces 与 actions 交错生成]] |
| [[Reflexion]] | 尝试后的评价、反思和经验回流 | `Trajectory -> Evaluator -> Self-reflection -> Experience -> Actor` | 轨迹、任务反馈、评价信号 | reflective text、experience memory、下一轮策略 | [[Reflexion - Language Agents with Verbal Reinforcement Learning#必读块 2：Abstract / episodic memory buffer]] |

## 最容易混淆的边界

### Plan-and-Solve vs ReAct

[[Plan-and-Solve Prompting]] 的 plan 仍然是一次回答内部的文本结构。它没有外部 Action，也没有 Observation 反馈；如果 plan 错了，系统不会天然通过环境反馈纠正。

[[ReAct]] 的关键不是“先写计划”，而是行动会改变可见信息：Action 触发工具或环境，Observation 回到上下文，影响下一轮判断。换句话说，Plan-and-Solve 更像把任务拆清楚再答；ReAct 更像边做边看反馈。

### ReAct vs Reflexion

[[ReAct]] 的 observation 通常影响当前 trajectory 的下一步：查到新资料、工具失败、网页状态变化，都会让下一轮 action 改变。

[[Reflexion]] 的 reflection 更偏一次尝试之后的经验总结：它读取 trajectory 和 evaluator feedback，生成 reflective text，再影响下一次 Actor。它不只是“看到 observation 后继续行动”，而是把评价过的经验保存下来。

### Plan-and-Solve vs Reflexion

Plan-and-Solve 的 plan 面向未来：在求解前预先组织步骤。Reflexion 的 reflective text 面向过去：从已发生的 trajectory / feedback 中抽取经验。

因此，不要把“计划”误写成“反思”，也不要把“反思”误写成“更长的计划”。前者问“接下来怎么做”，后者问“刚才为什么错，下一轮要避免什么”。

## 执行时序 / 机制差异

```text
Plan-and-Solve Prompting
User Question -> Prompt asks for Plan -> Model writes Plan -> Model solves -> Answer

ReAct
Goal/Context -> Reasoning Trace -> Action -> Environment/Tool -> Observation -> next Reasoning/Action -> Answer

Reflexion
Attempt Trajectory -> Evaluator Feedback -> Self-reflection -> Experience Memory -> next Actor/Attempt
```

把它们放在一条更长的工程时间线里：

```text
Before attempt:  Plan-and-Solve style decomposition
During attempt:  ReAct style action-observation loop
After attempt:   Reflexion style evaluation-reflection-memory loop
```

这条时间线是学习综合，不是三篇论文共同给出的统一架构。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

做一道复杂菜：

- Plan-and-Solve：开火前先写菜谱步骤，避免漏掉“先腌制”或“先备料”。
- ReAct：做菜时边尝味道边调整，发现太咸就加水，发现没熟就继续加热。
- Reflexion：这次做失败后，记录“下次先控盐，最后再收汁”，下次做菜前读这条经验。

类比的边界：真实 Agent 不只是厨师的脑内想法；工具执行、状态记录、权限、trace 和 evaluator 都属于外部 runtime / harness 的责任。

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[ReAct]] 卡和 source note 支持 reasoning / action / observation 交替这个地基思想；现代工程来源进一步提示它通常会被 [[Tool Calling]]、[[Agent State]]、[[Trace]]、[[Guardrails]] 和 [[Agent Harness]] 包住。
- [[Plan-and-Solve Prompting]] 卡和 source note 支持“先拆成子任务，再按计划求解”的 prompt-level 方法；现代系统会把这个思想升级成任务列表、依赖关系、验收标准或 planner-executor workflow。
- [[Reflexion]] 卡和 source note 支持“评价反馈 -> 反思文本 -> experience memory”的机制；现代系统会把它吸收到 retry policy、failure summarization、memory 写入门槛和 [[Trajectory Evaluation]] 中。

### 工程综合 / inference

把三者看成“任务可靠性的三个插入点”是本页的学习综合：

- 行动前：先拆任务，降低漏步骤。
- 行动中：用外部反馈校正下一步。
- 行动后：把失败归因和经验回流到下一轮。

这个综合有助于学习现代 Agent，但不能反向写成某篇论文原本提出的统一框架。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 单轮复杂推理，主要风险是漏步骤 | [[Plan-and-Solve Prompting]] | 先显式拆解任务，再求解 | 计划可能看似完整但不可验证；不适合需要外部环境反馈的任务 |
| 任务需要查资料、调工具、观察网页或环境变化 | [[ReAct]] | Action 产生 Observation，Observation 改变下一步 | 裸 prompt parser 脆弱；必须由 tool schema、state、权限和 trace 接管执行边界 |
| 任务会多次尝试，且有 evaluator 能判断失败原因 | [[Reflexion]] | 失败反馈可转成下一轮经验 | evaluator 错误会污染经验；反思写入长期记忆前需要门槛 |
| 生产级长任务 Agent | 三者都只能作为局部思想 | 需要 plan、action loop、eval、memory、guardrails、human-in-the-loop 组合 | 不应把任何一个论文范式当完整 Agent framework |

## 它们共同不是什么

- 它们都不是完整的生产级 [[Agent Framework]]。
- 它们都不是模型权重训练方法；Reflexion 明确强调通过语言反馈而不是更新权重。
- 它们都不保证可靠性本身；可靠性还需要 [[Evaluation]]、[[Trace]]、权限、状态、重试和人类确认。
- 它们都不等于“模型真实内心”。reasoning trace、plan、reflection 都是可用文本产物，但不能当作未验证事实。

## 证据锚点

- Definition / mechanism anchors:
  - [[ReAct - Synergizing Reasoning and Acting in Language Models#必读块 1：Abstract / reasoning traces 与 actions 交错生成]]
  - [[ReAct - Synergizing Reasoning and Acting in Language Models#必读块 2：Abstract / 外部信息和 hallucination]]
  - [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#必读块 1：Abstract / Zero-shot-CoT 的三类错误]]
  - [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#必读块 2：Method / Plan then Solve]]
  - [[Reflexion - Language Agents with Verbal Reinforcement Learning#必读块 1：Abstract / linguistic feedback 而非权重更新]]
  - [[Reflexion - Language Agents with Verbal Reinforcement Learning#必读块 2：Abstract / episodic memory buffer]]
- Concept synthesis anchors: [[ReAct#概念详解]], [[Plan-and-Solve Prompting#概念详解]], [[Reflexion#概念详解]]
- Evidence type: paper source notes + existing concept-card synthesis + explicitly labeled learning analogy.
- Confidence: core distinctions 为 medium-high；modern-system absorption summary 为 medium，因为它是跨卡工程综合。
- Boundary: 论文/source note 支持各自机制；“行动前 / 行动中 / 行动后”是本页学习框架，不是任一论文的原文主张。

## 复习触发

1. 如果一个方法只有 `Plan -> Solve -> Answer`，为什么它还不是 ReAct？
2. ReAct 中的 Observation 和 Reflexion 中的 evaluator feedback 最小区别是什么？
3. 为什么 Reflexion 的 reflective text 不等于普通 [[Reasoning Trace]]？
4. 给一个浏览器 Agent 失败案例：哪些部分适合用 plan，哪些部分适合用 ReAct loop，哪些部分适合写成 Reflexion experience？
5. 如果 evaluator 给错反馈，三者里哪个机制最容易把错误固化到下一轮？为什么？

## 相关链接

- [[ReAct]]
- [[Plan-and-Solve Prompting]]
- [[Reflexion]]
- [[Agent Loop]]
- [[Planning]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Trajectory]]
- [[Trajectory Evaluation]]
- [[Memory Reflection]]
- [[Agent Workflow]]
- [[Agent Harness]]
- [[LLM Wiki 工作流]]
