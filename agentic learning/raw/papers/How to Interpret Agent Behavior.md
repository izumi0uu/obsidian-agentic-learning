---
type: source
source_type: paper
title: "How to Interpret Agent Behavior"
url: "https://arxiv.org/abs/2605.13625"
pdf: "assets/How to Interpret Agent Behavior.pdf"
extracted: "extracted/How to Interpret Agent Behavior.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13625"
doi: "10.48550/arXiv.2605.13625"
author:
  - Jie Gao
  - Kaiser Sun
  - Jen-tse Huang
  - Katherine Van Koevering
  - Sijie Ji
  - Heyuan Huang
  - Weiyan Shi
  - Zhuoran Lu
  - Ziang Xiao
  - Daniel Khashabi
  - Mark Dredze
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - trace
  - observability
  - evaluation
  - coding-agent
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13625"
related:
  - "[[Trace]]"
  - "[[Trajectory]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Observability]]"
  - "[[Coding Agent]]"
---

# How to Interpret Agent Behavior

## 原文信息

- 论文标题：How to Interpret Agent Behavior
- 作者：Jie Gao, Kaiser Sun, Jen-tse Huang, Katherine Van Koevering, Sijie Ji, Heyuan Huang, Weiyan Shi, Zhuoran Lu, Ziang Xiao, Daniel Khashabi, Mark Dredze
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.13625>
- PDF：<https://arxiv.org/pdf/2605.13625>
- 本地 PDF：`assets/How to Interpret Agent Behavior.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/How to Interpret Agent Behavior.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇适合放在第二位，因为它回答“Agent 跑了很久以后，我怎么看懂它到底在做什么”。它不是再给一个最终分数，而是试图给 Claude Code / Codex 这类长时运行 Agent 的 reasoning trajectory 和 execution trace 做行为分类。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

ACT*ONOMY 把 Agent runtime trace 从自然语言流水账转成可比较、可扩展的行为分类。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / 动机

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：确认作者为什么认为长时运行 Agent 需要过程解释，而不是只看最终结果。
- 原文短摘：
  > agents such as Claude Code and Codex
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Trace]]
  - [[Trajectory]]
  - [[Reasoning Trace]]
- 证据边界：
  - 支撑 [[Coding Agent]]、[[Observability]]；只能说明这类 Agent 需要解释，不能说明 taxonomy 本身完备。

#### 必读块 2：Taxonomy 层级

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：读 10 actions / 46 subactions / 120 leaf categories 的设计，理解行为粒度。
- 原文短摘：
  > 10 actions, 46 subactions, and 120 leaf categories
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Trace]]
  - [[Trajectory]]
  - [[Reasoning Trace]]
- 证据边界：
  - 支撑 [[Trajectory Evaluation]]、[[Trace]]；分类粒度是作者设计，不等同于所有任务的最优 taxonomy。

#### 必读块 3：Automated analysis pipeline

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看它如何把 living taxonomy 应用于 agent trajectories。
- 原文短摘：
  > living taxonomy
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Trace]]
  - [[Trajectory]]
  - [[Reasoning Trace]]
- 证据边界：
  - 支撑 [[Observability]]；自动标注质量需要看实验和误差分析。

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

- 可能更新的概念卡：[[Trace]], [[Trajectory]], [[Reasoning Trace]], [[Trajectory Evaluation]], [[Observability]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 长时运行 Agent 的诊断、debug 和 oversight 需要分析 reasoning trajectories 与 execution traces。 | Abstract | high | [[Trace]] |
| ACT*ONOMY 提供三层行为 taxonomy，并配套 open repository / analysis pipeline。 | Abstract | medium-high | [[Trajectory Evaluation]] |
| 行为画像可以比较不同 Agent 或同一 Agent 在不同 trajectories 下的模式。 | Abstract / experiments | medium | [[Observability]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[How to Interpret Agent Behavior#需要我读的内容]]。
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

- PDF：`assets/How to Interpret Agent Behavior.pdf`
- Extracted Markdown：`extracted/How to Interpret Agent Behavior.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Trajectory Evaluation]] | 从结果评分扩展到过程行为分类 | [[How to Interpret Agent Behavior#需要我读的内容]] | P1 |
| [[Trace]] | trace 不只是日志，还可以变成行为分析对象 | [[How to Interpret Agent Behavior#需要我读的内容]] | P1 |
| [[Reasoning Trace]] | 需要区分模型文本推理、工具事件和外部 observation | [[How to Interpret Agent Behavior#需要我读的内容]] | P2 |

## 我的疑问

- ACT*ONOMY 的 leaf category 如何避免过拟合 Claude Code / Codex 当前交互样式？
- 行为 taxonomy 能否和 OpenTelemetry GenAI trace schema 对齐？
- 哪些行为类别最能暴露“看似努力但没有新信息”的循环？

## 边界提醒

- 这篇更像行为解释和观测方法，不是 Agent 能力提升方法。taxonomy 能帮助分析 trace，但不能直接证明模型意图，也不能替代任务正确性评估。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
