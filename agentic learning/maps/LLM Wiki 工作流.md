---
type: map
topic:
  - obsidian
  - llm-wiki
  - workflow
status: active
created: 2026-05-05
updated: 2026-05-12
source: "/Users/idah/Downloads/llm-wiki.md"
related:
  - "[[Agent 知识地图]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[06 Wiki 健康检查]]"
  - "[[字段规范]]"
  - "[[资料收集索引]]"
---

# LLM Wiki 工作流

这页把 `llm-wiki.md` 的方法改造成当前 Agent 学习 vault 的操作规则。

核心思想：不要让 LLM 每次回答问题时都从 raw 资料里重新拼答案，而是让 LLM 持续维护一个可增长的 wiki。raw 是来源，wiki 是已经沉淀的理解，maps 是导航。

## 三层结构

```text
raw/  -> source notes, immutable evidence
wiki/ -> concept cards, topics, projects, people
maps/ -> index, reading plans, workflow, questions, frontier tracking
```

学习过程记录单独放在 `reviews/`：

```text
reviews/ -> concept-triggered review, Feynman answers, write-back candidates
```

小边界：`reviews/` 记录“我怎么检查自己有没有懂”，不替代 `wiki/` 的稳定概念卡，也不作为 `raw/` 的来源证据。

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

## 操作 1：Ingest

当用户说“ingest 这篇资料”“处理这个 raw note”“把这篇文章进 wiki”时执行。

步骤：

1. 读取 raw source note。
2. 确认它的 `type: source`、`source_type`、`topic`、`url`、`status`。
3. 提取 3 类内容：关键主张、可拆概念、不懂的问题。
4. 更新或创建 `wiki/concepts/` 里的概念卡。创建或更新前，先执行 [[LLM Wiki 工作流#操作 6：现代性 / 前沿性判定]]，判断这个概念应放在基础地基、历史过渡、当前工程实践还是前沿 / 易变层。
5. 给概念卡补 `source` 和 `evidence`。没有段落级证据时，至少链接到 source note 小节。
6. 如果涉及主题聚合，更新 `wiki/topics/`。
7. 如果影响导航或复习方式，更新 `maps/Agent 知识地图.md`、[[02 问题池]]、[[05 Query 写回队列]] 或 [[04 页面目录]]。
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
