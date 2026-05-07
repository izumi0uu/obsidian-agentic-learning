---
type: concept
topic:
  - tools
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[Model Context Protocol 官方文档]]"
  - "[[Playwright MCP Repo]]"
  - "[[MCP Tool Poisoning Threat Model]]"
evidence:
  - "[[Model Context Protocol 官方文档#为什么收]]"
  - "[[Playwright MCP Repo#为什么收]]"
  - "[[MCP Tool Poisoning Threat Model#为什么收]]"
related:
  - "[[Tool Calling]]"
  - "[[MCP]]"
  - "[[Tool Poisoning]]"
  - "[[Least Privilege Tools]]"
---

# Tool Registry

## 一句话

Tool Registry 是管理 Agent 可用工具名称、schema、描述、版本、来源、权限和状态的目录。

## 它解决什么问题

Agent 调工具前必须知道：工具叫什么、参数是什么、能做什么、谁提供、是否可信、需要什么权限、是否已经弃用。

当工具越来越多，靠 prompt 里手写列表会变得不可维护。

## 它不是什么

Tool Registry 不是工具本身。

它也不是简单函数列表。真正的 registry 还应该处理版本、权限、可见性、信任等级、审计和禁用。

## 最小例子

浏览器 Agent 的 tool registry 可能有：

- `browser.open`
- `browser.click`
- `browser.type`
- `browser.extract_text`
- `browser.submit_form`

其中 `submit_form` 需要 [[Approval Gate]]，`extract_text` 只能访问 allowlist 域名。

## 常见误解 / 风险 / 边界细节

- 工具描述会影响模型选择工具，因此描述也是攻击面。
- 工具版本变化可能破坏旧任务。
- registry 里能看到工具，不代表 Agent 就应该能调用。
- 远程工具需要供应链信任和权限隔离。

## 证据锚点

- Source: [[Model Context Protocol 官方文档]]
- Source: [[Playwright MCP Repo]]
- Source: [[MCP Tool Poisoning Threat Model]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Tool Calling]]
- [[MCP]]
- [[Tool Poisoning]]
- [[Least Privilege Tools]]
- [[Approval Gate]]
