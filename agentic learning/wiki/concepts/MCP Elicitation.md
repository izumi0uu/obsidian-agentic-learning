---
type: concept
topic:
  - agent
  - tools
  - protocol
  - mcp
status: seed
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: watch
conflicts: []
aliases:
  - MCP elicitation
  - Elicitation
  - MCP 用户澄清
  - MCP 结构化追问
  - MCP 结构化补充信息请求
  - MCP 表单追问
  - MCP URL 授权请求
source:
  - "[[Model Context Protocol 官方文档]]"
evidence:
  - "[[Model Context Protocol 官方文档#Elicitation 补充]]"
related:
  - "[[MCP]]"
  - "[[MCP Transport]]"
  - "[[Tool Permissioning]]"
  - "[[Approval Gate]]"
  - "[[Human-in-the-loop]]"
  - "[[Tool Calling]]"
---

# MCP Elicitation

## 一句话

MCP Elicitation 是 MCP server 在交互过程中通过 client/host 向用户请求额外输入或授权流程的协议能力。

## 概念详解

[[MCP]] 通常被记成 “host/client 连接 server，server 暴露 tools、resources、prompts”。Elicitation 补上了另一个方向：当 server 执行某个交互流程时，如果缺少必要信息或需要外部授权，它可以向 client 发起 `elicitation/create` 请求，让 client/host 以合适的 UI 向用户询问，并把用户的 accept / decline / cancel 结果返回给 server。

这个设计的关键不是“server 直接和用户聊天”。官方 spec 强调 client 仍控制用户交互和数据分享方式。Server 提出需要什么信息；在 `form` 模式里给出受限 JSON Schema，在 `url` 模式里给出外部授权或配置链接；client 决定如何呈现、如何让用户审查/修改/拒绝/取消，以及是否允许这类请求。换句话说，Elicitation 把“server 缺信息”变成一个可审计的 host-mediated interaction，而不是让 server 绕过 host 直接获得用户信任。

因此 Elicitation 是 MCP 里的 human-input / clarification / external-flow 能力，而不是普通 tool result。它适合需要用户补字段、选择选项、确认非敏感参数或跳转授权配置的流程，例如让用户提供 GitHub username、选择项目、填写非敏感配置，或进入 OAuth 授权页面。它不适合索要密码、token、银行卡、cookie 或其它敏感信息。

## 它解决什么问题

有些 MCP server workflow 不能只靠一次工具调用完成，因为 server 不知道用户偏好、目标对象或必要字段。Elicitation 给 server 一个标准方式请求补充信息，同时让 client/host 保留交互控制权。

## 它不是什么

MCP Elicitation 不是 [[Approval Gate]]。Approval gate 重点是高风险动作执行前的准入；elicitation 重点是补充结构化输入。二者可以组合，但不能互相替代。

它也不是模型自由追问。模型可以在对话里问用户问题；MCP Elicitation 是 server 通过 MCP 协议向 client 请求用户输入。

它也不是工具执行结果。Elicitation 是 server 发出的信息请求，返回的是用户动作和内容。

## 最小例子

```text
MCP server: 需要知道目标 repo owner
  -> client: elicitation/create(mode: "form", message, requestedSchema)
  -> host UI: 显示“哪个 GitHub 用户名？”
  -> user: accept + 填写 username
  -> client: 返回 { action: "accept", content: { name: "octocat" } }
  -> server: 继续 workflow
```

如果用户拒绝，返回 `decline`；如果用户关掉弹窗或没有明确选择，返回 `cancel`。

另一个常见形态是 `mode: "url"`：server 提供外部授权链接，client 显示来源、URL 和风险提示，用户完成或拒绝后 workflow 再继续。

## 常见误解 / 风险

- 误解：Elicitation 是让 MCP server 获得直接和用户对话的权力。实际上 client/host 仍应控制 UI、策略和隐私。
- 误解：Elicitation 可以索要任何信息。官方安全边界禁止 server 用它请求敏感信息。
- 风险：server 频繁发起 elicitation 会骚扰用户或诱导越权披露，需要 rate limit 和清晰来源提示。
- 风险：如果 UI 不显示哪个 server 在请求信息，用户可能把不可信 server 当成可信系统。
- 风险：schema 只能帮客户端校验结构，不能证明业务意图安全。

## 边界细节

Elicitation 与 [[Tool Calling]] 的边界：tool calling 是模型要求 runtime 执行工具；elicitation 是 MCP server 要求 client/host 询问用户。方向不同，控制责任也不同。

Elicitation 与 [[Human-in-the-loop]] 的关系：它是 HITL 的一种协议化入口，但只覆盖“补充信息 / 用户选择”这一类交互；人工审批、接管、标注、评审仍需要更广的 human-in-the-loop 设计。

Elicitation 与 [[Tool Permissioning]] 的关系：如果 elicitation 会影响后续工具参数，permissioning 仍要在执行前检查参数范围、数据范围和副作用。

## 现代性状态

- frontier / watch：Elicitation 是 MCP 2025-06-18 spec 开始出现并在 2025-11-25 spec 继续演进的 client feature。
- 稳定学习价值：server 请求信息、client 控制 UX/隐私、用户可 accept/decline/cancel、禁止敏感信息请求，这些边界值得保留。
- 易变部分：`form` / `url` 模式、具体客户端 UI、SDK 支持、schema 限制和安全默认值需要随 MCP spec 复查。

## 现代系统怎么吸收 MCP Elicitation 的价值 / 局限

价值在于把“工具服务需要问用户”的场景标准化，避免 server 自己发明私有交互协议。局限在于它只解决信息请求结构，不解决信任和授权。现代 host 应把 elicitation 当成一个可审计事件：显示请求来源，限制频率，禁止敏感字段，保存用户选择，并在后续工具执行前继续做 policy check。

## 证据锚点

- Evidence type: official spec — [[Model Context Protocol 官方文档#Elicitation 补充]]
- Evidence type: engineering synthesis — 本卡把 MCP 2025-06-18 / 2025-11-25 Elicitation spec 转成 host/client/server 责任边界。
- Boundary: Elicitation 只写成 MCP server 请求用户补充信息或外部流程的 client feature，不写成 approval gate、普通模型追问、tool result 或敏感凭证采集机制。
- Confidence: medium. Spec 是官方来源，但该能力处于 watch 状态。

## 复习触发

- 为什么 Elicitation 不是普通 tool result？
- 为什么 server 不能直接向用户索要敏感信息？
- accept / decline / cancel 三种结果对 workflow 处理有什么不同？
- Elicitation 和 Approval Gate 什么时候要组合使用？

## 相关链接

- [[MCP]]
- [[MCP Transport]]
- [[Tool Permissioning]]
- [[Approval Gate]]
- [[Human-in-the-loop]]
- [[Tool Calling]]
