---
type: concept
topic:
  - llm
  - decoding
  - structured-output
  - tools
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: watch
conflicts: []
aliases:
  - constrained decoding
  - 约束解码
  - 受限解码
source:
  - "[[OpenAI Structured Outputs 文档]]"
  - "[[OpenAI Function Calling 文档]]"
  - "[[Agentproof - Static Verification of Agent Workflow Graphs]]"
  - "[[raw/repos/xiaolinnote/questions/127 ai llm 18. 大模型为什么会出现幻觉？怎么缓解？]]"
evidence:
  - "[[OpenAI Structured Outputs 文档#Constrained decoding 锚点]]"
  - "[[OpenAI Function Calling 文档#Strict mode / Structured Outputs]]"
  - "[[Agentproof - Static Verification of Agent Workflow Graphs#Related work：constrained decoding 与 workflow verification]]"
  - "[[raw/repos/xiaolinnote/questions/127 ai llm 18. 大模型为什么会出现幻觉？怎么缓解？#4. 约束解码（Constrained Decoding）]]"
related:
  - "[[Structured Outputs]]"
  - "[[Tool Calling]]"
  - "[[Type-safe Agent SDK]]"
  - "[[Workflow Guardrails]]"
  - "[[Hallucination]]"
  - "[[Token]]"
  - "[[Top-K]]"
  - "[[Prompt Engineering]]"
---

# Constrained Decoding

## 一句话

Constrained Decoding（约束解码）是在模型逐 token 生成时，根据 schema、grammar 或允许集合把会导致非法输出的 token mask 掉，让模型只能选择仍可能组成合法结构的 token。

## 概念详解

LLM 默认生成时会给下一 token 的整个词表分配概率，再由 greedy、sampling、top-k、top-p 等解码策略选择。Constrained Decoding 在这个步骤前后加了一层确定性约束：系统维护“当前已经生成的 partial output 是否仍能走向合法结构”，并根据目标 schema / grammar 计算下一步允许的 token 集合。不允许的 token 概率会被设为 0，模型只能从合法候选里继续生成。

这就是它和普通 prompt instruction 的最小区别。提示词说“请输出 JSON”只是影响概率分布，模型仍可能漏字段、乱加字段或输出不合法结构；Constrained Decoding 则把非法 token 从搜索空间里移除。它也不是生成后的 schema validation：validation 是输出结束后检查并可能重试，Constrained Decoding 是生成过程中避免走到非法结构。

OpenAI Structured Outputs、Outlines、Guidance 这类能力/库的共同思想是：把 JSON Schema、grammar 或格式约束编译成 token-level 约束。Agentproof 的 related work 也把它和 workflow graph verification 区分开：constrained decoding 约束单次模型调用内部生成什么，workflow verification 约束节点之间怎么转移。

## 它解决什么问题

它主要解决结构化输出不稳定的问题：

- JSON 少右括号、字段名拼错、额外字段乱入。
- tool arguments 类型不对、枚举不在允许集合、必填字段缺失。
- 需要输出 SQL、正则、表格、DSL、固定 grammar 或受限 vocabulary 时，模型自由生成容易跑偏。

在 Agent 工程里，它常用于把模型输出接到可解析的软件边界上：tool call arguments、structured result、classifier enum、routing decision、extraction schema。它让“格式合法性”更接近确定性工程问题，而不是完全靠模型服从提示。

## 它不是什么

Constrained Decoding 不是 [[Tool Calling]] 本身。Tool Calling 是模型表达“我要调用哪个工具、参数是什么”的接口形式；Constrained Decoding 是让这类结构化输出在 token 级更不容易越界的解码机制。

它不是 [[Type-safe Agent SDK]]。Type-safe SDK 会用类型、schema、Pydantic / Zod 等校验对象承接模型输出；Constrained Decoding 只发生在模型生成阶段。两者可以组合，但一个是解码约束，一个是应用层类型/验证边界。

它不是 [[Workflow Guardrails]]。Guardrails 可以检查输入、检索、工具、输出、状态和副作用；Constrained Decoding 只保证某次生成更符合形式约束。

它也不是事实正确性保证。一个合法 JSON 可以包含错误事实、错误金额、越权字段意图或被污染工具结果。schema 合法只说明结构通过，不说明语义可靠。

## 最小例子

目标 schema 要求：

```json
{
  "type": "object",
  "properties": {
    "priority": {
      "type": "string",
      "enum": ["low", "medium", "high"]
    }
  },
  "required": ["priority"],
  "additionalProperties": false
}
```

模型生成到这里：

```json
{"priority": "
```

普通解码下，模型可能继续输出 `urgent`、`critical`、`高` 或任意字符串。Constrained Decoding 会让下一步只允许仍可能组成 `low` / `medium` / `high` 的 token 路径；不可能导向合法 enum 的 token 被 mask。

更一般地说：

```text
schema / grammar + partial output -> allowed next tokens -> masked logits -> next token
```

## 常见误解 / 风险

- 误解：Structured Outputs 就是更强的 prompt。实际关键边界在解码和 schema adherence，不只是自然语言说明。
- 误解：输出能通过 schema，就说明内容正确。实际 schema 只能约束形状，不能证明事实、引用、金额、权限或业务规则正确。
- 误解：Constrained Decoding 可以替代运行时校验。实际仍需要 runtime validation，因为实现可能只支持 schema 子集，业务约束也常常超出 JSON Schema。
- 误解：所有 structured output 都一定用同一种 constrained decoding。不同厂商和库可能结合模型训练、token mask、grammar parser、retry、validator 或 fine-tuned behavior，具体实现要看文档。
- 风险：约束过窄会让模型无法表达真实答案，只能在合法但错误的空间里选择；约束写错会稳定地产生错误结构。

## 边界细节

和相邻概念的最小区别：

```text
Prompt instruction: 用自然语言提高遵守格式的概率
JSON mode: 通常保证输出是合法 JSON
Structured Outputs: 要求输出贴合给定 schema
Constrained Decoding: 解码时 mask 非法 token
Schema validation: 生成后检查输出是否符合 schema
Tool Calling: 让模型表达工具名和 arguments
Type-safe Agent SDK: 在应用层用类型/验证承接模型输出
Workflow Guardrails: 在 workflow 多个边界做策略和安全检查
```

Constrained Decoding 和 [[Top-K]] 也都发生在解码阶段，但目的不同：Top-K 是采样策略，限制“从概率最高的 K 个 token 中采样”；Constrained Decoding 是合法性约束，限制“只能选仍满足 grammar/schema 的 token”。两者可以同时存在。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：用 token-level constraints 提高结构化输出合法性，是现代 LLM 工程的基础机制之一。
- 当前工程吸收：OpenAI Structured Outputs、tool calling strict mode、Outlines、Guidance、vLLM / TGI 等生态都围绕 schema / grammar / allowed token set 提供不同形式的结构化生成能力。
- 易变部分：各家支持的 schema 子集、API 字段、streaming 行为、错误模式、模型覆盖范围和性能开销会变化，需要按官方文档复查。

## 现代系统怎么吸收 Constrained Decoding 的价值

现代系统通常把它放在“模型输出 -> 软件契约”的第一道门：

- 生成合法 tool arguments，减少 parser 和 retry 压力。
- 让 extraction / classification 输出固定字段或枚举。
- 给 LLM-as-judge、router、planner 输出固定结构，方便后续程序消费。
- 和 runtime validation、business rules、permissioning、approval、trace、eval 组合，形成多层可靠性边界。

小边界：Constrained Decoding 让“能解析”更稳，不让“该不该执行”自动变稳。尤其在工具调用里，结构合法的危险请求仍然需要 [[Tool Permissioning]] 和 [[Approval Gate]]。

## 证据锚点

- Source: [[OpenAI Structured Outputs 文档]]
- Source: [[OpenAI Function Calling 文档]]
- Source: [[Agentproof - Static Verification of Agent Workflow Graphs]]
- Source: [[raw/repos/xiaolinnote/questions/127 ai llm 18. 大模型为什么会出现幻觉？怎么缓解？]]
- Anchor: [[OpenAI Structured Outputs 文档#Constrained decoding 锚点]]
- Anchor: [[OpenAI Function Calling 文档#Strict mode / Structured Outputs]]
- Anchor: [[Agentproof - Static Verification of Agent Workflow Graphs#Related work：constrained decoding 与 workflow verification]]
- Anchor: [[raw/repos/xiaolinnote/questions/127 ai llm 18. 大模型为什么会出现幻觉？怎么缓解？#4. 约束解码（Constrained Decoding）]]
- Evidence type: official docs/source note + paper related-work boundary + raw interview/tutorial source + engineering synthesis.
- Confidence: high for mechanism boundary; medium for provider/library implementation details because API and schema support evolve.
- Boundary: 本卡只承诺结构合法性边界，不把 constrained decoding 写成事实可靠性、安全权限或业务正确性的保证。

## 复习触发

1. Constrained Decoding 和“生成后 schema validation”的最小区别是什么？
2. 为什么 JSON 合法不等于事实正确？
3. Tool Calling、Structured Outputs、Constrained Decoding 三者分别在什么层？
4. 为什么 Top-K 和 Constrained Decoding 都是解码相关，但不是同一类控制？

## 相关链接

- [[Structured Outputs]]
- [[Tool Calling]]
- [[Type-safe Agent SDK]]
- [[Workflow Guardrails]]
- [[Hallucination]]
- [[Token]]
- [[Top-K]]
- [[Prompt Engineering]]
