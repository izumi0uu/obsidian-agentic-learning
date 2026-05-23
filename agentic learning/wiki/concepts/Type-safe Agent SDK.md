---
type: concept
topic:
  - agent
  - framework
  - sdk
  - evaluation
status: growing
created: 2026-05-12
updated: 2026-05-23
last_checked: 2026-05-12
freshness: volatile
source:
  - "[[Pydantic AI 官方文档]]"
  - "[[OpenAI Structured Outputs 文档]]"
  - "[[Microsoft Agent Framework 官方文档]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
evidence:
  - "[[Pydantic AI 官方文档#必读块 1：type-safe agent framework 定位]]"
  - "[[Pydantic AI 官方文档#必读块 2：依赖注入与结构化输出]]"
  - "[[OpenAI Structured Outputs 文档#Schema adherence 锚点]]"
  - "[[Agent Framework 全量选型对比 2026-05#Pydantic AI vs OpenAI Agents SDK]]"
related:
  - "[[Tool Calling]]"
  - "[[Constrained Decoding]]"
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Agent Framework]]"
---

# Type-safe Agent SDK

## 一句话

Type-safe Agent SDK 是把 Agent 的依赖、工具参数、结构化输出和运行上下文纳入类型系统/验证框架的 SDK 路线，用来减少“LLM 输出能跑但结构不可信”的工程错误。

## 概念详解

Agent 应用常见失败不只是模型答错，还包括参数结构错、工具输入缺字段、输出格式漂移、依赖对象混乱、测试时难以替换外部服务。Type-safe Agent SDK 用类型声明、schema validation、依赖注入和结构化输出，把这些边界提前暴露出来。

[[Pydantic AI 官方文档]] 的 source note 把 Pydantic AI 定位为 Python-first、type-safe 的 GenAI / Agent framework：用 Pydantic 的验证、依赖注入和结构化输出降低 runtime 错误，同时补 eval、Logfire observability、MCP/A2A、durable execution 和 graph 支持。其示例把 deps_type、output_type、RunContext、tool schema 和 Pydantic 校验放进 Agent 类型里，这说明类型安全不是“代码风格”，而是 Agent 运行边界的一部分。

工程综合：Type-safe Agent SDK 的价值是把 LLM 的不确定文本输出接到可验证的软件契约上；局限是类型正确仍不代表事实正确。

Type-safe 的学习重点是把“不稳定的自然语言接口”尽量包进可验证边界。工具参数、依赖对象、输出 schema、eval fixture 和错误处理都可以被类型系统或 runtime validation 提前暴露。它不能让模型推理必然正确，但能减少工程胶水层的隐性失败。现代系统常把 type-safe SDK 与 eval、observability、durable execution 组合，用结构化边界承接 LLM 的非确定性。

和 [[Constrained Decoding]] 的关系：Constrained Decoding 尽量在生成阶段产出 schema 合法的结构；Type-safe Agent SDK 在应用层把这些结构映射成类型对象、验证错误和可测试契约。前者减少非法输出进入系统，后者决定非法或语义不合格输出如何被拒绝、重试或降级。
## 它解决什么问题

- 工具参数缺字段或类型不匹配导致运行时错误。
- 结构化输出格式漂移，后续业务代码无法稳定消费。
- 测试和评估时难以替换依赖、复现上下文。
- Agent SDK 和后端工程类型系统割裂。

## 它不是什么

- 不是事实校验器。JSON schema 通过不代表答案真实。
- 不是完整 orchestration runtime。复杂长任务仍可能需要 workflow / state graph。
- 不是只属于 Python。Pydantic AI 是代表样本，TypeScript / .NET 也有自己的类型生态路线。

## 最小例子

```python
class RefundResult(BaseModel):
    approved: bool
    reason: str

agent = Agent(deps_type=CustomerDb, output_type=RefundResult)
# tool 输入和 final output 都经过 schema / 类型验证
```

## 常见误解 / 风险

- 误解：结构化输出通过就代表业务正确。风险是错误事实被包装成正确 JSON。
- 误解：类型越复杂越可靠。过度类型化会让迭代变慢，并掩盖评估集不足。
- 风险：把 schema validation 当成 guardrail，忽略权限、审计和人工确认。

## 边界细节

Type-safe Agent SDK 和 [[Tool Calling]] 密切相关：工具 schema 约束模型如何调用工具，type-safe SDK 进一步约束代码端如何注入依赖、验证输入输出和测试。它和 [[Provider-first Agent SDK]] 的区别是：provider-first 围绕供应商平台能力，type-safe 围绕应用类型契约；两者可以重叠。

## 现代性状态

- 判定：current-practice / volatile API。
- 稳定部分：结构化输出、tool schema、runtime validation、依赖注入和 eval 已成为 Agent SDK 的重要方向。
- 易变部分：Pydantic AI 具体 API、durable execution 集成和协议支持。

## 现代系统怎么吸收 Type-safe Agent SDK 的价值 / 局限

现代系统会用 type-safe SDK 锁住工具输入、业务输出和依赖边界，再用 evaluation 检查事实正确，用 trace 审查轨迹，用 approval 处理高风险动作。类型层负责“形状正确”，eval/业务层负责“内容正确”。

## 证据锚点

- [[Pydantic AI 官方文档#必读块 1：type-safe agent framework 定位]]：type-safe agent framework、eval、observability、durable execution 等定位。
- [[Pydantic AI 官方文档#必读块 2：依赖注入与结构化输出]]：deps_type、output_type、RunContext、tool schema 和 Pydantic 校验。
- [[OpenAI Structured Outputs 文档#Schema adherence 锚点]]：支持 schema adherence 与结构化输出边界。
- [[Agent Framework 全量选型对比 2026-05#Pydantic AI vs OpenAI Agents SDK]]：typed app SDK 与 provider-first SDK 边界。

- Evidence type: official Pydantic AI/Microsoft/OpenAI docs + framework comparison map + engineering synthesis.
- Boundary: Type-safe Agent SDK 强调类型/schema/依赖注入，不等于 provider-first SDK、完整 runtime，也不替代业务级 evaluation。
## 复习触发

1. 为什么类型安全只能保证“结构正确”，不能保证“事实正确”？
2. Type-safe Agent SDK 和 tool schema 的关系是什么？
3. 如果一个退款 Agent 输出 JSON 通过了 schema，但批准了错误退款，应该在哪一层修？

## 相关链接

- [[Tool Calling]]
- [[Constrained Decoding]]
- [[Evaluation]]
- [[Eval Harness]]
- [[Agent Framework]]
- [[Agent Framework 全量选型对比 2026-05]]
