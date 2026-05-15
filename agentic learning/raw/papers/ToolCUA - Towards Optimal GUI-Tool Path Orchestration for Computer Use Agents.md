---
type: source
source_type: paper
title: "ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents"
url: "https://arxiv.org/abs/2605.12481"
pdf: "assets/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.pdf"
extracted: "extracted/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12481"
doi: "10.48550/arXiv.2605.12481"
author:
  - Xuhao Hu
  - Xi Zhang
  - Haiyang Xu
  - Kyle Qiao
  - Jingyi Yang
  - Xuanjing Huang
  - Jing Shao
  - Ming Yan
  - Jieping Ye
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - computer-use
  - tool-use
  - gui
  - trajectory
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12481"
related:
  - "[[Computer Use]]"
  - "[[Browser Agent]]"
  - "[[GUI Grounding]]"
  - "[[Tool Use]]"
  - "[[Tool Calling]]"
  - "[[Trajectory]]"
  - "[[Tool Permissioning]]"
---

# ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents

## 原文信息

- 论文标题：ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
- 作者：Xuhao Hu, Xi Zhang, Haiyang Xu, Kyle Qiao, Jingyi Yang, Xuanjing Huang, Jing Shao, Ming Yan, Jieping Ye
- 提交日期：2026-05-12
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.12481>
- PDF：<https://arxiv.org/pdf/2605.12481>
- 本地 PDF：`assets/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇补 Computer Use Agent 的执行边界：同一个任务里，Agent 既可以点 UI，也可以调用高层工具。真正难点不是“会不会点屏幕”，而是什么时候该继续 GUI、什么时候切到工具。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

ToolCUA 把 Computer Use Agent 的 GUI action 和 tool call 看成混合行动空间，并学习 GUI-Tool 路径选择。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / hybrid action space

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：先读 CUAs 为什么会在原子 GUI 动作和高层工具之间犹豫。
- 原文短摘：
  > Computer Use Agents (CUAs) can act through both atomic GUI actions (e.g., click, type) and high-level tool calls (e.g., API-based file operations), but they are often confused by this hybrid action space: they do not know when to ...
- 中文概括：
  - 这段原文直接支撑本块阅读目标：先读 CUAs 为什么会在原子 GUI 动作和高层工具之间犹豫。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Computer Use]]
  - [[Browser Agent]]
  - [[GUI Grounding]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：Interleaved GUI-Tool trajectories

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：理解作者如何合成 interleaved GUI-Tool trajectory supervision。
- 原文短摘：
  > We first introduce anInterleaved GUI-Tool Trajectory Scaling Pipelinethat repurposes abundant static GUI trajectories and synthesizes a grounded library of tools, making it possible to scale diverse GUI-Tool trajectories without manual engineering or real tool-trajectory collection.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：理解作者如何合成 interleaved GUI-Tool trajectory supervision。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Computer Use]]
  - [[Browser Agent]]
  - [[GUI Grounding]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：Tool-Efficiency Reward

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看工具切换决策如何被 reward 约束，而不是无限调用 API。
- 原文短摘：
  > Experiments on OSWorld-MCP show that ToolCUA achieves 46.85% accuracy, a relative improvement of approximately 66% over the baseline, establishing a new state of the art among models of comparable scale.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看工具切换决策如何被 reward 约束，而不是无限调用 API。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Computer Use]]
  - [[Browser Agent]]
  - [[GUI Grounding]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

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

- 可能更新的概念卡：[[Computer Use]], [[Browser Agent]], [[GUI Grounding]], [[Tool Use]], [[Tool Calling]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Computer Use Agents 面临原子 GUI action 与高层 tool call 的路径选择问题。 | Abstract | high | [[Computer Use]] |
| 高质量 interleaved GUI-Tool trajectories 稀缺，限制了 GUI-Tool path selection 监督。 | Abstract | medium-high | [[Trajectory]] |
| ToolCUA 通过 staged training 和 Online Agentic RL 优化 GUI-Tool 切换。 | Abstract | medium | [[GUI Grounding]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「Interleaved GUI-Tool trajectories」相关：We first introduce anInterleaved GUI-Tool Trajectory Scaling Pipelinethat repurposes abundant static GUI trajectories and synthesizes a grounded library of tools, making it possible to scale diverse GUI-Tool trajectories without manual engineering or real tool-trajectory collection.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「hybrid action space / Interleaved GUI-Tool trajectories / Tool-Efficiency Reward」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：Experiments on OSWorld-MCP show that ToolCUA achieves 46.85% accuracy, a relative improvement of approximately 66% over the baseline, establishing a new state of the art among models of comparable scale.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.pdf`
- Extracted Markdown：`extracted/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Computer Use]] | 补 GUI 与 tool call 混合行动空间 | [[ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents#需要我读的内容]] | P1 |
| [[GUI Grounding]] | 视觉状态识别和工具路径选择的连接点 | [[ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents#需要我读的内容]] | P2 |
| [[Tool Use]] | 工具使用不只是会调用，还包括何时不用 GUI | [[ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents#需要我读的内容]] | P2 |

## 我的疑问

- GUI action 和 tool call 的切换错误分别会造成什么失败？
- 高层工具是否会绕过 UI 中本来存在的人类确认和权限边界？
- Tool efficiency 与 safety approval 冲突时，应该谁优先？

## 边界提醒

- 这篇主要服务 Computer Use / GUI Agent 线。不要把它泛化成所有 Agent 的最佳 tool policy；它的训练数据、环境和 reward 设计需要正文复核。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
