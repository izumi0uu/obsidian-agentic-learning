---
type: source
source_type: docs
title: Anthropic Tool Use Documentation
url: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use
author: Anthropic
site: docs.anthropic.com
topic:
  - llm
  - agent
  - tools
created: 2026-05-10
updated: 2026-05-10
last_checked: 2026-05-10
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Tool Registry]]"
  - "[[Agent Harness]]"
---

# Anthropic Tool Use 文档

## 为什么收

这是理解 Claude tool use 的官方工程来源。它明确把工具定义拆成 `name`、`description`、`input_schema`、示例和 tool choice 等字段，适合校准 [[Tool Calling]] schema 的跨厂商边界。

## 一句话

Anthropic Tool Use 用 `tools` 参数把工具定义传给 Claude；工具的输入参数由 `input_schema` 这个 JSON Schema 对象描述。

## Tool schema 锚点

官方页面：<https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use>

Anthropic 文档中的工具定义核心字段：

- `name`：工具名。
- `description`：告诉模型工具做什么、何时使用、有哪些限制。
- `input_schema`：定义工具期望输入参数的 JSON Schema。
- `input_examples`：可选，用来给复杂工具提供合法输入示例。

文档还强调，工具描述质量会显著影响模型是否选对工具、是否填对参数。

## Strict tool use

Anthropic 文档提供 strict tool use：可以结合 tool choice，让模型调用工具时更严格地遵循 schema。

边界：即使有 strict schema，运行时仍然需要校验、权限控制、错误处理和结果审计。

## 边界提醒

- `input_schema` 是工具输入契约，不是工具实现。
- 工具返回结果也需要被设计成高信号、低噪音，否则会浪费上下文并误导下一轮推理。
- 具体 API 字段可能变化，因此这份 source 标记为 `freshness: volatile`。
