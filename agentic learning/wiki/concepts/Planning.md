---
type: concept
topic:
  - agent
  - planning
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[LangGraph 官方文档]]"
evidence:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#为什么收]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]]"
  - "[[Anthropic - Building Effective Agents#边界提醒]]"
  - "[[LangGraph 官方文档#一句话]]"
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

## 概念详解

Planning 在 Agent 学习里不是“写一个好看的 todo list”，而是把目标、约束、依赖、风险和停止条件显式化，让系统知道下一步为什么要做、什么时候要改计划。它出现的原因很简单：很多任务的答案不在初始上下文里，需要先拆解，再通过工具、检索、测试或用户反馈逐步逼近结果。如果没有 planning，Agent 容易在复杂任务里跳步、遗漏依赖、提前宣布完成，或者在失败后不知道从哪里恢复。

不同来源支持的是 planning 的不同层次。[[Plan-and-Solve Prompting]] 证明了 prompt 层“先计划再求解”可以减少 missing-step error，但它仍是一轮文本推理；[[ReAct]] 把推理和外部 action / observation 交替起来，让计划能被环境反馈修正；Anthropic 的 workflow vs agent 边界提醒我们：不是所有任务都需要自主规划，稳定路径应该优先固定成 workflow；LangGraph 这类框架则把 planning 结果放进 graph/state/edge，使它能和执行、replan、checkpoint、human approval 连接。

因此 Planning 更像一组工程问题，而不是单个 prompt 技巧：计划由谁生成？计划是否结构化？计划是否进入 state？执行中 observation 是否会改变计划？什么条件说明计划完成或失效？谁有权批准高风险步骤？这些边界决定了 planning 是学习辅助、一次性推理草稿，还是生产 Agent 的控制结构。

对学习者有用的小边界是：planning 不是越早越完整越好，而是要和不确定性匹配。信息充分、路径稳定时，计划可以变成固定 workflow；信息不足、环境会变化时，计划应该保留 replan 入口；风险高时，计划需要被人或 evaluator 审查后再执行。于是 planning 的质量不只看“步骤是否清楚”，还要看它是否标出依赖、证据缺口、失败恢复、验证方式和停止条件。

在复盘失败时，可以问四个问题：计划是否覆盖了必要子目标，是否把未知信息标出来，是否把验证放在执行后面，是否允许根据 observation 改变路线。若答案是否定的，问题往往不在模型“不会规划”，而在系统没有把计划变成可检查、可更新的对象。
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

## 常见误解 / 风险

- 误解：计划越长越可靠。实际长计划可能只是把错误拆得更细，反而增加执行负担。
- 误解：模型写出计划就等于会执行计划。没有 state、tool result、测试或 evaluator，计划不会自动校正。
- 误解：所有 Agent 都要先完整规划。探索性任务可能需要边做边观察，过早固定计划会错过反馈。
- 风险：计划没有验收标准，Agent 会把“完成步骤”误当成“完成目标”。

## 边界细节

Planning 至少有三种层次：prompt-level planning（先写计划再回答）、runtime planning（把计划写入 state 并驱动执行）、organizational planning（把任务分给多个 agent / worker / human）。本卡主要讨论前两者。

和相邻概念的区别：[[Plan-and-Solve Prompting]] 是提示方法；[[ReAct]] 是 reasoning/action/observation 交替；[[Agent Workflow]] 是把步骤、分支、循环、审批和 handoff 固化成可运行结构；Planning 是这些结构里关于“目标如何分解、顺序如何决定、何时重规划”的能力。

反例：一个静态 checklist 不一定是有效 planning；如果它不接收 observation、不包含停止条件，也不能在失败后调整，只是任务描述。

## 现代性状态

- 判定：foundation / current-practice
- 稳定部分：复杂任务需要显式分解、依赖管理、检查点和停止条件；计划应能被反馈修正。
- 历史过渡：只靠 prompt 写“先制定计划”属于早期或轻量方法，适合学习和简单推理，但不能替代运行时控制。
- 当前工程实践：现代 Agent 通常把 planning 放进 workflow、state graph、planner-executor、replan 节点、eval harness 或 human approval。
- 易变部分：具体框架如何表达 plan、task graph、checkpoint 和 replan API 会变化；概念边界本身相对稳定。

## 证据锚点

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Source: [[Anthropic - Building Effective Agents]]
- Source: [[LangGraph 官方文档]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#为什么收]], [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]], [[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]], [[Anthropic - Building Effective Agents#边界提醒]], [[LangGraph 官方文档#一句话]]
- Evidence type: prompting paper source note + agent pattern source note + official/practice docs + engineering synthesis.
- Confidence: medium
- Boundary: Plan-and-Solve 证据支持 prompt-level planning；runtime/state/workflow 部分来自现代工程来源和本 vault 的综合理解。

## 复习触发

- 为什么“先写计划”不等于“计划会被执行”？缺了哪些 runtime 结构？
- 给一个测试失败任务，写出 plan、observation、replan、stop condition 四个部分。
- 什么时候应该用固定 workflow，而不是让 Agent 自主 planning？

## 相关链接

- [[Agent]]
- [[Agent Loop]]
- [[Evaluation]]
- [[Plan-and-Solve Prompting]]
- [[ReAct]]
