---
type: map
topic:
  - query
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-20
related:
  - "[[LLM Wiki 工作流]]"
  - "[[02 问题池]]"
  - "[[04 页面目录]]"
---

# 05 Query 写回队列

这页收集“聊天里已经产生了有用理解，但还没写回 wiki”的内容。

## 使用规则

- 如果回答产生了新定义、新边界、新对比、新操作流程，必须进入这里或直接写进概念卡。
- 每周维护时处理 pending 项。
- 写回后把状态改成 `done`，并链接目标页面。

## 队列

| 日期 | 状态 | 问题 | 应写入 | 处理 |
|---|---|---|---|---|
| 2026-05-07 | done | “我现在这个项目践行了 LLM Wiki 吗？” | [[Obsidian + LLM Wiki]], [[LLM Wiki 工作流]] | 已写回“早期可用版 / 人工监督的 LLM 学习 wiki”边界 |
| 2026-05-07 | done | “$ralplan 底层是在做什么？” | [[Oh My Codex (OMX)]], [[oh-my-codex 使用教程]] | 已写回 prompt routing + state + plan artifact + stop hook |
| 2026-05-08 | done | “现在的 agent 都在使用 ReAct 范式吗？ReAct 的局限现在怎么解决？” | [[ReAct]], [[Agent Loop]], [[Agent Harness]] | 已写回 ReAct 作为行动循环思想、不是所有 Agent 固定模板的边界 |
| 2026-05-08 | done | “现在框架是怎么更好地接管 ReAct / Plan-and-Solve 这类 prompt pattern？” | [[Agent Framework]], [[Agent Harness]], [[Tool Calling]] | 已写回框架接管 prompt loop 的工具、状态、流程、执行、权限、观测六层 |
| 2026-05-09 | done | “现在的 LLM 模型是怎么被训练得越来越强的？” | [[LLM]], [[Evaluation]], [[LLM Training Pipeline]] | 已写回：预训练 scaling、数据质量、SFT、偏好优化/RLHF/RLAIF、推理强化、工具/代码/多模态训练、评测闭环和 Agent 框架兼容性 |
| 2026-05-11 | done | “Deep Agent 是什么？” | [[LangChain DeepAgents]], [[03 前沿追踪]] | 已写回 LangChain / LangGraph `deepagents` 作为具体 SDK / harness；边界区分通用 deep agent 形态和 RUC-NLPIR DeepAgent 论文/项目名 |
| 2026-05-12 | done | “建立概念对比 / 类比 topic 机制，并以 ReAct / Plan-and-Solve / Reflexion 做样板” | [[LLM Wiki 工作流]], [[ReAct Plan-and-Solve Reflexion 对比]], [[概念对比页]] | 已写回准入标准、证据边界、模板、样板页和候选队列 |
| 2026-05-12 | done | “当前热门 Agent Framework 全量对比，覆盖 13 个框架并写入 wiki” | [[Agent Framework 全量选型对比 2026-05]], [[Agent Framework]] | 已写回官方来源、选型矩阵、全量对比表、现代性状态和复习触发 |
| 2026-05-12 | done | “Agent Framework 全量选型对比页里还有概念没有创建概念卡” | [[State Graph Runtime]], [[Provider-first Agent SDK]], [[Crew Orchestration]], [[Role-playing Agent]], [[Data-first Agent Framework]], [[Type-safe Agent SDK]], [[Frontend-first AI Toolkit]], [[Agent Control Plane]] | 已创建 8 张 framework 选型边界概念卡，并回链 [[Agent Framework 全量选型对比 2026-05]] |
| 2026-05-12 | done | “补充 RAG 主题页，沉淀学习路线、组件边界、类型入口和诊断路径” | [[RAG 主题]], [[Knowledge Graph]] | 已补充 RAG 主题导航、pipeline、失败诊断、证据锚点和复习触发，并创建 [[Knowledge Graph]] 概念卡 |
| 2026-05-12 | done | “RAG and LLM boundary backlog：补齐 RAG 可靠性治理、检索决策、GraphRAG 构图评估和 LLM 输入输出基础边界” | [[RAG Citation Faithfulness]], [[RAG Access Control]], [[Query Rewrite]], [[Query Planning]], [[Graph Construction Evaluation]], [[Entity Resolution]], [[Token]], [[Context Window]], [[Prompt]], [[Hallucination]], [[RAG 可靠性与治理对比]], [[Query Rewrite Query Planning Agentic Retrieval 对比]], [[GraphRAG 构图与评估对比]], [[LLM 输入输出基础边界对比]] | 已创建 10 张概念卡和 4 张对比 topic，并写回 RAG / LLM / Agent 导航 |
| 2026-05-13 | done | “一个真实的 LangGraph 向实战项目是什么样子，需要解决什么方案，涉及什么技术？” | [[LangGraph 生产项目蓝图]], [[LangGraph]], [[Agent Workflow]], [[Agent State]], [[Durable Execution]], [[Human-in-the-loop]], [[Trace]], [[Evaluation]], [[Agent Framework 全量选型对比 2026-05]] | 已沉淀为 [[LangGraph 生产项目蓝图]]：多源检索 + 工具执行 + 审批 + checkpoint/resume + trace/eval + 部署治理 |
| 2026-05-13 | done | “Claw Bot / OpenClaw 与 Hermes 的边界是什么？” | [[OpenClaw Repo]], [[OpenClaw Repo vs Hermes Agent]], [[03 前沿追踪]], [[Agent Harness]], [[Coding Agent 执行边界对比]] | 已创建 OpenClaw official repo source note 和 OpenClaw / Hermes 对比 topic；边界：按 OpenClaw / Clawbot legacy alias 处理为 volatile 具体 Agent gateway / personal assistant harness source，不建 “Claw Bot” 稳定概念卡 |
| 2026-05-15 | done | “向量数据库 Qdrant / pgvector / Chroma / FAISS / Milvus / Weaviate / Pinecone 等 Agent 开发选型边界是什么？” | [[Vector Database]], [[Retrieval 组件对比]], [[RAG 主题]], [[Context RAG Memory 对比]] | 已写回 [[Vector Database#Agent / RAG 选型边界]]、[[Retrieval 组件对比#什么时候用哪个判断]]、[[RAG 主题#组件入口]]、[[Context RAG Memory 对比#什么时候用哪个判断]]；结论：记录为类别级选型边界，不为每个 vendor 直接建稳定概念卡。 |
| 2026-05-15 | done | “Top-K 是什么 / 补概念卡” | [[Top-K]], [[01 术语表]], [[RAG 主题]], [[Agent 知识地图]] | 已创建 [[Top-K]] 轻量概念卡，补 retrieval Top-K / decoding top-k 边界，并接入术语表、RAG 主题和 Agent 知识地图。 |
| 2026-05-17 | done | “错误 Skill 能否靠 Agent 反思发现？” | [[Tool Poisoning]], [[Tool Registry]], [[Agent Harness]], [[Evaluation]], [[Agent 安全控制点对比]], [[Agent Skills]] | 已写回 skill selection / skill trust 边界：`SKILL.md` / skill metadata 是会影响发现、选择和信任的 operational text；reflection 只能辅助怀疑，不等于 verification。当时未建弱卡；2026-05-20 已在官方 docs + paper evidence 支撑下创建 [[Agent Skills]]。 |
| 2026-05-17 | done | “Query enhancement / HyDE / MQE 与 Abstract Folder taxonomy 边界” | [[Query Rewrite]], [[Multi-Query Retrieval]], `scripts/interview_question_concept_aliases.json` | 已补 [[Multi-Query Retrieval]] 的 `MQE` / `Multi-Query Expansion` / `多查询扩展` aliases，并同步面试题 alias map；[[Query Rewrite]] 写明“查询增强策略 / 查询优化”是策略群边界，不是 Query Rewrite 的 alias；保留既有 `Multi-Query Retrieval up [[Query Rewrite]]`，不新建 HyDE 或查询增强策略弱卡。 |
| 2026-05-17 | done | “检索侧 Query Rewrite / Multi-Query / HyDE / Step-back / Query Planning / Agentic Retrieval 如何成组学习？” | [[HyDE]], [[Step-back Prompting]], [[Query Rewrite Query Planning Agentic Retrieval 对比]], [[RAG 主题]], `scripts/interview_question_concept_aliases.json` | 已创建 [[HyDE]] 与 [[Step-back Prompting]]，升级对比 topic 覆盖 6 个概念，并同步 alias map、raw evidence 回链、RAG 导航、概念候选 backlog 和 log；旧 folded 决策已重开为 done。 |
| 2026-05-17 | done | “Codex CLI / Claude Code 客户端为什么不显式用传统 RAG？” | [[Coding Agent 为什么不用传统 RAG]], [[Repo Context]], [[Context RAG Memory 对比]] | 已创建小型 topic 页：把结论写成 repo context gathering vs traditional document RAG 的边界；不新建弱概念卡，不修改 alias map。 |
| 2026-05-17 | done | “LLM 的上下文受什么限制，未来突破需要什么因素？” | [[LLM 上下文限制与突破条件]], [[Context Window]], [[Context Engineering]] | 已创建小型 topic 页：把上下文限制拆成容量、计算、结构、有效使用和治理五层；结论是长上下文突破需要模型、推理系统和外部上下文工程共同进步。 |
| 2026-05-17 | done | “KV Cache 在 LLM 推理中解决什么问题，相关论文如何定位 MQA / GQA / PagedAttention / FlashAttention？” | [[KV Cache]], [[LLM 上下文限制与突破条件]], [[资料收集索引]] | 已创建 [[KV Cache]] 概念卡和 4 篇 paper source note；边界：MQA/GQA 是 attention 结构层减少 K/V 份数，PagedAttention 是 KV cache 内存管理，FlashAttention 是 attention IO 实现优化，不把它们强行建成弱概念卡。 |
| 2026-05-18 | done | “Agent 鲁棒性 / Agent Robustness 的边界是什么？” | [[Agent Robustness]], [[Task Success Rate]], [[Evaluation]], [[Evaluation 层次对比]], `scripts/interview_question_concept_aliases.json` | 已创建 [[Agent Robustness]] 概念卡；边界写明它是扰动条件下的系统级稳定性和恢复能力，不等于通用可靠性、安全性、evaluation 或 task success rate，也不把裸 `鲁棒性 / Robustness` 自动当 alias。 |
| 2026-05-19 | pending | “为什么在 Agent 出来之前，RAG 概念并没有明显进入市场和日常生活？” | [[RAG]], [[Agentic RAG]], [[RAG 主题]] | 待写回：校正“RAG 没应用”的前提；RAG 在 Agent 前已用于企业搜索、知识库问答和文档检索，但它更像后台信息管道。Agent 把 RAG 接到目标、工具、状态、workflow、评估和行动闭环里，才让普通用户感知为可交付的 AI 产品能力。 |
| 2026-05-20 | done | “近期值得学习的 AI / Agent 概念应录入哪些边界？” | [[Agent Skills]], [[Managed Agent Harness]], [[MCP Elicitation]], [[Agent Payments Protocol]], [[03 前沿追踪]] | 已录入 4 张概念卡和 3 份 official/source note；边界：优先沉淀能力包、托管运行外壳、MCP 结构化用户输入和 Agent 支付授权协议，不把产品 API、beta header 或前沿论文标题写成稳定概念。 |

## 写回模板

```md
| YYYY-MM-DD | pending | 问题 | `目标页面` | 处理动作 |
```


## 概念对比候选队列

准入规则见 [[LLM Wiki 工作流#概念对比 / 类比 topic 页写法]]。候选只代表“值得排查 / 可能值得写”，不是自动新建页面；执行前仍要确认每个概念有足够证据锚点。

| 优先级 | 状态 | 候选概念组 | 为什么值得对比 | 下一步 |
|---|---|---|---|---|
| P1 | done | [[ReAct]] / [[Plan-and-Solve Prompting]] / [[Reflexion]] | 都改善复杂任务可靠性，但分别介入行动前、行动中、行动后；混淆风险高且 paper source note 充分 | 已写入 [[ReAct Plan-and-Solve Reflexion 对比]] |
| P1 | done | [[Agent Framework]] / [[Agent Harness]] / [[Agent Workflow]] / [[Agent State]] / [[Agent Loop]] | 都描述 Agent 工程承载层，但边界分别是框架、运行支架、流程图/步骤、状态数据和循环机制 | 已写入 [[Agent 工程分层对比]] |
| P1 | done | [[Tool Use]] / [[Tool Calling]] / [[Tool Registry]] / [[Tool Permissioning]] / [[MCP]] / [[MCP Registry]] | 都和工具有关，但分别是能力范畴、结构化调用契约、工具发现/注册、权限边界和协议生态 | 已写入 [[Tool 接口层对比]] |
| P1 | done | [[Prompt Injection]] / [[Indirect Prompt Injection]] / [[Tool Poisoning]] / [[Data Exfiltration]] / [[Guardrails]] / [[Policy Engine]] / [[Approval Gate]] / [[Least Privilege Tools]] | 都是 Agent 安全控制点，但攻击入口、传播路径、策略判断、人类批准和最小权限边界不同 | 已写入 [[Agent 安全控制点对比]] |
| P2 | done | [[Memory]] / [[Agent State]] / [[Long-term Memory]] / [[Episodic Memory]] / [[Semantic Memory]] / [[Memory Reflection]] / [[Parametric Memory]] / [[Non-Parametric Memory]] | 都是 Agent memory 线索，但分别是运行态、长期保存、事实/语义、事件经验、反思生成和模型内外知识来源 | 已写入 [[Agent Memory 类型对比]] |
| P2 | done | [[Evaluation]] / [[Benchmark]] / [[Eval Harness]] / [[LLM-as-Judge]] / [[Task Success Rate]] / [[RAG Evaluation]] / [[Trajectory Evaluation]] | 都和“判断系统是否有效”有关，但分别位于指标、数据集、运行支架、judge 方法和任务/轨迹/RAG 层 | 已写入 [[Evaluation 层次对比]] |
| P2 | done | [[Observability]] / [[Trace]] / [[Audit Log]] / [[Replay]] / [[OpenTelemetry GenAI]] | 都记录系统行为，但分别服务实时可观测、结构化执行记录、审计责任、复现调试和标准化 telemetry | 已写入 [[Observability Audit 对比]] |
| P2 | done | [[Browser Agent]] / [[Computer Use]] / [[GUI Grounding]] / [[Observation]] / [[Sandbox Workspace]] / [[Code Execution Sandbox]] / [[Tool Permissioning]] | 都在 GUI / computer-use 执行栈上相邻，但感知、行动、反馈、隔离和权限控制边界不同 | 已写入 [[Browser Computer Use 执行栈对比]] |
| P2 | done | [[Context Engineering]] / [[RAG]] / [[Memory]] / [[Repo Context]] / [[Retriever]] / [[Chunking]] / [[Embedding]] | 都在给模型提供上下文，但分别负责上下文设计、外部检索、跨轮保留、代码仓库投影和检索组件 | 已写入 [[Context RAG Memory 对比]] |
| P2 | done | [[Retriever]] / [[Hybrid Search]] / [[Reranking]] / [[Vector Database]] / [[Embedding]] / [[Document Ingestion]] | 都是 retrieval pipeline 组件，但分别对应资料入库、向量表示、候选召回、多路召回和排序校正 | 已写入 [[Retrieval 组件对比]] |
| P2 | done | [[Multi-agent Orchestration]] / [[Handoff]] / [[A2A]] / [[ACP]] / [[MCP]] / [[Agent Workflow]] / [[Durable Execution]] | 都处理 Agent 协作或跨边界连接，但 workflow、handoff、agent-to-agent 协议、tool/resource 协议和持久执行不是同一层 | 已写入 [[Multi-agent Handoff Protocol 对比]] |
| P2 | done | [[Coding Agent]] / [[Repo Context]] / [[Patch Validation]] / [[Sandbox Workspace]] / [[Code Execution Sandbox]] / [[AGENTS.md]] | 都在代码 Agent 执行边界附近，但分别是行动主体、上下文、补丁验证、工作区隔离、代码执行隔离和人类规则入口 | 已写入 [[Coding Agent 执行边界对比]] |
| P2 | existing | [[Trajectory]] / [[Trace]] / [[Reasoning Trace]] / [[Trajectory Evaluation]] / [[Replay]] | 已有高价值边界页，说明 trajectory、trace 和 reasoning trace 的层级差异 | 见 [[Trajectory Trace 类型对比]]；后续只做维护 |
| P2 | existing | [[RAG]] / [[Agentic RAG]] / [[Corrective RAG]] / [[Self-RAG]] | 已有 RAG 类型比较入口，适合继续补 evidence / modernity | 见 [[RAG 类型对比]]；后续只做维护 |
| P3 | done | [[Transformer]] / [[Self-Attention]] / [[Multi-Head Attention]] / [[Positional Encoding]] | 都是 LLM 架构地基，容易把架构、机制和位置编码混成同一层 | 已写入 [[LLM 基础结构对比]] |
| P3 | pending | [[LLM]] / [[LLM Training Pipeline]] / [[Zero-shot CoT]] / [[Plan-and-Solve Prompting]] | 都和 LLM 能力来源有关，但训练流程、模型能力、prompt-time reasoning pattern 证据层级不同 | **分流：只留 backlog / 证据补齐后再评估**。先补训练主源、Zero-shot CoT 与 Plan-and-Solve paper 证据边界；证据不足前不强行创建“能力来源对比页”。 |
| P3 | pending | [[Oh My Codex (OMX)]] / [[Hermes Agent]] / [[LangChain DeepAgents]] / [[Agent Framework]] | 都是具体 runtime / 产品 / framework 生态，变化快且容易把产品能力误当通用 Agent 定义 | **分流：需查新后再写**。只在官方文档 / repo / release 边界更新后再决定是维护已有页，还是新建 runtime 产品生态对比；不得把单一产品能力升格为通用 [[Agent Framework]] 定义。 |
| P3 | done | [[LangGraph]] / OpenAI Agents SDK / [[Microsoft Agent Framework]] / [[AutoGen]] / CrewAI / LlamaIndex / Pydantic AI / Agno / Mastra / Vercel AI SDK / Google ADK / [[AgentScope]] / [[CAMEL]] | 都是热门 Agent framework / SDK / toolkit，但分别位于 state graph、provider SDK、enterprise workflow、conversation team、crew/flow、data/RAG、typed Python、platform stack、TS workflow、frontend toolkit、Google Cloud ADK、message platform、role-playing society 等不同层 | 旧范式页见 [[Agent Framework 编排范式对比]]；全量选型已写入 [[Agent Framework 全量选型对比 2026-05]] |

## 2026-05-17 剩余候选分流

这次分流只处理“当前仍是 pending 的概念对比候选”，不新建概念卡、不改 canonical name / alias，也不改面试题 alias map。

| 分流 | 项目 | 结论 | 边界 |
|---|---|---|---|
| 现在就能成页 | 无 | 当前没有新的高证据对比页可直接创建。 | P1 / P2 的高价值候选已经是 `done` 或 `existing`；为了减少弱页，不用“填空式”新建 topic。 |
| 证据补齐后再评估 | [[LLM]] / [[LLM Training Pipeline]] / [[Zero-shot CoT]] / [[Plan-and-Solve Prompting]] | 保留为 P3 backlog。 | 这组混淆点真实存在，但“训练流程如何形成能力”和“prompt-time reasoning pattern 如何调用能力”证据层不同；补训练主源和 prompting paper 证据前不强行成页。 |
| 查新后再写 | [[Oh My Codex (OMX)]] / [[Hermes Agent]] / [[LangChain DeepAgents]] / [[Agent Framework]] | 保留为 P3 freshness-check。 | 它们是具体 runtime / 产品 / framework 生态，变化快；下一步应先查官方文档、repo 或 release，再决定维护已有页还是创建产品生态对比。 |
| 只留 backlog，不成页 | 当前无永久搁置项 | 两个 pending 项都仍有学习价值，只是未达到直接成页条件。 | 若后续查新或精读后仍证据不足，再降级到 [[02 问题池]] 或继续留本页，不创建弱 topic。 |
