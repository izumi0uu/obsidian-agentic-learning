---
type: concept
topic:
  - security
  - human-in-the-loop
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-24
last_checked: 2026-05-10
freshness: watch
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
  - "[[Gating Mechanism]]"
  - "[[Computer Use]]"
  - "[[Tool Calling]]"
---

# Approval Gate

## 一句话

Approval Gate 是在高风险动作执行前要求人类确认的控制点。

## 概念详解

Approval Gate 的问题背景是 Agent 能把语言输出转成真实动作：发邮件、提交表单、删文件、付费、调用外部系统。只要动作会产生不可逆影响，安全边界就不能只放在 prompt 里。approval gate 把“模型建议做什么”和“系统真正执行什么”切开，让高风险步骤在执行前进入人工确认、策略检查或二次验证。

机制上，approval gate 通常出现在工具调用前、GUI 动作前、跨权限边界前或高影响输出前。它可以是用户确认弹窗，也可以是 policy engine 根据风险等级自动放行、拒绝或升级人工审核。Computer Use 文档强调截图/action loop 和 sandbox，OWASP Agentic 风险强调 excessive agency、工具误用和人类信任边界；这些 source evidence 支撑了 approval gate 作为 Agent 行动边界，而不是 UI 小功能。

它和 [[Human-in-the-loop]] 相关但不等同。human-in-the-loop 可以参与澄清、标注、评审或接管；approval gate 特指“执行前的准入点”。它和 [[Policy Engine]] 也不同：policy engine 负责判断规则，approval gate 是把判断结果暴露成执行阻断或确认流程。好的 gate 要给出动作、参数、来源、风险和可回滚性，否则用户只是机械点确认。

最容易忽略的细节是 gate 必须发生在执行前，而不是失败后补日志。对高风险动作，系统应在模型生成意图后暂停，把工具名、参数、目标账号、数据来源和潜在影响展示出来；用户或策略层确认后，执行器才真正动作。这样做会牺牲一点流畅性，但换来可解释、可审计和可回滚的控制点。


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

## 边界细节

Approval Gate 应放在不可逆、高影响、跨权限或外部提交动作之前。低风险读取可以自动通过，高风险写入应展示动作、参数、来源和风险。只弹一个“确认吗”但不给可判断信息，不是好的 gate。

它和 [[Gating Mechanism]] 是 false friend：二者都可以被中文叫“门 / gate”，但 Approval Gate 是系统执行前的安全准入点，Gating Mechanism 是模型内部选择性放行信息、特征或计算路径的数学机制。

## 现代性状态

current-practice / watch。执行前审批已经是现代 Agent 安全实践的一部分，但不同 SDK、computer-use 产品和企业策略会快速变化，因此保持 watch。稳定的是“高风险动作前要有可审计准入点”。

## 证据锚点

- Evidence type: source evidence — [[OpenAI Computer Use 文档#为什么收]]；[[Anthropic Computer Use 文档#为什么收]]；[[OWASP Agentic Applications Top 10#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[OpenAI Computer Use 文档]]；[[Anthropic Computer Use 文档]]；[[OWASP Agentic Applications Top 10]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- 哪些 Agent 动作必须进入 approval gate？
- 一个好的审批界面至少要展示哪些信息？

## 相关链接

- [[Least Privilege Tools]]
- [[Policy Engine]]
- [[Gating Mechanism]]
- [[Computer Use]]
- [[Sandbox Workspace]]
