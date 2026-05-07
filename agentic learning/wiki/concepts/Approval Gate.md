---
type: concept
topic:
  - security
  - human-in-the-loop
  - agent
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
  - "[[OWASP Agentic Applications Top 10]]"
evidence:
  - "[[OpenAI Computer Use 文档#为什么收]]"
  - "[[Anthropic Computer Use 文档#为什么收]]"
  - "[[OWASP Agentic Applications Top 10#为什么收]]"
related:
  - "[[Least Privilege Tools]]"
  - "[[Policy Engine]]"
  - "[[Computer Use]]"
  - "[[Tool Calling]]"
---

# Approval Gate

## 一句话

Approval Gate 是在高风险动作执行前要求人类确认的控制点。

## 它解决什么问题

Agent 能行动后，错误会变成真实后果：付款、删除文件、发送邮件、提交表单、部署代码。Approval Gate 把不可逆或高风险动作从自动执行中拦出来。

## 它不是什么

Approval Gate 不是每一步都问用户。

如果所有动作都确认，Agent 就失去效率；如果高风险动作不确认，系统就失去安全边界。

## 最小例子

Browser Agent 可以自动搜索和读取网页，但遇到：

- 提交订单。
- 输入密码。
- 发送邮件。
- 删除文件。

必须停下来说明将要做什么，并等待用户确认。

## 常见误解 / 风险 / 边界细节

- 确认弹窗要给足上下文，不然用户会盲点同意。
- 低风险动作可以自动化，高风险动作要分级。
- 审批结果应记录到 trace/audit log。
- Prompt injection 可能诱导 Agent 隐瞒风险，所以审批信息应由系统生成。

## 证据锚点

- Source: [[OpenAI Computer Use 文档]]
- Source: [[Anthropic Computer Use 文档]]
- Source: [[OWASP Agentic Applications Top 10]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Least Privilege Tools]]
- [[Policy Engine]]
- [[Computer Use]]
- [[Sandbox Workspace]]
