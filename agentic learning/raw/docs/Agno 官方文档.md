---
type: source
source_type: docs
title: Agno Documentation
url: https://docs.agno.com/
author: Agno
site: docs.agno.com
topic:
  - agent
  - framework
  - platform
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Framework]]"
  - "[[Agent Harness]]"
  - "[[Observability]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# Agno 官方文档

## 为什么收

Agno 在热门 Agent framework 讨论中经常出现，但当前官方首页强调的是“build, run, manage agent platforms”。这使它成为一个重要边界样本：有些工具不只是 SDK，而是在 SDK、runtime、control plane / AgentOS 之间分层。

## 先读什么

- Welcome to Agno
- SDK / AgentOS / Deploy
- Runtime: Storage, Context, Human Approval, Observability, Security & Auth, Scheduling, Deploy
- Demo OS: Knowledge & Memory, Multi-Agent Teams

## 一句话

Agno 当前更像 Agent platform stack：SDK 负责 agents / teams / workflows，Runtime 把它们作为服务运行，Control Plane / AgentOS 负责管理、会话、tracing、scheduling、RBAC 和接口。

## 需要我读的内容

### 必读块 1：三层架构

- 位置：Welcome to Agno / 3-layer architecture。
- 为什么必读：支撑 Agno 不应只被归入普通 Python agent SDK。
- 中文概括：官方文档把 Agno 分成 SDK、Runtime、Control Plane：SDK 构建 agents/teams/workflows，Runtime 服务化运行，Control Plane 管理平台。
- 支撑概念：[[Agent Framework]], [[Agent Harness]], [[Observability]]。
- 证据边界：这反映当前产品定位；具体开源/商业边界需要持续复查。

### 必读块 2：生产平台能力

- 位置：Agno features。
- 为什么必读：支撑“Agno 偏平台化/产品化”选型判断。
- 中文概括：官方列出 API、storage、integrations、context providers、human approval、OpenTelemetry tracing、audit logs、RBAC、interfaces、scheduling、deploy anywhere 等运行能力。
- 支撑概念：[[Approval Gate]], [[Trace]], [[Audit Log]], [[Tool Permissioning]]。
- 证据边界：功能覆盖广不等于每个能力都适合你的组织流程；部署前仍需验证权限、数据隔离和观测闭环。

## 可以拆成概念卡

- Agent platform stack
- Runtime vs SDK vs control plane
- AgentOS

## 我的疑问

- Agno SDK 与“用任何 agent framework 构建”的平台兼容边界是什么？
- Runtime / Control Plane 的商业能力和开源能力如何分割？

## 边界提醒

Agno 的关键不是“又一个 agent 类”，而是 SDK + runtime + platform 的三层产品化路径；和 LangGraph 这类底层 state graph runtime 不在同一层。
