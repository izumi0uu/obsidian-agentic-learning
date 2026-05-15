---
type: source
source_type: paper
title: "Harnessing Agentic Evolution"
url: "https://arxiv.org/abs/2605.13821"
pdf: "assets/Harnessing Agentic Evolution.pdf"
extracted: "extracted/Harnessing Agentic Evolution.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13821"
doi: "10.48550/arXiv.2605.13821"
author:
  - Jiayi Zhang
  - Yongfeng Gu
  - Jianhao Ruan
  - Maojia Song
  - Yiran Peng
  - Zhiguang Han
  - Jinyu Xiang
  - Zhitao Wang
  - Caiyin Yang
  - Yixi Ouyang
  - Bang Liu
  - Chenglin Wu
  - Yuyu Luo
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - self-improvement
  - workflow
  - evaluation
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13821"
related:
  - "[[Agent Harness]]"
  - "[[Agent Workflow]]"
  - "[[Evaluation]]"
  - "[[Trace]]"
  - "[[Memory]]"
  - "[[Agent State]]"
---

# Harnessing Agentic Evolution

## 原文信息

- 论文标题：Harnessing Agentic Evolution
- 作者：Jiayi Zhang, Yongfeng Gu, Jianhao Ruan, Maojia Song, Yiran Peng, Zhiguang Han, Jinyu Xiang, Zhitao Wang, Caiyin Yang, Yixi Ouyang, Bang Liu, Chenglin Wu, Yuyu Luo
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- URL：<https://arxiv.org/abs/2605.13821>
- PDF：<https://arxiv.org/pdf/2605.13821>
- 本地 PDF：`assets/Harnessing Agentic Evolution.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Harnessing Agentic Evolution.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇放在第二梯队，是因为它把“Agentic evolution”从固定手工流程或泛化 agent 漂移之间，转成有 harness 的 meta-editing 问题：积累的 candidates、feedback、traces、failures 应该成为 process-level state。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 2 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 2]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 2]]。

## 一句话

Harnessing Agentic Evolution 把迭代生成-评估-反馈的演化过程，放进一个可被 meta-agent 编辑的 harness。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / evolution context as state

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看 accumulated candidates / feedback / traces / failures 如何变成 process-level state。
- 原文短摘：
  > process-level state
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent Harness]]
  - [[Agent Workflow]]
  - [[Evaluation]]
- 证据边界：
  - 支撑 [[Agent State]]；不能推出所有自我改进都安全。

#### 必读块 2：Meta-agent edits procedure

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解 meta-agent 不是直接提下一个 candidate，而是编辑生成未来 candidate 的 procedure。
- 原文短摘：
  > editing the procedure
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent Harness]]
  - [[Agent Workflow]]
  - [[Evaluation]]
- 证据边界：
  - 支撑 [[Agent Workflow]]；需正文核对 action space。

#### 必读块 3：Drift boundary

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看作者如何处理 long-horizon evolution drift。
- 原文短摘：
  > can drift in long-horizon evolution
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent Harness]]
  - [[Agent Workflow]]
  - [[Evaluation]]
- 证据边界：
  - 支撑 [[Evaluation]]；摘要不足以判断防漂移效果。

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

- 可能更新的概念卡：[[Agent Harness]], [[Agent Workflow]], [[Evaluation]], [[Trace]], [[Memory]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Agentic evolution 通过生成候选、评估并利用反馈改进程序 / workflow / 科学解。 | Abstract | medium-high | [[Agent Workflow]] |
| 固定手工流程刚性强，通用 agent 灵活但长程演化易漂移。 | Abstract | medium | [[Agent Harness]] |
| AEvo 让 meta-agent 观察 evolution context 并编辑 procedure / controller。 | Abstract | medium | [[Agent State]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Harnessing Agentic Evolution#需要我读的内容]]。
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

- PDF：`assets/Harnessing Agentic Evolution.pdf`
- Extracted Markdown：`extracted/Harnessing Agentic Evolution.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Agent Harness]] | self-improvement 需要 harness / state / trace 约束 | [[Harnessing Agentic Evolution#需要我读的内容]] | P1 |
| [[Agent Workflow]] | 演化对象可能是过程本身，不只是下一次输出 | [[Harnessing Agentic Evolution#需要我读的内容]] | P2 |
| [[Evaluation]] | 自我改进必须有反馈和漂移检测 | [[Harnessing Agentic Evolution#需要我读的内容]] | P2 |

## 我的疑问

- meta-agent 编辑 procedure 时如何避免 reward hacking？
- evolution context 应保存哪些 trace / failure，哪些应丢弃？
- 这和 AutoML / program synthesis / Reflexion 的边界在哪里？

## 边界提醒

- 这是 agentic self-improvement 的前沿论文。不要把它读成 Agent 可以无限自主变强；关键边界是 harnessed evolution 与漂移控制。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
