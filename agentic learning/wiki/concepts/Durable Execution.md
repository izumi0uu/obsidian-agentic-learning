---
type: concept
topic:
  - agent
  - workflow
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Agent Loop]]"
  - "[[Memory]]"
  - "[[Replay]]"
  - "[[Agent Harness]]"
---

# Durable Execution

## 一句话

Durable Execution 是让长任务可以暂停、恢复、重试、记录状态并在失败后继续执行的运行能力。

## 概念详解

Agent 任务一旦超过单次模型调用，就会遇到运行时问题：工具失败、网络超时、用户迟迟不审批、进程重启、上下文被压缩、步骤执行到一半但副作用已经发生。Durable Execution 关注的不是“模型怎么想”，而是 runtime 如何把任务拆成可持久化、可恢复、可审计的步骤。

它通常依赖 checkpoint、workflow state、重试策略、幂等键、事件日志和人工等待点。模型可以参与规划下一步，但“已经执行到哪一步”“哪些工具调用成功了”“失败后能不能重试”“重启后从哪里恢复”属于 [[Agent Harness]] / workflow runtime 的责任。

代表生态包括 Temporal、Restate、Inngest、LangGraph durable execution 等。它们的共同点不是都服务 Agent，而是都把长流程从脆弱的内存调用变成可恢复的运行记录。

## 它解决什么问题

Agent 任务可能持续几分钟到几天，中途会遇到网络失败、工具失败、人工等待、进程重启和模型错误。没有 durable execution，任务状态容易丢失，系统只能重新开始或靠人肉回忆恢复。

它还解决“失败后应该从哪一步继续”的问题：如果付款工具已经成功，就不能简单重放整个任务；如果只是检索接口超时，则可以安全重试。

## 它不是什么

Durable Execution 不是 [[Memory]] 本身。它保存的是运行状态、步骤进度、事件和恢复点；长期用户偏好、项目知识和经验仍属于 memory 或数据库层。

它也不是“自动保证正确”。durable 只能让流程可恢复，不能替你判断计划是否合理、工具参数是否安全、业务规则是否满足。

它也不等于备份聊天记录。真正的 durable execution 要知道步骤边界、副作用边界和恢复策略，而不只是保存一段 transcript。

## 最小例子

```text
step 1 retrieve data
step 2 summarize candidate action
step 3 wait for human approval
step 4 call external tool
step 5 record idempotency key and result
step 6 retry only transient failures
step 7 resume after process restart
```

如果系统在 step 4 后崩溃，恢复时应该先读取 checkpoint，确认外部工具是否已经执行成功，而不是盲目再执行一次。

## 常见误解和风险

- 重试不可逆动作可能造成重复付款、重复邮件或重复写入。
- 状态持久化也需要权限和隐私控制。
- durable 不等于正确，仍然要 eval、audit 和人工边界。
- 只保存最终答案不够；恢复需要知道中间步骤、工具结果和副作用状态。

## 边界细节

和 [[Replay]] 的边界：durable execution 是运行时继续执行的能力；replay 更偏用历史记录复现、调试或评估。一个系统可以把 durable event log 用于 replay，但二者目标不同。

和 [[Agent Loop]] 的边界：Agent loop 描述观察、思考、行动的循环；durable execution 负责循环跨时间、跨进程、跨失败边界还能继续。

和 [[Agent State]] 的边界：state 是“当前是什么状态”；durable execution 是“如何持久化、恢复和推进状态”。

## 现代性状态

Durable Execution 是当前工程实践。

- 基础思想来自长期存在的 workflow engine、job queue、transaction log 和 checkpoint。
- 在现代 Agent 中，它变成长任务、human-in-the-loop、tool retry、context compaction 和 crash recovery 的核心 runtime 能力。
- 前沿 / 易变部分是具体框架如何暴露 durable graph、session、checkpoint store、interrupt 和 resume API。

## 现代系统怎么吸收 Durable Execution 的价值

现代 Agent framework 通常把模型输出放在 workflow 节点里，再由 runtime 负责 checkpoint、重试、等待、恢复和可观测性。这样模型不需要在 prompt 里“记住自己执行到哪里”，而是从持久化 state 中恢复上下文。

这也让人工审批成为流程的一部分：系统可以在审批节点暂停，等待用户确认后继续，而不是让一次长对话一直占着上下文窗口。

## 证据锚点

- Evidence type: engineering source note / infrastructure source — [[Agent 工程基础设施主源]]。
- Boundary: 当前卡片基于 source note 的基础设施主题做工程综合，支持 durable execution 的问题域和代表生态；不声称证明某一产品的具体 API 行为。
- Engineering synthesis: 幂等、副作用边界、checkpoint、resume 与 human-in-the-loop 的关系是运行时设计总结，需要在具体框架文档中二次核对。
- Confidence: medium。

## 复习触发

- Durable execution 和 Memory 最容易混淆在哪里？
- 为什么重试工具调用前必须先判断副作用边界？
- 如果一个 Agent 等待人工审批 24 小时，哪些状态必须持久化？

## 相关链接

- [[Agent Loop]]
- [[Memory]]
- [[Replay]]
- [[Agent Harness]]
