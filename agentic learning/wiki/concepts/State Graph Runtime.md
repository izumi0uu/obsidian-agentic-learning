---
type: concept
topic:
  - agent
  - framework
  - workflow
  - runtime
status: growing
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: watch
source:
  - "[[LangGraph 官方文档]]"
  - "[[Google ADK 官方文档]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
evidence:
  - "[[LangGraph 官方文档#一句话]]"
  - "[[LangGraph 官方文档#边界提醒]]"
  - "[[Google ADK 官方文档#必读块 2：scale / evaluation / deployment / context]]"
  - "[[Agent Framework 全量选型对比 2026-05#全量对比表]]"
related:
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Durable Execution]]"
  - "[[Human-in-the-loop]]"
  - "[[LangGraph]]"
---

# State Graph Runtime

## 一句话

State Graph Runtime 是把 Agent / workflow 的执行过程显式建模为“状态 + 节点 + 边 + 路由 + checkpoint”的运行时，让长任务可以循环、分支、暂停、恢复和审计。

## 概念详解

State Graph Runtime 出现，是因为自然语言 prompt loop 很难稳定表达复杂控制流。一个 Agent 可能需要先检索资料、再调用工具、遇到高风险动作时暂停等待人工确认、失败后重试、完成后把中间结果写回状态。如果这些步骤只靠模型在上下文里“记住”，调试和恢复都会很脆弱。

图运行时把这些隐含责任拆成工程对象：state schema 记录当前任务数据，node 执行一段模型调用或工具逻辑，edge / router 决定下一步，checkpoint 保存可恢复点，human-in-the-loop 节点允许人工插入判断。[[LangGraph 官方文档]] 的 source note 明确把 LangGraph 概括为低层 agent orchestration runtime，用状态图组织长任务 Agent，并把节点、边、状态、持久化、human-in-the-loop 和 durable execution 变成显式工程对象。[[Google ADK 官方文档]] 也把 graph-based workflows 放在生产 Agent 路线里，说明图/工作流化已经成为现代 Agent 工程的重要吸收方式。

工程综合：State Graph Runtime 的关键不是“画图看起来高级”，而是把“下一步怎么走”和“失败后从哪里恢复”从 prompt 软约束变成可测试、可审计的 runtime 规则。

## 它解决什么问题

- 长任务中间状态散落在对话上下文里，难以恢复。
- 工具调用、人工审批、重试、分支和终止条件靠 prompt 约定，容易失控。
- 线上失败后只能看日志，很难重放具体路径。
- 多 Agent / 多工具流程没有统一状态边界，容易互相污染。

## 它不是什么

- 不是图数据库。这里的 graph 是执行控制图，不是知识图谱或向量索引。
- 不是 UI 流程图。图只是外显表示，真正关键是 runtime 如何保存 state、执行 node、路由 edge 和恢复 checkpoint。
- 不是所有 Agent 都必须使用的底层。固定步骤的简单任务用普通函数或传统 workflow 可能更合适。

## 最小例子

```text
State: {question, retrieved_docs, draft, approved?}
node retrieve -> update retrieved_docs
node draft_answer -> update draft
edge if risky -> human_approval
edge if approved -> final
checkpoint after each node
```

这个例子里，模型不是自由决定所有步骤；它只在节点内完成局部判断，整体路径由图和状态约束。

## 常见误解 / 风险

- 误解：用了 graph 就自动可靠。风险是节点逻辑、状态 schema、工具幂等和错误处理仍然可能很差。
- 误解：所有业务流程都要建成复杂图。风险是简单任务被过度工程化，调试成本上升。
- 风险：state schema 设计不清，会让上下文投影、长期记忆和运行态状态混在一起。

## 边界细节

State Graph Runtime 最适合需要循环、分支、恢复、审批、长任务和审计的场景。它和 [[Agent Workflow]] 的关系是：workflow 是路径/任务结构，runtime 是执行和恢复这条路径的软件层；它和 [[Agent State]] 的关系是：state 是数据，runtime 负责何时读取、更新、保存和投影这些数据。

与 provider SDK 的差异：OpenAI Agents SDK 等可以封装 Agent、tools 和 handoffs，但不一定要求你显式画状态图；State Graph Runtime 更强调控制流和状态恢复。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 稳定部分：显式 state、node、edge、checkpoint、human-in-the-loop 是现代 Agent framework 共同吸收的工程方向。
- 易变部分：具体 API、部署平台、checkpoint store、graph 可视化和云托管能力。

## 现代系统怎么吸收 State Graph Runtime 的价值 / 局限

现代系统通常把高风险或长周期任务放进 state graph：把确定步骤固定成节点/边，把不确定判断局限在某些模型节点，把危险动作接到 approval gate，把每一步写入 trace。局限是图运行时只能提供控制结构，不会自动给出正确业务策略、评测集或安全权限模型。

## 证据锚点

- [[LangGraph 官方文档#一句话]]：LangGraph 作为低层 state graph / orchestration runtime 的来源。
- [[LangGraph 官方文档#边界提醒]]：LangGraph 与 Deep Agents harness 的分层边界。
- [[Google ADK 官方文档#必读块 2：scale / evaluation / deployment / context]]：graph workflows 作为生产 Agent 路线的一部分。
- [[Agent Framework 全量选型对比 2026-05#全量对比表]]：把 LangGraph / Google ADK 等放在状态与流程维度比较。

## 复习触发

1. 为什么 state graph runtime 解决的是“恢复和控制流”问题，而不是“模型更聪明”问题？
2. 给一个退款审批 Agent，哪些步骤应该写成节点和边？哪些判断可以留给模型？
3. State Graph Runtime 和普通 workflow engine 的差异在哪里？

## 相关链接

- [[Agent Workflow]]
- [[Agent State]]
- [[Durable Execution]]
- [[Human-in-the-loop]]
- [[LangGraph]]
- [[Agent Framework 全量选型对比 2026-05]]
