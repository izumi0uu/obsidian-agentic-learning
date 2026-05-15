---
type: source
source_type: paper
title: "Executable Agentic Memory for GUI Agent"
url: "https://arxiv.org/abs/2605.12294"
pdf: "assets/Executable Agentic Memory for GUI Agent.pdf"
extracted: "extracted/Executable Agentic Memory for GUI Agent.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12294"
doi: "10.48550/arXiv.2605.12294"
author:
  - Zerui Qin
  - Sheng Yue
  - Xingyuan Hua
  - Yongjian Fu
  - Ju Ren
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - memory
  - computer-use
  - gui
  - planning
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12294"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Computer Use]]"
  - "[[GUI Grounding]]"
  - "[[Agent State]]"
  - "[[Trajectory]]"
  - "[[Planning]]"
---

# Executable Agentic Memory for GUI Agent

## 原文信息

- 论文标题：Executable Agentic Memory for GUI Agent
- 作者：Zerui Qin, Sheng Yue, Xingyuan Hua, Yongjian Fu, Ju Ren
- 提交日期：2026-05-12
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.12294>
- PDF：<https://arxiv.org/pdf/2605.12294>
- 本地 PDF：`assets/Executable Agentic Memory for GUI Agent.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Executable Agentic Memory for GUI Agent.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇放在第二梯队的原因是：它把 GUI Agent 的长期任务失败，切到“每一步都重新看 UI、重新决定动作”的 model-centric 问题上，并提出把多步 routine 压缩成可检索、可执行的 agentic memory。它适合补充 [[Memory]]、[[Computer Use]] 和 [[GUI Grounding]] 的交界。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 2 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 2]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 2]]。

## 一句话

Executable Agentic Memory 把 GUI 操作经验组织成结构化知识图，让长程 GUI Agent 能检索并执行已有 routine，而不是每屏重新推理。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / GUI step-wise fragility

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解为什么 GUI Agent 每屏重新解释 UI 会在长程任务里脆弱。
- 原文短摘：
  > model-centric and step-wise interaction paradigm
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
  - [[Computer Use]]
- 证据边界：
  - 支撑 [[Computer Use]]；不能推出所有 GUI 任务都应该变成可执行记忆。

#### 必读块 2：Memory construction pipeline

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看 state-aware DFS 和 action-group mining 如何把多步 routine 压缩成 memory。
- 原文短摘：
  > state-aware DFS
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
  - [[Computer Use]]
- 证据边界：
  - 支撑 [[Memory]]、[[Trajectory]]；需正文核对算法和采样条件。

#### 必读块 3：Graph search and Q-function

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看 value-guided graph search / MCTS 如何把 memory 用于规划。
- 原文短摘：
  > value-guided graph search
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
  - [[Computer Use]]
- 证据边界：
  - 支撑 [[Planning]]；轻量 Q-function 的有效性需看实验设置。

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

- 可能更新的概念卡：[[Memory]], [[Long-term Memory]], [[Computer Use]], [[GUI Grounding]], [[Agent State]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| GUI Agent 的逐屏重解释范式在长程任务中脆弱。 | Abstract | medium-high | [[Computer Use]] |
| EAM 用结构化 KG 将 GUI planning 从自由生成转为 retrieval-and-execution。 | Abstract | medium | [[Memory]] |
| 作者报告 EAM 在 AndroidWorld 上提升表现并降低 token cost。 | Abstract | medium | [[Evaluation]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Executable Agentic Memory for GUI Agent#需要我读的内容]]。
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

- PDF：`assets/Executable Agentic Memory for GUI Agent.pdf`
- Extracted Markdown：`extracted/Executable Agentic Memory for GUI Agent.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Memory]] | 补 executable / procedural memory 与普通 RAG memory 的边界 | [[Executable Agentic Memory for GUI Agent#需要我读的内容]] | P1 |
| [[Computer Use]] | 补 GUI long-horizon routine 复用问题 | [[Executable Agentic Memory for GUI Agent#需要我读的内容]] | P1 |
| [[GUI Grounding]] | 把屏幕状态识别和可执行路径连接起来 | [[Executable Agentic Memory for GUI Agent#需要我读的内容]] | P2 |

## 我的疑问

- 可执行记忆如何避免把过期 UI routine 固化？
- KG / MCTS 路径和普通 workflow graph 的边界在哪里？
- token cost 降低是否牺牲了泛化能力？

## 边界提醒

- 这不是通用长期记忆标准，而是 GUI Agent 场景里的 procedural / executable memory 思路。第一轮不要把 EAM 等同于所有 Agent memory。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
