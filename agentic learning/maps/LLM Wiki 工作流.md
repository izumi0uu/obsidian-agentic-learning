---
type: map
topic:
  - obsidian
  - llm-wiki
  - workflow
status: active
created: 2026-05-05
updated: 2026-05-10
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
4. 更新或创建 `wiki/concepts/` 里的概念卡。
5. 给概念卡补 `source` 和 `evidence`。没有段落级证据时，至少链接到 source note 小节。
6. 如果涉及主题聚合，更新 `wiki/topics/`。
7. 如果影响导航或复习方式，更新 `maps/Agent 知识地图.md`、[[02 问题池]]、[[05 Query 写回队列]] 或 [[04 页面目录]]。
8. 将 source note 的 `status` 从 `inbox` 改成 `seed` 或 `growing`，并补 `last_checked` / `freshness`。
9. 追加 `log.md`。

### 概念卡写法

默认把 `wiki/concepts/` 写成学习卡，而不是百科条目。优先保留这个骨架：

1. `## 一句话`
2. `## 它解决什么问题`
3. `## 它不是什么`
4. `## 最小例子`
5. `## 常见误解` 或 `## 风险`
6. `## 边界细节`
7. 对 Agent、prompting、framework、evaluation 类概念，必要时补 `## 现代系统怎么吸收 X 的价值` 或 `## 现代系统怎么吸收 X 的局限`
8. `## 证据锚点`
9. `## 相关链接`

写法参照 [[Plan-and-Solve Prompting]]：先从这个概念自己解决的问题讲起，再用“它不是什么”“常见误解”和“边界细节”把邻近概念切开；如果它来自论文时代的 prompt / agent 范式，还要说明现代系统如何把它包进 workflow、tool calling、state、guardrails、trace、evaluation 或 human-in-the-loop。

如果嵌入用户提供的图片或重绘 asset，必须在正文说明这张图是原论文内容、用户截图重绘，还是帮助理解的工程类比；并在 `## 证据锚点` 里写明 asset 路径。

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
3. 检查概念卡是否有 `它不是什么` 和 `证据锚点`。
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

当用户问“这个现在还成立吗”“现代系统怎么吸收 X 的局限”“这是前沿还是历史过渡”时，不直接把它归为前沿。先把问题拆成四类：

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
