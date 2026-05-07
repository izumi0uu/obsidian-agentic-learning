---
type: concept
topic:
  - tool
  - security
  - agent
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[MCP Tool Poisoning Threat Model]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[MCP Tool Poisoning Threat Model#为什么收]]"
related:
  - "[[Least Privilege Tools]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Tool Calling]]"
---

# Tool Permissioning

## 一句话

Tool Permissioning 是给 Agent 工具和工具动作设置权限、范围、审批和风险等级的机制。

## 它解决什么问题

工具可调用不等于应该随便调用。读文件、发邮件、转账、删库、联网、访问私密数据的风险完全不同，需要分级授权。

## 它不是什么

Tool Permissioning 不是工具列表。

它也不等于 [[Least Privilege Tools]]。最小权限是原则，permissioning 是具体执行机制。

## 最小例子

```text
read_docs: auto allow
send_email: require approval
delete_file: deny outside workspace
charge_card: human approval + audit log
```

## 常见误解和风险

- 工具描述可信，不代表工具行为安全。
- 权限只看工具名不够，还要看参数和上下文。
- 审批应该保留理由和记录。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[MCP Tool Poisoning Threat Model]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Least Privilege Tools]]
- [[Policy Engine]]
- [[Approval Gate]]
- [[Tool Calling]]
