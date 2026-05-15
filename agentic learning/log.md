---
type: log
topic:
  - obsidian
  - llm-wiki
status: active
created: 2026-05-05
updated: 2026-05-12
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

## [2026-05-10] cleanup | remove daily plan and fixed learning route

- Removed `agentic learning/daily/` and the Obsidian daily-notes config.
- Removed [[00 学习路线]] and cleared current navigation links to the fixed 30-day route.
- Updated [[index]], [[资料收集索引]], [[Agent 知识地图]], [[02 问题池]], [[04 页面目录]], [[LLM Wiki 工作流]], [[字段规范]], and README toward a question-driven / Feynman-review learning loop.
- Boundary: historical log entries still mention the old daily plan as past maintenance facts; current navigation no longer treats it as active structure.
## [2026-05-10] asset | ReAct tools-LLM-environment diagram

- Asset: `agentic learning/raw/assets/reAct.png`（用户提供原始透明背景截图）
- Asset: `agentic learning/raw/assets/reAct-white-bg.png`（为透明 PNG 添加白色背景，保证可见性）
- Asset: `agentic learning/raw/assets/react-agent-loop.svg`（按 [[Reflexion]] 图风格重绘，便于 LLM 和 Obsidian 理解）
- Updated: [[ReAct]], [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Boundary: the original image captures the external components around a ReAct-style loop; the redraw makes the missing runtime loop explicit: LLM proposes action, harness executes tools/environment steps, observation is written back into context/state, then the next LLM step starts.
## [2026-05-10] review | ReAct concept-triggered review

- Added: [[01 概念触发式复习]]
- Updated: [[实验记录索引]], [[index]]
- Seeded the first concept-triggered review with the user's own ReAct explanation, a calibrated version, five Feynman-style follow-up questions, and write-back candidates.
- Boundary: this is a review/learning record, not a raw source and not a replacement for [[ReAct]] as the durable concept card.
## [2026-05-10] maintenance | review folder and concept-triggered template

- Moved: [[01 概念触发式复习]] into `agentic learning/reviews/`.
- Added: [[reviews/复习记录索引]], [[templates/概念触发式复习]]
- Updated: [[index]], [[04 页面目录]], [[字段规范]], [[LLM Wiki 工作流]], [[实验记录索引]]
- Boundary: `reviews/` is a learning-process layer for Feynman review and write-back candidates; it is not raw evidence and not a durable concept-card layer.
## [2026-05-10] maintenance | concept card style rule

- Updated: [[Plan-and-Solve Prompting]], [[LLM Wiki 工作流]]
- Updated skill: `obsidian-llm-wiki`
- Updated project instruction: `AGENTS.md`
- Boundary: durable concept cards should follow the [[ReAct]]-style learning-card shape, with explicit "它不是什么", "边界细节", evidence anchors, and a modern-system absorption section when a paper/prompting pattern needs to be separated from production Agent runtime behavior.
## [2026-05-10] correction | concept card style reference

- Corrected style reference from [[ReAct]] to [[Plan-and-Solve Prompting]] in `obsidian-llm-wiki`, [[LLM Wiki 工作流]], and `AGENTS.md`.
- Updated: [[ReAct]]
- Boundary: [[Plan-and-Solve Prompting]] is the preferred concept-card standard because it includes the fuller learning-card flow: problem, non-goals, common misunderstanding, boundary details, modern-system absorption, evidence anchors, and related links.

## [2026-05-10] concept-update | Observation

- Updated: [[Observation]], [[01 术语表]], [[Agent 知识地图]]
- Evidence: [[ReAct - Synergizing Reasoning and Acting in Language Models]], [[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]
- Boundary: Observation 是动作后的外部反馈，不是模型 Thought，也不是 Action 本身；本次重点补充了来源类型（tool result、environment state、user feedback、test output、browser state）和风险（污染、过期、格式不稳定、被模型误读）。
## [2026-05-10] concept-update | Trajectory boundary

- Added: [[Trajectory]]
- Updated: [[Trace]], [[Reasoning Trace]], [[Trajectory Evaluation]], [[Reflexion]], [[01 术语表]], [[Agent 知识地图]]
- Boundary: Trajectory 是任务实际走过的行动路径；[[Trace]] 是对路径的观测记录；[[Reasoning Trace]] 是路径中模型显式推理文字的切片。
## [2026-05-10] map | analogy comparison cards

- Added: [[Trajectory Trace 类型对比]]
- Updated: [[RAG 类型对比]], [[Agent 主题]], [[04 页面目录]], [[Trajectory]], [[Trace]], [[Reasoning Trace]]
- Boundary: 对比型 topic 卡用于学习类比和边界训练，不替代单概念卡；本次为 RAG 类型和 Trajectory/Trace/Reasoning Trace 都补了生活类比。
## [2026-05-10] map | Environment Observation analogy

- Added: [[Environment Observation 类型对比]]
- Updated: [[Observation]], [[ReAct]], [[Agent 主题]], [[04 页面目录]]
- Boundary: Environment 是动作发生的外部世界或系统；[[Observation]] 是这个外部世界对某次 action 返回给 agent runtime 的反馈结果。

## [2026-05-10] concept-update | OMX dollar commands

- Added: [[OMX $ 指令]]
- Updated: [[Oh My Codex (OMX)]], [[oh-my-codex 使用教程]], [[01 术语表]], [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]], [[index]]
- Evidence: local `omx list --json` (catalog `2026.02.28.1`) and local OMX skill definitions under `${CODEX_HOME:-~/.codex}/skills/*/SKILL.md`.
- Boundary: OMX `$` 指令是 Codex 会话里的 skill/workflow 触发入口，不等于普通 shell CLI；goal 类 shell commands 写 `.omx/` artifacts 和 handoff，不直接修改隐藏 Codex `/goal` 状态。

## [2026-05-10] review | Plan-and-Solve concept-triggered review

- Updated: [[01 概念触发式复习]]
- Source concept: [[Plan-and-Solve Prompting]]
- Added the user's Feynman-style explanation, a calibrated version, follow-up questions, and write-back candidates.
- Boundary: the user's description captures modern plan-and-execute / replan [[Agent Workflow]] well, but strict [[Plan-and-Solve Prompting]] is a prompt-layer zero-shot CoT method without external Action, [[Observation]], or runtime replan.

## [2026-05-10] autoresearch | modernity classification rule

- Updated: [[LLM Wiki 工作流]], [[03 前沿追踪]], [[ReAct]], [[Agent Framework]], [[Agent Workflow]]
- Sources checked: [[ReAct - Synergizing Reasoning and Acting in Language Models]], [[Anthropic - Building Effective Agents]], [[OpenAI - A Practical Guide to Building Agents]], [[LangGraph 官方文档]], [[OpenAI Agents SDK 文档]]
- Source freshness: refreshed `last_checked` for Anthropic/OpenAI/LangGraph/OpenAI Agents SDK source notes to 2026-05-10; [[ReAct - Synergizing Reasoning and Acting in Language Models]] was already checked today.
- Rule: 论文范式通常是基础地基或历史过渡；框架吸收方式通常是当前工程实践；具体 SDK/API/产品能力才更可能是前沿或易变。
- Boundary: “现代系统怎么吸收旧范式”不自动等于前沿。旧范式可能仍是稳定概念语言；裸 prompt 实现可能是历史过渡；runtime、state、tool schema、guardrails、trace 和 eval 是现代工程吸收层。

## [2026-05-10] concept-update | Zero-shot CoT

- Added: [[Zero-shot CoT]]
- Updated: [[Plan-and-Solve Prompting]], [[01 术语表]], [[LLM 主题]], [[04 页面目录]]
- Evidence: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]], [[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]], [[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]
- Boundary: Zero-shot CoT 是 prompt 层的文本推理激活方法，不是 [[ReAct]]、不是 [[Agent Workflow]]，也不是模型真实思维的可靠窗口。

## [2026-05-10] workflow | proactive modernity classification

- Updated: [[LLM Wiki 工作流]], [[templates/概念卡]]
- Updated project instruction: `AGENTS.md`
- Updated skill: `obsidian-llm-wiki`
- Rule: 创建或更新概念卡时，LLM 要主动判断 `foundation / transitional / current-practice / frontier / 不适用`，并写入 `## 现代性状态` 或相邻现代系统段落，不等用户单独追问。
- Boundary: 这条规则不要求每个普通生活类比或静态基础术语都硬套“前沿”判断；但凡涉及 Agent、prompting、framework、evaluation、RAG、memory、tooling、安全、协议或产品生态，就必须显式判断。

## [2026-05-10] autoresearch | agent lifecycle hooks and observability

- Added: [[Agent Lifecycle Hook]]
- Added sources: [[Claude Code Hooks 文档]], [[Arize Phoenix Tracing 文档]], [[OpenTelemetry GenAI Semantic Conventions]]
- Updated: [[Agent Harness]], [[Trace]], [[Observability]], [[OpenTelemetry GenAI]], [[Oh My Codex (OMX)]], [[ReAct]], [[01 术语表]], [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]], [[资料收集索引]], [[index]]
- Local evidence: `~/.codex/hooks.json` maps `PreToolUse`, `PostToolUse`, `SessionStart`, `UserPromptSubmit`, `PreCompact`, `PostCompact`, and `Stop` to OMX `codex-native-hook.js`; `.omx/` contains turn logs, metrics, session state, subagent tracking, and autoresearch ledger artifacts.
- Boundary: lifecycle hooks are runtime / harness control points, not LLM model internals; hook events can feed [[Trace]] and [[Observability]], while action approval and side-effect prevention still belong to [[Agent Harness]], [[Guardrails]], and [[Tool Permissioning]].

## [2026-05-10] query-writeback | OMX observability recommendation

- Updated: [[Oh My Codex (OMX)]], [[Observability]]
- Answer: OMX 当前更推荐先用本地 operator observability：`.omx/` artifacts、`omx hud --watch/json`、`omx sidecar`、hooks 和 notifications；LangSmith、Langfuse、Phoenix、OpenTelemetry 属于外接观测平台，需要额外 adapter。
- Boundary: OMX 的 HUD/sidecar/notifications 是本地运行时可见性，不等于标准 APM/OTel trace，也不自动提供质量评估。

## [2026-05-10] workflow | concept-card standardization

- Updated standard: `AGENTS.md`, [[LLM Wiki 工作流]], [[templates/概念卡]], [[06 Wiki 健康检查]]
- Updated style anchors: [[Agent]], [[Trace]], [[Trajectory Evaluation]], [[RAG]]
- Rule: 概念卡按“双层学习 + 判断卡”写；`## 一句话` 只是入口，不等于整卡只写一句话。够格卡应有问题背景、边界细节、现代性状态、证据锚点和复习触发。
- Lint finding: 90 张概念卡中，修复 4 张样例卡后仍有 57 张缺 `## 边界细节`，79 张缺 `## 现代性状态`，86 张缺 `## 复习触发`（修复前为 60 / 83 / 90）；已写入 [[06 Wiki 健康检查]] 队列。
- Boundary: 本次只修标准、模板、健康队列和 4 张样例卡；未批量重写旧概念卡，后续批量修复需要用户确认。

## [2026-05-10] review | ReAct Feynman answers

- Updated: [[01 概念触发式复习]]
- Feedback: Q1 和 Q3 已掌握；Q2 需要补“Observation 驱动下一轮决策”；Q4 已理解方向但需补权限、格式、停止条件和 trace/eval；Q5 需要继续练习停止、纠错、评估和人工升级四类机制。
- Next review: 新增 ReAct 第二轮追问 5 题。

## [2026-05-10] concept-update | P1 concept-card repair

- Updated: [[Agent Loop]], [[Agent Framework]], [[Agent State]], [[Agent Workflow]], [[Evaluation]], [[Eval Harness]], [[LLM-as-Judge]], [[RAG Evaluation]], [[06 Wiki 健康检查]]
- Change: 按新概念卡标准小范围修复 P1 Agent 工程组和 Evaluation 组：补问题背景、最小例子、常见误解/风险、边界细节、现代性状态、现代系统吸收方式、证据锚点、复习触发和相关链接。
- Verification: 8 张目标卡 section/evidence audit PASS；hard-boundary audit PASS（未改 raw/、AGENTS.md、模板页，未批量改 P2 协议/前沿卡）；`git diff --check` PASS。
- Health counts: [[06 Wiki 健康检查]] 更新为仍缺 `## 边界细节` 51、`## 现代性状态` 73、`## 复习触发` 78。
- Boundary: 本次是小范围 P1 结构修复，不是全量重写；未把卡片扩成百科长文，未把无来源推断写成来源事实。`reviews/` 中的学习记录仍是学习校准材料，不作为 raw evidence。用户随后指出：结构完整不等于概念详解充分，后续已升级标准。

## [2026-05-10] autoresearch | Tool Calling schema

- Added sources: [[OpenAI Function Calling 文档]], [[Anthropic Tool Use 文档]]
- Updated: [[Tool Calling]], [[Model Context Protocol 官方文档]], [[资料收集索引]], [[04 页面目录]], [[01 概念触发式复习]]
- Answer: Tool Calling schema 是工具的说明书 / 参数契约，通常用 JSON Schema 或类似结构表达工具名、描述、参数字段、类型、必填项和枚举约束。
- Boundary: schema 只约束调用请求的形状，不执行工具，也不替代权限、业务校验、工具结果可信度、trace 或评估。

## [2026-05-10] workflow | concept-detail standard upgrade

- Updated standard: `AGENTS.md`, [[LLM Wiki 工作流]], [[templates/概念卡]], local `obsidian-llm-wiki` skill, [[06 Wiki 健康检查]]
- Updated deep examples: [[Agent Loop]], [[Evaluation]]
- Rule: `## 一句话` 只是入口；qualified / anchor 概念卡必须有 `## 概念详解`，且详解应占最高解释比重，覆盖概念动机、机制、论文/官方文档/社区实践描述、现代系统吸收方式和证据边界。
- Evidence: [[Agent Loop]] 详解引用 ReAct source note、OpenAI/Anthropic/LangGraph/Agents SDK source notes；[[Evaluation]] 详解引用 GAIA、SWE-bench、LangSmith、Langfuse source notes。
- Boundary: section 完整只是最低门槛；没有连续解释、来源边界和例子的卡仍然是浅卡。P1 剩余 6 张进入详解深度复查队列。

## [2026-05-10] concept-update | P1 concept-detail completion

- Updated: [[Agent Framework]], [[Agent State]], [[Agent Workflow]], [[Eval Harness]], [[LLM-as-Judge]], [[RAG Evaluation]], [[06 Wiki 健康检查]]
- Change: 补齐 P1 剩余 6 张卡的 `## 概念详解`，让详解成为主体段落，而不是只满足 section 完整；每张都补充动机、机制/组件、官方文档或社区实践证据、现代工程吸收方式和证据边界。
- Evidence: Agent 工程组引用 [[LangGraph 官方文档]], [[OpenAI Agents SDK 文档]], [[Anthropic - Building Effective Agents]], [[OpenAI - A Practical Guide to Building Agents]]；评估组引用 [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]], [[SWE-bench]], [[Microsoft RAG 官方文档]]。
- Verification: P1 8 张目标卡均有 `## 概念详解`、`## 证据锚点` 中的 Evidence type / Boundary；本次未改 `raw/`；`git diff --check` 与 `git diff --cached --check` PASS。
- Boundary: 本次完成的是 P1 8 张目标卡的深度样例化，不是全量重写 90 张概念卡；后续仍需按主题小批量修复旧卡。

## [2026-05-10] workflow | team concept-card standardization protocol

- Added: [[07 Team 概念卡全量规范化]]
- Added local audit tool: `scripts/concept_card_audit.py`
- Updated: [[04 页面目录]], [[index]], `scripts/README.md`
- Purpose: 将“7 个进程全量修概念卡”变成可分工、可审计、可回滚的执行协议：5 个 writer lane、1 个 evidence auditor、1 个 final verifier。
- Audit baseline: 90 张概念卡；脚本当前判定 82 张需处理；深度分布为 anchor 22、qualified 28、volatile 37、seed-lite 3。
- Boundary: 本次只实现协议、脚本和导航，不启动 `$team`，不改 `raw/`，不重写概念卡正文；脚本是辅助 lint，最终仍需 leader/verifier 判断概念详解是否真的讲透。

## [2026-05-10] workflow | review round limit

- Updated: [[01 概念触发式复习]], [[templates/概念触发式复习]], [[reviews/复习记录索引]]
- Rule: 概念触发式复习最多两轮追问；第一轮暴露误解，第二轮只处理关键卡点，之后必须收束到写回候选、问题池或概念卡。
- Boundary: 如果两轮后仍不清楚，优先说明概念卡或材料需要重写，不用继续追问拖慢学习节奏。

## [2026-05-10] query-writeback | DeepSeek reasoning model vs Zero-shot CoT

- Updated: [[Zero-shot CoT]], [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- Answer: 2024-11-20 的 DeepSeek-R1-Lite-Preview 从用户体验上很像长 CoT / thinking mode，但不等于经典 Zero-shot CoT prompting；它更接近把长推理、验证和反思训练成模型行为，再在推理时展开更多 token。
- Evidence: DeepSeek 官方 R1-Lite-Preview release note、DeepSeek-R1 release note、DeepSeek-R1 arXiv 摘要。
- Boundary addendum: DeepSeek-R1 可以说继承 CoT / Zero-shot CoT 的思想脉络，但不能说训练原理只是照搬这篇 prompt 论文；R1 的关键在 RL、可验证奖励、cold-start 数据和多阶段训练。

## [2026-05-11] concept-update | team concept-card full standardization completion

- Merged team writer lanes: worker-1 Agent foundations, worker-3 evaluation/observability, worker-4 RAG/retrieval, worker-5 security/protocol/frontier, plus worker-2 runtime/memory lane follow-up.
- Updated runtime/memory residuals: [[Memory]], [[Durable Execution]], [[Handoff]], [[Agent Lifecycle Hook]], [[Code Execution Sandbox]], [[LLM Gateway]], [[Long-term Memory]], [[Semantic Memory]], [[Episodic Memory]], [[Memory Reflection]], [[Non-Parametric Memory]], [[Parametric Memory]], [[AGENTS.md]], [[双链]].
- Evidence cleanup: corrected stale `[[前沿主源清单#RAG 进化]]` anchors in [[Agent Harness]], [[Multi-agent Orchestration]], [[Trace]], [[Computer Use]].
- Verification: `python3 scripts/concept_card_audit.py --format markdown` reports 90 cards / Needs action 0; `git diff --check` PASS; `git diff --cached --check` PASS; raw boundary check PASS.
- Boundary: This completes current structural/depth standardization, not final human learning. A concept is still only learned when the user can explain it in their own words via `reviews/`.

## [2026-05-11] autoresearch-goal | Hermes Agent

- Added source: [[Hermes Agent Repo]]
- Added concept: [[Hermes Agent]]
- Updated: [[资料收集索引]], [[前沿主源清单]], [[Agent 知识地图]], [[01 术语表]], [[Agent 主题]], [[03 前沿追踪]], [[04 页面目录]], [[06 Wiki 健康检查]]
- Evidence: official GitHub repo, official docs raw markdown for architecture / memory / skills / security / MCP / persistent goals, and GitHub latest release API checked on 2026-05-11 (`v2026.5.7`, Hermes Agent v0.13.0).
- Boundary: Hermes Agent is recorded as a volatile concrete runtime/project, not as the general definition of Agent and not as proof that self-improving skills are reliable without evaluation.

## [2026-05-11] workflow | paper source template and constraints

- Added: [[templates/论文]]
- Updated: [[字段规范]], [[资料收集索引]], [[04 页面目录]]
- Rule: `raw/papers/` 新建论文 source note 使用 paper 专属 frontmatter（`pdf`、`arxiv`、`doi`、`venue`、`pages`、`extracted`）和固定证据 section；raw note 只回答“论文原文说了什么、可支撑哪些概念”，不替代 `wiki/concepts/` 的稳定理解。
- Boundary: 本次只增加模板和规则约束，不批量迁移或重写已有 `raw/papers/*.md`；已有论文笔记后续可按需小批量规范化。

## [2026-05-11] workflow | paper required-reading extraction rule

- Updated: [[templates/论文]], [[资料收集索引]]
- Rule: `raw/papers/` 的 `### 必读` 不再只是阅读清单，而是必读证据提取区；每个必读块要写位置、为什么必读、原文短摘、中文概括、支撑概念和证据边界。
- Boundary: 内容过多时只摘 1-3 句关键原话，其余用中文概括；原文短摘负责证据，中文概括负责学习，不把长篇原文搬进 raw note，也不把概括伪装成论文原话。

## [2026-05-11] source-maintenance | paper source-note required-reading extraction

- Updated: all 15 `raw/papers/*.md` paper source notes.
- Added audit: `scripts/paper_source_audit.py`; documented in `scripts/README.md`; `.gitignore` now allows this audit script to be versioned beside `concept_card_audit.py`.
- Change: 全量把 `### 必读` 从阅读清单升级为“必读证据提取区”；每篇至少 2 个 `#### 必读块`，分开写位置、为什么必读、原文短摘、中文概括、机制、支撑概念和证据边界。
- Evidence: 有本地 extracted/PDF 的论文优先锚到 `raw/papers/extracted/` page；其余论文使用论文 abstract / paper page 的短摘，并标明 `last checked 2026-05-11`。已用脚本核对短摘能回到本地 extracted 或 arXiv 页面。
- Verification: `python3 scripts/paper_source_audit.py` PASS；`python3 scripts/concept_card_audit.py --format markdown` Needs action 0；`git diff --check` PASS；scoped deslop 未发现 TODO / 临时 fallback / 待精读占位。
- Boundary: 本次只改 raw paper source notes 和审计脚本，不改 `wiki/concepts/`；raw note 仍是 evidence 层，不替代稳定概念卡。原文短摘保持短句，长内容只用中文概括，不伪造页码或段落级证据。

## [2026-05-11] autoresearch-goal | LangChain DeepAgents

- Added source: [[LangChain Deep Agents 官方文档]]
- Added concept: [[LangChain DeepAgents]]
- Updated: [[资料收集索引]], [[前沿主源清单]], [[Agent 知识地图]], [[01 术语表]], [[Agent 主题]], [[03 前沿追踪]], [[04 页面目录]], [[05 Query 写回队列]]
- Evidence: LangChain Deep Agents docs, LangChain products / layer docs, `langchain-ai/deepagents` repo, and existing [[LangGraph 官方文档]] source note checked on 2026-05-11.
- Boundary: This card records LangChain / LangGraph `deepagents` as a volatile SDK / harness, not the universal definition of deep agent and not RUC-NLPIR DeepAgent.

## [2026-05-12] workflow | concept comparison topic mechanism

- Added standard/template: [[LLM Wiki 工作流]], [[概念对比页]]
- Added exemplar: [[ReAct Plan-and-Solve Reflexion 对比]]
- Updated navigation: [[Agent 主题]], [[Agent 知识地图]], [[04 页面目录]], [[05 Query 写回队列]], [[index]]
- Updated backlinks: [[ReAct]], [[Plan-and-Solve Prompting]], [[Reflexion]]
- Rule: 概念对比页用于训练边界辨析；对比组可以是 2/N 者，但必须满足混淆风险、相近问题不同介入点、证据锚点、现代工程边界和复习价值。
- Evidence: 样板页锚到 ReAct、Plan-and-Solve、Reflexion 三张概念卡和对应 paper source note 的必读块。
- Boundary: 本次只建立机制、模板、首个样板页和候选队列；未批量重写旧卡，未新建弱对比页，未修改 `raw/` source notes。

## [2026-05-12] review | ReAct Plan-and-Solve Reflexion follow-up cards

- Added: [[01-2 ReAct Plan-and-Solve Reflexion 追问卡]]
- Updated: [[复习记录索引]]
- Purpose: 基于 [[01 概念触发式复习]] 暴露出的卡点生成独立追问卡，避免继续拉长原复习页。
- Focus: ReAct 原地打转止损、一次性 tool calling vs ReAct、plan 文本 / Agent State task list / context 投影、代码任务越过 prompt-only Plan-and-Solve、workflow replan 补救、Reflexion Experience 与长期记忆边界、三者执行时序对比。
- Boundary: 本次只生成复习追问卡，不把学习记录当作 raw evidence，也不直接改概念卡定义。

## [2026-05-12] review-feedback | ReAct Plan-and-Solve Reflexion follow-up answers

- Updated: [[01-2 ReAct Plan-and-Solve Reflexion 追问卡]]
- Added Codex feedback for all 7 follow-up answers and marked this second-round review as 收束.
- Writeback candidates: card 5 workflow replan boundary, card 6 Experience-to-long-term-memory filter, card 7 execution-order comparison.
- Remaining review-only gaps: card 1 still needs repeat-action detection -> correction/escalation; card 3 still needs state vs context projection boundary.
- Boundary: This is learning-process calibration, not raw evidence and not yet a concept-card writeback.

## [2026-05-12] review-writeback | ReAct Plan-and-Solve Reflexion follow-up answers

- Updated: [[Agent Workflow]], [[Long-term Memory]], [[Memory Reflection]], [[ReAct Plan-and-Solve Reflexion 对比]], [[01-2 ReAct Plan-and-Solve Reflexion 追问卡]]
- Writeback: card 5 plan-error recovery boundary added to workflow replan / evidence / escalation; card 6 Experience-to-long-term-memory filter added to long-term memory and memory reflection; card 7 execution-order knife-edge added to the comparison topic.
- Deferred: card 1 repeat-action correction/escalation and card 3 state vs context projection remain review-only gaps.
- Boundary: Review answers are learning calibration, not raw evidence; concept-card evidence remains anchored to existing docs and paper source notes.

## [2026-05-12] review | classic agent paradigms chapter practice

- Added: [[02 经典智能体范式综合实践]]
- Updated: [[复习记录索引]]
- Purpose: 把用户提供的章节综合题整理成第二轮实践入口，覆盖 ReAct / Plan-and-Solve / Reflection 的范式选型、代码解析、工具扩展、动态重规划、Reflection 终止条件、提示词工程和电商客服智能体产品设计。
- Boundary: 本页是 review/practice，不是 raw evidence；先保留回答区、实验记录和写回候选，等待用户逐题作答或实际编写代码后再反馈和写回概念卡。

## [2026-05-12] review-writeback | deferred 01-2 boundaries

- Updated: [[Agent Harness]], [[Agent State]], [[01-2 ReAct Plan-and-Solve Reflexion 追问卡]]
- Writeback: card 1 repeat-action loop control added to Agent Harness; card 3 plan text / state task list / context projection boundary added to Agent State.
- Reason for prior deferral: original answers covered the stopping and high-level distinction, but not the full correction/escalation chain or state-vs-context projection boundary; this writeback uses Codex-calibrated feedback rather than treating the original answers as fully mastered.
- Boundary: Review notes remain learning calibration, not raw evidence; durable cards keep evidence anchored to existing source notes and label these additions as engineering synthesis.

## [2026-05-12] workflow | review card mandatory writeback constraint

- Updated: [[复习记录索引]], [[LLM Wiki 工作流]], [[templates/概念触发式复习]]
- Rule: 追问卡回答完后，每张卡都必须有写回归宿；成熟边界写回概念卡 / 对比页，不成熟但重要的缺口写入 [[02 问题池]] 或 [[05 Query 写回队列]]。
- Boundary: mandatory writeback does not mean forcing half-understood material into durable concept cards; weak or unstable items must be preserved as questions or pending writeback instead.

## [2026-05-12] topic-update | comparison topic standard retrofit

- Updated: [[RAG 类型对比]], [[Environment Observation 类型对比]], [[Trajectory Trace 类型对比]]
- Change: 按 [[LLM Wiki 工作流#概念对比 / 类比 topic 页写法]] 补齐旧对比 topic 的准入理由、共同问题域、核心区别表、机制差异、非证据类比、现代系统吸收/工程推论边界、选型判断、共同非目标、证据锚点和复习触发。
- Evidence: 旧 topic 的差异判断回链到对应概念卡 `## 证据锚点` 和已有 paper/docs source notes；类比均标注为 learning analogy / 非证据。
- Boundary: 本次只改已有对比类 topic 页；未强行把 [[Agent 主题]]、[[LLM 主题]]、[[RAG 主题]] 等普通入口页套进对比模板，未修改 `raw/`。

## [2026-05-12] topic-update | P1/P2/P3 comparison topic full update

- Added: [[Agent 工程分层对比]], [[Tool 接口层对比]], [[Agent 安全控制点对比]], [[Agent Memory 类型对比]], [[Evaluation 层次对比]], [[Observability Audit 对比]], [[Browser Computer Use 执行栈对比]], [[Context RAG Memory 对比]], [[Retrieval 组件对比]], [[Multi-agent Handoff Protocol 对比]], [[Coding Agent 执行边界对比]], [[LLM 基础结构对比]].
- Updated navigation: [[04 页面目录]], [[05 Query 写回队列]], [[06 Wiki 健康检查]], [[Agent 知识地图]], [[Agent 主题]], [[RAG 主题]], [[LLM 主题]].
- Method: `$team 4:executor` with worker launch args `--model gpt-5.5 -c model_reasoning_effort="xhigh"`; workers used worktrees and leader integrated commits.
- Evidence: comparison pages anchor definitions/differences to existing concept cards and source notes; learning analogies are labeled non-evidence; runtime/product and LLM ability-source P3 groups remain pending rather than forced into weak pages.
- Boundary: worker-2 / worker-3 lifecycle had false terminal failures from read-only probe state, but their artifacts were already integrated into leader HEAD and recorded in mailbox evidence. `raw/` source notes were not modified.

## [2026-05-12] autoresearch-goal | agent framework comparison

- Added source notes: [[AutoGen 官方文档]], [[AgentScope 官方文档]], [[CAMEL-AI 官方文档]], [[Microsoft Agent Framework 官方文档]]; refreshed [[LangGraph 官方文档]].
- Added concept cards: [[AutoGen]], [[AgentScope]], [[CAMEL]], [[LangGraph]], [[Microsoft Agent Framework]].
- Added comparison topic: [[Agent Framework 编排范式对比]].
- Updated navigation: [[资料收集索引]], [[前沿主源清单]], [[04 页面目录]], [[05 Query 写回队列]], [[Agent 知识地图]], [[Agent 主题]], [[Agent Framework]].
- Evidence: 官方 docs / paper/source notes anchor each framework's abstraction center: AutoGen conversation team, AgentScope message-centered platform, CAMEL role-playing/inception prompting, LangGraph state graph runtime, Microsoft Agent Framework agent/workflow SDK and AutoGen + Semantic Kernel successor boundary, LangChain DeepAgents harness on LangGraph.
- Boundary: 本次对比训练的是 framework 编排范式和责任层，不做框架排行榜、性能评测或最新 API 教程；所有框架生态标记为 watch/volatile，需要按官方文档持续复查。

## [2026-05-12] autoresearch-goal | 13-agent-framework full comparison

- Added source notes: [[CrewAI 官方文档]], [[LlamaIndex Agents 官方文档]], [[Pydantic AI 官方文档]], [[Agno 官方文档]], [[Mastra 官方文档]], [[Vercel AI SDK 官方文档]], [[Google ADK 官方文档]].
- Updated source notes: [[OpenAI Agents SDK 文档]], [[LangGraph 官方文档]], [[AutoGen 官方文档]], [[AgentScope 官方文档]], [[CAMEL-AI 官方文档]], [[Microsoft Agent Framework 官方文档]].
- Added comparison topic: [[Agent Framework 全量选型对比 2026-05]].
- Updated navigation: [[资料收集索引]], [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]], [[05 Query 写回队列]], [[Agent Framework]], [[Agent Framework 编排范式对比]].
- Evidence: official docs / first-party source notes for LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, AutoGen, CrewAI, LlamaIndex, Pydantic AI, Agno, Mastra, Vercel AI SDK, Google ADK, AgentScope, and CAMEL checked on 2026-05-12.
- Boundary: this is a volatile framework selection map, not a benchmark, popularity ranking, API tutorial, or production readiness guarantee; concrete SDK APIs, preview status, cloud platform features, and commercial control planes require periodic re-check.

## [2026-05-12] query-writeback | Agent State explicit vs implicit

- Updated: [[Agent State]]
- Writeback: clarified that some orchestration frameworks expose state as a first-class object, while others hide state in message history, session, trace, workflow variables, or caller-owned storage.
- Boundary: absence of a field named `state` is not absence of runtime state; the learning question is who owns it, who updates it, how it is projected into context, and whether it supports recovery.

## [2026-05-12] review | LangGraph special answer workspace

- Added: [[03 LangGraph 专项回答]]
- Updated: [[复习记录索引]]
- Purpose: 基于三步 Tavily 搜索助手案例，创建专项回答页，覆盖 LangGraph state graph、线性流程图、reflection 条件边、循环型应用设计、state / checkpoint / trace 分层和框架选型。
- Boundary: 本页是 review/practice，不是 raw evidence；先保留回答区和写回候选，等待用户作答后再校准并写回 [[LangGraph]]、[[Agent Workflow]]、[[Agent State]]、[[Evaluation]] 或框架对比页。

## [2026-05-12] autoresearch-goal | missing concept cards for full framework comparison

- Added concept cards: [[State Graph Runtime]], [[Provider-first Agent SDK]], [[Crew Orchestration]], [[Role-playing Agent]], [[Data-first Agent Framework]], [[Type-safe Agent SDK]], [[Frontend-first AI Toolkit]], [[Agent Control Plane]].
- Updated topic: [[Agent Framework 全量选型对比 2026-05]] now links the recurring boundary terms to durable concept cards.
- Updated navigation: [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]], [[05 Query 写回队列]].
- Evidence: existing official source notes for LangGraph, OpenAI Agents SDK, CrewAI, CAMEL-AI, LlamaIndex Agents, Pydantic AI, Vercel AI SDK, Mastra, Agno, AgentScope, Google ADK, and the full comparison topic.
- Boundary: this pass creates only high-value framework-selection boundary cards; it does not force every API name, product module, or vendor feature into a concept card.
## [2026-05-12] autoresearch-goal | rag topic supplement

- Updated topic: [[RAG 主题]] now includes learning route, RAG pipeline layers, component/type entrances, boundary judgments, failure diagnosis path, evidence anchors, and review triggers.
- Added concept card: [[Knowledge Graph]] to clarify the graph-structure layer behind GraphRAG / Neo4j.
- Updated navigation: [[Agent 知识地图]], [[04 页面目录]], [[05 Query 写回队列]].
- Evidence: existing RAG concept cards, [[Retrieval 组件对比]], [[RAG 类型对比]], [[Context RAG Memory 对比]], [[Microsoft RAG 官方文档]], [[Neo4j GraphRAG 官方文档]].
- Boundary: this pass supplements the RAG topic map and one high-value missing concept; it does not force every retrieval sub-technique such as query rewrite, citation faithfulness, or access control into standalone concept cards.

## [2026-05-12] autoresearch-goal | rag and llm boundary backlog

- Added concept cards: [[RAG Citation Faithfulness]], [[RAG Access Control]], [[Query Rewrite]], [[Query Planning]], [[Graph Construction Evaluation]], [[Entity Resolution]], [[Token]], [[Context Window]], [[Prompt]], [[Hallucination]].
- Added comparison topics: [[RAG 可靠性与治理对比]], [[Query Rewrite Query Planning Agentic Retrieval 对比]], [[GraphRAG 构图与评估对比]], [[LLM 输入输出基础边界对比]].
- Updated navigation: [[RAG 主题]], [[LLM 主题]], [[Agent 知识地图]], [[04 页面目录]], [[05 Query 写回队列]].
- Evidence: existing concept cards and source notes including [[RAG Evaluation]], [[Microsoft RAG 官方文档]], [[Azure AI Search Agentic Retrieval]], [[Neo4j GraphRAG 官方文档]], [[Attention Is All You Need]], [[OpenAI - A Practical Guide to Building Agents]], [[OWASP LLM Top 10 2025]], and [[OWASP Agentic Applications Top 10]].
- Boundary: this pass closes the recommended RAG / LLM boundary backlog without forcing [[temperature]] or every decoding parameter into a weak card; those remain follow-up candidates in [[LLM 主题]].

## [2026-05-13] query-writeback | LangGraph production project blueprint

- Updated: [[05 Query 写回队列]]
- Writeback: added pending synthesis for a realistic LangGraph-oriented production project blueprint covering multi-source retrieval, tool execution, human approval, checkpoint/resume, trace/eval, deployment, and governance boundaries.
- Boundary: this is queued as a project blueprint candidate rather than a new concept card, because the answer combines multiple existing concepts instead of introducing one stable standalone concept.

## [2026-05-13] autoresearch-goal | Claw Bot / OpenClaw intake decision

- Updated: [[05 Query 写回队列]]
- Decision: Claw Bot is worth tracking only as OpenClaw / Clawbot legacy alias, a volatile concrete Agent gateway / personal-assistant harness source.
- Boundary: do not create a stable [[Claw Bot]] concept card; if ingested later, start from [[OpenClaw Repo]], [[03 前沿追踪]], [[Agent Harness]], and [[Coding Agent 执行边界对比]].

## [2026-05-13] autoresearch-goal | OpenClaw Repo vs Hermes Agent

- Added source note: [[OpenClaw Repo]].
- Added comparison topic: [[OpenClaw Repo vs Hermes Agent]].
- Updated navigation: [[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]], [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]], [[05 Query 写回队列]].
- Evidence: OpenClaw official repo/docs checked on 2026-05-13, including README, Gateway architecture, Agent runtime, Agent workspace, Memory, Skills, Multi-agent routing, Background tasks, Security, Sandboxing, Clawbot alias, and GitHub latest release API; Hermes evidence reused from [[Hermes Agent Repo]] and [[Hermes Agent]].
- Boundary: OpenClaw is recorded as a volatile project/source and compared as a Gateway-first personal assistant harness; no stable [[Claw Bot]] or [[OpenClaw]] concept card was created.

## [2026-05-13] review | LangGraph reflection loop answer

- Updated: [[03 LangGraph 专项回答]]
- Embedded: [[Drawing 2026-05-11 21.47.57.excalidraw 1]]
- Writeback: 整理 LG-B 反思节点答案，明确 `reflect` 是必要新增节点，`rewrite_query` / `regenerate_answer` 可视为对 `understand_query` / `generate_answer` 的可选拆分。
- Boundary: 本次只整理 review 练习答案和图嵌入；暂不更新 [[LangGraph]] / [[Agent Workflow]] 概念卡。

## [2026-05-14] review | LangGraph diagrams embedded

- Updated: [[03 LangGraph 专项回答]]
- Embedded: [[Drawing 2026-05-11 21.47.57.excalidraw]] and [[Drawing 2026-05-11 21.47.57.excalidraw 1]]
- Writeback: 将 LG-A 线性流程图和 LG-B 反思循环图都嵌入对应回答区，并标注为已回答的用户图。
- Boundary: 图是用户学习图 / Excalidraw 作答，不作为 raw evidence；本次只整理 review 页，不更新概念卡。

## [2026-05-14] ingest | Agentproof paper

- Added source note: [[Agentproof - Static Verification of Agent Workflow Graphs]].
- Added concept card: [[Agent Workflow Static Verification]].
- Updated navigation: [[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]], [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]], [[Agent Workflow]], [[LangGraph]].
- Evidence: arXiv abstract/PDF/HTML checked on 2026-05-14, local PDF and extracted text saved under `raw/papers/assets/` and `raw/papers/extracted/`.
- Boundary: recorded Agentproof as a frontier / watch research artifact; the durable concept is not “Agentproof is production standard”, but that explicit agent workflow graphs can be checked for topology-level defects before deployment.

## [2026-05-14] autoresearch-goal | workflow guardrails sources

- Added source notes: [[Workflow Guardrails 主源]], [[Prefect Workflow Control Points]].
- Added concept card: [[Workflow Guardrails]].
- Added mapping topic: [[Workflow Guardrails 与 Prefect 控制点映射]].
- Updated navigation and anchors: [[Guardrails]], [[Agent 安全控制点对比]], [[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]], [[Agent 知识地图]], [[Agent 主题]], [[04 页面目录]].
- Evidence: OpenAI Agents SDK, LangChain, NVIDIA NeMo Guardrails, AWS Bedrock ApplyGuardrail, Guardrails AI, Semantic Kernel filters, Google ADK callbacks, Anthropic Building Effective Agents, IBM Research orchestration page, Agentproof, and Prefect docs checked on 2026-05-14.
- Boundary: recorded the durable idea as guardrail placement at workflow boundaries; concrete SDK/API names remain watch/volatile source details, not standalone stable concept cards.

## [2026-05-14] cleanup | project-context label removed

- Updated: [[Workflow Guardrails 主源]], [[Workflow Guardrails]], [[Workflow Guardrails 与 Prefect 控制点映射]].
- Change: removed a project-specific context label from wiki prose and replaced it with generic “业务项目 / Prefect” wording.
- Boundary: preserved the workflow guardrails engineering mapping while avoiding project-context leakage in durable wiki pages.

## [2026-05-14] autoresearch-goal | LangGraph production project blueprint

- Added topic: [[LangGraph 生产项目蓝图]].
- Updated navigation: [[05 Query 写回队列]], [[04 页面目录]], [[Agent 知识地图]].
- Writeback: closed the 2026-05-13 LangGraph production-project queue item with a blueprint covering business fit, architecture, state schema, nodes/edges, multi-source RAG, tool permissioning, human approval, checkpoint/resume, trace/eval, deployment governance, and failure modes.
- Evidence: [[LangGraph 官方文档]], [[LangGraph GitHub Repo]], [[LangSmith Evaluation and Observability]], [[LangGraph Memory 官方文档]], plus official LangGraph / LangSmith pages checked on 2026-05-14.
- Boundary: this is a production blueprint and engineering synthesis, not a LangGraph API tutorial, framework ranking, or claim that every Agent requires LangGraph.

## [2026-05-14] autoresearch-goal | arXiv Agent paper shortlist 1-8 intake

- Added reading map: `Agent 论文速读清单 2026-05-14` (later removed by cleanup).
- Added source notes: [[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents]], [[How to Interpret Agent Behavior]], [[Rollout Cards - A Reproducibility Standard for Agent Research]], [[Do Androids Dream of Breaking the Game - BenchJack]], [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation]], [[MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning]], [[ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents]], [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]].
- Updated navigation: [[index]], [[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]], [[Agent 主题]], [[Agent 知识地图]], [[04 页面目录]].
- Evidence: arXiv cs.AI recent / abstract pages checked on 2026-05-14; each paper note is `status: seed` and explicitly marks PDF/extracted text as not yet downloaded.
- Boundary: this pass records source evidence and a reading route only; it does not create weak concept cards or treat arXiv preprints as stable production standards.

## [2026-05-14] review | RAG concept-triggered review 04

- Added review note: [[04 RAG 概念触发式复习]].
- Updated navigation: [[复习记录索引]], [[04 页面目录]].
- Review focus: RAG pipeline, vector database boundary, RAG / Memory / Context Engineering distinction, layered failure diagnosis, and upgrade triggers for Agentic RAG / GraphRAG / Corrective RAG.
- Boundary: this is a learning-check page under `reviews/`; it is not raw evidence and does not rewrite the durable [[RAG]] concept card.

## [2026-05-14] workflow | map admission boundary tightened

- Updated project guidance: [[LLM Wiki 工作流]] and `AGENTS.md`.
- Decision: maps are scarce durable navigation/control surfaces, not automatic records for every ingest batch.
- New boundary: do not create or spread "近期论文速读入口", "速读清单", "第 N 梯队清单", or similar batch-specific map entries unless explicitly requested as a durable reading route.
- Preferred homes: batch source notes stay in [[资料收集索引]] or raw notes; unstable questions go to [[02 问题池]]; future write-backs go to [[05 Query 写回队列]]; frontier observations go to [[03 前沿追踪]].

## [2026-05-14] ingest | arXiv Agent paper shortlist second tier

- Added reading map: `Agent 论文第二梯队速读清单 2026-05-14` (later removed by cleanup).
- Added source notes: [[Executable Agentic Memory for GUI Agent]], [[Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems]], [[Cognifold - Always-On Proactive Memory via Cognitive Folding]], [[Harnessing Agentic Evolution]], [[PIVOT - Bridging Planning and Execution in LLM Agents via Trajectory Refinement]], [[OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents]], [[CANTANTE - Optimizing Agentic Systems via Contrastive Credit Attribution]], [[EVOCHAMBER - Test-Time Co-evolution of Multi-Agent System at Individual Team and Population Scales]], [[Position - Assistive Agents Need Accessibility Alignment]], [[RealICU - Do LLM Agents Understand Long-Context ICU Data]], [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations]].
- Updated navigation at the time: [[index]], `Agent 论文速读清单 2026-05-14` (later removed), [[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]], [[Agent 主题]], [[Agent 知识地图]], [[04 页面目录]].
- Evidence: arXiv cs.AI recent / abstract pages checked on 2026-05-14; each paper note is `status: seed` and marks PDF/extracted text as not yet downloaded.
- Boundary: second-tier intake records source evidence and a reading route only; no weak concept cards were created for title terms such as agentic evolution, cognitive folding, or accessibility alignment.

## [2026-05-14] cleanup | remove batch reading maps

- Deleted batch maps: `Agent 论文速读清单 2026-05-14` and `Agent 论文第二梯队速读清单 2026-05-14`.
- Cleaned active navigation: [[index]], [[Agent 主题]], [[Agent 知识地图]], [[04 页面目录]], [[资料收集索引]], [[03 前沿追踪]], and [[前沿主源清单]] no longer promote the batch maps as durable entry points.
- Updated 19 raw paper source notes to point their batch context at [[资料收集索引]] and [[03 前沿追踪]] instead of deleted speed-read maps.
- Boundary: raw paper source notes remain evidence; only the temporary map/control-surface layer was removed.

## [2026-05-14] workflow | paper reading priority rule

- Updated durable rules: `AGENTS.md`, [[LLM Wiki 工作流]], and [[资料收集索引]].
- Added current raw/papers priority tiers: P0 for core/foundation and high-leverage Agent judgment papers, P1 for current Agent engineering frontier papers, P2 for topic-triggered expansion, and P3 for LLM training/alignment background.
- Decision: paper priority is based on learning leverage and boundary yield, not recency or ingest batch order.
- Boundary: this priority lives in existing source/workflow surfaces; no new paper priority map was created.

## [2026-05-14] maintenance | paper source and extracted paths completed

- Updated 37 `source_type: paper` raw notes so `source` points back to each original paper URL.
- Added or verified `pdf` and `extracted` frontmatter for all existing paper notes, including GAIA and SWE-bench source notes outside `raw/papers/`.
- Generated 30 new extracted Markdown files under `raw/papers/extracted/` from the corresponding PDF URLs.
- Updated [[资料收集索引]] paper table to show `source`, `pdf`, and `extracted` for all `source_type: paper` notes, including paper notes outside `raw/papers/`.
- Boundary: extracted files are automatic plain-text evidence helpers only; formulas, tables, figures, footnotes, references, and two-column reading order may be lossy, so precision claims still need PDF page / section checks before being written into concept cards.

## [2026-05-14] autoresearch-goal | Hermes arXiv Agent paper supplement intake

- Added source notes: [[Useful Memories Become Faulty When Continuously Updated by LLMs]], [[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging]], [[Retrieval is Cheap, Show Me the Code - Executable Multi-Hop Reasoning for Retrieval-Augmented Generation]], [[It's not the Language Model, it's the Tool - Deterministic Mediation for Scientific Workflows]], [[Beyond Cooperative Simulators - Generating Realistic User Personas for Robust Evaluation of LLM Agents]], [[MMSkills - Towards Multimodal Skills for General Visual Agents]], [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents]], [[ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles]], [[Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning]], [[Position - Agentic AI System Is a Foreseeable Pathway to AGI]].
- Reused existing source notes in the same source-index batch: [[Harnessing Agentic Evolution]], [[How to Interpret Agent Behavior]], [[Cognifold - Always-On Proactive Memory via Cognitive Folding]], [[MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning]], [[RealICU - Do LLM Agents Understand Long-Context ICU Data]].
- Updated navigation / priority surfaces: [[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]], [[04 页面目录]].
- Evidence: user-provided Hermes list plus official arXiv abstract/API metadata checked on 2026-05-14; new paper notes are `status: seed`, with remote PDF links and no local extracted text yet.
- Boundary: per map admission rules, no new batch speed-read map was kept; this pass records source evidence, priority placement, and frontier observations only, without creating weak concept cards for title terms.

## [2026-05-15] maintenance | paper PDFs downloaded and extracted completed

- Downloaded 40 missing paper PDFs into `raw/papers/assets/` and updated paper source-note `pdf` fields to local relative paths.
- Generated 10 missing extracted Markdown files under `raw/papers/extracted/`.
- Normalized 10 new paper notes from quoted `type/source_type` values to `type: source` and `source_type: paper` so `scripts/paper_source_audit.py` can verify them.
- Updated [[资料收集索引]] with the current paper-localization status.
- Verification: 47 / 47 `source_type: paper` notes now resolve to local PDFs and extracted Markdown files; `scripts/paper_source_audit.py --root 'agentic learning/raw/papers'` passes.
- Boundary: local PDFs and extracted text improve evidence availability, but extracted text remains lossy for figures, formulas, tables, footnotes, references, and two-column order.

## [2026-05-15] query | vector database selection boundary queued

- Added pending write-back: vector database product/category selection boundary for Agent/RAG development.
- Target pages: [[Vector Database]], [[Retrieval 组件对比]], [[RAG 主题]], [[Context RAG Memory 对比]].
- Boundary: record category-level selection heuristics and interview framing; do not create stable concept cards for every vendor (Qdrant, Milvus, Pinecone, etc.) without official docs or project-practice source notes.

## [2026-05-15] wiki | vector database selection boundary recorded

- Updated concept: [[Vector Database]] with Agent / RAG 选型边界 covering Chroma, FAISS, PostgreSQL + pgvector, Qdrant, Milvus, Weaviate, Pinecone, Elasticsearch/OpenSearch, and Neo4j.
- Updated topics: [[Retrieval 组件对比]], [[RAG 主题]], [[Context RAG Memory 对比]].
- Updated source links: [[Agent 工程基础设施主源#RAG / 检索基础设施]] now includes official/project docs for the added vector/search/graph options checked on 2026-05-15.
- Writeback: closed the 2026-05-15 query queue item as done.
- Boundary: this is a category-level selection heuristic and interview framing, not a vendor benchmark or permanent product ranking; Agent 长期记忆 should separate semantic recall from deterministic state, permissions, preferences, config, and audit records.

## [2026-05-15] autoresearch-goal | Top-K concept card recorded

- Added concept: [[Top-K]] as a lightweight RAG / retrieval / decoding-boundary card.
- Updated navigation: [[01 术语表]], [[RAG 主题]], [[Agent 知识地图]], [[04 页面目录]], and [[LLM 主题]].
- Writeback: closed the Top-K query item in [[05 Query 写回队列]] as done.
- Evidence: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#必读块 2：Figure 1 / retriever + generator 流程]], [[Retriever#概念详解]], [[Vector Database#概念详解]], [[Reranking#概念详解]], [[RAG Evaluation#概念详解]], and [[Self-RAG - Learning to Retrieve Generate and Critique#必读块 1：Abstract / adaptive retrieval]].
- Boundary: Top-K is recorded as a stable selection rule and confusion boundary, not a fixed tuning recommendation; retrieval Top-K and decoding top-k are adjacent terms but live in different layers.

## [2026-05-15] wiki | 常用向量数据库对比录入

- Added topic: [[常用向量数据库对比]].
- Covered: Chroma, FAISS, PostgreSQL + pgvector, Qdrant, Milvus, Weaviate, Pinecone, Elasticsearch/OpenSearch vector search, and Neo4j vector / GraphRAG ecosystem.
- Updated navigation: [[Vector Database]], [[Retrieval 组件对比]], [[RAG 主题]], [[Agent 知识地图]], [[04 页面目录]].
- Evidence: official/project docs linked through [[Agent 工程基础设施主源#RAG / 检索基础设施]] and checked on 2026-05-15.
- Boundary: this is a category-level learning and selection page, not a benchmark or permanent product ranking; 产品能力、API、价格、部署方式和 hybrid search support remain watch-level details.

## [2026-05-15] maintenance | request-meta wording filtered

- Cleaned request-side intake wording from existing durable notes and queued write-backs.
- Updated guardrails: `AGENTS.md` and [[LLM Wiki 工作流]] now treat 收录价值判断、执行请求、项目名、任务名和临时 side context as operation metadata rather than wiki knowledge.
- Boundary: durable pages should preserve learning value, evidence, and concept boundaries; user prompt scaffolding belongs in the current reply or, at most, this maintenance log.

## [2026-05-15] autoresearch-goal | Hybrid Search concept strengthened

- Updated concept: [[Hybrid Search]].
- Added clearer sparse/dense retrieval framing, BM25/fulltext boundary, RRF as a common fusion idea, and the distinction from [[Reranking]], [[Agentic Retrieval]], [[GraphRAG]], and [[RAG Evaluation]].
- Evidence: [[Agent 工程基础设施主源#RAG / 检索基础设施]], [[RAG 类型对比#一张表先抓住]], [[Microsoft RAG 官方文档#一句话]], [[Azure Search OpenAI Demo Repo#一句话]], and [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第三层：召回优化]].
- Boundary: keep Hybrid Search as a stable retrieval-quality concept; keep product defaults, fusion weights, API details, and benchmark claims under watch-level review.

## [2026-05-15] ralph | paper source evidence excerpts completed

- Upgraded 32 paper source notes (30 under `raw/papers/` plus [[GAIA Benchmark]] and [[SWE-bench]] under `raw/articles/`) whose required-reading blocks still had keyword-only `原文短摘`, arXiv-placeholder wording, or `待精读正文后补` despite local extracted Markdown being available.
- Representative repaired card: [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation]] now anchors Lucky Pass, AgentLens-Bench, and PTA reference to concrete extracted Page 1 short excerpts instead of one-word keywords.
- Added a stricter local quality audit check for this maintenance pass: `scripts/paper_source_quality_audit.py` flags placeholder wording, keyword-only excerpts, and overlong/too-short blockquotes.
- Verification: `scripts/paper_source_audit.py --root 'agentic learning/raw/papers'` and `scripts/paper_source_quality_audit.py --root 'agentic learning/raw/papers'` pass across the localized paper set: structural audit for 45 `raw/papers/` notes and quality audit for 47 `source_type: paper` notes under `raw/`.
- Boundary: this pass improves raw/source evidence cards only. It does not claim full paper精读, does not create weak concept cards, and still requires PDF section/table/figure checks before moving numerical claims or method details into durable `wiki/concepts/` pages.

## [2026-05-15] autoresearch-goal | parallel search and explicit merging topic added

- Added topic: [[Parallel Search and Explicit Merging 检索模式]].
- Updated navigation: [[RAG 主题]], [[Query Rewrite Query Planning Agentic Retrieval 对比]], [[Agent 知识地图]], and [[04 页面目录]].
- Evidence: [[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging#论文主张]], [[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging#方法 / 机制]], extracted Page 1 / Abstract, Page 4 / Method, Page 6-8 / Experiments, and Page 18 / Limitations.
- Boundary: this page treats MultiSearch as a frontier/watch evidence source for retrieval-during-reasoning, not as a stable default RAG architecture; QA benchmark and static-corpus limits remain explicit.

## [2026-05-15] wiki | TF-IDF and sparse retrieval boundary clarified

- Updated [[Hybrid Search]] to state that sparse retrieval is the broader term, BM25 is the common modern sparse-retrieval representative, and TF-IDF is an older term-weighting method rather than a strict synonym.
- Evidence: [[Hybrid Search#概念详解]], [[Hybrid Search#边界细节]], and [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第二路：BM25 关键词检索（Sparse Retrieval）]].
- Boundary: this clarifies a terminology edge case for RAG study notes; it does not create a new standalone concept card for sparse retrieval or TF-IDF.

## [2026-05-15] ralph | source-note intake metadata cleanup

- Removed per-paper intake provenance paragraphs from paper source notes, keeping only source evidence and learning-value framing.
- Neutralized project-specific supplement/list wording into stable “arXiv Agent 论文补充批次” navigation in [[资料收集索引]], [[前沿主源清单]], and [[03 前沿追踪]].
- Cleaned remaining source-note template wording into neutral learning prompts about concept cards, topics, and question-pool writeback.
- Preserved true [[Hermes Agent Repo]] / [[Hermes Agent]] references where Hermes is the actual source/project topic.
- Verification: `scripts/paper_source_audit.py --root 'agentic learning/raw/papers'` PASS; `scripts/paper_source_quality_audit.py --root 'agentic learning/raw'` PASS; targeted request-meta grep returned no matches; `git diff --check` PASS.
- Boundary: this cleanup changes source-note and navigation wording only; it does not claim full paper精读 and does not create weak concept cards.

## [2026-05-15] maintenance | hard rule added for intake/provenance text

- Added a hard rule to [[LLM Wiki 工作流]] and `AGENTS.md`: any paragraph whose main job is to say who supplied a source, which batch it belongs to, where it is indexed, or which frontier judgment to follow must be deleted from source-note/topic/concept正文 instead of rewritten in place.
- Boundary: preserve only neutral evidence, learning value, and write-back metadata; keep request-side provenance out of durable knowledge pages.

## [2026-05-15] autoresearch-goal | TF-IDF concept recorded

- Added source note: [[scikit-learn TF-IDF 文档]].
- Added concept: [[TF-IDF]] as a sparse retrieval / text vectorization boundary card.
- Updated navigation: [[Embedding]], [[Hybrid Search]], [[Retrieval 组件对比]], [[RAG 主题]], [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], and [[Agent 工程基础设施主源]].
- Evidence: scikit-learn TF-IDF user guide and `TfidfVectorizer` API reference checked on 2026-05-15.
- Boundary: TF-IDF is recorded as a foundation concept for sparse lexical vectors and hybrid search, not as dense embedding or a default production RAG ranking algorithm.
