---
type: map
topic:
  - agent
  - workflow
  - protocol
  - multi-agent
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Multi-agent Orchestration]]"
  - "[[Handoff]]"
  - "[[A2A]]"
  - "[[ACP]]"
  - "[[MCP]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent2Agent Protocol]]"
  - "[[Agent Communication Protocol]]"
  - "[[Model Context Protocol 官方文档]]"
  - "[[Oh My Codex Repo]]"
evidence:
  - "[[Multi-agent Orchestration#证据锚点]]"
  - "[[Handoff#证据锚点]]"
  - "[[A2A#证据锚点]]"
  - "[[ACP#证据锚点]]"
  - "[[MCP#证据锚点]]"
  - "[[Agent Workflow#证据锚点]]"
  - "[[Durable Execution#证据锚点]]"
related:
  - "[[Agent 主题]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Handoff]]"
  - "[[A2A]]"
  - "[[ACP]]"
  - "[[MCP]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent Framework]]"
  - "[[Agent Harness]]"
  - "[[Tool Registry]]"
  - "[[Policy Engine]]"
---

# Multi-agent Handoff Protocol 对比

## 一句话总览

这页区分多 Agent 协作里最容易混在一起的三层：[[Multi-agent Orchestration]] 是一个任务内部的分工、调度、集成和验证；[[Handoff]] 是控制权、上下文和责任从一个执行者转给另一个执行者；[[A2A]] / [[ACP]] / [[MCP]] 是跨边界通信或工具连接协议；[[Agent Workflow]] 和 [[Durable Execution]] 则是让这些协作可控、可恢复的运行结构。

最小边界：orchestration 是“谁和谁怎样协作”；handoff 是“什么时候交给谁”；A2A / ACP 是“Agent 服务之间怎样通信”；MCP 是“Agent 应用怎样连接工具和上下文服务”；workflow / durable execution 是“这条协作链怎样被约束和恢复”。

## 为什么这组值得对比

- 混淆风险高：社区讨论里常把“多个 Agent”“handoff”“A2A”“MCP server”“agent workflow”统称为 multi-agent。
- 共同问题域清楚：它们都围绕“一个执行者不够时，能力、任务、状态、工具和责任如何跨边界移动”。
- 介入点不同：有的是组织模式，有的是交接动作，有的是协议边界，有的是本地 workflow / runtime 能力。
- 证据密度足够：相关概念卡已经分别锚到 OMX、本地工程主源、OpenAI Agents SDK、A2A / ACP / MCP source note 和 durable execution source note。
- 工程价值高：分清这组概念能避免把“协议互操作”误当成“任务编排质量”，或把“工具连接”误当成“远端 Agent 协作”。

边界：这页不是 A2A / ACP / MCP 规格说明，也不判断协议生态胜负；具体字段和版本属于 volatile source note 范围。

## 共同问题域

共同问题是：Agent 系统经常需要把工作交给另一个能力边界。这个边界可能是同一进程里的专业 agent、同一 workflow 里的人工审批节点、远端 Agent 服务、MCP server 暴露的工具、或等待 24 小时后恢复的 durable step。

```text
local task goal
  -> orchestration decides roles / ownership / validation
  -> workflow chooses fixed path, branch, handoff or approval
  -> handoff transfers responsibility + context + permitted tools
  -> protocol boundary may be A2A / ACP / MCP / ordinary API
  -> durable execution preserves task state, retries and resume points
```

它们适合一起对比，是因为“协作成功”不是由单一协议保证，而是由组织分工、交接上下文、权限边界、通信协议、状态恢复和验证闭环共同决定。

## 核心区别表

| 概念 | 主要介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Multi-agent Orchestration]] | 多 Agent / 多 worker 的任务切分、调度、通信、集成和验证 | 任务开始前切分，执行中协调，结束时集成验证 | 总目标、角色、ownership、任务状态、验证标准 | worker lane、进度/阻塞报告、整合结果 | [[Multi-agent Orchestration#证据锚点]] |
| [[Handoff]] | 控制权、上下文和责任主体迁移 | workflow / loop 中某个节点触发；可能临时委托或完全转交 | 交接原因、必要上下文、接收方权限、当前 state | 新执行者接管、trace 记录、返回结果或升级 | [[Handoff#证据锚点]] |
| [[A2A]] | Agent 与 Agent 之间的跨系统互操作 | 当远端能力本身是 Agent、会处理任务状态或流式进度时 | agent card / 能力发现、任务、消息、状态 | 远端 Agent 的状态、消息、artifact、追问或结果 | [[A2A#证据锚点]] |
| [[ACP]] | Agent 服务、应用和人之间的标准化消息通信 | Agent 被服务化、需要同步/异步/streaming/多模态交互时 | 应用请求、用户输入、消息、任务生命周期 | 标准化消息、进度、结果、可能的用户补充请求 | [[ACP#证据锚点]] |
| [[MCP]] | AI 应用连接工具、资源、prompt 和上下文服务的协议 | 模型调用工具之前：host/client 发现并暴露能力；执行时返回工具结果 | server tools/resources/prompts、schema、host 权限策略 | 可调用工具/资源能力、工具 observation | [[MCP#证据锚点]] |
| [[Agent Workflow]] | 本地任务路径、分支、循环、approval、handoff 的运行结构 | 贯穿协作路径，决定何时走固定步骤、模型节点或交接节点 | 输入、state、路由规则、风险条件、审批条件 | 下一节点、handoff、停止、重试或人工等待 | [[Agent Workflow#证据锚点]] |
| [[Durable Execution]] | 长任务暂停、恢复、重试、checkpoint、副作用边界 | 跨时间、跨进程、跨失败；尤其在长任务和 human-in-the-loop 中 | workflow state、event log、idempotency key、人工等待点 | 恢复点、可安全重试/不可重试判断、继续执行 | [[Durable Execution#证据锚点]] |

## 最容易混淆的边界

- [[Multi-agent Orchestration]] vs [[A2A]]：orchestration 是任务组织和验证模式；A2A 是跨系统 Agent 互操作协议。没有 ownership、集成权威和验证路径，使用 A2A 也只是会通信，不等于可靠编排。
- [[Handoff]] vs [[A2A]] / [[ACP]]：handoff 是控制权或责任迁移的模式；A2A / ACP 可能承载跨系统 handoff，但 handoff 也可以完全发生在同一个框架、同一个 workflow 或人类审批节点里。
- [[MCP]] vs [[A2A]]：MCP 连接工具、资源和上下文服务；A2A 连接有任务处理能力和状态语义的 Agent。如果对方只是函数或数据源，更像 MCP/API；如果对方会持续处理任务、返回状态或追问，更像 A2A。
- [[ACP]] vs [[A2A]]：两者都关心 Agent 通信，但 ACP 更强调 Agent 服务 / 应用 / 人之间的消息和长任务交互入口；A2A 更强调 Agent-to-Agent 互操作。两者生态边界仍在变化，不宜背字段。
- [[Agent Workflow]] vs orchestration：workflow 是可执行路径；orchestration 是多个执行者如何被组织和收敛。单 Agent 也可以有 workflow，多 Agent 也可能没有好 orchestration。
- [[Durable Execution]] vs handoff：durable execution 让任务跨失败和等待继续；handoff 让责任主体改变。一个 24 小时人工审批节点常同时需要两者。

## 执行时序 / 机制差异

```text
1. Orchestrator / leader 判断任务是否需要多执行者，并定义 ownership、共享事实来源和验证标准。
2. Agent Workflow 把任务写成节点、分支、approval gate、handoff 和停止条件。
3. 某个节点触发 handoff：只传必要上下文、交接原因、接收方权限和当前 state。
4. 如果接收方是远端 Agent，可通过 A2A / ACP / 普通 API 交互；如果接收方是工具或数据源，可通过 MCP / API 接入。
5. Durable Execution 保存 checkpoint、event log、idempotency key 和等待点，防止长任务或副作用操作丢失边界。
6. Trace / evaluation / leader integration 判断协作结果是否满足任务，而不是只相信某个子 Agent 的局部报告。
```

这个机制强调：协议只解决“能连接”和“怎样表达任务/工具”，不自动解决“该不该交接”“交给谁”“权限是否过宽”“结果是否可信”“失败后能不能恢复”。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或协议证据。

把一次多 Agent 任务想成“医院会诊”：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Multi-agent Orchestration]] | 主治医生安排科室分工、会诊顺序和最终诊断责任 | 协调质量不由人数保证 |
| [[Handoff]] | 从急诊转给专科，并附上病历、原因和权限 | 转诊不等于所有资料无限共享 |
| [[A2A]] | 两家医院的医生系统能传递会诊任务和状态 | 协议能通信，不保证诊断正确 |
| [[ACP]] | 医院 App、患者和医生之间的标准消息 / 进度通道 | 服务消息不等于临床决策本身 |
| [[MCP]] | 医生系统接入检验、影像、药品库等工具/数据源 | 工具连接不等于另一个医生 |
| [[Agent Workflow]] | 挂号、检查、会诊、审批、治疗的流程 | 流程可以含人工判断和异常分支 |
| [[Durable Execution]] | 病历、医嘱和预约让治疗跨天继续 | 持久化不保证决策正确 |

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[Multi-agent Orchestration]] 支持：可靠协作需要任务切分、通信协议、集成权威和验证路径，而不只是多个 Agent 并行。
- [[Handoff]] 支持：交接要带交接原因、必要上下文和接收方权限；否则会导致上下文丢失或权限过宽。
- [[A2A]] / [[ACP]] 支持：Agent 通信协议关注任务、消息、长任务状态、streaming、发现和互操作，但具体字段属于 volatile 层。
- [[MCP]] 支持：MCP 是工具、资源、prompt 和上下文服务连接层，不替代 Agent 框架、多 Agent 编排或安全策略。
- [[Agent Workflow]] / [[Durable Execution]] 支持：协作链需要可执行路径、checkpoint、重试、等待人工和副作用边界。

### 工程综合 / inference

现代多 Agent 系统通常会把本地协作用 workflow 和 state 管住，把跨 Agent 边界交给 handoff / A2A / ACP，把工具边界交给 MCP / tool registry，把长任务交给 durable execution，把最终可信度交给 trace、evaluation 和 leader/human integration。这个分层是工程综合，不是某一个协议的完整声明。

### 仍需警惕的外推

A2A、ACP、MCP 的生态、版本和安全实践变化快。概念层应保留“对象边界”：Agent-to-Agent、Agent-service messaging、tool/context connection；不要把当下字段、registry 状态或供应商实现写成长期稳定事实。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 需要多个 worker 分头处理不同文件/证据 | [[Multi-agent Orchestration]] | 核心是 ownership、进度、冲突和最终验证 | 没有集成权威会局部正确、整体冲突 |
| 一个 triage agent 要把账单问题交给 billing agent | [[Handoff]] | 控制权、上下文和工具权限发生迁移 | 交接上下文过多或过少都会出错 |
| 本地 Agent 要委托远端“能自己处理任务”的 Agent | [[A2A]] | 对方有 Agent 能力、任务状态和可能的长任务语义 | 不要把普通函数包装成 Agent |
| UI / 应用 / 人要和 Agent 服务进行长任务消息交互 | [[ACP]] | 关注消息、streaming、任务生命周期和服务化入口 | 具体生态仍 volatile，需要按日期复查 |
| Agent 要连接文件系统、数据库、浏览器或 SaaS 工具 | [[MCP]] | 对象是工具/资源/context server，不是另一个 Agent | 连接越容易，越需要 permissioning 和审计 |
| 协作路径需要审批、分支、重试或人工节点 | [[Agent Workflow]] | 这是执行路径设计问题 | 不要让模型在 prompt 里临时决定所有路径 |
| 长任务可能中断、等待审批或有副作用重试 | [[Durable Execution]] | 需要 checkpoint、event log 和副作用边界 | 盲目 replay 可能重复执行不可逆动作 |

## 它们共同不是什么

- 都不是“多个聊天机器人互相说话就能解决问题”。可靠协作需要 ownership、权限、状态、trace、evaluation 和集成权威。
- 都不是安全保证。协议连接、handoff 和 workflow 仍需要身份、权限、least privilege、approval gate、sandbox 和 audit。
- 都不是模型能力本身。它们组织、连接或恢复能力，但不能替代任务理解、证据质量和结果验证。
- 都不是长期稳定 API 记忆题。尤其 A2A / ACP / MCP 的字段和生态需要回到 source note 的 `last_checked` 复查。

## 证据锚点

- Concept anchors: [[Multi-agent Orchestration#证据锚点]], [[Handoff#证据锚点]], [[A2A#证据锚点]], [[ACP#证据锚点]], [[MCP#证据锚点]], [[Agent Workflow#证据锚点]], [[Durable Execution#证据锚点]]。
- Source examples: [[Oh My Codex Repo]], [[Agent 工程基础设施主源]], [[OpenAI Agents SDK 文档]], [[Agent2Agent Protocol]], [[Agent Communication Protocol]], [[Model Context Protocol 官方文档]], [[Model Context Protocol Python SDK Repo]], [[MCP Tool Poisoning Threat Model]]。
- Evidence type: concept-card synthesis + source/docs notes + engineering synthesis + learning analogy.
- Confidence: medium for protocol boundary because A2A / ACP / MCP ecosystems are volatile; medium-high for orchestration / handoff / workflow responsibility boundaries.
- Boundary: 本页只使用现有 concept/source note 锚点，不新增协议事实；学习类比不是来源证据；MCP 同时涉及 worker-2 的工具接口主题，本页只在 protocol/coordination 边界内使用它。

## 复习触发

1. 为什么使用 A2A 不自动等于有好的 Multi-agent Orchestration？
2. 给一个例子说明 handoff 和 tool call 的区别。
3. 如果远端能力只有一个同步函数返回结果，它更像 MCP/API 还是 A2A？如果它会持续处理任务并流式回报呢？
4. 一个长任务在人工审批后恢复执行，workflow、handoff 和 durable execution 分别承担什么？
5. MCP 为什么会让 tool permissioning 和 tool poisoning 风险更重要，而不是更不重要？

## 相关链接

- [[Agent 主题]]
- [[Multi-agent Orchestration]]
- [[Handoff]]
- [[A2A]]
- [[ACP]]
- [[MCP]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Agent Framework]]
- [[Agent Harness]]
- [[Tool Registry]]
- [[Tool Permissioning]]
- [[Policy Engine]]
- [[Trace]]
- [[Evaluation]]
