---
type: source
source_type: paper
title: "RS-Claw: Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents"
url: "https://arxiv.org/abs/2605.13391"
pdf: "assets/RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents.pdf"
extracted: "extracted/RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13391"
doi: "10.48550/arXiv.2605.13391"
author:
  - Liangtian Liu
  - Zeyuan Wang
  - Ziyu Li
  - Kai Ouyang
  - Zichao Tang
  - Chengfu Liu
  - Haifeng Li
  - Hanwen Yu
  - Wentao Yang
  - Cheng Yang
  - Dongyang Hou
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - tool-use
  - remote-sensing
  - skills
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13391"
related:
  - "[[Tool Use]]"
  - "[[Tool Registry]]"
  - "[[MCP Registry]]"
  - "[[Query Planning]]"
  - "[[Computer Use]]"
---

# RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents

## 原文信息

- 论文标题：RS-Claw: Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents
- 作者：Liangtian Liu, Zeyuan Wang, Ziyu Li, Kai Ouyang, Zichao Tang, Chengfu Liu, Haifeng Li, Hanwen Yu, Wentao Yang, Cheng Yang, Dongyang Hou
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.13391>
- PDF：<https://arxiv.org/pdf/2605.13391>
- 本地 PDF：`assets/RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents.pdf`
- extracted：`extracted/RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇虽然是遥感 Agent，但问题很通用：工具太多时，flat 注册会爆上下文，RAG 检索又可能漏关键工具，Agent 需要主动探索和组织工具空间。


本页来自 2026-05-14 对用户提供的 Hermes arXiv cs.AI recent Agent 论文补充清单录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文 Hermes 补充]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文 Hermes 补充]]。

## 一句话

RS-Claw 用 hierarchical skill trees 支持 Agent 在巨大遥感工具空间中渐进式主动探索，而不是被动选择已注册或检索到的工具。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。


#### 必读块 1：Abstract / flat tool registration

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：确认全量注册工具为什么导致 context load 问题。
      - 原文短摘：
        > full tool registration
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Tool Use]]
- [[Tool Registry]]
- [[MCP Registry]]
      - 证据边界：
        - 支撑 [[Tool Registry]]；具体结论受遥感工具生态影响。
#### 必读块 2：Abstract / passive RAG selection

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：看 RAG 检索在工具发现中为什么可能漏关键工具。
      - 原文短摘：
        > RAG retrieval
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Tool Use]]
- [[Tool Registry]]
- [[MCP Registry]]
      - 证据边界：
        - 支撑 [[MCP Registry]]；不能推出 RAG 工具发现无效。
#### 必读块 3：Abstract / active tool exploration

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：理解 Agent 作为 tool-space explorer 的机制边界。
      - 原文短摘：
        > active explorer
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Tool Use]]
- [[Tool Registry]]
- [[MCP Registry]]
      - 证据边界：
        - 支撑 [[Tool Use]]；需看层级树如何构造。

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

- 可能更新的概念卡：[[Tool Use]], [[Tool Registry]], [[MCP Registry]], [[Query Planning]], [[Computer Use]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]。
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 巨大工具空间下，flat registration 与 RAG selection 各有失败模式。 | Abstract | medium-high | [[Tool Registry]] |
| hierarchical skill tree 是组织工具描述和探索路径的一种方式。 | Abstract | medium | [[Query Planning]] |
| Agent 可从被动工具选择走向主动工具空间探索。 | Abstract | medium | [[Tool Use]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents#需要我读的内容]]。
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

- PDF：`assets/RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents.pdf`
- Extracted Markdown：`extracted/RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入到 Hermes 补充来源批次。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Tool Registry]] | 补工具太多时的注册/检索边界 | [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents#需要我读的内容]] | P1 |
| [[Tool Use]] | 补 active tool exploration | [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents#需要我读的内容]] | P1 |
| [[MCP Registry]] | 补工具发现和上下文预算问题 | [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents#需要我读的内容]] | P2 |

## 我的疑问

- hierarchical skill tree 是人工构造、模型归纳还是混合？
- 主动探索工具空间如何控制成本和安全权限？
- 这能否映射到 MCP server discovery / tool routing？

## 边界提醒

- RS-Claw 的实验场景是 remote sensing；通用价值在工具空间组织，不是遥感方法本身。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
