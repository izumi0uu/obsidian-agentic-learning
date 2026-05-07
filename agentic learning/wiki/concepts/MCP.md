---
type: concept
topic:
  - agent
  - tools
  - protocol
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[Model Context Protocol 官方文档]]"
  - "[[Model Context Protocol Python SDK Repo]]"
  - "[[MCP Tool Poisoning Threat Model]]"
evidence:
  - "[[Model Context Protocol 官方文档#为什么收]]"
  - "[[Model Context Protocol Python SDK Repo#为什么收]]"
  - "[[MCP Tool Poisoning Threat Model#为什么收]]"
related:
  - "[[Tool Calling]]"
  - "[[Tool Registry]]"
  - "[[A2A]]"
  - "[[Tool Poisoning]]"
---

# MCP

## 一句话

MCP 是让 AI 应用以标准方式连接工具、数据源和上下文服务的协议。

## 它解决什么问题

没有协议时，每个应用都要为每个工具写一套连接方式。MCP 把工具、资源、提示、server/client/host 等对象标准化，让 Agent 能发现和调用外部能力。

## 它不是什么

MCP 不是 Agent 框架。

它也不是模型的 function calling 本身。Function calling 是模型输出结构化调用意图；MCP 更关注应用和外部工具/数据源如何连接、发现和传输上下文。

## 最小例子

Obsidian 学习 Agent 通过 MCP 连接：

- 文件系统 server：读取 vault。
- 浏览器 server：打开网页。
- Jira server：查询任务。

Agent 看到的是一组标准化工具，而不是每个服务的私有 SDK。

## 常见误解 / 风险 / 边界细节

- MCP server 的工具描述也是输入，可能被投毒。
- MCP 不自动提供权限安全，host/client/server 各自都要做约束。
- 远程 server 带来供应链和身份风险。
- 工具越容易接入，越需要 [[Least Privilege Tools]] 和 [[Approval Gate]]。

## 证据锚点

- Source: [[Model Context Protocol 官方文档]]
- Source: [[Model Context Protocol Python SDK Repo]]
- Source: [[MCP Tool Poisoning Threat Model]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Tool Calling]]
- [[Tool Registry]]
- [[A2A]]
- [[ACP]]
- [[Tool Poisoning]]
