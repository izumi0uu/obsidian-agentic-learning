---
type: map
topic:
  - agent
  - tools
  - protocol
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-20
source:
  - "[[Tool Use]]"
  - "[[Tool Calling]]"
  - "[[Agent Skills]]"
  - "[[Tool Registry]]"
  - "[[Tool Permissioning]]"
  - "[[MCP]]"
  - "[[MCP Transport]]"
  - "[[MCP Registry]]"
  - "[[Toolformer]]"
  - "[[OpenAI Function Calling 文档]]"
  - "[[Anthropic Tool Use 文档]]"
  - "[[Model Context Protocol 官方文档]]"
evidence:
  - "[[Tool Use#证据锚点]]"
  - "[[Tool Calling#证据锚点]]"
  - "[[Agent Skills#证据锚点]]"
  - "[[Tool Registry#证据锚点]]"
  - "[[Tool Permissioning#证据锚点]]"
  - "[[MCP#证据锚点]]"
  - "[[MCP Transport#证据锚点]]"
  - "[[MCP Registry#证据锚点]]"
related:
  - "[[Agent 知识地图]]"
  - "[[Tool Use]]"
  - "[[Tool Calling]]"
  - "[[Agent Skills]]"
  - "[[Tool Registry]]"
  - "[[Tool Permissioning]]"
  - "[[MCP]]"
  - "[[MCP Transport]]"
  - "[[MCP Registry]]"
  - "[[Agent 安全控制点对比]]"
---

# Tool 接口层对比

## 一句话总览

这页回答：Agent “会用工具 / 能力”到底由哪些层组成。最小边界是：[[Tool Use]] 是行为能力，[[Tool Calling]] 是模型表达调用意图的结构化接口，[[Agent Skills]] 是可按需加载的做事方法和资源包，[[Tool Registry]] 是 host 内部可用工具/能力目录，[[Tool Permissioning]] 是能不能看见、调用和带什么参数执行的授权机制，[[MCP]] 是连接外部 tools / resources / prompts 的协议，[[MCP Transport]] 是 MCP client/server 传递 JSON-RPC 消息的通道层，[[MCP Registry]] 是 MCP server 的发现和分发层。

最容易出错的理解是把这些都叫“function calling”。Function / tool calling 只解决“模型如何提出一个结构化调用请求”；它不自动解决工具从哪里来、是否可信、是否越权、是否需要审批、执行结果是否能作为可信 observation。

## 为什么这组值得对比

- 混淆风险高：Tool Use、Tool Calling、Tool Registry、MCP、MCP Registry 常被混称为“工具能力”。
- 共同问题域相同：都围绕“LLM / Agent 如何安全、可追踪地接入外部能力”。
- 不同介入点清晰：有的在模型输出层，有的在 host 目录层，有的在权限层，有的在跨进程/跨应用协议层。
- 证据密度足够：相关概念卡已有 Toolformer、OpenAI / Anthropic tool docs、MCP docs、MCP tool poisoning threat model 等锚点。
- 复习价值高：这组边界能帮助判断一个 Agent 工程问题究竟要改 schema、registry、permission、protocol，还是工具实现本身。

边界：这页不比较具体 SDK API 字段，也不把 MCP 当成完整 Agent framework；具体产品能力需要按各自 source 的 `freshness` 复查。

## 共同问题域

共同问题是：LLM 本身只能生成 token，不能天然查询实时信息、运行代码、读写文件、操作浏览器或调用企业系统。Agent 要行动，就必须把“模型想做什么”和“外部系统真正执行什么”接起来。

可以把接口层粗略拆成：

```text
task/context
  -> tool need / tool use decision
  -> tool call schema and arguments
  -> optional skill/workflow package selection
  -> registry exposes candidate tools
  -> permission layer filters / gates execution
  -> protocol/client connects external server
  -> transport carries MCP messages
  -> tool execution
  -> tool result / observation
```

这条链路的每一层失败方式不同：模型可能选错工具，schema 可能含糊，registry 可能暴露过多工具，permission 可能过宽，MCP server 可能不可信，transport 选型可能扩大网络暴露面，tool result 可能被注入或污染。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Tool Use]] | 行为能力：模型/Agent 借助外部能力完成任务 | 需求判断贯穿任务前、中、后 | 目标、上下文、可用工具、工具结果 | “是否用工具、用哪个、如何利用结果”的行为路径 | [[Tool Use#证据锚点]] |
| [[Tool Calling]] | 结构化调用接口：工具名、参数、schema | 模型生成 action intent 后，runtime 执行前 | tool schema、上下文、模型输出约束 | tool call 请求；通常还要 runtime 校验 | [[Tool Calling#证据锚点]] |
| [[Agent Skills]] | 可按需加载的能力包 / 做事方法 | 任务匹配后，工具调用前后都可能介入 | `SKILL.md`、metadata、脚本、模板、参考资料 | 可执行流程、上下文资源、脚本调用和完成标准 | [[Agent Skills#证据锚点]] |
| [[Tool Registry]] | host 内部工具目录和元数据管理 | 模型选择工具前；工具上线/下线/版本变化时 | 工具名、description、schema、版本、权限标签、来源 | 当前任务可见/可调用工具集合 | [[Tool Registry#证据锚点]] |
| [[Tool Permissioning]] | 授权与风险控制机制 | 工具展示前、调用前、参数提交前、执行前 | 用户/任务/工具/参数/数据范围/风险等级 | allow / deny / require approval / sandbox-only 等执行边界 | [[Tool Permissioning#证据锚点]] |
| [[MCP]] | AI host 连接外部 tools / resources / prompts 的协议层 | host 与 MCP server 建连、发现能力、调用 server 工具时 | MCP server 能力、tool definitions、resources、prompts、transport | 可被 host 转成模型工具空间的外部能力 | [[MCP#证据锚点]] |
| [[MCP Transport]] | MCP client/server 消息承载通道 | MCP client/server 已建立协议语义、需要传递 JSON-RPC 消息时 | JSON-RPC 消息、stdio 管道、Streamable HTTP endpoint、可选 SSE stream | 跨进程或跨网络传递的 MCP 请求/响应/通知 | [[MCP Transport#证据锚点]] |
| [[MCP Registry]] | MCP server 发现、发布、分发和版本入口 | 接入工具生态前；安装/升级/审查 server 时 | server 元数据、来源、版本、安装信息 | 候选 MCP server 列表；不等于安全背书 | [[MCP Registry#证据锚点]] |

## 最容易混淆的边界

- [[Tool Use]] vs [[Tool Calling]]：前者是“会不会借助外部能力”的行为问题；后者是“如何表达一次调用请求”的接口问题。一个系统可以有 tool calling API，却仍然不会在正确时机用工具。
- [[Agent Skills]] vs [[Tool Calling]]：skill 是做事方法和资源包，可能包含脚本、模板和参考资料；tool calling 是一次结构化调用请求。Skill 可以指导何时调用工具，但不是 tool call 本身。
- [[Agent Skills]] vs [[MCP]]：MCP 连接外部 server 暴露的 tools/resources/prompts；skill 组织 Agent 如何执行一类任务。Skill 可以调用 MCP tool，但 skill 自身不等于 MCP server。
- [[Tool Calling]] vs tool execution：tool call 是请求，不是执行本身。真正读文件、发请求、写数据库或付款的是 runtime / harness / 应用代码。
- [[Tool Registry]] vs [[MCP Registry]]：Tool Registry 可以是单个 host 内部的工具目录和权限视图；MCP Registry 更偏生态级 MCP server 发现与分发。被发现不等于可自动信任。
- [[MCP]] vs [[Tool Calling]]：MCP 是 host/client/server 的连接协议；Tool Calling 是模型输出结构化调用意图的接口。MCP server 暴露的 tool 最终仍可能被 host 转成模型可调用的 schema。
- [[Tool Permissioning]] vs [[Tool Registry]]：registry 记录“有哪些工具以及元数据”；permissioning 决定“当前任务、用户和参数下能不能看见/调用/执行”。
- [[Tool Permissioning]] vs [[Approval Gate]]：permissioning 是分层授权机制；approval gate 是高风险动作执行前的一个准入点，通常由 permission / policy 决定是否触发。

## 执行时序 / 机制差异

```text
Tool Use:          Goal -> decide external capability is needed -> use result in next reasoning/action
Tool Calling:      Tool schema -> model emits tool name + arguments -> runtime validates/executes -> observation
Agent Skills:      Skill metadata -> task match -> load SKILL.md/resources/scripts -> guide workflow/tool use
Tool Registry:     Tool lifecycle -> register/describe/version/tag -> expose subset to model/runtime
Tool Permissioning:User/task/data/risk -> allow/deny/gate/sandbox -> execute or stop
MCP:               Host/client -> discover server tools/resources/prompts -> call server -> receive result
MCP Registry:      Search/select server -> inspect metadata/source/version -> install/connect under host policy
```

机制上的关键分层是：模型只应该看到经过 host 和 policy 收窄后的工具空间；外部 server、registry 描述和工具结果都应被当成可能出错或被污染的输入，而不是天然可信控制指令。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把 Agent 工具层想成一家实验室：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Tool Use]] | 研究员知道什么时候需要用显微镜、计算器或数据库 | 说明行为能力，不说明接口格式 |
| [[Tool Calling]] | 填一张标准借用单：设备名、参数、用途 | 借用单不等于设备已经安全运行 |
| [[Agent Skills]] | 实验 SOP 和工具箱索引：某类实验该按什么流程做 | SOP 不是设备接口，也不能自动获得全部权限 |
| [[Tool Registry]] | 实验室设备目录：有哪些设备、型号、状态、负责人 | 目录不等于权限批准 |
| [[Tool Permissioning]] | 门禁和授权：谁能用、能用多久、能调哪些参数 | 权限规则仍需审计和更新 |
| [[MCP]] | 实验室和外部设备供应商之间的标准插口 | 插口标准化不等于供应商可信 |
| [[MCP Registry]] | 可采购/可安装供应商目录 | 上架不等于适合当前实验 |

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[Toolformer]] 和 [[Tool Use#证据锚点]] 支持“工具使用是一种模型/Agent 行为能力，需要判断何时调用、调用什么、如何利用结果”。
- [[OpenAI Function Calling 文档]]、[[Anthropic Tool Use 文档]] 和 [[Tool Calling#证据锚点]] 支持“结构化 schema / tool call / tool result 是现代工具接口的基础层”。
- [[Anthropic Agent Skills 文档]] 和 [[Agent Skills#证据锚点]] 支持“skill 是按需加载的能力包 / 做事方法，不是单次 tool call 或 MCP server”。
- [[Model Context Protocol 官方文档]]、[[MCP#证据锚点]] 和 [[MCP Registry#证据锚点]] 支持“协议与 registry 解决工具/上下文服务接入和发现问题”。
- [[MCP Tool Poisoning Threat Model]]、[[Tool Registry#证据锚点]] 和 [[Tool Permissioning#证据锚点]] 支持“工具描述、server 来源、权限和供应链是安全边界”。

### 工程综合 / inference

现代 Agent harness 通常会把工具接口拆成多层治理：schema 让调用可解析，registry 让工具可管理，permissioning 让工具可控，protocol 让外部能力可接入，trace/evaluation 让失败可复盘。把所有风险都压给 prompt 或 tool description，是不稳的架构。

### 仍需警惕的外推

- 不同厂商对 tool / function / tool result / strict mode 的 API 命名会变化；概念边界稳定，字段细节不稳定。
- MCP 与 MCP Registry 仍是快速演进生态；本页只沉淀协议/registry 的学习边界，不声明某个 registry 或 server 已安全。
- Registry metadata 和 tool descriptions 可能影响模型选择，应按不可信输入处理。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 想判断模型是否需要外部能力 | [[Tool Use]] | 关注行为决策：何时用工具、用哪个、结果怎么进入下一步 | 容易把“能调用”误当成“会正确使用” |
| 模型输出参数格式不稳定 | [[Tool Calling]] | 关注 schema、必填字段、枚举、strict mode 和 runtime validation | schema 正确仍可能业务越权 |
| 同类任务需要复用流程、脚本、模板和参考资料 | [[Agent Skills]] | 关注做事方法如何按需发现、加载和执行 | skill metadata 可能误导选择或扩大权限 |
| 工具数量变多、prompt 里塞不下 | [[Tool Registry]] | 需要目录、版本、可见性、描述和状态管理 | 工具描述本身可能被投毒 |
| 需要限制文件路径、网络域名、写操作或付款 | [[Tool Permissioning]] | 关注数据范围、参数范围、动作副作用和审批阈值 | 只隐藏工具名无法覆盖参数级越权 |
| 要把外部服务作为可复用工具接入多个 AI app | [[MCP]] | 关注 host/client/server 协议和能力发现 | 协议接入不是安全背书 |
| 要发现或安装 MCP server | [[MCP Registry]] | 关注 server 来源、版本、分发和升级入口 | registry 上架不等于可信或最小权限 |

## 它们共同不是什么

- 都不是完整 Agent。工具接口层不替代 planning、state、memory、evaluation、observability 或 handoff。
- 都不是安全保证。schema、registry、MCP 和 permissioning 都需要 policy、approval、sandbox、trace 和测试配合。
- 都不是工具实现本身。真正副作用发生在执行器、外部 API、文件系统、浏览器或数据库里。
- 都不是越多越好。暴露过多工具会增加选择错误、权限扩大、prompt injection 和 tool poisoning 风险。

## 证据锚点

- Concept anchors: [[Tool Use#证据锚点]], [[Tool Calling#证据锚点]], [[Agent Skills#证据锚点]], [[Tool Registry#证据锚点]], [[Tool Permissioning#证据锚点]], [[MCP#证据锚点]], [[MCP Registry#证据锚点]]
- Source examples: [[Toolformer]], [[OpenAI Function Calling 文档]], [[Anthropic Tool Use 文档]], [[Model Context Protocol 官方文档]], [[Model Context Protocol Python SDK Repo]], [[MCP Tool Poisoning Threat Model]]
- Evidence type: concept-card synthesis + paper/docs source notes + protocol source notes + engineering synthesis + learning analogy.
- Confidence: high for Tool Use / Tool Calling / execution boundary; medium for MCP Registry and registry/security layering because生态和具体实现仍在变化。
- Boundary: 类比只帮助学习，不是来源证据；MCP 相关判断只沉淀协议与工具治理边界，不替代最新官方文档复查。

## 复习触发

1. 一个系统支持 tool calling API，为什么仍可能没有可靠的 Tool Use？
2. Tool Registry 和 MCP Registry 的最小区别是什么？
3. MCP server 暴露了一个工具后，为什么 host 仍然需要 Tool Permissioning？
4. 如果工具描述里写“调用我可以安全读取所有文件”，系统应该相信吗？为什么？
5. schema validation、permissioning、approval gate 分别拦截哪一类失败？
6. 什么时候应该做成 Agent Skill，而不是只新增一个 tool schema？

## 相关链接

- [[Agent 知识地图]]
- [[Tool Use]]
- [[Tool Calling]]
- [[Agent Skills]]
- [[Tool Registry]]
- [[Tool Permissioning]]
- [[MCP]]
- [[MCP Registry]]
- [[Tool Poisoning]]
- [[Approval Gate]]
- [[Agent 安全控制点对比]]
