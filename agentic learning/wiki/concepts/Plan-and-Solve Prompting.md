---
type: concept
topic:
  - llm
  - reasoning
  - planning
status: seed
created: 2026-05-08
updated: 2026-05-21
source:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
  - "[[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models]]"
evidence:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#为什么收]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]"
  - "[[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models#需要我读的内容]]"
last_checked: 2026-05-10
freshness: stable
conflicts: []
related:
  - "[[Zero-shot CoT]]"
  - "[[Planning]]"
  - "[[Reasoning Trace]]"
  - "[[ReAct]]"
  - "[[ReWOO]]"
  - "[[Agent Loop]]"
  - "[[Agent Workflow]]"
  - "[[Evaluation]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
---

# Plan-and-Solve Prompting

## 一句话

Plan-and-Solve Prompting 是把 [[Zero-shot CoT]] 从“直接一步步想”改成“先生成计划，再按计划求解”的提示方法。

## 概念详解

Plan-and-Solve Prompting 是 prompt-era planning 的代表：它不先给示例，而是在问题前要求模型先生成解决计划，再按计划求解。它从 [[Zero-shot CoT]] 的经验出发，但指出“让我们一步步思考”仍可能遗漏关键步骤。Plan-and-Solve 的 plan 不是生产系统里的任务图，而是一次回答内部的结构化草稿：先列出要做哪些子步骤，再生成推理和答案。

论文证据主要支持三件事：第一，Zero-shot CoT 容易有 missing-step error；第二，先计划再求解能让模型更显式地覆盖必要步骤；第三，PS+ 通过更具体的指令降低计算、推理和语义理解错误。这个证据边界很重要：它说明 prompt 层的显式计划有价值，但不说明模型已经具备可靠执行、工具使用、状态持久化或失败恢复能力。

现代 Agent 系统吸收它时，通常把“先结构化任务”变成更硬的工程对象：任务列表、验收标准、依赖关系、state graph、planner-executor、replan 节点、human approval 或 evaluator。也就是说，Plan-and-Solve 是 [[Planning]] 的轻量入口：它帮助用户理解“先拆再做”的价值；但一旦任务需要外部世界反馈，就要升级到 [[ReAct]]、[[Agent Loop]] 或 [[Agent Workflow]]。

这张卡也帮助区分“计划作为推理脚手架”和“计划作为执行控制面”。Plan-and-Solve 的 plan 主要给同一次生成中的 solve 阶段使用，通常不会被外部系统单独保存、审查或重排；生产 Agent 的 plan 则可能变成任务队列、状态字段、依赖图、checkpoint 或人类审批材料。前者改善文本推理，后者约束真实行动。把这两层混在一起，会让人误以为 prompt 里出现 plan 就已经拥有了工程意义上的规划能力。

因此它的最佳学习用途，是作为从 CoT 到 Agent planning 的桥。你先看到“步骤显式化会减少遗漏”，再进一步看到“步骤必须被验证和更新”。如果停在第一层，就会高估 prompt 的力量；如果跨到第二层，就能理解为什么现代系统需要 state、tool result、evaluation 和 replan。
## 它解决什么问题

普通 [[Zero-shot CoT|Zero-shot Chain-of-Thought]] 常用 “Let's think step by step” 触发逐步推理，但模型可能漏掉关键步骤。

Plan-and-Solve 先要求模型生成 plan，相当于先搭一个任务骨架，再逐步填答案。这样尤其针对 missing-step error：不是算错某一步，而是根本没做某一步。

PS+ 进一步把提示词写得更明确，用额外 instruction 去压低计算错误、推理错误和语义误解。它的核心不是让模型“变成 Agent”，而是让一次回答里的推理过程更有结构。

## 它不是什么

Plan-and-Solve Prompting 不是 [[ReAct]]。

它没有外部 Action，也没有 [[Observation]] 反馈。它解决的是一次推理回答中的“先规划再求解”，不是 Agent 在环境中循环行动。

它也不是完整 [[Agent]] 框架。它不处理工具权限、状态持久化、失败重试、trace、评测或 human-in-the-loop。

更细一点：它不是“规划能力”的全部。这里的 plan 仍然只是模型输出的一段文本；如果计划错了、漏了，系统不会天然发现，也不会自动回滚或重试。

## 最小例子

```text
Question: 一道多步数学题

Prompt: 先制定解决计划，然后按计划一步步求解。

Plan:
1. 找出已知条件。
2. 写出需要计算的中间量。
3. 用中间量得到最终答案。

Solve:
按计划逐步计算，并给出答案。
```

## 常见误解

不要把“模型写了计划”直接等同于“模型真的会执行计划”。

计划文本本身也可能幻觉、漏项或过度抽象。没有工具反馈和评测时，它只是更有结构的 reasoning trace，不是可靠执行保证。

也不要把“强模型自己会思考”理解成“显式 plan 没价值”。强模型可能在内部完成部分规划，但当任务需要可检查的拆解、可复用的任务清单或人类确认时，显式 plan 仍然有工程价值。

## 边界细节

可以把它放在三层里理解：

- [[Reasoning Trace]] 层：计划和求解都还是模型生成的文本。
- [[Planning]] 层：它让规划出现在回答前，但规划不会随环境反馈动态更新。
- [[Agent Loop]] 层：它还没进入行动循环；一旦加入工具调用、观察反馈、状态保存和重试，才更接近 Agent。

和 [[ReAct]]、plan-and-execute workflow 的最小区别：

```text
Plan-and-Solve Prompting: Prompt -> Plan -> Solve -> Answer
ReWOO: Goal -> Planner(Plan/#E) -> Worker(Evidence) -> Solver(Answer)
ReAct: Thought -> Action -> Observation -> Thought -> ... -> Answer
Plan-and-execute workflow: Goal -> Plan -> Task list -> Execute -> Evaluate/Replan
```

和 [[ReWOO]] 的区别尤其适合校准“计划”这个词：Plan-and-Solve 的 plan 仍然是一次回答内部的文本脚手架；ReWOO 的 Planner 会预留 `#E` evidence slots，并让 Worker 调工具填 evidence，再由 Solver 汇总。也就是说，ReWOO 吸收了“先计划”的直觉，但已经进入工具增强推理；它不是纯 prompt-level plan-solve。

用户提供的 Planning Phase / Solving Phase 图里出现了 Task Agent、Exec、Loop 和 Replan。那张图更接近 plan-and-execute workflow：它把计划变成任务清单，并在执行阶段允许重新规划。它可以帮助理解 planning 的工程形态，但不要直接当成 Plan-and-Solve Prompting 论文方法本身。

![[plan-and-solve-planning-solving-phase.svg]]

## 现代性状态

- 判定：foundation / transitional
- 基础地基：先显式拆解任务再求解，是理解 [[Planning]]、[[Reasoning Trace]] 和 plan-first workflow 的稳定思想。
- 历史过渡：把 planning 完全写在 prompt 文本里，属于 prompt-era 轻量实现；它适合教学、单轮推理和低风险任务，不是现代 Agent runtime。
- 当前工程吸收：复杂系统会把 plan 转成 task graph、state、checklist、eval rubric 或 human-review artifact，再由执行层和 observation 校正。
- 易变部分：具体模型是否需要显式 plan、是否暴露推理链、如何在 API 中表达 reasoning / planning，会随模型和产品变化。

## 现代系统怎么吸收 Plan-and-Solve 的价值

现代 Agent 或复杂 LLM 应用通常不会只靠一句“先计划再求解”来托管长任务，而是把这个思想工程化：

- 对简单问题，不强制输出长 plan，避免把低成本问答变慢、变啰嗦。
- 对复杂任务，让模型先输出结构化计划，例如任务列表、依赖关系、验收标准或下一步动作。
- 对高风险任务，把 plan 放进显式 state，由框架、人类或 evaluator 先检查，再进入执行。
- 对执行中变化的任务，用 [[Agent Workflow]]、planner-executor、replan 节点或 [[Agent Loop]] 根据反馈更新计划。
- 对“计划写了但没照做”的问题，用 [[Evaluation]]、trace、单元测试、预算上限和停止条件检查实际轨迹，而不是只看计划文本。

所以它在今天更像一个可迁移的设计原则：先把任务结构显式化，再决定哪些部分由模型推理、哪些部分由框架执行和校验。

## 证据锚点

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#为什么收]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#图片录入：Planning Phase / Solving Phase]]
- Asset: `agentic learning/raw/assets/plan-and-solve-planning-solving-phase.svg`（根据用户截图重绘，2026-05-08；用于说明工程类比，不等同于论文原法）
- Evidence type: paper source note + user-provided visual asset + engineering analogy.
- Confidence: medium
- Boundary: 论文证据支持 prompt-level plan-then-solve；“Task Agent / Exec / Replan” 是工程类比，不应反向写成论文方法本身。

## 复习触发

- Plan-and-Solve 和 Zero-shot CoT 的最小差别是什么？
- 为什么 Plan-and-Solve 还不是 [[ReAct]] 或生产 Agent workflow？
- 给一个多步问题，指出哪些错误属于 missing-step error，哪些属于计算或语义误解。

## 相关链接

- [[Planning]]
- [[Zero-shot CoT]]
- [[Reasoning Trace]]
- [[ReAct]]
- [[ReWOO]]
- [[Agent Loop]]
- [[Agent Workflow]]
- [[Evaluation]]
- [[ReAct Plan-and-Solve Reflexion 对比]]
