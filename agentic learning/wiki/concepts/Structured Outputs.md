---
type: concept
topic:
  - llm
  - structured-output
  - tools
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: watch
conflicts: []
aliases:
  - structured outputs
  - Structured Output
  - structured output
  - 结构化输出
  - schema mode
  - schema-constrained output
source:
  - "[[AI Engineering From Scratch - Structured Outputs]]"
  - "[[OpenAI Structured Outputs 文档]]"
  - "[[OpenAI Function Calling 文档]]"
  - "[[Pydantic AI 官方文档]]"
evidence:
  - "[[AI Engineering From Scratch - Structured Outputs#关键事实]]"
  - "[[OpenAI Structured Outputs 文档#Schema adherence 锚点]]"
  - "[[OpenAI Function Calling 文档#Strict mode / Structured Outputs]]"
  - "[[Pydantic AI 官方文档#必读块 2：依赖注入与结构化输出]]"
related:
  - "[[Constrained Decoding]]"
  - "[[Tool Calling]]"
  - "[[Type-safe Agent SDK]]"
  - "[[Workflow Guardrails]]"
  - "[[Hallucination]]"
  - "[[Prompt Engineering]]"
---

# Structured Outputs

## 一句话

Structured Outputs 是让 LLM 输出符合可解析、可验证的软件结构契约的工程层，通常通过 JSON mode、JSON Schema、tool schema、Pydantic / Zod validation、retry loop 或 constrained decoding 实现。

## 概念详解

LLM 原生输出是 token 序列，应用程序需要的是可解析对象。Structured Outputs 解决的就是这条边界：让模型输出能被下游代码稳定消费的字段、类型、枚举、数组、嵌套对象或工具参数。它不是一个单一 API 名称，而是一组从弱到强的结构控制方法。

最弱层是 prompt-based JSON：在 prompt 里写“请输出 JSON”。这能提高概率，但模型仍可能加解释、代码围栏、漏括号或漏字段。JSON mode 往前一步，通常保证语法上是合法 JSON，但不保证符合业务 schema。Schema mode / Structured Outputs 更进一步，要求字段、类型、必填项、枚举等贴合 schema。最底层机制可能是 [[Constrained Decoding]]：生成时把不可能导向合法结构的 token mask 掉。

应用层通常还会用 Pydantic、Zod、JSON Schema validator 或 Instructor 这类 retry layer 承接输出。验证失败时，系统可以把错误反馈给模型重试；验证通过后，代码得到 typed object，而不是继续解析自由文本。

这个边界非常关键：schema compliance 只证明形状通过，不证明内容真实。模型可以输出类型正确但事实错误的价格、日期、引用或权限意图。Structured Outputs 应该和证据核查、业务规则、权限控制、审批、trace 和 eval 一起构成可靠边界。

## 它解决什么问题

它解决的是“自然语言答案无法稳定接入软件系统”的问题。常见场景包括信息抽取、分类标签、router decision、tool arguments、LLM-as-judge 输出、planner step、RAG citation object 和审批前检查结果。

## 它不是什么

Structured Outputs 不是 [[Constrained Decoding]] 的同义词。Structured Outputs 是应用层目标和 API / SDK surface；Constrained Decoding 是可能使用的解码层机制。

它不是 [[Tool Calling]] 本身。Tool Calling 用结构化参数表达工具调用；Structured Outputs 也可以用于非工具场景，例如抽取 JSON 或 judge score。

它不是事实验证。合法 JSON 仍可能幻觉；schema validation 不能替代 evidence checking。

## 最小例子

```json
{
  "product": "Sony WH-1000XM5",
  "price": 348.0,
  "in_stock": true
}
```

对应 schema 约束：

```json
{
  "type": "object",
  "properties": {
    "product": { "type": "string" },
    "price": { "type": "number", "minimum": 0 },
    "in_stock": { "type": "boolean" }
  },
  "required": ["product", "price", "in_stock"]
}
```

schema 能检查 `price` 是非负数字，但不能证明原文里的价格真的就是 348。

## 常见误解 / 风险

- 误解：JSON mode 等于 Structured Outputs。JSON mode 只保证可解析，不保证 schema adherence。
- 误解：Pydantic validation 通过就代表答案正确。它只证明类型和约束通过。
- 误解：Structured Outputs 不再需要 prompt。schema 定义形状，prompt 仍要定义任务、证据使用和语义边界。
- 风险：optional field 太多，模型会省略业务上重要的信息。
- 风险：schema 过深或过复杂，模型 / provider 可能支持不完整或错误率上升。
- 风险：schema version 改动没有 diff 和 eval，导致下游 consumer 断裂。

## 边界细节

结构化输出谱系：

```text
Prompt-based JSON: 自然语言要求，软约束
JSON mode: 保证 JSON 语法，未必符合 schema
Schema mode / Structured Outputs: 要求贴合 schema
Constrained Decoding: token-level mask 非法输出路径
Runtime validation + retry: 生成后检查并修复
Business validation: 检查事实、权限、引用和业务规则
```

和 [[Type-safe Agent SDK]]：Type-safe SDK 把 structured output 放进更大的开发者体验，包括依赖注入、工具参数、输出类型、eval 和 observability。Structured Outputs 是其中一块边界。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：LLM 应用需要把自然语言输出接到 typed data boundary，结构化输出是生产系统基础。
- 当前工程吸收：OpenAI Structured Outputs、tool calling strict mode、Anthropic tool use、Gemini response schema、Pydantic AI、Instructor、Outlines、Guidance 等都提供不同层次的结构化输出能力。
- 易变部分：具体 API 字段、schema 子集、streaming 行为、provider 支持和性能开销会变化，需要按官方文档复查。

## 现代系统怎么吸收 Structured Outputs 的价值

现代系统把结构化输出当成 LLM 与代码之间的契约：节点输出必须有 schema，写库前必须 validation，tool arguments 必须过权限和业务规则，judge / router 输出必须可审计。高可靠系统还会维护 extraction eval、field-level accuracy、schema diff、低置信字段复核和失败样例回归。

## 证据锚点

- [[AI Engineering From Scratch - Structured Outputs#关键事实]]：支持结构化输出谱系、Pydantic pattern、retry loop 和失败模式。
- [[OpenAI Structured Outputs 文档#Schema adherence 锚点]]：支持 Structured Outputs 的 schema adherence 目标。
- [[OpenAI Function Calling 文档#Strict mode / Structured Outputs]]：支持 tool calling strict mode 与 schema adherence 边界。
- [[Pydantic AI 官方文档#必读块 2：依赖注入与结构化输出]]：支持类型验证和结构化输出进入 Agent SDK。
- Evidence type: course source note + official docs source notes + engineering synthesis.
- Boundary: 本卡记录 LLM 输出与软件类型 / schema 契约之间的应用层边界；不把它等同于 constrained decoding、tool calling、业务规则校验、事实核查或权限安全控制。
- Confidence: high for boundary; medium for provider-specific details because API surfaces evolve.

## 复习触发

1. JSON mode 和 schema mode 的最小区别是什么？
2. Structured Outputs 和 Constrained Decoding 分别在哪一层？
3. 为什么 schema 合法不等于事实正确？
4. 一个 extraction pipeline 应该评估哪些 field-level 指标？

## 相关链接

- [[Constrained Decoding]]
- [[Tool Calling]]
- [[Type-safe Agent SDK]]
- [[Workflow Guardrails]]
- [[Hallucination]]
- [[Prompt Engineering]]
