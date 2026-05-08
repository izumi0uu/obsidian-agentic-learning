---
type: concept
topic:
  - agent
  - workflow
  - memory
status: seed
created: 2026-05-08
updated: 2026-05-08
source:
  - "[[Agent Framework]]"
  - "[[LangGraph 官方文档]]"
evidence:
  - "[[Agent Framework#框架怎样接管 prompt loop]]"
  - "[[LangGraph 官方文档#为什么收]]"
last_checked: 2026-05-08
freshness: watch
conflicts: []
related:
  - "[[Agent Framework]]"
  - "[[Agent Loop]]"
  - "[[Memory]]"
  - "[[Context Engineering]]"
  - "[[Trace]]"
---

# Agent State

## 一句话

Agent State 是 Agent 在一次任务运行中用来保存当前位置、已知信息、中间结果和下一步依据的显式状态。

## 它解决什么问题

如果只靠 prompt 和上下文窗口，Agent 很容易忘记任务进度、重复做事、丢掉工具结果，或者不知道自己已经尝试过什么。

Agent State 把这些运行时信息变成框架可读写的结构，例如当前目标、计划、待办、工具结果、错误、审批状态和最近 observation。

## 它不是什么

Agent State 不是 [[Memory]] 的同义词。

[[Memory]] 更偏跨时间保存和复用信息；Agent State 更偏当前运行里的工作状态。一个任务结束后，state 可能被丢弃、归档成 [[Trace]]，或者提炼成长期 memory。

Agent State 也不是 context window。context window 是模型本次调用能看到的内容；state 是框架保存的结构化运行数据，只有被选中写入上下文时，模型才会看到。

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
needs_human_approval: false
```

## 常见误解

- 把所有历史对话都塞进 state，会让 state 变成噪音仓库。
- state 持久化不等于 Agent 变聪明；它只是让运行过程更可恢复。
- state 里保存敏感信息时，同样需要权限、过期和审计策略。

## 边界细节

可以把三者分开：

- [[Agent State]]：当前任务怎么走到这里。
- [[Memory]]：过去哪些信息值得以后复用。
- [[Trace]]：这次执行到底发生过什么。

State 是框架接管 prompt loop 的关键：模型不必在自然语言里“记住一切”，框架可以在每一步把必要 state 注入上下文，并在工具返回后更新 state。

## 证据锚点

- Source: [[Agent Framework]]
- Source: [[LangGraph 官方文档]]
- Anchor: [[Agent Framework#框架怎样接管 prompt loop]]
- Confidence: medium

## 相关链接

- [[Agent Framework]]
- [[Agent Loop]]
- [[Memory]]
- [[Context Engineering]]
- [[Trace]]
