---
type: source
source_type: paper
title: "OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents"
url: "https://arxiv.org/abs/2605.11169"
pdf: "assets/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.pdf"
extracted: "extracted/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.extracted.md"
arxiv: "https://arxiv.org/abs/2605.11169"
doi: "10.48550/arXiv.2605.11169"
author:
  - Sheldon Yu
  - Junda Wu
  - Xintong Li
  - Nikki Lijing Kuang
  - Sizhe Zhou
  - Tong Yu
  - Jiawei Han
  - Jingbo Shang
  - Julian McAuley
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - react
  - online-learning
  - action-selection
  - decision-making
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.11169"
related:
  - "[[ReAct]]"
  - "[[Agent Loop]]"
  - "[[Tool Use]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
  - "[[Trace]]"
---

# OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents

## 原文信息

- 论文标题：OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents
- 作者：Sheldon Yu, Junda Wu, Xintong Li, Nikki Lijing Kuang, Sizhe Zhou, Tong Yu, Jiawei Han, Jingbo Shang, Julian McAuley
- 提交日期：2026-05-11
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.11169>
- PDF：<https://arxiv.org/pdf/2605.11169>
- 本地 PDF：`assets/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

OLIVIA 适合补 ReAct 的现代边界：部署中重复处理相关多步任务时，小的 action-selection 错误会累积；单靠 prompt / retrieval 间接改行为，不如显式建一个可更新的 action selection layer。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 2 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 2]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 2]]。

## 一句话

OLIVIA 在 ReAct-style Agent 的推理时动作选择层做在线适应，让候选 action 可评分、可表示不确定性、可由反馈更新。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / ReAct action errors

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：确认小 action-selection 错误如何累积成工具浪费、延迟和可靠性下降。
- 原文短摘：
  > action-selection errors
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[ReAct]]
  - [[Agent Loop]]
  - [[Tool Use]]
- 证据边界：
  - 支撑 [[ReAct]]；不能推出 ReAct 必须加 OLIVIA。

#### 必读块 2：Explicit decision layer

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解为什么 prompting / retrieval 只是间接影响行为。
- 原文短摘：
  > explicit decision layer
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[ReAct]]
  - [[Agent Loop]]
  - [[Tool Use]]
- 证据边界：
  - 支撑 [[Agent Loop]]、[[Tool Use]]；需正文看 contextual linear bandit / adaptation 细节。

#### 必读块 3：Online feedback

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看 action-level feedback 如何在部署时更新。
- 原文短摘：
  > updated online from action-level feedback
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 它把 Agent 问题切到哪一层。
  2. 它的输入、输出或评价信号是什么。
  3. 它不能外推到什么。
- 支撑概念：
  - [[ReAct]]
  - [[Agent Loop]]
  - [[Tool Use]]
- 证据边界：
  - 支撑 [[Evaluation]]；需警惕在线学习安全边界。

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

- 可能更新的概念卡：[[ReAct]], [[Agent Loop]], [[Tool Use]], [[Planning]], [[Evaluation]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| ReAct-style agents 在部署相关多步任务时会因 action-selection errors 累积成本。 | Abstract | medium-high | [[ReAct]] |
| 现有 inference-time adaptation 多通过 prompt / retrieval 间接影响行为。 | Abstract | medium | [[Agent Loop]] |
| OLIVIA 将 final action-selection layer 建模为可在线更新的决策层。 | Abstract | medium | [[Tool Use]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents#需要我读的内容]]。
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

- PDF：`assets/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.pdf`
- Extracted Markdown：`extracted/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[ReAct]] | 补 ReAct 部署时 action adaptation 边界 | [[OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents#需要我读的内容]] | P1 |
| [[Agent Loop]] | reason-action-observation 中 action selection 可被单独建模 | [[OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents#需要我读的内容]] | P1 |
| [[Evaluation]] | 需要 action-level feedback 而非只看最终答案 | [[OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents#需要我读的内容]] | P2 |

## 我的疑问

- 在线 action adaptation 如何避免学到错误用户反馈？
- action-level uncertainty 应如何暴露给 human-in-the-loop？
- OLIVIA 和 tool ranking / policy engine 的边界在哪里？

## 边界提醒

- 这篇不是经典 ReAct 定义，而是对 ReAct-style Agent 的部署期适应方法。写概念卡时应回到 [[ReAct]] 的原始论文边界。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
