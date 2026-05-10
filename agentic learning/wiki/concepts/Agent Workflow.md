---
type: concept
topic:
  - agent
  - workflow
status: growing
created: 2026-05-08
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent Framework]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Agent Framework#框架怎样接管 prompt loop]]"
  - "[[Agent Framework#现代系统怎么吸收 Agent Framework 的价值 / 局限]]"
  - "[[Anthropic - Building Effective Agents#一句话]]"
  - "[[Anthropic - Building Effective Agents#边界提醒]]"
  - "[[OpenAI - A Practical Guide to Building Agents#一句话]]"
  - "[[LangGraph 官方文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#一句话]]"
related:
  - "[[Agent Framework]]"
  - "[[Agent Loop]]"
  - "[[Agent State]]"
  - "[[Planning]]"
  - "[[Handoff]]"
  - "[[Durable Execution]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
---

# Agent Workflow

## 一句话

Agent Workflow 是把 Agent 任务组织成可控制步骤、分支、循环、审批和交接的流程结构，让模型自主性只出现在合适节点。

## 它解决什么问题

纯 prompt loop 容易让模型临场决定所有事情：先做什么、何时调用工具、失败后怎么重试、什么时候交给别人、什么时候停。Agent Workflow 把可预测路径放进工程流程，只把需要判断的节点交给模型或 Agent loop。

Anthropic 的工程建议提供了一个重要边界：很多任务用 workflow 就足够，复杂自主 Agent 应该在任务确实需要动态判断、多步反馈和不确定环境时再引入。

## 它不是什么

Agent Workflow 不是 [[Agent Loop]] 的同义词。Loop 描述观察、决策、行动、反馈的基本循环；workflow 描述系统如何把这些循环、工具、人类确认和角色交接组织成任务路径。

Agent Workflow 也不等于 [[Agent Framework]]。Framework 是软件工具箱；workflow 是你用工具箱搭出来的路径。

它也不等于 [[Planning]]。Planning 偏“目标如何拆成步骤”；workflow 偏“系统如何执行这些步骤，并在分支、失败、审批和交接中保持可控”。

## 最小例子

```text
triage request
-> decide route
-> retrieve context
-> draft answer
-> if high risk: ask human approval
-> call allowed tool
-> trace result
-> evaluate final answer and trajectory
```

这里模型可能参与 route、draft 或异常处理，但付款、删除、发送等高风险动作由 workflow 放在 approval gate 后面。

## 常见误解 / 风险

- 误解：Workflow 越复杂越好。风险是简单任务被拆成高延迟、高成本、难调试的流程。
- 误解：Workflow 会消灭模型决策。实际目标是把模型决策放在需要判断的节点，而不是让它控制所有节点。
- 误解：所有步骤都让 Agent 自主决定才先进。风险是工程边界退回脆弱 prompt loop。
- 风险：workflow 写死过多，遇到异常无法恢复；放开过多，又无法审计、评估和控制。

## 边界细节

常见 workflow pattern 包括：

- prompt chaining：一步输出成为下一步输入。
- routing：根据任务类型选择不同路径或模型。
- parallelization：多个子任务并行执行再合并。
- orchestrator-workers：一个 orchestrator 拆任务，多个 worker 执行。
- evaluator-optimizer：生成后由评估器检查并迭代改进。
- handoff：把任务交给另一个 Agent 或人类。

边界判断：如果路径主要由工程预先定义，它更像 workflow；如果下一步主要由模型根据 observation 动态选择，它更像 Agent loop。真实系统常混合：稳定路径用 workflow 固定，不确定节点进入 loop。

## 现代性状态

- 判定：current-practice
- 为什么：workflow 没有过时；它从“单独卖点”变成 Agent 系统的内部控制结构。现代框架仍然依赖 graph、router、handoff、approval、checkpoint 和 evaluator loop。
- 稳定部分：用 workflow 限制 Agent 自由度，把可预测路径工程化，把不确定判断留给模型。
- 易变部分：具体框架的节点接口、图语法、checkpoint 存储、handoff API、可视化 trace 和部署方式。
- 复查点：当主流框架对 workflow vs agent 的边界有新共同定义时更新本卡；单个平台 API 变化优先写 source note。

## 现代系统怎么吸收 Agent Workflow 的价值 / 局限

现代系统通常用 workflow 做控制层：

- 固定高确定性路径，例如检索、格式校验、引用检查、审批和最终验收。
- 在低确定性节点调用模型，例如 routing、规划、异常分析、草稿生成和工具选择。
- 用 [[Agent State]] 保存每个节点的输入输出、错误和下一步依据。
- 用 [[Durable Execution]] 支持长任务暂停、恢复、重试和人工等待。
- 用 [[Trace]] / [[Evaluation]] 检查路径是否安全、经济、合规，而不只看最终答案。

局限是：workflow 需要设计。设计过窄会卡在异常路径，设计过宽会失去控制；它应该和 eval、trace、human-in-the-loop 一起迭代，而不是一次画完就固定。

## 证据锚点

- Source: [[Anthropic - Building Effective Agents]]
- Anchor: [[Anthropic - Building Effective Agents#一句话]] / [[Anthropic - Building Effective Agents#边界提醒]]
- Source: [[Agent Framework]]
- Anchor: [[Agent Framework#框架怎样接管 prompt loop]] / [[Agent Framework#现代系统怎么吸收 Agent Framework 的价值 / 局限]]
- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Anchor: [[OpenAI - A Practical Guide to Building Agents#一句话]]
- Source: [[LangGraph 官方文档]] / [[OpenAI Agents SDK 文档]]
- Anchor: [[LangGraph 官方文档#一句话]] / [[OpenAI Agents SDK 文档#一句话]]
- Evidence type: official docs/source notes + engineering synthesis.
- Confidence: medium
- Boundary: workflow patterns 和 graph/handoff/approval 的组合是工程综合；具体 API 和平台能力属于 watch。

## 复习触发

- 为什么说 workflow 不是 Agent Loop，也不是 Agent Framework？
- 给一个“固定 workflow 足够”的任务，再给一个“需要 Agent loop”的任务。
- 如果一个 workflow 在异常路径上卡死，你会从 state、handoff、durable execution、trace 哪几层排查？

## 相关链接

- [[Agent Framework]]
- [[Agent Loop]]
- [[Agent State]]
- [[Planning]]
- [[Handoff]]
- [[Durable Execution]]
- [[Trace]]
- [[Evaluation]]
