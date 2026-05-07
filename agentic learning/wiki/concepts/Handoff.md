---
type: concept
topic:
  - agent
  - workflow
status: seed
created: 2026-05-06
updated: 2026-05-06
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

Handoff 是一个 Agent 把任务、上下文和控制权交给另一个 Agent 或人类的机制。

## 它解决什么问题

单个 Agent 不一定适合所有任务。客服、代码、研究、审批、支付等步骤可能需要不同角色、权限和工具。Handoff 让任务在角色之间流转。

## 它不是什么

Handoff 不是多 Agent 越多越好。

它也不等于 [[A2A]]。A2A 更偏协议互操作；handoff 是任务交接模式，可以发生在同一个框架内部。

## 最小例子

```text
triage agent -> billing agent -> human approval -> execution agent
```

## 常见误解和风险

- 交接时丢失上下文会导致重复问问题。
- 权限没有收窄时，专门 agent 可能拿到过多工具。
- 交接链太长会增加延迟和不可解释性。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Agent Framework]]
- [[Human-in-the-loop]]
- [[A2A]]
