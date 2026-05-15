---
type: source
source_type: paper
title: "AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents"
url: "https://arxiv.org/abs/2605.13357"
pdf: "assets/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.pdf"
extracted: "extracted/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13357"
doi: "10.48550/arXiv.2605.13357"
author:
  - Hailin Zhong
  - Shengxin Zhu
site: arXiv
venue: "arXiv 2026"
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
source: "https://arxiv.org/abs/2605.13357"
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
- 本地 PDF：`assets/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇是本轮最值得先读的原因：它把软件 Agent 可靠性从“模型够不够强”改写成“模型 + harness + environment 的系统能力”。它正好补强 vault 里 [[Agent Harness]] 的证据层，让你看到 harness 不是泛泛的外壳，而是任务规格、上下文选择、工具、项目记忆、状态、可观测性、失败归因、验证、权限、熵审计和人工干预记录等责任的集合。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

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

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / 问题定位

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：先确认作者为什么把可靠性缺口放在 harness，而不是只放在模型能力。
- 原文短摘：
  > model-harness-environment system
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent Harness]]
  - [[Coding Agent]]
  - [[Evaluation]]
- 证据边界：
  - 支撑 [[Agent Harness]]、[[Coding Agent]]；只说明本文的问题 framing，不能证明所有 Agent 失败都来自 harness。

#### 必读块 2：Harness responsibilities

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：精读 11 个 component responsibilities，把它们映射到当前 vault 的 tool access、project memory、task state、observability、verification、permissions。
- 原文短摘：
  > eleven component responsibilities
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent Harness]]
  - [[Coding Agent]]
  - [[Evaluation]]
- 证据边界：
  - 支撑 [[Agent Harness]]、[[Agent Lifecycle Hook]]、[[Evaluation]]；责任清单是论文框架，不等于行业标准已定型。

#### 必读块 3：Trace-based evaluation

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：看作者如何把一次 agent run 转成可审计 episode package。
- 原文短摘：
  > auditable episode package
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Agent Harness]]
  - [[Coding Agent]]
  - [[Evaluation]]
- 证据边界：
  - 支撑 [[Trace]]、[[Trajectory Evaluation]]、[[Patch Validation]]；它强调证据结构，不替代 benchmark 任务本身。

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

- 可能更新的概念卡：[[Agent Harness]], [[Coding Agent]], [[Evaluation]], [[Trace]], [[Patch Validation]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 软件 Agent 可靠性可以从 model-harness-environment 系统来分析，而不只归因于模型能力。 | Abstract / Introduction | medium-high | [[Agent Harness]] |
| harness 至少包含任务规格、上下文、工具、记忆、状态、观测、失败归因、验证、权限和干预记录等责任。 | Abstract / framework sections | medium | [[Agent Harness]] |
| trace-based episode package 可把 agent run 变成后续审计、比较和复盘的证据单元。 | Abstract / evaluation protocol | medium | [[Trace]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents#需要我读的内容]]。
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

- PDF：`assets/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.pdf`
- Extracted Markdown：`extracted/AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
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
- episode package 的最小字段能不能落到本 vault 的 Agent 评测模板？

## 边界提醒

- 这是一篇 arXiv 2026 预印本；当前只录入摘要级和阅读路线证据。不要把 “AI Harness Engineering” 当作已经稳定的行业标准术语；先把它作为 [[Agent Harness]] 的前沿证据和概念扩展观察。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
