---
type: map
topic:
  - agent
status: active
created: 2026-05-05
updated: 2026-05-21
related:
  - "[[Agent]]"
  - "[[ReAct]]"
  - "[[ReWOO]]"
  - "[[Coding Agent]]"
  - "[[Agent Workflow Static Verification]]"
  - "[[Agent 知识地图]]"
  - "[[Agent 工程分层对比]]"
  - "[[Workflow Guardrails 与 Prefect 控制点映射]]"
  - "[[OpenClaw Repo vs Hermes Agent]]"
  - "[[Tool 接口层对比]]"
  - "[[A2A MCP ANP 对比]]"
  - "[[Agent 安全控制点对比]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
---

# Agent 主题

这个主题页聚合所有 `topic` 包含 `agent` 的笔记。

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "agent")
SORT file.name ASC
```

## 待处理资料

```dataview
TABLE source_type, site, created, status
FROM "raw"
WHERE contains(topic, "agent") AND status = "inbox"
SORT created DESC
```

## 相关地图

- [[Agent 知识地图]]
- [[Agent 工程分层对比]]
- [[Tool 接口层对比]]
- [[A2A MCP ANP 对比]]
- [[Agent 安全控制点对比]]
- [[Workflow Guardrails 与 Prefect 控制点映射]]
- [[Agent Memory 类型对比]]
- [[Multi-agent Handoff Protocol 对比]]
- [[Browser Computer Use 执行栈对比]]
- [[Coding Agent 执行边界对比]]
- [[OpenClaw Repo vs Hermes Agent]]
- [[Environment Observation 类型对比]]
- [[Trajectory Trace 类型对比]]
- [[ReAct Plan-and-Solve Reflexion 对比]]
- [[03 前沿追踪]]
- [[oh-my-codex 使用教程]]

## 论文进入的关键概念

- [[ReAct]]
- [[Reflexion]]
- [[Plan-and-Solve Prompting]]
- [[ReWOO]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Coding Agent]]
- [[Repo Context]]
- [[Patch Validation]]
- [[Agent Workflow Static Verification]]


## Framework 选型边界概念

- [[State Graph Runtime]]
- [[Provider-first Agent SDK]]
- [[Crew Orchestration]]
- [[Role-playing Agent]]
- [[Data-first Agent Framework]]
- [[Type-safe Agent SDK]]
- [[Frontend-first AI Toolkit]]
- [[Agent Control Plane]]

## 工程工具教程

- [[oh-my-codex 使用教程]]
- [[Oh My Codex (OMX)]]
- [[Hermes Agent]]
- [[OpenClaw Repo]]
- [[LangChain DeepAgents]]
- [[AutoGen]]
- [[AgentScope]]
- [[CAMEL]]
- [[LangGraph]]
- [[Microsoft Agent Framework]]
- [[Agent Framework 编排范式对比]]
- [[Agent Framework 全量选型对比 2026-05]]
- [[OMX $ 指令]]
- [[Agent Lifecycle Hook]]
- [[Agent Workflow Static Verification]]
- [[Workflow Guardrails]]
