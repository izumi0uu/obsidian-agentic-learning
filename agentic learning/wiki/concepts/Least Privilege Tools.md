---
type: concept
topic:
  - security
  - tools
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[OWASP LLM Top 10 2025]]"
  - "[[OWASP Agentic Applications Top 10]]"
  - "[[OpenAI Computer Use 文档]]"
evidence:
  - "[[OWASP LLM Top 10 2025#为什么收]]"
  - "[[OWASP Agentic Applications Top 10#为什么收]]"
  - "[[OpenAI Computer Use 文档#为什么收]]"
related:
  - "[[Tool Calling]]"
  - "[[Tool Registry]]"
  - "[[Approval Gate]]"
  - "[[Policy Engine]]"
---

# Least Privilege Tools

## 一句话

Least Privilege Tools 是让 Agent 只拥有完成当前任务所需的最小工具、最小数据和最小动作权限。

## 它解决什么问题

Agent 一旦被 prompt injection、tool poisoning 或模型错误影响，过大的工具权限会把小错误放大成真实破坏。

最小权限把可调用工具、参数范围、数据访问和动作能力限制在必要范围内。

## 它不是什么

最小权限不是“不给 Agent 工具”。

它是精细授权：该读的能读，该写的受限，高风险动作需要确认。

## 最小例子

学习 Agent 需要整理 Obsidian vault：

- 可以读写 `agentic learning/`。
- 不可以读浏览器 cookie。
- 不可以访问 SSH key。
- 删除文件前必须确认。

## 常见误解 / 风险 / 边界细节

- 工具权限要按任务动态收窄。
- 只限制工具名不够，还要限制参数和数据范围。
- 权限变化应进入 audit log。
- 最小权限和用户体验之间要平衡。

## 证据锚点

- Source: [[OWASP LLM Top 10 2025]]
- Source: [[OWASP Agentic Applications Top 10]]
- Source: [[OpenAI Computer Use 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Tool Registry]]
- [[Approval Gate]]
- [[Policy Engine]]
- [[Sandbox Workspace]]
