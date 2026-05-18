---
type: concept
topic:
  - agent
  - workflow
  - memory
status: growing
created: 2026-05-08
updated: 2026-05-12
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent Framework]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
evidence:
  - "[[Agent Framework#框架怎样接管 prompt loop]]"
  - "[[Agent Framework#现代系统怎么吸收 Agent Framework 的价值 / 局限]]"
  - "[[LangGraph 官方文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
  - "[[OpenAI - A Practical Guide to Building Agents#一句话]]"
related:
  - "[[Agent Framework]]"
  - "[[Agent Loop]]"
  - "[[Agent Workflow]]"
  - "[[Memory]]"
  - "[[Context Engineering]]"
  - "[[Long-Horizon Context Engineering]]"
  - "[[Trace]]"
  - "[[Durable Execution]]"
---

# Agent State

## 一句话

Agent State 是一次 Agent 运行中被系统保存和更新的工作状态：目标、阶段、已知信息、中间结果、工具反馈、错误、审批状态和下一步依据；有些框架把它作为一等对象显式暴露，有些框架只把它藏在消息历史、session、trace 或外部应用代码里。

## 概念详解

Agent State 之所以需要被单独学习，是因为 Agent 的任务不是静态输入到静态输出，而是一个会随外部反馈变化的运行过程。模型读过什么、工具返回了什么、哪些步骤已经完成、哪里失败过、是否等待人工审批，这些信息如果只散落在 prompt 或聊天上下文里，就很容易被截断、污染或遗忘。State 把“任务走到哪里”从自然语言记忆变成可读写的运行数据。

从机制上看，state 至少包含三类东西：控制状态、工作数据和上下文投影。控制状态回答“当前处在哪个阶段、下一步应该去哪、是否需要停或等人”；工作数据保存工具返回、检索片段、中间草稿、错误和尝试记录；上下文投影决定哪些 state 片段会被注入下一次模型调用。[[LangGraph 官方文档]] 的 source note 把状态、节点、边和循环描述为显式工程对象，适合支持这种 stateful graph 理解；[[OpenAI Agents SDK 文档]] 的 tracing 补充说明运行时的模型调用、工具调用、handoff、guardrail 等事件可以被组织成 trace，这给 state transition 可观察化提供了工程证据。

Agent State 的一个细边界是：它不是“模型当前能看到的全部内容”。框架可以持有很多状态，但每次模型调用只应该看到必要片段；否则 state 会变成另一个大上下文垃圾桶。它也不是长期 [[Memory]]：当前任务的错误日志、一次性审批状态、临时检索结果，不一定值得写入长期记忆。任务结束后，state 可能被丢弃、归档为 [[Trace]]，或者抽取少量稳定事实进入 memory。

现代系统通常把 state 设计成 schema + update rule + checkpoint + trace linkage。schema 让字段可解释；更新规则避免工具结果、人工确认和模型草稿互相覆盖；checkpoint 让长任务可以暂停、恢复、重试；trace linkage 让每次状态变化能被调试和评估。这里的证据边界也要分清：source notes 支持“现代框架把状态/图/trace 显式化”；具体 state schema、context injection 和 memory extraction 的分层，是本卡对工程实践的综合整理。

在 [[Long-Horizon Context Engineering]] 里，Agent State 是 compaction 和结构化笔记的事实来源之一：摘要要保留哪些阶段、错误和下一步，通常取决于 state schema；哪些 state 片段进入下一轮上下文，则由 context projection 决定。

## 它解决什么问题

如果只靠 prompt 和 context window，Agent 很容易忘记任务进度、重复做事、丢掉工具结果，或者不知道自己已经尝试过什么。Agent State 把“任务走到哪里了”变成可读写的结构，而不是让模型在自然语言里凭记忆维持整个过程。

它还解决恢复问题：长任务可能被中断，工具可能失败，人类可能稍后才审批。显式 state 让 runtime 可以暂停、恢复、重试、分支，或者把一次运行归档成 [[Trace]]。

## 它不是什么

Agent State 不是 [[Memory]] 的同义词。Memory 更偏跨时间保存和复用信息；Agent State 更偏当前运行里的工作状态。一次任务结束后，state 可能被丢弃、归档成 trace，或者提炼成长期 memory。

Agent State 也不是 context window。context window 是模型本次调用能看到的内容；state 是框架保存的结构化运行数据，只有被选择性注入上下文时，模型才会看到。

Agent State 也不是普通数据库表。数据库可以存业务数据；Agent State 关注的是运行控制：当前阶段、待办、工具结果、错误、权限和下一步依据。

## 最小例子

```yaml
goal: "整理一篇论文"
phase: "extract_concepts"
plan:
  - "读取 raw note"
  - "创建概念卡"
  - "更新索引"
completed:
  - "读取 raw note"
last_observation: "论文强调 plan-first prompting"
last_error: null
needs_human_approval: false
next_step: "起草概念卡"
```

这里最重要的不是 YAML，而是这些字段让 runtime 和下一轮模型调用知道“现在该从哪里继续”。

## 常见误解 / 风险

- 误解：把所有历史对话都塞进 state 就更安全。风险是 state 变成噪音仓库，反而污染下一轮上下文。
- 误解：state 持久化等于 Agent 变聪明。state 只是让过程可恢复，不能替代判断、工具质量和评估。
- 误解：state 和 memory 可以混用。风险是短期错误、敏感数据或一次性工具结果被错误写入长期记忆。
- 误解：某个框架没有显式 `State` API，就说明它没有 state。更准确地说，它可能没有把 state 作为一等抽象暴露，但消息历史、tool result、session、run trace、workflow local variables 或调用方数据库仍在承担状态职责。
- 风险：state 里保存敏感信息时，同样需要权限、过期、脱敏和审计策略。

## 边界细节

可以把三者分开：

- [[Agent State]]：当前任务怎么走到这里，以及下一步依据是什么。
- [[Memory]]：过去哪些信息值得以后复用。
- [[Trace]]：这次执行到底发生过什么。

State 是框架接管 prompt loop 的关键：模型不必在自然语言里“记住一切”，框架可以每一步只把必要 state 注入上下文，并在工具返回后更新 state。

这里还要切开 `plan 文本`、`Agent State 里的 task list` 和 `context 投影`：

- `plan 文本` 是模型输出的一段计划草稿，可能只是自然语言或临时推理脚手架。
- `Agent State 里的 task list` 是 runtime 可读、可更新、可检查的任务状态，可以记录 `pending / in_progress / done / blocked`、失败原因、依赖关系和下一步依据。
- `context 投影` 是框架从 state、memory、trace、文件、工具结果中挑出本轮模型调用需要看的切片。它不是多模态处理的同义词，也不是把整个 state 原样塞回 prompt。

边界：state 是系统持有的运行事实；context 是给模型看的当前输入投影。把 plan 放进 state 不等于模型每轮都能看到全部 plan；框架仍然需要 context assembly / context engineering 决定放入哪些字段、压缩哪些字段、隐藏哪些字段。

工程边界：state 需要 schema、更新规则和清理策略。没有 schema，state 会变成随手堆文本；没有更新规则，工具结果和人工确认可能覆盖错字段；没有清理策略，旧状态会误导新任务。

框架差异：不是所有 Agent 编排框架都像 [[LangGraph]] 一样把 state graph 放在抽象中心。conversation-first 框架可能主要暴露 message history / speaker selection；SDK 型框架可能暴露 session、run、trace、handoff 或 tool call 事件；轻量工具调用库甚至把状态完全留给应用层数据库或调用方变量。学习时要问的是“状态由谁保存、谁能更新、怎样投影给模型、失败后能否恢复”，而不是只找一个叫 `state` 的字段。

## 现代性状态

- 判定：current-practice
- 为什么：显式 state、state graph、checkpoint、session / run 记录是现代 Agent framework 的核心工程层；但具体字段、存储、恢复 API 和持久化策略仍随框架变化。
- 稳定部分：当前运行需要可读写状态，且只有必要状态应进入模型上下文。
- 易变部分：LangGraph 等框架的节点/边/state reducer/checkpoint API，OpenAI Agents SDK 的 session/tracing 细节，以及各平台对 state 的可视化方式。
- 复查点：当主流框架对 state、memory、trace 的边界有新稳定定义时更新本卡。

## 现代系统怎么吸收 Agent State 的价值 / 局限

现代系统通常把 state 分成几层处理：

- runtime state：当前 run 的目标、阶段、工具结果、错误和审批状态。
- checkpoint：让长任务可以暂停、恢复、重试或回滚。
- context injection：只把当前模型调用需要的 state 片段放进上下文。
- context projection：把 state / memory / trace 中和当前决策有关的信息压缩、排序、过滤成模型可用输入，避免把完整运行状态变成上下文垃圾桶。
- trace linkage：把 state transition 和工具调用记录到 trace，方便调试和评估。
- memory extraction：任务结束后，只把值得长期复用的信息提炼进 memory。

局限是：state 让过程可控，但不会自动判断哪些信息重要。state 设计过粗会丢信息，过细会污染上下文；这部分需要工程 schema、评估和复盘不断校准。

## 证据锚点

- Source: [[Agent Framework]]
- Anchor: [[Agent Framework#框架怎样接管 prompt loop]] / [[Agent Framework#现代系统怎么吸收 Agent Framework 的价值 / 局限]]
- Source: [[LangGraph 官方文档]]
- Anchor: [[LangGraph 官方文档#一句话]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: [[OpenAI Agents SDK 文档#Tracing 补充]]
- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Anchor: [[OpenAI - A Practical Guide to Building Agents#一句话]]
- Evidence type: official docs/source notes + local engineering synthesis.
- Confidence: medium
- Boundary: source notes支持“框架/图/trace 接管运行结构”；state schema/checkpoint/context-injection/context-projection 的拆分是工程综合。

## 复习触发

- 为什么 Agent State 不是 Memory，也不是 context window？
- 用一个长任务中断恢复的例子，说明 state、checkpoint、trace 分别保存什么。
- 如果一个 Agent 反复忘记已经调用过某个工具，你会检查 state 的哪些字段？
- 用一句话区分 plan 文本、Agent State 里的 task list、context 投影。

## 相关链接

- [[Agent Framework]]
- [[Agent Loop]]
- [[Agent Workflow]]
- [[Memory]]
- [[Context Engineering]]
- [[Long-Horizon Context Engineering]]
- [[Trace]]
- [[Durable Execution]]
