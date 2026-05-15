---
type: source
source_type: paper
title: "Cognifold: Always-On Proactive Memory via Cognitive Folding"
url: "https://arxiv.org/abs/2605.13438"
pdf: "assets/Cognifold - Always-On Proactive Memory via Cognitive Folding.pdf"
extracted: "extracted/Cognifold - Always-On Proactive Memory via Cognitive Folding.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13438"
doi: "10.48550/arXiv.2605.13438"
author:
  - Suli Wang
  - Yiqun Duan
  - Yu Deng
  - Rundong Zhao
  - Dai Shi
  - Xinliang Zhou
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - memory
  - long-term-memory
  - autonomy
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13438"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
  - "[[Memory Reflection]]"
  - "[[Agent State]]"
---

# Cognifold: Always-On Proactive Memory via Cognitive Folding

## 原文信息

- 论文标题：Cognifold: Always-On Proactive Memory via Cognitive Folding
- 作者：Suli Wang, Yiqun Duan, Yu Deng, Rundong Zhao, Dai Shi, Xinliang Zhou
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- URL：<https://arxiv.org/abs/2605.13438>
- PDF：<https://arxiv.org/pdf/2605.13438>
- 本地 PDF：`assets/Cognifold - Always-On Proactive Memory via Cognitive Folding.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Cognifold - Always-On Proactive Memory via Cognitive Folding.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇值得作为 memory 方向的前沿观察：它反对“memory 只是被动检索库”，主张 always-on 地把事件流折叠成更高层 cognitive structure。它可以帮助你区分 reactive retrieval memory、reflection memory 和 proactive memory。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 2 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 2]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 2]]。

## 一句话

Cognifold 把 agent memory 设想成持续自组织的结构：从碎片事件流中合并、衰减、重连并浮现 intent。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / reactive memory limitation

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：确认作者批评的是被动检索式 memory 缺少自主组织经验的能力。
- 原文短摘：
  > reactive and retrieval-based
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Memory]]
  - [[Long-term Memory]]
  - [[Semantic Memory]]
- 证据边界：
  - 支撑 [[Memory]]；不能推出所有 retrieval memory 都过时。

#### 必读块 2：Cognitive folding mechanism

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看事件流如何 merge、decay、relink、surface intents。
- 原文短摘：
  > graph-topology self-organization
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Memory]]
  - [[Long-term Memory]]
  - [[Semantic Memory]]
- 证据边界：
  - 支撑 [[Long-term Memory]]、[[Memory Reflection]]；需正文核对实现。

#### 必读块 3：CLS / intent layer analogy

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解 hippocampus / neocortex / prefrontal intent layer 类比的证据边界。
- 原文短摘：
  > prefrontal intent layer
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Memory]]
  - [[Long-term Memory]]
  - [[Semantic Memory]]
- 证据边界：
  - 支撑 memory 现代性判断；脑科学类比不能直接当工程证明。

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

- 可能更新的概念卡：[[Memory]], [[Long-term Memory]], [[Semantic Memory]], [[Episodic Memory]], [[Memory Reflection]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 现有 agent memory 多是 reactive retrieval，缺少自主组织成持久结构的能力。 | Abstract | medium | [[Memory]] |
| Cognifold continuously folds fragmented event streams into cognitive structures。 | Abstract | medium | [[Long-term Memory]] |
| 作者用三层 CLS 扩展和 graph topology self-organization 支撑 proactive memory 设计。 | Abstract | low-medium | [[Memory Reflection]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Cognifold - Always-On Proactive Memory via Cognitive Folding#需要我读的内容]]。
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

- PDF：`assets/Cognifold - Always-On Proactive Memory via Cognitive Folding.pdf`
- Extracted Markdown：`extracted/Cognifold - Always-On Proactive Memory via Cognitive Folding.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Long-term Memory]] | 补 proactive / self-organizing memory 方向 | [[Cognifold - Always-On Proactive Memory via Cognitive Folding#需要我读的内容]] | P1 |
| [[Memory Reflection]] | 区分 reflection summary 与持续结构折叠 | [[Cognifold - Always-On Proactive Memory via Cognitive Folding#需要我读的内容]] | P2 |
| [[Semantic Memory]] | 事件流如何变成更抽象结构 | [[Cognifold - Always-On Proactive Memory via Cognitive Folding#需要我读的内容]] | P2 |

## 我的疑问

- always-on memory 如何避免噪音和错误经验固化？
- intent layer 是工程模块还是学习类比？
- proactive memory 什么时候会侵犯隐私或越界行动？

## 边界提醒

- 这篇含明显脑启发类比，第一轮应把它作为前沿 memory 设想，不要把“cognitive folding”当成已验证通用架构。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
