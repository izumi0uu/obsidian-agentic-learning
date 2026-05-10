---
type: concept
topic:
  - agent
  - llm
  - tools
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Toolformer]]"
  - "[[OpenAI Function Calling 文档]]"
  - "[[Anthropic Tool Use 文档]]"
  - "[[Model Context Protocol 官方文档]]"
  - "[[raw/repos/xiaolinnote/questions/052 ai tools 1. 什么是 Function Calling ？原理是什么？]]"
evidence:
  - "[[Toolformer#为什么收]]"
  - "[[OpenAI Function Calling 文档#Tool schema 锚点]]"
  - "[[OpenAI Function Calling 文档#Strict mode / Structured Outputs]]"
  - "[[Anthropic Tool Use 文档#Tool schema 锚点]]"
  - "[[Model Context Protocol 官方文档#Tool schema 补充]]"
  - "[[raw/repos/xiaolinnote/questions/052 ai tools 1. 什么是 Function Calling ？原理是什么？#工具定义，schema 的每个字段都有含义]]"
related:
  - "[[Agent Loop]]"
  - "[[Tool Use]]"
  - "[[Tool Registry]]"
  - "[[Tool Permissioning]]"
  - "[[Observation]]"
  - "[[MCP]]"
---

# Tool Calling

## 一句话

Tool Calling 是让模型用结构化格式表达“我要调用哪个工具、参数是什么”，再由外部运行时真正执行工具并把结果回填给模型。

## 它解决什么问题

LLM 只靠生成文本无法真正访问实时信息、运行代码、查询数据库或修改外部系统。早期做法常靠解析自然语言，例如模型说“我需要查天气”，程序再用 if/else 猜它想调用哪个 API；这种方式很脆。

Tool Calling 把这件事变成显式接口：

```text
工具定义 / schema -> 模型输出 tool call -> runtime 执行工具 -> tool result / observation -> 模型继续回答
```

它把 [[ReAct]] 里容易脆弱的 `Action: ...` 文本解析，部分交给结构化 tool call、schema 校验和 [[Tool Registry]] 管理。

[[Toolformer]] 把工具使用推进成一种模型能力问题：模型不仅要会发出工具调用，还要知道什么时候调用、传什么参数、如何利用返回结果。

## 它不是什么

Tool Calling 不是 Agent 本身。它是 Agent 可以使用的一种能力。

会调用天气 API 的聊天机器人，不一定能自主规划旅行、比较航班、检查预算并提醒用户确认付款。

Tool Calling schema 也不是工具实现。schema 只是“工具说明书 / 参数契约”，真正读文件、查数据库、发请求、付款或改代码的动作仍由 [[Agent Harness]] / 应用代码执行。

Tool Calling 也不等于 JSON mode。JSON mode 只关心输出是不是合法 JSON；tool schema / Structured Outputs / strict tool use 更关心输出是否符合指定字段、类型、必填项和枚举约束。

## 最小例子

用户问：“今天上海天气怎么样？”

模型不直接猜答案，而是请求调用天气工具。工具返回结果后，模型再把结果解释给用户。

一个简化的 tool schema 可以长这样：

```json
{
  "name": "get_weather",
  "description": "查询指定城市的实时天气。",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "城市名，例如上海"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"]
      }
    },
    "required": ["city"],
    "additionalProperties": false
  }
}
```

模型看到这个 schema 后，可能输出：

```json
{
  "name": "get_weather",
  "arguments": {
    "city": "上海",
    "unit": "celsius"
  }
}
```

这一步仍然只是“请求调用”。你的程序要检查参数、执行真实天气 API，再把结果作为 tool result / [[Observation]] 回给模型。

## Tool Calling schema 是什么

Tool Calling schema 是给模型和运行时共同阅读的工具契约，通常采用 JSON Schema 或类似结构。它至少回答四个问题：

- 工具叫什么：`name`。
- 工具什么时候该用：`description`。
- 参数长什么样：`parameters` / `input_schema` / `inputSchema`。
- 哪些字段必填、类型是什么、取值范围是什么：`required`、`type`、`enum`、`additionalProperties` 等。

不同生态命名略有差别：

| 生态 | 常见字段 | 含义 |
|---|---|---|
| OpenAI function calling | `name` / `description` / `parameters` | function tool 的 JSON Schema 参数定义 |
| Anthropic tool use | `name` / `description` / `input_schema` | Claude 工具输入 schema |
| MCP tools | `name` / `description` / `inputSchema` / `outputSchema` | server 暴露工具的输入/输出 schema |

schema 的两层作用要分开看：

- 对模型：帮助它判断该不该调用、调用哪个工具、参数怎么填。
- 对 runtime：帮助程序做解析、参数校验、拒绝非法字段、生成类型、记录 trace 和触发 retry。

工具越强，权限越需要清晰。读文件、写文件、发邮件、付款、删除数据这类动作应该有不同的确认策略。

## 常见误解

1. 误以为 schema 会执行工具。

schema 不执行任何东西。它只是描述工具。真正执行动作的是应用代码、MCP client/server、插件或 agent harness。

2. 误以为 schema 写清楚就安全。

schema 能减少格式错、类型错、漏字段，但不能自动判断“这次调用是否越权”“这个订单能不能退款”“工具结果是否被投毒”。这些属于 [[Tool Permissioning]]、[[Guardrails]]、审批、审计和业务校验。

3. 误以为 description 只是给人看的注释。

工具和参数的 `description` 会强烈影响模型选工具和填参数。写得太短，模型容易误用；写得太宽，模型可能在不该调用时也调用。

4. 误以为 Tool Calling 一定是一次性调用。

一次 tool call 可以是单轮的；放进 [[Agent Loop]] 后，也可以形成多轮 “tool call -> observation -> 再决策”。

## 边界细节

Tool Calling 里至少有四个对象，不能混在一起：

| 对象 | 说明 |
|---|---|
| tool schema | 工具说明书和参数契约 |
| tool call | 模型生成的调用请求 |
| tool execution | 应用侧真正执行函数/API/命令 |
| tool result / observation | 执行结果，回填给模型或 state |

schema 能接管 ReAct 的 Action 格式，但接管不了整个 Agent：

- 它不能决定任务目标是否完成，需要停止条件或 evaluator。
- 它不能保存长期任务进度，需要 [[Agent State]]。
- 它不能天然防止危险动作，需要 [[Tool Permissioning]] 和 [[Approval Gate]]。
- 它不能保证结果正确，需要 [[Evaluation]]、业务校验和 trace/replay。
- 它不能自动管理大量工具，需要 [[Tool Registry]] 或 MCP 这类协议/注册层。

## 现代性状态

当前工程实践（current-practice）。

Tool Calling schema 不是前沿论文概念，而是现代 Agent 工程的基础接口层。稳定的部分是“用结构化工具定义替代自然语言 Action 解析”；易变的部分是各厂商 API 字段、strict mode 支持范围、MCP schema 版本和工具搜索/延迟加载等产品能力。因此概念本身可稳定学习，具体 API 要按 `freshness: watch/volatile` 定期复查。

## 现代系统怎么吸收 ReAct 的局限

裸 [[ReAct]] prompt 常见问题是 action 文本解析不稳、参数格式不稳、工具描述散落在 prompt 里、权限和错误处理靠临时逻辑。现代系统通常这样吸收它：

- 用 Tool Calling schema 接管 `Action: search[...]` 这种文本格式。
- 用 runtime validation 拦截缺字段、类型错、额外字段。
- 用 [[Tool Registry]] 管理工具名、描述、版本、可见性和来源。
- 用 [[Tool Permissioning]] / [[Approval Gate]] 决定哪些 tool call 可以自动执行。
- 用 [[Trace]] 记录 schema、tool call、tool result、错误和重试，方便复现。

[[Tool Use]] 更偏“行为能力”，Tool Calling 更偏“接口形式”。一个系统可以有 tool calling API，但仍然不会可靠地使用工具。

## 证据锚点

- Source: [[Toolformer]]
- Source: [[OpenAI Function Calling 文档]]
- Source: [[Anthropic Tool Use 文档]]
- Source: [[Model Context Protocol 官方文档]]
- Source: [[raw/repos/xiaolinnote/questions/052 ai tools 1. 什么是 Function Calling ？原理是什么？]]
- Anchor: OpenAI 文档说明 function tool 由 JSON Schema 定义，并区分 tool、tool call、tool call output。
- Anchor: Anthropic 文档说明工具字段包含 `name`、`description`、`input_schema`，且 `input_schema` 是工具输入 JSON Schema。
- Anchor: MCP Tools spec 说明 tool definition 包含 `inputSchema` 和可选 `outputSchema`。
- Confidence: high for schema/interface boundary; medium for vendor-specific API细节，因为 API 会变。

## 复习触发

1. 请用一句话解释：schema、tool call、tool result 分别是什么？
2. 为什么说 schema 只能接管 `Action` 格式，不能替代权限控制？
3. JSON mode、Structured Outputs、Tool Calling schema 三者最小区别是什么？

## 相关链接

- [[Agent Loop]]
- [[Tool Use]]
- [[Tool Registry]]
- [[Tool Permissioning]]
- [[Observation]]
- [[MCP]]
