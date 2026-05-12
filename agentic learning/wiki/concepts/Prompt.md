---
type: concept
topic:
  - llm
  - prompting
  - agent
status: growing
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: stable
source:
  - "[[Context Engineering]]"
  - "[[LLM]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
evidence:
  - "[[Context Engineering#概念详解]]"
  - "[[LLM#它不是什么]]"
  - "[[Plan-and-Solve Prompting#证据锚点]]"
  - "[[OpenAI - A Practical Guide to Building Agents#为什么收]]"
related:
  - "[[LLM]]"
  - "[[Token]]"
  - "[[Context Window]]"
  - "[[Context Engineering]]"
  - "[[Prompt Injection]]"
---

# Prompt

## 一句话

Prompt 是给模型的输入指令和上下文组织，用来告诉模型任务、约束、资料、输出格式和可用工具；它不是模型能力或系统可靠性的全部。

## 概念详解

Prompt 的基本作用是把人类意图、系统规则、任务背景、例子、检索证据、工具说明和输出要求组织成模型可读的输入。对 LLM 来说，prompt 会被转换成 [[Token]] 并放入 [[Context Window]]；模型根据这些上下文生成后续 token。

Prompt 重要，但它只是系统的一层。[[Context Engineering]] 把 prompt 扩展为运行时信息环境：不仅有文字指令，还有工具 schema、memory、RAG evidence、trace summary、权限规则和输出格式。Agent 系统里，prompt 常常与 state、tools、guardrails、evaluation 和 human-in-the-loop 配合；只靠“写得更好的 prompt”无法替代权限、检索、测试和审计。

证据边界：[[Plan-and-Solve Prompting]] 支持特定 prompt pattern 可以改善复杂推理；[[Context Engineering]] 支持现代系统把 prompt 放在更大的上下文装配问题中；OpenAI agent guide source note 支持构建 Agent 时需要清晰指令和边界。具体 prompt 模板是实践策略，不写成稳定定义。

## 它解决什么问题

Prompt 解决“模型这一轮应该按什么任务和约束生成”的输入组织问题。没有清晰 prompt，模型可能不知道角色、目标、输出格式、证据使用规则或拒答条件。

## 它不是什么

Prompt 不是模型训练。它在推理时改变输入，不直接改变模型参数。

Prompt 也不是安全系统。恶意输入、工具权限和数据泄露不能只靠 prompt 承诺解决。

Prompt 也不是完整 [[Context Engineering]]；后者还包括信息选择、排序、预算、来源、记忆和工具结果装配。

## 最小例子

```text
你是 RAG 评估助手。
只基于给定 evidence 回答。
如果 evidence 不支持结论，请说“证据不足”。
输出：结论 + 引用 source id。
```

## 常见误解 / 风险

- 误解：prompt 写好就能解决幻觉、权限和工具风险。
- 误解：prompt 越长越好。长 prompt 可能增加冲突和噪音。
- 风险：外部资料中的 [[Prompt Injection]] 被放入上下文后，可能和真实 instruction 混淆。
- 风险：prompt 模板过度拟合 demo，换数据就失效。

## 边界细节

和 [[Token]] 的边界：prompt 是内容组织，token 是模型处理 prompt 的单位。

和 [[Context Window]] 的边界：prompt 必须放入窗口预算；窗口不足时，prompt、证据和输出会竞争空间。

和 [[Context Engineering]] 的边界：prompt engineering 更关注指令文本；context engineering 管理整轮模型输入环境。

## 现代性状态

- 判定：foundation。
- 稳定部分：模型通过输入上下文接收任务、规则和证据。
- 易变部分：具体 prompt pattern、模型对指令层级的遵循能力、工具 schema 和产品 API 会变化。
- 复查点：新模型上线时，不要假设旧 prompt 模板仍然最优；要用 eval 样本验证。

## 现代系统怎么吸收 Prompt 的价值 / 局限

现代系统把 prompt 模板版本化，并和 eval、trace、guardrails、retrieval 和 tool policies 一起管理。Agent runtime 通常会把 system/developer/user/tool/context 分层，防止外部资料升级成 instruction。

局限是 prompt 只是软约束。高风险动作需要硬权限、sandbox、approval、audit log 和测试验证。

## 证据锚点

- Concept anchor: [[Context Engineering#概念详解]]
- Concept anchor: [[LLM#它不是什么]]
- Concept anchor: [[Plan-and-Solve Prompting#证据锚点]]
- Source anchor: [[OpenAI - A Practical Guide to Building Agents#为什么收]]
- Evidence type: concept/source synthesis + engineering inference.

## 复习触发

1. Prompt 和 Context Engineering 的区别是什么？
2. 为什么 prompt 不是安全边界？
3. prompt、token、context window 如何共同限制一次模型调用？

## 相关链接

- [[LLM]]
- [[Token]]
- [[Context Window]]
- [[Context Engineering]]
- [[Prompt Injection]]
- [[LLM 输入输出基础边界对比]]
