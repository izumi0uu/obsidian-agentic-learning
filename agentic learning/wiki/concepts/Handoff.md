---
type: concept
topic:
  - agent
  - workflow
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Agent Framework]]"
  - "[[Human-in-the-loop]]"
  - "[[A2A]]"
---

# Handoff

## 一句话

Handoff 是一个 Agent、workflow 节点或人类角色把任务、上下文和控制权交给另一个执行者的机制。

## 概念详解

Handoff 解决的是“谁应该接着处理”而不是“模型下一句说什么”。在多角色 Agent 系统里，triage agent 可能只负责判断问题类型，billing agent 负责账单工具，coding agent 负责仓库修改，人类负责审批高风险动作。Handoff 把任务从一个责任边界移动到另一个责任边界。

一个好的 handoff 至少包含三件事：交接原因、必要上下文、接收方权限。交接原因说明为什么当前 agent 不继续做；上下文避免接收方重复问问题；权限边界避免接收方拿到不需要的工具或数据。

在 runtime 上，handoff 可以是框架内的 agent 切换、workflow 节点跳转、人工接管，也可以跨系统进入协议层。但学习时要先把“任务交接模式”和“跨 Agent 协议”分开。

## 它解决什么问题

单个 Agent 不一定适合所有任务。客服、代码、研究、审批、支付等步骤可能需要不同角色、权限和工具。Handoff 让任务在角色之间流转，同时保留必要上下文和责任边界。

它还解决专门化问题：不是让一个大 agent 拿所有工具，而是让不同角色只在自己的边界内行动。

## 它不是什么

Handoff 不是多 Agent 越多越好。过多交接会增加延迟、上下文丢失和责任不清。

它也不等于 [[A2A]]。A2A 更偏协议互操作；handoff 是任务交接模式，可以发生在同一个框架内部，也可以发生在人和 agent 之间。

它也不等于简单函数调用。工具调用通常由同一个 agent 请求外部动作；handoff 是控制权或责任主体发生变化。

## 最小例子

```text
triage agent
-> billing agent（只带账单上下文和账单工具权限）
-> human approval（确认退款）
-> execution agent（执行已批准动作）
```

如果 triage agent 把所有聊天记录、所有工具权限和模糊目标都直接交出去，这不是好的 handoff，而是责任边界失效。

## 常见误解和风险

- 交接时丢失上下文会导致重复问问题。
- 权限没有收窄时，专门 agent 可能拿到过多工具。
- 交接链太长会增加延迟和不可解释性。
- 没有记录交接原因时，后续 audit 很难判断为什么换人或换 agent。

## 边界细节

Handoff 的核心边界是“控制权 / 责任归属”。如果只是同一个 agent 调用检索工具，那不是 handoff；如果任务从研究 agent 转给写代码 agent，且后者接管下一步决策，那就是 handoff。

和 [[Human-in-the-loop]] 的边界：human-in-the-loop 是一种可能的 handoff 接收方，但 handoff 也可以发生在 agent 到 agent 之间。

和 [[Agent Framework]] 的边界：framework 提供声明 handoff、传递上下文和约束工具权限的机制；handoff 是这种机制承载的任务模式。

## 现代性状态

Handoff 是当前工程实践。

- 基础思想来自工作流分派、客服转接、权限分层和人类组织协作。
- 在现代 Agent framework 中，它被实现为 agent routing、handoff tool、graph edge、human approval node 或 escalation path。
- 前沿 / 易变部分是具体 SDK 怎样表达 handoff、传哪些 metadata、如何和 tracing / guardrails / permissions 集成。

## 现代系统怎么吸收 Handoff 的价值

现代系统会把 handoff 放进 runtime 和 trace，而不是只让模型在自然语言里说“交给另一个专家”。框架可以记录交接边、接收方、输入上下文、工具范围和最终结果，方便调试、评估和权限审计。

这也让“少而清晰的 agent 分工”比“很多人格化 agent 聊天”更重要：handoff 的价值在边界清楚，而不是角色名字多。

## 证据锚点

- Evidence type: official docs note — [[OpenAI Agents SDK 文档]]，用于支持 Agents SDK 语境下的 handoff / agent 编排入口。
- Evidence type: engineering source note — [[Agent 工程基础设施主源]]，用于支持 runtime / infrastructure 视角的任务交接边界。
- Boundary: 当前卡片是模式级解释，不等同于 A2A 协议规范，也不证明任一 SDK 的最新参数名。
- Engineering synthesis: “交接原因、必要上下文、接收方权限”是学习用检查框架，应在具体系统设计中落实到 trace、state 和 permission 字段。
- Confidence: medium。

## 复习触发

- Handoff 和工具调用的边界是什么？
- 为什么 handoff 时不能把所有上下文和所有工具权限都交出去？
- A2A 和 handoff 的关系是协议互操作 vs 任务交接模式，能举例说明吗？

## 相关链接

- [[Agent]]
- [[Agent Framework]]
- [[Human-in-the-loop]]
- [[A2A]]
