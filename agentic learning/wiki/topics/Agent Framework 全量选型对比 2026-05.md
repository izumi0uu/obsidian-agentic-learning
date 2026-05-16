---
type: map
topic:
  - agent
  - framework
  - comparison
  - frontier
status: active
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: volatile
source:
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[Microsoft Agent Framework 官方文档]]"
  - "[[AutoGen 官方文档]]"
  - "[[CrewAI 官方文档]]"
  - "[[LlamaIndex Agents 官方文档]]"
  - "[[Pydantic AI 官方文档]]"
  - "[[Agno 官方文档]]"
  - "[[Mastra 官方文档]]"
  - "[[Vercel AI SDK 官方文档]]"
  - "[[Google ADK 官方文档]]"
  - "[[AgentScope 官方文档]]"
  - "[[CAMEL-AI 官方文档]]"
evidence:
  - "[[LangGraph 官方文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#一句话]]"
  - "[[Microsoft Agent Framework 官方文档#必读块 1：Agent vs workflow 边界]]"
  - "[[AutoGen 官方文档#必读块 1：Teams / group chat 抽象]]"
  - "[[CrewAI 官方文档#必读块 1：Agents / crews / flows 三层]]"
  - "[[LlamaIndex Agents 官方文档#必读块 1：agent loop 与 tool 选择]]"
  - "[[Pydantic AI 官方文档#必读块 1：type-safe agent framework 定位]]"
  - "[[Agno 官方文档#必读块 1：三层架构]]"
  - "[[Mastra 官方文档#必读块 1：agent vs workflow 边界]]"
  - "[[Vercel AI SDK 官方文档#必读块 1：ToolLoopAgent]]"
  - "[[Google ADK 官方文档#必读块 1：production agents 定位]]"
  - "[[AgentScope 官方文档#必读块 1：AgentScope 的平台定位]]"
  - "[[CAMEL-AI 官方文档#必读块 1：Role-playing / inception prompting]]"
related:
  - "[[Agent Framework]]"
  - "[[Agent Framework 编排范式对比]]"
  - "[[Agent 工程分层对比]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Tool Calling]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
  - "[[Human-in-the-loop]]"
  - "[[Agent Control Plane]]"
  - "[[Frontend-first AI Toolkit]]"
  - "[[Type-safe Agent SDK]]"
  - "[[Data-first Agent Framework]]"
  - "[[Role-playing Agent]]"
  - "[[Crew Orchestration]]"
  - "[[Provider-first Agent SDK]]"
  - "[[State Graph Runtime]]"
---

# Agent Framework 全量选型对比 2026-05

## 一句话总览

这 13 个热门 Agent framework / SDK / toolkit 不在同一层：[[LangGraph]]、[[Microsoft Agent Framework]]、Google ADK、Mastra 更接近 workflow/[[State Graph Runtime|runtime]]；OpenAI Agents SDK、Pydantic AI、Vercel AI SDK 更像模型/应用 SDK；CrewAI、AutoGen、CAMEL、AgentScope 更强调多 Agent 协作范式或平台；LlamaIndex 从 data/RAG 生态进入；Agno 更像 SDK + runtime + [[Agent Control Plane|control plane]] 的 Agent platform stack。

最小选型问题不是“哪个最火”，而是：**你需要谁来负责状态、流程、工具权限、数据/RAG、多人协作、观测评测和部署？** 如果这些责任没有先分层，framework 热度只会放大复杂度。

## 为什么这组值得对比

- 用户明确要求覆盖：LangGraph、OpenAI Agents SDK、Microsoft Agent Framework、AutoGen、CrewAI、LlamaIndex、Pydantic AI、Agno、Mastra、Vercel AI SDK、Google ADK、AgentScope、CAMEL。
- 它们都声称能构建 agentic applications，但抽象中心不同：graph、SDK、workflow、team、[[Role-playing Agent|role-playing]]、[[Data-first Agent Framework|data/RAG]]、[[Type-safe Agent SDK|type-safe Python]]、[[Frontend-first AI Toolkit|frontend streaming]]、[[Agent Control Plane|platform runtime]]。
- 这些差异会直接影响工程责任：状态是否显式、恢复是否可靠、人工审批在哪里、工具副作用如何限制、trace/eval 是否可用、是否绑定某个云/模型/语言生态。
- 证据足够：每个条目都有官方文档或一手 source note 锚点；本页的选型建议是基于文档的工程综合，而不是性能 benchmark。

边界：本页不是排行榜、star 数统计、性能评测或最新 API 教程。所有具体 SDK/API/产品能力都标记为 `freshness: volatile`，需要按官方文档定期复查。

## 共同问题域

这些工具都在处理同一组 Agent 工程问题：

```text
LLM call
  -> tool calling / structured output
  -> agent loop / state / memory
  -> workflow / graph / handoff / multi-agent
  -> human approval / guardrails / sandbox
  -> trace / eval / observability
  -> deployment / team governance / platform lifecycle
```

差异在于谁是“第一抽象”：有的先画图，有的先定义 Agent 类，有的先定义 crew/team，有的先定义 role-playing society，有的先处理 RAG/data，有的先接 UI streaming。

## 本页新增概念卡入口

这些卡不是框架排行榜，而是把选型时反复出现的边界词沉淀成可复习概念：[[State Graph Runtime]]、[[Provider-first Agent SDK]]、[[Crew Orchestration]]、[[Role-playing Agent]]、[[Data-first Agent Framework]]、[[Type-safe Agent SDK]]、[[Frontend-first AI Toolkit]]、[[Agent Control Plane]]。

## 快速选型矩阵

| 你真正需要的是 | 优先看 | 为什么 | 先警惕什么 |
|---|---|---|---|
| 可恢复、可审计的状态图 / human-in-the-loop workflow | LangGraph | state、nodes、edges、checkpoint、durable execution 是核心 | 图复杂度、状态 schema、节点幂等和部署治理仍要自己设计 |
| OpenAI-first 的 agent app，内置 handoffs / guardrails / tracing | OpenAI Agents SDK | SDK 直接围绕 OpenAI 平台抽象 Agent、tools、handoffs、guardrails、traces | 不要把它当通用 [[State Graph Runtime|state graph runtime]]；平台 API 易变 |
| 微软 / Azure / .NET / Semantic Kernel / AutoGen 迁移路线 | Microsoft Agent Framework | 官方当前把 agents 与 workflows 放进统一框架，并承接 AutoGen + SK 经验 | public preview / 继任路线仍 volatile；迁移成本需复查 |
| 对话式 multi-agent team / group chat 原型 | AutoGen | AgentChat Teams 以 group chat、speaker selection、termination、handoff 为核心 | 微软官方新路线偏 MAF；AutoGen 更适合沉淀 conversation-first 范式 |
| 业务角色协作 + [[Crew Orchestration|crew]] + flow + 企业控制台 | CrewAI | agents / crews / tasks / flows 同时覆盖角色协作和自动化流程 | 角色多不等于责任清；平台/企业能力边界需验证 |
| 知识密集型 Agent / RAG / query engine as tool | LlamaIndex | 数据连接、索引、query engine、AgentWorkflow 与 RAG 生态强 | 不要把 RAG 框架误当所有控制流的最佳 runtime |
| Python 类型安全、结构化输出、依赖注入、eval | Pydantic AI | Pydantic 验证 + deps/output/tools/evals/Logfire 适合后端工程 | 类型正确不等于事实正确；复杂流程可能还要 graph/workflow runtime |
| Agent 平台栈：SDK + runtime + [[Agent Control Plane|control plane]] | Agno | 官方三层架构强调 agents/teams/workflows、runtime service、AgentOS/control plane | 开源/商业/平台边界和组织治理成本需复查 |
| TypeScript-first full-stack agents + workflows + evals | Mastra | agents、workflows、memory、approval、observability、evals、deploy 同栈 | API/product 演进快；与 Vercel AI SDK 分工需明确 |
| Next.js / frontend streaming UI / lightweight tool loop | Vercel AI SDK | ToolLoopAgent、provider、[[Frontend-first AI Toolkit|streaming UI]]、telemetry、workflow patterns 贴近应用层 | 不是完整多 Agent 平台；复杂状态/恢复可能外接 runtime |
| Google / Gemini / Vertex / multi-language production agents | Google ADK | multi-agent、workflow agents、graph workflows、eval、deploy、context、Cloud path | 语言版本和 ADK 2.0 等能力状态需复查；生态绑定要评估 |
| message-centered multi-agent platform / 分布式实验与应用 | AgentScope | message、agent、tool、memory、observability、deployment、distributed 是平台线索 | 官方能力广，不等于所有部署都低成本可扩展 |
| [[Role-playing Agent|role-playing]] / agent society / communicative agents 研究与框架 | CAMEL | 原始地基是 role-playing + inception prompting，现代扩展到 agents/societies/memory/RAG | paper 范式不等于生产成熟度；与 AutoGen group chat 要切开 |

## 核心区别表

| 框架 / 路线 | 主要抽象 | 最适合判断的问题 | 容易误用的边界 | 证据锚点 |
|---|---|---|---|---|
| [[State Graph Runtime]] / [[LangGraph]] | state、node、edge、durable execution | 复杂流程是否需要可恢复状态图？ | 不等于所有 Agent SDK；简单脚本可能过重 | [[LangGraph 官方文档#一句话]] |
| [[Provider-first Agent SDK]] / OpenAI Agents SDK | agent、tool、handoff、guardrail、trace | 是否优先绑定模型供应商生态？ | 不等于通用 workflow runtime | [[OpenAI Agents SDK 文档#一句话]] |
| [[Type-safe Agent SDK]] / Pydantic AI | 类型、schema、依赖注入、结构化输出 | 是否要用类型边界压住工具和输出漂移？ | 类型安全不保证模型推理正确 | [[Pydantic AI 官方文档#必读块 1：type-safe agent framework 定位]] |
| [[Data-first Agent Framework]] / LlamaIndex | 数据、索引、query engine、agent workflow | 任务是否以知识检索和数据连接为中心？ | 不自动解决复杂 runtime 和治理 | [[LlamaIndex Agents 官方文档#必读块 1：agent loop 与 tool 选择]] |
| [[Crew Orchestration]] / CrewAI | role、task、crew、flow | 是否需要角色分工和业务协作结构？ | 角色名不等于可靠多 Agent 系统 | [[CrewAI 官方文档#必读块 1：Agents / crews / flows 三层]] |

## 全量对比表

| 框架 | 首要抽象 | 语言 / 生态 | 状态与流程 | 多 Agent | 数据 / 记忆 / RAG | 观测 / 评测 / 部署 | 现代性判断 |
|---|---|---|---|---|---|---|---|
| LangGraph | [[State Graph Runtime|state graph runtime]] | Python / JS，LangChain / LangSmith | 强：state、nodes、edges、checkpoint、durable execution、HITL | 可建 multi-agent graph | memory / store / persistence 可接入 | LangSmith、部署/平台能力 | current-practice；API watch |
| OpenAI Agents SDK | [[Provider-first Agent SDK|OpenAI-first agent SDK]] | Python，OpenAI platform | 中：agent loop、sessions、handoff；非底层 graph | handoffs 是核心协作方式 | tools、MCP、sessions；RAG 依赖外部/平台 | tracing、guardrails、platform 集成 | current-practice / volatile |
| Microsoft Agent Framework | agent + workflow 统一 SDK | Python / .NET / Microsoft / Azure | 强：agents vs workflows、state、middleware、telemetry | 支持 multi-agent / orchestration | Semantic Kernel / Azure 生态衔接 | telemetry、middleware、Azure path | frontier/volatile；preview 边界 |
| AutoGen | conversation-first team | Python，Microsoft / AutoGen | 中：team preset、termination、state；非首要 graph runtime | 强：group chat、speaker selection、handoff | tools / memory 可接入 | observability 有文档，但路线需看 MAF | transitional -> current-practice pattern |
| CrewAI | agents + crews + flows | Python / CrewAI platform | 中强：crews 管协作，flows 管显式流程 | 强：role/task/crew 协作 | memory、knowledge、tools | guardrails、observability、enterprise console | current-practice / volatile |
| LlamaIndex | [[Data-first Agent Framework|data/RAG-first agent workflow]] | Python / TS，LlamaCloud | 中：AgentWorkflow、FunctionAgent、workflows | 有 multi-agent patterns | 强：indexes、query engine、retrieval、RAG | observability/evaluating/LlamaCloud | current-practice；data-first |
| Pydantic AI | [[Type-safe Agent SDK|type-safe Python agent SDK]] | Python / Pydantic / Logfire | 中：Agent、deps、output、Pydantic Graph / durable | 有 MCP/A2A 等集成线索 | tools、structured output、deps；RAG 外接 | Pydantic Evals、Logfire | current-practice / volatile |
| Agno | SDK + runtime + [[Agent Control Plane|control plane]] | Python/platform，AgentOS | 中强：agents/teams/workflows + runtime | 强：teams / multi-agent demos | memory、knowledge、context providers | OTel、audit logs、RBAC、deploy | platform-frontier / volatile |
| Mastra | TypeScript agent + workflow framework | TypeScript / full-stack | 强：agents for open-ended，workflows for deterministic control | supervisor agents / multi-agent | memory、tools、MCP、structured output | observability、evals、deploy | current-practice / volatile |
| Vercel AI SDK | [[Frontend-first AI Toolkit|frontend-first AI app toolkit]] | TypeScript / Next.js / UI | 轻中：ToolLoopAgent、loop control、workflow patterns | subagents pattern | memory/context；RAG 外接 | telemetry、streaming UI、Vercel app stack | toolkit-current / volatile |
| Google ADK | multi-language agent development kit | Python / TS / Go / Java，Google Cloud | 强：workflow agents、graph workflows、sessions/context | 强：multi-agent systems、routing | memory/context/artifacts/tools/MCP | eval、observability、Cloud Run/GKE/Agent Runtime | frontier/volatile |
| AgentScope | message-centered multi-agent platform | Python / Alibaba / AgentScope | 中强：Msg、agent、orchestration、distribution | 强：message hub / multi-agent | tools、memory、MCP/A2A | observability、deployment、distributed | current-practice / volatile |
| CAMEL | [[Role-playing Agent|role-playing]] / agent society | Python / CAMEL-AI | 中：role-playing/society；现代模块扩展 | 强：communicative agents / societies | memory、RAG、synthetic data | framework/docs 能力需按版本核验 | foundation/transitional + volatile framework |

## 维度横切判断

| 维度 | 已成为当前工程实践的部分 | 更强代表 | 边界细节 |
|---|---|---|---|
| 显式工具调用 | 几乎所有框架都把 tools/function calling 结构化 | OpenAI Agents SDK、Pydantic AI、Mastra、Vercel AI SDK、LlamaIndex | tool schema 不等于权限治理；高风险工具还需要 approval、sandbox、audit |
| 显式状态 / workflow | graph、workflow、session、state 已经是主流 | LangGraph、Microsoft Agent Framework、Google ADK、Mastra、CrewAI flows | workflow 可恢复性取决于 checkpoint、幂等和外部副作用设计 |
| 多 Agent 协作 | team、handoff、crew、society、routing 都常见 | AutoGen、CrewAI、AgentScope、CAMEL、Google ADK、OpenAI Agents SDK | 多 Agent 增加成本和 trace 噪音；简单任务先优化 single agent |
| 数据 / RAG | RAG 不再只是检索函数，常被封为 agent tool / workflow | LlamaIndex、CAMEL、Agno、Google ADK、CrewAI | 知识检索强不代表开放式行动可靠；评估要分 RAG 与 agent trajectory |
| Human-in-the-loop | approval / interrupt / user input 逐渐成为生产默认 | LangGraph、Google ADK、Mastra、Agno、OpenAI Guardrails / handoffs 路线 | HITL 不是“问一下用户”这么简单，还涉及权限、审计和恢复 |
| Observability / eval | tracing、telemetry、evals 已成为框架卖点 | OpenAI Agents SDK、Pydantic AI/Logfire、Mastra、Google ADK、AgentScope、Agno | trace 只说明发生了什么；eval 才判断是否有效 |
| 部署 / 平台化 | SDK 之外的 runtime / cloud / console 重要性上升 | Google ADK、Agno、CrewAI、AgentScope、Microsoft AF | 平台化带来治理能力，也带来供应商绑定和版本风险 |
| 类型系统 / 语言生态 | Python 与 TypeScript 路线分化明显 | Pydantic AI、Microsoft AF、Mastra、Vercel AI SDK、Google ADK | 语言生态决定团队可维护性，不能只看 demo 效果 |

## 最容易混淆的边界

### LangGraph vs OpenAI Agents SDK

LangGraph 首先是 [[State Graph Runtime|state graph runtime]]：你显式设计状态、节点、边、循环和恢复。OpenAI Agents SDK 首先是 OpenAI-first SDK：你用 Agent、tools、handoffs、guardrails、tracing 快速构建 agentic app。前者更像“底层控制流骨架”，后者更像“平台 SDK”。

### Microsoft Agent Framework vs AutoGen

AutoGen 的稳定学习价值是 conversation-first team / group chat 范式。Microsoft Agent Framework 是微软当前把 AutoGen 与 Semantic Kernel 经验收敛后的 agent + workflow 统一路线。新项目如果在微软生态，不能只看 AutoGen；学习范式时仍值得理解 AutoGen。

### CrewAI vs AutoGen vs CAMEL

三者都容易被叫作“多 Agent 框架”。CrewAI 偏业务角色协作与流程自动化，AutoGen 偏 team/group chat orchestration，CAMEL 的地基是 role-playing / inception prompting。最小刀口：CrewAI 问 crew/flow，AutoGen 问谁发言/何时停止，CAMEL 问角色和任务如何被 inception。

### LlamaIndex vs LangGraph

LlamaIndex 的强项是 data/RAG/index/query engine 与 agent tool 的结合；LangGraph 的强项是任意状态图和可恢复流程。知识密集型任务可以先看 LlamaIndex；复杂控制流和 HITL recovery 更要看 LangGraph。

### Pydantic AI vs OpenAI Agents SDK

Pydantic AI 的关键是 Python 类型、Pydantic 验证、依赖注入和结构化输出；OpenAI Agents SDK 的关键是 OpenAI 平台原生 agent/tool/handoff/guardrail/tracing。前者更像 typed app SDK，后者更像 provider-first agent SDK。

### Mastra vs Vercel AI SDK

两者都在 TypeScript 生态。Mastra 更像完整 Agent + workflow framework，覆盖 memory、approval、observability、evals、deployment；Vercel AI SDK 更像 AI app / UI / streaming / tool-loop toolkit。可以组合，但必须明确谁负责 runtime，谁负责 UI。

### Agno vs AgentScope vs Google ADK

三者都带平台化味道。Agno 强调 SDK + Runtime + Control Plane / AgentOS；AgentScope 强调 message-centered multi-agent platform 与部署/分布式；Google ADK 强调 Google Cloud / multi-language / workflow agents / eval / deployment 生产路径。它们不只是 API 风格不同，而是组织治理和生态绑定不同。

## 现代性状态

- **foundation / transitional**：CAMEL 的 role-playing / inception prompting、AutoGen 的 group chat/team 是理解多 Agent 的重要地基和过渡范式；它们的思想被现代框架吸收，但具体 API/项目路线会变。
- **current-practice**：显式 tool calling、state/workflow、handoff/team、memory/RAG as tools、trace/eval、HITL、guardrails 已经是多个官方框架共同采用的工程实践。
- **frontier / volatile**：OpenAI Agents SDK、Microsoft Agent Framework、Google ADK、Agno、Mastra、CrewAI、Vercel AI SDK 等具体 SDK/API、云平台、部署路径、商业控制台、版本号和推荐集成都属于易变层。
- **不适用的比较方式**：用 GitHub star、官网口号或 demo 复杂度直接排名，不适合学习选型；需要回到状态、权限、评测和部署边界。

## 现代系统怎么吸收这些框架的价值 / 局限

现代系统很少只靠一个框架解决全部问题。更稳的组合方式是：

1. 用 framework / SDK 管理 agent、tools、state、workflow、handoff。
2. 用 harness / platform 管理权限、approval、sandbox、audit、成本、停止条件和用户体验。
3. 用 observability / eval 管理 trace、回放、回归测试、线上指标和人审。
4. 用团队治理管理版本锁定、工具白名单、数据边界、事故复盘和供应商风险。

因此，framework 的价值是降低工程样板和暴露控制点；局限是它不能自动给出正确业务目标、可靠工具、安全策略或评测集。

## 什么时候不用复杂 Agent Framework

- 任务是固定步骤、规则清楚、普通函数或传统 workflow 足够。
- 只需要一次结构化输出，不需要 tool loop、memory、state、handoff 或恢复。
- 还没有评测集、权限模型、工具幂等和 trace 需求，先上框架会让失败难以定位。
- 你的团队主要问题是数据质量、需求定义或业务流程不清，而不是 agent runtime 缺失。

## 执行时序 / 机制差异

Agent framework 的差异通常发生在运行时序：provider-first SDK 先把一次模型调用、tool loop 和 handoff 接进供应商平台；state graph runtime 先建模状态和节点，再让模型/工具作为节点执行；data-first framework 先组织索引、query engine 和知识工具；crew orchestration 先定义角色、任务和交接。这个时序差异会决定 debug、恢复、评估和权限控制落在哪一层。

## 学习类比（非证据）

可以把这些框架类比成不同类型的“施工组织方式”：provider-first 像使用某个厂商的一站式工具箱，state graph 像先画施工流程图，data-first 像先搭资料库和查询台，crew 像先安排岗位分工。

类比边界：这只是学习类比（非证据），不代表任何官方文档把框架定义成施工组织，也不替代具体 API / runtime 证据。

## 现代系统如何吸收或限制

来源支持的是各框架已经把 tool calling、state、trace、eval、deployment、权限或数据连接变成显式对象；工程综合 / inference 是：生产系统通常不会只选一个标签，而会把 provider SDK、state runtime、data layer、observability 和 governance 组合起来。限制在于框架生态变化快，2026-05 的选型判断需要按 `last_checked` 定期复查。

## 什么时候用哪个判断

- 先问任务主瓶颈：状态恢复、数据连接、类型边界、角色协作、供应商集成还是生产治理。
- 再问组织约束：团队语言栈、部署环境、合规权限、已有数据系统和 observability 栈。
- 最后问迁移成本：是否接受绑定某个 provider / framework runtime，还是更需要框架中立。

## 它们共同不是什么

它们共同不是“让模型自动可靠”的魔法层，也不是 eval、权限、数据治理和人工审批的替代品。框架只能提供抽象和运行面；具体任务边界、工具权限、失败回放、质量评估仍需要工程设计。

## 证据锚点

### Source notes

- [[LangGraph 官方文档]]：[[State Graph Runtime|state graph runtime]]、durable execution、human-in-the-loop。
- [[OpenAI Agents SDK 文档]]：Agent、tools、handoffs、guardrails、tracing、sessions、MCP。
- [[Microsoft Agent Framework 官方文档]]：agents vs workflows、AutoGen + Semantic Kernel successor / preview 边界。
- [[AutoGen 官方文档]]：Teams / group chat、speaker selection、termination、handoff。
- [[CrewAI 官方文档]]：agents、crews、tasks/processes、flows、memory、knowledge、observability、deployment。
- [[LlamaIndex Agents 官方文档]]：agent loop、tools/query engines、AgentWorkflow、multi-agent patterns。
- [[Pydantic AI 官方文档]]：type-safe Python agent framework、deps/output/tools/evals/Logfire/durable execution。
- [[Agno 官方文档]]：SDK / Runtime / Control Plane 三层、AgentOS、OTel、audit、RBAC、deploy。
- [[Mastra 官方文档]]：TypeScript agents vs workflows、memory、tools、approval、observability、evals。
- [[Vercel AI SDK 官方文档]]：ToolLoopAgent、loop control、structured workflows、streaming UI、telemetry。
- [[Google ADK 官方文档]]：production agents、multi-agent、workflow/graph workflows、eval、observability、deployment、context。
- [[AgentScope 官方文档]]：message-centered multi-agent platform、tools、memory、observability、deployment、distributed。
- [[CAMEL-AI 官方文档]]：role-playing / inception prompting、agents/societies/memory/RAG 模块。

### 外部官方链接

- LangGraph: <https://docs.langchain.com/oss/python/langgraph/overview>
- OpenAI Agents SDK: <https://openai.github.io/openai-agents-python/>
- Microsoft Agent Framework: <https://learn.microsoft.com/en-us/agent-framework/overview/>
- AutoGen: <https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html>
- CrewAI: <https://docs.crewai.com/>
- LlamaIndex Agents: <https://developers.llamaindex.ai/python/framework/understanding/agent/>
- Pydantic AI: <https://pydantic.dev/docs/ai/overview/>
- Agno: <https://docs.agno.com/>
- Mastra: <https://mastra.ai/docs/agents/overview>
- Vercel AI SDK: <https://ai-sdk.dev/docs/agents/overview>
- Google ADK: <https://adk.dev/>
- AgentScope: <https://doc.agentscope.io/>
- CAMEL-AI: <https://docs.camel-ai.org/>

Evidence type: 官方文档 / 官方 source note + 工程综合。Confidence: medium-high for abstraction centers; medium for roadmap、preview、版本和平台能力。

- Boundary: 本页记录 2026-05 的框架选型边界；产品 API、托管能力和生态定位会变化，需要按 source notes 复查。
## 复习触发

1. 如果你要做一个“能恢复、能审批、能回放”的长任务 Agent，为什么先看 state/workflow/[[State Graph Runtime|runtime]]，而不是先看哪个框架 demo 最酷？
2. CrewAI、AutoGen、CAMEL 都强调多 Agent，三者的第一抽象分别是什么？
3. LlamaIndex、LangGraph、Mastra 都能做 workflow，为什么 LlamaIndex 更偏 data/RAG，LangGraph 更偏 state graph，Mastra 更偏 TS full-stack？
4. OpenAI Agents SDK、Pydantic AI、Vercel AI SDK 都像 SDK，它们分别围绕什么生态建立边界？
5. 设计一个金融转账 Agent：哪些部分必须固定成 workflow / approval / audit，哪些部分才允许 agent 自主选择？

## 相关链接

- [[Agent Framework]]
- [[Agent Framework 编排范式对比]]
- [[Agent 工程分层对比]]
- [[Multi-agent Handoff Protocol 对比]]
- [[Tool 接口层对比]]
- [[Agent 安全控制点对比]]
- [[Evaluation 层次对比]]
- [[Observability Audit 对比]]
