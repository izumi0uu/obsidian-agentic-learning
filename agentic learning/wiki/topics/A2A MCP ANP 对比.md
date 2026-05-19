---
type: map
topic:
  - agent
  - protocol
  - multi-agent
  - comparison
status: active
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
source:
  - "[[ANP]]"
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[Agent Network Protocol]]"
  - "[[Agent2Agent Protocol]]"
  - "[[Model Context Protocol 官方文档]]"
evidence:
  - "[[ANP#证据锚点]]"
  - "[[A2A#证据锚点]]"
  - "[[MCP#证据锚点]]"
  - "[[Agent Network Protocol#主源事实]]"
related:
  - "[[ANP]]"
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[Multi-agent Handoff Protocol 对比]]"
  - "[[Tool 接口层对比]]"
  - "[[Agent 主题]]"
---

# A2A MCP ANP 对比

## 一句话总览

[[A2A]]、[[MCP]]、[[ANP]] 都在解决 Agent 生态的互操作问题，但对象不同：A2A 是 Agent 与 Agent 围绕任务协作；MCP 是 AI 应用连接工具、资源和上下文服务；ANP 是 Agent 在网络里如何拥有身份、被发现、被描述并协商通信协议。

最小边界：A2A 问“远端 Agent 怎样接任务并返回状态/消息/artifact”；MCP 问“host 怎样发现和调用工具/资源/context server”；ANP 问“网络中的 Agent 怎样被识别、发现、描述和安全协商通信”。

## 为什么这组值得对比

- 混淆风险高：三者都带 protocol，都和 Agent 互操作有关，很容易被说成“Agent 之间互联”。
- 对象边界不同：A2A 的对象是 Agent 协作者，MCP 的对象是 tool/resource/context server，ANP 的对象是网络中的 Agent identity/description/communication entry。
- 成熟度不同：MCP 已经成为工具接入生态的重要协议；A2A 是 Agent-to-Agent 协作的前沿协议；ANP 更像 Agentic Web / network-layer 的前沿方向。
- 工程吸收方式不同：MCP 先落在工具接入和权限；A2A 先落在远端 Agent 委派；ANP 先落在身份、发现、描述和协议协商。

边界：这页不是协议字段说明，也不判断协议胜负。具体字段、SDK、registry 和生态采用度都属于 volatile 内容，需要按 `last_checked` 回源复查。

## 共同问题域

三者共同面对的是 Agent 生态从单应用内运行走向跨系统互操作之后的连接问题：能力怎样被发现、接口怎样被描述、调用/协作怎样被标准化、身份和权限怎样不被默认信任。

差异在于它们切的对象层不同。[[MCP]] 先把外部能力做成 tools / resources / prompts / context server；[[A2A]] 把远端能力保留为能处理任务的 Agent；[[ANP]] 再往网络层抬一层，关心 Agent identity、description、discovery 和 communication negotiation。这个问题域相同但对象不同，是最容易混淆的地方。

## 核心区别表

| 维度 | [[A2A]] | [[MCP]] | [[ANP]] |
|---|---|---|---|
| 最小对象 | 另一个可处理任务的 Agent | 工具、资源、prompt、context server | 网络中的 Agent identity 和 description |
| 核心问题 | Agent-to-Agent 任务协作怎么标准化 | AI 应用怎样标准接入外部能力 | Agent 怎样被识别、发现、描述并协商通信 |
| 典型入口 | Agent Card / task / message / artifact / 状态流转 | host / client / server / tools / resources / prompts | DID / Agent Description / discovery / encrypted communication / meta-protocol |
| 更像哪一层 | 跨系统 Agent 协作协议 | 工具与上下文连接协议 | Agent 网络互联与协议协商层 |
| 状态语义 | 远端 Agent 可有自己的任务状态和进度 | 工具调用返回 observation / result，状态多由 host 管 | 描述和协商入口，不等于具体任务状态协议 |
| 发现重点 | 找到能协作的 Agent 及其能力说明 | 找到可用 server / tool / resource | 找到可验证身份和描述的 Agent |
| 安全重点 | 远端 Agent 是否可信、权限是否过宽、结果是否可验证 | tool poisoning、least privilege、approval、server trust | identity、encrypted communication、description trust、开放发现攻击面 |
| 典型场景 | 研究 Agent 委托绘图 Agent 生成图表 | Agent 调用文件系统、数据库、浏览器、SaaS | Agent 在开放网络里发现对方并协商用什么协议交互 |
| 不解决 | 本地编排、最终验证、权限策略本身 | planning、memory、多 Agent 编排、安全策略本身 | 任务质量、具体协作协议细节、本地 Agent framework |

## 执行时序 / 机制差异

```text
ANP:
  Who is this agent?
  Where can I discover it?
  What does it claim it can do?
  How do we establish secure communication?
  Which protocol should we use?

A2A:
  Given an agent-to-agent task protocol,
  how do I send task/message/context,
  track state, stream progress,
  and receive artifact/result?

MCP:
  Given an AI host/app,
  how do I expose tools/resources/prompts
  from external servers
  so the model can use them through the host?
```

这个模型故意把“发现/身份”“任务协作”“工具连接”拆开。真实系统可能组合使用三者，但排错时要先定位问题在哪一层。

执行时序上，ANP 常出现在“连接前”：先识别、发现、读取描述、协商协议；A2A 出现在“协作中”：发送任务、跟踪状态、交换消息和 artifact；MCP 出现在“能力调用中”：host/client 发现 server 暴露的 tool/resource/prompt，并在权限边界内调用。真实系统不一定严格串行，但这个顺序能帮助判断问题属于哪一层。

## 学习类比（非证据）

非证据类比：可以把 ANP 想成“远端 Agent 的身份目录 + 名片 + 协议协商入口”，把 A2A 想成“两个协作者之间的任务委托和进度回报规则”，把 MCP 想成“AI 应用接入工具箱和资料柜的标准插口”。

类比边界：这个比喻只帮助记忆，不是官方定义。真实协议里身份、描述、任务、工具和权限会交叉出现，不能因为类比相似就把 A2A、MCP、ANP 合并成同一个 alias 族。

## 最容易混淆的边界

### A2A vs MCP

[[A2A]] 把远端能力看作能处理任务的 Agent；[[MCP]] 把远端能力暴露成工具、资源或 prompt。一个同步函数、数据库查询或文件读取更像 MCP/API；一个能接收任务、持续处理、返回进度、追问并交付 artifact 的远端能力更像 A2A。

### A2A vs ANP

A2A 关注任务协作协议。ANP 关注 Agent 网络互联入口：身份、发现、描述、安全通信和协议协商。一个 Agent 可以先通过 ANP 被发现和协商，然后使用 A2A 作为具体任务协作协议。

### MCP vs ANP

MCP 让 AI 应用连接外部工具和 context server。ANP 让 Agent 在网络中被识别、描述和协商通信。MCP 的 server 不一定是独立 Agent；ANP 的对象通常是带身份和能力描述的 Agent。

### Registry vs Discovery

[[MCP Registry]] / [[Tool Registry]] 更偏目录、发布、分发和治理。ANP discovery 更偏“如何找到并验证网络中的 Agent 描述”。目录可以辅助 discovery，但 discovery 还要处理 identity、trust、version 和 communication entry。

## 什么时候用哪个判断

| 场景 | 优先概念 | 为什么 |
|---|---|---|
| Agent 要调用文件系统、浏览器、数据库或 Jira | [[MCP]] | 对象是工具/资源/context server |
| Agent 要委托远端 Agent 完成一段任务，并等待进度/结果 | [[A2A]] | 对象有任务处理和状态语义 |
| Agent 要在开放网络中找到某个可信 Agent，并知道怎么和它通信 | [[ANP]] | 对象是 identity、description、discovery 和 negotiation |
| Agent 要判断是否把任务交给另一个执行者 | [[Handoff]] / [[Multi-agent Orchestration]] | 这是责任迁移和编排质量问题，不是单一协议问题 |
| 团队要发布和治理一组可用工具 | [[Tool Registry]] / [[MCP Registry]] | 这是目录、分发、版本和信任治理问题 |

## 现代系统如何吸收或限制

来源支持 A2A / MCP / ANP 的对象边界；下面的组合方式是工程综合 / inference，用于帮助架构判断，不代表任一协议官方要求系统必须这样串接。

一个现代 Agent 平台可能这样组合：

1. 用 ANP 风格的 identity / discovery / description 思路找到远端 Agent，并确认它的来源和能力。
2. 协商本次交互使用 A2A、普通 API 或其他协议。
3. 在本地 orchestrator 中把这次远端调用建模为 handoff 或 delegated task。
4. 用 MCP 连接本地或远端工具、数据库、浏览器和 context server。
5. 用 policy engine、least privilege、approval gate、trace 和 evaluation 检查安全与质量。

工程判断点：协议只让系统“能连接”。可靠协作还需要 ownership、权限、状态恢复、审计和最终验证。

## 它们共同不是什么

- 它们都不是 Agent framework。它们不替代 LangGraph / Agents SDK / AutoGen 这类本地编排和运行时。
- 它们都不是安全保证。身份、schema、tool description 和 Agent description 都可能过时、夸大或被污染。
- 它们都不是任务成功保证。协议能表达任务和能力，不保证计划正确、证据真实或结果可用。
- 它们都不是长期稳定 API 记忆题。尤其 A2A / ANP 的生态和字段仍要回源复查。

## 证据锚点

- Concept anchors: [[ANP#证据锚点]], [[A2A#证据锚点]], [[MCP#证据锚点]]
- Source anchors: [[Agent Network Protocol#主源事实]], [[Agent2Agent Protocol#为什么收]], [[Model Context Protocol 官方文档#为什么收]]
- Evidence type: concept-card synthesis + source/docs notes + engineering synthesis.
- Confidence: medium。A2A / MCP / ANP 的对象边界清晰，但协议生态和具体字段属于 frontier / volatile。
- Boundary: 本页沉淀对象边界和工程判断，不替代 A2A / MCP / ANP 官方文档或具体版本字段复查；学习类比不是来源证据。

## 复习触发

1. 远端能力什么时候更像 MCP tool，什么时候更像 A2A Agent？
2. 为什么 ANP 的 identity/discovery/description 层不能替代 A2A 的任务协作层？
3. 一个开放 Agent 网络里，Agent description 为什么不能直接等同于真实能力？
4. 如果系统已经用了 MCP，还缺什么才可能进入跨 Agent 网络互联？

## 相关链接

- [[ANP]]
- [[A2A]]
- [[MCP]]
- [[ACP]]
- [[Multi-agent Handoff Protocol 对比]]
- [[Tool 接口层对比]]
- [[Agent 知识地图]]
