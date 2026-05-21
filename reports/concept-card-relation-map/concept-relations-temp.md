# Temporary Concept Relationship Map

Generated: `2026-05-21T09:47:24Z`

> 临时文件：用于后续概念层级开发评估。不要把候选边自动写回概念卡；每条 candidate 都需要单独人工/LLM 复核。

## Summary

- total_concepts: 154
- edge_counts: {'related_link': 918, 'body_link': 274, 'typed_relation': 57, 'taxonomy': 39}
- typed_relation_counts: {'contrasts_with': 8, 'related_to': 15, 'representative_of': 2, 'based_on_intuition': 1, 'paired_with': 2, 'mechanism_for': 1, 'projects_from': 1, 'draws_from': 2, 'risk_for': 1, 'concrete-harness-for': 1, 'built-on': 1, 'composes_with': 8, 'uses': 4, 'pattern_for': 1, 'specializes': 1, 'mitigates': 1, 'concrete-platform-for': 1, 'adjacent-to': 1, 'used_by': 1, 'precedes': 1, 'composed_into': 2, 'foundational_for': 1}
- concepts_without_up: 115
- core_orphans: 0
- weakly_connected_concepts: 1
- dangling_core_targets: 31
- candidate_edges: 79
- taxonomy_candidates: 11
- topic_family_review_signals: 68

## Existing taxonomy edges (`up`)

| Source | relation | Target | Evidence | Note |
|---|---|---|---|---|
| [[Agent Evaluation Benchmark]] | up | [[Benchmark]] | frontmatter.up |  |
| [[AgentScope]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[Agentic RAG]] | up | [[RAG]] | frontmatter.up |  |
| [[Agentic Retrieval]] | up | [[Retriever]] | frontmatter.up |  |
| [[Audit Log]] | up | [[Observability]] | frontmatter.up |  |
| [[AutoGen]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[BFCL]] | up | [[Agent Evaluation Benchmark]] | frontmatter.up |  |
| [[BM25]] | up | [[Sparse Retrieval]] | frontmatter.up |  |
| [[CAMEL]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[Computer Use]] | up | [[Tool Use]] | frontmatter.up |  |
| [[Context Precision]] | up | [[RAG Evaluation]] | frontmatter.up |  |
| [[Context Recall]] | up | [[RAG Evaluation]] | frontmatter.up |  |
| [[Corrective RAG]] | up | [[RAG]] | frontmatter.up |  |
| [[Crew Orchestration]] | up | [[Agent Workflow]] | frontmatter.up |  |
| [[Cross-Encoder]] | up | [[Reranking]] | frontmatter.up |  |
| [[Data-first Agent Framework]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[Dense Retrieval]] | up | [[Retriever]] | frontmatter.up |  |
| [[Episodic Memory]] | up | [[Memory]] | frontmatter.up |  |
| [[Graph Construction Evaluation]] | up | [[Evaluation]] | frontmatter.up |  |
| [[GraphRAG]] | up | [[RAG]] | frontmatter.up |  |
| [[Hybrid Search]] | up | [[Retriever]] | frontmatter.up |  |
| [[LangChain DeepAgents]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[LangGraph]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[Long-term Memory]] | up | [[Memory]] | frontmatter.up |  |
| [[Memory Reflection]] | up | [[Memory]] | frontmatter.up |  |
| [[Microsoft Agent Framework]] | up | [[Agent Framework]] | frontmatter.up |  |
| [[Multi-Query Retrieval]] | up | [[Query Rewrite]] | frontmatter.up |  |
| [[Multi-Route Retrieval]] | up | [[Retriever]] | frontmatter.up |  |
| [[Multi-agent Orchestration]] | up | [[Agent Workflow]] | frontmatter.up |  |
| [[Non-Parametric Memory]] | up | [[Memory]] | frontmatter.up |  |
| [[Parametric Memory]] | up | [[Memory]] | frontmatter.up |  |
| [[Parent-Child Chunking]] | up | [[Chunking]] | frontmatter.up |  |
| [[RAG Evaluation]] | up | [[Evaluation]] | frontmatter.up |  |
| [[Reciprocal Rank Fusion]] | up | [[Multi-Route Retrieval]] | frontmatter.up |  |
| [[Self-RAG]] | up | [[RAG]] | frontmatter.up |  |
| [[Semantic Memory]] | up | [[Memory]] | frontmatter.up |  |
| [[Sparse Retrieval]] | up | [[Retriever]] | frontmatter.up |  |
| [[Tool Calling]] | up | [[Tool Use]] | frontmatter.up |  |
| [[Trajectory Evaluation]] | up | [[Evaluation]] | frontmatter.up |  |

## Existing typed relations

| Source | relation | Target | Evidence | Note |
|---|---|---|---|---|
| [[ANP]] | contrasts_with | [[A2A]] | frontmatter.relations | A2A 更聚焦 Agent-to-Agent 任务协作和状态/消息/artifact；ANP 更强调 Agent 网络身份、发现、描述和通信协商。 |
| [[ANP]] | contrasts_with | [[MCP]] | frontmatter.relations | MCP 连接 AI 应用与工具/资源/context server；ANP 连接网络中的 Agent 身份和通信入口。 |
| [[ANP]] | related_to | [[MCP Registry]] | frontmatter.relations | 两者都涉及发现与生态分发，但 MCP Registry 面向 MCP server；ANP discovery 面向 Agent identity/description。 |
| [[Agent Robustness]] | related_to | [[Guardrails]] | frontmatter.relations | Guardrails 可以提高部分扰动下的可控性，但安全拦截机制不等于鲁棒性指标。 |
| [[Agent Robustness]] | related_to | [[Task Success Rate]] | frontmatter.relations | Agent Robustness 常用扰动条件下的成功率下降幅度来观察；Task Success Rate 是被观察指标，不是鲁棒性本身。 |
| [[Agent Robustness]] | related_to | [[Trajectory Evaluation]] | frontmatter.relations | 工具超时、异常返回、噪声输入和恢复动作都需要看 trajectory，而不只看最终输出。 |
| [[BFCL]] | representative_of | [[Agent Evaluation Benchmark]] | frontmatter.relations | BFCL 是工具/function calling 方向的代表性 Agent evaluation benchmark；代表关系不等于 AST、state check 或 harness 组件本身。 |
| [[BM25]] | based_on_intuition | [[TF-IDF]] | frontmatter.relations | BM25 延续 TF-IDF 的词项权重直觉，但加入长度归一化和饱和控制。 |
| [[BM25]] | related_to | [[Hybrid Search]] | frontmatter.relations | Hybrid Search 常把 BM25 作为 sparse route 或关键词侧候选。 |
| [[BM25]] | representative_of | [[Sparse Retrieval]] | frontmatter.relations | BM25 是 sparse retrieval 的常见代表算法。 |
| [[Context Precision]] | paired_with | [[Context Recall]] | frontmatter.relations | Context Precision 看检索上下文的相关性和排序质量；Context Recall 看必要信息是否被覆盖。 |
| [[Context Projection]] | draws_from | [[Memory]] | frontmatter.relations | 记忆只有被选中并投影进上下文时才影响本轮回答。 |
| [[Context Projection]] | draws_from | [[Trace]] | frontmatter.relations | trace 可作为失败复盘、长任务继续或审计解释时的候选材料。 |
| [[Context Projection]] | mechanism_for | [[Context Engineering]] | frontmatter.relations | 把系统持有的信息投影成模型本轮可见、可用、可预算的上下文。 |
| [[Context Projection]] | projects_from | [[Agent State]] | frontmatter.relations | 从当前 run 的状态中选择、压缩、排序本轮决策需要的片段。 |
| [[Context Recall]] | paired_with | [[Context Precision]] | frontmatter.relations | Context Recall 看该找的信息有没有覆盖；Context Precision 看找回内容里相关信息是否靠前、噪音是否过多。 |
| [[Context Rot]] | contrasts_with | [[Context Window]] | frontmatter.relations | Context Window 是容量边界；Context Rot 是长输入中有效使用质量下降的风险。 |
| [[Context Rot]] | related_to | [[Long-Horizon Context Engineering]] | frontmatter.relations | 长任务直接累积历史、工具结果和中间产物时，context rot 是核心风险之一。 |
| [[Context Rot]] | risk_for | [[Context Engineering]] | frontmatter.relations | 上下文工程需要通过选择、结构化、去噪和压缩来降低 context rot。 |
| [[Cross-Encoder]] | contrasts_with | [[Dense Retrieval]] | frontmatter.relations | Dense Retrieval 常用双塔/bi-encoder 思路快速召回；Cross-Encoder 把 query 和 chunk 放在一起深度判断，适合小候选集精排。 |
| [[DeerFlow]] | built-on | [[LangGraph]] | frontmatter.relations |  |
| [[DeerFlow]] | concrete-harness-for | [[Agent Harness]] | frontmatter.relations |  |
| [[Dense Retrieval]] | composes_with | [[Hybrid Search]] | frontmatter.relations | Hybrid Search 常把 dense retrieval 和 sparse/BM25 route 组合起来互补。 |
| [[Dense Retrieval]] | contrasts_with | [[Cross-Encoder]] | frontmatter.relations | Bi-encoder / Dense Retrieval 把 query 和 chunk 分开编码，适合快速召回；Cross-Encoder 把二者放在一起判断，适合小候选集精排。 |
| [[Dense Retrieval]] | contrasts_with | [[Sparse Retrieval]] | frontmatter.relations | Dense Retrieval 用稠密语义向量找相似内容；Sparse Retrieval / BM25 用词项、倒排和词面信号找精确匹配。 |
| [[Dense Retrieval]] | uses | [[Embedding]] | frontmatter.relations | Dense Retrieval 依赖文档和 query 的 embedding 表示。 |
| [[GSSC Pipeline]] | composes_with | [[Progressive Disclosure]] | frontmatter.relations | 两者都服务按需控制上下文；GSSC 是构建流水线，Progressive Disclosure 是信息暴露策略。 |
| [[GSSC Pipeline]] | pattern_for | [[Context Engineering]] | frontmatter.relations | 把上下文构建拆成 gather、select、structure、compress 四个工程阶段。 |
| [[Hybrid Search]] | composes_with | [[Dense Retrieval]] | frontmatter.relations | Hybrid Search 通常把 dense retrieval 作为另一条语义召回。 |
| [[Hybrid Search]] | composes_with | [[Sparse Retrieval]] | frontmatter.relations | Hybrid Search 通常把 sparse retrieval / BM25 作为一路候选。 |
| [[Hybrid Search]] | related_to | [[Multi-Route Retrieval]] | frontmatter.relations | Hybrid Search 是多路召回最常见的双路形态，但多路召回更宽。 |
| [[Long-Horizon Context Engineering]] | specializes | [[Context Engineering]] | frontmatter.relations | 把上下文选择、压缩、外部化和隔离用于超出单窗口的长任务。 |
| [[Long-Horizon Context Engineering]] | uses | [[Agent State]] | frontmatter.relations | 当前 run 的阶段、待办、错误和下一步依据需要结构化保存。 |
| [[Long-Horizon Context Engineering]] | uses | [[Memory]] | frontmatter.relations | 结构化笔记是跨上下文窗口持久化关键事实的一种 memory 形态。 |
| [[Multi-Query Retrieval]] | composes_with | [[Multi-Route Retrieval]] | frontmatter.relations | Multi-Query Retrieval 可以作为多路召回中的 query route，用多个问题变体扩大覆盖。 |
| [[Multi-Query Retrieval]] | contrasts_with | [[Query Planning]] | frontmatter.relations | Multi-query 是生成多个检索 query；query planning 更强调任务/子问题/知识源的规划。 |
| [[Multi-Route Retrieval]] | composes_with | [[Hybrid Search]] | frontmatter.relations | Hybrid Search 通常是多路召回的一种常见两路形态，但多路召回还可以包括多 Query、图检索、metadata filter、不同索引粒度或多 retriever。 |
| [[Multi-Route Retrieval]] | composes_with | [[Reranking]] | frontmatter.relations | 多路结果通常先融合成候选集合，再交给 reranker 精排；reranking 不是召回路线本身。 |
| [[Multi-Route Retrieval]] | composes_with | [[Sparse Retrieval]] | frontmatter.relations | 多路召回常把 sparse retrieval / BM25 作为精确词面一路。 |
| [[Parent-Child Chunking]] | mitigates | [[Context Precision]] | frontmatter.relations | 子 chunk 帮助精确检索，父 chunk 帮助保留上下文；但是否改善 precision/recall 仍需评估。 |
| [[Parent-Child Chunking]] | uses | [[Retriever]] | frontmatter.relations | 检索时用子 chunk 精准定位，命中后回取父 chunk 给 LLM 阅读。 |
| [[RAGFlow]] | adjacent-to | [[Data-first Agent Framework]] | frontmatter.relations |  |
| [[RAGFlow]] | concrete-platform-for | [[RAG]] | frontmatter.relations |  |
| [[RAGGraph]] | contrasts_with | [[GraphRAG]] | frontmatter.relations | GraphRAG 是图结构参与检索和上下文构造；RAGGraph 更可能指 RAG 执行流程图或项目名，二者不能互当别名。 |
| [[RAGGraph]] | related_to | [[Agentic RAG]] | frontmatter.relations | 若 RAGGraph 指带分支和循环的检索工作流，它更接近 Agentic RAG / workflow graph 的实现语境，而不是独立稳定方法族。 |
| [[RAGGraph]] | related_to | [[RAG]] | frontmatter.relations | RAGGraph 讨论的是 RAG pipeline 可能被图式编排，但这个命名不稳定；当前不把它写成 RAG 的 strict taxonomy 子类。 |
| [[ReWOO]] | related_to | [[Observation]] | frontmatter.relations | ReWOO 的核心边界就是限制 observation 对 planner reasoning 的中途回流。 |
| [[ReWOO]] | related_to | [[Plan-and-Solve Prompting]] | frontmatter.relations | ReWOO 保留先计划再求解的直觉，但加入 Worker 工具取证；不是纯 prompt-level plan-solve。 |
| [[ReWOO]] | related_to | [[ReAct]] | frontmatter.relations | ReWOO 与 ReAct 都面向工具增强推理，但 ReAct 让 Observation 反馈驱动下一步，ReWOO 先规划 evidence slots 后取证。 |
| [[Reciprocal Rank Fusion]] | precedes | [[Reranking]] | frontmatter.relations | RRF 是候选融合/粗排；reranking 是融合后对较小候选集做精排。 |
| [[Reciprocal Rank Fusion]] | used_by | [[Hybrid Search]] | frontmatter.relations | Hybrid Search 常用 RRF 把 dense/vector 与 sparse/BM25 两路排序融合。 |
| [[Sparse Retrieval]] | composed_into | [[Hybrid Search]] | frontmatter.relations | Sparse Retrieval 常被组合进 Hybrid Search 作为词面检索一路。 |
| [[Sparse Retrieval]] | composed_into | [[Multi-Route Retrieval]] | frontmatter.relations | Sparse Retrieval 可以作为多路召回中的词面检索一路；这是 route/strategy 组合关系，不是 `up`。 |
| [[Sparse Retrieval]] | related_to | [[BM25]] | frontmatter.relations | BM25 是 sparse retrieval 的常见代表；这张卡覆盖更宽的词法检索家族。 |
| [[Sparse Retrieval]] | related_to | [[Dense Retrieval]] | frontmatter.relations | Sparse Retrieval 关注词项、倒排和精确匹配；Dense Retrieval 关注语义相似。 |
| [[TF-IDF]] | foundational_for | [[Sparse Retrieval]] | frontmatter.relations | TF-IDF 提供稀疏词项权重的基础直觉；Sparse Retrieval 是更大的检索家族。 |
| [[TF-IDF]] | related_to | [[Multi-Route Retrieval]] | frontmatter.relations | 多路召回可能通过 sparse retrieval / BM25 路线间接受益于 TF-IDF-style 词项权重；TF-IDF 本身不是召回路线或多路召回策略。 |

## Candidate edges for review

Candidate type boundary: `taxonomy_candidate` is a possible `up` edge for human review; `topic_family_review` is only a batching / neighborhood signal and must not be bulk-written into `up`.

Retrieval boundary: representation/feature concepts such as TF-IDF, route families such as Sparse Retrieval, and orchestration strategies such as Multi-Route Retrieval live on different semantic layers. A feature or route may support a strategy through `relations`, but that does not make it a taxonomy child for `up`.

| Source | Candidate target | Candidate type | Confidence | Support | Rationale |
|---|---|---|---|---|---|
| [[OpenTelemetry GenAI]] | [[Observability]] | taxonomy_candidate | medium | frontmatter.related | trace/observability title family |
| [[RAGGraph]] | [[RAG]] | taxonomy_candidate | medium | frontmatter.related, relations:related_to | RAG method/title family |
| [[State Graph Runtime]] | [[Agent Workflow]] | taxonomy_candidate | medium | frontmatter.related | workflow/runtime title family |
| [[Top-K]] | [[Retriever]] | taxonomy_candidate | medium | frontmatter.related | retrieval/search title family |
| [[Agent Control Plane]] | [[Observability]] | topic_family_review | low | frontmatter.related | topic family: observability |
| [[Agent Framework]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[Agent Harness]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Agent Lifecycle Hook]] | [[Observability]] | topic_family_review | low | frontmatter.related | topic family: observability |
| [[Agent Loop]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[Agent Robustness]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Agent State]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[Agent State]] | [[Memory]] | topic_family_review | low | frontmatter.related | topic family: memory |
| [[Agent Workflow Static Verification]] | [[Agent Framework]] | topic_family_review | low | frontmatter.related | topic family: framework |
| [[Agent Workflow Static Verification]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[Benchmark]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Chunking]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Context Engineering]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Context Projection]] | [[Memory]] | topic_family_review | low | frontmatter.related, relations:draws_from | topic family: memory |
| [[DeerFlow]] | [[Agent Framework]] | topic_family_review | low | frontmatter.related | topic family: framework |
| [[Document Ingestion]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Durable Execution]] | [[Agent Workflow]] | taxonomy_candidate | low | title/topic heuristic | workflow/runtime title family |
| [[Embedding]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Eval Harness]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Frontend-first AI Toolkit]] | [[Agent Framework]] | topic_family_review | low | frontmatter.related | topic family: framework |
| [[Guardrails]] | [[Evaluation]] | topic_family_review | low | body wikilink | topic family: evaluation |
| [[Hallucination]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Handoff]] | [[Agent Workflow]] | taxonomy_candidate | low | title/topic heuristic | workflow/runtime title family |
| [[Hermes Agent]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[Human-in-the-loop]] | [[Agent Workflow]] | taxonomy_candidate | low | title/topic heuristic | workflow/runtime title family |
| [[HyDE]] | [[Retriever]] | topic_family_review | low | frontmatter.related | topic family: retrieval/search |
| [[Indirect Prompt Injection]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Knowledge Graph]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[LLM Gateway]] | [[Observability]] | topic_family_review | low | frontmatter.related | topic family: observability |
| [[LLM Training Pipeline]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[LLM-as-Judge]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Long-Horizon Context Engineering]] | [[Memory]] | topic_family_review | low | frontmatter.related, relations:uses | topic family: memory |
| [[Neo4j]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[OMX $ 指令]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[Observability]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[OpenTelemetry GenAI]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[OpenTelemetry GenAI]] | [[Observability]] | topic_family_review | low | frontmatter.related | topic family: observability |
| [[Patch Validation]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Plan-and-Solve Prompting]] | [[Planning]] | topic_family_review | low | frontmatter.related | topic family: planning |
| [[Progressive Disclosure]] | [[Tool Use]] | topic_family_review | low | body wikilink | topic family: tool-use/tools |
| [[Prompt Engineering]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Provider-first Agent SDK]] | [[Agent Framework]] | topic_family_review | low | frontmatter.related | topic family: framework |
| [[Query Planning]] | [[Retriever]] | topic_family_review | low | frontmatter.related | topic family: retrieval/search |
| [[Query Rewrite]] | [[Retriever]] | topic_family_review | low | frontmatter.related | topic family: retrieval/search |
| [[RAG Access Control]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[RAG Citation Faithfulness]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[RAGFlow]] | [[Agent Framework]] | topic_family_review | low | body wikilink | topic family: framework |
| [[RAGFlow]] | [[RAG]] | topic_family_review | low | frontmatter.related, relations:concrete-platform-for | topic family: rag |
| [[RAGGraph]] | [[RAG]] | topic_family_review | low | frontmatter.related, relations:related_to | topic family: rag |
| [[Reasoning Trace]] | [[Observability]] | taxonomy_candidate | low | title/topic heuristic | trace/observability title family |
| [[Reflexion]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Replay]] | [[Evaluation]] | topic_family_review | low | body wikilink | topic family: evaluation |
| [[Replay]] | [[Observability]] | topic_family_review | low | frontmatter.related | topic family: observability |
| [[Repo Context]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Reranking]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Reranking]] | [[Retriever]] | topic_family_review | low | frontmatter.related | topic family: retrieval/search |
| [[Retriever]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Role-playing Agent]] | [[Agent Framework]] | topic_family_review | low | frontmatter.related | topic family: framework |
| [[State Graph Runtime]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |
| [[TF-IDF]] | [[RAG]] | topic_family_review | low | body wikilink | topic family: rag |
| [[TF-IDF]] | [[Retriever]] | topic_family_review | low | frontmatter.related | topic family: retrieval/search |
| [[TTL]] | [[Memory]] | topic_family_review | low | frontmatter.related | topic family: memory |
| [[TTL]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Task Success Rate]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Tool Permissioning]] | [[Tool Use]] | taxonomy_candidate | low | title/topic heuristic | tool-use title family |
| [[Tool Poisoning]] | [[Tool Use]] | taxonomy_candidate | low | title/topic heuristic | tool-use title family |
| [[Tool Registry]] | [[Tool Use]] | taxonomy_candidate | low | title/topic heuristic | tool-use title family |
| [[Top-K]] | [[Retriever]] | topic_family_review | low | frontmatter.related | topic family: retrieval/search |
| [[Trace]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Trace]] | [[Observability]] | topic_family_review | low | frontmatter.related | topic family: observability |
| [[Type-safe Agent SDK]] | [[Agent Framework]] | topic_family_review | low | frontmatter.related | topic family: framework |
| [[Type-safe Agent SDK]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Vector Database]] | [[RAG]] | topic_family_review | low | frontmatter.related | topic family: rag |
| [[Win Rate]] | [[Evaluation]] | topic_family_review | low | frontmatter.related | topic family: evaluation |
| [[Workflow Guardrails]] | [[Agent Workflow]] | topic_family_review | low | frontmatter.related | topic family: workflow |

## Concepts without `up`

- [[A2A]]
- [[ACP]]
- [[AGENTS.md]]
- [[ANP]]
- [[Agent]]
- [[Agent Control Plane]]
- [[Agent Framework]]
- [[Agent Harness]]
- [[Agent Lifecycle Hook]]
- [[Agent Loop]]
- [[Agent Payments Protocol]]
- [[Agent Robustness]]
- [[Agent Skills]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Agent Workflow Static Verification]]
- [[Approval Gate]]
- [[Benchmark]]
- [[Browser Agent]]
- [[Chunking]]
- [[Code Execution Sandbox]]
- [[Coding Agent]]
- [[Context Engineering]]
- [[Context Projection]]
- [[Context Rot]]
- [[Context Window]]
- [[Data Exfiltration]]
- [[DeerFlow]]
- [[Document Ingestion]]
- [[Durable Execution]]
- [[Embedding]]
- [[Entity Resolution]]
- [[Eval Harness]]
- [[Evaluation]]
- [[Frontend-first AI Toolkit]]
- [[GSSC Pipeline]]
- [[GUI Grounding]]
- [[Guardrails]]
- [[Hallucination]]
- [[Handoff]]
- [[Hermes Agent]]
- [[Human-in-the-loop]]
- [[HyDE]]
- [[Indirect Prompt Injection]]
- [[KV Cache]]
- [[Knowledge Graph]]
- [[LLM]]
- [[LLM Gateway]]
- [[LLM Training Pipeline]]
- [[LLM-as-Judge]]
- [[Least Privilege Tools]]
- [[Long-Horizon Context Engineering]]
- [[MCP]]
- [[MCP Elicitation]]
- [[MCP Registry]]
- [[MCP Transport]]
- [[Managed Agent Harness]]
- [[Memory]]
- [[Multi-Head Attention]]
- [[NLP]]
- [[Neo4j]]
- [[OMX $ 指令]]
- [[Observability]]
- [[Observation]]
- [[Obsidian + LLM Wiki]]
- [[Oh My Codex (OMX)]]
- [[OpenTelemetry GenAI]]
- [[Patch Validation]]
- [[Plan-and-Solve Prompting]]
- [[Planning]]
- [[Policy Engine]]
- [[Positional Encoding]]
- [[Progressive Disclosure]]
- [[Prompt]]
- [[Prompt Engineering]]
- [[Prompt Injection]]
- [[Provider-first Agent SDK]]
- [[Query Planning]]
- [[Query Rewrite]]
- [[RAG]]
- [[RAG Access Control]]
- [[RAG Citation Faithfulness]]
- [[RAGFlow]]
- [[RAGGraph]]
- [[ReAct]]
- [[ReWOO]]
- [[Reasoning Trace]]
- [[Reflexion]]
- [[Replay]]
- [[Repo Context]]
- [[Reranking]]
- [[Retriever]]
- [[Role-playing Agent]]
- [[Sandbox Workspace]]
- [[Self-Attention]]
- [[State Graph Runtime]]
- [[Step-back Prompting]]
- [[TF-IDF]]
- [[TTL]]
- [[Task Success Rate]]
- [[Token]]
- [[Tool Permissioning]]
- [[Tool Poisoning]]
- [[Tool Registry]]
- [[Tool Use]]
- [[Top-K]]
- [[Trace]]
- [[Trajectory]]
- [[Transformer]]
- [[Type-safe Agent SDK]]
- [[Vector Database]]
- [[Win Rate]]
- [[Workflow Guardrails]]
- [[Zero-shot CoT]]
- [[双链]]

## Weakly connected concepts

- [[双链]]

## Dangling core targets

| Source | relation | Missing/external target | Kind |
|---|---|---|---|
| [[A2A]] | related | A2A MCP ANP 对比 | related_link |
| [[ACP]] | related | A2A MCP ANP 对比 | related_link |
| [[ANP]] | related | A2A MCP ANP 对比 | related_link |
| [[Agent Framework]] | related | Agent Framework 编排范式对比 | related_link |
| [[Agent Framework]] | related | Agent Framework 全量选型对比 2026-05 | related_link |
| [[AgentScope]] | related | Agent Framework 编排范式对比 | related_link |
| [[AutoGen]] | related | Agent Framework 编排范式对比 | related_link |
| [[BFCL]] | related | GAIA Benchmark | related_link |
| [[CAMEL]] | related | Agent Framework 编排范式对比 | related_link |
| [[Context Rot]] | related | LLM 上下文限制与突破条件 | related_link |
| [[GraphRAG]] | related | RAG 类型对比 | related_link |
| [[KV Cache]] | related | LLM 上下文限制与突破条件 | related_link |
| [[LangGraph]] | related | Agent Framework 编排范式对比 | related_link |
| [[MCP]] | related | A2A MCP ANP 对比 | related_link |
| [[Microsoft Agent Framework]] | related | Agent Framework 编排范式对比 | related_link |
| [[Observation]] | related | Environment Observation 类型对比 | related_link |
| [[Obsidian + LLM Wiki]] | related | index | related_link |
| [[Obsidian + LLM Wiki]] | related | 04 页面目录 | related_link |
| [[Obsidian + LLM Wiki]] | related | 05 Query 写回队列 | related_link |
| [[Obsidian + LLM Wiki]] | related | 06 Wiki 健康检查 | related_link |
| [[Plan-and-Solve Prompting]] | related | ReAct Plan-and-Solve Reflexion 对比 | related_link |
| [[ReAct]] | related | Environment Observation 类型对比 | related_link |
| [[ReAct]] | related | ReAct Plan-and-Solve Reflexion 对比 | related_link |
| [[ReWOO]] | related | ReAct Plan-and-Solve Reflexion 对比 | related_link |
| [[Reasoning Trace]] | related | Trajectory Trace 类型对比 | related_link |
| [[Reflexion]] | related | ReAct Plan-and-Solve Reflexion 对比 | related_link |
| [[Trace]] | related | Trajectory Trace 类型对比 | related_link |
| [[Trajectory]] | related | Trajectory Trace 类型对比 | related_link |
| [[Vector Database]] | related | 常用向量数据库对比 | related_link |
| [[双链]] | related | 字段规范 | related_link |
| [[双链]] | related | Agent 知识地图 | related_link |

## Recommended next stages

1. Run `decide.py` to create a per-candidate decision ledger before any writeback.
2. Run `writeback.py --dry-run` and inspect the planned `up` additions.
3. Apply only a small reviewed batch with `writeback.py --apply --limit N`; never bulk-apply `topic_family_review` signals.
4. For each accepted taxonomy edge, update only the child card `up`; explain non-taxonomy relationships in `relations` only when needed.
5. Keep `related` as ordinary adjacency; do not treat it as hierarchy.
6. If Breadcrumbs visualization later needs non-taxonomy edges, add mirror fields only after the relation type is stable.

## Validation commands

```bash
python3 scripts/concept_taxonomy/build.py
python3 scripts/concept_taxonomy/decide.py
python3 scripts/concept_taxonomy/writeback.py --dry-run
python3 scripts/concept_taxonomy/writeback.py --apply --limit 12
python3 scripts/concept_taxonomy/validate.py
git diff --check
```
