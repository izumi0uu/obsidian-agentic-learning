---
type: concept
topic:
  - agent
  - framework
  - workflow
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
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

## 常见误解和风险

- 框架 demo 看起来强，不代表生产可靠。
- 框架抽象会影响你理解 Agent Loop。
- 过早选复杂框架会增加学习成本。

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
