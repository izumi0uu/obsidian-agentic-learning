---
type: concept
topic:
  - agent
  - framework
  - workflow
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Agent 工程基础设施主源#Agent 框架和编排]]"
  - "[[Agent 工程基础设施主源#本次判断]]"
  - "[[Anthropic - Building Effective Agents#一句话]]"
  - "[[Anthropic - Building Effective Agents#边界提醒]]"
  - "[[OpenAI - A Practical Guide to Building Agents#一句话]]"
  - "[[LangGraph 官方文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
related:
  - "[[Agent]]"
  - "[[Agent Harness]]"
  - "[[Tool Calling]]"
  - "[[Handoff]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Guardrails]]"
  - "[[Trace]]"
---

# Agent Framework

## 一句话

Agent Framework 是帮助开发者构建、编排、运行和观测 Agent 的软件框架：它把工具、状态、流程、交接、护栏、追踪和恢复做成可复用工程抽象。

## 它解决什么问题

真实 Agent 不只是“模型 + prompt”。它需要注册工具、校验参数、保存运行状态、处理分支和循环、等待人工确认、恢复长任务、记录 trace、评估结果，并把危险动作限制在权限边界内。

Agent Framework 解决的是这些工程责任的重复建设问题：与其每个项目都手写工具解析、状态管理、重试、handoff 和观测，不如用框架提供的抽象把它们组合起来。代表生态包括 LangGraph、LlamaIndex、Semantic Kernel、AutoGen、CrewAI、OpenAI Agents SDK、Pydantic AI、Mastra、Vercel AI SDK 等。

## 它不是什么

Agent Framework 不是 [[Agent]] 本身。框架提供运行结构，Agent 是围绕目标行动的系统；一个框架可以承载很多不同 Agent，也可能只被用来搭普通 workflow。

Agent Framework 也不是模型能力本身。换成更强模型不能自动替代权限、状态、trace、重试和评估；换框架也不能自动解决需求不清、工具危险、评估缺失或上下文污染。

它也不等于 [[Agent Harness]]。Framework 偏开发抽象和编排能力；harness 偏运行时外壳、权限、沙箱、审计、停止条件和产品化治理。实际系统里两者常重叠。

## 最小例子

```text
define agent
-> register tools and schemas
-> define state / workflow
-> run loop or graph
-> checkpoint / recover if needed
-> trace calls and tool results
-> evaluate final result and risky trajectory
```

这个例子不是说每个项目都要上完整框架，而是说明框架通常接管哪些原本散落在 prompt、脚本和日志里的责任。

## 框架怎样接管 prompt loop

早期 ReAct-like 系统常把很多责任塞进 prompt：要求模型按格式输出 Action、自己记住步骤、自己决定何时停止、自己说明是否需要工具。现代框架会把这些责任拆到 runtime 里：

- 工具接管：用 [[Tool Calling]]、schema、参数校验和工具 registry 接管 `Action: ...` 文本解析。
- 状态接管：把对话、任务进度、中间结果、memory 和 scratchpad 放进显式 [[Agent State]]，而不是只靠上下文窗口。
- 流程接管：用 [[Agent Workflow]]、graph、router、handoff 或 orchestrator-workers 决定哪些路径固定、哪些路径交给模型动态选择。
- 执行接管：用 [[Durable Execution]] 保存 checkpoint、处理重试、恢复长任务、等待人工确认。
- 权限接管：用 [[Guardrails]]、policy engine、approval gate 和 least-privilege tools 限制高风险动作。
- 观测接管：用 [[Trace]]、日志、成本和延迟指标记录每一步，方便复现和评估。

所以“接管”不是让模型不思考，而是把原来靠 prompt 软约束的东西，变成可验证、可恢复、可审计的工程对象。

## 常见误解 / 风险

- 误解：框架 demo 看起来强，就代表生产可靠。风险是忽略数据权限、失败恢复、评估集和线上监控。
- 误解：选了框架就不用理解 [[Agent Loop]]。风险是框架抽象遮住了 loop、state、workflow、trace 的真实边界。
- 误解：越复杂的框架越先进。风险是简单任务被过度编排，成本、延迟、调试难度和失败面都增加。
- 风险：把具体 SDK API 当成稳定概念；API 会变，但“框架接管结构、状态和观测”这个边界更稳定。

## 边界细节

判断一个工具是不是 Agent Framework，可以问：它是否提供了多项 Agent 工程责任，而不只是单点能力？例如只提供向量检索的库更像 RAG / retrieval 基础设施；只提供模型路由的是 gateway；只提供日志采集的是 observability 工具；同时组织 agent、tools、state、workflow、handoff、guardrails、tracing 的，才更接近 Agent Framework。

和相邻概念的区别：

- [[Agent Workflow]] 是任务路径；framework 是用来搭路径的软件工具箱。
- [[Agent State]] 是运行数据；framework 提供 state schema、更新规则、checkpoint 或注入上下文的机制。
- [[Tool Calling]] 是行动接口；framework 负责工具注册、权限、错误处理和结果回填。
- [[Trace]] 是观测记录；framework 可能自动生成 trace，但 trace 本身不等于 framework。

边界反例：一个 prompt 模板库不一定是 Agent Framework；一个完整 IDE coding agent 产品也不只是 framework，它还包含 UI、权限、文件系统、沙箱、团队流程和商业策略。

## 现代性状态

- 判定：current-practice / frontier-adjacent
- 为什么：把工具、状态、workflow、handoff、guardrails、trace 和 durable execution 做成工程层，已经是当前 Agent 系统实践；但具体框架 API、SDK 能力和生态排序仍会快速变化。
- 稳定部分：框架负责把 prompt 软约束拆成可验证、可恢复、可审计的工程对象。
- 易变部分：框架名称、API、内置 memory/session/tracing、MCP 集成、可视化调试、部署方式和默认模型适配。
- 复查点：当多个主流框架同时改变 Agent/workflow/state 的抽象边界时，更新本卡；单个 SDK 改名或版本升级优先写 source note / 前沿追踪。

## 现代系统怎么吸收 Agent Framework 的价值 / 局限

现代系统吸收 framework 价值的方式，通常不是“把全部逻辑交给框架”，而是分层：

- framework 接管开发抽象：agent、tool、state、workflow、handoff、guardrail、trace。
- harness / product 接管运行边界：权限、沙箱、审批、审计、成本、停止条件和用户体验。
- eval / observability 接管质量闭环：trace dataset、regression、online monitoring、人审和业务指标。
- team / org 接管变更治理：版本锁定、工具白名单、数据权限和事故复盘。

局限是：框架只能降低工程样板和提供边界，不会自动给出正确任务分解、可靠工具、好评测集或安全业务策略。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#Agent 框架和编排]] / [[Agent 工程基础设施主源#本次判断]]
- Source: [[Anthropic - Building Effective Agents]]
- Anchor: [[Anthropic - Building Effective Agents#一句话]] / [[Anthropic - Building Effective Agents#边界提醒]]
- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Anchor: [[OpenAI - A Practical Guide to Building Agents#一句话]]
- Source: [[LangGraph 官方文档]] / [[OpenAI Agents SDK 文档]]
- Anchor: [[LangGraph 官方文档#一句话]] / [[OpenAI Agents SDK 文档#一句话]] / [[OpenAI Agents SDK 文档#Tracing 补充]]
- Evidence type: official docs/source notes + engineering synthesis.
- Confidence: medium
- Boundary: 具体框架名单和 API 属于 watch；本卡稳定核心是“框架接管 Agent 工程责任”。

## 复习触发

- 为什么 Agent Framework 不是 Agent 本身，也不是模型能力本身？
- 给一个工具调用 demo，指出哪些部分应该由 framework 接管，哪些仍属于 harness / evaluation。
- 什么时候不应该上复杂 Agent Framework？

## 相关链接

- [[Agent]]
- [[Agent Harness]]
- [[Tool Calling]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Guardrails]]
- [[Trace]]
