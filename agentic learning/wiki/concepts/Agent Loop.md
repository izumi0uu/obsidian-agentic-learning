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

Agent Loop 是 Agent 的行动反馈循环：系统围绕目标反复观察状态、决定下一步、执行动作、接收 [[Observation]]，再把结果写回上下文、[[Agent State]] 或 [[Trace]]，直到任务完成、失败或需要人类接管。

## 概念详解

Agent Loop 之所以重要，是因为 Agent 面对的任务通常不是一次文本补全就能解决。代码修复要看测试结果，网页任务要看页面变化，RAG 要看检索结果是否足够，工具调用要看 API 返回什么。每一次外部反馈都会改变“下一步应该做什么”。如果系统没有 loop，LLM 只能在初始上下文里猜测；如果有 loop，系统可以把外部世界的结果变成下一轮决策依据。

[[ReAct - Synergizing Reasoning and Acting in Language Models]] 是理解这个概念的经典入口。当前 source note 摘要里把 ReAct 的核心写成：reasoning trace、Action 和 [[Observation]] 交替出现，外部环境或工具返回的 observation 会改变后续推理。这里的重点不是某个固定字符串格式，而是“推理 / 行动 / 反馈”被放进同一个循环。ReAct 论文证据支持的是这种交替范式：只推理容易幻觉和错误传播，只行动缺少计划和状态跟踪，外部反馈可以帮助修正下一步。

但现代 Agent Loop 不能等同于裸 ReAct prompt。工程系统通常把 loop 拆成几层：模型负责提出下一步意图，[[Tool Calling]] 把 action 变成结构化调用，runtime 执行工具并拿到 observation，[[Agent State]] 保存当前目标、已完成步骤、错误和下一步依据，[[Trace]] 记录真实执行轨迹，[[Evaluation]] 或停止条件决定是否继续。也就是说，现代 loop 更像“runtime 控制的反馈系统”，不是 LLM 在脑内自己循环。

官方/工程文档给这个概念补了现代边界。[[LangGraph 官方文档]] 的 source note 把 LangGraph 描述为用图结构组织 Agent workflow，让状态、节点、边和循环变成显式工程对象；这说明 loop 在框架里通常不是自由文本，而是图、节点、状态和边的运行。[[OpenAI Agents SDK 文档]] 的 tracing 补充说明模型调用、工具调用、handoff、guardrail 等运行时事件可以被组织成 trace；这说明 loop 的每一步应该可观察、可调试，而不是只保存在聊天上下文里。[[OpenAI - A Practical Guide to Building Agents]] 和 [[Anthropic - Building Effective Agents]] 则提醒：构建 Agent 不只是让模型自由发挥，还要给任务、工具、边界和评估；很多场景简单 workflow 比高自主 loop 更可靠。

因此，Agent Loop 可以理解为三层合成概念：论文层的 “reasoning / action / observation 交替”，框架层的 “stateful graph / workflow / runtime control”，工程层的 “权限、停止、trace、eval、人类接管”。这三层不能混在一起说：ReAct 解释了为什么反馈循环有价值；LangGraph / Agents SDK 说明现代系统如何把循环工程化；guardrails / evaluation / human-in-the-loop 说明循环为什么需要边界。

## 它解决什么问题

没有 Agent Loop，系统只能一次性给出答案，无法根据真实反馈修正。比如模型说“我已经修复测试”，但如果不运行测试、不读取失败日志、不把新日志写回下一轮，它只是声明成功；真正的 Agent Loop 会把测试结果作为 observation，再决定继续修改、回滚、请求帮助或停止。

Agent Loop 也解决“环境不可预知”的问题。网页按钮可能不存在，检索结果可能为空，工具参数可能报错，用户可能拒绝授权。Loop 让系统可以在每次外部反馈之后调整策略，而不是把所有步骤一次性写死。

## 它不是什么

Agent Loop 不是固定 prompt 模板。`Thought -> Action -> Observation` 是理解 ReAct 的学习入口，但现代系统常用结构化 tool call、state graph、checkpoint、trace 和 guardrail 承载同样的循环价值。

Agent Loop 不是 [[Agent Workflow]] 的同义词。Loop 描述一次行动如何根据反馈继续；workflow 描述多个步骤、分支、审批、handoff 和循环如何被组织。一个 workflow 里可以包含多个 loop，也可以完全是固定流程。

Agent Loop 也不是可靠性保证。没有停止条件、权限边界、预算、trace 和 evaluation 的循环，可能只是更快地重复错误。

## 最小例子

任务：帮我修一个测试失败。

```text
observe: 读取失败日志
plan: 判断可能是断言或 fixture 过期
act: 修改最小相关代码
evaluate: 重新跑目标测试
observe: 如果仍失败，读取新日志；如果通过，停止并报告证据
```

关键点：测试输出不是附属信息，而是下一轮行动的输入。如果测试结果没有被写回上下文 / state / trace，这个系统并没有真正闭环。

## 常见误解 / 风险

- 误解：只要让模型多轮对话，就是 Agent Loop。问题是多轮聊天不一定有外部 action，也不一定把 observation 写入 state。
- 误解：让模型自评就等于 evaluation。自评可能把错误解释得更合理，但不能替代测试、用户反馈、规则检查或人工复核。
- 风险：observation 太弱或未结构化保存，模型下一轮看不到真正关键的环境变化。
- 风险：循环没有 budget、timeout、approval gate 或人工接管，导致无限重试、重复调用工具或执行危险动作。

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
- 为什么：行动后接收外部反馈并用于下一步决策，是 Agent 的稳定基础；但裸 ReAct 文本格式属于历史过渡，现代框架通常把它拆进 tool calling、state graph、guardrails、tracing 和 evaluation。
- 稳定部分：行动必须产生 observation，observation 必须影响下一轮决策或停止判断。
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

- Paper source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Paper anchors: [[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]], [[ReAct - Synergizing Reasoning and Acting in Language Models#图片录入：ReAct Tools / LLM / Environment]]
- Official/practice sources: [[OpenAI - A Practical Guide to Building Agents]], [[Anthropic - Building Effective Agents]], [[LangGraph 官方文档]], [[OpenAI Agents SDK 文档]]
- Official/practice anchors: [[OpenAI - A Practical Guide to Building Agents#一句话]], [[Anthropic - Building Effective Agents#边界提醒]], [[LangGraph 官方文档#一句话]], [[OpenAI Agents SDK 文档#Tracing 补充]]
- Evidence type: paper source note + official docs/source notes + engineering synthesis.
- Confidence: medium
- Boundary: ReAct 证据支持 reasoning/action/observation 交替；现代 runtime/state/trace/guardrail 拆分是工程综合理解，不是 ReAct 论文原文逐条声明。

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
