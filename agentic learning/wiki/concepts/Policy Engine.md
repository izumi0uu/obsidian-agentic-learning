---
type: concept
topic:
  - security
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
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

## 概念详解

Policy Engine 的问题背景是 Agent 行动不能只由模型自然语言自律决定。系统需要一个更确定的控制层，根据任务、用户、工具、参数、数据分类、来源、风险等级和历史状态判断“这一步能不能做”。如果没有 policy engine，权限规则会散落在 prompt、工具描述、UI 弹窗和人工习惯里，很难审计和维护。

机制上，policy engine 可以在工具选择前、参数提交前、输出发送前或跨系统访问前运行。它读取上下文，套用规则或风险模型，返回 allow、deny、require approval、redact、sandbox-only 等决策。OWASP Agentic source note 强调 Agent 风险来自目标、工具、身份、供应链、记忆、通信和人类信任；OpenAI Agents SDK source note把 guardrails、tools、tracing 放在现代 Agent 工程抽象里。这些 evidence 支撑 policy engine 作为 runtime 控制点。

它和 [[Guardrails]] 的边界：guardrails 是整体防护层，policy engine 是其中更偏决策的核心。它和 [[Tool Permissioning]] 的边界：permissioning 关心授权模型，policy engine 执行和组合这些授权规则。好的 policy engine 要可解释、可测试、可审计，并能和 trace/eval 连接；否则规则越多，越容易变成不可预测的黑箱。

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

## 边界细节

Policy Engine 应输出可执行、可审计的决策，而不是只生成建议文本。规则过粗会误挡，过细会不可维护；应和 trace、测试用例、approval gate 和 least privilege 一起演进。

## 现代性状态

current-practice / watch。策略引擎是现代 Agent 安全控制的工程吸收方式；具体规则语言、SDK hook 和企业集成会变化，但“模型外决策层”边界稳定。

## 证据锚点

- Evidence type: source evidence — [[OWASP Agentic Applications Top 10#为什么收]]；[[OpenAI Agents SDK 文档#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[OWASP Agentic Applications Top 10]]；[[OpenAI Agents SDK 文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Policy Engine 应输出哪些类型的决策？
- 它和 Guardrails、Tool Permissioning 的边界是什么？

## 相关链接

- [[Approval Gate]]
- [[Least Privilege Tools]]
- [[Tool Registry]]
- [[Prompt Injection]]
