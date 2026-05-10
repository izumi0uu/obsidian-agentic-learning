---
type: source
source_type: docs
title: "Claude Code Hooks Reference"
url: "https://code.claude.com/docs/en/hooks"
author: Anthropic
site: code.claude.com
topic:
  - agent
  - infrastructure
  - tool-use
  - observability
created: 2026-05-10
updated: 2026-05-10
last_checked: 2026-05-10
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Lifecycle Hook]]"
  - "[[Agent Harness]]"
  - "[[Tool Permissioning]]"
  - "[[Trace]]"
  - "[[Observability]]"
---

# Claude Code Hooks 文档

## 为什么收

这是 Claude Code 关于 hooks 的官方参考文档。它适合用来校准 `PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`Stop` 等生命周期 hook 的工程边界：哪些事情发生在工具执行前，哪些发生在工具执行后，哪些能阻断工具，哪些只能补充反馈。

这份文档不是 Codex 官方文档，因此不能直接证明 Codex 或 OpenAI 服务器的内部实现；它更适合作为“代码 Agent 产品如何把 agent loop 暴露成可拦截事件”的主源例子。

## 关键事实

- Hooks 可以按 session、turn、tool call 等 cadence 触发；`PreToolUse` / `PostToolUse` 位于 agentic loop 的每次工具调用边界。
- `PreToolUse` 在模型生成工具参数之后、工具真正执行之前触发，可以用于 allow、deny、ask、defer、补充上下文或阻断工具调用。
- `PostToolUse` 在工具成功执行之后触发，可以读取 `tool_input` 和 `tool_response`，并把额外上下文或替换后的工具输出反馈给模型；但它不能阻止已经发生的副作用。
- Hook handler 可以是本地 command、HTTP endpoint、MCP tool、prompt hook 或 agent hook；因此 hook 是 runtime / harness 能力，不是 LLM 参数内部能力。

## 可以拆成概念卡

- [[Agent Lifecycle Hook]]
- [[Agent Harness]]
- [[Tool Permissioning]]
- [[Observability]]
- [[Trace]]

## 边界提醒

不要把 Claude Code 的 hook API 当成所有 Agent 框架的统一标准。稳定的是“生命周期事件 + 外部 handler + 权限/观测/反馈”的设计模式；易变的是具体事件名、JSON schema、权限字段和 UI 行为。
