---
type: concept
topic:
  - agent
  - browser
  - computer-use
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
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

## 证据锚点

- Source: [[OpenAI Computer Use 文档]]
- Source: [[Anthropic Computer Use 文档]]
- Source: [[browser-use GitHub Repo]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Computer Use]]
- [[GUI Grounding]]
- [[Approval Gate]]
- [[Prompt Injection]]
