---
type: source
source_type: paper
title: "Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations"
url: "https://arxiv.org/abs/2605.11633"
pdf: "assets/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.pdf"
extracted: "extracted/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.extracted.md"
arxiv: "https://arxiv.org/abs/2605.11633"
doi: "10.48550/arXiv.2605.11633"
author:
  - Junjue Wang
  - Weihao Xuan
  - Heli Qi
  - Pengyu Dai
  - Kunyi Liu
  - Hongruixuan Chen
  - Zhuo Zheng
  - Junshi Xia
  - Stefano Ermon
  - Naoto Yokoya
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - benchmark
  - geospatial
  - tool-use
  - emergency
  - evaluation
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.11633"
related:
  - "[[Benchmark]]"
  - "[[Tool Use]]"
  - "[[Agent Workflow]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
  - "[[Guardrails]]"
  - "[[MCP]]"
---

# Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations

## 原文信息

- 论文标题：Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations
- 作者：Junjue Wang, Weihao Xuan, Heli Qi, Pengyu Dai, Kunyi Liu, Hongruixuan Chen, Zhuo Zheng, Junshi Xia, Stefano Ermon, Naoto Yokoya
- 提交日期：2026-05-12
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.11633>
- PDF：<https://arxiv.org/pdf/2605.11633>
- 本地 PDF：`assets/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

DORA / disaster response 方向的学习价值在于：它把 Agent 评估从通用 tool use 推到真实应急流程：多传感器、道路网络、人口和设施、撤离规划、报告生成，还带 108 个 specialized tools。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 2 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 2]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 2]]。

## 一句话

DORA 用真实灾害事件和可重放 tool-call gold trajectories，评估 LLM Agents 的端到端灾害响应工作流。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / operational disaster response

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：理解灾害响应不只是遥感感知，还包括路网、人口、设施、撤离和报告。
- 原文短摘：
  > However, disaster operations uniquely combineheterogeneousdatafusion,longcompositionalpipelines,anddisaster-specificknowledgegroundingthatprioragentand RS benchmarks rarely test together, leaving the full operational pipeline of disaster response largely unexplored.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：理解灾害响应不只是遥感感知，还包括路网、人口、设施、撤离和报告。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Benchmark]]
  - [[Tool Use]]
  - [[Agent Workflow]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：515 tasks / 108-tool MCP library

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看任务规模、工具库和 replayable gold trajectories。
- 原文短摘：
  > Inthispaper,weintroduceDisasterOperationalResponseAgentbenchmark(DORA),thefirstagenticbenchmark for end-to-end disaster response: 515 expert-authored tasks across 45 real-world disaster events spanning 10 types, paired with expert-verified, replayable gold trajectories totaling 3,500 tool-call steps.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看任务规模、工具库和 replayable gold trajectories。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Benchmark]]
  - [[Tool Use]]
  - [[Agent Workflow]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：Five dimensions

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：读 disaster perception、spatial relational analysis、rescue/evacuation planning、temporal evolution reasoning、report synthesis 五维。
- 原文短摘：
  > Tasks span five dimensions that cover the operational disaster-response pipeline: disaster perception, spatial relational analysis, disaster operational planning, temporal evolution reasoning,andmulti-modalreportsynthesis.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：读 disaster perception、spatial relational analysis、rescue/evacuation planning、temporal evolution reasoning、report synthesis 五维。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Benchmark]]
  - [[Tool Use]]
  - [[Agent Workflow]]
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
- 它给当前 vault 哪张概念卡提供证据？

### 读完要更新

- 可能更新的概念卡：[[Benchmark]], [[Tool Use]], [[Agent Workflow]], [[Planning]], [[Evaluation]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 端到端灾害响应需要多源信号整合、空间关系、撤离规划和行动报告。 | Abstract | high | [[Agent Workflow]] |
| DORA 包含 515 expert-authored tasks、45 real-world disaster events 和 3,500 tool-call steps。 | Abstract | medium-high | [[Benchmark]] |
| 任务使用 108-tool MCP library 覆盖异构 geospatial data。 | Abstract | medium | [[Tool Use]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「515 tasks / 108-tool MCP library」相关：Inthispaper,weintroduceDisasterOperationalResponseAgentbenchmark(DORA),thefirstagenticbenchmark for end-to-end disaster response: 515 expert-authored tasks across 45 real-world disaster events spanning 10 types, paired with expert-verified, replayable gold trajectories totaling 3,500 tool-call steps.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「operational disaster response / 515 tasks / 108-tool MCP library / Five dimensions」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：Tasks span five dimensions that cover the operational disaster-response pipeline: disaster perception, spatial relational analysis, disaster operational planning, temporal evolution reasoning,andmulti-modalreportsynthesis.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.pdf`
- Extracted Markdown：`extracted/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Benchmark]] | 补真实应急任务的 tool-call trajectory benchmark | [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#需要我读的内容]] | P1 |
| [[Tool Use]] | 多工具 orchestration 在高风险场景中的评估边界 | [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#需要我读的内容]] | P1 |
| [[Planning]] | 撤离 / 时间演化推理需要长程计划 | [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#需要我读的内容]] | P2 |

## 我的疑问

- 灾害响应 Agent 的 gold trajectory 是否允许多种等价方案？
- 108 个工具的权限、失败和回滚如何建模？
- 在真实应急系统中，LLM Agent 应该只建议还是允许执行？

## 边界提醒

- 这是高风险应急 benchmark source，不是部署建议。实际灾害响应需要专业人员、权限、审计和责任链；Agent benchmark 只能模拟部分工作流。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
