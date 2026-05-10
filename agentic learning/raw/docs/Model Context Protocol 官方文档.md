---
type: source
source_type: docs
title: "Model Context Protocol Documentation"
url: "https://modelcontextprotocol.io/docs/getting-started/intro"
author: Model Context Protocol
site: modelcontextprotocol.io
topic:
  - agent
  - tools
  - mcp
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Tool Calling]]"
  - "[[Agent]]"
  - "[[MCP]]"
  - "[[Tool Registry]]"
  - "[[Tool Permissioning]]"
---

# Model Context Protocol 官方文档

## 为什么收

MCP 是理解“Agent 如何连接外部工具和数据源”的重要协议。它提供了一种标准化上下文和工具接入方式。

## 先读什么

- Introduction
- Architecture
- Servers
- Clients
- Tools and resources

## 一句话

MCP 为 AI 应用和外部工具/数据源之间提供标准连接协议。

## 可以拆成概念卡

- [[Tool Calling]]
- [[MCP]]
- [[Tool Registry]]
- tool server
- resource
- client-server architecture

## 我的疑问

- MCP 和普通 function calling 的边界是什么？
- MCP server 的权限应该如何设计？

## 边界提醒

MCP 是连接协议，不是 Agent 框架本身。

## Tool schema 补充

官方 Tools spec：<https://modelcontextprotocol.io/specification/2025-06-18/server/tools>

MCP 的 Tools spec 把 tool definition 拆成 `name`、`title`、`description`、`inputSchema`、可选 `outputSchema` 和 `annotations`。

- `inputSchema`：JSON Schema，用来定义工具期望的输入参数。
- `outputSchema`：可选 JSON Schema，用来定义结构化工具结果。
- `annotations`：工具行为提示，例如只读、破坏性、幂等等；出于安全考虑，客户端不能无条件信任来自不可信 server 的 annotations。

这说明 MCP 和 function calling 不在同一层：MCP 负责工具发现、协议和 server/client 连接；具体让模型发出调用请求时，仍要映射到模型侧支持的 tool/function calling 格式。
