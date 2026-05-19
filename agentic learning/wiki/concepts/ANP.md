---
type: concept
topic:
  - agent
  - protocol
  - frontier
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
aliases:
  - Agent Network Protocol
  - Agent Network Protocol (ANP)
  - 智能体网络协议
source:
  - "[[Agent Network Protocol]]"
  - "[[A2A]]"
  - "[[MCP]]"
evidence:
  - "[[Agent Network Protocol#为什么收]]"
  - "[[Agent Network Protocol#主源事实]]"
  - "[[Agent Network Protocol#边界提醒]]"
related:
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[ACP]]"
  - "[[MCP Registry]]"
  - "[[Tool Registry]]"
  - "[[A2A MCP ANP 对比]]"
relations:
  - type: contrasts_with
    target: "[[A2A]]"
    note: "A2A 更聚焦 Agent-to-Agent 任务协作和状态/消息/artifact；ANP 更强调 Agent 网络身份、发现、描述和通信协商。"
  - type: contrasts_with
    target: "[[MCP]]"
    note: "MCP 连接 AI 应用与工具/资源/context server；ANP 连接网络中的 Agent 身份和通信入口。"
  - type: related_to
    target: "[[MCP Registry]]"
    note: "两者都涉及发现与生态分发，但 MCP Registry 面向 MCP server；ANP discovery 面向 Agent identity/description。"
---

# ANP

## 一句话

ANP（Agent Network Protocol）是面向 Agent 网络互联的协议方向，重点不是“工具怎么接入”，而是 Agent 如何拥有身份、被发现、描述能力，并在安全通信中协商协议。

## 概念详解

ANP 出现的背景是：如果未来有大量 Agent 分布在不同组织、不同框架、不同运行环境里，它们不能只靠临时 API 文档或聊天 prompt 互相认识。一个 Agent 网络至少要回答五个问题：谁是这个 Agent，去哪里发现它，它声称自己能做什么，通信是否可信，以及双方用什么协议完成交互。

ANP 的主源把这些问题放进 Agentic Web / network protocol 的语境里。它关心的对象包括去中心化身份、加密通信、Agent Description Document、发现机制和 meta-protocol negotiation。这个重心和 [[A2A]]、[[MCP]] 不一样：A2A 更像“两个 Agent 如何围绕任务、消息、状态和 artifact 协作”；MCP 更像“AI 应用如何连接工具、资源和 context server”；ANP 更像“网络中的 Agent 如何被标识、被发现、被描述，并在通信前协商协议”。

机制上，可以把 ANP 看成一组网络互联层约定：身份层让 Agent 有可验证身份；描述层让外部系统知道它的能力、接口和元数据；发现层让其他 Agent 能找到它；通信层通过加密和协议协商减少跨系统互操作的不确定性。它不保证 Agent 做得对，也不保证任务协作质量；它只是尝试让 Agent 在开放网络中有更标准的入口。

学习 ANP 的价值，不在于背某个当前字段，而在于补上一个边界：随着 Agent 从单应用内的 workflow 走向跨组织网络，问题会从“我怎么调用工具”扩展到“我怎样识别、发现、信任并协商一个远端 Agent”。这也是它和 [[MCP Registry]]、[[Tool Registry]] 相邻但不等价的地方：registry 解决目录和分发，ANP 还把 Agent identity、description 和 communication negotiation 纳入协议边界。

## 它解决什么问题

- 让 Agent 在开放网络里有可验证身份，而不是只靠域名、API key 或聊天上下文猜测对方是谁。
- 让远端 Agent 的能力、接口和元数据可被机器读取。
- 让 Agent 之间在通信前协商可用协议和交互方式。
- 让发现、描述和通信安全成为协议问题，而不是每个应用自己拼胶水。
- 给 A2A / MCP 之外的 Agentic Web 问题提供观察入口。

## 它不是什么

ANP 不是 [[MCP]]。MCP 的主对象是工具、资源、prompts 和 context server；ANP 的主对象是网络中的 Agent 身份、发现、描述和通信协商。

ANP 也不是 [[A2A]] 的同义词。A2A 更聚焦 Agent-to-Agent 协作任务如何表达、跟踪和返回结果；ANP 更聚焦 Agent 网络互联的身份和协议协商层。

ANP 不是 Agent 框架。它不负责本地 planning、workflow、memory、evaluation、trace、durable execution 或 tool permissioning。

ANP 也不是“去中心化身份就能解决信任”。DID / 加密通信能改善身份和传输边界，但仍需要权限策略、审计、sandbox、数据最小化和结果验证。

## 最小例子

```text
一个研究 Agent 想找外部绘图 Agent：

1. 通过发现机制找到候选 Agent。
2. 读取对方的 Agent Description Document，确认能力、接口和通信入口。
3. 用可验证身份和安全通信确认对方来源。
4. 双方通过 meta-protocol 协商：这次任务用哪种消息/任务协议交互。
5. 真正任务协作可能再落到 A2A、普通 API 或其他约定。
```

这里 ANP 负责“网络入口、身份、描述、协商”；具体任务状态和 artifact 怎么传，可能由协商后的协议负责。

## 常见误解 / 风险

- 误解：ANP 会替代 A2A / MCP。更稳的理解是三者处在不同对象边界，可能互补，也可能在生态中竞争。
- 误解：有 DID 和加密通信就等于安全。身份和传输安全只是起点，仍要处理授权、越权调用、恶意 Agent、数据外泄和结果验证。
- 误解：Agent description 等于真实能力。描述文件可能过时、夸大或被污染，仍需要评测、信誉和运行时审计。
- 风险：开放发现会扩大攻击面；越容易找到和连接 Agent，越需要 least privilege、allowlist、policy engine 和审计。
- 风险：协议协商增加灵活性，也增加实现复杂度；如果缺少版本治理和兼容测试，互操作会退化成多套私有约定。

## 边界细节

和 [[A2A]] 的边界：A2A 关注 Agent-to-Agent 协作里的任务、消息、状态、artifact 和 streaming；ANP 关注 Agent 网络中的身份、发现、描述和通信协议协商。一个系统可以用 ANP 发现和协商，再用 A2A 承载任务协作。

和 [[MCP]] 的边界：MCP 关注 host/client/server 如何连接 tools、resources、prompts 和 context 服务。ANP 不把远端能力默认压扁成工具，而是把远端当成有身份和能力描述的 Agent。

和 [[ACP]] 的边界：ACP 更像 Agent 服务、应用和人之间的消息通信入口；ANP 更偏 Agentic Web 的网络身份、发现和协议协商。两者都属于 frontier / volatile，不宜只背字段。

和 [[MCP Registry]] / [[Tool Registry]] 的边界：registry 是目录和分发基础设施；ANP 的 discovery / description 还涉及 Agent 身份、能力声明和通信入口。目录可以是发现的一部分，但不是整个 ANP。

## 现代性状态

frontier / volatile。ANP 代表 Agent 网络互联方向的前沿尝试，问题空间很重要，但协议生态、实现采用度、和 A2A/MCP/ACP 的关系都未完全稳定。学习时应保留“Agent identity + discovery + description + secure communication + meta-protocol”的问题结构，不把当前字段或项目状态写成长期事实。

## 现代系统怎么吸收这个概念的价值

现代 Agent 系统可以先吸收 ANP 的问题分层，而不急着押注具体实现：

- 身份：远端 Agent 不能只靠 URL 或模型名被信任，需要可验证 identity。
- 描述：能力声明要机器可读，并且要能进入评测、权限和审计。
- 发现：Agent 发现不只是搜索目录，还要处理来源、版本、信誉和权限。
- 协商：跨组织 Agent 不一定共享同一协议，meta-protocol 可以把“用哪套交互规则”显式化。
- 治理：越开放的 Agent 网络越需要 policy engine、approval gate、trace 和安全边界。

## 证据锚点

- Evidence type: source evidence — [[Agent Network Protocol#为什么收]]；[[Agent Network Protocol#主源事实]]；[[Agent Network Protocol#边界提醒]]
- Evidence type: comparison anchors — [[A2A#证据锚点]]；[[MCP#证据锚点]]
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代系统怎么吸收”把 ANP 主源与本 vault 的 A2A / MCP / registry / security 边界综合起来。
- Boundary: 当前只按官网、GitHub/white paper 和规格入口做 seed 级录入；未把具体字段、SDK 状态、采用度或版本兼容性写成稳定结论。
- Confidence: medium

## 复习触发

1. ANP 里的 identity / discovery / description / communication negotiation 分别解决什么问题？
2. 为什么 ANP 不是 MCP，也不是 A2A 的简单别名？
3. 如果一个 Agent 已经能通过 A2A 接任务，为什么还可能需要 ANP 这样的网络身份和发现层？
4. Agent description 被污染或夸大时，系统应该靠什么补救？

## 相关链接

- [[A2A MCP ANP 对比]]
- [[A2A]]
- [[MCP]]
- [[ACP]]
- [[MCP Registry]]
- [[Tool Registry]]
- [[Policy Engine]]
- [[Tool Permissioning]]
