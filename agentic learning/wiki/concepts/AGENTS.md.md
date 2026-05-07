---
type: concept
topic:
  - coding-agent
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[AGENTS.md and Codex Agent Loop]]"
evidence:
  - "[[AGENTS.md and Codex Agent Loop#为什么收]]"
related:
  - "[[Coding Agent]]"
  - "[[Repo Context]]"
  - "[[Sandbox Workspace]]"
  - "[[Agent Harness]]"
---

# AGENTS.md

## 一句话

AGENTS.md 是给代码 Agent 读取的仓库级操作说明。

## 它解决什么问题

代码 Agent 进入一个 repo 时，不知道项目惯例、测试命令、禁止操作、目录职责、提交规范和验证边界。AGENTS.md 把这些信息写成 Agent 可读的上下文，减少它乱猜。

## 它不是什么

AGENTS.md 不是 README。

README 面向人类用户和开发者；AGENTS.md 更像给 Agent 的“本仓库工作规程”。它应该清楚告诉 Agent 如何探索、修改、测试、避免破坏用户改动。

## 最小例子

一个 AGENTS.md 可以写：

- 改代码前先读 `maps/字段规范.md`。
- raw source 不要删除。
- 修改概念卡必须保留“它不是什么”。
- 追加 log，不重写历史。

## 常见误解 / 风险 / 边界细节

- 写太长会让 Agent 忽略重点。
- 指令冲突会让行为不可预测。
- 多层 AGENTS.md 要注意作用范围。
- 不要把机密信息写进 AGENTS.md。

## 证据锚点

- Source: [[AGENTS.md and Codex Agent Loop]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Coding Agent]]
- [[Repo Context]]
- [[Sandbox Workspace]]
- [[Agent Harness]]
