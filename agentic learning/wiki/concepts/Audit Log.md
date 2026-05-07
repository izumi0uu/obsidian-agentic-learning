---
type: concept
topic:
  - observability
  - security
  - evaluation
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
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Policy Engine]]"
  - "[[Tool Permissioning]]"
---

# Audit Log

## 一句话

Audit Log 是为安全、合规和复盘保存的 Agent 行动记录。

## 它解决什么问题

Agent 调用了什么工具、访问了什么数据、谁批准了高风险动作、输出了什么结果，都需要事后可查。否则出错后无法定位责任和根因。

## 它不是什么

Audit Log 不等于完整 [[Trace]]。

Trace 偏调试和观测，可能包含详细 prompt、token 和中间状态；Audit Log 更偏合规和关键动作记录。

## 最小例子

```text
time, user, agent, tool, action, parameters summary, approval, result, risk level
```

## 常见误解和风险

- 记录太少无法审计。
- 记录太多可能泄露敏感数据。
- 审计日志本身要防篡改和控制访问。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Policy Engine]]
- [[Tool Permissioning]]
