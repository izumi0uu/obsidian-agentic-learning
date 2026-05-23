---
type: source
source_type: article
title: "AI Engineering From Scratch - Structured Outputs"
url: https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/03-structured-outputs
author: Rohit G.
site: aiengineeringfromscratch.com
topic:
  - llm
  - structured-output
  - decoding
  - tools
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: watch
status: seed
source:
related:
  - "[[Structured Outputs]]"
  - "[[Constrained Decoding]]"
  - "[[Tool Calling]]"
  - "[[Type-safe Agent SDK]]"
  - "[[Workflow Guardrails]]"
---

# AI Engineering From Scratch - Structured Outputs

## 为什么收

这篇 lesson 补的是结构化输出的生产表层：JSON mode、schema mode、JSON Schema、Pydantic validation、tool use 和 retry loop 如何把 LLM 的自然语言输出接到 typed software boundary 上。

已有 [[Constrained Decoding]] 解释了解码层机制；本 note 用来承接“应用应该怎样选择结构化输出策略、怎样验证和重试、哪些失败不是 schema 能解决的”。

## 一句话

Structured output 的工程问题不是“让模型像 JSON 那样说话”，而是把输出形状、类型、枚举、必填字段、验证、重试和事实核查放进同一条软件契约链。

## 关键事实

- 课程把结构化输出分成四层：prompt-based JSON、JSON mode、schema mode、constrained decoding。越往后，格式和 schema adherence 越接近系统约束。
- JSON mode 只保证语法上能解析成 JSON，不保证字段、类型、枚举、必填项符合业务 schema。
- Schema mode / Structured Outputs 要求输出匹配 JSON Schema 或等价 schema surface，适合抽取、分类、routing、tool arguments 和 judge / planner 输出。
- JSON Schema 是结构契约语言，可以描述 object、array、string、number、boolean、required、enum、min/max、pattern 和组合结构。
- Pydantic pattern 的价值是从 Python 类型模型生成 schema，并把 LLM 输出转换成可验证对象；Instructor 这类库会在验证失败时把错误反馈给模型重试。
- Tool calling / tool use 是结构化输出的相邻接口：模型不是返回自由文本，而是生成工具名和 typed arguments。
- 常见失败包括：schema 合法但值是幻觉、枚举语义近似但不在允许集合、嵌套太深导致错误、数组长度不符合预期、可选字段被省略。
- Schema validation 不能证明事实正确、引用真实、权限安全或业务规则通过；它只证明形状和部分类型/约束符合。
- 生产化还需要 schema diff / versioning、extraction eval、field-level accuracy、type compliance 和低置信字段人工复核。

## 概念拆分

- [[Structured Outputs]]：应用层结构化输出策略谱系。
- [[Constrained Decoding]]：生成时 token-level 合法性约束。
- [[Tool Calling]]：结构化 tool invocation 接口。
- [[Type-safe Agent SDK]]：用类型系统、schema validation 和依赖注入承接输出。
- [[Workflow Guardrails]]：把结构化输出检查放在写库、调用工具或产生副作用之前。

## 边界提醒

结构合法不是事实正确。一个完全符合 schema 的 JSON 仍可能包含错误金额、臆造字段、错误引用或越权意图。schema / constrained decoding / Pydantic validation 应该和 evidence checking、business validation、permissioning、approval gate、trace 和 eval 一起使用。

## 外部链接

- Lesson: <https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/03-structured-outputs>
- Source markdown: <https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/phases/11-llm-engineering/03-structured-outputs/docs/en.md>
