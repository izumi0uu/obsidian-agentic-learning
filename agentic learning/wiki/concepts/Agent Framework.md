---
type: concept
topic:
  - agent
  - framework
  - workflow
status: growing
created: 2026-05-06
updated: 2026-05-08
last_checked: 2026-05-08
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[LangGraph 官方文档#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
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

Agent Framework 是帮助开发者构建、编排、运行和观测 Agent 的软件框架。

## 它解决什么问题

真实 Agent 需要工具调用、状态、工作流、记忆、human-in-the-loop、trace、handoff、错误恢复和部署接口。框架把这些能力组织成可复用抽象。

代表生态包括 LangGraph、LlamaIndex、Semantic Kernel、AutoGen、CrewAI、OpenAI Agents SDK、Pydantic AI、Mastra、Vercel AI SDK。

## 它不是什么

Agent Framework 不是 Agent 本身，也不是模型能力本身。

换框架不能自动解决需求不清、工具危险、评估缺失或上下文污染。

## 最小例子

```text
define agent -> register tools -> set state -> run loop/workflow -> trace -> evaluate
```

## 框架怎样接管 prompt loop

早期 ReAct-like 系统常把很多责任塞进 prompt：要求模型按格式输出 Action、自己记住步骤、自己决定何时停止、自己说明是否需要工具。现代框架会把这些责任拆到 runtime 里：

- 工具接管：用 [[Tool Calling]]、schema、参数校验和工具 registry 接管 `Action: ...` 文本解析。
- 状态接管：把对话、任务进度、中间结果、memory 和 scratchpad 放进显式 [[Agent State]]，而不是只靠上下文窗口。
- 流程接管：用 [[Agent Workflow]]、graph、router、handoff 或 orchestrator-workers 决定哪些路径固定、哪些路径交给模型动态选择。
- 执行接管：用 [[Durable Execution]] 保存 checkpoint、处理重试、恢复长任务、等待人工确认。
- 权限接管：用 [[Guardrails]]、policy engine、approval gate 和 least-privilege tools 限制高风险动作。
- 观测接管：用 [[Trace]]、日志、成本和延迟指标记录每一步，方便复现和评估。

所以“接管”不是让模型不思考，而是把原来靠 prompt 软约束的东西，变成可验证、可恢复、可审计的工程对象。

## 常见误解和风险

- 框架 demo 看起来强，不代表生产可靠。
- 框架抽象会影响你理解 Agent Loop。
- 过早选复杂框架会增加学习成本。
- 框架只能接管结构、状态和边界，不能自动保证模型判断正确。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[LangGraph 官方文档]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Agent Harness]]
- [[Tool Calling]]
- [[Handoff]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Guardrails]]
- [[Trace]]
