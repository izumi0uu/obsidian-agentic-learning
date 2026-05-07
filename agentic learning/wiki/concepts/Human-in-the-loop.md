---
type: concept
topic:
  - agent
  - safety
  - workflow
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Approval Gate]]"
  - "[[Policy Engine]]"
  - "[[Handoff]]"
  - "[[Agent Loop]]"
---

# Human-in-the-loop

## 一句话

Human-in-the-loop 是在 Agent 工作流中让人类参与确认、修正、接管或提供判断的机制。

## 它解决什么问题

Agent 会遇到高风险动作、需求不清、权限不足、事实不确定和伦理/合规判断。人类介入可以降低不可逆错误。

## 它不是什么

Human-in-the-loop 不是每一步都问人。

它也不等于 [[Approval Gate]]。Approval Gate 更像某个动作前的确认点；Human-in-the-loop 更广，包括澄清、反馈、编辑、接管和最终审核。

## 最小例子

```text
Agent 生成删除数据库迁移计划
-> policy 判断为高风险
-> 人类审批或修改
-> Agent 才能执行
```

## 常见误解和风险

- 过多确认会让系统不可用。
- 人类审批如果没有足够上下文，也只是橡皮图章。
- 审批点应该由风险和权限决定，而不是模型心情决定。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Approval Gate]]
- [[Policy Engine]]
- [[Handoff]]
- [[Agent Loop]]
