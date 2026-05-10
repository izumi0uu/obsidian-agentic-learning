---
type: concept
topic:
  - agent
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]]"
  - "[[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？#页面正文]]"
related:
  - "[[Agent Loop]]"
  - "[[ReAct]]"
  - "[[Environment Observation 类型对比]]"
  - "[[Tool Calling]]"
  - "[[Agent State]]"
  - "[[Trace]]"
  - "[[Guardrails]]"
---

# Observation

## 一句话

Observation 是 Agent 执行动作后，由工具、环境、测试、人类或安全策略返回的反馈；它会被写回上下文、[[Agent State]] 或 [[Trace]]，影响下一轮模型决策。

## 它解决什么问题

Agent 需要知道自己的动作产生了什么结果，才能决定下一步。Observation 把外部世界的状态带回循环中，让 [[ReAct]] 不只是“模型自己想”，而是“想一下、做一下、看结果、再调整”。

它主要解决三件事：

- 事实校准：用搜索结果、数据库结果、执行日志或页面状态修正模型内部知识。
- 行动闭环：让下一轮推理建立在真实动作结果上，而不是建立在模型想象的结果上。
- 过程可追踪：把工具返回、错误信息、环境变化记录下来，方便后续 [[Replay]]、调试和 [[Evaluation]]。

## 它不是什么

Observation 不是模型自己的想法。模型的分析属于 [[Reasoning Trace]] 或内部推理；Observation 是动作之后从外部返回的信号。

Observation 也不是 Action。Action 是“要调用什么、带什么参数”，Observation 是“调用之后发生了什么、返回了什么”。

Observation 也不是 Environment。Environment 是动作发生的外部世界或系统；Observation 是这个外部世界对某次动作返回的反馈。这个边界可以看 [[Environment Observation 类型对比]]。

Observation 不是完整的 Memory 或 State。它通常是一轮动作的反馈片段，进入长期记忆或任务状态之前还需要筛选、摘要和归档。

它也不一定可信。网页、工具返回值、检索片段、终端输出或环境状态可能错误、过期、噪声很大，甚至被 [[Prompt Injection]] 或 [[Tool Poisoning]] 污染。

## 来源类型

Observation 不只来自工具调用。更准确地说，它是 Agent 动作后被 runtime 收集到的外部反馈，常见来源包括：

- tool result：搜索结果、数据库查询结果、API 返回值、计算器结果。
- environment state：任务环境的新状态，例如游戏状态、机器人传感器读数、文件系统变化、命令执行后的工作区状态。
- user feedback：用户确认、用户纠错、人工审批、人工补充信息。
- test output：单元测试、lint、typecheck、CI、benchmark 或脚本运行结果。
- browser state：网页 DOM、截图、URL、表单状态、按钮是否可见、点击后的页面变化。

## 最小例子

经典 ReAct 形式：

```text
Thought: 我需要查一下最新信息。
Action: search
Action Input: ReAct paper authors
Observation: 搜索结果显示 ReAct 论文作者包括 Yao 等人。
Thought: 现在我可以把作者信息放进回答里。
Final Answer: ...
```

代码 Agent 形式：

```text
Action: run_tests
Action Input: pytest tests/test_agent_loop.py
Observation: 2 failed, 14 passed；失败日志显示 Observation 没有写入 state。
```

这两个例子里，Observation 都不是模型“觉得发生了什么”，而是外部动作返回给 Agent runtime 的结果。

## 工程处理

现代 Agent 框架通常不会把 Observation 原样无脑塞回 prompt，而会做一层运行时处理：

- 结构化：保留工具名、参数、返回值、错误码、耗时、来源和时间戳。
- 校验：检查 schema、权限、返回大小、敏感信息和异常状态。
- 压缩：长网页、日志或搜索结果先摘要，再放入上下文，原始结果留在 [[Trace]] 或外部存储。
- 溯源：记录这个 Observation 来自哪个工具、哪次调用、哪份文档或哪个页面。
- 防护：对外部网页、文档和工具返回值做 [[Guardrails]]，避免把恶意指令当成系统命令。
- 复查：高风险决策前用二次检索、测试、人工确认或交叉来源验证关键 Observation。

## 风险

- 污染：网页、文档、工具返回值里可能夹带恶意指令或错误信息，典型问题是 [[Prompt Injection]] 和 [[Tool Poisoning]]。
- 过期：搜索结果、缓存数据、页面状态或环境状态可能已经不是当前真实状态。
- 格式不稳定：工具返回字段、错误码、HTML/DOM 结构或日志格式变化，会让解析和后续推理失稳。
- 被模型误读：模型可能把错误日志、网页广告、检索摘要或用户反馈理解错，导致下一步 Action 走偏。

## 边界细节

没有 Observation，[[Agent Loop]] 容易退化成一次性计划生成。

在经典 ReAct prompt 里，Observation 常被追加成一行文本，再把完整历史传回模型；在现代 [[Tool Calling]] / agent framework 里，Action 通常已经结构化，但 Observation 仍然需要 runtime 负责执行、保存、过滤、摘要和回填。

也就是说，Tool Calling 让“调用工具”更可靠，但不自动解决“工具结果是否可信、是否该进入上下文、如何影响下一步”的问题。Observation 的质量，直接决定 Agent 下一轮决策的地基。

## 费曼检查

- 为什么 Observation 不是模型自己的 Thought？
- 如果第一轮 Observation 是错的，ReAct 后面的推理会发生什么？
- 为什么现代框架要把 Observation 放进 state/trace，而不是只拼进 prompt？

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Source: [[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]
- Anchor: ReAct source note 的方法摘要；小林 ReAct 页对 Thought / Action / Observation 分工、系统填回历史、错误传播的说明。
- Confidence: medium

## 相关链接

- [[Agent Loop]]
- [[ReAct]]
- [[Environment Observation 类型对比]]
- [[Tool Calling]]
- [[Agent State]]
- [[Trace]]
- [[Guardrails]]
- [[Prompt Injection]]
- [[Tool Poisoning]]
