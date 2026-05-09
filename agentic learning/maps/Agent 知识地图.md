---
type: map
topic:
  - agent
status: active
created: 2026-05-05
updated: 2026-05-08
related:
  - "[[Agent]]"
  - "[[前沿主源清单]]"
  - "[[LLM]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
---

# Agent 知识地图

这张地图负责回答：学习 Agent 时，哪些概念是地基，哪些概念是扩展。

前沿扩展见：[[前沿主源清单]]

## 地基

- [[LLM]]：模型如何生成文本，以及它本身不能做什么。
- [[Agent]]：什么是围绕目标行动的系统。
- [[Agent Loop]]：Agent 如何在观察、行动和反馈中推进任务。

LLM 地基：

- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]

## 行动能力

- [[Tool Calling]]：模型如何请求外部工具执行动作。
- [[Planning]]：目标如何拆成步骤，并在执行中调整。
- [[Memory]]：Agent 如何保存和使用过去的信息。
- [[Oh My Codex (OMX)]]：一个具体的 Codex CLI 编排实践，用来观察 Agent Harness 如何落地。
- [[Agent Framework]]：理解 LangGraph、OpenAI Agents SDK、AutoGen 等框架解决的是哪层工程问题。
- [[Agent State]]：理解框架如何保存当前任务的进度、中间结果和下一步依据。
- [[Agent Workflow]]：理解框架如何把任务组织成步骤、分支、循环和交接。
- [[Durable Execution]]：理解长任务为什么需要暂停、恢复和重试。
- [[Reflexion]]：理解 Agent 如何把失败反馈转成反思文本，并用经验改进下一轮行动。
- [[Human-in-the-loop]]：理解人类确认、接管和修正如何进入 Agent loop。

## 知识能力

- [[RAG]]：如何从外部知识库检索资料再生成回答。
- [[Document Ingestion]]：理解资料进入知识库前的解析、切分和元数据质量。
- [[Vector Database]]：理解向量检索底座。
- [[Hybrid Search]] 和 [[Reranking]]：理解生产 RAG 的检索质量层。
- [[Neo4j]]：GraphRAG 工程实现层，帮助理解图数据库、知识图谱和检索系统如何结合。
- [[Obsidian + LLM Wiki]]：我的个人知识库如何适配 LLM 辅助学习。

## 可靠性

- [[Evaluation]]：如何检查 Agent 是否稳定有效。
- [[RAG Evaluation]]：理解 RAG 失败要分层评估。
- [[OpenTelemetry GenAI]]：理解 trace 标准化为什么重要。
- [[Audit Log]]：理解可审计行动记录和 trace 的边界。

## 安全和基础设施

- [[Code Execution Sandbox]]：理解 Agent 运行代码为什么需要隔离。
- [[LLM Gateway]]：理解模型调用路由、fallback、限流和成本治理。
- [[MCP Registry]]：理解工具发现和供应链治理。
- [[Guardrails]]、[[Tool Permissioning]]、[[Data Exfiltration]]：理解生产 Agent 的安全边界。

## 前沿扩展

- [[前沿主源清单]]：Agent 领域当前需要追踪的概念结构。
- [[03 前沿追踪]]：还没稳定成概念卡的新词和前沿判断记录。

## 当前概念卡

```dataview
TABLE topic, status, updated, related
FROM "wiki/concepts"
WHERE type = "concept"
SORT file.name ASC
```

## 下一批要补的概念

- [ ] Token
- [ ] context window
- [ ] prompt
- [ ] hallucination
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
- [x] [[Prompt Injection]]
- [x] [[Oh My Codex (OMX)]]

## 30 天路线

- [[00 学习路线]]：从 [[2026-05-06]] 到 [[2026-06-04]] 的每日学习轨道。
- [[01 术语表]]：基础术语和前沿术语的一句话入口。
