---
type: source
source_type: docs
title: Google Agent Development Kit Documentation
url: https://adk.dev/
author: Google
site: adk.dev
topic:
  - agent
  - framework
  - google
  - multi-agent
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts:
  - ADK 首页显示 Python 2.0 beta / TypeScript 1.0 等快速演进信号；版本和语言支持需持续复查。
status: seed
source:
related:
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Evaluation]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# Google ADK 官方文档

## 为什么收

Google ADK 是 Google 生态当前主推的 Agent Development Kit。它值得纳入全量对比，因为官方首页把多语言 SDK、multi-agent orchestration、graph-based workflows、evaluation、deployment、context management 和 Google Cloud production path 放在一起。

## 先读什么

- Home / Build production agents
- Build Agents: LLM agents, Workflow agents, Multi-agent systems, Agent routing
- Tools and Integrations: Function tools, MCP tools, OpenAPI tools, Authentication
- Run Agents: Runtime, Deployment, Observability, Evaluation, Safety and Security
- Components: Sessions & Memory, Context, Artifacts, Events, Apps, Plugins, A2A Protocol
- ADK 2.0: Graph-based workflows, Collaborative agents, Dynamic workflows

## 一句话

Google ADK 是多语言、Google/Vertex/Cloud 生态友好的 agent development framework：从简单 tool-calling agent 扩展到 agent teams、workflow agents、graph workflows、evaluation、observability 和部署。

## 需要我读的内容

### 必读块 1：production agents 定位

- 位置：ADK 首页 / Build production agents。
- 为什么必读：支撑 ADK 与普通 agent demo 的边界。
- 中文概括：官方把 ADK 描述为开源 agent development framework，可构建、调试、部署企业规模 agent，支持 Python、TypeScript、Go、Java。
- 支撑概念：[[Agent Framework]], [[Agent Workflow]], [[Observability]]。
- 证据边界：官方定位强，但各语言 SDK 版本状态和 API 成熟度需复查。

### 必读块 2：scale / evaluation / deployment / context

- 位置：ADK 首页 / Powerful simplicity / Evaluation / FAQ。
- 为什么必读：支撑 ADK 的选型价值：不仅有 agent class，也有 workflow、eval、cloud deployment 和 context 管理叙事。
- 中文概括：官方路径从 prompts/tools 扩展到 multi-agent、graph workflows、performance evaluation 和 deployment；FAQ 强调 context management、Cloud Run/GKE/Agent Runtime 部署、observability 和安全边界。
- 支撑概念：[[Context Engineering]], [[Evaluation]], [[Trace]], [[Durable Execution]]。
- 证据边界：Google Cloud 托管能力对 Google 生态用户有价值；跨云/本地部署仍要验证成本和供应商绑定。

## 可以拆成概念卡

- Google ADK
- Workflow agents
- ADK context management

## 我的疑问

- ADK 2.0 graph workflows 与 LangGraph 在 checkpoint、state schema、human input 上如何比较？
- ADK 与 Google Agent Engine / Vertex AI / A2A 的边界如何持续演进？

## 边界提醒

ADK 是快速演进的生态型框架。选型时要区分“Google 生态生产路径”与“通用 agent framework 能力”；不要把首页能力列表直接等同于所有语言 SDK 都成熟一致。
