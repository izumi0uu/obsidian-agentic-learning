---
type: map
topic:
  - agent
status: active
created: 2026-05-05
updated: 2026-05-14
related:
  - "[[Agent]]"
  - "[[前沿主源清单]]"
  - "[[LLM]]"
  - "[[Agent Loop]]"
  - "[[Observation]]"
  - "[[Tool Calling]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
  - "[[Agent 工程分层对比]]"
  - "[[Agent Framework 编排范式对比]]"
  - "[[Tool 接口层对比]]"
---

# Agent 知识地图

这张地图负责回答：学习 Agent 时，哪些概念是地基，哪些概念是扩展。

前沿扩展见：[[前沿主源清单]]

## 地基

- [[LLM]]：模型如何生成文本，以及它本身不能做什么。
- [[Agent]]：什么是围绕目标行动的系统。
- [[Agent Loop]]：Agent 如何在观察、行动和反馈中推进任务。
- [[Observation]]：Agent 动作后的外部反馈如何回填到上下文、state 或 trace。

LLM 地基：

- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]

## 行动能力

- [[Tool Calling]]：模型如何通过结构化 tool call 和 schema 请求外部工具执行动作。
- [[Planning]]：目标如何拆成步骤，并在执行中调整。
- [[Memory]]：Agent 如何保存和使用过去的信息。
- [[Oh My Codex (OMX)]]：一个具体的 Codex CLI 编排实践，用来观察 Agent Harness 如何落地。
- [[Hermes Agent]]：一个具体的 self-improving Agent runtime，用来观察 memory、skills、messaging gateway、MCP、security approval 和 `/goal` 如何组合。
- [[OpenClaw Repo]]：一个 local-first personal assistant / Agent gateway source，用来观察多渠道入口、workspace memory、skills、sandbox、security audit 和 background tasks 如何组合。
- [[OMX $ 指令]]：理解 OMX 如何把澄清、计划、执行、研究、评审和 goal 验收做成可触发的 skill/workflow 入口。
- [[Agent Framework]]：理解 LangGraph、OpenAI Agents SDK、AutoGen 等框架解决的是哪层工程问题。
- [[Agent Framework 编排范式对比]]：区分 AutoGen、AgentScope、CAMEL、LangGraph、Microsoft Agent Framework 和 DeepAgents 的编排范式。
- [[AutoGen]]：理解 conversation-first team / group chat 多 Agent 编排。
- [[AgentScope]]：理解 message-centered multi-agent application platform。
- [[CAMEL]]：理解 role-playing / inception prompting 进入多 Agent 协作的范式。
- [[LangGraph]]：理解 state graph orchestration runtime。
- [[Microsoft Agent Framework]]：理解微软 AutoGen + Semantic Kernel 的 agent / workflow 统一路线。
- [[LangChain DeepAgents]]：理解 LangChain 如何在 LangGraph runtime 上封装长任务 Agent harness。
- [[Agent State]]：理解框架如何保存当前任务的进度、中间结果和下一步依据。
- [[Agent Workflow]]：理解框架如何把任务组织成步骤、分支、循环和交接。
- [[Agent Workflow Static Verification]]：理解显式 workflow graph 如何在部署前检查死路、不可达、human gate 覆盖和时序安全策略。
- [[Durable Execution]]：理解长任务为什么需要暂停、恢复和重试。
- [[Reflexion]]：理解 Agent 如何把失败反馈转成反思文本，并用经验改进下一轮行动。
- [[Human-in-the-loop]]：理解人类确认、接管和修正如何进入 Agent loop。
- [[Agent Lifecycle Hook]]：理解 runtime 如何在工具调用前后、会话开始/停止和上下文压缩等边界拦截、记录和恢复 Agent loop。

## 知识能力

- [[RAG]]：如何从外部知识库检索资料再生成回答；完整学习入口见 [[RAG 主题]]。
- [[Document Ingestion]]、[[Chunking]] 和 [[Embedding]]：理解资料进入知识库、被切成证据单元并变成语义表示的入口质量。
- [[Retriever]]、[[Vector Database]]、[[Hybrid Search]] 和 [[Reranking]]：理解生产 RAG 的召回、基础设施、混合检索和排序质量层。
- [[Knowledge Graph]]、[[GraphRAG]] 和 [[Neo4j]]：理解关系结构、图增强检索和图数据库工程生态如何结合。
- [[RAG Evaluation]]：理解 RAG 失败要分层评估检索、上下文、引用和最终回答。
- [[RAG Citation Faithfulness]] 和 [[RAG Access Control]]：理解 RAG 可靠性不只看答案，还要看引用支持和权限过滤。
- [[Query Rewrite]]、[[Query Planning]] 和 [[Agentic Retrieval]]：理解检索层如何从改写 query 走向检索计划和多轮检索控制。
- [[Entity Resolution]] 和 [[Graph Construction Evaluation]]：理解 GraphRAG 的构图质量、实体合并和评估边界。
- [[RAG 可靠性与治理对比]]、[[Query Rewrite Query Planning Agentic Retrieval 对比]]、[[GraphRAG 构图与评估对比]]：RAG 可靠性、检索决策和构图评估的对比入口。
- [[Obsidian + LLM Wiki]]：我的个人知识库如何适配 LLM 辅助学习。


## Framework 选型边界概念

- [[State Graph Runtime]]：区分状态图运行时和普通 SDK / UI toolkit。
- [[Provider-first Agent SDK]]：区分供应商优先 SDK 和通用 workflow runtime。
- [[Crew Orchestration]]：区分 crew / 角色任务协作和普通 group chat。
- [[Role-playing Agent]]：理解 CAMEL 式 role-playing / inception prompting 的稳定地基与生产边界。
- [[Data-first Agent Framework]]：区分 data/RAG-first 框架和通用状态图框架。
- [[Type-safe Agent SDK]]：区分类型/结构验证和事实正确性。
- [[Frontend-first AI Toolkit]]：区分 UI streaming/tool-loop toolkit 和完整 Agent platform。
- [[Agent Control Plane]]：区分 SDK、runtime 和平台治理控制面。

## 可靠性

- [[Evaluation]]：如何检查 Agent 是否稳定有效。
- [[RAG Evaluation]]：理解 RAG 失败要分层评估。
- [[Observability]]：理解 Agent 系统的 trace、span、日志、成本、延迟和错误如何被实时观察。
- [[Trace]]：理解执行过程如何被保存成可调试、可重放、可评估的记录。
- [[Agent Workflow Static Verification]]：理解 workflow topology 的静态检查和 runtime trace / guardrails 的互补关系。
- [[OpenTelemetry GenAI]]：理解 trace 标准化为什么重要。
- [[Audit Log]]：理解可审计行动记录和 trace 的边界。

## 安全和基础设施

- [[Code Execution Sandbox]]：理解 Agent 运行代码为什么需要隔离。
- [[LLM Gateway]]：理解模型调用路由、fallback、限流和成本治理。
- [[MCP Registry]]：理解工具发现和供应链治理。
- [[Guardrails]]、[[Tool Permissioning]]、[[Data Exfiltration]]：理解生产 Agent 的安全边界。
- [[Agent Workflow Static Verification]]：理解部署前 graph safety check 和运行时防护的边界。

## 前沿扩展

- [[前沿主源清单]]：Agent 领域当前需要追踪的概念结构。
- [[03 前沿追踪]]：还没稳定成概念卡的新词和前沿判断记录。


## 对比入口

- [[Agent 工程分层对比]]：区分 framework、harness、workflow、state 和 loop。
- [[Agent Framework 全量选型对比 2026-05]]：按当前官方文档横向比较 13 个热门 Agent framework / SDK / toolkit 的抽象层、状态/流程、多 Agent、RAG/memory、观测评测、部署和选型边界。
- [[Tool 接口层对比]]：区分 tool use、tool calling、registry、permissioning、MCP 和 registry。
- [[Agent 安全控制点对比]]：区分 prompt injection、tool poisoning、data exfiltration、guardrails、policy engine、approval gate 和 least privilege tools。
- [[Agent Memory 类型对比]]：区分 state、long-term、episodic、semantic、reflection、parametric / non-parametric memory。
- [[Multi-agent Handoff Protocol 对比]]：区分 orchestration、handoff、A2A、ACP、MCP、workflow 和 durable execution。
- [[Browser Computer Use 执行栈对比]]：区分 browser agent、computer use、GUI grounding、observation、sandbox 和 permissioning。
- [[Coding Agent 执行边界对比]]：区分 coding agent、repo context、patch validation、sandbox、code execution sandbox 和 AGENTS.md。
- [[OpenClaw Repo vs Hermes Agent]]：区分 OpenClaw 的 Gateway-first personal assistant harness 和 Hermes 的 runtime-first self-improving agent harness。
- [[Evaluation 层次对比]]：区分 evaluation、benchmark、eval harness、LLM-as-Judge、task success rate、RAG evaluation 和 trajectory evaluation。
- [[Observability Audit 对比]]：区分 observability、trace、audit log、replay 和 OpenTelemetry GenAI。
- [[ReAct Plan-and-Solve Reflexion 对比]]：从“行动前计划 / 执行中观察校正 / 执行后反思经验”切开 ReAct、Plan-and-Solve 和 Reflexion。
- [[Environment Observation 类型对比]]：区分 Environment、Observation、Tool Result 等反馈来源。
- [[Trajectory Trace 类型对比]]：区分 trajectory、trace、reasoning trace、trajectory evaluation 和 replay。
- [[RAG 类型对比]]：区分 RAG、Agentic RAG、Corrective RAG、Self-RAG 等检索增强路线。
- [[Context RAG Memory 对比]]：区分 context engineering、RAG、memory、repo context 和 retriever。
- [[Retrieval 组件对比]]：区分 retrieval pipeline 的入库、表示、召回、混合检索和重排。
- [[RAG 可靠性与治理对比]]：区分 RAG evaluation、citation faithfulness、access control、trace 和 audit 的治理位置。
- [[Query Rewrite Query Planning Agentic Retrieval 对比]]：区分 query rewrite、query planning、agentic retrieval 和 agentic RAG。
- [[GraphRAG 构图与评估对比]]：区分 knowledge graph、entity resolution、graph construction evaluation、GraphRAG 和 Neo4j。
- [[LLM 输入输出基础边界对比]]：区分 token、context window、prompt 和 hallucination。

## 当前概念卡

```dataview
TABLE topic, status, updated, related
FROM "wiki/concepts"
WHERE type = "concept"
SORT file.name ASC
```

## 下一批要补的概念

- [x] [[Token]]
- [x] [[Context Window]]
- [x] [[Prompt]]
- [x] [[Hallucination]]
- [x] [[Embedding]]
- [x] [[Vector Database]]
- [x] [[Chunking]]
- [x] [[Reranking]]
- [x] [[Hybrid Search]]
- [x] [[Document Ingestion]]
- [x] [[RAG Evaluation]]
- [x] [[Context Engineering]]
- [x] [[Neo4j]]
- [x] [[Guardrails]]
- [x] [[Human-in-the-loop]]
- [x] [[Tool Permissioning]]
- [x] [[Agent Framework]]
- [x] [[Agent State]]
- [x] [[Agent Workflow]]
- [x] [[Durable Execution]]
- [x] [[Reflexion]]
- [x] [[Handoff]]
- [x] [[Code Execution Sandbox]]
- [x] [[LLM Gateway]]
- [x] [[OpenTelemetry GenAI]]
- [x] [[MCP Registry]]
- [x] [[Audit Log]]
- [x] [[Data Exfiltration]]
- [x] [[Agent Harness]]
- [x] [[Eval Harness]]
- [x] [[GraphRAG]]
- [x] [[Agentic RAG]]
- [x] [[Long-term Memory]]
- [x] [[Computer Use]]
- [x] [[Trace]]
- [x] [[Trajectory]]
- [x] [[Prompt Injection]]
- [x] [[Oh My Codex (OMX)]]
- [x] [[OMX $ 指令]]
- [x] [[Agent Lifecycle Hook]]
- [x] [[LangChain DeepAgents]]

## 复习入口

- [[01 术语表]]：基础术语和前沿术语的一句话入口。
- [[02 问题池]]：把费曼复述时暴露出来的卡点沉淀成问题。
- [[05 Query 写回队列]]：把聊天里值得长期保留的解释写回 wiki。
