---
type: source
source_type: paper
title: "Useful Memories Become Faulty When Continuously Updated by LLMs"
url: "https://arxiv.org/abs/2605.12978"
pdf: "assets/Useful Memories Become Faulty When Continuously Updated by LLMs.pdf"
extracted: "extracted/Useful Memories Become Faulty When Continuously Updated by LLMs.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12978"
doi: "10.48550/arXiv.2605.12978"
author:
  - Dylan Zhang
  - Yanshan Lin
  - Zhengkun Wu
  - Yihang Sun
  - Bingxuan Li
  - Dianqi Li
  - Hao Peng
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - memory
  - evaluation
  - trace
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12978"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Agent Memory 类型对比]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
---

# Useful Memories Become Faulty When Continuously Updated by LLMs

## 原文信息

- 论文标题：Useful Memories Become Faulty When Continuously Updated by LLMs
- 作者：Dylan Zhang, Yanshan Lin, Zhengkun Wu, Yihang Sun, Bingxuan Li, Dianqi Li, Hao Peng
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.12978>
- PDF：<https://arxiv.org/pdf/2605.12978>
- 本地 PDF：`assets/Useful Memories Become Faulty When Continuously Updated by LLMs.pdf`
- extracted：`extracted/Useful Memories Become Faulty When Continuously Updated by LLMs.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇是 Hermes 清单里最值得优先读的 memory 边界论文：它提醒“持续由 LLM 总结和更新的记忆”可能先变好再退化，甚至低于 no-memory baseline。它能直接支撑本 vault raw evidence / wiki synthesis 分层的设计判断。


本页来自 2026-05-14 对用户提供的 Hermes arXiv cs.AI recent Agent 论文补充清单录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文 Hermes 补充]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文 Hermes 补充]]。

## 一句话

Useful Memories Become Faulty 说明 Agent memory 不是越持续重写越好；episodic trace、版本、验证和回滚可能比无限 consolidation 更重要。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。


#### 必读块 1：Abstract / episodic vs consolidated memory

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：先切开原始轨迹和抽象记忆的角色，防止把 memory 只理解成摘要库。
      - 原文短摘：
        > episodic traces
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
- [[Agent Memory 类型对比]]
      - 证据边界：
        - 支撑 [[Memory]] / [[Long-term Memory]]；不能推出“不要记忆”。
#### 必读块 2：Abstract / memory utility degradation

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：看作者如何描述 memory utility 先升后降，以及为什么这对长期 Agent 很危险。
      - 原文短摘：
        > memory utility first rises
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
- [[Agent Memory 类型对比]]
      - 证据边界：
        - 支撑 [[Agent Memory 类型对比]]；需要正文核对任务、基线和统计设置。
#### 必读块 3：Abstract / consolidation root cause

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：确认问题是否来自经验本身，还是来自 consolidation / update schedule。
      - 原文短摘：
        > consolidation step
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
- [[Agent Memory 类型对比]]
      - 证据边界：
        - 支撑 [[Trace]]；精读时要看 update schedule 和 ablation。

### 选读

- Related Work：用于判断它和已有概念卡 / 对比页的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：memory、planning、trajectory、multi-agent、evaluation、safety、tool use、RAG 还是 high-risk application？
- 它最容易被误读成什么？
- 它给当前 vault 哪张概念卡提供证据？

### 读完要更新

- 可能更新的概念卡：[[Memory]], [[Long-term Memory]], [[Agent Memory 类型对比]], [[Trace]], [[Evaluation]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]。
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 持续更新的 consolidated memories 可能从有用变成有害。 | Abstract | medium-high | [[Memory]] |
| 原始 episodic traces 和抽象 schema-like memory 需要分层保存。 | Abstract | medium | [[Trace]] |
| memory update schedule / consolidation 需要验证、版本和回滚边界。 | Abstract | medium | [[Evaluation]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Useful Memories Become Faulty When Continuously Updated by LLMs#需要我读的内容]]。
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

- PDF：`assets/Useful Memories Become Faulty When Continuously Updated by LLMs.pdf`
- Extracted Markdown：`extracted/Useful Memories Become Faulty When Continuously Updated by LLMs.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入到 Hermes 补充来源批次。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Memory]] | 补“连续总结式记忆会退化”的反例边界 | [[Useful Memories Become Faulty When Continuously Updated by LLMs#需要我读的内容]] | P1 |
| [[Long-term Memory]] | 补长期记忆不是无限追加 / 重写 | [[Useful Memories Become Faulty When Continuously Updated by LLMs#需要我读的内容]] | P1 |
| [[Agent Memory 类型对比]] | 把 episodic trace 与 consolidated abstraction 切开 | [[Useful Memories Become Faulty When Continuously Updated by LLMs#需要我读的内容]] | P1 |

## 我的疑问

- 什么时候应该保留原始 trajectory，而不是只保存总结？
- memory consolidation 的验证集、回滚点和置信度应该怎么设计？
- 这篇的 ARC-AGI 结论能外推到 coding agent / personal assistant 吗？

## 边界提醒

- 这篇不是反对 Agent memory，而是反对未经验证的连续 LLM consolidation。第一轮不要把它读成“所有记忆都会伤害 Agent”。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
