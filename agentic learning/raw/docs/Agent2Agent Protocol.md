---
type: source
source_type: docs
title: "Agent2Agent Protocol"
url: "https://github.com/a2aproject/A2A"
author: Google / Linux Foundation
site: github.com
topic:
  - agent
  - protocol
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[ACP]]"
---

# Agent2Agent Protocol

## 为什么收

A2A 是 Agent 互操作方向的主协议之一。它关注不同框架、不同厂商、不同服务器上的 Agent 如何作为 Agent 协作，而不是只把对方当作普通工具。

## 一句话

A2A 是面向 Agent-to-Agent 通信和互操作的开放协议。

## 先读什么

- GitHub README：协议目标和生态定位。
- Specification：看 Agent Card、task、message、streaming 等核心对象。

## 可以拆成概念卡

- [[A2A]]
- [[ACP]]
- [[MCP]]

## 我的疑问

- A2A 和 MCP 的边界是“Agent 对 Agent”与“Agent 对工具/数据源”吗？
- 多 Agent 协作什么时候需要协议，什么时候只需要普通 API？

## 边界提醒

A2A 不是多 Agent 框架。它更像跨系统互操作层，不能替代本地 orchestrator、权限系统和评测系统。
