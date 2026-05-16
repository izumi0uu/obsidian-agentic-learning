---
type: map
topic:
  - maintenance
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-16
related:
  - "[[LLM Wiki 工作流]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[08 面试题概念卡待补充]]"
  - "[[08 面试题概念链接待办]]"
  - "[[字段规范]]"
---

# 06 Wiki 健康检查

这页记录周期性 lint、freshness 和 contradiction check 的结果。

## 当前状态

- Last lint: 2026-05-16
- Missing links: none
- Concept cards: 130；`scripts/concept_card_audit.py --format markdown` 显示 Needs action = 27。
- Comparison topic pages: 23；`scripts/comparison_topic_audit.py --format markdown` 显示 Needs action = 6。
- Raw markdown pages: 908；其中 frontmatter `type: source` 859。主源清单仍看 [[资料收集索引]]。
- Paper source audit: `scripts/paper_source_audit.py` 检查 `raw/papers/` 45 个文件，PASS。
- Interview concept link audit: `scripts/interview_question_concept_links.py --self-test` PASS；`--dry-run` 扫描 757 个题页，would modify 0，missing concept candidates 0，protected region violations 0。
- Query write-back pending: 2（概念对比候选队列中 P3 两项暂不强行成页）。
- Current action queues: 27 张概念卡需要小修 evidence / detail；6 张对比 topic 需要补模板 section / evidence boundary。不要一次性批量重写，按主题小批量修。

边界：本节是“当前状态”，会覆盖上方读者对最新健康状态的理解；旧的 2026-05-10 / 2026-05-11 数字保留下方历史小节，不能再被当成现状。Needs action 代表排队修复，不代表要一次性批量重写旧卡；批量修复旧卡前需要用户确认。

## 每周检查清单

- [ ] 更新 [[04 页面目录]]。
- [ ] 跑 missing-link scan。
- [ ] 跑固定审计命令：
  - `python3 scripts/concept_card_audit.py --format markdown`
  - `python3 scripts/comparison_topic_audit.py --format markdown`
  - `python3 scripts/paper_source_audit.py`
  - `python3 scripts/interview_question_concept_links.py --self-test`
  - `python3 scripts/interview_question_concept_links.py --dry-run`
  - `git diff --check`
- [ ] 检查概念卡是否有“它不是什么”。
- [ ] 检查概念卡是否有 `## 边界细节`。
- [ ] 检查 Agent / prompting / framework / evaluation / RAG / memory / tooling / safety / protocol / product-ecosystem 概念卡是否有 `## 现代性状态`。
- [ ] 检查概念卡是否有 `## 复习触发`。
- [ ] 抽查概念卡是否只是“一句话 + 链接”，没有问题背景、最小例子、误解、边界或证据。
- [ ] 检查概念卡是否有“证据锚点”。
- [ ] 检查 raw source 是否有 `last_checked` 和 `freshness`。
- [ ] 处理 [[05 Query 写回队列]]。
- [ ] 处理 [[08 面试题概念卡待补充]] 和 [[08 面试题概念链接待办]] 中的可确认项；不确定项继续留 backlog。
- [ ] 把发现的问题和最新统计追加到本页；如果更新了“当前状态”，明确旧数字只是历史快照。

## 2026-05-16 规则控制面同步审计

本轮目标是把“项目规则评估”发现的状态漂移写回控制面，而不是直接修 27 张概念卡或 6 张对比页。

### 审计结果

| 检查项 | 当前结果 | 处理 |
|---|---:|---|
| Concept Card Audit | 130 张概念卡；Needs action = 27 | 进入小批量修复队列，不批量重写 |
| Comparison Topic Audit | 23 张对比 topic；Needs action = 6 | 进入小批量修复队列，不批量重写 |
| Paper Source Audit | `raw/papers/` 45 个文件 PASS | 维持现状 |
| Interview concept links self-test | PASS | 维持现状 |
| Interview concept links dry-run | 757 个题页；would modify 0；missing concept candidates 0；protected region violations 0 | 维持现状 |
| `git diff --check` | PASS | 维持现状 |

### 当前修复边界

- 本轮只同步规则控制面、导航入口、模板日期和审计命令，不修 concept / comparison 正文。
- [[08 面试题概念卡待补充]] 和 [[08 面试题概念链接待办]] 已纳入入口 / 页面目录，后续 weekly maintenance 必须检查。
- 旧健康检查数字保留为历史，不能覆盖“当前状态”。

## 2026-05-10 概念卡标准化 lint

本次 lint 的目标不是全量改写，而是把概念卡标准升级为“双层学习 + 判断卡”，并建立后续修复队列。

### 抽样结果

| 检查项 | 数量 | 解释 | 处理策略 |
|---|---:|---|---|
| 概念卡总数 | 90 | `wiki/concepts/*.md` | 只抽样修复 4 张风格锚点 |
| 缺 `## 边界细节` | 57 | 很多旧卡有定义但缺少邻近概念切分；本次修复前为 60 | 排入队列，按主题逐批修 |
| 缺 `## 现代性状态` | 79 | 旧卡多未主动判断 foundation / transitional / current-practice / frontier；本次修复前为 83 | 只对本次修改和高价值卡先补 |
| 缺 `## 复习触发` | 86 | 旧模板没有把概念卡连接到 review 流程；本次修复前为 90 | 后续每次修卡都补 1-3 个问题 |

### 第一批修复队列

| 优先级 | 候选卡 | 主要缺口 | 处理方式 |
|---|---|---|---|
| P0 | [[Agent]] | 基础概念，但缺 `边界细节`、`现代性状态`、`复习触发` | 本次作为 anchor 样例修复 |
| P0 | [[Trace]] | 已较完整，但缺现代性和复习触发；需切开 [[Trajectory]] / [[Reasoning Trace]] / eval | 本次作为 observability 样例修复 |
| P0 | [[Trajectory Evaluation]] | evaluation 判断卡代表；需拆开 trace、trajectory、score、judge 的边界 | 本次作为 eval 样例修复 |
| P0 | [[RAG]] | 非 Agent 但核心知识概念；需补现代系统吸收和复习触发 | 本次作为 RAG 样例修复 |
| P1 | [[Agent Loop]], [[Agent Framework]], [[Agent State]], [[Agent Workflow]] | Agent 工程骨架，现代性状态和复习触发不齐 | 已完成小范围修复：补齐问题背景、边界、现代性、现代系统吸收、证据锚点和复习触发 |
| P1 | [[Evaluation]], [[Eval Harness]], [[LLM-as-Judge]], [[RAG Evaluation]] | 评估概念相互依赖，需统一 “记录 vs 判断 vs harness” 边界 | 已完成小范围修复：统一 evaluation / harness / judge / RAG eval 的责任边界和复习触发 |
| P2 | [[A2A]], [[ACP]], [[MCP]], [[MCP Registry]] | 协议/生态变化较快，需要 freshness 与前沿追踪联动 | 需要查新后再修 |

### 不做的事

- 不批量重写 90 张旧概念卡。
- 不把每张卡扩成百科长文。
- 不把没有证据的工程直觉写成来源结论。
- 不把 `reviews/` 当作 raw evidence；复习记录只用于学习校准和写回候选。

## 2026-05-10 P1 概念卡小范围修复

本轮只修 P1 的 8 张目标卡，不批量重写旧卡。注意：这一轮最初完成的是“结构修复”，不是“深度解释完成”；用户反馈后，标准已升级为 `## 概念详解` 为主体。

- Agent 工程组：[[Agent Loop]], [[Agent Framework]], [[Agent State]], [[Agent Workflow]]
- Evaluation 组：[[Evaluation]], [[Eval Harness]], [[LLM-as-Judge]], [[RAG Evaluation]]

### 结构验收结果

- 8 张目标卡均包含：`一句话`、`它解决什么问题`、`它不是什么`、`最小例子`、`常见误解/风险`、`边界细节`、`现代性状态`、`证据锚点`、`复习触发`、`相关链接`。
- 新增判断均保留来源锚点，或明确作为工程综合理解处理。
- `git diff --check` 通过。
- hard boundary 通过：未改 `raw/`、`AGENTS.md`、模板页，也未批量改 P2 协议/前沿卡。

边界：这次完成的是 P1 抽样修复，不代表 90 张旧概念卡已经全部统一；剩余缺口继续按主题小批量排队。结构完整也不等于概念讲透，后续 qualified / anchor 卡要检查 `## 概念详解` 是否承担主体解释。

## 2026-05-10 概念详解标准升级

用户反馈：概念卡可以保留 `## 一句话`，但详解应该是最高比重；不能只做“一句话解释 + section 补齐”。

### 新增验收点

- qualified / anchor 卡必须有 `## 概念详解`。
- `## 概念详解` 是主体段落，应解释：概念为什么出现、解决什么原始问题、机制/组成部分、论文/官方文档/社区实践如何描述它、现代系统如何吸收或限制它。
- `## 证据锚点` 必须区分 paper source、official docs、community practice、engineering synthesis、user redraw / analogy。
- section 完整只是最低门槛；如果缺少连续解释、来源边界和例子，仍然属于浅卡。

### 已重修为深度样例

- [[Agent Loop]]：加入 ReAct 论文层、LangGraph / Agents SDK 工程层、guardrails / trace / eval 边界。
- [[Evaluation]]：加入 GAIA、SWE-bench、LangSmith / Langfuse 证据层，并拆成任务、样例、判断方法、运行机制四层。

### 完成状态

P1 8 张目标卡已按新标准补齐 `## 概念详解`：

- 第一批深度样例：[[Agent Loop]], [[Evaluation]]。
- 本次补齐剩余 6 张：[[Agent Framework]], [[Agent State]], [[Agent Workflow]], [[Eval Harness]], [[LLM-as-Judge]], [[RAG Evaluation]]。

边界：这表示 P1 目标卡完成了“概念详解主体化”，不代表 90 张旧概念卡已全量深修；后续仍按主题小批量推进。


## 2026-05-12 Team 概念对比 topic 全量更新

本轮按 `$team 4:executor` 启动 4 个 `gpt-5.5 xhigh` worker，目标是把 P1/P2/P3 中证据足够的概念组写成边界判断型 topic 对比页。

### 新增 / 集成页面

- Agent 工程 / 协议：[[Agent 工程分层对比]], [[Tool 接口层对比]], [[Multi-agent Handoff Protocol 对比]]。
- 安全 / 执行边界：[[Agent 安全控制点对比]], [[Browser Computer Use 执行栈对比]], [[Coding Agent 执行边界对比]]。
- Memory / RAG / retrieval：[[Agent Memory 类型对比]], [[Context RAG Memory 对比]], [[Retrieval 组件对比]]。
- Evaluation / observability：[[Evaluation 层次对比]], [[Observability Audit 对比]]。
- LLM 地基：[[LLM 基础结构对比]]。

### 验收边界

- 所有新增对比页都应保留 [[LLM Wiki 工作流#概念对比 / 类比 topic 页写法]] 要求的 section：一句话总览、为什么值得对比、共同问题域、核心区别表、混淆边界、机制差异、非证据类比、现代系统吸收/限制、什么时候用哪个判断、共同不是什么、证据锚点、复习触发、相关链接。
- `raw/` 仍保持 evidence 层，本轮不编辑 raw source notes。
- [[Oh My Codex (OMX)]] / [[Hermes Agent]] / [[LangChain DeepAgents]] / [[Agent Framework]] 这类 runtime / 产品对比暂不强行成页；它们变化快，进入 [[05 Query 写回队列]] 的 P3 pending。
- [[LLM]] / [[LLM Training Pipeline]] / [[Zero-shot CoT]] / [[Plan-and-Solve Prompting]] 的“能力来源”对比也暂不强行成页；需先补训练主源与 prompting paper 的证据边界。

### Team lifecycle 备注

- worker 页面内容已通过 team auto-commit / cherry-pick 集成到 leader branch。
- worker-2 / worker-3 的 task lifecycle 曾因 native subagent read-only probe 误判进入 `failed` terminal；后续 mailbox 和 commit 证据显示对应内容已存在于 leader HEAD。最终关闭 team 时按“terminal failed but acknowledged / deliverable integrated”处理，而不是继续重复派发弱修复任务。

## Freshness 规则

| freshness | 复查节奏 | 适用对象 |
|---|---|---|
| stable | 低频，学习复盘时查 | 经典论文、基础概念 |
| watch | 每月 | 框架、repo、前沿方向 |
| volatile | 1-2 周 | API 文档、安全榜单、活跃产品 |
| stale | 立即 | 已发现可能过期的来源 |

## 待复查来源

```dataview
TABLE source_type, site, freshness, last_checked, status
FROM "raw"
WHERE type = "source" AND (freshness = "watch" OR freshness = "volatile" OR freshness = "stale")
SORT freshness DESC, last_checked ASC
```

## 证据锚点缺口

```dataview
TABLE source, evidence, status, updated
FROM "wiki/concepts"
WHERE type = "concept" AND !evidence
SORT file.name ASC
```

## 潜在矛盾

| 日期 | 概念 | 冲突说法 | 来源 | 处理状态 |
|---|---|---|---|---|
| 2026-05-07 | [[Agent]] | OpenAI、Anthropic、LangGraph 对 Agent/workflow 边界表述不同 | [[OpenAI - A Practical Guide to Building Agents]], [[Anthropic - Building Effective Agents]], [[LangGraph 官方文档]] | pending |
| 2026-05-07 | [[GraphRAG]] / [[RAGGraph]] | RAGGraph 可能是项目名、工作流图，也可能被误当作 GraphRAG 同义词 | [[03 前沿追踪]], [[RAGGraph]] | watching |

## 本次维护记录

- 2026-05-07：建立 page catalog、query 写回队列、健康检查页、证据锚点规范、freshness 字段。
- 2026-05-10：完成 P1 小范围概念卡修复（Agent 工程组 4 张 + Evaluation 组 4 张），并把缺口统计更新为 `边界细节` 51、`现代性状态` 73、`复习触发` 78。
- 2026-05-10：完成 P1 8 张目标卡的 `## 概念详解` 深修；后续不按“有 section 即通过”，而按详解是否解释动机、机制、证据和现代工程吸收来验收。
- 2026-05-11：录入 [[Hermes Agent]] / [[Hermes Agent Repo]] 后，`scripts/concept_card_audit.py --format markdown` 显示 91 张概念卡，Needs action = 0；`git diff --check` PASS。

## 2026-05-11 Team 概念卡全量规范化收尾

本轮接续 `$team 7` 的 worktree 结果完成 leader 收尾。原 tmux pane 被误关后，team state 仍保留；已合并 5 个 writer lane，并按 worker-6 / worker-7 报告修复剩余问题。

### 验收结果

- `scripts/concept_card_audit.py --format markdown`：90 张概念卡，Needs action = 0。
- `git diff --check`：PASS。
- `git diff --cached --check`：PASS。
- raw 边界：从 checkpoint `0a9362d` 到当前 HEAD / 工作区未修改 `agentic learning/raw/`。
- 证据锚点：修正 [[Agent Harness]]、[[Multi-agent Orchestration]]、[[Trace]]、[[Computer Use]] 中误指向 `[[前沿主源清单#RAG 进化]]` 的锚点，改为更贴近语义的 `#代码 Agent`、`#评测与观测`、`#计算机使用`。

### 本轮重点补齐

- worker-2 runtime / memory lane 的残留深度缺口：[[Memory]], [[Durable Execution]], [[Handoff]], [[Agent Lifecycle Hook]], [[Code Execution Sandbox]], [[LLM Gateway]], [[Long-term Memory]], [[Semantic Memory]], [[Episodic Memory]], [[Memory Reflection]], [[Non-Parametric Memory]], [[Parametric Memory]], [[双链]], [[AGENTS.md]]。
- seed-lite 卡不强行扩写成长文，但补清 `## 边界细节`、`## 现代性状态` 和 `## 复习触发`，明确为什么保持 seed-lite。

边界：审计脚本为 0 表示结构 / 深度阈值 / evidence marker 达到当前规范，不等于每张卡已经达到论文级精读。后续维护仍应按 source freshness、用户复习暴露的问题和新资料证据继续小步迭代。
