---
type: concept
topic:
  - tools
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
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

## 概念详解

Tool Registry 的问题背景是 Agent 可用工具一多，prompt 里手写函数列表就会失控。系统需要一个目录记录工具名称、描述、schema、版本、来源、权限、状态、可见性和审计信息，让模型/运行时知道当前任务能用哪些能力，也让人能管理哪些工具应该下线、升级或隔离。

机制上，tool registry 处在模型 tool calling 和实际工具执行之间。MCP 官方文档 source note说明 tool definition 包含 name、title、description、inputSchema、outputSchema 和 annotations；Playwright MCP source note说明浏览器自动化能力可以通过 MCP 暴露给 Agent；MCP Tool Poisoning source note提醒工具描述本身是攻击面。三者合在一起说明 registry 既是能力目录，也是信任边界。

它和 [[MCP Registry]] 的边界：MCP Registry 偏生态级 server 发现和分发；Tool Registry 可以是某个 Agent host 内部的可用工具目录。它也不是工具本身，不保证工具安全。成熟 registry 应该支持权限、版本、来源、可见性、禁用、风险标签和审计，而不只是把函数名塞给模型。

对模型来说，registry 的 description 和 schema 会直接影响工具选择；对系统来说，registry 是权限、版本和审计的入口。因此成熟 registry 往往要把“给模型看的描述”和“给执行器看的安全元数据”分开管理，避免模型为了完成任务而把工具自述当成不可挑战的事实。


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

## 边界细节

Tool Registry 是 host 内部能力目录，不等于外部 server registry，也不等于工具实现。registry 里的描述会影响模型行为，因此它本身需要版本、来源、权限和禁用机制。

## 现代性状态

current-practice / watch。工具目录是现代 Agent harness 常见结构；MCP registry、SDK tool schema 和权限标签会变化，内部 registry 的边界相对稳定。

## 证据锚点

- Evidence type: source evidence — [[Model Context Protocol 官方文档#为什么收]]；[[Playwright MCP Repo#为什么收]]；[[MCP Tool Poisoning Threat Model#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Model Context Protocol 官方文档]]；[[Playwright MCP Repo]]；[[MCP Tool Poisoning Threat Model]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Tool Registry 除了函数列表还应记录什么？
- 为什么工具描述本身也是攻击面？

## 相关链接

- [[Tool Calling]]
- [[MCP]]
- [[Tool Poisoning]]
- [[Least Privilege Tools]]
- [[Approval Gate]]
