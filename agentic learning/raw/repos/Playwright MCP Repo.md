---
type: source
source_type: repo
title: "microsoft/playwright-mcp"
url: "https://github.com/microsoft/playwright-mcp"
author: Microsoft
site: github.com
topic:
  - agent
  - browser
  - mcp
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Browser Agent]]"
  - "[[MCP]]"
  - "[[Tool Registry]]"
  - "[[Computer Use]]"
---

# Playwright MCP Repo

## 为什么收

Playwright MCP 把浏览器自动化能力通过 MCP 暴露给 Agent，是理解“浏览器自动化工具如何进入工具协议”的主项目。

## 一句话

Playwright MCP 是一个让 Agent 通过 MCP 控制浏览器的服务器。

## 先读什么

- README：安装和可用工具。
- Playwright agents 文档：它如何服务 AI agents 和 LLM-driven automation。

## 可以拆成概念卡

- [[Browser Agent]]
- [[MCP]]
- [[Tool Registry]]

## 我的疑问

- MCP 浏览器工具返回 DOM/accessibility 信息时，如何控制 token 成本？
- 对稳定流程，Agent 调 MCP 好，还是生成/运行 Playwright 脚本好？

## 边界提醒

Playwright MCP 适合探索和自动化浏览器状态，但不等于可靠业务流程本身。稳定生产任务仍需要测试、重试、监控和权限控制。
