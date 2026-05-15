---
type: source
source_type: paper
title: "Position: Assistive Agents Need Accessibility Alignment"
url: "https://arxiv.org/abs/2605.13579"
pdf: "assets/Position - Assistive Agents Need Accessibility Alignment.pdf"
extracted: "extracted/Position - Assistive Agents Need Accessibility Alignment.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13579"
doi: "10.48550/arXiv.2605.13579"
author:
  - Jie Hu
  - Changyuan Yan
  - Yu Zheng
  - Ziqian Wang
  - Jiaming Zhang
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - accessibility
  - alignment
  - safety
  - evaluation
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13579"
related:
  - "[[Agent]]"
  - "[[Evaluation]]"
  - "[[Guardrails]]"
  - "[[Human-in-the-loop]]"
  - "[[Computer Use]]"
  - "[[Policy Engine]]"
---

# Position: Assistive Agents Need Accessibility Alignment

## 原文信息

- 论文标题：Position: Assistive Agents Need Accessibility Alignment
- 作者：Jie Hu, Changyuan Yan, Yu Zheng, Ziqian Wang, Jiaming Zhang
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- 备注：9 pages, 1 figures, Accepted to ICML 2026
- URL：<https://arxiv.org/abs/2605.13579>
- PDF：<https://arxiv.org/pdf/2605.13579>
- 本地 PDF：`assets/Position - Assistive Agents Need Accessibility Alignment.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/Position - Assistive Agents Need Accessibility Alignment.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇是高风险应用边界的代表：Assistive Agent 面向 BVI 用户时，失败成本、验证方式和交互假设不同，不能用 sighted-user 低成本试错假设来设计。它很适合训练“Agent alignment 不只是拒答安全，也包括特定用户群体的可验证性和风险边界”。

## 一句话

Accessibility alignment 把无障碍需求提升为 Agent 设计和评估的一等 alignment 目标，而不是事后 UI 适配。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / sighted-user assumption mismatch

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：理解 sighted interaction / low-cost verification / tolerable trial-and-error 假设为什么不适合 BVI assistive scenarios。
- 原文短摘：
  > Drawing on an analysis of 778 assistance task instances from prior work, we show that current agentic AI remain prone to failure in assistive scenarios due to mismatches between sighted-user design assumptions and the verification, risk, and interaction ...
- 中文概括：
  - 这段原文直接支撑本块阅读目标：理解 sighted interaction / low-cost verification / tolerable trial-and-error 假设为什么不适合 BVI assistive scenarios。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent]]
  - [[Evaluation]]
  - [[Guardrails]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：778 assistance task instances

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看作者如何从 prior work 分析 assistive task failure。
- 原文短摘：
  > To substantiate this position, we conducted a large-scale analysis of assistive tasks extracted from 417 previous works, comprising 778 task instances related to BVI assistance.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看作者如何从 prior work 分析 assistive task failure。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent]]
  - [[Evaluation]]
  - [[Guardrails]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：Lifecycle design pipeline

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：读 accessibility-aligned assistive agents 的生命周期管线。
- 原文短摘：
  > To this end, we introduce accessibility alignment and propose a lifecycle-oriented design pipeline for accessibility-aligned assistive agents, spanning user research, system design, deployment and post-deployment iteration.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：读 accessibility-aligned assistive agents 的生命周期管线。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent]]
  - [[Evaluation]]
  - [[Guardrails]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

### 选读

- Related Work：用于判断它和已有概念卡 / 对比页的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：memory、planning、trajectory、multi-agent、evaluation、safety 还是 high-risk application？
- 它最容易被误读成什么？
- 它能支撑哪张概念卡、topic 或问题池条目？

### 读完要更新

- 可能更新的概念卡：[[Agent]], [[Evaluation]], [[Guardrails]], [[Human-in-the-loop]], [[Computer Use]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| BVI assistive agents 需要把 accessibility alignment 作为一等设计目标。 | Abstract | high | [[Agent]] |
| 当前 agentic AI 常隐含 sighted-user design assumptions，导致 assistive scenarios 中系统性失败。 | Abstract | medium-high | [[Evaluation]] |
| 作者主张 accessibility 是 alignment problem，而不是外围 usability concern。 | Abstract | medium-high | [[Guardrails]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「778 assistance task instances」相关：To substantiate this position, we conducted a large-scale analysis of assistive tasks extracted from 417 previous works, comprising 778 task instances related to BVI assistance.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「sighted-user assumption mismatch / 778 assistance task instances / Lifecycle design pipeline」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：To this end, we introduce accessibility alignment and propose a lifecycle-oriented design pipeline for accessibility-aligned assistive agents, spanning user research, system design, deployment and post-deployment iteration.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/Position - Assistive Agents Need Accessibility Alignment.pdf`
- Extracted Markdown：`extracted/Position - Assistive Agents Need Accessibility Alignment.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂无；本页先作为 raw source evidence，后续精读后再决定是否拆卡。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Evaluation]] | 补高风险用户场景的评估假设边界 | [[Position - Assistive Agents Need Accessibility Alignment#需要我读的内容]] | P1 |
| [[Human-in-the-loop]] | 辅助场景中的 human verification 成本不同 | [[Position - Assistive Agents Need Accessibility Alignment#需要我读的内容]] | P2 |
| [[Guardrails]] | 风险控制需要贴合用户能力和环境 | [[Position - Assistive Agents Need Accessibility Alignment#需要我读的内容]] | P2 |

## 我的疑问

- BVI 用户不能低成本验证时，Agent 应该如何表达不确定性？
- Accessibility alignment 和 general safety alignment 的最小区别是什么？
- 哪些 assistive task 必须 human-in-the-loop，哪些可以自动化？

## 边界提醒

- 这是 position paper / 高风险用户群体边界，不是通用 Agent benchmark。不要把 accessibility 当作 UI 美化；这里的关键是验证成本、错误后果和交互假设。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
