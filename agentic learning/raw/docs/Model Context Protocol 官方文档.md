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
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Tool Calling]]"
  - "[[Agent]]"
  - "[[MCP]]"
  - "[[Tool Registry]]"
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
