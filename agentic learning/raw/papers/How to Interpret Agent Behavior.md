---
type: source
source_type: paper
title: How to Interpret Agent Behavior
url: https://arxiv.org/abs/2605.13625
pdf: assets/How to Interpret Agent Behavior.pdf
extracted: extracted/How to Interpret Agent Behavior.extracted.md
arxiv: https://arxiv.org/abs/2605.13625
doi: 10.48550/arXiv.2605.13625
author:
  - Jie Gao
  - Kaiser Sun
  - Jen-tse Huang
  - Katherine Van Koevering
  - Sijie Ji
  - Heyuan Huang
  - Weiyan Shi
  - Zhuoran Lu
  - Ziang Xiao
  - Daniel Khashabi
  - Mark Dredze
site: arXiv
venue: arXiv 2026
pages:
topic:
  - agent
  - trace
  - observability
  - evaluation
  - coding-agent
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: https://arxiv.org/abs/2605.13625
related:
  - "[[Trace]]"
  - "[[Trajectory]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Observability]]"
  - "[[Coding Agent]]"
---

# How to Interpret Agent Behavior

## 原文信息

- 论文标题：How to Interpret Agent Behavior
- 作者：Jie Gao, Kaiser Sun, Jen-tse Huang, Katherine Van Koevering, Sijie Ji, Heyuan Huang, Weiyan Shi, Zhuoran Lu, Ziang Xiao, Daniel Khashabi, Mark Dredze
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.13625>
- PDF：<https://arxiv.org/pdf/2605.13625>
- 本地 PDF：`assets/How to Interpret Agent Behavior.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/How to Interpret Agent Behavior.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇适合放在第二位，因为它回答“Agent 跑了很久以后，我怎么看懂它到底在做什么”。它不是再给一个最终分数，而是试图给 Claude Code / Codex 这类长时运行 Agent 的 reasoning trajectory 和 execution trace 做行为分类。

## 一句话

ACT*ONOMY 把 Agent runtime trace 从自然语言流水账转成可比较、可扩展的行为分类。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / 动机

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：确认作者为什么认为长时运行 Agent 需要过程解释，而不是只看最终结果。
- 原文短摘：
  > Act·ONOMYhas two components: (1)the taxonomy itself, developed through Grounded Theory and structured as a three-level hierarchy of 10 actions, 46 subactions, and 120 leaf categories; and (2)an open repositorythat hosts the living taxonomy, provides an automated analysis pipeline ...
- 中文概括：
  - 这段原文直接支撑本块阅读目标：确认作者为什么认为长时运行 Agent 需要过程解释，而不是只看最终结果。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Trace]]
  - [[Trajectory]]
  - [[Reasoning Trace]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：Taxonomy 层级

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：读 10 actions / 46 subactions / 120 leaf categories 的设计，理解行为粒度。
- 原文短摘：
  > We introduce Act·ONOMY, 3 a taxonomy for describing and analyzing agent behavior at runtime.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：读 10 actions / 46 subactions / 120 leaf categories 的设计，理解行为粒度。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Trace]]
  - [[Trajectory]]
  - [[Reasoning Trace]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：Automated analysis pipeline

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看它如何把 living taxonomy 应用于 agent trajectories。
- 原文短摘：
  > Our experiments show that Act·ONOMY can compare behavioral profiles across agents and characterize a single agent’s behavior across diverse trajectories, surfacing patterns indicative of failure modes.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看它如何把 living taxonomy 应用于 agent trajectories。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Trace]]
  - [[Trajectory]]
  - [[Reasoning Trace]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

### 选读

- Related Work：用于判断它和已有 [[Agent Harness]]、[[Trajectory Evaluation]]、[[Benchmark]]、[[Computer Use]] 等概念的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：模型、harness、workflow、trace、evaluation、security 还是 tool/action space？
- 它最容易被误读成什么？
- 它能支撑哪张概念卡、topic 或问题池条目？

### 读完要更新

- 可能更新的概念卡：[[Trace]], [[Trajectory]], [[Reasoning Trace]], [[Trajectory Evaluation]], [[Observability]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 长时运行 Agent 的诊断、debug 和 oversight 需要分析 reasoning trajectories 与 execution traces。 | Abstract | high | [[Trace]] |
| ACT*ONOMY 提供三层行为 taxonomy，并配套 open repository / analysis pipeline。 | Abstract | medium-high | [[Trajectory Evaluation]] |
| 行为画像可以比较不同 Agent 或同一 Agent 在不同 trajectories 下的模式。 | Abstract / experiments | medium | [[Observability]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「Taxonomy 层级」相关：We introduce Act·ONOMY, 3 a taxonomy for describing and analyzing agent behavior at runtime.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「动机 / Taxonomy 层级 / Automated analysis pipeline」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：Our experiments show that Act·ONOMY can compare behavioral profiles across agents and characterize a single agent’s behavior across diverse trajectories, surfacing patterns indicative of failure modes.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/How to Interpret Agent Behavior.pdf`
- Extracted Markdown：`extracted/How to Interpret Agent Behavior.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂无；本页先作为 raw source evidence，后续精读后再决定是否拆卡。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Trajectory Evaluation]] | 从结果评分扩展到过程行为分类 | [[How to Interpret Agent Behavior#需要我读的内容]] | P1 |
| [[Trace]] | trace 不只是日志，还可以变成行为分析对象 | [[How to Interpret Agent Behavior#需要我读的内容]] | P1 |
| [[Reasoning Trace]] | 需要区分模型文本推理、工具事件和外部 observation | [[How to Interpret Agent Behavior#需要我读的内容]] | P2 |

## 我的疑问

- ACT*ONOMY 的 leaf category 如何避免过拟合 Claude Code / Codex 当前交互样式？
- 行为 taxonomy 能否和 OpenTelemetry GenAI trace schema 对齐？
- 哪些行为类别最能暴露“看似努力但没有新信息”的循环？

## 边界提醒

- 这篇更像行为解释和观测方法，不是 Agent 能力提升方法。taxonomy 能帮助分析 trace，但不能直接证明模型意图，也不能替代任务正确性评估。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
