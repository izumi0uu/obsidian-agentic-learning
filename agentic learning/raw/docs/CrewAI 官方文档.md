---
type: source
source_type: docs
title: CrewAI Documentation
url: https://docs.crewai.com/
author: CrewAI
site: docs.crewai.com
topic:
  - agent
  - framework
  - multi-agent
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Framework]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# CrewAI 官方文档

## 为什么收

CrewAI 是热门多 Agent 框架之一。它把 agent、crew、task/process、flow、guardrails、memory、knowledge、observability 和企业部署放在同一产品/框架叙事里，适合和 LangGraph、AutoGen、Mastra、Agno 等比较“业务协作流程”与“底层 runtime”的边界。

## 先读什么

- Home / Documentation
- Agents
- Crews
- Flows
- Tasks & Processes
- Knowledge / Memory
- Guardrails / Observability / Enterprise console

## 一句话

CrewAI 更像面向“协作式业务自动化”的多 Agent 框架：用 agents + crews 表达角色协作，用 flows 表达显式流程，并在文档中强调 guardrails、memory、knowledge、observability 和部署管理。

## 需要我读的内容

### 必读块 1：Agents / crews / flows 三层

- 位置：CrewAI Documentation 首页 / Build the basics。
- 为什么必读：支撑本 vault 对 CrewAI 的定位：它不是只做 tool loop，而是把角色协作和流程自动化一起包装。
- 中文概括：文档把 agents、flows、tasks/processes 并列为基础构建块；agents 可组合 tools、memory、knowledge 和结构化输出，flows 负责 start/listen/router、state、持久化和恢复。
- 支撑概念：[[Agent Framework]], [[Agent Workflow]], [[Multi-agent Orchestration]]。
- 证据边界：这是官方产品/文档定位，不等于证明所有生产场景都比底层 graph runtime 更可靠。

### 必读块 2：生产化叙事

- 位置：CrewAI Documentation 首页 / Enterprise journey。
- 为什么必读：支撑“CrewAI 偏业务自动化平台”的选型判断。
- 中文概括：CrewAI 文档把部署 automations、触发器、企业 console、team management / RBAC 放入官方路径，说明它不只是 research multi-agent demo。
- 支撑概念：[[Agent Harness]], [[Observability]], [[Approval Gate]]。
- 证据边界：具体企业能力、云端功能和版本变化快，必须保持 `freshness: volatile`。

## 可以拆成概念卡

- Crew / crew orchestration
- Flow vs crew
- Business automation agent framework

## 我的疑问

- Crew 的 role/task 结构在复杂业务中如何避免“角色很多但责任不清”？
- Flow 的状态恢复和外部副作用幂等性具体如何治理？
- 企业控制台能力和开源框架能力的边界在哪里？

## 边界提醒

CrewAI 的强项不是最低层状态图控制，而是面向“多角色协作 + 工作流自动化 + 企业部署”的产品化路径。不要仅凭 demo 中 agent 数量判断可靠性。
