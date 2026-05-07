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

- Source: [[raw/articles/xiaolinnote/小林 Note 面试题索引]]
- Crawled: 120 sitemap URLs from <https://xiaolinnote.com/sitemap.xml>.
- Added raw source pages under `raw/articles/xiaolinnote/`: 120 successful pages, 0 failed pages.
- Updated: [[资料收集索引]], [[04 页面目录]], [[index]]
- Boundary: this batch is raw evidence import only; it has not yet been digested into concept cards.
