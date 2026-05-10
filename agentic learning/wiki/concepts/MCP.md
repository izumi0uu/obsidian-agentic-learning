---
type: concept
topic:
  - agent
  - tools
  - protocol
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
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

## 概念详解

MCP 的问题背景是每个 AI 应用都要连接文件、数据库、浏览器、代码仓库、SaaS 和内部服务。如果每个工具都用私有 SDK 接入，Agent harness 会变成大量不可复用的胶水代码。MCP 把 AI 应用和外部工具/数据源之间的连接协议标准化，让 host/client 能发现 server 提供的 tools、resources、prompts，并把这些能力映射到模型可使用的工具接口。

机制上，MCP 不等于模型的 function calling。function calling 描述模型如何输出结构化调用意图；MCP 描述应用如何和外部 server 连接、发现能力、传输上下文和接收结果。官方 source note 的 Tool schema 补充提到 tool definition 包含 name、title、description、inputSchema、可选 outputSchema 和 annotations；这说明 MCP 在模型调用之前提供工具目录和协议层信息，真正执行时仍需要 host 把它接到具体模型和权限系统。

MCP 的现代价值是降低工具接入碎片化，让 Agent 能更快连接真实系统；它的现代风险是连接越容易，攻击面越大。MCP server 的描述、schema、annotations、返回值和供应链都可能影响模型行为，所以 MCP 必须和 [[Tool Permissioning]]、[[Least Privilege Tools]]、[[Approval Gate]]、sandbox、registry 信任和 trace 配合。把 MCP 当成 Agent 框架是常见误解：它不负责 planning、memory、eval、恢复或多 Agent 编排，只负责一类上下文/工具连接边界。

一个最小心智模型是：MCP server 暴露能力，client/host 管理连接与权限，模型只看到经过 host 转换后的工具选择空间。这个分层让同一个 server 可被不同 AI 应用复用，也让安全责任分散到多个点：server 要准确描述工具，host 要限制可见性和执行，用户/策略层要决定高风险动作是否允许。


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

## 边界细节

MCP 的边界是协议连接层。它不替代模型 tool calling，不替代 Agent 框架，也不自动提供安全。MCP 让工具更容易接入，因此更需要 permissioning、registry 信任、sandbox 和审计。

## 现代性状态

frontier / volatile。MCP 是当前工具协议生态的重要前沿，核心抽象相对清晰，但 specification、SDK、registry 和远程 server 安全实践仍需按日期复查。

## 证据锚点

- Evidence type: source evidence — [[Model Context Protocol 官方文档#为什么收]]；[[Model Context Protocol Python SDK Repo#为什么收]]；[[MCP Tool Poisoning Threat Model#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Model Context Protocol 官方文档]]；[[Model Context Protocol Python SDK Repo]]；[[MCP Tool Poisoning Threat Model]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- MCP 和 function calling 分别处在哪一层？
- MCP 为什么会放大 permissioning 和 tool poisoning 的重要性？

## 相关链接

- [[Tool Calling]]
- [[Tool Registry]]
- [[A2A]]
- [[ACP]]
- [[Tool Poisoning]]
