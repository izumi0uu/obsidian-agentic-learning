---
type: source
source_type: docs
title: Smithery MCP Registry
url: https://smithery.ai/
author: Smithery
site: smithery.ai
topic:
  - agent
  - mcp
  - registry
  - tools
  - frontier
created: 2026-05-21
updated: 2026-05-21
last_checked: 2026-05-21
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[MCP]]"
  - "[[MCP Registry]]"
  - "[[Tool Registry]]"
  - "[[Tool Poisoning]]"
  - "[[Tool Permissioning]]"
---

# Smithery MCP Registry

## 为什么收

Smithery 是 MCP 生态里的第三方 registry / discovery / connection 平台例子。它适合放进 [[MCP]] 和 [[MCP Registry]] 的学习边界里，用来区分：MCP 是 client/server 连接协议，registry 是发现、发布、连接和筛选 MCP server 的生态层。

## 一句话

Smithery 帮用户发现和连接 MCP server，也让开发者把 server 发布到 Smithery registry；它是 MCP server 发现/分发层的具体平台例子，不是 MCP 协议本身。

## 先读什么

- Smithery 首页：<https://smithery.ai/>
- Connect docs：<https://smithery.ai/docs/use/connect>
- Publish docs：<https://smithery.ai/docs/build/publish>
- Registry API docs：<https://smithery.ai/docs/registry>
- Servers API：<https://smithery.ai/docs/api-reference/servers/list-all-servers>

## 关键事实

- Smithery 文档把用户侧入口描述为发现和连接 MCP server；这说明它位于 MCP server discovery / connection 生态层，而不是 host 内部 tool calling 层。
- Publish docs 面向开发者，说明 server 可以发布到 Smithery registry；这支持“registry 负责发布和分发入口”的边界。
- Registry / API docs 提供按关键词、tag、remote / verified 等元数据筛选 server 的能力；这些字段适合帮助初筛候选 server，但不等于安全背书。
- Smithery 首页展示的 server / user 数量属于产品状态，变化快；概念卡里只保留“第三方 MCP registry 平台”这个稳定学习边界，不记录具体数量。

## 可以拆成概念卡

- [[MCP Registry]]：已经存在；Smithery 只是它的生态实例，不单独建概念卡。
- [[Tool Registry]]：用于对比 host 内部工具目录和生态级 MCP server registry。
- [[Tool Poisoning]]：registry 发现 server 后仍要审查 tool description / schema / source。

## 边界提醒

Smithery 上能发现或连接某个 MCP server，不代表该 server 在当前任务里可信、权限合理、schema 无污染或供应链安全。正确链路仍然是：发现候选 server -> 检查来源、版本、权限和运行方式 -> host 做最小权限暴露 -> 运行时保留 approval / audit / trace。

## 证据边界

本 note 只做 source-level 摘要。Smithery 的具体 server 数量、verified 规则、API 字段和连接方式都属于 volatile 产品状态；后续写概念卡时只引用稳定边界，不把页面上的实时产品数字写成长期事实。
