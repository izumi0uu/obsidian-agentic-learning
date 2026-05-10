---
type: concept
topic:
  - agent
  - workflow
status: seed
created: 2026-05-08
updated: 2026-05-10
source:
  - "[[Agent Framework]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[LangGraph 官方文档]]"
evidence:
  - "[[Agent Framework#框架怎样接管 prompt loop]]"
  - "[[Anthropic - Building Effective Agents#为什么收]]"
  - "[[LangGraph 官方文档#为什么收]]"
last_checked: 2026-05-10
freshness: watch
conflicts: []
related:
  - "[[Agent Framework]]"
  - "[[Agent Loop]]"
  - "[[Planning]]"
  - "[[Handoff]]"
  - "[[Durable Execution]]"
  - "[[Multi-agent Orchestration]]"
---

# Agent Workflow

## 一句话

Agent Workflow 是把 Agent 任务拆成可控制步骤、分支、循环和交接的流程结构。

## 它解决什么问题

纯 prompt loop 容易让模型临场决定所有事情：先做什么、何时调用工具、失败后怎么重试、什么时候交给别人。Agent Workflow 把可预测路径放进工程流程，只把需要判断的节点交给模型。

## 它不是什么

Agent Workflow 不是 [[Agent Loop]] 的同义词。

[[Agent Loop]] 描述观察、决策、行动、反馈的基本循环；Agent Workflow 描述系统把这些循环、工具、人类确认和角色交接怎样组织起来。

Agent Workflow 也不等于 [[Agent Framework]]。Framework 是软件工具箱；workflow 是你在工具箱里搭出来的任务路径。

## 最小例子

```text
triage request
-> decide route
-> retrieve context
-> draft answer
-> if high risk: human approval
-> call tool
-> trace and evaluate result
```

## 常见误解

- Workflow 越复杂不一定越好；简单任务用固定链路更稳。
- Workflow 不是消灭模型决策，而是把模型决策放在合适节点。
- 所有步骤都让 Agent 自主决定，会把工程边界重新退回 prompt。

## 边界细节

常见 workflow pattern 包括：

- prompt chaining：一步输出成为下一步输入。
- routing：根据任务类型选择不同路径或模型。
- parallelization：多个子任务并行执行再合并。
- orchestrator-workers：一个 orchestrator 拆任务，多个 worker 执行。
- evaluator-optimizer：生成后由评估器检查并迭代改进。
- handoff：把任务交给另一个 Agent 或人类。

和 [[Planning]] 的关系：Planning 偏“目标如何拆成步骤”；Agent Workflow 偏“系统如何执行这些步骤，并在分支、失败、审批和交接中保持可控”。

## 现代性状态

Workflow 没有“不流行了”。更准确地说，纯固定 workflow 不适合所有开放任务，但 workflow 作为工程控制层仍然是当前实践。

- 基础地基：workflow 继承的是软件工程里的流程、状态机、DAG、router 和审批思想。
- 历史过渡：把所有步骤都写死、完全没有模型判断的链式 demo，容易显得僵硬；把所有步骤都交给模型临场决定，又会退回脆弱 prompt loop。
- 当前工程实践：稳定路径用 workflow 固定下来，不确定节点才调用模型或 agent loop；需要长任务、重试、人类确认和恢复时，用 graph 或 durable execution 管起来。
- 前沿 / 易变：某个框架对 workflow 的 API 命名、节点接口、checkpoint 存储和可视化 trace 会变，但“用 workflow 限制 Agent 自由度”这个原则相对稳定。

所以用户问“workflow 是不是过时了”时，答案不是“过时”，而是“它从单独卖点退回了 Agent 系统的内部控制结构”。

## 证据锚点

- Source: [[Agent Framework]]
- Source: [[Anthropic - Building Effective Agents]]
- Source: [[LangGraph 官方文档]]
- Anchor: [[Agent Framework#框架怎样接管 prompt loop]]
- Confidence: medium

## 相关链接

- [[Agent Framework]]
- [[Agent Loop]]
- [[Planning]]
- [[Handoff]]
- [[Durable Execution]]
- [[Multi-agent Orchestration]]
