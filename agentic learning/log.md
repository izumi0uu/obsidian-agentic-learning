---
type: log
topic:
  - obsidian
  - llm-wiki
status: active
created: 2026-05-05
updated: 2026-05-18
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

## [2026-05-15] wiki | sparse retrieval and BM25 concept cards recorded

- Added concepts: [[Sparse Retrieval]] and [[BM25]] as RAG retrieval boundary cards.
- Updated navigation: [[Hybrid Search]], [[TF-IDF]], [[Retrieval 组件对比]], [[RAG 主题]], [[Agent 知识地图]], and [[04 页面目录]].
- Evidence: [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#关键词检索：字面匹配，靠统计]], [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第二路：BM25 关键词检索（Sparse Retrieval）]], and [[raw/repos/xiaolinnote/questions/023 ai rag 10. 你使用 RAG 给大模型一个输入，系统是怎样的工作流程？#第三步：向量检索（ANN 搜索）+ 多路召回]].
- Boundary: [[TF-IDF]] is the foundation term-weighting intuition, [[BM25]] is the common sparse retrieval representative, [[Sparse Retrieval]] is the broader lexical retrieval family, and [[Hybrid Search]] is the fusion strategy that combines sparse and dense signals.

## [2026-05-16] team | 面试题正文概念链接审计脚本补齐

- Added deterministic helper: `scripts/interview_question_concept_links.py` with dry-run/apply/report/backlog support and conservative protected-region handling for frontmatter、代码块、URL、已有链接、source metadata 与 `## 相关知识 wiki`。
- Added alias map: `scripts/interview_question_concept_aliases.json` for high-confidence Agent / RAG / tool / memory / evaluation terms.
- Created backlog page: [[08 面试题概念卡待补充]] from the approved template; current audit found no unresolved related-link targets, so it remains a candidate intake page rather than a concept explanation page.
- Verification: script self-test PASS; full dry-run and post-apply audit both scanned 757 question pages（120 xiaolinnote + 637 agent_java_offer）, found 757 related sections, 0 missing targets, 0 protected-region violations, and 0 request-meta hits; `git diff --check` PASS.
- Boundary: this pass adds the missing reproducible audit/control surface for the team run. It does not create weak concept cards, does not rewrite interview answers, and leaves skipped/no-match backend/Git/Linux/SQL pages as conservative non-links unless future concept scope is explicitly expanded.

## [2026-05-16] team | 面试题概念内联链接最终验证修正

- Re-ran the interview-question inline-link helper after team execution and tightened alias boundaries for `工作流程` and generic `成功率`.
- Cleaned obvious false-friend `related` entries in both frontmatter and `## 相关知识 wiki` where backend terms had been mapped to Agent concepts, including Netty Reactor vs [[ReAct]], JVM/off-heap memory vs [[Memory]], and `volatile`/AQS backend state vs RAG/Agent links.
- Verification target: post-apply dry-run remains 757 scanned pages, 757 related sections, 0 would-modify pages, 0 missing concept candidates, and 0 protected-region violations.
- Boundary: this is a narrow semantic cleanup for the interview-question linking exception; it does not create backend concept cards or broaden raw-page synthesis rules.

## [2026-05-16] wiki | 概念层级字段规范阶段 1 落地

- 更新 [[字段规范]]：新增概念关系字段 `up` / `relations` / `children` 的边界，明确 `up` 只表示严格上位概念，`relations` 承载代表、思想来源、组合与高混淆相关关系。
- 更新 [[概念卡]] 模板：frontmatter 增加 `up` 与 `relations`，并加入不要为了插件图谱强行加 `up` 的提示。
- 更新 [[插件配置]]：记录 Abstract Folder 使用 `up`、Breadcrumbs 使用默认 `up/down` 并 rebuild graph、Juggl 只作为 Breadcrumbs/Obsidian 图的可视化层。
- 示例边界：用 BM25 / TF-IDF / Sparse Retrieval / Hybrid Search 说明 taxonomy、代表关系、思想来源和组合关系的区别。
- Boundary: 本阶段只改规范、模板和插件配置说明；不移动物理文件夹，不新增临时 map，不批量修改旧概念卡。

## [2026-05-16] maintenance | bilingual terminology audit rule recorded

- Added project-level hard rule in `AGENTS.md` requiring a Chinese/English terminology gate before durable concept links, concept cards, raw-question links, alias-map changes, or terminology-heavy topic updates.
- Updated [[LLM Wiki 工作流]] with the bilingual terminology audit workflow: trigger conditions, audit table, canonical-name priority, backlog/forbidden-mapping states, landing synchronization, false-friend examples, and validation commands.
- Updated [[字段规范]] and [[概念卡]] template with `aliases` guidance for concept cards, including the boundary that aliases are same-concept names only and do not replace `scripts/interview_question_concept_aliases.json` for interview auto-linking.
- Boundary: this records the rule and template/schema guidance only. It does not complete the full bilingual terminology audit or create new concept cards for pending terms such as Multi-Route Retrieval, RRF, or Context Recall.

## [2026-05-16] maintenance | hybrid search MCP retrieval default recorded

- Added project-level retrieval tooling guidance to `AGENTS.md`: prefer `obsidian_status` / `obsidian_search` / `obsidian_read` for vault query and maintenance before broad filesystem search.
- Updated [[LLM Wiki 工作流]] with the same retrieval order and the boundary that semantic recall does not collapse the `raw/`、`wiki/`、`maps/` knowledge layers.
- Updated the local `obsidian-llm-wiki` skill so future skill-triggered wiki work uses the hybrid search MCP tools by default when available.
- Boundary: this records retrieval behavior only. Runtime details such as proxy settings, model cache paths, MCP install commands, and local Codex config remain outside durable wiki content.

## [2026-05-16] wiki | multi-route retrieval concept recorded

- Added concept: [[Multi-Route Retrieval]] as the broader RAG multi-route recall pattern behind dense, sparse/BM25, multi-query, graph, filter, or multi-retriever candidate recall.
- Updated navigation and comparison surfaces: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]], [[Hybrid Search]], [[Retrieval 组件对比]], [[RAG 主题]], [[Agent 知识地图]], [[04 页面目录]], and [[08 面试题概念卡待补充]].
- Updated interview alias map so `多路召回` and `多路检索` resolve to [[Multi-Route Retrieval]] instead of being collapsed into [[Hybrid Search]].
- Synchronized the new concept mention backlink-sweep rule into `AGENTS.md`, [[LLM Wiki 工作流]], [[概念卡]], and the local `obsidian-llm-wiki` skill so future concept cards trigger a project-wide mention check.
- Evidence: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#什么是多路召回？]], its Dense Retrieval / BM25 / multi Query / RRF sections, and [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#混合检索：两者结合]].
- Boundary: this records Multi-Route Retrieval as broader than [[Hybrid Search]] and separate from [[Reranking]]; RRF, Multi-Query Retrieval, and Dense Retrieval remain candidate concepts unless later evidence justifies separate cards.

## [2026-05-16] maintenance | new concept mention backlink sweep rule recorded

- Added a project-level hard rule in `AGENTS.md`: after creating a new concept card or accepting a major alias/canonical name, scan the vault for existing mentions and add correct Obsidian references or record why a hit remains unlinked.
- Updated [[LLM Wiki 工作流]] with the new concept backlink sweep workflow: triggers, search scope, hit classification, raw-source boundary, two-way synchronization, and validation commands.
- Updated [[概念卡]] template with a reminder that new cards and important aliases must trigger a backlink sweep before completion.
- Boundary: this records the future rule only. It does not run a full backlink sweep for existing concepts in this pass.

## [2026-05-16] maintenance | hybrid search truncated-read rule recorded

- Updated `AGENTS.md`, [[LLM Wiki 工作流]], and the local `obsidian-llm-wiki` skill with a truncated-read rule for hybrid search MCP usage.
- Rule: for synthesis, concept comparison, wiki edits, or evidence claims, if `obsidian_read` returns truncated content, re-read the core note individually with a larger `snippet_length` or without truncation before making claims.
- Boundary: this is a usage rule for MCP reads, not a runtime configuration or model/cache setting.

## [2026-05-16] wiki | bilingual terminology audit implemented

- Promoted high-confidence bilingual RAG terms from [[08 面试题概念卡待补充]] into concept cards: [[Dense Retrieval]], [[Reciprocal Rank Fusion]], [[Multi-Query Retrieval]], [[Cross-Encoder]], [[Context Recall]], [[Context Precision]], and [[Parent-Child Chunking]].
- Fixed canonical mapping: `向量检索` now maps to [[Dense Retrieval]] rather than the broader [[Retriever]] component; `多路召回` remains [[Multi-Route Retrieval]] rather than [[Hybrid Search]].
- Updated `scripts/interview_question_concept_aliases.json`, related raw-question pages, and RAG navigation surfaces so Chinese terms link to stable English canonical cards while ambiguous metrics/strategies remain in backlog.
- Backlog boundary: Bi-encoder, Hit@K, MRR, Faithfulness/Groundedness, and HyDE remain pending candidates; they were not promoted because this pass lacked enough scope to define separate durable cards without over-splitting.
- Verification: `python3 scripts/interview_question_concept_links.py --self-test` PASS; dry-run scanned 757 question pages with 0 would-modify pages, 0 missing candidates, and 0 protected-region violations; false-mapping grep for the Retriever-as-向量检索 and HybridSearch-as-多路召回 patterns returned no matches; added-link target audit PASS; changed-file frontmatter YAML parse PASS; `git diff --check` PASS.

## [2026-05-16] wiki | 概念层级插件阶段 2 配置

- 安装并启用本地 Obsidian 插件：Abstract Folder `1.14.0`、Breadcrumbs `4.9.5`、Juggl `1.5.0`，并写入 `agentic learning/.obsidian/community-plugins.json`。
- 配置 Abstract Folder：`propertyName` / `parentPropertyNames` 使用 `up`，`childrenPropertyName` / `childrenPropertyNames` 保持 `children`。
- 更新 [[插件配置]]：记录三款插件的当前安装版本、启用状态和本 vault 的使用边界。
- Boundary: 本阶段只配置插件显示层；不运行物理文件夹转换，不批量修改概念卡，不把 `relations` 强行镜像成 Breadcrumbs edge fields。

## [2026-05-16] wiki | 概念层级插件阶段 3 样板卡落地

- 在代表性检索概念卡上写入机器可读层级字段：[[BM25]] 增加 `up: [[Sparse Retrieval]]` 与 `representative_of` / `based_on_intuition` / `related_to`，[[Sparse Retrieval]] 增加 `up: [[Retriever]]` 与 `related_to` / `composed_into`，[[Hybrid Search]] 增加 `up: [[Retriever]]` 与 `composes_with` / `related_to`。
- 保持 [[TF-IDF]] 作为基础词项表示卡，不把它错误挂成严格 taxonomy；它仍通过正文和既有 related 边界为 BM25 / sparse retrieval 提供学习直觉。
- 验证：frontmatter YAML 解析 PASS；`git diff --check` PASS；三张卡都只新增了预期的 `up` / `relations` 字段，没有把 `TF-IDF` 强行改成子概念。
- Boundary: 本阶段只做代表性样板卡，不把全库检索概念一次性批量重写。

## [2026-05-16] wiki | Abstract Folder 非概念文件排除

- 更新 Abstract Folder 本地配置：`excludedPaths` 排除 `raw/`、`maps/`、`reviews/`、`templates/`、`Excalidraw/`、`assets/`、`wiki/topics/`、`wiki/projects/`、`.obsidian/`、`.trash/`、`index.md`、`log.md`。
- 更新 [[插件配置]]：记录排除策略、路径前缀匹配语义，以及“只影响虚拟树显示，不移动或删除文件”的边界。
- Boundary: 第一版虚拟文件夹只作为 `wiki/concepts/` 概念 taxonomy 浏览器；面试题、raw 来源、map 控制面、review、topic、project、入口页和日志不进入 Abstract Folder 概念树。

## [2026-05-16] wiki | Abstract Folder 配置回写覆盖修复

- 发现外部直接编辑 `.obsidian/plugins/abstract-folder/data.json` 时，运行中的 Obsidian 会把插件内存中的旧设置回写成空数组，导致 `excludedPaths` 看起来“没生效”。
- 处理方式：先退出 Obsidian，再把 `excludedPaths` 写回 `data.json`，然后重新打开 vault，确认配置稳定保留。
- 更新 [[插件配置]]：补充“本地插件配置外部改写的回写覆盖风险”以及推荐的生效方式。
- Boundary: 这是插件运行时状态与磁盘文件之间的覆盖问题，不是 `excludedPaths` 语法本身的问题。

## [2026-05-16] wiki | Juggl 大库局部视图边界补强

- 更新 [[插件配置]]：明确 Juggl 在卡片很多的库里只用于局部子树和短时探索，不承担全库主视图。
- 同步保留前一版边界：Abstract Folder / Breadcrumbs 负责主层级，`up` / `relations` 负责语义；Juggl 只是看图工具。
- Boundary: 这次只补强文档边界，不改 Juggl 插件本身，也不新增全库图谱设置。

## [2026-05-16] wiki | RAG 检索家族边界同步

- 同步更新相关检索概念卡与主题页：[[Dense Retrieval]]、[[Sparse Retrieval]]、[[BM25]]、[[Hybrid Search]]、[[Query Rewrite]]、[[RAG Evaluation]]、[[RAG 主题]]、[[Retrieval 组件对比]]，以及一条 RAG 面试题 raw 关联。
- 增补边界与别名：`Bi-encoder / 双塔` 归入 [[Dense Retrieval]] 的常见实现说明；`HyDE` / `Step-back Prompting` 归入 [[Query Rewrite]] 的子策略；[[RAG Evaluation]] 细化为检索排序指标、上下文、生成、引用与答案质量的分层评估。
- Boundary: 这些同步是为了让 retrieval / evaluation / rewrite 关系更可读，不把它们误压成单一父子树；仍由 `up` + `relations` 承担严格层级与关系解释。

## [2026-05-16] wiki | Juggl 从日常启用中移除

- 将 `agentic learning/.obsidian/community-plugins.json` 中的 `juggl` 移除，改为按需临时启用，而不是日常工作流组件。
- 更新 [[插件配置]]：明确 Juggl 在卡片很多的库里即使临时启用也只适合极小局部，不承担全库主视图；当前默认停用。
- Boundary: 这是性能与工作流边界收缩，不影响 Abstract Folder / Breadcrumbs 作为主层级方案。

## [2026-05-16] wiki | bilingual terminology audit second pass

- 完成 vault-wide 中英术语二轮扫描：概念卡 130 张、alias map 87 项、面试题 bilingual pattern 942 次 / 697 个唯一噪声候选，审计报告写入项目内维护报告目录。
- 安全补充同义 alias：[[Agent]]、[[RAG]]、[[Embedding]]、[[Tool Calling]]、[[MCP]]；同步 `scripts/interview_question_concept_aliases.json` 中的 `Query Rewriting`、`Rerank`、`精排`、`Rerank 精排`，并把 `Tools` 从 [[Tool Calling]] 操作匹配改到 [[Tool Use]]。
- 修正 alias 边界：把 Bi-encoder、HyDE、Step-back、Hit@K、MRR、nDCG、Faithfulness、Groundedness、Answer Relevancy 从 frontmatter aliases 中排除，保留在 [[Dense Retrieval]]、[[Query Rewrite]]、[[RAG Evaluation]] 的正文边界 / 指标家族说明里。
- 更新 [[08 面试题概念卡待补充]]：将 Bi-encoder、RAG ranking metrics、generation metrics、HyDE / Step-back 标为 folded，并新增 Chunking 子策略候选家族。
- 自动链接验证：脚本新增/修正 `[[Reranking|Rerank]]`、`[[Tool Use|Tools]]`、`[[Tool Calling|调工具]]`、`[[Tool Calling|Function Calling]]`；后续 dry-run 回到 0 would-modify、0 missing candidates、0 protected-region violations。
- Boundary: 本轮没有把所有 alias map 词条批量写入概念卡 frontmatter；generic/broad/false-friend 风险项先保留在审计报告和 backlog，避免把“相关”误写成“同义”。

## [2026-05-16] maintenance | bilingual rules kept abstract

- 收紧项目规则的表达层级：在 `AGENTS.md`、[[LLM Wiki 工作流]]、[[字段规范]] 中，把术语对齐规则保留为方法论与边界判断，不把细分 agent / RAG 术语写成规则词表。
- 具体词例、子策略、指标和代表算法继续留在概念卡正文、`relations`、[[08 面试题概念卡待补充]]、审计报告和 raw 证据页中；规则只负责说明“如何判定、如何落地、如何验证”。
- Boundary: 这是控制面抽象瘦身，不是放弃术语边界；同义词、子策略、指标和 false friend 仍然要在知识层单独判断。

## [2026-05-16] wiki | Abstract Folder 英文显示优先

- 将 `.obsidian/plugins/abstract-folder/data.json` 的 `displayNameOrder` 改为 `title -> basename`，并把 `showAliases` 关掉，让 Abstract Folder 不再把 `aliases` 当默认显示名来源。
- 为两张遗留中文概念卡补充英文 `title`：[[OMX $ 指令]] → `OMX $ Commands`，[[双链]] → `Bidirectional Links`，从而让 Abstract Folder 概念树显示全量落到英文。
- 更新 [[插件配置]]：补充显示名策略说明，强调 `aliases` 只保留给搜索和术语对齐；少数旧卡如果需要英文显示名，可以再补 `title`。
- Boundary: 这次只改虚拟树的显示优先级，不改概念卡语义，不批量重命名文件。

## [2026-05-16] maintenance | 项目规则控制面同步

- Updated: `AGENTS.md`, [[LLM Wiki 工作流]], [[06 Wiki 健康检查]], [[04 页面目录]], [[index]], [[08 面试题概念卡待补充]], [[08 面试题概念链接待办]], `agentic learning/templates/`。
- Evidence: concept card audit 当前为 130 张概念卡 / 27 needs action；comparison topic audit 当前为 23 张对比 topic / 6 needs action；paper source audit PASS；面试题链接 self-test PASS；dry-run would modify 0。
- Boundary: 本轮只同步规则控制面、导航入口、审计命令和模板日期，不批量修复 27 张概念卡或 6 张对比页；`scripts/README.md` 已包含 audit bundle 说明但本轮没有产生 tracked diff；旧健康检查数字保留为历史快照，不再作为当前状态。

## [2026-05-16] wiki | Juggl 退役后层级方案同步

- 更新 [[字段规范]] 与 [[插件配置]]：后续概念层级浏览只以 Abstract Folder + Breadcrumbs 为主，不再把 Juggl 作为安装、配置、可视化或验收依赖。
- 明确 Juggl 因性能问题退出后续方案；`relations` 的镜像字段只在未来 Breadcrumbs 侧确有稳定可视化需求时再评估。
- Boundary: 这是层级方案和控制面同步，不重启插件安装，不移动物理文件夹，不批量改概念卡，也不删除可能残留的本地 Juggl 插件目录。

## [2026-05-16] maintenance | 概念关系临时图评估

- 评估 `agentic learning/wiki/concepts/` 下 130 张 `type: concept` 概念卡，并生成项目内临时关系文件：`reports/concept-card-relation-map/concept-relations-temp.md` 与 `reports/concept-card-relation-map/concept-relations-temp.json`。
- 统计：现有 `up` taxonomy 边 11 条，`relations` typed relation 边 25 条，frontmatter `related` 边 702 条，body wikilink 边 241 条；119 张卡暂未写 `up`；core orphan 0；weakly connected 1；dangling core targets 23；候选 review signal 123 条，其中 taxonomy_candidate 36 条、topic_family_review 87 条。
- Boundary: 这是临时评估图，不自动写回概念卡；`topic_family_review` 只用于分组复核，不是 parent；每条候选 `up` 都需要单独审查后才能落入 `relations` / `up`。

## [2026-05-16] wiki | sqlite-vec 选型边界写回

- 更新 [[Vector Database]]：把 sqlite-vec 归入 “SQLite 嵌入式扩展 / 本地单文件向量检索” 边界，而不是单独建弱概念卡或把它当作独立向量数据库服务。
- 补充区别：sqlite-vec 负责 SQLite 内的向量存储与 KNN 查询；embedding 生成、权限、多用户隔离、hybrid search、rerank 和评测仍需外部设计；sqlite-vec、sqlite-vss、SQLite 官方 Vec1 不应混成同一个项目。
- Boundary: 本轮是单卡边界补强，不更新 alias map、面试题链接脚本、模板或项目规则控制面。

## [2026-05-16] maintenance | 审计队列 27+6 一次性批量维护

- 用户明确授权后，一次性处理健康检查剩余队列：27 张概念卡与 6 张 comparison topic。
- 概念卡修复：补强 `## 概念详解` 的学习解释密度，并为缺口卡补 `Evidence type:` / `Boundary:`，不改 canonical name、aliases、alias map，也不新增概念卡。
- 对比页修复：补必备 comparison section、学习类比（非证据）、现代系统吸收边界、证据类型 / 置信度 / 边界标记，以及核心区别表中的可比较双链锚点。
- 控制面：更新 [[06 Wiki 健康检查]] 当前状态和本轮维护记录；未新增 27+6 相关规则，`AGENTS.md`、[[字段规范]] 和模板未改。[[LLM Wiki 工作流]] 若有概念关系门禁 diff，属于独立关系建模维护，不计入本轮验收。
- Boundary: 这是一次用户授权的系统性批量维护，不代表后续可以默认批量重写旧卡；本轮没有触碰 raw source，也没有处理独立 Juggl 退役分支。

## [2026-05-16] maintenance | 概念关系台账与小批量写回流水线

- 实现 `scripts/concept_taxonomy/` 与 `reports/concept-card-relation-map/` 受控流水线：`build.py` 全量生成临时图，`decide.py` 生成逐条候选关系台账，`writeback.py` 提供 dry-run 与带 limit 的小批量 apply，并拒绝无界 apply；`validate.py` 验证台账、写回报告和 Abstract Folder / Breadcrumbs 兼容性。
- 生成 pre-writeback 临时图快照：130 张概念卡、11 条现有 `up`、123 条候选 review signal；台账判定为 27 条 accepted taxonomy、8 条 rejected taxonomy、1 条 deferred taxonomy、64 条 adjacency only、23 条 duplicate signal。
- 首批只给高置信子卡新增顶层 `up`：[[AgentScope]]、[[Agentic RAG]]、[[Agentic Retrieval]]、[[Audit Log]]、[[AutoGen]]、[[CAMEL]]、[[Corrective RAG]]、[[Crew Orchestration]]、[[Episodic Memory]]、[[GraphRAG]]、[[LangChain DeepAgents]]、[[LangGraph]]。
- 同步 [[LLM Wiki 工作流]]：把“临时图 → 台账 → dry-run → 小批量写回 → 插件验证”固化为后续关系写回门禁。
- 验证：无界 apply 按预期拒绝；`python3 scripts/concept_taxonomy/validate.py` PASS；plugin 兼容报告显示 130 张概念卡 / 23 条 `up` 检查、0 problems；`git diff --check` PASS。
- Boundary: 本轮没有把 `topic_family_review` 写入 `up`，没有全量盲改 130 张概念卡，没有新增 `down` / 常规 `children` / Juggl 镜像字段。

## [2026-05-16] maintenance | 检索关系边界守卫修正

- 修正概念关系流水线的非层级边界：将 TF-IDF / BM25 / Sparse Retrieval / Multi-Route Retrieval 这类“基础表示 / 代表算法 / 召回路线 / 编排策略”链条列为 forbidden-as-up 守卫，避免被候选台账或 dry-run/apply 误写入 `up`。
- 更新 `scripts/concept_taxonomy/boundary_policy.py`、`decide.py`、`writeback.py`、`validate.py`：共享 guardrail policy，台账输出 `non_taxonomy_boundary_policy`，写回拒绝 forbidden pair，验证检查 dry-run、apply report 和现有概念卡里都没有 forbidden `up`。
- 小范围补强 [[TF-IDF]] 与 [[Sparse Retrieval]] 的 typed `relations`：TF-IDF `foundational_for` Sparse Retrieval；Sparse Retrieval `composed_into` Multi-Route Retrieval，明确这是基础/路线/组合关系而不是 taxonomy。
- 同步 [[LLM Wiki 工作流]]、[[字段规范]] 和概念卡模板的边界说明。
- 验证：`python3 -m py_compile scripts/concept_taxonomy/*.py` PASS；policy count 14/14；`build.py` / `decide.py` / `writeback.py --dry-run` / `validate.py` PASS；`git diff --check` PASS。
- Boundary: 本轮没有执行第二批 apply，没有新增 `down` / `children` / Juggl 镜像字段，也没有全量重写概念卡；只改两张被点名的检索边界卡与系统性控制面。

## [2026-05-16] maintenance | 剩余 accepted 关系候选二次审查

- 审查 `reports/concept-card-relation-map/writeback-dry-run.*` 中上一轮剩余 15 条 accepted candidates；本轮只审查，不执行第二批 apply。
- 保留 13 条 strict taxonomy 候选，当前 dry-run 为 13 planned / 13 ready。
- 将 2 条从 accepted 降级为 reject taxonomy：`OpenTelemetry GenAI -> Observability`（语义约定/标准化层支撑 observability，不是 observability 子类）和 `State Graph Runtime -> Agent Workflow`（runtime 执行并持久化 workflow，不是 workflow 子类）。
- 更新 `scripts/concept_taxonomy/decide.py` 并生成 `remaining-accepted-candidates-review.md/json`；同步 [[LLM Wiki 工作流]] 与 [[字段规范]]，把“accepted apply 前仍需二次复核”和“标准化/支撑/执行不等于 taxonomy”写成规则。
- 验证：`python3 -m py_compile scripts/concept_taxonomy/*.py` PASS；`build.py` / `decide.py` / `writeback.py --dry-run` / `validate.py` PASS；`git diff --check` PASS。
- Boundary: 本轮没有改任何概念卡 `up`，没有新增 `down` / `children` / Juggl 镜像字段，没有执行第二批写回；13 条剩余 ready 只作为下一批人工/LLM 复核后的候选。

## [2026-05-16] maintenance | 概念关系小批量写回

- 第二批写回只写 13 条 safe strict taxonomy，不恢复 2 条已降级的非 taxonomy 边。
- 新增 `up`：[[Long-term Memory]] → [[Memory]]、[[Microsoft Agent Framework]] → [[Agent Framework]]、[[Non-Parametric Memory]] → [[Memory]]、[[RAG Evaluation]] → [[Evaluation]]、[[Self-RAG]] → [[RAG]]、[[Semantic Memory]] → [[Memory]]、[[Tool Calling]] → [[Tool Use]]、[[Trajectory Evaluation]] → [[Evaluation]]、[[Computer Use]] → [[Tool Use]]、[[Data-first Agent Framework]] → [[Agent Framework]]、[[Graph Construction Evaluation]] → [[Evaluation]]、[[Multi-agent Orchestration]] → [[Agent Workflow]]、[[Parametric Memory]] → [[Memory]]。
- 保持拒绝：`OpenTelemetry GenAI -> Observability` 与 `State Graph Runtime -> Agent Workflow` 仍为标准化/支撑/执行关系，不写 `up`。
- 重新生成临时图与台账后：130 张概念卡、36 条 taxonomy `up`、67 条候选信号、0 条剩余 writeback candidates；post-apply dry-run 为 0 planned / 0 ready，表示本批 accepted edges 已写完。
- 同步 [[LLM Wiki 工作流]]：明确 post-apply 空 dry-run 在 `writeback_candidates=0` 时是完成态，验证仍要追踪 apply report 历史边是否真实存在。
- 验证：`python3 -m py_compile scripts/concept_taxonomy/*.py` PASS；`python3 scripts/concept_taxonomy/validate.py` PASS（130 cards / 1007 edges / 36 up / 13 applied / 0 plugin problems）；`git diff --check` PASS；逐张检查 13 张子卡均只有顶层 `up`，无 `down` / `children`。
- Boundary: 本轮没有全量重写 130 张概念卡，没有新增 `relations` 镜像字段，没有恢复 Juggl，也没有把 `related`、body wikilink 或 `topic_family_review` 升格为层级关系。

## [2026-05-16] wiki | Sparse Retrieval 机制分层写回

- 更新 [[Sparse Retrieval]]：新增“内部机制分层”，把 sparse representation、search structure、scoring 分开，明确 count vector / TF-IDF / sparse neural vector、inverted index、full-text scoring / BM25 分别处在不同层。
- 更新 [[08 面试题概念卡待补充]]：新增 Inverted Index 与 Sparse Neural Retrieval 候选；二者只进入 backlog，建卡前分别需要搜索系统证据和 SPLADE / sparse embedding 证据。
- Boundary: 本轮没有新建概念卡，没有修改 alias map、脚本、模板、`up` 虚拟层级或项目规则；`count vector` 与 `full-text scoring` 只作为 [[Sparse Retrieval]] 内部机制边界说明，不作为独立卡候选。

## [2026-05-16] maintenance | 概念关系尾巴闭环

- 关闭上一轮关系流水线剩余的关系尾巴：`defer_taxonomy` 从 1 降为 0，`reject_taxonomy` 与 `adjacency_only` 改为明确的 terminal non-writeback 决策，不再当作待办数量。
- 重新判定 `RAGGraph -> RAG`：[[RAGGraph]] 是 workflow graph / [[GraphRAG]] 混淆提醒卡，保留 related/relations，不写 `up: [[RAG]]`；因此改为 `reject_taxonomy` + `terminal_non_writeback`。
- 更新 [[RAGGraph]]：补 `relations` 到 [[RAG]]、[[GraphRAG]]、[[Agentic RAG]]，并在边界细节写明当前关系写回结论；更新 [[02 问题池]] 中两个 RAGGraph 边界问题为已闭环。
- 更新 `scripts/concept_taxonomy/decide.py` 与 `validate.py`：台账新增 `resolution_status`、`open_writeback_items`、`open_review_items`、`relation_tail_open_items`、`relation_tail_status`、`terminal_non_writeback_decisions`；验证会拒绝新的 `needs_review` / `defer_taxonomy` 开放尾巴。
- 重新生成报告后：130 张概念卡、36 条 taxonomy `up`、31 条 typed relations、67 条候选信号；ledger 为 `reject_taxonomy: 11`、`adjacency_only: 56`、`open_review_items: 0`、`open_writeback_items: 0`、`relation_tail_status: closed`；dry-run 为 0 planned / 0 ready。
- 验证：`python3 -m py_compile scripts/concept_taxonomy/*.py` PASS；`build.py` / `decide.py` / `writeback.py --dry-run` / `validate.py` PASS；`git diff --check` PASS；RAGGraph 断言检查 PASS（无 `up: [[RAG]]`，有 safe `relations`）。
- Boundary: 本轮没有新增任何 `up`，没有把 56 条 adjacency 信号强行写回，也没有新增 `down` / `children` / Juggl 字段；`reject_taxonomy` 是审查终态，不是“失败”。

## [2026-05-17] maintenance | 概念层级归属全量审计

- 实现 `scripts/concept_taxonomy/taxonomy_placement_review.py`，把当前临时关系图转换为全量“层级归属待审计概念卡”台账，而不是继续使用抽象的 `no-up` 命名。
- 生成 `reports/concept-card-relation-map/concept-hierarchy-placement-review.json` 与 `reports/concept-card-relation-map/concept-hierarchy-placement-review.md`：130 张概念卡全部入队；已有 `up` 的卡仍标记为待复核；无 `up` 的卡进入 review queue；候选证据、forbidden-as-up pair 和 drift guard 进入逐卡记录。
- 完成初始分流：36 张 `already_has_up_reviewed`，19 张 `root_or_anchor_no_up`，48 张 `relation_only_terminal`，4 张 `weak_or_backlog_terminal`，23 张 `defer_boundary_review`。
- Boundary: 本轮只建立审计基线与 routing，不写回任何概念卡 `up`，不新增 `down` / `children` / Juggl 字段；`concepts_without_up` 继续只是审计信号，不是失败指标。

## [2026-05-17] maintenance | Query 写回队列剩余候选分流

- 更新 [[05 Query 写回队列]]：把剩余 2 个 P3 pending 概念对比候选分成“证据补齐后再评估”和“查新后再写”，并明确当前没有可直接成页的新高证据候选。
- 更新 [[06 Wiki 健康检查]] 当前状态：Query write-back pending 仍为 2，但不再是未分类尾巴；它们分别是 LLM 能力来源证据补齐 backlog 与 runtime / 产品 / framework 生态 freshness-check。
- Boundary: 本轮不新建概念卡或 topic，不改 canonical name、aliases、alias map、字段规范、模板或项目规则；只是 backlog 分类与健康状态同步。

## [2026-05-17] maintenance | 概念层级父类白名单与保守候选

- 更新 `scripts/concept_taxonomy/taxonomy_placement_review.py`：把稳定父类白名单、非自动批准锚点、缺失 phantom parent、root/foundation anchor、deferred 卡的 parent-route precheck 写入审计台账。
- 重新生成 `reports/concept-card-relation-map/concept-hierarchy-placement-review.json/md`：`classification_stage: parent_whitelist_review`，approved stable parents 14，proposed anchors not auto-approved 3，missing proposed anchors 2，deferred rows parent-prechecked 23。
- 生成 `reports/concept-card-relation-map/concept-hierarchy-placement-candidates.json/md`，并更新 review artifact：`classification_stage: conservative_candidates`，generated candidates 3，suppressed signals 20。
- 当前候选只有 `Approval Gate -> Agent Workflow`、`Memory Reflection -> Memory`、`ReAct -> Agent Workflow`；它们仍是候选，不是 accepted taxonomy。
- Boundary: 本轮不写任何概念卡 `up`，不调度 dry-run；component-of、broad anchor、support/protect/execute 等信号继续被挡在 `up` 之外。

## [2026-05-17] source-update | 小林 Note sitemap 面试题

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Scope: `all`; checked 142 sitemap URLs.
- Result: new 22, changed 120, unchanged 0, errors 0.
- Updated navigation: [[资料收集索引]], [[04 页面目录]], [[index]]
- Boundary: this is raw evidence refresh; changed pages still need explicit wiki/concept digestion if their content matters.

## [2026-05-17] maintenance | 概念层级候选判定、dry-run 与有限写回

- 更新 `scripts/concept_taxonomy/taxonomy_placement_review.py`：把保守候选逐条判定为 accepted / rejected，并生成独立 adjudication artifact。
- 判定结果：`Memory Reflection -> Memory` 为 `accept_taxonomy` + `add_up`；`Approval Gate -> Agent Workflow` 与 `ReAct -> Agent Workflow` 均为 `reject_taxonomy`，因为它们分别是 workflow 控制点和 Agent Loop 模式，不是 Agent Workflow 子类。
- 生成 `reports/concept-card-relation-map/concept-hierarchy-placement-writeback-dry-run.json/md`：dry-run 只规划 1 条 ready taxonomy write：[[Memory Reflection]] → [[Memory]]。
- 只写回 1 条：[[Memory Reflection]] → [[Memory]]；[[Memory Reflection]] frontmatter 新增 `up: ["[[Memory]]"]`，`updated` 更新为 2026-05-17。被拒绝的两条非 taxonomy 候选继续排除，不进入 planned/applied。
- 重新生成临时关系图和 concept hierarchy placement artifacts：`classification_stage: limited_apply`，post-apply dry-run 为 0 planned / 0 ready。
- 验证：`python3 -m py_compile scripts/concept_taxonomy/*.py` PASS；writeback dry-run check PASS；`python3 scripts/concept_taxonomy/validate.py` PASS；面试题链接 self-test PASS；`git diff --check` PASS。
- Boundary: 本轮没有全量盲改 parentless cards，没有新增 `down` / `children` / Juggl 字段 / Breadcrumbs mirror 字段，也没有把 `related`、body wikilink 或 topic similarity 升格为 hierarchy。

## [2026-05-17] maintenance | 概念层级验证与控制面同步

- 加固 `scripts/concept_taxonomy/taxonomy_placement_review.py`：重复执行有限写回时会保留既有 apply report，记录幂等复核时间，并重建 post-apply artifacts，而不是把“已写回 1 条”的历史证据覆盖成空 apply。
- 加固 `scripts/concept_taxonomy/validate.py`：中央验证现在会检查 concept hierarchy placement apply report、已写入子卡 `up`、post-apply dry-run、excluded rows，以及无 `down` / `children` 字段。
- 新增 `scripts/concept_taxonomy/plugin_contract_verification.py` 和 `control_surface_sync.py`，生成 `reports/concept-card-relation-map/plugin-contract-verification.*` 与 `control-surface-sync.*`，把重建验证、插件契约和控制面同步做成可复跑证明。
- 同步 [[LLM Wiki 工作流]] 与 [[06 Wiki 健康检查]]：记录 130 张概念卡已审计、37 条顶层 `up`、验证 0 problems、`open_writeback: 0`、20 张 `defer_boundary_review` 进入后续边界队列。
- Boundary: 本轮不改 [[字段规范]] 或模板，因为 `up` / `relations` 语义和概念卡形状未变化；不新增概念卡关系，不新增 `down` / `children` / Juggl 字段 / Breadcrumbs mirror 字段。

## [2026-05-17] visual | Prompt Injection boundary diagram

- 新增 [[Prompt Injection vs Jailbreak vs Tool Poisoning.excalidraw]]，并在 [[Prompt Injection]] 的 `## 图示` 中嵌入。
- 图示把三者按入口和被改变的控制点分开：Prompt Injection 改上下文/任务流，Jailbreak 改内容策略，Tool Poisoning 改工具生态对模型的说明与副作用路径。
- Boundary: 这是学习型边界图，基于 [[Prompt Injection]]、[[Tool Poisoning]] 和 [[Agent 安全控制点对比]] 的工程综合；不是新增 source evidence，也不在本轮创建弱 `Jailbreak` 概念卡。
- Verification: Excalidraw compressed-json 反解为 69 elements / 35 text elements / 12 arrows，12/12 arrows 有双端 `startBinding` / `endBinding`，无中文文本残留；用本机 `excalidraw-diagram-skill` renderer 导出 PNG 视觉检查通过；`git diff --check` PASS。

## [2026-05-17] maintenance | 概念层级审计闭环与基线镜像

- 扩展 `scripts/concept_taxonomy/taxonomy_placement_review.py`：把剩余开放 review 收束为可复跑的审计闭环报告。
- 生成 `reports/concept-card-relation-map/concept-hierarchy-placement-closure.json/md`，并更新 `concept-hierarchy-placement-review.json/md` 到 `classification_stage: audit_closure`。
- 完成状态：130 张概念卡全部已审计；`taxonomy_placement_unreviewed: 0`，`open_unclassified: 0`，`open_review: 0`，`open_writeback: 0`，`dry_run_planned: 0`。
- 剩余 20 张 `defer_boundary_review` 没有被强行补父类；全部标记为 `review_status: deferred_with_backlog`，归宿写入 [[06 Wiki 健康检查#2026-05-17 概念层级审计边界队列]]。
- 新增 [[09 概念层级审计基线]]：把 `reports/concept-card-relation-map/concept-hierarchy-placement-review.json` 与 closure 的逐卡审计摘要导出为 vault 内长期可读 map。
- 同步入口：[[index]]、[[04 页面目录]]、[[LLM Wiki 工作流]]、[[06 Wiki 健康检查]] 与本日志。
- 该 map 记录 130 张概念卡的分类基线、37 条已有 `up`、20 条 deferred-with-backlog，以及未来新增卡如何对照已审计父类 / terminal parentless / deferred backlog。
- Boundary: 这只是稳定镜像和导航入口，不是新的写回授权；项目内机器报告只是可复跑 ledger，任何新增 `up` 仍必须走 candidate / adjudication / dry-run / limited apply。

## [2026-05-17] writeback | skill selection trust boundary

- Updated: [[Tool Poisoning]], [[Tool Registry]], [[Agent Harness]], [[Evaluation]], [[Agent 安全控制点对比]], [[05 Query 写回队列]]
- Source: [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]
- Boundary: `SKILL.md` / skill metadata is treated as operational text that can affect discovery, selection, trust, and loading; Agent reflection can help detect obvious mismatch but does not replace registry review, least privilege, trace, evaluation, or human approval.
- Terminology: no weak Agent Skill concept card was created and `scripts/interview_question_concept_aliases.json` was not changed; the term remains a source-backed boundary under [[Tool Poisoning]] / [[Tool Registry]] until more stable evidence is consolidated.

## [2026-05-17] maintenance | 概念层级审计项目化完成

- 将概念关系与层级审计的长期入口固化为 `scripts/concept_taxonomy/`，机器基线固化为 `reports/concept-card-relation-map/`，vault 内可读镜像为 [[09 概念层级审计基线]]。
- 补齐项目脚本入口说明：`scripts/README.md` 记录概念关系审计命令、面试题概念链接报告默认路径和候选 backlog 模板；`reports/concept-card-relation-map/README.md` 只把项目内报告目录作为长期事实来源。
- 新增 [[templates/面试题概念卡待补充]]，用于生成候选 backlog 页面形状；模板只记录待判定候选，不授权新建弱概念卡，也不改写 raw/source 正文。
- 同步 [[04 页面目录]] 与 [[06 Wiki 健康检查]]：把概念层级审计基线、项目脚本入口、报告目录、面试题链接报告和候选模板纳入长期维护视图。
- Boundary: 本轮不改 `up` / `relations` 字段语义，不改概念卡页面形状，不新增任何概念卡层级关系，不新增 `down` / `children` / Juggl 字段；本地工具状态目录仍只作为执行记录，不作为知识事实来源。

## [2026-05-17] maintenance | 请求元信息泄漏审计项目化

- 新增 `scripts/request_meta_audit.py`，作为聊天包装、运行态片段、请求路由话术和 intake provenance 脚手架的 durable vault 审计入口。
- 同步项目规则：`AGENTS.md`、[[LLM Wiki 工作流]]、[[06 Wiki 健康检查]] 和 `scripts/README.md` 都把 request meta audit 纳入 weekly / systemic maintenance。
- 验证：`python3 -m py_compile scripts/request_meta_audit.py` PASS；`python3 scripts/request_meta_audit.py --format markdown` 扫描 1113 个 Markdown 文件，PASS，命中 0。
- Boundary: 脚本只读检查 `wiki/`、`raw/`、`maps/`、`reviews/` 与 `log.md`；误报先收窄规则或写明边界，不把真实技术短语当作泄漏删除。

## [2026-05-17] maintenance | 概念层级基线门禁提升

- 更新 `AGENTS.md`：新增 Concept Taxonomy Baseline Gate，要求新增/更新概念关系前读取 [[09 概念层级审计基线]]，以 `reports/concept-card-relation-map/` 为机器基线，以 `scripts/concept_taxonomy/` 为复跑入口。
- 同步 [[LLM Wiki 工作流]]、[[09 概念层级审计基线]] 与 [[06 Wiki 健康检查]]：把基线读取、dry-run、limited apply 和验证命令写成未来 agent 的固定门禁。
- 更新 `scripts/concept_taxonomy/control_surface_sync.py`：把 `AGENTS.md` 纳入控制面同步验证。
- Boundary: 本轮只提升规则和复跑验证，不新增任何概念卡父类，不改 `up` / `relations` 字段语义，不修改概念卡模板。

## [2026-05-17] writeback | query enhancement boundary and MQE alias

- Updated: [[Query Rewrite]], [[Multi-Query Retrieval]], [[05 Query 写回队列]], `scripts/interview_question_concept_aliases.json`.
- Terminology: `MQE`, `Multi-Query Expansion`, `Multi Query Expansion`, and `多查询扩展` are aliases of [[Multi-Query Retrieval]].
- Boundary: “查询增强策略 / 查询优化” is a query-side strategy family, not a [[Query Rewrite]] alias; HyDE remains folded into [[Query Rewrite]] as a sub-strategy, and no weak HyDE or query-enhancement concept card was created.
- Taxonomy: kept the existing `Multi-Query Retrieval up [[Query Rewrite]]` Abstract Folder relationship; no `children`, `down`, Breadcrumbs mirror field, or new parent node was added.

## [2026-05-17] writeback | query-side retrieval strategy concept cluster

- Created: [[HyDE]], [[Step-back Prompting]].
- Updated: [[Query Rewrite]], [[Multi-Query Retrieval]], [[Query Planning]], [[Agentic Retrieval]], [[Query Rewrite Query Planning Agentic Retrieval 对比]], [[RAG 主题]], [[Agent 知识地图]], [[04 页面目录]], [[01 术语表]], [[08 面试题概念卡待补充]], [[05 Query 写回队列]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[HyDE]] / [[Step-back Prompting]] or [[Multi-Query Retrieval]] to high-confidence raw-question `related` / `## 相关知识 wiki` sections without rewriting source正文.
- Terminology: HyDE / Hypothetical Document Embeddings / 假设文档嵌入 are one canonical card; Step-back Prompting / Step Back Prompting / 后退提问 are one canonical card; neither is a [[Query Rewrite]] alias.
- Taxonomy: no direct `up` was written for the new cards; they are connected through `related`, body boundaries, alias map, and topic navigation pending concept-taxonomy validation.
- Mention sweep: searched HyDE, Hypothetical Document Embeddings, 假设文档/假想文档, Step-back/Step Back/后退提问, Multi-Query/MQE/多查询 across wiki, raw, maps, reviews, and alias map; linked high-confidence same-concept hits and left raw source text unchanged.

## [2026-05-17] validation | query-side retrieval strategy taxonomy closure

- Synced [[09 概念层级审计基线]] and [[06 Wiki 健康检查]] to the regenerated taxonomy reports: 132 concept cards, 37 top-level `up`, 95 concept cards without `up`, 22 `defer_boundary_review` rows closed as `deferred_with_backlog`.
- Added [[HyDE]] and [[Step-back Prompting]] to [[06 Wiki 健康检查#2026-05-17 概念层级审计边界队列]] and [[09 概念层级审计基线#Deferred with backlog：已审计但未来可重开]] as reviewed-but-parentless boundaries.
- Taxonomy boundary: no direct `up` was written for [[HyDE]] or [[Step-back Prompting]]; future parent placement must reopen candidate generation, adjudication, dry-run, and limited apply.
- Validation: taxonomy validate / plugin contract / control-surface sync / baseline-map validation PASS; concept-card audit 132 / needs 0; comparison-topic audit 23 / needs 0; request-meta audit 1116 files / 0 hits; paper source audit 45 PASS; interview link self-test PASS and dry-run reports 6 pages / 11 proposed inline links / 0 missing candidates / 0 protected violations; `git diff --check` PASS.

## [2026-05-17] writeback | coding agent repo context vs traditional RAG

- Added [[Coding Agent 为什么不用传统 RAG]] as a small topic boundary page.
- Updated navigation: [[Agent 知识地图]], [[04 页面目录]], [[05 Query 写回队列]].
- Boundary: kept [[Repo Context]] as the canonical concept; the new page answers a reusable product/architecture question about Codex CLI / Claude Code style clients and does not create a weak “coding-agent RAG” concept card.
- Terminology: no changes to `scripts/interview_question_concept_aliases.json`; “traditional RAG” and “repo context gathering” are boundary phrases, not new aliases.

## [2026-05-17] writeback | LLM context limit breakthrough topic

- Added [[LLM 上下文限制与突破条件]] as a small topic boundary page.
- Updated navigation: [[LLM 主题]], [[Agent 知识地图]], [[04 页面目录]], [[05 Query 写回队列]].
- Boundary: kept [[Context Window]], [[Context Engineering]], [[Memory]] and [[RAG]] as the canonical concepts; the new page answers a reusable architecture/interview question about what limits LLM context and what future breakthroughs require.
- Terminology: no new concept card, no `up` / `relations` writeback, and no changes to `scripts/interview_question_concept_aliases.json`; long-context / 上下文限制 are topic-level boundary phrases here, not new aliases.

## [2026-05-17] writeback | TTL lifecycle boundary concept

- Created: [[TTL]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], [[RAG]], [[Memory]], [[Long-term Memory]], [[RAG 主题]], [[Agent Memory 类型对比]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[TTL]] to high-confidence cache, memory, and RAG freshness source notes: [[109 01_AI 04_上下文工程与记忆 记忆系统与状态设计（短期 长期 State）]], [[113 01_AI 04_上下文工程与记忆 长期记忆如何做过期与纠错？]], [[272 02_后端 02_Redis 缓存穿透如何处理？]], [[274 02_后端 02_Redis 缓存雪崩如何处理？]], [[305 02_后端 05_缓存与一致性 缓存穿透如何处理？]], [[307 02_后端 05_缓存与一致性 缓存雪崩如何处理？]], [[529 05_项目表达 01_AI应用平台 如果知识库内容 过期或错误 ，怎么避免误导模型？]].
- Terminology: `TTL`, `Time To Live`, `生存时间`, `存活时间`, `有效期`, `过期时间`, and `缓存有效期` are aliases of the same lifecycle-boundary concept; network packet TTL is documented as a neighboring hop-limit usage, not as the cache/RAG freshness implementation itself.
- Taxonomy: no direct `up` was written; [[TTL]] is treated as a cross-cutting relation-only / parentless concept pending taxonomy candidate generation and dry-run.
- Mention sweep: searched TTL / Time To Live / 生存时间 / 存活时间 / 缓存有效期 / 有效期 / 过期时间 across wiki, raw, maps, reviews, and alias map; linked high-confidence same-concept hits and left raw source正文 unchanged.
- Validation: interview link self-test PASS; dry-run scanned 779 question pages / would modify 11 / inline links 16 / missing candidates 0 / protected violations 0; concept-card audit 133 / needs 0; comparison-topic audit 23 / needs 0; taxonomy validate, plugin contract, control-surface sync, baseline-map validation PASS; request-meta audit 1118 files / 0 hits; `git diff --check` PASS.

## [2026-05-17] writeback | KV Cache inference boundary and papers

- Created: [[KV Cache]].
- Added paper source notes: [[Fast Transformer Decoding - One Write-Head is All You Need]], [[GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints]], [[Efficient Memory Management for Large Language Model Serving with PagedAttention]], [[FlashAttention - Fast and Memory-Efficient Exact Attention with IO-Awareness]].
- Updated navigation and synthesis: [[LLM 主题]], [[LLM 上下文限制与突破条件]], [[Agent 知识地图]], [[01 术语表]], [[04 页面目录]], [[资料收集索引]], [[05 Query 写回队列]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[KV Cache]] to high-confidence xiaolinnote source notes for KV cache / prompt caching, MHA-MQA-GQA-FlashAttention, vLLM/PagedAttention deployment, quantization, and Agent memory compression / Prompt Caching.
- Terminology: `KV Cache`, `Key-Value Cache`, `K/V Cache`, `KV 缓存`, and `键值缓存` are aliases of the same inference-time cache concept; Prompt Caching, PagedAttention, MQA/GQA, and FlashAttention are related mechanisms, not aliases.
- Taxonomy: no direct `up` was written; [[KV Cache]] is treated as an LLM inference/runtime mechanism connected through `related` and evidence anchors pending taxonomy candidate generation, adjudication, dry-run, and limited apply.
- Mention sweep: searched KV Cache / KV cache / K/V Cache / Key-Value Cache / 键值缓存 / KV 缓存 / Prompt Caching / PagedAttention / FlashAttention / MQA / GQA across wiki, raw, maps, reviews, and alias map; linked high-confidence same-concept hits and left raw source正文 unchanged.
- Validation: paper source audit 49 PASS; concept-card audit 134 / needs 0; comparison-topic audit 23 / needs 0; interview link self-test PASS and dry-run reports 779 pages / would modify 15 / inline links 20 / missing candidates 0 / protected violations 0; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS with 134 concepts / 22 deferred-with-backlog; request-meta audit 1123 files / 0 hits; `git diff --check` PASS.

## [2026-05-17] source-localization | KV Cache paper PDFs

- Downloaded local PDFs into `raw/papers/assets/` for [[Fast Transformer Decoding - One Write-Head is All You Need]], [[GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints]], [[Efficient Memory Management for Large Language Model Serving with PagedAttention]], and [[FlashAttention - Fast and Memory-Efficient Exact Attention with IO-Awareness]].
- Updated each paper source note `pdf` field from arXiv PDF URL to the local `assets/*.pdf` path and synchronized [[资料收集索引]] paper localization counts.
- Boundary: extracted Markdown is still pending for these 4 PDFs because no local `markitdown` command was available in this environment; paper source notes remain raw evidence and do not claim page-level extracted anchors yet.
- Validation: `file` identifies all 4 downloaded assets as PDF; 49 / 49 paper notes now have `pdf: assets/...`; `python3 scripts/paper_source_audit.py` PASS; `python3 scripts/paper_source_quality_audit.py --root 'agentic learning/raw/papers'` PASS; `git diff --check` PASS.

## [2026-05-17] writeback | Prompt Engineering concept boundary

- Created: [[Prompt Engineering]].
- Updated navigation and synthesis: [[Prompt]], [[Context Engineering]], [[LLM 主题]], [[LLM 输入输出基础边界对比]], [[Agent 知识地图]], [[01 术语表]], [[04 页面目录]], [[09 概念层级审计基线]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[Prompt Engineering]] to high-confidence prompt/context source notes: [[123 01_AI 04_上下文工程与记忆 Prompt Engineering 及 Prompt 优化策略有哪些？]], [[124 01_AI 04_上下文工程与记忆 Prompt Engineering 和微调策略如何协同？]], [[127 01_AI 04_上下文工程与记忆 你如何定义“上下文工程”？和 Prompt Engineering 的边界是什么？]], [[126 01_AI 04_上下文工程与记忆 Context Engineering for AI Agents Lessons from Building Manus]], [[137 01_AI 04_上下文工程与记忆 补充材料：Context Engineering 的系统化做法]], [[136 ai llm 16. 如何写好 Prompt？分享下 Prompt 工程实践经验？]].
- Terminology: `Prompt Engineering`, `prompt engineering`, `Prompt 工程`, `提示词工程`, and `提示工程` are aliases of the same prompt-design engineering practice; `Prompt 优化` is treated as an activity inside Prompt Engineering rather than a canonical alias.
- Taxonomy: no direct `up` was written; [[Prompt Engineering]] is treated as relation-only / parentless because it is not [[Prompt]] itself and no stable `Prompting` parent card exists yet.
- Mention sweep: searched Prompt Engineering / prompt engineering / Prompt 工程 / 提示词工程 / 提示工程 / Prompt 优化 across wiki, raw, maps, reviews, and alias map; linked high-confidence same-concept hits and left raw source正文 unchanged.
- Validation: interview link self-test PASS; dry-run scanned 779 question pages / would modify 18 / inline links 24 / missing candidates 0 / protected violations 0; concept-card audit 135 / needs 0; comparison-topic audit 23 / needs 0; taxonomy build, decide, writeback dry-run, placement close-audit, validate, plugin contract, control-surface sync, and baseline-map validation PASS; paper source audit 49 PASS.

## [2026-05-18] writeback | Agent Robustness concept boundary

- Created: [[Agent Robustness]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], [[05 Query 写回队列]], [[06 Wiki 健康检查]], [[09 概念层级审计基线]], [[Evaluation]], [[Task Success Rate]], [[Evaluation 层次对比]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[Agent Robustness]] to high-confidence Agent evaluation source notes, including q174/q176/q183/q182/q186/q173/q194/q216/q523 and the paper source notes [[Beyond Cooperative Simulators - Generating Realistic User Personas for Robust Evaluation of LLM Agents]] / [[Rollout Cards - A Reproducibility Standard for Agent Research]], without rewriting raw source正文.
- Terminology: `Agent Robustness`, `Agentic Robustness`, `Agent 鲁棒性`, `Agent 稳健性`, `智能体鲁棒性`, `智能体稳健性`, `Robustness of Planning and Reasoning`, and `规划与推理的鲁棒性` are the same Agent-system robustness concept. Bare `鲁棒性 / 稳健性 / Robustness` remains intentionally excluded from alias map because model robustness, RAG robustness, benchmark robustness, and long-context position robustness are adjacent but not equivalent.
- Taxonomy: no direct `up` was written; regenerated taxonomy reports classify [[Agent Robustness]] as `relation_only_terminal` with typed relations to [[Task Success Rate]], [[Trajectory Evaluation]], and [[Guardrails]]. Topic-family overlap with [[Evaluation]] is a review signal only, not a parent write.
- Mention sweep: searched Agent Robustness / Agentic Robustness / Agent 鲁棒性 / 智能体鲁棒性 / 规划与推理的鲁棒性 / Robustness across wiki, raw, maps, reviews, and alias map; linked high-confidence Agent-system hits and skipped model/RAG/long-context robustness false friends.
- Validation: JSON alias map parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 19 / inline links 25 / missing candidates 0 / protected violations 0; concept-card audit 136 / needs 0; comparison-topic audit 23 / needs 0; paper source audit 49 PASS; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS with 136 concepts / 22 deferred-with-backlog; request-meta audit 1125 files / 0 hits; `git diff --check` PASS.

## [2026-05-18] writeback | RAGFlow and DeerFlow project concept boundaries

- Created source notes: [[RAGFlow 官方文档]], [[DeerFlow Repo]].
- Created concept cards: [[RAGFlow]], [[DeerFlow]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[RAG 主题]], [[资料收集索引]], [[前沿主源清单]], [[04 页面目录]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[RAGFlow]] to high-confidence agent_java_offer framework/RAG question notes q210/q212/q218/q219 without rewriting raw source正文.
- Terminology: `RAGFlow`, `Ragflow`, and `ragflow` are the InfiniFlow platform; bare `RAG Flow / RAG 流程` remains excluded as a generic pipeline phrase. `DeerFlow`, `deer-flow`, and `Deep Exploration and Efficient Research Flow` are the ByteDance project; bare `Deep Research` remains excluded because DeerFlow 2.0 is a broader super agent harness.
- Taxonomy: no direct `up` was written; both cards use `relations`, `related`, and source evidence pending taxonomy candidate generation, adjudication, dry-run, and validation.
- Mention sweep: searched RAGFlow / Ragflow / ragflow / RAG Flow and DeerFlow / deer-flow / Deep Exploration / Deep Research across wiki, raw, maps, reviews, scripts, and reports; linked high-confidence same-project hits and kept ambiguous generic phrases unlinked.
- Validation: JSON alias map parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 22 / inline links 28 / missing candidates 0 / protected violations 0; concept-card audit 138 / needs 0; comparison-topic audit 23 / needs 0; paper source audit 49 PASS; request-meta audit 1129 files / 0 hits; taxonomy build, decide, writeback dry-run, close-audit, validate, plugin contract, control-surface sync, and baseline-map validation PASS with 138 concepts / 37 top-level `up` / 22 deferred-with-backlog / 0 open writeback; `git diff --check` PASS.

## [2026-05-18] writeback | NLP foundation concept boundary

- Created: [[NLP]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[LLM 主题]], [[04 页面目录]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[NLP]] to high-confidence definition/comparison/evaluation source notes: [[161 01_AI 05_模型调优与微调 11 NLP是什么]], [[164 01_AI 05_模型调优与微调 补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系]], [[142 ai llm 1. 什么是大语言模型？和传统 NLP 模型有什么区别？]], [[170 01_AI 06_评测与监控 为什么传统的 NLP 评估指标（如 BLEU, ROUGE）对于评估现代 LLM 的生成质量来说，存在很大的局限性？]], and [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]].
- Terminology: `NLP`, `Natural Language Processing`, and `自然语言处理` are aliases of the same natural-language task-domain concept. `传统 NLP` is treated as a historical/pipeline style inside the domain, not a separate alias or card.
- Taxonomy: no direct `up` was written; [[NLP]] is treated as a foundation/domain anchor connected through `related` and body boundary notes, pending any future taxonomy candidate generation and dry-run.
- Mention sweep: searched NLP / Natural Language Processing / 自然语言处理 across wiki, raw, maps, reviews, and alias map; linked high-confidence same-concept source and navigation hits, skipped bibliography/conference-name noise and repeated raw references.
- Validation: JSON alias map parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 26 / inline links 32 / missing candidates 0 / protected violations 0; concept-card audit 139 / needs 0; `git diff --check` PASS.

## [2026-05-18] source-update | 小林 Note sitemap 面试题

- Source: [[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]
- Scope: `all`; checked 142 sitemap URLs.
- Result: new 0, changed 0, unchanged 142, errors 0.
- Updated navigation: [[资料收集索引]], [[04 页面目录]], [[index]]
- Automation: adjusted `scripts/update_xiaolinnote.py` to preserve the collection index `created` date during refresh.
- Boundary: this is raw evidence refresh; changed pages still need explicit wiki/concept digestion if their content matters.

## [2026-05-18] writeback | Progressive Disclosure concept boundary

- Created: [[Progressive Disclosure]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[Progressive Disclosure]] to high-confidence Skill / context-loading source notes: [[060 ai tools 9. Skill 是什么？]], [[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？]], [[Hermes Agent Repo]], [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]], [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents]], q240, and q523 without rewriting raw source正文.
- Terminology: `Progressive Disclosure`, `progressive disclosure`, `渐进式披露`, `渐进披露`, and `渐进式加载` are treated as the same information-disclosure / context-loading pattern. `按需加载` is intentionally excluded from the alias map because it is too generic and can describe ordinary lazy loading or runtime resource loading outside the Agent/context pattern.
- Taxonomy: no direct `up` was written; [[Progressive Disclosure]] is treated as relation-only / parentless because it is a cross-cutting context and capability-presentation pattern, not a strict child of [[Tool Use]], [[Tool Registry]], or [[Context Engineering]].
- Mention sweep: searched Progressive Disclosure / progressive disclosure / 渐进式披露 / 渐进披露 / 渐进式加载 / Progressive Active Tool Exploration across wiki, raw, maps, reviews, and alias map; linked high-confidence same-concept hits and kept RS-Claw's Progressive Active Tool Exploration as an adjacent mechanism rather than an alias.
- Validation: JSON alias map parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 30 / inline links 36 / missing candidates 0 / protected violations 0; concept-card audit 140 / needs 0; request-meta audit 1131 files / 0 hits; taxonomy build, decide, writeback dry-run, placement close-audit, validate, plugin contract, control-surface sync, and baseline-map validation PASS with 140 concepts / 37 top-level `up` / 22 deferred-with-backlog / 0 open writeback; `git diff --check` PASS.

## [2026-05-18] writeback | GSSC Pipeline context-builder pattern

- Created: [[GSSC Pipeline]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], [[LLM 上下文限制与突破条件]], [[Context Engineering]], `scripts/interview_question_concept_aliases.json`.
- Raw evidence backlinks: added [[GSSC Pipeline]] to [[Hello-Agents Repo]] and q122 without rewriting raw source正文.
- Terminology: `GSSC Pipeline`, `GSSC`, `Gather-Select-Structure-Compress`, `Gather Select Structure Compress`, `上下文构建四阶段流水线`, `收集-选择-结构化-压缩`, and `获取-选择-结构化-压缩` are treated as the same context-builder pipeline. Generic `上下文工程`, `压缩`, `选择`, `结构化` are intentionally excluded because they are broader operations, not this named pipeline.
- Taxonomy: no direct `up` was written; [[GSSC Pipeline]] uses `relations: pattern_for [[Context Engineering]]` pending candidate generation, adjudication, dry-run, and validation.
- Mention sweep: searched GSSC / Gather-Select-Structure-Compress / Gather Select Structure Compress / 上下文构建四阶段流水线 / 收集-选择-结构化-压缩 / 获取-选择-结构化-压缩 across wiki, raw, maps, and alias map; linked high-confidence same-pipeline hits and left generic gather/select/structure/compress wording unlinked.
- Validation: JSON alias map parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 30 / inline links 37 / missing candidates 0 / protected violations 0; concept-card audit 142 / needs 0; request-meta audit 1133 files / 0 hits; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS with 142 concepts / 37 top-level `up` / 22 deferred-with-backlog / 0 open writeback; `git diff --check` PASS.

## [2026-05-18] automation | public GitHub search index

- Added `scripts/build_search_index.py` to generate root `search-index.json` from committed Markdown for public GitHub/search-tool consumption.
- Added `.github/workflows/search-index.yml` to verify the generated index on push and pull request.
- Updated README and scripts documentation with the search-index boundary: public JSON search surface, not Obsidian local index, vector DB, or GitHub Code Search replacement.
- Generated `search-index.json` with 1135 documents and type counts: concept 142, source 886, map 49, review 5, project-index 2, plus README / AGENTS / index / log / generic markdown.

## [2026-05-18] writeback | Context Projection concept boundary

- Created: [[Context Projection]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], [[Agent State]], [[Long-Horizon Context Engineering]], [[GSSC Pipeline]], [[Context Window]], [[State Graph Runtime]], [[LLM 上下文限制与突破条件]].
- Terminology: `Context Projection`, `context projection`, and `上下文投影` are treated as the same Agent/context runtime mechanism. `state projection` / `state projector` are narrower state-focused uses, linked with display text where useful but intentionally not added as aliases. Generic `context assembly` / `上下文组装` remains broader RAG/context-building wording and is intentionally not mapped to this card.
- Taxonomy: no direct `up` was written; the card uses typed `relations` to [[Context Engineering]], [[Agent State]], [[Memory]], and [[Trace]], pending candidate generation, adjudication, dry-run, and validation.
- Mention sweep: searched Context Projection / context projection / 上下文投影 / state projection / state projector / context assembly / 上下文组装 across wiki, raw, maps, reviews, alias map, and taxonomy reports; linked high-confidence same-concept wiki hits and left raw RAG context-assembly mentions unlinked.
- Validation: alias JSON parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 30 / inline links 37 / missing candidates 0 / protected violations 0; request-meta audit PASS with 1136 files / 0 hits; taxonomy build, decide, writeback dry-run, placement close-audit, validate, plugin contract, control-surface sync, and baseline-map validation PASS with 144 concepts / 37 top-level `up` / 22 deferred-with-backlog / 0 open writeback; `git diff --check` PASS. Residual health debt: concept-card audit still flags existing [[Context Rot]] for evidence type/boundary repair; [[Context Projection]] itself is not flagged.

## [2026-05-18] writeback | Context Rot long-context reliability boundary

- Created source note: [[Chroma - Context Rot 技术报告]].
- Created concept card: [[Context Rot]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[04 页面目录]], [[资料收集索引]], [[LLM 主题]], [[LLM 上下文限制与突破条件]], [[Context RAG Memory 对比]], [[Context Window]], [[Context Engineering]], and [[Long-Horizon Context Engineering]].
- Terminology: `Context Rot`, `context rot`, `context degradation`, `long-context degradation`, `上下文退化`, `上下文腐化`, `长上下文退化`, and `长上下文可靠性退化` are treated as the same long-context effective-use degradation phenomenon. Generic model degradation, memory degradation, index degradation, service latency degradation, and security contamination remain adjacent or false-friend meanings unless the failure is specifically about reliable use of information already inside a long context.
- Taxonomy: no direct `up` was written; [[Context Rot]] is kept as a relation-only long-context reliability risk with typed relations to [[Context Window]], [[Context Engineering]], and [[Long-Horizon Context Engineering]] pending a stable long-context reliability or LLM reliability parent.
- Mention sweep: searched Context Rot / context degradation / long-context degradation / 上下文退化 / 上下文腐化 / 长上下文退化 across wiki, raw, maps, reviews, and scripts; linked high-confidence same-concept mentions and left the PIVOT paper's generic `context degradation` phrase unlinked because it is related evidence but not yet a same-concept canonical mapping.
- Validation: concept-card audit PASS with 144 concept cards / needs action 0; comparison-topic audit PASS with 23 pages / needs action 0; request-meta audit PASS with 1136 files / 0 hits; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS with 144 concepts; `git diff --check` PASS. Search index regenerated after writeback.

## [2026-05-18] writeback | ANP Agent Network Protocol boundary and protocol comparison

- Created source note: [[Agent Network Protocol]].
- Created concept card: [[ANP]].
- Created topic page: [[A2A MCP ANP 对比]].
- Updated navigation and synthesis: [[01 术语表]], [[Agent 知识地图]], [[Agent 主题]], [[03 前沿追踪]], [[04 页面目录]], [[资料收集索引]], [[前沿主源清单]], [[06 Wiki 健康检查]], [[09 概念层级审计基线]], [[A2A]], [[ACP]], [[MCP]], and `scripts/interview_question_concept_aliases.json`.
- Terminology: `ANP`, `Agent Network Protocol`, `Agent Network Protocol (ANP)`, and `智能体网络协议` are the same Agent network interoperability protocol concept. [[A2A]] and [[MCP]] are adjacent protocols, not ANP aliases.
- Taxonomy: no direct `up` was written; regenerated taxonomy reports classify [[ANP]] as `relation_only_terminal`, with a health-check backlog note that a future protocol / agent protocol parent must be created and reviewed before any `up` writeback.
- Mention sweep: searched ANP / Agent Network Protocol / AgentNetworkProtocol / 智能体网络协议 / 智能体网络 across wiki, raw, maps, reviews, and alias map; hits were the new source/concept/topic/navigation surfaces, so no old raw/source text required rewriting.
- Validation: alias JSON parse PASS; interview link self-test PASS and dry-run reports 779 pages / would modify 30 / inline links 37 / missing candidates 0 / protected violations 0; concept-card audit PASS with 145 concept cards / needs action 0; comparison-topic audit PASS with 24 pages / needs action 0; paper source audit 49 PASS; request-meta audit PASS with 1171 files / 0 hits; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS with 145 concepts / 37 top-level `up` / 22 deferred-with-backlog / 0 open writeback; `git diff --check` PASS. Search index regenerated with 1141 documents.

## [2026-05-18] source-ingest | 2026-05-15 arXiv Agent / RAG / Evaluation paper batch

- Created 16 raw paper source notes under `raw/papers/`: [[SaaS-Bench - Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows]], [[Argus - Evidence Assembly for Scalable Deep Research Agents]], [[DimMem - Dimensional Structuring for Efficient Long-Term Agent Memory]], [[FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast]], [[Context, Reasoning, and Hierarchy - A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP]], [[Differentiable Mixture-of-Agents Incentivizes Swarm Intelligence of Large Language Models]], [[TopoClaw - A Human-Centric and Topology-Aware Agent Operating System]], [[AstraFlow - Dataflow-Oriented Reinforcement Learning for Agentic LLMs]], [[Nudging Beyond the Comfort Zone - Efficient Strategy-Guided Exploration for RLVR]], [[SGR - A Stepwise Reasoning Framework for LLMs with External Subgraph Generation]], [[Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation]], [[DebiasRAG - A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation]], [[Fairness-Aware Retrieval Optimization for Retrieval-Augmented Generation]], [[BioXArena - Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks]], [[Confirming Correct, Missing the Rest - LLM Tutoring Agents Struggle Where Feedback Matters Most]], and [[Formal Methods Meet LLMs - Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems]].
- Downloaded 16 local PDF assets into `raw/papers/assets/` and generated 16 pypdf extracted Markdown files under `raw/papers/extracted/`.
- Updated durable navigation: [[资料收集索引]], [[03 前沿追踪]], and [[04 页面目录]]. Search index regenerated after ingest.
- Boundary: this is a raw evidence batch, not concept-card creation. P1/P2 priorities were recorded for reading order, but title terms such as SaaS-Bench, Argus, DimMem, FORGE, TopoClaw, DebiasRAG, and BioXArena remain source-level until 精读 establishes stable concept boundaries.
- Validation: metadata fetched from arXiv API for all 16 IDs; local assets passed PDF header/size checks; paper source audit PASS with 65 files; paper source quality audit PASS with 65 files; concept-card audit PASS with 145 concept cards / needs action 0; comparison-topic audit PASS with 24 pages / needs action 0; request-meta audit PASS with 1171 files / 0 hits; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS with 145 concepts; `git diff --check` PASS. Search index regenerated with 1173 documents.

## [2026-05-19] navigation | paper reading priority route cleanup

- Updated [[资料收集索引#Paper 阅读优先级规则（以后遵守）]] from a single broad P0/P1/P2/P3 table into a global route: P0 foundation, P1-A Agent system judgment, P1-B Research / RAG / Memory reliability, P1-C long-context / inference-cost boundary, P2 topic-triggered reading, and P3 background / on-demand reading.
- Integrated the 2026-05-15 arXiv batch into the global route: SaaS-Bench / Context, Reasoning, and Hierarchy / TopoClaw moved into P1-A; Argus / DimMem / FORGE moved into P1-B; Block Attention moved into P1-C; RAG fairness, domain benchmark, runtime compliance, multi-agent, SGR, and RLVR/system-training papers remain P2/P3 unless their topic becomes active.
- Updated [[03 前沿追踪#2026-05-15 arXiv Agent / RAG / Evaluation 论文批次]] with the route writeback boundary.
- Boundary: this is reading-route maintenance, not concept creation. Frontier paper titles remain source-level until 精读 establishes reusable concept boundaries and evidence anchors.

## [2026-05-19] query-writeback | RAG market visibility before Agent

- Added pending queue item to [[05 Query 写回队列]] for the boundary question: why RAG felt less visible in market / daily-life products before Agent-style systems.
- Target pages: [[RAG]], [[Agentic RAG]], [[RAG 主题]].
- Boundary: this is a durable query synthesis, not a new concept card. The key distinction is that pre-Agent RAG already existed in enterprise search, knowledge-base QA, and document retrieval, but Agent systems made it visible by connecting retrieval to goals, tools, state, workflow, evaluation, and action loops.

## [2026-05-19] concept-update | MCP core capability boundary

- Updated [[MCP]] with the Tools / Resources / Prompts capability split and the client-server call sequence: establish connection, discover capabilities, call tool, return result, and continue using the server.
- Terminology: Tools are active operations, Resources are passive data exposure, and Prompts are reusable guidance templates. They are related MCP server capabilities, not aliases of one another and not all safely reducible to “tools”.
- Evidence: linked the update to [[055 ai tools 4. 什么是 MCP（模型上下文协议）？讲讲它的核心内容？]] and [[056 ai tools 5. MCP 由哪几部分组成？]] while keeping the existing official-doc and security evidence anchors.
- Diagram: added a Mermaid learning-diagram transcription of the user-provided MCP client / filesystem server sequence to [[MCP#调用流程图（学习图）]]; marked it as learning diagram / engineering analogy, not official source evidence.
- Role boundary: added [[MCP#Host / Client / Server 角色分工]] to separate host as model/UI/policy holder, client as one-server protocol connector, and server as external capability provider/executor; reinforced that MCP server is not an Agent or model.
- Tool selection: added [[MCP#工具选择流程]] to explain discovery, model-visible schema construction, LLM tool-call intent, host-side checks, MCP server execution, and result integration; clarified that tool descriptions influence model selection and are part of the tool-poisoning risk surface.
- Boundary: simple content work; no new concept cards, no alias-map change, and no taxonomy `up` writeback.

## [2026-05-19] review | MCP concept-triggered review

- Created and updated [[05 MCP 概念触发式复习]] to check host / client / server role separation, MCP client as protocol connection module, Tools / Resources / Prompts boundaries, MCP vs [[Tool Calling|Function Calling]], tool selection flow, and permission / approval / audit thinking.
- Added Tool Calling / Function Calling follow-up questions for the two-turn tool-call loop, schema field effects, and the boundary between structured call requests and runtime governance.
- Added [[Tool 接口层对比]] follow-up questions for Tool Use / Tool Calling / Tool Registry / Tool Permissioning / MCP / MCP Registry layer separation and “Function Calling only vs introduce MCP” scenarios.
- Added [[Tool Calling]] and [[Tool 接口层对比]] as explicit review anchors so Function Calling is studied as the model-to-runtime structured request layer, while MCP remains the host/client/server connection protocol layer.
- Updated [[复习记录索引]] with the new review entry.
- Boundary: review note only; no concept-card schema, alias-map, taxonomy, or source evidence changes.

## [2026-05-20] concept-update | NLP and LLM algorithm boundary

- Updated [[NLP]] to make the reusable boundary explicit: NLP is a natural-language task domain and method/algorithm collection, not one fixed algorithm or a synonym for LLM.
- Updated [[LLM]] with the two-level algorithm boundary: as a black box it can be viewed as a large autoregressive probability function; internally it combines tokenization, Transformer/attention computation, normalization/activation, cache/runtime concerns, and decoding/sampling strategies.
- Filtered out AWS-Thrive / clinical-service implementation details; only the general NLP / LLM concept boundary was written into durable wiki pages.
- Terminology: `LLM`, `Large Language Model`, `Large Language Models`, `大语言模型`, and `大型语言模型` are treated as the same concept. `大模型` remains in the interview alias map because existing interview material uses it that way, but the concept card keeps the narrower language-model aliases in frontmatter.
- Updated `scripts/interview_question_concept_aliases.json` so interview auto-linking can recognize `Large Language Model`, `Large Language Models`, and `大语言模型`.
- Mention sweep: searched NLP / Natural Language Processing / 自然语言处理 / LLM / Large Language Model(s) / 大语言模型 / 大型语言模型 across wiki, raw, maps, backlog, and alias map. Existing raw/source hits already had related wiki anchors or were title/reference occurrences; no raw quotations were rewritten.
- Taxonomy: no `up` or `relations` writeback. [[NLP]] remains a foundation/domain card without a safe parent; [[LLM]] remains a foundation model card.
- Control surfaces: updated concept cards, alias map, and log only. Did not update AGENTS.md, [[LLM Wiki 工作流]], [[字段规范]], templates, or taxonomy reports because no workflow/schema/relationship rule changed.
- Validation: alias JSON parse PASS; interview link self-test PASS; interview dry-run scanned 779 pages and would modify 30 with 37 inline links / 0 missing candidates / 0 protected violations; concept-card audit PASS with 145 cards / needs action 0; request-meta audit PASS with 1172 files / 0 hits; `git diff --check` PASS.

## [2026-05-20] source-ingest | Coding Agent host vs Agent SDK runtime repo samples

- Created raw repo source notes: [[Claude Code CLI Repo]] and [[Antigravity SDK Python Repo]].
- Updated [[资料收集索引#第三轮：看项目和示例]] with both project samples.
- Boundary: both are source-level engineering samples, not new concept cards. `claude-code-cli` is recorded as a Coding Agent CLI host / harness source-code analysis repo with DeepWiki as Devin-generated secondary code guide; `antigravity-sdk-python` is recorded as an Agent SDK / runtime framework sample with DeepWiki as secondary code guide.
- Terminology: `Agent Harness`, `Agent Framework`, `Coding Agent`, `Tool Calling`, `Tool Permissioning`, and `MCP` already have canonical concept cards or alias-map entries. No new aliases, no interview auto-link changes, and no taxonomy `up` / `relations` writeback.
- Source boundary: GitHub README / source remain primary evidence; DeepWiki pages are useful for module navigation and code-reading entry points but do not replace source review.
- Validation: full AGENTS.md audit bundle PASS after source ingest: concept-card audit 145 cards / needs action 0; comparison-topic audit 24 pages / needs action 0; paper source audit 65 files PASS; interview link self-test PASS; interview dry-run scanned 779 pages and would modify 30 with 37 inline links / 0 missing candidates / 0 protected violations; taxonomy validate PASS with 145 concepts / 0 open review / 0 open writeback; plugin contract, control-surface sync, and baseline-map validation PASS; request-meta audit PASS with 1174 files / 0 hits; `git diff --check` PASS; Obsidian search finds both new source notes and the updated source index entry.

## [2026-05-20] maintenance | public search index regeneration

- Regenerated root `search-index.json` after adding the repo source notes and updating [[资料收集索引]] / [[log]].
- Script boundary: no missing script; the project already owns `scripts/build_search_index.py`, and CI verifies it through `.github/workflows/search-index.yml`.
- Validation: initial `python3 scripts/build_search_index.py --check` reported stale; after regeneration, `--check` PASS with 1176 documents and `git diff --check` PASS.

## [2026-05-20] workflow-rule | validation and search-index gate

- Updated project rule `AGENTS.md` with a diff-driven verification gate: always run `git diff --check`, regenerate/check `search-index.json` when indexed Markdown changes, and run the relevant audit scripts for concept cards, comparison topics, paper sources, interview links, request-meta hygiene, and taxonomy changes.
- Updated [[LLM Wiki 工作流#验证与公开搜索索引门禁]] with the operational version of the same rule.
- Boundary: this is a validation workflow rule change, not a schema/template/script change. `scripts/build_search_index.py` and `.github/workflows/search-index.yml` already existed, so no new script was added.
- Validation: full audit bundle PASS after rule update: concept-card audit 145 cards / needs action 0; comparison-topic audit 24 pages / needs action 0; paper source audit 65 files PASS; interview link self-test PASS; interview dry-run scanned 779 pages with 0 missing candidates and 0 protected violations; taxonomy validate PASS with 145 concepts / 0 open review / 0 open writeback; plugin contract, control-surface sync, and baseline-map validation PASS; request-meta audit PASS with 1174 files / 0 hits; search index regenerated and `--check` PASS with 1176 documents; `git diff --check` PASS.

## [2026-05-20] concept-update | MCP transport boundary

- Created [[MCP Transport]] as the durable card for MCP client/server message transport, instead of creating separate weak cards for `Stdio Transport`, `Streamable HTTP Transport`, `SSE Transport`, `HTTP Transport`, and `Memory Transport`.
- Updated [[MCP]] with a transport boundary section and corrected the learning diagram connection label from `Stdio / SSE / HTTP` to `Stdio / Streamable HTTP`.
- Updated source/navigation surfaces: [[Model Context Protocol 官方文档#Transport 补充]], [[048 ai tools 13. MCP 协议通常采用什么通信方式？]], [[055 ai tools 4. 什么是 MCP（模型上下文协议）？讲讲它的核心内容？]], [[056 ai tools 5. MCP 由哪几部分组成？]], [[049 ai tools 14. 说说 WebSocket 和 SSE 通信的区别及局限性？]], [[01 术语表]], [[Agent 知识地图]], [[Tool 接口层对比]], and [[05 MCP 概念触发式复习]].
- Terminology: `MCP Transport`, `MCP 传输层`, `Stdio Transport`, `Streamable HTTP Transport`, and legacy `HTTP+SSE Transport` are recorded as the same MCP transport-boundary card. Bare `HTTP`, bare `SSE`, and bare `stdio` were intentionally not used as aliases because they are broader transport/protocol terms and can create false links.
- Boundary: current standard MCP transports are `stdio` and `Streamable HTTP`; old HTTP+SSE is legacy / deprecated compatibility; SSE can still appear as a stream mechanism inside Streamable HTTP; Memory Transport is SDK/internal/testing scope, not a production transport choice.
- Taxonomy: no `up` or `relations` writeback. [[09 概念层级审计基线]] has no stable protocol-transport parent, and [[MCP]] is relation-only rather than a safe strict parent.
- Mention sweep: searched `MCP Transport`, `MCP 传输`, `传输层`, `stdio`, `Streamable HTTP`, `SSE Transport`, `HTTP+SSE`, and `Memory Transport` across wiki, raw, maps, reviews, and alias map; only high-confidence MCP transport mentions were linked.
- Validation: alias JSON parse PASS; interview link self-test PASS; interview dry-run scanned 779 pages and would modify 34 with 41 inline links / 0 missing candidates / 0 protected violations; concept-card audit PASS with 146 cards / needs action 0; comparison-topic audit PASS with 24 pages / needs action 0; request-meta audit PASS with 1175 files / 0 hits; taxonomy build/decide/dry-run/closure synced reports to 146 concepts with 0 open review / 0 open writeback and 24 deferred-with-backlog; taxonomy validate, plugin contract, control-surface sync, and baseline-map validation PASS; search index regenerated and `--check` PASS with 1177 documents; `git diff --check` PASS.
