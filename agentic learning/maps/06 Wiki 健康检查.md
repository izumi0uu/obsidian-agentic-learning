---
type: map
topic:
  - maintenance
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-18
related:
  - "[[LLM Wiki 工作流]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[08 面试题概念卡待补充]]"
  - "[[08 面试题概念链接待办]]"
  - "[[09 概念层级审计基线]]"
  - "[[字段规范]]"
---

# 06 Wiki 健康检查

这页记录周期性 lint、freshness 和 contradiction check 的结果。

## 当前状态

- Last lint: 2026-05-18
- Missing links: none
- Concept cards: 138；`scripts/concept_card_audit.py --format markdown` 显示 Needs action = 0。
- Comparison topic pages: 23；`scripts/comparison_topic_audit.py --format markdown` 显示 Needs action = 0。
- Raw markdown pages: 936；其中 frontmatter `type: source` 887。主源清单仍看 [[资料收集索引]]。
- Paper source audit: `scripts/paper_source_audit.py` 检查 `raw/papers/` 49 个文件，PASS。
- Interview concept link audit: `scripts/interview_question_concept_links.py --self-test` PASS；`--dry-run` 扫描 779 个题页，would modify 22，proposed inline links 28，missing concept candidates 0，protected region violations 0；默认报告写入 `reports/interview-question-concept-card-links-report.*`，候选 backlog 页面形状由 [[templates/面试题概念卡待补充]] 提供。
- Request meta audit: `scripts/request_meta_audit.py --format markdown` 扫描 1129 个 durable vault Markdown 文件，PASS；聊天包装、运行态片段和请求路由话术命中 0。
- Query write-back pending: 2（概念对比候选队列中 P3 两项已在 [[05 Query 写回队列#2026-05-17 剩余候选分流]] 分流：1 项证据补齐后再评估，1 项查新后再写；当前均不强行成页）。
- 概念层级归属审计：138 张概念卡已纳入审计；37 条顶层 `up`；审计闭环通过；[[Agent Robustness]]、[[RAGFlow]] 和 [[DeerFlow]] 被判为 `relation_only_terminal`，不从 topic-family 信号直接写 `up`；项目规则已要求新增/更新概念关系前先读 [[09 概念层级审计基线]]；机器基线保存在 `reports/concept-card-relation-map/`，长期复跑入口是 `scripts/concept_taxonomy/`；`open_review: 0`，`open_writeback: 0`，`dry_run_planned: 0`；22 张 `defer_boundary_review` 已全部标记为 `deferred_with_backlog`，不得为了清零强行补父类。
- Current action queues: concept-card audit、comparison-topic audit 与概念层级归属审计的本轮 open tail 均已清空；22 张 deferred-with-backlog 卡是未来可重开的边界队列，不是当前可直接写 `up` 的任务。

边界：本节是“当前状态”，会覆盖上方读者对最新健康状态的理解；旧的 2026-05-10 / 2026-05-11 数字和“27+6”队列保留下方历史小节，不能再被当成现状。本次 27+6 全量修复是用户明确授权的一次性系统性批量维护；以后仍不要在未确认时批量重写旧卡。Needs action = 0 只表示固定审计脚本当前通过，不表示所有概念卡已经达到百科式深度。

## 2026-05-17 请求元信息泄漏审计项目化入口

本节记录“不要把当前对话、IDE 上下文、hook 片段和执行请求写进知识正文”的项目脚本入口。

| Surface | Role | Boundary |
|---|---|---|
| `scripts/request_meta_audit.py` | 项目级可复跑审计脚本 | 只扫描 durable vault Markdown；误报先收窄规则，不删除真实概念内容 |
| [[LLM Wiki 工作流#用户请求元信息隔离]] | 工作流规则 | 定义哪些请求侧话术应被中性化 |
| `AGENTS.md` | 项目级规则 | 把 request meta audit 纳入 weekly / systemic maintenance bundle |

当前验收点：weekly maintenance 和系统性维护都应运行 `python3 scripts/request_meta_audit.py --format markdown`；若发现命中，先判断是泄漏、历史日志摘要、还是真实技术短语，再选择中性化正文、收窄规则或记录边界。

## 2026-05-17 概念层级审计项目化入口

本节记录概念关系审计能力的项目内稳定入口。

| Surface | Role | Boundary |
|---|---|---|
| `AGENTS.md` | 项目级硬规则 | 新增/更新概念关系前必须读取基线并跑验证；不直接写 `up` |
| `scripts/concept_taxonomy/` | 项目级可复跑脚本 | 真实写回仍必须 `--apply --limit N` |
| `reports/concept-card-relation-map/` | 机器可读 baseline / report store | 保存 JSON/MD 证明；报告不自动授权写 `up` |
| [[09 概念层级审计基线]] | 人类 / agent 可读镜像 | 用于新增卡嵌合判断；不是直接写回清单 |

当前验收点：AGENTS 顶层规则、项目脚本、项目 reports、workflow、健康检查、baseline map 和日志都必须提到 `scripts/concept_taxonomy/` 与 `reports/concept-card-relation-map/`；`字段规范.md` 和模板不改，因为 `up` / `relations` 语义没有变化。

## 2026-05-17 概念层级审计边界队列

本节是概念层级归属审计的 backlog home：这些卡已经被审计过，但当前证据下没有安全的 strict taxonomy parent。它们不是“漏写 `up`”，而是“未来如果有更窄父类或新证据，可以显式重开”的边界队列。

| Concept | Suppressed target | Why not `up` now | Reopen trigger |
|---|---|---|---|
| [[A2A]] | [[Agent]] | 协议 / 生态卡；`Agent` 太宽，当前没有 approved protocol parent。 | 新建并审计 protocol / agent protocol 父类，或卡片证据证明 strict kind-of。 |
| [[ACP]] | [[Agent]] | 协议 / 生态卡；`Agent` 太宽，当前没有 approved protocol parent。 | 新建并审计 protocol / agent protocol 父类，或卡片证据证明 strict kind-of。 |
| [[Browser Agent]] | [[Agent]] | 看似 Agent 子类，但 `Agent` 不是自动父类，缺更窄 reviewed parent。 | 若建立 Computer-use Agent / Browser Automation Agent 等稳定父类再重开。 |
| [[Code Execution Sandbox]] | [[Tool Use]] | sandbox 是安全运行边界，不是 tool-use 行为本身。 | 若建立 Sandbox / Execution Isolation / Security Boundary 父类再重开。 |
| [[Data Exfiltration]] | [[Prompt]] | 数据外泄是风险 / attack class，不是 Prompt 的一种。 | 若建立 Security Risk / Prompt Attack / Data Security 风险类父卡再重开。 |
| [[Entity Resolution]] | [[Knowledge Graph]] | 它可支撑 Knowledge Graph / retrieval，但 support/use 不是 taxonomy。 | 若卡片边界改为某个 approved entity-matching 方法族成员再重开。 |
| [[GUI Grounding]] | [[Agent]] | GUI grounding 是能力 / 对齐方式，不是宽泛 Agent 子类。 | 若建立 Computer-use / Grounding Capability 父类再重开。 |
| [[KV Cache]] |  | 它是 attention / inference runtime state；当前没有 approved Inference Runtime 或 Attention Cache 父类，不能因 related 到 [[Transformer]] / [[Context Window]] 就写 `up`。 | 若建立推理运行时 / attention cache 父类，或卡片证据证明 strict kind-of，再走候选生成 / adjudication / dry-run。 |
| [[Least Privilege Tools]] | [[Tool Use]] | 最小权限约束 Tool Use，但 policy principle 不是 Tool Use 子类。 | 若建立 Tool Safety Policy / Permissioning 父类再重开。 |
| [[MCP]] | [[Tool Use]] | MCP 是协议 / 生态根，不是 tool-use 行为。 | 若建立 Agent Protocol / Tool Protocol 父类并审计通过再重开。 |
| [[MCP Registry]] | [[MCP]] | Registry 很靠近 MCP，但 MCP 还不是 approved parent。 | 若 MCP 被审计为 protocol parent 或建立 Registry/Discovery 父类再重开。 |
| [[Multi-Head Attention]] | [[Transformer]] | Transformer component-of，不是 kind-of Transformer。 | 若建立 Attention Mechanism / Transformer Component 父类再重开。 |
| [[Observation]] | [[Agent Workflow]] | Observation 是 loop/runtime signal，不是 workflow 本身。 | 若建立 Agent Loop Signal / Trace Event 父类再重开。 |
| [[Obsidian + LLM Wiki]] | [[RAG]] | 本地 wiki/workflow 可能借用检索思想，但不是 RAG 子类。 | 若卡片改为某类 LLM Wiki / Knowledge Workflow 系统父类再重开。 |
| [[Oh My Codex (OMX)]] | [[Agent Framework]] | OMX 是具体 runtime / workflow ecosystem；不能无审查归入 Agent Framework。 | 若产品边界证明它是某类 Codex orchestration framework，再走新判定。 |
| [[Policy Engine]] | [[Tool Use]] | policy engine 约束工具/动作，不是 tool-use 行为子类。 | 若建立 Policy / Guardrail Runtime 父类再重开。 |
| [[Positional Encoding]] | [[Transformer]] | Transformer component-of，不是 kind-of Transformer。 | 若建立 Transformer Component / Representation Mechanism 父类再重开。 |
| [[Prompt Injection]] | [[Prompt]] | Prompt Injection 操纵 prompt，但它是 attack class，不是 Prompt 子类。 | 若建立 Prompt Attack / LLM Security Risk 父类再重开。 |
| [[Sandbox Workspace]] | [[Tool Use]] | sandbox workspace 承载工具/动作，但 hosting infra 不是 Tool Use 子类。 | 若建立 Workspace / Sandbox / Execution Environment 父类再重开。 |
| [[Self-Attention]] | [[Transformer]] | Transformer component-of，不是 kind-of Transformer。 | 若建立 Attention Mechanism / Transformer Component 父类再重开。 |
| [[Step-back Prompting]] |  | 它是抽象式 prompting / query-side strategy；当前缺 approved Prompting 或 query-strategy 父类，不直接挂到 [[Query Rewrite]] 或 [[Planning]]。 | 若建立 Prompting Strategy / Query-side Retrieval Strategy 父类，或卡片边界改为某个 approved 子类，再重开。 |
| [[Trajectory]] | [[Evaluation]] | Trajectory 是被观察/评估的对象，不是 evaluation 方法。 | 若建立 Trace Object / Agent Run Artifact 父类再重开。 |

审计闭环证明：`defer_boundary_review` 仍可作为语义状态保留，但只要它同时有 `review_status: deferred_with_backlog` 和本节 backlog home，就不再算当前 open tail。未来新增卡片若落入上述边界，必须重开候选生成 / LLM 判定 / dry-run / limited apply，不得直接把 suppressed target 写入 `up`。

## 每周检查清单

- [ ] 更新 [[04 页面目录]]。
- [ ] 跑 missing-link scan。
- [ ] 跑固定审计命令：
  - `python3 scripts/concept_card_audit.py --format markdown`
  - `python3 scripts/comparison_topic_audit.py --format markdown`
  - `python3 scripts/paper_source_audit.py`
  - `python3 scripts/interview_question_concept_links.py --self-test`
  - `python3 scripts/interview_question_concept_links.py --dry-run`
  - `python3 scripts/concept_taxonomy/validate.py`
  - `python3 scripts/concept_taxonomy/plugin_contract_verification.py`
  - `python3 scripts/concept_taxonomy/control_surface_sync.py`
  - `python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py`
  - `python3 scripts/request_meta_audit.py --format markdown`
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

## 2026-05-17 小林 Note source refresh

本轮修复的是 source updater 与当前 raw/repos 布局不一致的问题，并刷新小林 Note sitemap 面试题页。它属于脚本驱动的系统性维护：raw source、索引、导航、健康检查和日志需要同步，但不直接把新题目提升为概念卡。

| 检查项 | 结果 | 处理 |
|---|---:|---|
| `scripts/update_xiaolinnote.py` | 142 URLs；新增 22；变化 120；失败 0 | 写入 `raw/repos/xiaolinnote/questions/`，按 URL 复用旧页 |
| `scripts/interview_question_concept_links.py --apply` | 修改 81 页；插入 170 个链接 | 新增/刷新题页补齐现有概念回链 |
| `scripts/interview_question_concept_links.py --dry-run` | 扫描 779 题页；would modify 0；missing 0；protected violations 0 | 链接写回后无剩余自动修复项 |
| `scripts/update_xiaolinnote.py --dry-run` | 142 checked；new 0；changed 0；unchanged 142；errors 0 | updater 当前幂等 |
| 固定审计与 diff 检查 | concept audit 130 / needs 0；comparison audit 23 / needs 0；paper audit 45 PASS；`git diff --check` PASS | 本次系统性刷新未制造新的健康检查缺口 |

边界：本轮只刷新小林 Note raw evidence 与题页回链；`agent_java_offer` 远端 `main` 没有新提交，因此不更新；没有新增弱概念卡，也没有改 alias map / 字段规范 / 概念卡模板。

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

## 2026-05-16 审计队列一次性批量维护

用户明确授权一次性处理上一轮健康检查留下的 27 张概念卡和 6 张对比 topic。本轮属于系统性批量维护，但没有改变字段语义、alias 规则、概念卡标准或对比页模板规则；因此控制面同步范围限定为本页当前状态与 `log.md`。

### 修复结果

| 检查项 | 修复前 | 修复后 | 处理 |
|---|---:|---:|---|
| Concept Card Audit | 130 张概念卡；Needs action = 27 | 130 张概念卡；Needs action = 0 | 补 `## 概念详解` 深度、`Evidence type:`、`Boundary:` |
| Comparison Topic Audit | 23 张对比 topic；Needs action = 6 | 23 张对比 topic；Needs action = 0 | 补必备 section、证据类型 / 置信度 / 边界标记、核心表链接锚点 |

### 维护边界

- 没有新增概念卡、没有改 canonical name、没有改 `aliases` 或面试题 alias map，因此没有触发新的中英术语映射落库或新概念 backlink sweep。
- 没有改 raw source；概念卡和对比页只补学习解释、证据类型和边界说明。
- 本轮没有新增 27+6 修复规则；`AGENTS.md`、[[字段规范]] 和模板未改，[[LLM Wiki 工作流]] 无 27+6 相关规则变更。若工作树中存在概念关系写回门禁 diff，它属于独立关系建模维护，不计入本轮验收。

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
