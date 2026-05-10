---
type: concept
topic:
  - llm
  - agent
  - tool-use
status: seed
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Toolformer]]"
  - "[[OpenAI Function Calling 文档]]"
  - "[[Anthropic Tool Use 文档]]"
evidence:
  - "[[Toolformer#为什么收]]"
  - "[[OpenAI Function Calling 文档#Tool schema 锚点]]"
  - "[[Anthropic Tool Use 文档#Tool schema 锚点]]"
related:
  - "[[Tool Calling]]"
  - "[[Agent]]"
  - "[[LLM]]"
---

# Tool Use

## 一句话

Tool Use 是模型或 Agent 使用外部工具来补足自身能力的行为。

## 概念详解

Tool Use 是比 [[Tool Calling]] 更宽的概念：它描述模型或 Agent 使用外部能力完成自己不能稳定完成的事。这个外部能力可以是搜索、计算器、数据库、代码执行器、浏览器、文件系统、日历、邮件、支付 API 或人类反馈。它出现的根本原因是 LLM 的参数知识和上下文窗口有限，不能天然访问实时世界、执行精确操作或产生真实副作用。

[[Toolformer]] 提供了一个重要视角：工具使用不只是工程接口，也是模型要学习的决策问题——什么时候该调用工具、调用什么、参数怎么填、返回结果怎么用于后续生成。现代 OpenAI / Anthropic tool docs 则把这种行为落到结构化接口上，让 tool use 通过 schema、tool call、tool result 和 runtime validation 进入系统。

边界上，Tool Use 是行为能力，Tool Calling 是接口形式。一个人可以“使用工具”但不用标准 tool calling API；一个模型也可能输出合法 tool call，却因为目标不清、工具描述差、权限错误或 observation 被污染而没有真正完成任务。学习 Tool Use 时要同时看三层：模型是否知道何时用工具，runtime 是否安全执行工具，Agent loop 是否能利用工具结果继续推进目标。

Tool Use 的关键能力其实包含三个判断：是否需要工具、选择哪个工具、如何利用返回结果。许多失败不是发生在工具本身，而是发生在这三个判断之间：模型在不需要时调用了搜索，选择了权限过大的工具，或者拿到结果后没有验证就继续写答案。现代系统用 tool calling、tool registry、least-privilege tools、observation filtering 和 evaluation 来降低这些错误，但仍需要在任务设计上限制工具暴露面。
## 它解决什么问题

LLM 不能天然访问实时信息、精确计算、调用 API 或操作环境。工具使用让系统可以把这些任务交给外部能力完成。

## 它不是什么

Tool Use 不等于 Agent。

会使用工具只是能力之一。Agent 还需要目标、状态、规划、反馈循环、权限和评估。

## 最小例子

模型遇到数学计算时调用 calculator，遇到事实问题时调用 search，遇到日期问题时调用 calendar。

## 常见误解 / 风险

- 误解：Tool Use 等于 Tool Calling。前者是能力和行为，后者是结构化接口。
- 误解：能用搜索就能解决事实问题。搜索结果可能过期、片面或被注入，仍需要来源判断和验证。
- 误解：工具越多越好。工具过多会增加选择错误、权限风险、上下文噪音和延迟。
- 风险：没有最小权限和审批时，工具使用会把模型错误转化成真实副作用。
## 边界细节

[[Tool Calling]] 更偏接口和结构化调用；Tool Use 更偏能力和行为。

## 现代性状态

- 判定：foundation / current-practice
- 基础地基：让模型借助外部能力补足实时性、精确计算和环境操作，是稳定需求。
- 当前工程实践：主流系统通常用 [[Tool Calling]]、tool registry、permissioning、observation handling 和 trace 来实现 tool use。
- 易变部分：具体工具协议、API 字段、自动选择策略、工具检索和权限模型会随平台演进。
- 小边界：工具使用能力变强不代表 Agent 可靠；可靠性还依赖目标、状态、反馈、评估和安全边界。

## 证据锚点

- Source: [[Toolformer]]
- Source: [[OpenAI Function Calling 文档]]
- Source: [[Anthropic Tool Use 文档]]
- Anchor: [[Toolformer#为什么收]], [[OpenAI Function Calling 文档#Tool schema 锚点]], [[Anthropic Tool Use 文档#Tool schema 锚点]]
- Evidence type: paper source note + official tool docs + engineering synthesis.
- Confidence: medium
- Boundary: Toolformer 支持“工具使用作为模型能力”的视角；现代 schema / permission / trace 边界来自工程文档综合。

## 复习触发

- Tool Use 和 Tool Calling 的最小区别是什么？
- 为什么“工具更多”可能让 Agent 更不可靠？
- 举一个需要工具的任务，并说明模型决策、runtime 执行和 observation 回填分别在哪里。

## 相关链接

- [[Tool Calling]]
- [[Agent]]
- [[LLM]]
