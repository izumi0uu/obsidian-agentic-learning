---
type: log
topic:
  - obsidian
  - llm-wiki
status: active
created: 2026-05-05
updated: 2026-05-10
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
