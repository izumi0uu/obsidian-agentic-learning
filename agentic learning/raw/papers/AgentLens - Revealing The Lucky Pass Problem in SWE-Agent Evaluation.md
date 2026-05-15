---
type: source
source_type: paper
title: "AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation"
url: "https://arxiv.org/abs/2605.12925"
pdf: "assets/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.pdf"
extracted: "extracted/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12925"
doi: "10.48550/arXiv.2605.12925"
author:
  - Priyam Sahoo
  - Gaurav Mittal
  - Xiaomin Li
  - Shengjie Ma
  - Benjamin Steenhoek
  - Pingping Lin
  - Yu Hu
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - coding-agent
  - evaluation
  - trajectory
  - swe-bench
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12925"
related:
  - "[[Coding Agent]]"
  - "[[Patch Validation]]"
  - "[[Trajectory Evaluation]]"
  - "[[Trace]]"
  - "[[Task Success Rate]]"
  - "[[SWE-bench]]"
---

# AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

## 原文信息

- 论文标题：AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation
- 作者：Priyam Sahoo, Gaurav Mittal, Xiaomin Li, Shengjie Ma, Benjamin Steenhoek, Pingping Lin, Yu Hu
- 提交日期：2026-05-13
- 学科：Software Engineering (cs.SE); Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.12925>
- PDF：<https://arxiv.org/pdf/2605.12925>
- 本地 PDF：`assets/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇是 SWE-Agent 评估的反直觉提醒：测试通过可能只是 Lucky Pass。它直接连接 [[Patch Validation]]、[[Task Success Rate]] 和 [[Trajectory Evaluation]]，适合训练你不要把“最后绿了”误当成“过程可靠”。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

AgentLens 关注 SWE-Agent 的过程质量，指出有些 passing trajectories 包含回归循环、盲目重试、缺验证或时序混乱。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / Lucky Pass 定义

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：先读哪些 passing trajectories 被称为 Lucky Pass。
- 原文短摘：
  > Lucky Pass
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Task Success Rate]]、[[Trajectory Evaluation]]；不能把 10.7% 外推到所有模型和任务。

#### 必读块 2：AgentLens-Bench

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看数据集如何标注 quality scores、waste signals 和 divergence points。
- 原文短摘：
  > process-level assessment
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Trace]]、[[Patch Validation]]；需读正文确认标注协议。

#### 必读块 3：PTA reference

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解通过多条 passing solutions 合并出的 task-level process reference。
- 原文短摘：
  > Prefix Tree Acceptor
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Coding Agent]]
  - [[Patch Validation]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Trajectory Evaluation]]；这种 reference 是否稳定要看任务和轨迹数量。

### 选读

- Related Work：用于判断它和已有 [[Agent Harness]]、[[Trajectory Evaluation]]、[[Benchmark]]、[[Computer Use]] 等概念的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：模型、harness、workflow、trace、evaluation、security 还是 tool/action space？
- 它最容易被误读成什么？
- 它给当前 vault 哪张概念卡提供证据？

### 读完要更新

- 可能更新的概念卡：[[Coding Agent]], [[Patch Validation]], [[Trajectory Evaluation]], [[Trace]], [[Task Success Rate]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| SWE-Agent 评估不能只看最终 patch 是否通过测试；过程质量也会显著不同。 | Abstract | high | [[Patch Validation]] |
| 部分 passing trajectories 存在 regression cycles、blind retries、missing verification 等 Lucky Pass 行为。 | Abstract | medium-high | [[Trajectory Evaluation]] |
| AgentLens 用 task-level process references 和 intent labeler 做过程级评估。 | Abstract | medium | [[Trace]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]]。
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

- PDF：`assets/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.pdf`
- Extracted Markdown：`extracted/AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Task Success Rate]] | 分数通过不等于过程可靠 | [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]] | P1 |
| [[Trajectory Evaluation]] | 补充 coding agent 过程参考和 waste signal | [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]] | P1 |
| [[Patch Validation]] | 验证不仅是最后跑测试，也包括过程是否有序 | [[AgentLens - Revealing The Lucky Pass Problem in SWE-Agent Evaluation#需要我读的内容]] | P2 |

## 我的疑问

- Lucky Pass 和普通探索式调试的边界在哪里？
- 过程质量差但最终通过时，产品该降权、重试还是人工复核？
- PTA reference 是否会惩罚创造性但有效的解法？

## 边界提醒

- 这篇基于 OpenHands、SWE-bench Verified 和特定任务子集；不要把摘要中的比例当成整个 SWE-Agent 领域的固定基准率。学习重点是“最终通过 ≠ 可靠过程”。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
