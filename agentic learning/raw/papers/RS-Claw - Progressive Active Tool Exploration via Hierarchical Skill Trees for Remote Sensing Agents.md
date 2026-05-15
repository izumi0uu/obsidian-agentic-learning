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

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

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

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / flat tool registration

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：定位论文的核心证据。
- 原文短摘：
  > To mitigate the context bottleneck induced by Flat paradigm, existing research has primarily explored tool registration paradigms based on external retrieval augmentation (RAG) [17].
- 中文概括：
  - 这段原文直接支撑本块阅读目标：定位论文的核心证据。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：Abstract / passive RAG selection

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：定位论文的核心证据。
- 原文短摘：
  > Comparison of agent tool selection paradigms. (a) Passive paradigm: Existing methods define the agent as a passive tool recipient.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：定位论文的核心证据。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：Abstract / active tool exploration

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：定位论文的核心证据。
- 原文短摘：
  > Systematic experiments on the Earth-Bench benchmark demonstrate that RS-Claw’s active exploration mechanism effectively filters semantic noise and substantially frees up reasoning space (achieving an input token compression ratio of up to 86%), comprehensively outperforming existing Flat and RAG ...
- 中文概括：
  - 这段原文直接支撑本块阅读目标：定位论文的核心证据。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

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

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「passive RAG selection」相关：Comparison of agent tool selection paradigms. (a) Passive paradigm: Existing methods define the agent as a passive tool recipient.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「flat tool registration / passive RAG selection / active tool exploration」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：Systematic experiments on the Earth-Bench benchmark demonstrate that RS-Claw’s active exploration mechanism effectively filters semantic noise and substantially frees up reasoning space (achieving an input token compression ratio of up to 86%), comprehensively outperforming existing Flat and RAG ...
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

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

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
