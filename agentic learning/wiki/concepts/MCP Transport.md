---
type: concept
topic:
  - agent
  - tools
  - protocol
  - infrastructure
status: growing
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: watch
conflicts: []
aliases:
  - MCP Transports
  - MCP 传输
  - MCP 传输层
  - MCP 通信方式
  - MCP Stdio Transport
  - MCP Streamable HTTP Transport
  - MCP SSE Transport
  - Stdio Transport
  - Streamable HTTP Transport
  - HTTP+SSE Transport
source:
  - "[[Model Context Protocol 官方文档]]"
  - "[[048 ai tools 13. MCP 协议通常采用什么通信方式？]]"
  - "[[055 ai tools 4. 什么是 MCP（模型上下文协议）？讲讲它的核心内容？]]"
  - "[[056 ai tools 5. MCP 由哪几部分组成？]]"
  - "[[049 ai tools 14. 说说 WebSocket 和 SSE 通信的区别及局限性？]]"
evidence:
  - "[[Model Context Protocol 官方文档#Transport 补充]]"
  - "[[048 ai tools 13. MCP 协议通常采用什么通信方式？#MCP 的消息格式：JSON-RPC 2.0]]"
  - "[[048 ai tools 13. MCP 协议通常采用什么通信方式？#传输方式一：stdio（标准输入输出）]]"
  - "[[048 ai tools 13. MCP 协议通常采用什么通信方式？#传输方式二：Streamable HTTP（当前标准的远程传输）]]"
  - "[[048 ai tools 13. MCP 协议通常采用什么通信方式？#为什么 SSE 被弃用了]]"
  - "[[049 ai tools 14. 说说 WebSocket 和 SSE 通信的区别及局限性？#在 AI 场景下怎么选？]]"
related:
  - "[[MCP]]"
  - "[[Tool Calling]]"
  - "[[Tool Registry]]"
  - "[[Tool Permissioning]]"
  - "[[MCP Registry]]"
---

# MCP Transport

## 一句话

MCP Transport 是 [[MCP]] client 和 server 之间承载 JSON-RPC 消息的传输层；当前要优先记住两种标准形态：本地用 `stdio`，远程用 `Streamable HTTP`。

## 概念详解

MCP 的上层语义是 host / client / server 如何发现 tools、resources、prompts 并发起调用；[[MCP Transport|传输层]]回答的是更低一层的问题：这些 JSON-RPC 消息具体从哪个通道过去、结果又从哪个通道回来。这个分层很重要，因为消息格式和传输方式是解耦的：同一类 `tools/call`、`resources/read` 或通知消息，可以跑在本地标准输入输出，也可以跑在远程 HTTP 连接上。

官方当前文档把 `stdio` 和 `Streamable HTTP` 列为标准 transport。`stdio` 的心智模型是“client 启动一个本地 server 子进程，然后用 stdin / stdout 管道传 JSON-RPC 消息”。它适合本地文件系统、代码仓库、桌面工具等近端能力：不需要开网络端口，生命周期通常跟随 host/client 管理，安全面也更集中在本机进程和文件权限上。

`Streamable HTTP` 的心智模型是“server 作为独立 HTTP 服务提供一个 MCP endpoint，client 用 HTTP POST 发送 JSON-RPC 消息，server 根据情况返回普通 JSON 或 SSE 流”。它适合远程部署、团队共享、多 client 连接和云端服务。代价是需要认真处理认证、Origin 校验、网络断连、会话状态和暴露面。

`SSE Transport` 容易被说乱。MCP 早期远程传输曾使用 `HTTP + SSE` 双端点方案：一个 POST 端点接收 client 请求，一个 SSE 端点持续推 server 消息。后来的 `Streamable HTTP` 用单 endpoint 合并了这条路径，但并不等于完全不用 SSE；当 server 需要流式返回多条消息时，响应体仍可能是 `text/event-stream`。所以更准确的说法是：旧的 `HTTP+SSE` transport 是 legacy / deprecated compatibility；SSE 作为流式响应机制仍可能被 Streamable HTTP 使用。

`HTTP Transport` 这个词太宽，单独录入会制造误解。普通 HTTP REST、早期 HTTP+SSE、当前 Streamable HTTP 都可能被口头说成“HTTP”，但它们的连接语义不同。学习和面试时应说清楚是 `Streamable HTTP`，而不是泛泛地说“HTTP 传输”。`Memory Transport` 也不适合单独建概念卡：它通常是 SDK 内部、测试或同进程模拟用的 transport，帮助写单元测试或连接 in-memory client/server，不是生产部署时和 `stdio` / `Streamable HTTP` 平级的标准选择。

## 它解决什么问题

- 把 MCP 的消息格式和底层通道拆开：JSON-RPC 负责“消息长什么样”，transport 负责“消息怎么送达”。
- 支持本地工具和远程服务两类部署：本地可以无网络、低延迟；远程可以多 client 共享、集中运维。
- 让同一个 MCP server 能被不同 host/client 复用，同时保留按部署场景选择通道的空间。

## 它不是什么

MCP Transport 不是 [[Tool Calling]]。Tool Calling 是模型输出结构化调用意图的接口；MCP Transport 是 MCP client/server 传递 JSON-RPC 消息的通道。

它也不是 [[MCP]] 的全部。MCP 还包括角色分工、能力发现、tools/resources/prompts 语义、schema、权限和安全边界；transport 只处理连接和消息承载。

它更不是“只要用了 HTTP 就是 Streamable HTTP”。HTTP 是底层协议族，Streamable HTTP 是 MCP 当前定义的远程 transport 形态；旧 HTTP+SSE 是历史兼容边界；普通 REST API 不是自动等于 MCP Transport。

## 最小例子

本地 `stdio`：

```text
host/client 启动 filesystem MCP server 子进程
client -> server stdin: {"jsonrpc":"2.0","method":"tools/call",...}
server stdout -> client: {"jsonrpc":"2.0","result":...}
```

远程 `Streamable HTTP`：

```text
client POST https://example.com/mcp
Accept: application/json, text/event-stream
Body: JSON-RPC request

server 简单请求 -> application/json
server 流式/多消息 -> text/event-stream
```

本机服务也可以用这张卡理解：`stdio` 更像“host 直接拉起一个本地进程”；如果某个 server 暴露 localhost 的 `/mcp` endpoint，则更像“本机上的 Streamable HTTP server”。即使地址仍在本机，连接语义也已经从进程管道切到 HTTP endpoint。

## 常见误解

- 误解：MCP 远程传输就是 WebSocket。更准确：当前标准远程 transport 是 Streamable HTTP；SSE 可作为流式响应机制出现，WebSocket 不是 MCP 当前标准 transport。
- 误解：SSE Transport 已经完全没用了。更准确：旧的 HTTP+SSE 双端点 transport 是 legacy / deprecated；SSE 作为 HTTP 流式响应机制仍被 Streamable HTTP 吸收。
- 误解：HTTP Transport 是一个清楚概念。更准确：必须区分普通 HTTP、HTTP+SSE legacy transport 和 Streamable HTTP。
- 误解：Memory Transport 值得和 stdio、Streamable HTTP 并列学习。更准确：它更像 SDK 内部/测试 transport，用来做 in-process 连接或单元测试，不是面向部署选型的核心概念。

## 边界细节

| 名称 | 是否值得单独建卡 | 在本卡中的边界 |
| --- | --- | --- |
| `Stdio Transport` | 不单独建弱卡 | 当前标准 transport；本地子进程、stdin/stdout、低延迟、无网络端口 |
| `Streamable HTTP Transport` | 不单独建弱卡 | 当前标准 transport；远程/共享 server；单 endpoint；可普通 JSON 或 SSE stream |
| `SSE Transport` | 不单独建弱卡 | 旧 HTTP+SSE 双端点方案属于 legacy；SSE 机制仍可被 Streamable HTTP 用于流式返回 |
| `HTTP Transport` | 不建卡 | 词太宽，容易把 REST、HTTP+SSE、Streamable HTTP 混在一起 |
| `Memory Transport` | 不建卡 | SDK/测试/in-process 边界；不是生产部署主 transport |

本卡没有写 `up`：[[09 概念层级审计基线]] 当前没有稳定的 “protocol transport” 父类，`[[MCP]]` 也是 relation-only protocol anchor，不应直接把“组成部分/支撑层”升格为 taxonomy parent。后续若创建稳定的协议/transport 父类，应走 taxonomy 候选、dry-run 和 limited apply。

## 现代性状态

current-practice / watch。`stdio` 和 `Streamable HTTP` 是当前 MCP 文档中的标准 transport，但 MCP 规范、SDK 和远程 server 安全实践仍在演进；涉及生产部署时要按 `last_checked` 复查官方文档，尤其是 Streamable HTTP 的认证、Origin 校验、session 和 SSE 行为。

## 现代系统怎么吸收这个概念的价值

现代 Agent host 通常不会让模型直接关心 transport。host/client 负责把某个 MCP server 通过 `stdio` 或 `Streamable HTTP` 接进来，再把 server 暴露的能力转换成模型可见工具空间。模型看到的是工具 schema 和上下文，transport 影响的是延迟、部署、安全面、共享方式和故障恢复。

选型时可以用一个简单判断：

- 本地、单用户、跟随桌面应用或 CLI 生命周期：优先 `stdio`。
- 远程、团队共享、需要集中部署/认证/观测：优先 `Streamable HTTP`。
- 看到旧教程写 `SSE`：先判断它说的是 legacy HTTP+SSE transport，还是 Streamable HTTP 响应里的 SSE stream。
- 看到 SDK 里的 `MemoryTransport`：把它当测试/内部连接工具，不当生产协议边界。

## 证据锚点

- Evidence type: official docs — [[Model Context Protocol 官方文档#Transport 补充]] 记录官方 docs / spec 当前把 `stdio` 和 `Streamable HTTP` 作为标准 transport，并说明 Streamable HTTP 替代 2024-11-05 的 HTTP+SSE transport。
- Evidence type: source evidence — [[048 ai tools 13. MCP 协议通常采用什么通信方式？#传输方式一：stdio（标准输入输出）]]；[[048 ai tools 13. MCP 协议通常采用什么通信方式？#传输方式二：Streamable HTTP（当前标准的远程传输）]]；[[048 ai tools 13. MCP 协议通常采用什么通信方式？#为什么 SSE 被弃用了]]
- Evidence type: adjacent transport evidence — [[049 ai tools 14. 说说 WebSocket 和 SSE 通信的区别及局限性？#在 AI 场景下怎么选？]] 用来理解为什么 AI 文本流常用 SSE，以及为什么 WebSocket 不是默认答案。
- Boundary: `HTTP Transport` 和 `Memory Transport` 只作为边界说明，不作为独立概念卡。
- Confidence: high for current stdio / Streamable HTTP boundary; medium for SDK-specific Memory Transport naming because different SDKs may expose it differently.

## 复习触发

- 为什么说 JSON-RPC 是消息格式，transport 是承载通道？
- 本地 MCP server 为什么常用 `stdio`，而不是默认开 localhost HTTP 服务？
- Streamable HTTP 和旧 HTTP+SSE 的最小区别是什么？
- 为什么不能把 `SSE Transport`、`HTTP Transport`、`Memory Transport` 都平铺成同等级概念？

## 相关链接

- [[MCP]]
- [[Tool Calling]]
- [[Tool Registry]]
- [[Tool Permissioning]]
- [[MCP Registry]]
