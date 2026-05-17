---
type: source
source_type: paper
title: "AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents"
url: https://arxiv.org/abs/2605.13357
pdf: assets/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.pdf
extracted: extracted/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.extracted.md
arxiv: https://arxiv.org/abs/2605.13357
doi: 10.48550/arXiv.2605.13357
author:
  - Hailin Zhong
  - Shengxin Zhu
site: arXiv
venue: arXiv 2026
pages:
topic:
  - agent
  - coding-agent
  - harness
  - evaluation
  - software-engineering
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: https://arxiv.org/abs/2605.13357
related:
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Evaluation]]"
  - "[[Trace]]"
  - "[[Patch Validation]]"
  - "[[Repo Context]]"
  - "[[Agent Lifecycle Hook]]"
---

# AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents

## 原文信息

- 论文标题：AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents
- 作者：Hailin Zhong, Shengxin Zhu
- 提交日期：2026-05-13
- 学科：Software Engineering (cs.SE); Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.13357>
- PDF：<https://arxiv.org/pdf/2605.13357>
- 本地 PDF：`assets/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇值得优先读的原因：它把软件 Agent 可靠性从“模型够不够强”改写成“模型 + harness + environment 的系统能力”。它能补强 [[Agent Harness]] 的证据层，让读者看到 harness 不是泛泛的外壳，而是任务规格、上下文选择、工具、项目记忆、状态、可观测性、失败归因、验证、权限、熵审计和人工干预记录等责任的集合。

## 一句话

软件工程 Agent 的能力不只来自 foundation model，还来自 runtime harness 如何组织观察、行动、反馈和完成证据。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / 问题定位

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：先确认作者为什么把可靠性缺口放在 harness，而不是只放在模型能力。
- 原文短摘：
  > Foundation models have transformed automated code generation, yet autonomous softwareengineering agents remain unreliable in realistic development settings.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：先确认作者为什么把可靠性缺口放在 harness，而不是只放在模型能力。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent Harness]]
  - [[Coding Agent]]
  - [[Evaluation]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 2：Harness responsibilities

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：精读 11 个 component responsibilities，并对应到 tool access、project memory、task state、observability、verification、permissions 等 Agent harness 责任。
- 原文短摘：
  > We formalize this substrate as anAI Harness Engineering and identify eleven component responsibilities: task specification, context selection, tool access, project memory, task state, observability, failure attribution, verification, permissions, entropy auditing, and intervention recording.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：精读 11 个 component responsibilities，并对应到 tool access、project memory、task state、observability、verification、permissions 等 Agent harness 责任。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent Harness]]
  - [[Coding Agent]]
  - [[Evaluation]]
- 证据边界：
  - 这条短摘只证明作者在论文第一页/摘要中提出该 claim；不能证明方法已经被独立复现或成为稳定工程标准。
  - 如果短摘包含数字、排名、benchmark、攻击成功率、性能提升或用户研究，必须再读 Evaluation / Table / Limitations 后才能写入概念卡。

#### 必读块 3：Trace-based evaluation

- 位置：extracted Page 1 / Abstract（必要时连同 Page 1 Introduction 交叉核对）
- 为什么必读：看作者如何把一次 agent run 转成可审计 episode package。
- 原文短摘：
  > We operationalize the harness through a four-level ladder (H0–H3) that progressively exposes runtime support to the agent, and we propose a trace-based evaluation protocol that converts each agent run into an auditable episode package.
- 中文概括：
  - 这段原文直接支撑本块阅读目标：看作者如何把一次 agent run 转成可审计 episode package。
  - 当前摘录只证明作者在摘要或第一页如何界定问题、机制或结果；后续写稳定概念卡时仍要回正文核对方法、实验设置和限制。
- 我需要理解的机制：
  1. 原文里的对象、动作、约束和评价层级分别是什么。
  2. 这条证据属于问题定义、方法机制、数据/benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念:
  - [[Agent Harness]]
  - [[Coding Agent]]
  - [[Evaluation]]
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
- 它能支撑哪张概念卡、topic 或问题池条目？

### 读完要更新

- 可能更新的概念卡：[[Agent Harness]], [[Coding Agent]], [[Evaluation]], [[Trace]], [[Patch Validation]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 软件 Agent 可靠性可以从 model-harness-environment 系统来分析，而不只归因于模型能力。 | Abstract / Introduction | medium-high | [[Agent Harness]] |
| harness 至少包含任务规格、上下文、工具、记忆、状态、观测、失败归因、验证、权限和干预记录等责任。 | Abstract / framework sections | medium | [[Agent Harness]] |
| trace-based episode package 可把 agent run 变成后续审计、比较和复盘的证据单元。 | Abstract / evaluation protocol | medium | [[Trace]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从本地 extracted Page 1 / Abstract 可确认，论文核心机制与「Harness responsibilities」相关：We formalize this substrate as anAI Harness Engineering and identify eleven component responsibilities: task specification, context selection, tool access, project memory, task state, observability, failure attribution, verification, permissions, entropy auditing, and intervention recording.
- 输入 / 输出：本页只记录 Abstract / Page 1 可确认的对象、过程和产物；具体 schema、算法伪代码、工具接口或标注协议要读 Method / Appendix 后再补。
- 关键步骤：
  1. 先用 Abstract 界定论文的问题层级和评估对象。
  2. 再读 Method / Framework，核对上方必读块里的机制是否有可复用结构。
  3. 最后读 Evaluation / Limitations，判断结果能不能外推到其他 Agent 系统。
- 和相邻方法的差别：当前 Abstract 支持的差别线索是「问题定位 / Harness responsibilities / Trace-based evaluation」；不要把标题术语直接升格为稳定概念。

## 实验 / 证据

- 数据集 / benchmark：从本地 extracted Page 1 / Abstract 可确认的证据线索：We operationalize the harness through a four-level ladder (H0–H3) that progressively exposes runtime support to the agent, and we propose a trace-based evaluation protocol that converts each agent run into an auditable episode package.
- 指标：Abstract 层级没有展开完整指标清单；本页只保留作者明示的评价/结果线索，不补造未读过的 metric。
- 关键结果：见上方必读块和本节数据集 / benchmark；任何数字、排名、通过率或攻击成功率都必须回 PDF 表格和实验设置核对后再写入概念卡。
- 作者给出的局限：Abstract 层级不能替代完整 limitations；精读时优先核对 Limitations / Discussion / Appendix。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.pdf`
- Extracted Markdown：`extracted/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂无；本页先作为 raw source evidence，后续精读后再决定是否拆卡。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Agent Harness]] | 直接补强 harness 责任边界和运行 substrate 视角 | [[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents#需要我读的内容]] | P1 |
| [[Trajectory Evaluation]] | 把一次 agent run 看成 episode package，而非只看 final pass | [[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents#需要我读的内容]] | P2 |
| [[Patch Validation]] | 代码 Agent 完成判断需要 harness 证据 | [[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents#需要我读的内容]] | P2 |

## 我的疑问

- 论文的 H0-H3 ladder 与当前 Codex / Claude Code / OpenHands 的实际 harness 能力如何对应？
- “entropy auditing” 具体检测什么，和重复 action / 无新信息循环有什么关系？
- episode package 的最小字段能不能落到 Agent 评测模板？

## 边界提醒

- 这是一篇 arXiv 2026 预印本；当前只录入摘要级和阅读路线证据。不要把 “AI Harness Engineering” 当作已经稳定的行业标准术语；先把它作为 [[Agent Harness]] 的前沿证据和概念扩展观察。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；下一步精读时再补 PDF section/page/table anchor，避免把 Page 1 / Abstract 级判断伪装成全文证据。
