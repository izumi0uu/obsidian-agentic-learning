---
type: concept
topic:
  - security
  - tools
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
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

## 概念详解

Least Privilege Tools 的问题背景是 Agent 会犯错，也会被 prompt injection、tool poisoning 或错误检索影响。只要工具权限过宽，小错误就可能变成真实破坏：读到不该读的文件、调用不该调用的 API、把敏感数据传到外部、在错误账号下提交表单。最小权限原则把风险面从“模型想做什么”缩到“系统允许它做什么”。

机制上，最小权限不只是少给几个工具名。它包括工具可见性、参数范围、数据范围、网络域名、文件路径、动作类型、时间窗口、身份范围和审批阈值。OWASP source notes 把 excessive agency、工具误用、sensitive information disclosure 和 Agentic 安全放在核心风险里；OpenAI Computer Use source note 又强调 sandbox、allowlist 和 human-in-the-loop。这些都支持“权限是运行时控制”，不是 prompt 礼貌约束。

它和 [[Tool Permissioning]] 的边界：least privilege 是原则，permissioning 是实现机制。它和 [[Approval Gate]] 的边界：最小权限先让高风险工具不可见或不可用；approval gate 在必须越过风险边界时要求确认。最小权限也不是把 Agent 变废，而是按任务逐步授权、完成后收回，并把授权理由写进 trace/audit。

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

## 边界细节

最小权限不等于不给工具，而是按任务授予最小工具、最小参数、最小数据范围和最短时间窗口。权限应随任务阶段变化，并在越权或高风险动作前升级到 approval gate。

## 现代性状态

current-practice / watch。最小权限是经典安全原则，现代 Agent 把它落到工具、参数、数据和动作范围上。具体 SDK 权限接口会变化，原则稳定。

## 证据锚点

- Evidence type: source evidence — [[OWASP LLM Top 10 2025#为什么收]]；[[OWASP Agentic Applications Top 10#为什么收]]；[[OpenAI Computer Use 文档#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[OWASP LLM Top 10 2025]]；[[OWASP Agentic Applications Top 10]]；[[OpenAI Computer Use 文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- 最小权限要限制哪些维度，而不只是工具名？
- 它和 approval gate 如何配合？

## 相关链接

- [[Tool Registry]]
- [[Approval Gate]]
- [[Policy Engine]]
- [[Sandbox Workspace]]
