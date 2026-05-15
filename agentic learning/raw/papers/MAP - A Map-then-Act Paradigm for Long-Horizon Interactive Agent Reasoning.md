---
type: source
source_type: paper
title: "MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning"
url: "https://arxiv.org/abs/2605.13037"
pdf: "assets/MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning.pdf"
extracted: "extracted/MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13037"
doi: "10.48550/arXiv.2605.13037"
author:
  - Yuxin Liu
  - Ziang Ye
  - Yueqing Sun
  - Mingye Zhu
  - Jinwei Xiao
  - Zhuowen Han
  - Qi GU
  - Xunliang Cai
  - Lei Zhang
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - planning
  - reasoning
  - environment
  - trajectory
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13037"
related:
  - "[[Planning]]"
  - "[[Agent Loop]]"
  - "[[Observation]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Trajectory]]"
---

# MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning

## 原文信息

- 论文标题：MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning
- 作者：Yuxin Liu, Ziang Ye, Yueqing Sun, Mingye Zhu, Jinwei Xiao, Zhuowen Han, Qi GU, Xunliang Cai, Lei Zhang
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.13037>
- PDF：<https://arxiv.org/pdf/2605.13037>
- 本地 PDF：`assets/MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇适合学习长程交互 Agent 的时序边界：很多失败不是模型不会计划，而是先执行、后理解环境，导致 trial-and-error 卡在 epistemic bottleneck。MAP 的价值是把环境理解提前到行动前。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

Map-then-Act 先探索并构建环境认知地图，再执行任务，试图减少长程 Agent 的反应式试错。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / Delayed Environmental Perception

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：先读作者如何定义“行动中才补环境理解”的问题。
- 原文短摘：
  > This temporal inversion leads to Delayed Environmental Perception: agents must infer environmental constraints through trial-and-error, resulting in an Epistemic Bottleneck that traps them in inefficient failure cycles.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：先读作者如何定义“行动中才补环境理解”的问题。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Planning]]
  - [[Agent Loop]]
  - [[Observation]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：三阶段 MAP

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：读 Global Exploration、Task-Specific Mapping、Knowledge-Augmented Execution 三阶段如何切分时序。
- 原文短摘：
  > This naturally motivates our proposedMap-then-ActParadigm (MAP), which introduces an explicit <map> phase before action execution: <map>→ (<think>[observation]<act> ).
- 中文概括：
  - 这段原文直接支撑本块阅读目标：读 Global Exploration、Task-Specific Mapping、Knowledge-Augmented Execution 三阶段如何切分时序。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Planning]]
  - [[Agent Loop]]
  - [[Observation]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：MAP-2K / experiments

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看训练 map-then-act trajectories 为什么可能优于 expert execution traces。
- 原文短摘：
  > Experiments show consistent gains across benchmarks and LLMs.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看训练 map-then-act trajectories 为什么可能优于 expert execution traces。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Planning]]
  - [[Agent Loop]]
  - [[Observation]]
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
- 它给当前 vault 哪张概念卡提供证据？

### 读完要更新

- 可能更新的概念卡：[[Planning]], [[Agent Loop]], [[Observation]], [[Agent State]], [[Agent Workflow]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 当前 interactive LLM agents 常在执行中被动获取环境理解，可能造成低效失败循环。 | Abstract | medium-high | [[Agent Loop]] |
| MAP 把环境理解前置为 Global Exploration、Task-Specific Mapping 和 Knowledge-Augmented Execution。 | Abstract | high | [[Planning]] |
| 作者报告 MAP 在多个 benchmark / LLM 上有稳定提升，并提出 MAP-2K。 | Abstract | medium | [[Trajectory Evaluation]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「三阶段 MAP」相关：This naturally motivates our proposedMap-then-ActParadigm (MAP), which introduces an explicit <map> phase before action execution: <map>→ (<think>[observation]<act> ).
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「Delayed Environmental Perception / 三阶段 MAP / MAP-2K / experiments」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：Experiments show consistent gains across benchmarks and LLMs.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning.pdf`
- Extracted Markdown：`extracted/MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Planning]] | 补“先建图再行动”的长程规划边界 | [[MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning#需要我读的内容]] | P1 |
| [[Observation]] | observation 不只来自工具结果，也可形成环境地图 | [[MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning#需要我读的内容]] | P2 |
| [[Agent Workflow]] | MAP 可作为 workflow 时序模式观察 | [[MAP - A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning#需要我读的内容]] | P2 |

## 我的疑问

- 什么时候 map-building 的成本超过反应式试错的成本？
- MAP 和 ReAct / Plan-and-Solve 的最小区别是什么？
- 如果环境会动态变化，预先 map 会不会过期或误导执行？

## 边界提醒

- MAP 是长程交互 Agent 的一种时序范式，不是所有 Agent 的通用必要步骤。它尤其适合环境约束重要、试错昂贵或隐含规则多的任务。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
