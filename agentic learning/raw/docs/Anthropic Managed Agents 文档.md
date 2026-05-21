---
type: source
source_type: docs
title: Claude Managed Agents Documentation
url: https://platform.claude.com/docs/en/managed-agents/overview
author: Anthropic
site: platform.claude.com
topic:
  - agent
  - harness
  - runtime
  - cloud
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Managed Agent Harness]]"
  - "[[Agent Harness]]"
  - "[[Agent Skills]]"
  - "[[MCP]]"
  - "[[Sandbox Workspace]]"
  - "[[Trace]]"
---

# Anthropic Managed Agents 文档

## 为什么收

这是校准 [[Managed Agent Harness]] 的官方主源。它把 Managed Agents 明确放在“托管 harness + 运行基础设施”层，而不是普通 Messages API、单纯 SDK 或模型能力。

## 先读什么

- Claude Managed Agents overview
- Core concepts
- How it works
- Supported tools
- Anthropic engineering post: Scaling Managed Agents

## 一句话

Claude Managed Agents 是 Anthropic 提供的托管 Agent harness：开发者定义 agent、environment 和 session，平台负责长任务执行、工具运行、事件流和运行环境。

## 关键事实

- 官方 overview 把 Managed Agents 定位为预置、可配置、运行在托管基础设施里的 agent harness，适合长任务和异步工作。
- 核心对象包括 agent、environment、session 和 events。Agent 组合模型、system prompt、tools、MCP servers 和 skills；environment 决定托管云容器或自托管 sandbox；session 是一次运行实例；events 是应用和 agent 之间的消息。
- 工作流包括创建 agent、创建 environment、启动 session、发送 events / 流式接收结果、在执行中 steer 或 interrupt。
- 支持的能力包括 bash、文件操作、web search/fetch 和 MCP servers。
- Anthropic engineering post 把 session、harness、sandbox 拆成可替换接口，并强调把 “brain / harness”、 “hands / tools/sandbox” 和 session log 解耦。

## 可以拆成概念卡

- [[Managed Agent Harness]]
- [[Agent Harness]]
- [[Sandbox Workspace]]
- [[Agent Skills]]
- [[MCP]]
- [[Trace]]

## 边界提醒

Managed Agents 不是 LLM 本身，也不等于所有 Agent Framework。它把 agent loop、工具执行、环境、session 和事件流托管化，适合减少开发者自建 harness 的成本；但权限、数据驻留、beta 行为、供应商锁定、成本和可观测性仍要按产品文档复查。

## 证据边界

本 source note 依据 2026-05-20 可访问的 Claude Managed Agents overview 与 Anthropic engineering post。具体 API、beta header、工具清单和 AWS / cloud 差异属于 volatile 事实，不写成长期稳定结论。
