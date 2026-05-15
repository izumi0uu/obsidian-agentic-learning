---
type: source
source_type: paper
title: "ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles"
url: "https://arxiv.org/abs/2605.13725"
pdf: "assets/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.pdf"
extracted: "extracted/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13725"
doi: "10.48550/arXiv.2605.13725"
author:
  - Yitian Yang
  - Yiqun Duan
  - Linghan Huang
  - Yiqi Zhu
  - Francesco Bailo
  - Chunmeizi Su
  - Huaming Chen
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - multi-agent
  - social-simulation
  - memory
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13725"
related:
  - "[[Multi-agent Orchestration]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Evaluation]]"
  - "[[Role-playing Agent]]"
---

# ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles

## 原文信息

- 论文标题：ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles
- 作者：Yitian Yang, Yiqun Duan, Linghan Huang, Yiqi Zhu, Francesco Bailo, Chunmeizi Su, Huaming Chen
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI); Social and Information Networks (cs.SI)
- URL：<https://arxiv.org/abs/2605.13725>
- PDF：<https://arxiv.org/pdf/2605.13725>
- 本地 PDF：`assets/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.pdf`
- extracted：`extracted/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇偏 multi-agent social simulation，不是通用生产力 Agent，但它能补“多 Agent 个体状态 / belief / memory 如何影响群体动态”的建模边界。


本页来自 2026-05-14 对用户提供的 Hermes arXiv cs.AI recent Agent 论文补充清单录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文 Hermes 补充]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文 Hermes 补充]]。

## 一句话

ScioMind 用 memory-anchored belief update、层级记忆和动态 profiles，让 LLM 多 Agent 社会模拟不完全依赖自由对话。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。


#### 必读块 1：Abstract / belief update rule

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：确认 belief change 如何受 personality-conditioned anchoring strength 影响。
      - 原文短摘：
        > memory-anchored belief update
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Multi-agent Orchestration]]
- [[Memory]]
- [[Agent State]]
      - 证据边界：
        - 支撑 [[Agent State]]；不能当作认知科学定论。
#### 必读块 2：Abstract / memory architecture

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：看层级记忆如何支持 persistent belief formation。
      - 原文短摘：
        > hierarchical memory architecture
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Multi-agent Orchestration]]
- [[Memory]]
- [[Agent State]]
      - 证据边界：
        - 支撑 [[Memory]]；需正文核对记忆表示。
#### 必读块 3：Abstract / dynamic profiles

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：理解 profiles 如何从 corpus-grounded retrieval 生成并动态变化。
      - 原文短摘：
        > dynamic agent profiles
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Multi-agent Orchestration]]
- [[Memory]]
- [[Agent State]]
      - 证据边界：
        - 支撑 [[Role-playing Agent]]；需看数据和偏差。

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

- 可能更新的概念卡：[[Multi-agent Orchestration]], [[Memory]], [[Agent State]], [[Evaluation]], [[Role-playing Agent]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]。
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| LLM 多 Agent 社会模拟需要结构化 belief dynamics，而不只是自由对话。 | Abstract | medium | [[Multi-agent Orchestration]] |
| memory / profile 会影响个体 susceptibility 和群体意见演化。 | Abstract | medium | [[Agent State]] |
| 动态 profile 可增强异质性，但也带来偏差和验证问题。 | Abstract | medium | [[Evaluation]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles#需要我读的内容]]。
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

- PDF：`assets/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.pdf`
- Extracted Markdown：`extracted/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入到 Hermes 补充来源批次。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Multi-agent Orchestration]] | 补社会模拟中 agent state / belief 的边界 | [[ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles#需要我读的内容]] | P2 |
| [[Memory]] | 补 belief formation 与 memory architecture | [[ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles#需要我读的内容]] | P2 |
| [[Role-playing Agent]] | 补角色 profile 和真实人格模型的边界 | [[ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles#需要我读的内容]] | P2 |

## 我的疑问

- belief dynamics 是经验模型、心理学假设还是工程启发？
- dynamic profile 如何避免把检索语料偏见固化进 agent？
- 社会模拟 benchmark 如何验证接近真实社会过程？

## 边界提醒

- 这篇主要服务多 Agent 社会模拟，不应直接外推到生产力 Agent、coding agent 或企业 workflow。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
