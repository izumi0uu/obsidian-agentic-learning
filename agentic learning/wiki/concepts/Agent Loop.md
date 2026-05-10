---
type: concept
topic:
  - agent
  - workflow
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#图片录入：ReAct Tools / LLM / Environment]]"
  - "[[OpenAI - A Practical Guide to Building Agents#一句话]]"
  - "[[Anthropic - Building Effective Agents#边界提醒]]"
  - "[[LangGraph 官方文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
related:
  - "[[Agent]]"
  - "[[ReAct]]"
  - "[[Observation]]"
  - "[[Planning]]"
  - "[[Tool Calling]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
---

# Agent Loop

## 一句话

Agent Loop 是 Agent 的行动反馈循环：观察当前状态，决定下一步，执行动作，把 observation 写回上下文 / state / trace，再继续推进或停止。

## 它解决什么问题

很多任务不是一次回答就结束，而是需要在外部反馈中推进：测试会失败，网页会变化，检索可能为空，用户可能拒绝某个高风险动作。没有 loop，系统只能“猜下一步”；有 loop，系统可以用每次行动后的 [[Observation]] 校正后续判断。

[[ReAct]] 给了一个经典入口：reasoning trace、action 和 observation 交替出现。它的价值不是让模型“多想几步”，而是提醒我们：行动后的外部结果必须回到下一轮决策里，否则 Agent 只是一次性生成器加工具包装。

## 它不是什么

Agent Loop 不是固定 prompt 模板，也不等于裸 `Thought -> Action -> Observation` 文本格式。现代系统常把 action 变成结构化 [[Tool Calling]]，把 observation 写进显式 [[Agent State]]，把过程保存为 [[Trace]]。

Agent Loop 也不是 [[Agent Workflow]] 的同义词。Loop 描述一次行动如何根据反馈继续；workflow 描述多个步骤、分支、审批和交接如何被组织。

Agent Loop 更不是可靠性的保证。循环如果没有停止条件、权限边界和评估，只会把错误放大得更完整。

## 最小例子

任务：帮我修一个测试失败。

```text
observe: 读取失败日志
think/plan: 判断可能是断言或 fixture 过期
act: 修改最小相关代码
evaluate: 重新跑目标测试
observe: 如果仍失败，读取新日志；如果通过，停止并报告证据
```

关键点：测试输出不是附属信息，而是下一轮行动的输入。

## 常见误解 / 风险

- 误解：只要让模型循环，就会自动变成 Agent。风险是没有工具权限、状态更新、停止条件和验收标准。
- 误解：每轮让模型自评就够了。风险是 self-eval 把错误解释得更合理，而不是发现真实失败。
- 风险：observation 太弱或没有结构化保存，模型下一轮看不到真正关键的环境变化。
- 风险：循环没有 budget、timeout、approval gate 或人工接管，可能无限重试、重复调用工具或执行危险动作。

## 边界细节

最小判断：如果系统有“目标 -> 行动 -> 观察 -> 更新状态 -> 再行动 / 停止”，它才接近 Agent Loop；如果只是“输入 -> 输出”，通常还是普通 LLM 应用。

和相邻概念的区别：

- [[Agent]] 是更大的系统边界，包含目标、工具、状态、权限、评估和人类介入。
- [[Agent State]] 记录循环走到哪里、已经看到什么、下一步依据是什么。
- [[Agent Workflow]] 把多个 loop、固定步骤、分支、handoff 和审批组织起来。
- [[Trace]] 记录 loop 实际发生过什么，供调试、评估和回放使用。

一个容易忽略的边界：observation 只有被 runtime 写回上下文、state 或 trace，才真正进入 loop。工具在外部执行成功，但结果没有被正确解析或保存，下一轮模型仍然等于“没看见”。

## 现代性状态

- 判定：foundation / current-practice
- 为什么：行动-观察-再行动是 Agent 的稳定基础；但裸 ReAct 文本格式属于历史过渡，现代框架通常把它拆进 tool calling、state graph、guardrails、tracing 和 evaluation。
- 稳定部分：行动后必须接收外部反馈，并把反馈用于下一步决策。
- 易变部分：具体 SDK 的 tool call schema、trace 字段、checkpoint 方式、approval API 和可视化界面。
- 复查点：当主流框架不再把 loop/state/trace 作为 Agent 基础抽象时，才需要改本卡定义；单个 SDK API 变化优先写回对应 source note。

## 现代系统怎么吸收 Agent Loop 的价值 / 局限

现代系统通常不会让 prompt 独自承担 loop：

- [[Tool Calling]] 接管 action 的结构化表达、参数校验和工具执行。
- [[Agent State]] 接管任务进度、工具结果、错误、审批状态和下一步依据。
- [[Agent Workflow]] / graph 接管固定路径、分支、循环、handoff 和停止条件。
- [[Guardrails]]、approval gate、sandbox 和 least-privilege tools 限制高风险动作。
- [[Trace]] 和 [[Evaluation]] 把每轮行动变成可调试、可回归检查的证据。

工程综合边界：这些吸收方式来自现代框架 / SDK / observability 实践的合并理解，不是 ReAct 论文原文逐条声明。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: [[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]] / [[ReAct - Synergizing Reasoning and Acting in Language Models#图片录入：ReAct Tools / LLM / Environment]]
- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Anchor: [[OpenAI - A Practical Guide to Building Agents#一句话]]
- Source: [[Anthropic - Building Effective Agents]]
- Anchor: [[Anthropic - Building Effective Agents#边界提醒]]
- Source: [[LangGraph 官方文档]] / [[OpenAI Agents SDK 文档]]
- Evidence type: paper source note + official docs/source notes + engineering synthesis.
- Confidence: medium
- Boundary: ReAct 证据支持 reasoning/action/observation 交替；现代 runtime/state/trace/guardrail 拆分是工程综合。

## 复习触发

- 为什么说 Agent Loop 的关键不是“多想几步”，而是 observation 回到下一轮？
- 用一个测试失败或网页操作例子，说明 loop、state、workflow、trace 分别负责什么。
- 如果一个 Agent 无限重试同一个工具，你会从 loop 的哪几个边界排查？

## 相关链接

- [[Agent]]
- [[ReAct]]
- [[Observation]]
- [[Tool Calling]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Trace]]
- [[Evaluation]]
