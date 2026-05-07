---
type: concept
topic:
  - coding-agent
  - security
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[AGENTS.md and Codex Agent Loop]]"
  - "[[OpenAI Computer Use 文档]]"
  - "[[Anthropic Computer Use 文档]]"
evidence:
  - "[[AGENTS.md and Codex Agent Loop#为什么收]]"
  - "[[OpenAI Computer Use 文档#为什么收]]"
  - "[[Anthropic Computer Use 文档#为什么收]]"
related:
  - "[[Coding Agent]]"
  - "[[Agent Harness]]"
  - "[[Computer Use]]"
  - "[[Approval Gate]]"
---

# Sandbox Workspace

## 一句话

Sandbox Workspace 是给 Agent 执行命令、读写文件或操作 GUI 的隔离工作环境。

## 它解决什么问题

Agent 会运行命令、修改文件、访问网页、调用工具。没有隔离时，一次误操作就可能删除文件、泄露凭据、污染系统环境或破坏用户工作。

## 它不是什么

Sandbox 不是绝对安全。

它只是把风险限制在较小边界内，还需要权限、审批、网络控制、日志和人工介入。

## 最小例子

代码 Agent 在一个 repo workspace 里：

- 只能写当前项目目录。
- 运行测试前不能访问生产数据库。
- 高风险命令需要用户确认。
- 所有命令输出进入 trace。

## 常见误解 / 风险 / 边界细节

- Shell sandbox 不一定约束 MCP 工具。
- 浏览器 sandbox 也可能带登录态风险。
- 网络访问常常是隐藏风险。
- 沙箱越宽，越需要 [[Least Privilege Tools]]。

## 证据锚点

- Source: [[AGENTS.md and Codex Agent Loop]]
- Source: [[OpenAI Computer Use 文档]]
- Source: [[Anthropic Computer Use 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Coding Agent]]
- [[Agent Harness]]
- [[Computer Use]]
- [[Approval Gate]]
- [[Policy Engine]]
