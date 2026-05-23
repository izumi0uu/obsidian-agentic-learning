---
type: source
source_type: docs
title: OpenAI Structured Outputs Documentation
url: https://platform.openai.com/docs/guides/structured-outputs
author: OpenAI
site: platform.openai.com
topic:
  - llm
  - structured-output
  - tools
  - decoding
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: volatile
conflicts: []
status: seed
source:
  - https://platform.openai.com/docs/guides/structured-outputs
  - https://openai.com/index/introducing-structured-outputs-in-the-api/
related:
  - "[[Constrained Decoding]]"
  - "[[Tool Calling]]"
  - "[[Type-safe Agent SDK]]"
  - "[[Workflow Guardrails]]"
---

# OpenAI Structured Outputs 文档

## 为什么收

这份 source note 用来给 [[Constrained Decoding]] 提供官方产品证据：Structured Outputs 不只是“提示模型输出 JSON”，而是要求模型输出匹配开发者提供的 JSON Schema。它也帮助区分 JSON mode、strict tool calling、schema validation 和 structured output 的边界。

## 一句话

OpenAI Structured Outputs 是让模型输出符合指定 JSON Schema 的 API 能力；在 function calling strict mode 下，它用于提高 tool arguments 对 schema 的贴合度。

## Schema adherence 锚点

- 官方文档：<https://platform.openai.com/docs/guides/structured-outputs>
- 官方介绍：<https://openai.com/index/introducing-structured-outputs-in-the-api/>

中文概括：

- Structured Outputs 的目标是让模型输出满足开发者提供的 schema，而不只是语法上是 JSON。
- 在 function calling 中，`strict: true` 让函数参数更严格地遵循 schema。
- JSON mode 只保证 JSON 语法合法；Structured Outputs 关心字段、类型、枚举、必填项等 schema adherence。

支撑概念：

- [[Constrained Decoding]]
- [[Tool Calling]]
- [[Type-safe Agent SDK]]

证据边界：

- 这条证据支持 OpenAI 产品层的 schema adherence 目标；具体支持哪些 JSON Schema 子集、模型名称、API 参数和限制会变化，需要按官方文档复查。

## Constrained decoding 锚点

OpenAI 官方介绍文章把 Structured Outputs 的可靠性拆成模型训练和 constrained decoding 两部分。工程理解是：在生成过程中，系统根据 schema 和当前 partial output 计算哪些 token 仍可能导向合法输出，把不合法 token 从候选集中排除。

这支持 [[Constrained Decoding]] 的核心边界：它是在解码时约束 token 选择，不是生成后再检查，也不是单靠 prompt 要求模型“请遵守格式”。

证据边界：

- constrained decoding 能提高结构合法性，但不证明事实正确、业务规则正确、权限安全或工具结果可信。
- 对枚举、数字、字符串、嵌套对象等约束是否完全可表达，取决于具体 schema 子集和实现。

## 可以拆成概念卡

- [[Constrained Decoding]]
- structured output / schema adherence
- JSON mode vs Structured Outputs

## 边界提醒

Structured Outputs 属于产品/API 能力；[[Constrained Decoding]] 是更底层的生成控制机制。一个应用可以用 constrained decoding 生成合法 JSON，但仍然需要 runtime validation、业务校验、权限控制、trace 和 eval。
