---
type: concept
topic:
  - agent
  - protocol
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[Agent Communication Protocol]]"
evidence:
  - "[[Agent Communication Protocol#为什么收]]"
related:
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[Agent]]"
---

# ACP

## 一句话

ACP 是 Agent Communication Protocol，关注 Agent、应用和人之间的标准化消息通信。

## 它解决什么问题

Agent 需要异步任务、streaming、多模态消息、状态更新、发现和长任务交互。ACP 提供一套协议化的通信方式，让不同实现可以更容易互操作。

## 它不是什么

ACP 不是具体 Agent 产品。

它也不是长期完全稳定的基础概念。它处于协议演化和生态整合中，更适合作为“Agent 互操作问题”的观察入口。

## 最小例子

一个 UI 应用通过 ACP 给研究 Agent 发任务，研究 Agent streaming 返回计划、进度和最终结果，期间还可以请求用户补充文件或确认动作。

## 常见误解 / 风险 / 边界细节

- 看到 ACP 要先问版本和生态归属。
- 协议格式变化快时，不要把字段细节背成概念。
- 通信协议不能替代权限、审计和评测。
- 和 A2A 的边界可能随着生态合流而变化。

## 证据锚点

- Source: [[Agent Communication Protocol]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[A2A]]
- [[MCP]]
- [[Agent]]
- [[Observability]]
