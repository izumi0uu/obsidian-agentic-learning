---
type: log
topic:
  - obsidian
  - llm-wiki
status: active
created: 2026-05-05
updated: 2026-05-07
source:
related:
  - "[[LLM Wiki 工作流]]"
  - "[[资料收集索引]]"
---

# log

## [2026-05-05] setup | Agent learning vault

- Created `raw/`, `wiki/`, `maps/`, `daily/`, and `templates/` workflow.
- Added initial concept cards for Agent, LLM, Agent Loop, Tool Calling, RAG, Memory, Planning, and Evaluation.
- Added first source collection and reading plan.

## [2026-05-05] workflow | LLM Wiki adaptation

- Added project-level `AGENTS.md`.
- Added [[LLM Wiki 工作流]].
- Defined Ingest, Query, and Lint operations for this vault.

## [2026-05-05] skill | obsidian-llm-wiki

- Created local Codex skill at `~/.codex/skills/obsidian-llm-wiki`.
- Skill reads `AGENTS.md`, [[LLM Wiki 工作流]], and [[字段规范]] before wiki maintenance.
- Trigger phrases include ingest, query, lint, and "用 obsidian-llm-wiki".

## [2026-05-05] ingest | Attention Is All You Need

- Source: [[Attention Is All You Need]]
- Added PDF asset: `raw/papers/assets/Attention Is All You Need.pdf`
- Added extracted text: `raw/papers/extracted/Attention Is All You Need.extracted.md`
- Updated: [[LLM]], [[Transformer]], [[Self-Attention]], [[Multi-Head Attention]], [[Positional Encoding]]
- Questions: [[Transformer]] 为什么是 LLM 的地基但不是 Agent 能力；[[Self-Attention]] 和 [[Memory]] 的边界；[[Positional Encoding]] 和长上下文能力的关系。

## [2026-05-05] ingest | Remaining paper batch

- Sources: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]], [[ReAct - Synergizing Reasoning and Acting in Language Models]], [[Toolformer]], [[GAIA Benchmark]], [[SWE-bench]]
- Added PDF assets and extracted text under `raw/papers/assets/` and `raw/papers/extracted/`.
- Updated: [[RAG]], [[Agent Loop]], [[Tool Calling]], [[Evaluation]], [[Agent Harness]], [[Trace]]
- Added concepts: [[Parametric Memory]], [[Non-Parametric Memory]], [[Retriever]], [[ReAct]], [[Reasoning Trace]], [[Observation]], [[Tool Use]], [[Benchmark]], [[Task Success Rate]], [[Coding Agent]], [[Patch Validation]], [[Repo Context]]
- Note: ReAct PDF extraction has heavy `(cid:)` noise; use extracted text for high-level ingestion only and PDF for source verification.

## [2026-05-06] reading-plan | Paper source notes

- Updated paper source notes with "需要我读的内容" sections.
- Sources: [[Attention Is All You Need]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]], [[ReAct - Synergizing Reasoning and Acting in Language Models]], [[Toolformer]], [[GAIA Benchmark]], [[SWE-bench]]
- Added per-paper required sections, optional sections, skippable sections, self-check questions, and target concept updates.

## [2026-05-06] frontier | Candidate source collection and concept cards

- Sources: [[Azure AI Search Agentic Retrieval]], [[LangGraph Memory 官方文档]], [[Letta Memory 官方文档]], [[Zep Memory 官方文档]], [[Mem0 Memory 官方文档]], [[Agent2Agent Protocol]], [[Agent Communication Protocol]], [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]], [[OpenAI Computer Use 文档]], [[Anthropic Computer Use 文档]], [[browser-use GitHub Repo]], [[Playwright MCP Repo]], [[AGENTS.md and Codex Agent Loop]], [[OWASP LLM Top 10 2025]], [[OWASP Agentic Applications Top 10]], [[Self-RAG - Learning to Retrieve Generate and Critique]], [[Corrective Retrieval Augmented Generation]], [[MCP Tool Poisoning Threat Model]]
- Added concepts: [[Agentic Retrieval]], [[Eval Harness]], [[Long-term Memory]], [[Semantic Memory]], [[Episodic Memory]], [[Memory Reflection]], [[MCP]], [[A2A]], [[ACP]], [[Tool Registry]], [[Browser Agent]], [[GUI Grounding]], [[Observability]], [[Replay]], [[Trajectory Evaluation]], [[LLM-as-Judge]], [[AGENTS.md]], [[Sandbox Workspace]], [[Prompt Injection]], [[Indirect Prompt Injection]], [[Tool Poisoning]], [[Least Privilege Tools]], [[Approval Gate]], [[Policy Engine]], [[Corrective RAG]], [[Self-RAG]]
- Updated maps: `前沿概念候选表`（已合并进 [[03 前沿追踪]]）, [[前沿主源清单]], [[前沿主源清单]], [[资料收集索引]], [[02 问题池]]
- Boundary: [[RAGGraph]] remains an observation item because its usage is still split between graph workflow naming and graph-augmented retrieval.

## [2026-05-06] learning-path | Glossary and 30 daily templates

- Updated: [[01 术语表]], [[00 学习路线]], [[Agent 知识地图]], [[index]]
- Added 30 daily learning pages from [[2026-05-06]] to [[2026-06-04]].
- Structure: week 1 foundation, week 2 action systems, week 3 frontier structure, week 4 security and self-maintenance.
- Boundary: daily pages are execution templates, not proof of learning; each day still requires user's own explanation.

## [2026-05-06] source | Hello-Agents Repo

- Added source note: [[Hello-Agents Repo]]
- Updated: [[资料收集索引]], [[00 学习路线]], [[index]]
- Boundary: use it as a Chinese systematic learning/practice textbook, not as the latest frontier source.

## [2026-05-06] rag | RAG comparison and Neo4j source

- Added: [[RAG 类型对比]], [[Neo4j GraphRAG 官方文档]]
- Updated: [[RAG 主题]], [[GraphRAG]], [[前沿主源清单]], [[前沿主源清单]], [[02 问题池]]
- Boundary: Neo4j is an important GraphRAG implementation/tool ecosystem, not a separate RAG method at the same layer as [[Self-RAG]] or [[Corrective RAG]].

## [2026-05-06] concept | Neo4j as GraphRAG implementation layer

- Added: [[Neo4j]]
- Updated: [[GraphRAG]], [[RAG 主题]], [[RAG 类型对比]], [[01 术语表]], `前沿概念候选表`（已合并进 [[03 前沿追踪]]）, [[前沿主源清单]], [[Agent 知识地图]], [[资料收集索引]], [[前沿主源清单]], [[02 问题池]], [[Neo4j GraphRAG 官方文档]]
- Boundary: [[Neo4j]] belongs in the frontier source set because it is a major GraphRAG engineering ecosystem, but it should be learned as implementation/tooling rather than a new RAG method.

## [2026-05-06] tutorial | oh-my-codex

- Added source: [[Oh My Codex Repo]]
- Added concept: [[Oh My Codex (OMX)]]
- Added tutorial: [[oh-my-codex 使用教程]]
- Updated: [[index]], [[资料收集索引]], [[Agent 主题]], [[01 术语表]], [[前沿主源清单]], [[前沿主源清单]], [[Agent 知识地图]], [[02 问题池]]
- Boundary: OMX is a Codex CLI orchestration/harness layer, not a new model or a guarantee of correctness.

## [2026-05-06] lint | Missing wiki cards from links

- Added concepts: [[RAGGraph]], [[双链]]
- Updated: [[前沿主源清单]], `前沿概念候选表`（已合并进 [[03 前沿追踪]]）, [[02 问题池]], [[RAG 类型对比]], [[01 术语表]], [[Obsidian + LLM Wiki]], [[LLM Wiki 工作流]]
- Cleaned: escaped PDF extraction noise in `raw/papers/extracted/SWE-bench.extracted.md` so numeric vectors no longer appear as Obsidian pages.
- Result: missing-page scan for valid Obsidian links is clean.

## [2026-05-06] frontier-audit | Infrastructure gaps like Neo4j

- Added source: [[Agent 工程基础设施主源]]
- Added map: [[Agent 工程基础设施主源]]
- Added concepts: [[Vector Database]], [[Embedding]], [[Chunking]], [[Hybrid Search]], [[Reranking]], [[Document Ingestion]], [[RAG Evaluation]], [[Context Engineering]], [[Agent Framework]], [[Durable Execution]], [[Human-in-the-loop]], [[Handoff]], [[Code Execution Sandbox]], [[LLM Gateway]], [[OpenTelemetry GenAI]], [[MCP Registry]], [[Guardrails]], [[Tool Permissioning]], [[Audit Log]], [[Data Exfiltration]]
- Updated: [[前沿主源清单]], [[前沿主源清单]], [[Agent 知识地图]], [[01 术语表]], [[02 问题池]]
- Boundary: these are infrastructure and production layers, not necessarily new agent methods. They matter because they decide whether agent systems can ingest data, retrieve well, execute safely, recover, route models, observe behavior, and enforce permissions.

## [2026-05-06] maintenance | OMX on-demand setup cleanup

- Cleaned user-scope OMX setup with `omx uninstall` after backup at `~/.codex/backup-before-omx-cleanup-20260506-205446`.
- Preserved: npm `omx` command, Codex auth, existing non-OMX skills, and Jira MCP config.
- Removed: global OMX config block, native hooks, OMX prompts, OMX skills, and OMX native agent configs from `~/.codex`.
- Removed temporary preview directory: `/tmp/omx-setup-preview`.
- Updated: [[oh-my-codex 使用教程]]
- Boundary: this machine is now set up for project-scope OMX on demand, not global always-on OMX.

## [2026-05-06] tutorial | OMX relay provider

- Verified local Codex config uses `model_provider = "gettoken"` with a relay `base_url`, while `CODEX_HOME` is unset.
- Added concept: [[Multi-agent Orchestration]]
- Updated: [[oh-my-codex 使用教程]], [[前沿主源清单]], [[Agent 工程基础设施主源]]
- Boundary: OMX follows the same Codex config when launched from the same environment; only set a separate `CODEX_HOME` if you intentionally want a separate account/config/MCP stack.

## [2026-05-06] troubleshooting | OMX project-scope login prompt

- Updated: [[oh-my-codex 使用教程]]
- Added guidance for Codex login screen appearing after project-scope OMX launch.
- Boundary: project-scope OMX may use `./.codex` as Codex home, so it can miss global `~/.codex/auth.json`; either launch with `CODEX_HOME=$HOME/.codex` or link auth into project `.codex`.

## [2026-05-06] cleanup | Removed frontier maps

- Deleted: `maps/Agent 前沿概念全景.md`, `maps/Agent 前沿缺口审计.md`
- Repointed links to [[前沿主源清单]] or [[Agent 工程基础设施主源]] depending on whether the link was navigation or source evidence.
- Boundary: source notes and concept cards were preserved; only the two requested map files were removed.

## [2026-05-07] maintenance | Map slim-down

- Removed early scaffold maps: `maps/学习工作流.md`, `maps/第一周阅读计划.md`, `maps/阅读笔记索引.md`, `maps/前沿概念候选表.md`.
- Merged durable guidance into [[index]], [[00 学习路线]], [[03 前沿追踪]], [[资料收集索引]], and [[LLM Wiki 工作流]].
- Updated [[插件配置]] to mark Dataview/Templater as installed plugin files that still need Obsidian-side enablement if tables/templates do not work.
- Boundary: `maps/` should hold repeatedly used navigation and review pages, not one-time setup explanations.

## [2026-05-07] llm-wiki | Mechanism upgrade

- Added [[04 页面目录]] as a static page catalog.
- Added [[05 Query 写回队列]] so durable chat answers are written back instead of staying in conversation history.
- Added [[06 Wiki 健康检查]] for weekly lint, freshness, and contradiction tracking.
- Updated [[字段规范]], [[LLM Wiki 工作流]], [[index]], templates, and `AGENTS.md` with `evidence`, `last_checked`, `freshness`, and query-writeback rules.
- Batch-added evidence anchors to 81 concept cards and freshness metadata to 41 raw source notes.
- Wrote back durable answers into [[Obsidian + LLM Wiki]], [[Oh My Codex (OMX)]], and [[oh-my-codex 使用教程]].
- Verification: missing links none; concept evidence gaps 0; raw freshness gaps 0; bad evidence anchors 0.
- Boundary: current evidence is source-note / section level. Claim-level page or paragraph citations still require focused paper/source reading.

## [2026-05-07] publish | GitHub repository setup

- Added root `README.md` explaining the Obsidian + LLM Wiki structure, usage loop, Codex workflow, and Git asset policy.
- Added `.gitignore` for PDFs, images, media, archives, Obsidian plugin/theme bundles, workspace state, caches, vector indexes, and secrets.
- Boundary: GitHub tracks the Markdown knowledge system and reusable configuration; large source assets remain local evidence files.

## [2026-05-07] source | 小林 Note sitemap 面试题抓取

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Crawled: 120 sitemap URLs from <https://xiaolinnote.com/sitemap.xml>.
- Added raw source pages under `raw/articles/xiaolinnote/`: 120 successful pages, 0 failed pages.
- Updated: [[资料收集索引]], [[04 页面目录]], [[index]]
- Boundary: this batch is raw evidence import only; it has not yet been digested into concept cards.

## [2026-05-07] source-update | 小林 Note sitemap 面试题

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Scope: `all`; checked 120 sitemap URLs.
- Result: new 0, changed 0, unchanged 120, errors 0.
- Updated navigation: [[资料收集索引]], [[04 页面目录]], [[index]]
- Boundary: this is raw evidence refresh; changed pages still need explicit wiki/concept digestion if their content matters.

## [2026-05-08] query | ReAct 是否仍是 Agent 主流范式

- Question: 现在的 Agent 都在使用 ReAct 范式吗？ReAct 对模型能力、执行效率、提示词和局部最优的依赖现在怎么解决？
- Updated: [[ReAct]], [[05 Query 写回队列]]
- Sources checked: [[ReAct - Synergizing Reasoning and Acting in Language Models]], [[Anthropic - Building Effective Agents]], [[OpenAI - A Practical Guide to Building Agents]], [[LangGraph 官方文档]]
- Boundary: ReAct 仍是理解 [[Agent Loop]] 的经典模式，但现代生产 Agent 通常用 workflow、state graph、tool schema、guardrails、evaluation、trace、human-in-the-loop 和 harness 来包住它，而不是只靠一个 ReAct prompt 模板裸跑。

## [2026-05-08] ingest | Plan-and-Solve Prompting

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Added concept: [[Plan-and-Solve Prompting]]
- Updated: [[Planning]], [[01 术语表]], [[资料收集索引]], [[Agent 主题]]
- Boundary: Plan-and-Solve Prompting 是 zero-shot CoT 的 plan-first 提示方法，不是 [[ReAct]]，也不是完整 [[Agent Loop]]；它没有外部 Action 和 [[Observation]] 反馈。

## [2026-05-08] image-ingest | Planning Phase / Solving Phase

- Source: 用户提供截图，录入到 [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Updated: [[Plan-and-Solve Prompting]], [[Planning]]
- Asset: `agentic learning/raw/assets/plan-and-solve-planning-solving-phase.svg`（根据用户截图重绘）
- Boundary: 图片内容更接近 plan-and-execute / plan-and-replan workflow；它能解释 planning 的工程化形态，但不应直接等同于 [[Plan-and-Solve Prompting]] 论文里的纯 prompting 方法。

## [2026-05-08] query | Agent framework 如何接管 prompt loop

- Question: 现在框架是怎么更好地接管 ReAct / Plan-and-Solve 这类 prompt pattern？
- Updated: [[Agent Framework]], [[05 Query 写回队列]]
- Sources checked: [[OpenAI Agents SDK 文档]], [[LangGraph 官方文档]], [[Agent Framework]], [[Agent Harness]], [[Tool Calling]], [[Durable Execution]], [[Guardrails]]
- Boundary: 框架接管的不是“模型思考”本身，而是把工具调用格式、状态、流程、执行恢复、权限和 trace 从 prompt 软约束变成 runtime 工程对象。

## [2026-05-08] concept | Agent State and Agent Workflow

- Added concepts: [[Agent State]], [[Agent Workflow]]
- Updated: [[Agent Framework]], [[01 术语表]], [[Agent 知识地图]]
- Boundary: [[Agent State]] 解释框架如何保存当前任务运行状态，不等于 [[Memory]] 或 context window；[[Agent Workflow]] 解释任务路径如何被工程化控制，不等于 [[Agent Loop]] 或 [[Agent Framework]] 本身。

## [2026-05-08] ingest | Reflexion

- Source: [[Reflexion - Language Agents with Verbal Reinforcement Learning]]
- Added concept: [[Reflexion]]
- Updated: [[Memory Reflection]], [[01 术语表]], [[Agent 知识地图]], [[资料收集索引]], [[Agent 主题]]
- Image: 用户提供 Reflexion Agent Loop 截图，已录入 raw note 的图像结构摘要和 Mermaid 重画。
- Asset: `agentic learning/raw/assets/reflexion-agent-loop.svg`（根据用户截图重绘）
- Boundary: [[Reflexion]] 是执行后基于反馈生成反思文本并改进下一轮行动的机制；它不是普通 [[Reasoning Trace]]，也不等于 [[Memory Reflection]] 或模型权重训练。

## [2026-05-09] query-writeback | LLM Training Pipeline

- Added concept: [[LLM Training Pipeline]]
- Added sources: [[Scaling Laws for Neural Language Models]], [[Training Compute-Optimal Large Language Models]], [[Training Language Models to Follow Instructions with Human Feedback]], [[Constitutional AI - Harmlessness from AI Feedback]], [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]], [[The Llama 3 Herd of Models]]
- Updated: [[LLM]], [[Evaluation]], [[LLM 主题]], [[01 术语表]], [[05 Query 写回队列]]
- Boundary: 现代 LLM 变强不是单靠做大模型，而是预训练 scaling、数据质量、后训练、偏好优化、推理强化、工具/Agent 兼容性和评测闭环共同作用；模型训练提升决策质量，但 Agent runtime 仍负责工具、状态、权限、trace 和真实执行。

## [2026-05-09] source | agent_java_offer repo

- Source: [[raw/repos/agent_java_offer Repo]]
- Added raw repo source for <https://github.com/guoguo-tju/agent_java_offer>.
- Updated: [[资料收集索引]], [[04 页面目录]], [[index]]
- Boundary: this is an interview-prep source for Java backend / AI Agent / system design material; it is not yet digested into concept cards and should not replace papers, official docs, or framework source evidence.

## [2026-05-09] source-ingest | agent_java_offer interview questions

- Source: [[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]
- Crawled repo commit: `12bf4c915cca01f513e040935e1917d3687f8b35`.
- Scope: `docs/interview_prep/`; parsed 43 core Q&A files and generated 637 raw question notes under `raw/repos/agent_java_offer/questions/`.
- Breakdown: `question` 282, `followup-question` 267, `supplement-section` 39, `algorithm-problem` 49.
- Updated: [[agent_java_offer Repo]], [[资料收集索引]], [[04 页面目录]], [[index]]
- Boundary: this batch is raw evidence import only. It improves search and recall for interview practice, but concept cards still require separate digestion and stronger evidence from papers, official docs, or framework source.
## [2026-05-09] maintenance | agent_java_offer question wiki backlinks

- Updated: [[raw/repos/agent_java_offer/agent_java_offer 面试题索引]] and 637 question notes under `raw/repos/agent_java_offer/questions/`.
- Added `## 相关知识 wiki` to every question note.
- Result: 389 notes linked to existing wiki concepts/topics; 248 notes intentionally marked as having no direct existing concept card.
- Boundary: links are conservative retrieval aids based on title/body/category, not proof that the interview answer is conceptually calibrated.

## [2026-05-09] maintenance | xiaolinnote raw structure alignment

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Moved 120 小林 Note raw pages from `raw/articles/xiaolinnote/` into `raw/articles/xiaolinnote/questions/`.
- Updated the index links and source navigation to match the `agent_java_offer` layout: source index page plus `questions/` item pages.
- Verification: 120 index links checked, missing 0.
- Boundary: this is a path/layout normalization only; page content and source evidence were preserved.

## [2026-05-09] maintenance | xiaolinnote repo-layout and title normalization

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Moved xiaolinnote raw source from `raw/articles/xiaolinnote/` to `raw/repos/xiaolinnote/` to align interview-bank layout with [[raw/repos/agent_java_offer/agent_java_offer 面试题索引]].
- Renamed 120 question pages from URL slug filenames to readable `NNN 分类 子分类 页面标题.md` filenames; normalized each page H1 and index display title to the same cleaned page title.
- Preserved `source_type: web`, original URLs, sha256 evidence fields, and `crawl-manifest.json`.
- Boundary: this is raw source structure maintenance only; no new concept cards were created.

## [2026-05-09] maintenance | xiaolinnote question wiki backlinks

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Updated 120 xiaolinnote raw question cards with `## 相关知识 wiki` sections and matching `related` links.
- Link vocabulary: 140 unique targets; 85 are intentional redlinks for concepts not yet collected into wiki cards.
- Boundary: these are retrieval and study-path links only; raw interview notes remain source evidence and have not been promoted into concept cards.
