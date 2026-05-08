---
type: concept
topic:
  - agent
  - reasoning
  - tool-use
status: growing
created: 2026-05-05
updated: 2026-05-08
last_checked: 2026-05-08
freshness: watch
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[LangGraph 官方文档]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[Anthropic - Building Effective Agents#为什么收]]"
  - "[[OpenAI - A Practical Guide to Building Agents#为什么收]]"
  - "[[LangGraph 官方文档#为什么收]]"
related:
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Reasoning Trace]]"
  - "[[Observation]]"
  - "[[Planning]]"
  - "[[Agent Harness]]"
  - "[[Guardrails]]"
  - "[[Evaluation]]"
---

# ReAct

## 一句话

ReAct 是让语言模型交替生成 reasoning traces 和 actions 的 Agent 模式。

## 它解决什么问题

纯推理容易脱离外部事实并产生幻觉；纯行动又缺少可解释的计划和状态跟踪。ReAct 把“想”和“做”交替起来，让工具或环境反馈修正后续推理。

## 它不是什么

ReAct 不是完整的生产级 Agent 平台。

它也不是所有 Agent 都必须采用的固定格式。真实系统可能隐藏推理、改用结构化 planner，或把行动循环封装在框架里。

更细一点：ReAct 不是“Agent 的同义词”。它是理解 [[Agent Loop]] 的经典模式之一，但现代系统常把可预测部分做成 workflow，只把不可预测、需要环境反馈和动态决策的部分交给 agent loop。

## 最小例子

```text
Thought: 我需要查资料。
Action: Search[问题]
Observation: 搜索结果
Thought: 结果不够，换关键词。
Action: Search[新关键词]
```

## 边界细节

ReAct 的价值在于揭示 [[Agent Loop]] 的核心：行动不是一次性输出，而是和观察反馈绑定在一起。

## 现代系统怎么吸收 ReAct 的局限

截至 2026-05-08，生产 Agent 很少只靠一段 `Thought -> Action -> Observation` 提示词裸跑。更常见的是保留“模型根据观察决定下一步”的核心，但把脆弱部分移到工程层：

- 对可预测任务，用 prompt chaining、routing、parallelization 等 workflow，让路径由代码或图结构控制。
- 对不可预测任务，用 agent loop、state graph 或 orchestrator-workers，让模型动态拆解任务，但由 [[Agent Harness]] 管住状态、权限、trace、重试和停止条件。
- 对 Action 格式问题，用 [[Tool Calling]]、JSON schema、typed output、参数校验和失败重试，减少靠自然语言解析动作。
- 对局部最优和原地循环，用 [[Planning]]、evaluator-optimizer、trajectory evaluation、最大迭代数、预算上限、checkpoint 和 [[Human-in-the-loop]]。
- 对提示词脆弱性，用版本化 prompt、回归 eval、observability trace、清晰工具文档和分层 [[Guardrails]]。

所以现代 Agent 不是“抛弃 ReAct”，而是把 ReAct 从一个 prompt 模板，降级成一个可被框架、工具协议、评测和权限系统包住的行动循环思想。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Source: [[Anthropic - Building Effective Agents]]
- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Source: [[LangGraph 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent Loop]]
- [[Tool Calling]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Planning]]
- [[Agent Harness]]
- [[Guardrails]]
- [[Evaluation]]
