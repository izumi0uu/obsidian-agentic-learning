---
type: source
source_type: docs
title: Model Context Protocol Documentation
url: https://modelcontextprotocol.io/docs/getting-started/intro
author: Model Context Protocol
site: modelcontextprotocol.io
topic:
  - agent
  - tools
  - mcp
created: 2026-05-05
updated: 2026-05-20
last_checked: 2026-05-20
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Tool Calling]]"
  - "[[Agent]]"
  - "[[MCP]]"
  - "[[MCP Transport]]"
  - "[[MCP Elicitation]]"
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
- [[MCP Elicitation]]
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

## Transport 补充

官方 Transports docs / 2025-06-18 spec：<https://modelcontextprotocol.io/docs/concepts/transports>；<https://modelcontextprotocol.io/specification/2025-06-18/basic/transports>

当前文档把 MCP client-server 通信的标准 transport 列为两类：

- `stdio`：client 把 MCP server 作为子进程启动；server 从 `stdin` 读 JSON-RPC 消息，并把响应写到 `stdout`；消息用换行分隔，`stdout` 不应混入非 MCP 消息。
- `Streamable HTTP`：server 作为独立进程提供单个 MCP endpoint，支持 HTTP POST / GET；client 用 POST 发送 JSON-RPC 消息，server 可以返回 `application/json`，也可以返回 `text/event-stream` 做流式消息。

官方 docs 明确说明 Streamable HTTP 替代了 2024-11-05 规范里的 HTTP+SSE transport。实现 Streamable HTTP 时还要注意安全边界：server 应验证 `Origin` header；本地运行时优先只绑定 `127.0.0.1`；对连接实现合适的认证。

边界：SSE 不是完全消失，而是从旧的双端点 transport 边界变成 Streamable HTTP 可用的流式响应机制之一。`HTTP Transport` 这个说法太宽；新项目应明确说 `Streamable HTTP`。

## Elicitation 补充

官方 2025-11-25 Elicitation spec：<https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation>

Elicitation 是 MCP server 通过 client / host 请求用户补充信息的协议能力。Server 发起 `elicitation/create`，client 决定如何向用户展示请求、收集输入，并返回 `accept`、`decline` 或 `cancel`。

- 2025-06-18 spec 中的 Elicitation 已经把 server 请求结构化用户输入作为 client feature；2025-11-25 spec 继续明确当前请求模式。
- `mode: form` 用 `requestedSchema` 请求结构化表单输入；schema 受限，只允许 primitive、enum、数组和简单 object，不能使用任意 JSON Schema 特性。
- `mode: url` 允许 client 引导用户到外部 URL 完成授权或配置流程；client 应清晰展示请求来源和目标链接。
- Client / host 保留用户体验、隐私和安全控制权；用户可以接受、拒绝或取消。
- 安全边界：server 不应通过 elicitation 请求密码、token、银行卡、cookie 等敏感信息；client 应限制频率、显示来源并做策略检查。

边界：Elicitation 是“补充信息 / 用户选择”的协议入口，不等于 [[Approval Gate]]、不等于模型自由追问，也不替代后续 tool permissioning。
