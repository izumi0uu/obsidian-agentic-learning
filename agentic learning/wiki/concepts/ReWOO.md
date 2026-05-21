---
type: concept
topic:
  - agent
  - reasoning
  - planning
  - tool-use
status: seed
created: 2026-05-21
updated: 2026-05-21
last_checked: 2026-05-21
freshness: stable
conflicts: []
aliases:
  - Reasoning WithOut Observation
  - Reasoning Without Observation
source:
  - "[[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models]]"
  - "[[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations]]"
evidence:
  - "[[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models#需要我读的内容]]"
  - "[[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models#方法 / 机制]]"
  - "[[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#实验 / 证据]]"
related:
  - "[[ReAct]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[Observation]]"
  - "[[Tool Calling]]"
  - "[[Agent Loop]]"
  - "[[Agent Evaluation Benchmark]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
relations:
  - type: related_to
    target: "[[ReAct]]"
    note: "ReWOO 与 ReAct 都面向工具增强推理，但 ReAct 让 Observation 反馈驱动下一步，ReWOO 先规划 evidence slots 后取证。"
  - type: related_to
    target: "[[Plan-and-Solve Prompting]]"
    note: "ReWOO 保留先计划再求解的直觉，但加入 Worker 工具取证；不是纯 prompt-level plan-solve。"
  - type: related_to
    target: "[[Observation]]"
    note: "ReWOO 的核心边界就是限制 observation 对 planner reasoning 的中途回流。"
---

# ReWOO

## 一句话

ReWOO 是 Reasoning WithOut Observation：先让 Planner 一次性规划 `Plan / #E` 证据槽，再让 Worker 调工具填证据，最后由 Solver 综合答案的工具增强推理范式。

## 概念详解

ReWOO 出现的背景，是早期工具增强语言模型常用 [[ReAct]] 式交替循环：模型先想一步，发出 Action，工具返回 [[Observation]]，再把前面的 prompt、示例、reasoning trace、action 和 observation 全部喂回模型，让模型继续下一步。这个模式直观、灵活，但每一步都可能重复大量历史上下文，尤其在黑盒 API / stateless 调用里会带来 token 成本和延迟。

ReWOO 的思路是把“什么时候推理”和“什么时候看工具结果”拆开。Planner 先根据任务写出一组互相关联的计划，并预留 `#E1`、`#E2` 这样的 evidence slots；Worker 按这些槽位调用工具或检索系统，把真实 evidence 填进去；Solver 最后读原任务、计划和 evidence，合成答案。它不是拒绝外部信息，而是让 Planner 不在每一步工具返回后继续改写下一步 reasoning。

这张卡最值得学的地方，不是“ReWOO 比 ReAct 更好”这种排名判断，而是 observation feedback 的边界判断：如果任务的证据需求可以在一开始大致列出，先规划证据槽能减少重复 prompt，并把取证流程结构化；如果任务需要根据工具结果临时改变路线、处理失败、定位页面状态、读取几何/图像/数据库中间结果，过早锁定计划就可能损伤可靠性。

所以 ReWOO 是 [[ReAct]]、[[Plan-and-Solve Prompting]] 和现代 planner-executor workflow 之间的一张桥接卡。它继承 Plan-and-Solve 的“先拆任务”直觉，又比 Plan-and-Solve 多了工具取证；它和 ReAct 一样关心工具增强任务，但把 observation 从“每步反馈给下一步思考”降级成“填充预先规划的 evidence slots”。现代系统可以吸收它的分层思想，但通常还要加上 typed tool calls、state、trace、budget、replan、evaluator 和权限边界。

## 它解决什么问题

ReWOO 主要解决 observation-dependent 工具增强推理里的 prompt redundancy 和模块混杂问题。

在 ReAct 式循环里，每一次工具调用后，模型常常要重新接收完整上下文，才能继续生成下一步。对于可预判证据需求的任务，这会重复消费 token，也让 reasoning、tool execution 和 final synthesis 混在一条长轨迹里。ReWOO 用 Planner / Worker / Solver 拆层，让计划、取证、合成各自承担更清晰的责任。

它也帮助学习者看到一个成本-反馈权衡：中途 observation feedback 很贵，但它也很有价值。ReWOO 的价值不在于消灭 observation，而在于提醒我们：有些任务可以把 observation 延后到 evidence filling 和 final solve，有些任务必须让 observation 驱动下一步行动。

## 它不是什么

ReWOO 不是“不用工具”。Worker 仍然会调用外部工具、检索知识或收集 evidence；“without observation”指的是 Planner 的 reasoning 不在每一步 observation 之后继续展开。

ReWOO 不是 [[ReAct]]。ReAct 的核心是 Thought / Action / Observation 的交替循环，Observation 会影响当前 trajectory 的下一步；ReWOO 的核心是先写完整 blueprint，再填 evidence，再 solve。

ReWOO 也不是纯 [[Plan-and-Solve Prompting]]。Plan-and-Solve 主要是单次回答里的 prompt-level plan 和 solve；ReWOO 多了 Worker 工具取证和 evidence slots。

它更不是完整生产级 [[Agent Framework]]。它不天然处理工具权限、schema 校验、状态持久化、失败重试、trace、人工审批、成本预算或 benchmark 复现。

## 最小例子

```text
Question: 某电影的导演出生在哪个城市？

Planner:
Plan 1: 找到电影导演。#E1
Plan 2: 查询 #E1 的出生城市。#E2

Worker:
#E1 = Search[电影导演] -> 导演 A
#E2 = Search[导演 A 出生地] -> 城市 B

Solver:
根据计划和 #E1 / #E2，回答：城市 B。
```

如果用 ReAct，同一个任务可能是“查导演 -> 读 observation -> 决定查出生地 -> 读 observation -> 回答”。如果用 ReWOO，查询链条在一开始就被写成 evidence slots。

## 常见误解

不要把 ReWOO 理解成“没有观察反馈就更高级”。它节省的是多轮交替提示成本，代价是减少了中途根据 observation 改计划的机会。

也不要把 ReWOO 当成所有 RAG / Agent 任务的默认模式。很多真实任务的下一步取决于上一轮工具结果：网页状态、API 错误、检索结果质量、地理数据中间产物、测试失败信息、用户确认，都可能要求动态 replan。

另一个误解是把 `#E` 当成长期记忆。`#E` 只是当前任务蓝图里的证据槽，服务 final Solver；它不是跨任务 memory，也不是可审计 trace 的全部。

## 边界细节

最小边界可以这样切：

```text
Plan-and-Solve: Question -> Plan -> Solve -> Answer
ReAct: Goal -> Thought -> Action -> Observation -> next Thought/Action -> Answer
ReWOO: Goal -> Planner(Plan/#E) -> Worker(Evidence) -> Solver(Answer)
```

ReWOO 适合的条件：

- 证据需求能提前拆出来，例如多跳问答、固定检索链、可列举的子问题。
- 工具返回主要是填空式 evidence，而不是改变任务路线的状态反馈。
- 成本、延迟或上下文重复是主要瓶颈。
- Solver 有足够能力检查 evidence 是否支持最终答案。

ReWOO 不适合的条件：

- 每一步工具结果会显著改变下一步策略。
- 工具经常失败、返回歧义结果或需要参数修正。
- 任务依赖中间图像、几何、数据库状态、页面状态、测试输出等强反馈。
- 安全/权限要求必须在每一步 action 前动态审查。

DORA 的 scaffold ablation 是一个很好的反面证据：在灾害响应这种数据密集、几何和中间 masks 驱动的任务里，作者报告 ReWOO 相比 ReAct 明显掉分，并解释为移除 observation feedback 会伤害这类任务。这不推翻 ReWOO 的价值，但说明它的适用边界很窄、很任务相关。

## 现代性状态

- 判定：transitional / current-practice-adjacent。
- 稳定价值：把计划、取证和合成拆开，能帮助理解 planner-executor、evidence assembly、research workflow 和 cost-aware tool use。
- 历史过渡：作为单一 prompting scaffold，它属于早期 ALM / prompt-era 的模块化探索；不能直接等同于今天的生产 Agent runtime。
- 当前工程吸收：现代系统会把 ReWOO 的蓝图思想做成 task graph、evidence schema、retrieval plan、batch tool calls、parallel search、trace 和 final synthesis prompt。
- 易变部分：具体 benchmark 上 ReWOO 是否优于 ReAct，取决于模型、工具、任务反馈结构、成本模型和失败恢复机制。

## 现代系统怎么吸收 ReWOO 的价值 / 局限

现代系统最应该吸收的是它的“证据槽先行”思想，而不是照搬“without observation”。

对 deep research、RAG 或多跳问答，可以先生成 evidence plan：需要哪些事实、每个事实去哪类 source 查、哪些证据必须互相校验。然后系统可以并行检索、填充 evidence table，最后由 answer synthesizer 写答案。这是 ReWOO 的强项。

对 coding agent、browser agent、computer-use agent、数据分析 agent，则不能轻易移除中途 observation。测试失败、页面变化、工具报错、权限确认、文件 diff、用户补充输入都必须回到下一步决策。现代 harness 通常会保留 action-observation loop，同时把部分可预测子任务批处理或计划化。

工程上更稳的吸收方式是：先让 Planner 产出可审查计划和 evidence slots；执行层用 [[Tool Calling]]、schema、permission、trace 和 retry 去填 evidence；如果 evidence 与计划不匹配，触发 replan 或人工确认；最后 Solver 只在 evidence 足够时合成答案。也就是说，ReWOO 的价值被吸收到 workflow / harness，而不是取代 workflow / harness。

## 证据锚点

- Source: [[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models]]
- Source: [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations]]
- Anchor: [[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models#需要我读的内容]]
- Anchor: [[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models#方法 / 机制]]
- Anchor: [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#实验 / 证据]]
- Evidence type: paper source note + frontier benchmark source note + engineering synthesis.
- Confidence: medium-high for ReWOO mechanism; medium for modern engineering absorption and task-boundary judgment.
- Boundary: ReWOO 论文支持 Plan-Work-Solve / Planner-Worker-Solver 机制；DORA 支持“移除 observation feedback 在某些数据密集 benchmark 会伤害表现”的边界反例；现代系统吸收方式是跨卡工程综合。

## 复习触发

- 为什么 ReWOO 不是“不用工具”？
- 用一句话说明 ReWOO 和 [[ReAct]] 在 Observation 反馈上的最小区别。
- 什么时候应该用 ReWOO 式 evidence slots，什么时候必须保留 action-observation loop？
- ReWOO 为什么比 [[Plan-and-Solve Prompting]] 多一层 Worker / evidence？

## 相关链接

- [[ReAct]]
- [[Plan-and-Solve Prompting]]
- [[Observation]]
- [[Tool Calling]]
- [[Agent Loop]]
- [[Agent Evaluation Benchmark]]
- [[ReAct Plan-and-Solve Reflexion 对比]]
