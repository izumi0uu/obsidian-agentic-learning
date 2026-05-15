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
- 本地 PDF：`assets/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

DORA / disaster response 方向值得录入，因为它把 Agent 评估从通用 tool use 推到真实应急流程：多传感器、道路网络、人口和设施、撤离规划、报告生成，还带 108 个 specialized tools。

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

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / operational disaster response

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解灾害响应不只是遥感感知，还包括路网、人口、设施、撤离和报告。
- 原文短摘：
  > Operational disaster response
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Benchmark]]
  - [[Tool Use]]
  - [[Agent Workflow]]
- 证据边界：
  - 支撑 [[Agent Workflow]]；不能把它等同于普通 image QA。

#### 必读块 2：515 tasks / 108-tool MCP library

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看任务规模、工具库和 replayable gold trajectories。
- 原文短摘：
  > 108 specialized tools
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Benchmark]]
  - [[Tool Use]]
  - [[Agent Workflow]]
- 证据边界：
  - 支撑 [[Tool Use]]、[[MCP]]；需正文核对工具接口和评分。

#### 必读块 3：Five dimensions

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：读 disaster perception、spatial relational analysis、rescue/evacuation planning、temporal evolution reasoning、report synthesis 五维。
- 原文短摘：
  > five dimensions
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Benchmark]]
  - [[Tool Use]]
  - [[Agent Workflow]]
- 证据边界：
  - 支撑 [[Benchmark]]、[[Planning]]；高风险应用需要安全边界。

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

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#需要我读的内容]]。
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

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
