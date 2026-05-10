---
type: concept
topic:
  - agent
  - browser
  - computer-use
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[OpenAI Computer Use 文档]]"
  - "[[Anthropic Computer Use 文档]]"
  - "[[browser-use GitHub Repo]]"
  - "[[Playwright MCP Repo]]"
evidence:
  - "[[OpenAI Computer Use 文档#为什么收]]"
  - "[[Anthropic Computer Use 文档#为什么收]]"
  - "[[browser-use GitHub Repo#为什么收]]"
related:
  - "[[Computer Use]]"
  - "[[GUI Grounding]]"
  - "[[Tool Calling]]"
  - "[[Prompt Injection]]"
---

# Browser Agent

## 一句话

Browser Agent 是能观察网页、点击、输入、滚动、提取信息并完成网页任务的 Agent。

## 概念详解

Browser Agent 的问题背景是很多现实任务只存在于网页 UI：登录后台、填写表单、下载资料、跨页面查找信息。普通 API 或检索不能覆盖这些任务，因此 Agent 需要把浏览器当作可观察、可操作的环境。source notes 把 OpenAI / Anthropic Computer Use、browser-use、Playwright MCP 都连接到这张卡，说明 browser agent 是模型能力、浏览器自动化工具、状态管理和安全策略的组合。

机制上，Browser Agent 会读取网页状态（截图、DOM、可访问性树或工具返回值），选择动作（click、type、scroll、extract、submit），执行后再观察新状态。它可能通过 computer use 的截图/action loop，也可能通过 Playwright/MCP 这类结构化浏览器工具。关键不是“模型会点网页”，而是每一步都必须处理页面变化、登录态、弹窗、等待、失败恢复、数据来源和权限。

它和传统浏览器自动化的边界在于确定性：固定流程更适合写 Playwright 脚本；开放式、页面结构未知、需要语言理解的任务才更像 Browser Agent。它和 [[Computer Use]] 的边界是范围：Computer Use 可覆盖桌面/GUI，Browser Agent 专注浏览器环境。安全上，网页内容同时是资料和攻击面，必须考虑 indirect prompt injection、表单提交审批和登录态隔离。

## 它解决什么问题

很多真实任务没有好用 API，只能通过网页完成：查资料、填表、下载文件、跨页面比较信息。Browser Agent 把浏览器变成 Agent 的行动环境。

## 它不是什么

Browser Agent 不是普通爬虫。

爬虫偏批量抓取页面；Browser Agent 更偏交互式任务执行，会处理登录态、按钮、表单、弹窗、页面变化和失败恢复。

## 最小例子

“帮我找到 LangGraph 最新 memory 文档，并把关键链接保存进 raw。”

Browser Agent 可能会：

1. 打开搜索页。
2. 点击官方文档。
3. 读取页面标题和导航。
4. 提取 URL 和关键概念。
5. 写入 Obsidian source note。

## 常见误解 / 风险 / 边界细节

- 网页内容可能包含 [[Indirect Prompt Injection]]。
- 自动点击和提交表单需要确认门。
- 页面状态不稳定，失败重试很重要。
- 对稳定重复任务，确定性 Playwright 脚本可能比 Agent 更可靠。

## 边界细节

Browser Agent 适合开放式网页任务；稳定重复流程优先写确定性脚本/API。网页内容是资料也是攻击面，登录态、表单提交、下载、跨域跳转和隐藏文本都应进入权限与审计边界。

## 现代性状态

frontier / volatile。Browser Agent 是当前工程热点，browser-use、Playwright MCP、computer use SDK 的实现都在变化。稳定价值是网页 UI 自动化的观察-动作-反馈 loop 和安全边界。

## 证据锚点

- Evidence type: source evidence — [[OpenAI Computer Use 文档#为什么收]]；[[Anthropic Computer Use 文档#为什么收]]；[[browser-use GitHub Repo#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[OpenAI Computer Use 文档]]；[[Anthropic Computer Use 文档]]；[[browser-use GitHub Repo]]；[[Playwright MCP Repo]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- 什么时候应该用 Browser Agent，什么时候应该写 Playwright 脚本？
- 网页内容为什么同时是资料和攻击面？

## 相关链接

- [[Computer Use]]
- [[GUI Grounding]]
- [[Approval Gate]]
- [[Prompt Injection]]
