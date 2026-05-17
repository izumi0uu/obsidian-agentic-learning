---
type: map
topic:
  - obsidian
  - llm-wiki
  - workflow
status: active
created: 2026-05-05
updated: 2026-05-17
source: /Users/idah/Downloads/llm-wiki.md
related:
  - "[[Agent 知识地图]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[06 Wiki 健康检查]]"
  - "[[08 面试题概念卡待补充]]"
  - "[[08 面试题概念链接待办]]"
  - "[[09 概念层级审计基线]]"
  - "[[字段规范]]"
  - "[[资料收集索引]]"
---

# LLM Wiki 工作流

这页把 `llm-wiki.md` 的方法改造成当前 Agent 学习 vault 的操作规则。

核心思想：不要让 LLM 每次回答问题时都从 raw 资料里重新拼答案，而是让 LLM 持续维护一个可增长的 wiki。raw 是来源，wiki 是已经沉淀的理解，maps 是导航。maps 是稀缺控制面，不是每次录入资料时自动生成的批次记录。

## 三层结构

```text
raw/  -> source notes, immutable evidence
wiki/ -> concept cards, topics, projects, people
maps/ -> durable navigation, durable indexes, workflow, questions, frontier tracking
```

学习过程记录单独放在 `reviews/`：

```text
reviews/ -> concept-triggered review, Feynman answers, write-back candidates
```

小边界：`reviews/` 记录“我怎么检查自己有没有懂”，不替代 `wiki/` 的稳定概念卡，也不作为 `raw/` 的来源证据。

## Map 准入边界

`maps/` 只放会长期帮助“下一步去哪”的控制面。不要把每次 source batch、paper batch、repo batch 或“近期 / 速读”收集都做成新 map。

允许创建或更新 map 的情况：

- 用户明确要求一个阅读路线、索引、健康检查、问题池、前沿追踪或工作流规则。
- 新内容改变了长期导航，例如新增稳定主题、核心概念群、对比入口或维护流程。
- 现有 map 已经承载这个职责，只需要小范围追加入口或状态。

不应该创建或扩散 map 的情况：

- 只是一次论文 / 资料录入批次，不会长期作为学习入口。
- 只是为了记录“近期论文速读入口”“速读清单”“第 N 梯队清单”这类临时分组。
- 只是因为本轮新增文件很多，就把它们复制到多个 topic / index 页面。

替代归宿：

- 批次来源记录：写入 [[资料收集索引]] 的对应来源区，或保留在 raw source note。
- 不稳定但重要的问题：写入 [[02 问题池]]。
- 值得未来整理的理解：写入 [[05 Query 写回队列]]。
- 前沿观察：写入 [[03 前沿追踪]]，不要为每个批次新建 map。

写回约束：追问卡一旦回答完，每张卡都必须有写回归宿。成熟、稳定、可复用的边界写回 `wiki/concepts/` 或 `wiki/topics/`；还不稳定但值得保留的缺口写入 [[02 问题池]] 或 [[05 Query 写回队列]]；不能只把反馈留在 `reviews/` 里就结束。

## 用户请求元信息隔离

用户在提问里夹带收录决策或执行请求时，这些词是操作意图，不是知识内容。LLM 只能把最后沉淀出的概念、边界、证据和学习价值写进 wiki，不能把当时的请求话术写进概念卡、主题页或 source note 正文。

硬性规则：凡是只负责说明“谁提供的、哪个批次、先录到哪、前沿判断见哪、为什么先收/先读”的 intake / batch / provenance 话术，一律不得保留为 source note、topic 页或概念卡正文；需要时只能转写成中性的证据锚点、学习价值或写回队列说明。

必须过滤掉的元信息：

- 收录价值判断、是否建卡或是否进入 wiki 的决策话术。
- 用户顺口带入的项目名、任务名、临时文件名、个人偏好和本轮 agent 指令，除非它们就是本页要记录的主题。
- agent 执行过程、本轮判断、这个问题可保留等过程描述。

推荐改写：

- 把收录价值判断改成“学习价值在于”“应沉淀为某类边界”“证据支持的核心概念是”。
- 把建卡决策问题改成“X 是否已经有稳定概念边界、证据锚点和复习价值”。
- 把用户请求原句只放在 [[05 Query 写回队列]] 的问题栏时也要做语义净化：保留知识问题，不保留录入请求话术。

验收规则：`wiki/`、`raw/` 的 synthesis 段落、`maps/05 Query 写回队列.md` 的问题栏，都不应出现用户侧收录决策关键词；历史 log 可以记录操作，但也应优先写成中性边界语言。

项目脚本：`python3 scripts/request_meta_audit.py --format markdown` 是请求 / 会话元信息隔离的固定审计入口。它扫描 `wiki/`、`raw/`、`maps/`、`reviews/` 和 `log.md`，用于发现聊天包装、hook 文本、goal reconciliation 片段和请求路由话术是否被误写入 durable vault 页面。误报要先收窄规则或加明确边界，不要为了通过审计删除真实技术概念内容。

## 中英文术语对齐 / Bilingual Terminology Audit

当任务涉及新增概念卡、更新概念卡、给面试题/raw 正文加概念链接、维护 alias map、或整理一批中文面试题术语时，必须先做中英文术语对齐。目标不是把所有中文词都建卡，也不是把规则写成词表；目标是避免“中文词被错误映射到相邻英文概念”，并把可复用的边界沉淀到合适的知识层。

### 触发条件

- 中文术语和英文术语同时出现，且可能对应不同边界（例如 route、metric、sub-strategy、component）。
- 中文资料使用了工程俗称，但 `wiki/concepts/` 里只有英文概念卡。
- 一个中文词可能对应多个英文边界，例如“召回”可能是 retrieval、recall metric、candidate generation。
- 批量脚本、team、alias map 或 raw-question 内联链接会影响很多页面。

### 审计步骤

1. 同时搜索中文词、英文候选名、缩写和常见变体：`wiki/concepts/`、`wiki/topics/`、`raw/`、`maps/`、`scripts/interview_question_concept_aliases.json`、[[08 面试题概念卡待补充]]。
2. 建立术语判断表，至少记录：中文术语、英文候选、当前链接、是否已有概念卡、是否在 alias map、证据页、判断、风险。
3. 每个术语只能进入一个状态：
   - 已有概念卡：补 `aliases`、正文边界或 alias map。
   - 新建概念卡：有足够 evidence 和边界，按概念卡标准写入。
   - 并入已有卡：术语只是已有卡的别名、子策略或指标，不单独建卡。
   - 候选 backlog：英文 canonical name、证据或边界不稳。
   - 禁止映射：属于 false friend，后续 alias map 不得自动链接。
   - 术语判断表是工作表，不是规则词表；细分案例写进审计报告、概念卡或 backlog，不回灌成项目规则。
4. canonical name 选择优先级：
   - 论文、官方文档或事实标准中的稳定英文名优先。
   - 社区工程常用英文名其次。
   - 仅来自中文材料的直译名不直接升格为卡名；先进入候选 backlog。
   - 如果英文名不确定，宁可写 `pending`，不要创建弱卡。
5. 对高混淆词必须写边界：它和相邻概念最小区别是什么、为什么不能简单等号、是否只是组合关系或代表关系。

### 落地同步

确认一个术语后，按影响面同步：

- 新建/更新 `wiki/concepts/<Canonical Name>.md`，技术概念优先用稳定英文卡名。
- 在概念卡 frontmatter `aliases` 记录中文名、缩写和常见写法。
- 必要时更新 `up` / `relations`，区分严格上位、代表、组合、思想来源和普通相关。
- 若面试题自动链接需要识别该术语，更新 `scripts/interview_question_concept_aliases.json`。
- 更新相关 raw-question 页的 `related` 和 `## 相关知识 wiki`，但不把 raw source 改写成概念解释。
- 不确定项写入 [[08 面试题概念卡待补充]]；更宽的整理问题写入 [[05 Query 写回队列]]。
- 追加 `log.md`，说明本次同步了哪些控制面。

### 反例边界

- 不要把宽泛中文工程俗称直接等同为某个狭义英文卡名。
- 不要把通用词直接挂到别的技术领域的同名概念上。
- 不要把评估指标、子策略、代表算法当成同义词。
- 不要把行为层、接口层和能力集合混成一个 alias 族。
- 例如：`多路召回` 不能默认等于 [[Hybrid Search]]；Hybrid Search 常指 sparse + dense / vector + BM25 的混合；多路召回可以更宽，包括多 Query、图检索、metadata filter、不同索引粒度或多 retriever。
- 例如：`Memory` 不能默认链接 JVM memory、off-heap memory 或数据库缓存。
- 例如：`ReAct` 不能默认链接 Netty Reactor。
- 例如：`Context Recall` 是 RAG evaluation 指标，不是普通“召回层”的同义词。

### 验收

- 已有概念卡、中文别名、alias map 和 raw-question 链接不互相矛盾。
- 不稳定术语进入 backlog，而不是弱概念卡。
- false friend 有明确禁止映射或边界说明。
- 批量改动后至少运行 `git diff --check`；涉及面试题内联链接时运行：

```bash
python3 scripts/interview_question_concept_links.py --self-test
python3 scripts/interview_question_concept_links.py --dry-run
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
```

## 新概念反向提及扫描 / New Concept Mention Backlink Sweep

新增概念卡、确认新的 canonical name、给旧卡补重要 alias、或扩大概念边界后，必须回扫项目里已经提到该概念的地方，补上正确引用。目标是让新卡进入已有知识网络，而不是成为孤立页。

### 触发条件

- 新建 `wiki/concepts/<Concept>.md`。
- 旧概念卡新增重要中文名、英文名、缩写或同义工程说法。
- 从 backlog/面试题/raw 中确认一个术语应落到某张卡。
- 修改 `scripts/interview_question_concept_aliases.json`，导致同一概念未来会自动链接更多页面。

### 回扫步骤

1. 生成搜索词组：canonical title、中文 aliases、英文变体、缩写、常见大小写和连字符/空格变体。
2. 搜索范围至少覆盖：`wiki/concepts/`、`wiki/topics/`、`raw/`、`maps/`、`reviews/`、`scripts/interview_question_concept_aliases.json`；本地运行时优先用 Obsidian hybrid search，再用 `rg` 做确定性复核。
3. 对命中逐条分类：
   - 同一概念：补 `[[Concept]]` 或 `[[Concept|中文术语]]`。
   - raw/source 证据页：不改写原文或长摘；只更新 frontmatter `related`、`## 相关知识 wiki`、中性 synthesis、或证据锚点。
   - 相邻概念/上下位/组合关系：必要时写入 `relations` 或正文边界，不把它当同义链接。
   - false friend / 歧义命中：不链接；把禁止映射或待判定项写入边界、[[08 面试题概念卡待补充]]、[[05 Query 写回队列]] 或 [[06 Wiki 健康检查]]。
   - 高频重复命中：只链接首个学习有效位置，避免每句都加链接。
4. 同步双向关系：新卡的 `source` / `evidence` / `related`，提及页的 `related` 或 `## 相关知识 wiki`，以及必要的主题页、地图和索引。
5. 在 log 中记录搜索词、主要落点、跳过/不链接的边界。

### 验收

- 新概念卡不是孤立页；至少说明已搜索哪些 aliases/变体。
- 已知同义中文提及能跳到 canonical 卡；歧义提及没有被强行链接。
- raw 证据层没有被改写成概念解释。
- 至少运行：

```bash
git diff --check
```

若修改了面试题链接脚本或 alias map，还要运行：

```bash
python3 scripts/interview_question_concept_links.py --self-test
python3 scripts/interview_question_concept_links.py --dry-run
```

## 概念关系批量写回门禁 / Relation Writeback Gate

当任务涉及全库概念关系评估、脚本生成候选边、或把 `up` / `relations` 写回多张概念卡时，必须把它当系统性变更处理。临时关系图只是证据雷达，不是最终 taxonomy。

### 触发条件

- 从 `scripts/concept_taxonomy/`、`reports/concept-card-relation-map/`、审计脚本或其它批量工具生成候选关系。
- 准备给多张 `wiki/concepts/*.md` 新增或修改 `up`。
- 准备把普通 `related`、正文 wikilink、topic family 或标题启发式升格为层级关系。

### 强制流水线

1. **临时图全量生成**：先生成全库关系图，记录现有 `up`、`relations`、`related`、正文 wikilink 和候选边。
2. **候选关系台账**：每条 candidate 必须有明确 decision：`accept_taxonomy`、`reject_taxonomy`、`defer_taxonomy`、`adjacency_only` 或 `duplicate_signal`。
3. **dry-run 写回**：只把 `accept_taxonomy` 且目标字段为 `up` 的边放入 dry-run；dry-run 不改概念卡。
4. **剩余 accepted 复核**：每轮 apply 前，必须复核 dry-run 中剩余 accepted rows；若发现“标准/运行时/能力/机制支撑某父概念但不是其子类”，要降级为 `reject_taxonomy` 或 `defer_taxonomy`，不能因为上一轮已 accepted 就继续写入。
5. **小批量 apply**：写回必须带 limit，例如 `writeback.py --apply --limit 12`；禁止无界全量 apply。若使用逐卡层级归属台账，则必须走 `taxonomy_placement_review.py --apply-reviewed --limit N`，且输入只能来自已判定、已 dry-run 的 ready set。
6. **非层级边界守卫**：对“表示/特征 → 方法族 → 召回路线 → 编排策略”这类高混淆链条，台账和验证必须显式阻止写入 `up`。
7. **插件兼容验证**：验证只新增子卡顶层 `up`；不手写 `down`、不常规化 `children`、不新增 Juggl 或 Breadcrumbs 非 taxonomy 镜像字段。
8. **重建与验证门禁**：每次有限写回后必须重新生成临时图、台账、dry-run 和插件验证报告；插件契约报告必须证明 post-apply dry-run 为 0、apply report 中的历史写回边仍真实存在于子卡 `up`，且没有 `down` / `children` / Juggl / Breadcrumbs mirror 字段。
9. **尾巴闭环**：`defer_taxonomy` / `needs_review` 是开放尾巴，必须回到概念卡证据或 backlog 后再终止；`reject_taxonomy` / `adjacency_only` 若有明确理由、`resolution_status=terminal_non_writeback` 且不写 `up`，就是已闭环终态，不应再算待办。
10. **审计完成闭环**：可以把剩余 `defer_boundary_review` 关闭为 `review_status: deferred_with_backlog`，前提是每条都有明确 backlog home、suppressed-target 理由和 reopen trigger；这不是写 `up` 的许可。
11. **日志与控制面同步**：若规则或脚本行为改变，更新本页、字段规范/计划文档和 `log.md`；控制面/完成闭环报告要明确哪些表面已更新、哪些因字段语义未变而故意不改，并记录 `open_writeback: 0` 时不允许直接写回。
12. **稳定基线镜像**：审计闭环后，应把逐卡审计摘要导出到 [[09 概念层级审计基线]]；未来新增概念卡先对照这张基线判断是否进入已审计父类、terminal no-up、或 deferred-with-backlog。
13. **项目内工具入口**：概念关系治理的长期工具入口是 `scripts/concept_taxonomy/`，机器基线保存在 `reports/concept-card-relation-map/`。新增概念卡或复跑审计时，优先运行项目脚本；字段规范与模板不改，除非 `up` / `relations` 语义或页面形状发生变化。

### 判定边界

- `up` 只表示严格上位 / belongs-to。
- `relations` 表示非 taxonomy 的 typed relation，需要 `type + target + note`。
- `related` 是普通邻接，不证明父子。
- 正文 wikilink 是提及证据，不证明父子。
- `topic_family_review` 只能用于分组复核，永远不能直接写入 `up`。
- 标题规则只能提出候选；除非卡片正文/一句话/边界支持“X 是 Y 的一种”，否则不能落地。
- “支撑/标准化/承载/执行”不是 taxonomy：例如 OpenTelemetry GenAI 支撑 Observability 的语义记录，State Graph Runtime 执行 Agent Workflow，但它们不是对应父概念的子类。
- 检索链条要区分语义层：[[TF-IDF]] 是 sparse lexical weighting / 基础表示直觉；[[Sparse Retrieval]] / [[BM25]] 可以成为召回路线或路线代表；[[Multi-Route Retrieval]] 是组织多条路线的策略。TF-IDF 不是 Multi-Route Retrieval 的一种；Sparse Retrieval 进入多路召回应写 `relations`（如 `composed_into`），不能写成 `up`。
- `foundational_for`、`based_on_intuition`、`composes_with`、`composed_into` 这类关系即使很重要，也必须停在 `relations`，除非另有正文证据证明它同时满足 strict taxonomy。

### 验收

- 台账覆盖所有候选边，并保留 reject / defer 的理由。
- 台账对已知高混淆检索边界保留 `boundary_guardrail_applied` 或等价说明；dry-run / apply report 不得出现这些 forbidden non-taxonomy `up` pair。
- apply report 能列出每张被修改的概念卡、目标父概念和理由。
- 重新生成临时图后，新增 taxonomy 边数量与 apply report 对得上。
- 当一批 accepted edges 已全部写回后，post-apply dry-run 可以是 0 planned；前提是 ledger 的 `writeback_candidates` 同步为 0，且 apply report 中的历史写回边仍真实存在于子卡 `up`。
- 对“层级归属待审计概念卡”流程，limited apply 后必须重新生成临时图和 `concept-hierarchy-placement-review`；`concept-hierarchy-placement-apply-report` 要记录输入 dry-run、selected/applied 数、post-apply dry-run，并证明 rejected rows 未进入 planned/applied。
- 插件契约验证报告必须由 `python3 scripts/concept_taxonomy/plugin_contract_verification.py` 生成并保持 0 problems；若 `.obsidian/` 不在仓库中，验证的是 durable contract，不是 live plugin setting。
- 控制面同步报告必须记录项目脚本、项目报告、健康检查、基线页和日志状态；若 `字段规范.md` / 模板未改，应说明原因是字段语义和页面形状未变化。
- 完成闭环报告必须证明 `open_review: 0`、`open_writeback: 0`、`dry_run_planned: 0`，且剩余 `defer_boundary_review` 全部为 `deferred_with_backlog`；不得为了让 `defer_boundary_review` 归零而强行写父类。
- 最终闭环状态下，`open_review_items` 必须为 0；若 `reject_taxonomy` / `adjacency_only` 仍有数量，它们必须带有终态理由和 `terminal_non_writeback` 状态，而不是未完成尾巴。
- Abstract Folder / Breadcrumbs 兼容检查 0 problems。
- `git diff --check` 通过；若存在本任务外的历史 diff，最终报告必须说明边界，不得误称全部由本次写回产生。

## 角色分工

### 用户负责

- 选择值得收集的资料。
- 提出问题。
- 判断哪些解释真的帮助自己理解。
- 确认概念是否已经能用自己的话说明。

### LLM 负责

- 整理 source note。
- 生成和更新 concept card。
- 补双链。
- 发现矛盾、重复、缺口和孤立页。
- 维护索引和 log。

## 检索工具默认顺序

当任务是回答 vault 内问题、维护 wiki 页面、查找概念边界、整理相关页或做健康检查时，优先使用 Obsidian hybrid search MCP 工具，再做大范围文件系统搜索。

推荐顺序：

1. `obsidian_status`：确认索引可用、是否最新、忽略规则是否正确。
2. `obsidian_search`：用于概念 / topic 发现、相关页召回、标题模糊搜索、语义召回和多 query fan-out。
3. `obsidian_read`：在综合、修改或引用前读取精确页面正文。
4. 当任务是概念对比、wiki 写入、判断生成或引用证据时，如果 `obsidian_read` 返回内容出现 truncated，应单独重读核心页面，并提高 `snippet_length` 或取消截断后再下结论。
5. `rg` / 直接读文件：用于 MCP 不可用、索引陈旧、已知精确路径、脚本符号搜索或需要验证未索引文件时。

边界：检索工具只改变“怎么找资料”，不改变三层知识边界。回答和写回仍然先从 `wiki/` 与 `maps/` 形成理解，`raw/` 只作为证据；不要因为语义搜索召回了 raw note，就直接把 raw 内容当成稳定概念解释。

运行态边界：不要把代理、模型缓存、MCP 安装命令或本机 Codex 配置写入 wiki 正文。`.omx/**`、`.codex/**`、`.obsidian/**`、templates 和 canvas 文件应保持在 hybrid search 索引之外。

## 操作 1：Ingest

当用户说“ingest 这篇资料”“处理这个 raw note”“把这篇文章进 wiki”时执行。

步骤：

1. 读取 raw source note。
2. 确认它的 `type: source`、`source_type`、`topic`、`url`、`status`。
3. 提取 3 类内容：关键主张、可拆概念、不懂的问题。
4. 更新或创建 `wiki/concepts/` 里的概念卡。创建或更新前，先执行 [[LLM Wiki 工作流#操作 6：现代性 / 前沿性判定]]，判断这个概念应放在基础地基、历史过渡、当前工程实践还是前沿 / 易变层。
5. 给概念卡补 `source` 和 `evidence`。没有段落级证据时，至少链接到 source note 小节。
6. 如果涉及主题聚合，更新 `wiki/topics/`。
7. 如果影响长期导航或复习方式，优先更新现有 map：`maps/Agent 知识地图.md`、[[02 问题池]]、[[03 前沿追踪]]、[[05 Query 写回队列]] 或 [[04 页面目录]]。不要仅因本轮录入了一批资料就新建“速读清单 / 近期入口 / 梯队清单”类 map。
8. 将 source note 的 `status` 从 `inbox` 改成 `seed` 或 `growing`，并补 `last_checked` / `freshness`。
9. 追加 `log.md`。

### 概念卡写法

默认把 `wiki/concepts/` 写成“双层学习 + 判断卡”，而不是百科条目。

- 学习层：让自己能从问题、例子、误解和复述进入概念。
- 判断层：让自己能判断边界、适用条件、现代工程吸收方式、证据强弱和复习问题。

学习层必须足够显性，不能只靠“一句话 + bullet”让人猜。对 qualified / anchor 卡，`## 概念详解` 是主体段落，应该承担最高解释比重；`## 一句话` 只是入口，不等于整张卡只能写一句话。

优先保留这个骨架：

1. `## 一句话`
2. `## 概念详解`：主体段落，解释概念为什么出现、机制是什么、论文/官方文档/社区实践如何描述它，以及哪些是工程综合理解
3. `## 它解决什么问题`
4. `## 它不是什么`
5. `## 最小例子`
6. `## 常见误解` 或 `## 风险`
7. `## 边界细节`
8. `## 现代性状态`：LLM 必须主动判断 foundation / transitional / current-practice / frontier / 不适用。不是前沿就说明为什么不是前沿。
9. 对 Agent、prompting、framework、evaluation 类概念，必要时补 `## 现代系统怎么吸收 X 的价值` 或 `## 现代系统怎么吸收 X 的局限`
10. `## 证据锚点`
11. `## 复习触发`
12. `## 相关链接`

写法参照 [[Plan-and-Solve Prompting]]：先从这个概念自己解决的问题讲起，再用“它不是什么”“常见误解”和“边界细节”把邻近概念切开；录入时由 LLM 主动判断现代性状态。如果它来自论文时代的 prompt / agent 范式，还要说明现代系统如何把它包进 workflow、tool calling、state、guardrails、trace、evaluation 或 human-in-the-loop。

如果嵌入用户提供的图片或重绘 asset，必须在正文说明这张图是原论文内容、用户截图重绘，还是帮助理解的工程类比；并在 `## 证据锚点` 里写明 asset 路径。

#### “不是浅卡”的验收标准

一张够格概念卡至少满足：

- 有 `## 一句话`，但正文不只停在一句话。
- qualified / anchor 卡必须有 `## 概念详解`，并且它是解释主体：说明概念来源、机制、文档/论文/社区描述、现代工程吸收方式和证据边界。
- 有 `## 它解决什么问题`，说明没有这个概念时会出现的具体困难。
- 有 `## 它不是什么`，至少切开 1-2 个邻近概念或常见混淆。
- 有 `## 最小例子`；如果概念不适合例子，要说明原因并给替代反例或类比。
- 有 `## 常见误解` 或 `## 风险`。
- 有 `## 边界细节`，写适用条件、反例、邻近概念差异或工程落点。
- 对 Agent、prompting、framework、evaluation、RAG、memory、tooling、安全、协议或产品生态，写 `## 现代性状态`；必要时补现代系统吸收价值/局限的段落。
- 有 `## 证据锚点`，区分 source evidence、工程类比、用户截图/重绘等非原文证据。
- 有 `## 复习触发`，给出能检验用户是否真的理解的 1-3 个问题。

#### 深度分级

| 深度 | 适用对象 | 最低要求 |
|---|---|---|
| seed-lite | 暂存弱概念、待验证术语 | 骨架可不完整，但必须写清缺口；优先放 [[02 问题池]]，不要大量创建弱卡 |
| qualified | 大多数稳定概念卡 | 满足“不是浅卡”的验收标准；有 `## 概念详解` 主体段落；证据锚点到 source note 小节 |
| anchor | 地基概念、常用对比概念、风格样板 | `## 概念详解` 必须充分；多段解释、邻近概念边界、现代系统吸收、复习触发和相关链接都要完整 |
| volatile | API、SDK、产品能力、前沿协议 | 除 qualified 外，还要 `last_checked`、`freshness: watch/volatile`，并在 [[03 前沿追踪]] 或 [[06 Wiki 健康检查]] 留观察项 |


### 概念对比 / 类比 topic 页写法

当用户提出“X vs Y”“这些概念容易混”“帮我做类比/对比”时，优先判断是否应该创建 `wiki/topics/` 下的对比 topic 页，而不是把所有内容塞回单张概念卡。对比页的目标不是百科式重复每张卡，而是训练边界判断：这组概念为什么容易混、共同问题域是什么、最小区别在哪里、现代系统分别吸收了什么。

#### 准入标准

一个概念组值得对比，通常要同时满足多项条件：

- 学习者混淆风险高：名称、场景、表面结构或常见说法相近。
- 解决相近问题，但介入点不同：例如计划、行动、观察、评价、反思、记忆或权限边界不同。
- 有足够证据锚点：每个概念至少能回到概念卡、source note、paper、官方文档或可信社区来源。
- 能产出现代工程边界：对比能说明现代 Agent / RAG / evaluation / framework 如何吸收、限制或替代这些思想。
- 能生成复习问题：对比结果能变成判断题、反例题或 Feynman 复述题。
- 数量不固定：可以是 2 者、3 者或 N 者；数量由混淆风险和证据密度决定。

如果只是名字相似、没有清楚证据、或对比不能产生边界判断，就不要新建弱对比页；先写入 [[05 Query 写回队列]] 或 [[02 问题池]]。

#### 推荐结构

对比 topic 页优先使用 [[概念对比页]] 模板，并保留这些 section：

1. `## 一句话总览`：快速入口，不替代正文。
2. `## 为什么这组值得对比`：说明准入理由。
3. `## 共同问题域`：它们为什么可以放在一起比。
4. `## 核心区别表`：概念、介入点、时序/loop、输入输出、证据锚点。
5. `## 最容易混淆的边界`：pairwise 或 N-way 边界刀口。
6. `## 执行时序 / 机制差异`：必要时用伪流程说明 plan / act / observe / reflect / evaluate 的位置。
7. `## 学习类比（非证据）`：可选；必须标明只是 learning analogy。
8. `## 现代系统如何吸收或限制`：来源支持或明确标注为工程推论。
9. `## 什么时候用哪个判断`：写适用条件和风险，不写空泛建议。
10. `## 它们共同不是什么`：防止把整组概念误当成 Agent / framework / 训练方法等。
11. `## 证据锚点`：列出概念卡、source note、paper/docs anchor 和证据边界。
12. `## 复习触发`：输出能检验理解的题。
13. `## 相关链接`：回链到被比较概念和相邻 topic。

#### 证据边界

- 核心定义必须有来源锚点。
- 差异判断必须能回到概念卡或 source note 的证据段。
- 现代工程吸收方式如果来自官方文档或实践来源，要写出来源；如果是 LLM 综合推论，要明确标注为“工程综合 / inference”。
- 生活类比、工程类比只能帮助学习，不能冒充论文或官方文档原意。
- 对比页可以轻量回链到概念卡，但不要借机批量重写旧卡。

边界：统一模板不等于所有卡同样长；它要求每张卡能说明自己的证据、边界和学习检查点。

## 操作 2：Query

当用户问“Agent 和 RAG 有什么区别”“帮我基于 wiki 回答”时执行。

步骤：

1. 从 `index.md` 和相关 map 找入口。
2. 优先读 `wiki/concepts/` 和 `wiki/topics/`。
3. 需要证据时再读 `raw/`。
4. 回答时引用相关 Obsidian 页面。
5. 如果答案值得长期保存，必须写回以下位置之一：
   - 更新已有 `wiki/concepts/` 或 `wiki/topics/`。
   - 追加到 [[05 Query 写回队列]]，标记为 `pending`。
   - 如果只是疑问，追加到 [[02 问题池]]。

写回标准：凡是出现了新定义、新边界、新对比、新操作流程或纠正旧误解，都不应该只停留在聊天回答里。

## 操作 3：Lint

当用户说“lint wiki”“检查这个知识库”“整理一下”时执行。

检查：

- 是否有 raw source 没有被消化。
- 是否有概念卡没有 `它不是什么`。
- 是否有概念卡缺少 `## 边界细节`。
- 是否有 Agent / prompting / framework / evaluation / RAG / memory / tooling / security / protocol / product-ecosystem 概念卡缺少 `## 现代性状态`。
- 是否有概念卡缺少 `## 复习触发`，导致无法进入 `reviews/` 学习检查。
- 是否有概念卡实际只是一句话解释，没有问题背景、例子、边界或证据。
- 是否有孤立页。
- 是否有同义重复页。
- 是否有重要术语只出现为纯文本，未变成 `[[双链]]`。
- 是否有过期或互相矛盾的说法。
- 是否有缺失 frontmatter 的页面。
- 是否有概念卡缺少 `## 证据锚点`。
- 是否有 `freshness: watch/volatile/stale` 且 `last_checked` 过久的 source。
- 是否有同一概念在不同页面里出现互相冲突说法。

输出：

- 先列问题。
- 再做小范围修复。
- 大规模重构前先说明风险。

## 操作 4：Weekly Maintenance

每周做一次，不等用户积累到混乱后再整理。

1. 更新 [[04 页面目录]]。
2. 运行 missing-link scan。
3. 检查概念卡是否有 `它不是什么`、`边界细节`、`证据锚点` 和 `复习触发`。
4. 检查 raw source 的 `status`、`last_checked`、`freshness`。
5. 处理 [[05 Query 写回队列]] 中的 pending 条目。
6. 更新 [[06 Wiki 健康检查]]。
7. 追加 `log.md`。

固定审计命令：

```bash
python3 scripts/concept_card_audit.py --format markdown
python3 scripts/comparison_topic_audit.py --format markdown
python3 scripts/paper_source_audit.py
python3 scripts/interview_question_concept_links.py --self-test
python3 scripts/interview_question_concept_links.py --dry-run
python3 scripts/request_meta_audit.py --format markdown
git diff --check
```

写回规则：每次 weekly / systemic maintenance 都要把最新统计写回 [[06 Wiki 健康检查]] 的“当前状态”或新增 dated 小节，包括概念卡 needs-action、对比 topic needs-action、paper source audit、面试题链接 dry-run、请求元信息审计和 `git diff --check` 结果。旧数字保留为历史记录，但不得继续放在“当前状态”里冒充现状。

## 操作 5：Freshness / Contradiction Check

当资料可能过期，或者同一概念来自多个快速变化来源时执行。

检查顺序：

1. 优先看 source note 的 `freshness` 和 `last_checked`。
2. `stable` 通常不主动查新；`watch` 每月看一次；`volatile` 每 1-2 周看一次；`stale` 优先处理。
3. 发现新版本或冲突时，不直接覆盖旧卡；先写进 [[06 Wiki 健康检查]] 的“待复查 / 潜在矛盾”。
4. 更新概念卡时，在“证据锚点”里保留新旧来源的边界。

## 操作 6：现代性 / 前沿性判定

当用户问“这个现在还成立吗”“现代系统怎么吸收 X 的局限”“这是前沿还是历史过渡”，或 LLM 正在创建 / 更新概念卡时，不直接把它归为前沿。先把问题拆成四类：

- 基础地基（foundation）：论文、经典方法、稳定概念，主要帮助理解语言和边界。例如 [[ReAct]] 作为 reasoning/action/observation 交替思想。
- 历史过渡（transitional）：曾经主要靠 prompt 或手写格式实现、今天多被框架接管的形态。例如裸 `Thought -> Action -> Observation` prompt loop。
- 当前工程实践（current-practice）：多个框架或官方指南共同采用、已经相对稳定的工程吸收方式，例如 [[Tool Calling]]、显式 [[Agent State]]、[[Agent Workflow]] / graph、[[Guardrails]]、[[Trace]] / [[Evaluation]]、[[Human-in-the-loop]]。
- 前沿 / 易变（frontier / volatile）：具体 SDK/API、协议、产品、评测榜单或快速演进实现，例如某个 Agents SDK 的 guardrails、tracing、sessions、computer use、MCP 集成接口。

一句判断规则：

> 论文范式通常是基础地基或历史过渡；框架吸收方式通常是当前工程实践；具体 SDK/API/产品能力才更可能是前沿或易变。

执行步骤：

1. 先读对应概念卡，确认它原本解决的问题和“它不是什么”。
2. 再查最小证据集：一个原始来源（论文 / 原文）加至少一个现代官方工程来源（框架文档、SDK 文档或官方实践指南）。
3. 给出四类判定，并说明哪些部分稳定、哪些部分需要 `freshness: watch/volatile`。
4. 写回概念卡的 `## 现代性状态` 或 `## 现代系统怎么吸收 X 的价值/局限`。
5. 如果只是具体产品或 API 变化，优先更新 source note 的 `last_checked` / `freshness`，并在 [[03 前沿追踪]] 或 [[06 Wiki 健康检查]] 里留观察项，不把它误写成稳定概念。

概念卡默认行为：

- 新建概念卡时，除非明显不适用，都要有 `## 现代性状态`。
- 更新旧概念卡时，如果本次更新涉及 Agent、prompting、framework、evaluation、RAG、memory、tooling、安全、协议或产品生态，必须补现代性判定。
- 如果判定为 `frontier / volatile`，不要只写概念卡；还要检查是否需要更新 [[03 前沿追踪]]、source note 的 `freshness`，或 [[06 Wiki 健康检查]]。
- 如果判定为 `foundation` 或 `transitional`，要明确它今天的价值：是稳定语言、历史过渡、工程原则，还是已经被现代系统吸收的内部结构。

写回边界：

- “现代系统怎么做”不等于“这个概念过时了”。很多旧范式会变成现代系统的内部设计原则。
- “某个框架新增功能”不等于“概念定义改变”。只有当多个来源都改变抽象边界时，才更新概念卡定义。
- “模型变强”不等于“runtime 消失”。模型可能更会规划和遵循格式，但工具执行、状态、权限、trace、评测和恢复仍属于 [[Agent Harness]] / [[Agent Framework]] 的工程责任。

## 操作 7：Paper 阅读优先级判定

当 raw paper 数量增加时，不按“最新 / 最多 / 批次顺序”阅读，而按学习杠杆排序。优先级记录在 [[资料收集索引]]，不要为每批 paper 新建 map。

### 判定维度

1. **地基依赖**：是否支撑多个核心概念卡，例如 [[ReAct]]、[[RAG]]、[[Toolformer]]、[[Reflexion]]、[[Agent Harness]]、[[Evaluation]]。
2. **误解纠偏**：是否能纠正常见误解，例如“benchmark 分数等于可靠性”“test pass 等于过程可靠”“tool use 等于 Agent”。
3. **当前路线相关性**：是否直接服务当前学习线，例如 Agent harness、trace、trajectory evaluation、workflow safety、tool security、RAG reliability。
4. **证据成熟度**：是否已有 source note、PDF / extracted text、必读锚点或至少足够摘要证据。只有标题和 abstract 的前沿论文先保持 `seed`。
5. **专题必要性**：是否只在进入某个专题时才需要，例如 GUI memory、多 Agent 优化、医疗 / 灾害高风险应用。

### 优先级含义

| 优先级 | 含义 | 默认动作 |
|---|---|---|
| P0 | 先读 / 精读。它直接支撑当前知识地基或高频判断边界。 | 读完后必须写回概念卡、topic、问题池或复习卡。 |
| P1 | 下一批细读。它直接增强当前 Agent 工程判断，但不一定是所有概念的地基。 | 读时围绕一个明确问题，不从标题直接新建弱概念卡。 |
| P2 | 专题触发阅读。只有进入 memory、GUI、多 Agent、高风险应用等专题时才读。 | 先保留 source note 和问题，不急着升格。 |
| P3 | 背景 / 按需阅读。主要解释模型训练、规模化或对齐背景。 | 当用户问 LLM 能力来源、训练或对齐时再提升优先级。 |

### 规则

- P0/P1 不是“价值最高”的绝对排名，而是对当前 vault 的学习收益最大。
- 新 paper 录入后先给临时优先级；精读后可调整，但必须说明调整原因。
- 如果一篇前沿论文只提供新名词、没有稳定证据或不能改进现有边界判断，默认 P2，不创建新概念卡。
- 如果一篇模型训练论文对 Agent runtime 没有直接影响，默认 P3；当学习 LLM / alignment 主题时可以局部提升。
- 每次维护优先级时，只更新 [[资料收集索引]] 的优先级规则或现有列表，不新建“速读清单 / 梯队清单”map。

## 日志规则

`log.md` 是时间线，追加即可。

建议格式：

```md
## [2026-05-05] ingest | Title

- Source: [[Oh My Codex Repo]]
- Updated: [[Oh My Codex (OMX)]], [[Agent Harness]]
- Questions: OMX 的 team/worktree/hook/state 分别对应 Agent Harness 的哪一层？
```

## 当前项目的调整

原 `llm-wiki.md` 说 LLM 可以完全拥有 wiki 层。这里改成：

> LLM 可以维护 wiki，但学习完成的标准是用户能用自己的话解释。

所以概念卡必须保留边界段落，尤其是“它不是什么”。
