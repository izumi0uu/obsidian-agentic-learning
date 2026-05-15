---
type: source
source_type: paper
title: "AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation"
url: "https://arxiv.org/abs/2605.12925"
pdf: "assets/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.pdf"
extracted: "extracted/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12925"
doi: "10.48550/arXiv.2605.12925"
author:
  - Priyam Sahoo
  - Gaurav Mittal
  - Xiaomin Li
  - Shengjie Ma
  - Benjamin Steenhoek
  - Pingping Lin
  - Yu Hu
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - coding-agent
  - evaluation
  - trajectory
  - swe-bench
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12925"
related:
  - "[[Coding Agent]]"
  - "[[Patch Validation]]"
  - "[[Trajectory Evaluation]]"
  - "[[Trace]]"
  - "[[Task Success Rate]]"
  - "[[SWE-bench]]"
---

# AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

## 原文信息

- 论文标题：AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation
- 作者：Priyam Sahoo, Gaurav Mittal, Xiaomin Li, Shengjie Ma, Benjamin Steenhoek, Pingping Lin, Yu Hu
- 提交日期：2026-05-13
- 学科：Software Engineering (cs.SE); Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.12925>
- PDF：<https://arxiv.org/pdf/2605.12925>
- 本地 PDF：`assets/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇是 SWE-Agent 评估的反直觉提醒：测试通过可能只是 Lucky Pass。它直接连接 [[Patch Validation]]、[[Task Success Rate]] 和 [[Trajectory Evaluation]]，适合训练你不要把“最后绿了”误当成“过程可靠”。

## 一句话

AgentLens 关注 SWE-Agent 的过程质量，指出有些 passing trajectories 包含回归循环、盲目重试、缺验证或时序混乱。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / Lucky Pass 定义

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：先读哪些 passing trajectories 被称为 Lucky Pass。
- 原文短摘：
  > Among passing trajectories in this subset, 10.7% exhibit behavior we call a Lucky Pass: regression cycles, blind retries, missing verification, or temporally disordered exploration, implementation, and verification.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：先读哪些 passing trajectories 被称为 Lucky Pass。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：AgentLens-Bench

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看数据集如何标注 quality scores、waste signals 和 divergence points。
- 原文短摘：
  > We introduceAGENTLENS, a framework for process-level assessment of SWE-agent trajectories, and releaseAGENTLENS-Bench, a dataset of 1,815 trajectories annotated with quality scores, waste signals, divergence points, and 47 task-level Prefix Tree Acceptor (PTA) references.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看数据集如何标注 quality scores、waste signals 和 divergence points。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：PTA reference

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：理解通过多条 passing solutions 合并出的 task-level process reference。
- 原文短摘：
  > First, it merges multiple passing solutions for the same task into a PTA reference space of correct behaviors.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：理解通过多条 passing solutions 合并出的 task-level process reference。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
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

- 可能更新的概念卡：[[Coding Agent]], [[Patch Validation]], [[Trajectory Evaluation]], [[Trace]], [[Task Success Rate]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| SWE-Agent 评估不能只看最终 patch 是否通过测试；过程质量也会显著不同。 | Abstract | high | [[Patch Validation]] |
| 部分 passing trajectories 存在 regression cycles、blind retries、missing verification 等 Lucky Pass 行为。 | Abstract | medium-high | [[Trajectory Evaluation]] |
| AgentLens 用 task-level process references 和 intent labeler 做过程级评估。 | Abstract | medium | [[Trace]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「AgentLens-Bench」相关：We introduceAGENTLENS, a framework for process-level assessment of SWE-agent trajectories, and releaseAGENTLENS-Bench, a dataset of 1,815 trajectories annotated with quality scores, waste signals, divergence points, and 47 task-level Prefix Tree Acceptor (PTA) references.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「Lucky Pass 定义 / AgentLens-Bench / PTA reference」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：First, it merges multiple passing solutions for the same task into a PTA reference space of correct behaviors.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.pdf`
- Extracted Markdown：`extracted/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂无；本页先作为 raw source evidence，后续精读后再决定是否拆卡。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Task Success Rate]] | 分数通过不等于过程可靠 | [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]] | P1 |
| [[Trajectory Evaluation]] | 补充 coding agent 过程参考和 waste signal | [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]] | P1 |
| [[Patch Validation]] | 验证不仅是最后跑测试，也包括过程是否有序 | [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]] | P2 |

## 我的疑问

- Lucky Pass 和普通探索式调试的边界在哪里？
- 过程质量差但最终通过时，产品该降权、重试还是人工复核？
- PTA reference 是否会惩罚创造性但有效的解法？

## 边界提醒

- 这篇基于 OpenHands、SWE-bench Verified 和特定任务子集；不要把摘要中的比例当成整个 SWE-Agent 领域的固定基准率。学习重点是“最终通过 ≠ 可靠过程”。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
