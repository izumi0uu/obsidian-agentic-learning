---
type: concept
topic:
  - agent
  - protocol
  - payments
  - security
  - frontier
status: seed
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: volatile
conflicts: []
aliases:
  - AP2
  - Agent Payments Protocol
  - Agent Payment Protocol
  - Agentic Payment Protocol
  - Agent 支付协议
  - 代理支付协议
  - 智能体支付协议
source:
  - "[[Agent Payments Protocol 官方资料]]"
evidence:
  - "[[Agent Payments Protocol 官方资料#关键事实]]"
related:
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[Approval Gate]]"
  - "[[Tool Permissioning]]"
  - "[[Policy Engine]]"
  - "[[Audit Log]]"
  - "[[Data Exfiltration]]"
---

# Agent Payments Protocol

## 一句话

Agent Payments Protocol / Agentic Payment Protocol（AP2）是让 AI Agent 代表用户发起交易/支付时，证明授权、意图、真实性和责任归属的开放协议方向。

## 概念详解

Agent 一旦从“查资料 / 调 API”走到“替用户买东西、订票、采购、付款”，普通 tool calling 的边界就不够了。支付系统过去通常假设是人类在可信界面上点击购买；但 autonomous agent 可以在用户不在场时监控条件、选择商户、组合购物车并触发支付。系统必须回答：用户到底授权了什么？商户如何确认 agent 请求没有偏离用户意图？交易出错或欺诈时谁负责？

AP2 的学习价值就在这里：它把 agentic commerce 中的高风险动作从“一个工具调用”升级为“可验证的授权和审计链”。Google / AP2 official materials 把 AP2 放在可与 [[A2A]] 和 [[MCP]] 配合的开放协议位置：A2A 解决 Agent 间协作，MCP 解决工具/资源连接，AP2 解决交易/支付里的授权、真实性和 accountability。

AP2 的核心机制是 mandates 和 verifiable credentials。可以粗略理解为：用户意图、购物车内容和支付授权不只是 prompt 里的自然语言，而要形成可验证的数字契约和证据链。Human-present 场景里，用户先表达购买意图，agent 找到商品后用户再确认购物车；human-not-present 场景里，用户提前给出价格、时间、条件等规则，agent 满足条件后代表用户继续交易。两类场景都需要留下 intent -> cart -> payment 的审计链。

## 它解决什么问题

AP2 解决的是“Agent 能否安全、可审计、跨平台地代表用户交易”的问题。

没有这类协议时，商户和支付方只能看到一次 API 调用或付款请求，却很难知道它是否被用户授权、是否符合用户意图、是否被恶意 prompt 或工具结果诱导、是否可以追责。

## 它不是什么

AP2 不是 [[MCP]]。MCP 连接工具和数据源，AP2 处理交易/支付授权和证据链。

AP2 不是 [[A2A]]。A2A 处理 Agent 间发现、通信和协作，AP2 可作为交易/支付能力叠加在 Agent 协作之上。

AP2 也不是支付处理器、风控系统或钱包本身。它提供协议和证明结构，仍需要支付网络、商户系统、身份、风控、争议处理和合规体系。

## 最小例子

```text
用户：帮我买一双白色跑鞋，预算 120 美元以内。

Intent Mandate:
  用户授权 agent 寻找符合条件的商品。

Cart Mandate:
  agent 找到具体商品和价格后，用户确认购物车。

Payment:
  支付动作绑定到已确认的 intent / cart 证据链。
```

如果用户不在场，intent mandate 需要提前写清条件，例如最高价格、时间窗口、商品规格和可接受商户。

## 常见误解 / 风险

- 误解：Agent 支付就是给 Agent 一个信用卡工具。真正问题是授权、意图绑定、商户信任、责任和审计。
- 误解：有 AP2 就不需要审批。高风险支付仍可能需要 [[Approval Gate]] 或条件化授权。
- 误解：AP2 解决所有安全问题。Prompt injection、tool poisoning、replay、credential misuse、商户欺诈和账户接管仍要单独防护。
- 风险：用户意图写得太宽，Agent 可以在合法但不符合真实偏好的空间里行动。
- 风险：mandate 和后续 tool/action 没有强绑定时，容易出现上下文漂移或重放。

## 边界细节

AP2 与 [[Approval Gate]]：approval gate 是一次动作前的控制点；AP2 更像把支付授权结构化成可验证证据链。二者在支付场景常常同时存在。

AP2 与 [[Tool Permissioning]]：permissioning 决定当前 Agent 能否调用支付工具、能支付多少、能给谁支付；AP2 提供支付相关的授权和证明结构。没有 permissioning，AP2 仍可能被过宽工具权限放大风险。

AP2 与 [[Audit Log]]：AP2 的 mandates 和 proof chain 服务交易级审计；系统仍要保存 Agent 侧 trace、工具调用、用户事件和 policy 决策，才能复盘完整事故链。

## 现代性状态

- frontier / volatile：AP2 是 agentic commerce / agent-led payments 的前沿协议方向，repo、spec、标准化和生态支持仍会变化。
- 稳定学习价值：当 Agent 触发真实金钱流动时，必须把“用户说过”升级为可验证授权、意图绑定和审计证据。
- 不稳定部分：Agent Payments Protocol / Agentic Payment Protocol 命名、spec 版本、FIDO 标准化、x402 / stablecoin 扩展、SDK、商户集成和安全评估需要持续复查。

## 现代系统怎么吸收 Agent Payments Protocol 的价值 / 局限

现代 Agent 系统可以把 AP2 当成“高风险 tool action 的协议化升级”：普通工具调用前只需要 schema 和权限，支付动作前还需要授权证明、条件约束、不可抵赖审计和责任边界。

局限也很明显：协议不等于安全结论。系统仍要把 AP2 和 prompt-injection 防护、tool-result 隔离、policy engine、spending limits、merchant allowlist、human approval、replay 防护和审计日志一起设计。

## 证据锚点

- Evidence type: official source — [[Agent Payments Protocol 官方资料#关键事实]]
- Evidence type: engineering synthesis — 本卡把 Google Cloud announcement、AP2 GitHub repo、A2A / MCP / approval / audit 边界综合成 Agent 支付协议学习卡。
- Boundary: AP2 只写成 agent-led payments / commerce 的授权与审计协议方向，不写成支付处理器、风控系统、钱包或 MCP/A2A 的同义词。
- Confidence: medium. AP2 方向清晰，但协议版本、生态采纳和安全实践处于 volatile 状态。

## 复习触发

- 为什么 Agent 支付不能只看作一个 `pay(amount, merchant)` 工具？
- AP2 和 A2A / MCP 分别处在哪一层？
- Human-present 和 human-not-present 支付场景的授权差异是什么？
- 如果用户授权条件写得很宽，Agent 可能怎么“合法但错误”地执行？

## 相关链接

- [[A2A]]
- [[MCP]]
- [[Approval Gate]]
- [[Tool Permissioning]]
- [[Policy Engine]]
- [[Audit Log]]
- [[Data Exfiltration]]
