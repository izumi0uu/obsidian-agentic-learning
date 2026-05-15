---
type: source
source_type: paper
title: "Rollout Cards: A Reproducibility Standard for Agent Research"
url: "https://arxiv.org/abs/2605.12131"
pdf: "assets/Rollout Cards - A Reproducibility Standard for Agent Research.pdf"
extracted: "extracted/Rollout Cards - A Reproducibility Standard for Agent Research.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12131"
doi: "10.48550/arXiv.2605.12131"
author:
  - Charlie Masters
  - Ziyuan Liu
  - Stefano V. Albrecht
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - evaluation
  - reproducibility
  - trace
  - benchmark
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12131"
related:
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Trajectory Evaluation]]"
  - "[[Trace]]"
  - "[[Replay]]"
  - "[[Audit Log]]"
  - "[[Task Success Rate]]"
---

# Rollout Cards: A Reproducibility Standard for Agent Research

## 原文信息

- 论文标题：Rollout Cards: A Reproducibility Standard for Agent Research
- 作者：Charlie Masters, Ziyuan Liu, Stefano V. Albrecht
- 提交日期：2026-05-12
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.12131>
- PDF：<https://arxiv.org/pdf/2605.12131>
- 本地 PDF：`assets/Rollout Cards - A Reproducibility Standard for Agent Research.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Rollout Cards - A Reproducibility Standard for Agent Research.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇值得靠前读，因为它把 Agent 评估的证据单位从 headline score 拉回 rollout record。对 Agent 学习来说，这是一个很重要的边界：同一段行为可能因为截取、失败统计、cost/token 规则不同而得到不同分数。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

Rollout Cards 主张 Agent 研究复现时应公开 rollout record、reporting rules 和 drops manifest，而不只报告分数。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / 复现问题

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：先读为什么 Agent 研究比传统 ML 更依赖 rollout 证据。
- 原文短摘：
  > rollout records, not reported scores
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Evaluation]]
  - [[Benchmark]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Trajectory Evaluation]]；不能外推为所有论文都必须采用同一格式。

#### 必读块 2：Audit of repositories

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看 50 个 training / evaluation repositories 中失败、错误、跳过运行如何被遗漏。
- 原文短摘：
  > failed, errored, or were skipped
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Evaluation]]
  - [[Benchmark]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Benchmark]]、[[Task Success Rate]]；需读正文确认 audit criteria。

#### 必读块 3：Rollout card 数据模型

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解 views、reporting rules、drops manifests 分别记录什么。
- 原文短摘：
  > publication bundles
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Evaluation]]
  - [[Benchmark]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Trace]]、[[Replay]]、[[Audit Log]]；这是标准提案，不是已被普遍采用的事实。

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

- 可能更新的概念卡：[[Evaluation]], [[Benchmark]], [[Trajectory Evaluation]], [[Trace]], [[Replay]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Agentic tasks 的复现单位应是 rollout record，而非只看 reported score。 | Abstract | high | [[Trajectory Evaluation]] |
| 不同 reporting rules 可以改变 task-success、cost/token 和 timing 等结果。 | Abstract | medium-high | [[Evaluation]] |
| Rollout cards 保存 rollout record 并声明视图、报告规则和丢弃清单。 | Abstract | medium | [[Audit Log]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Rollout Cards - A Reproducibility Standard for Agent Research#需要我读的内容]]。
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

- PDF：`assets/Rollout Cards - A Reproducibility Standard for Agent Research.pdf`
- Extracted Markdown：`extracted/Rollout Cards - A Reproducibility Standard for Agent Research.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Trajectory Evaluation]] | 补强“过程记录是评估对象”这个核心判断 | [[Rollout Cards - A Reproducibility Standard for Agent Research#需要我读的内容]] | P1 |
| [[Benchmark]] | 补 benchmark reporting / reproducibility 边界 | [[Rollout Cards - A Reproducibility Standard for Agent Research#需要我读的内容]] | P1 |
| [[Replay]] | rollout record 与 replay / audit 的关系值得后续拆 | [[Rollout Cards - A Reproducibility Standard for Agent Research#需要我读的内容]] | P2 |

## 我的疑问

- 最小 rollout card 应该包含哪些字段，才能支持重算 task success rate？
- 失败、错误、跳过运行应该如何和最终分数一起报告？
- rollout card 与 trace / audit log / replay 的边界如何切开？

## 边界提醒

- 这篇是复现标准提案；它很适合支撑 [[Trajectory Evaluation]] 和 [[Evaluation 层次对比]]，但不能当成当前领域已统一遵守的规范。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
