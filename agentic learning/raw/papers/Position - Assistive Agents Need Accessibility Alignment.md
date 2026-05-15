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
- 本地 PDF：`assets/Position - Assistive Agents Need Accessibility Alignment.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Position - Assistive Agents Need Accessibility Alignment.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇是高风险应用边界的代表：Assistive Agent 面向 BVI 用户时，失败成本、验证方式和交互假设不同，不能用 sighted-user 低成本试错假设来设计。它很适合训练“Agent alignment 不只是拒答安全，也包括特定用户群体的可验证性和风险边界”。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 2 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 2]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 2]]。

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

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / sighted-user assumption mismatch

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解 sighted interaction / low-cost verification / tolerable trial-and-error 假设为什么不适合 BVI assistive scenarios。
- 原文短摘：
  > sighted interaction
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent]]
  - [[Evaluation]]
  - [[Guardrails]]
- 证据边界：
  - 支撑 [[Evaluation]]；不能用摘要直接定义完整 accessibility 标准。

#### 必读块 2：778 assistance task instances

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看作者如何从 prior work 分析 assistive task failure。
- 原文短摘：
  > 778 assistance task instances
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent]]
  - [[Evaluation]]
  - [[Guardrails]]
- 证据边界：
  - 支撑 [[Benchmark]] / [[Evaluation]]；需正文核对数据来源。

#### 必读块 3：Lifecycle design pipeline

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：读 accessibility-aligned assistive agents 的生命周期管线。
- 原文短摘：
  > lifecycle-oriented design pipeline
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent]]
  - [[Evaluation]]
  - [[Guardrails]]
- 证据边界：
  - 支撑 [[Guardrails]]、[[Human-in-the-loop]]；position paper 的 pipeline 需实践验证。

### 选读

- Related Work：用于判断它和已有概念卡 / 对比页的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：memory、planning、trajectory、multi-agent、evaluation、safety 还是 high-risk application？
- 它最容易被误读成什么？
- 它给当前 vault 哪张概念卡提供证据？

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

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Position - Assistive Agents Need Accessibility Alignment#需要我读的内容]]。
- 和相邻方法的差别：待精读后写回对应概念卡或对比页。

## 实验 / 证据

- 数据集 / benchmark：待精读正文后补。
- 指标：待精读正文后补。
- 关键结果：摘要中出现的数字和结论需回到正文核对实验设置。
- 作者给出的局限：待精读 Limitations / Discussion 后补。

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

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
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

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
