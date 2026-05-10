---
type: source
source_type: docs
title: "OpenAI Function Calling Documentation"
url: "https://platform.openai.com/docs/guides/function-calling?api-mode=chat"
author: OpenAI
site: platform.openai.com
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
  - "[[Agent Harness]]"
  - "[[Observation]]"
---

# OpenAI Function Calling 文档

## 为什么收

这是理解现代 [[Tool Calling]] / function calling 的官方工程来源。它说明 tool、tool call、tool call output 的分工，也说明 function tool 通过 JSON Schema 定义。

## 一句话

OpenAI Function Calling 让模型在需要外部系统时输出结构化 tool call，由应用侧代码执行工具，再把 tool output 回传给模型。

## Tool schema 锚点

官方页面：<https://platform.openai.com/docs/guides/function-calling?api-mode=chat>

OpenAI 文档把 function 视为一种 tool：function tool 由 JSON Schema 定义，模型根据这些工具定义决定是否生成 tool call，以及填入哪些参数。

最小分工：

- `tools` / function definition：应用提供给模型的工具定义和参数 schema。
- `tool call`：模型输出的调用请求，包含工具名和 arguments。
- `tool call output`：应用侧执行工具后生成的结果，再发回模型。

## Strict mode / Structured Outputs

结构化输出页面：<https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat>

OpenAI 文档建议对 function calling 开启 `strict: true`。在 strict mode 下，function call 的 arguments 会更可靠地贴合提供的 schema；这依赖 Structured Outputs。

边界：JSON mode 只保证输出是合法 JSON，不保证符合某个具体 schema；要 schema adherence，需要 Structured Outputs 或运行时校验。

## 边界提醒

- Function calling 不是模型亲自执行代码；模型只输出调用请求。
- Schema 约束的是“参数形状”，不自动解决权限、安全、业务合法性、工具结果可信度。
- API 文档和模型支持范围会变化，因此这份 source 标记为 `freshness: volatile`。
