---
type: concept
topic:
  - security
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[OWASP Agentic Applications Top 10]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[OWASP Agentic Applications Top 10#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
related:
  - "[[Approval Gate]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Registry]]"
  - "[[Sandbox Workspace]]"
---

# Policy Engine

## 一句话

Policy Engine 是根据规则、上下文和风险等级决定 Agent 能否调用工具、访问数据或执行动作的控制层。

## 它解决什么问题

仅靠模型“自觉遵守规则”不够。Policy Engine 把安全策略从自然语言提示中抽出来，用更确定的方式限制工具、数据和动作。

## 它不是什么

Policy Engine 不是系统 prompt。

系统 prompt 可以告诉模型“不要删除文件”；policy engine 应该真的拦截删除动作，或者要求审批。

## 最小例子

规则：

- `read_file` 只允许当前 vault。
- `delete_file` 永远需要用户确认。
- `send_email` 只能发送给 allowlist 域名。
- 如果网页内容包含 prompt injection 风险，禁止自动提交表单。

## 常见误解 / 风险 / 边界细节

- 规则太粗会挡住正常任务。
- 规则太细会难维护。
- Policy 决策要可解释和可审计。
- Policy Engine 需要和 tool registry、sandbox、approval gate 配合。

## 证据锚点

- Source: [[OWASP Agentic Applications Top 10]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Approval Gate]]
- [[Least Privilege Tools]]
- [[Tool Registry]]
- [[Prompt Injection]]
