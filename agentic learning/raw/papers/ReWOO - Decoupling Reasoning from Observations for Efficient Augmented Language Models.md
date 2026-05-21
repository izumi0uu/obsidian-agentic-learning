---
type: source
source_type: paper
title: ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models
url: https://arxiv.org/abs/2305.18323
pdf: https://arxiv.org/pdf/2305.18323
arxiv: https://arxiv.org/abs/2305.18323
doi: 10.48550/arXiv.2305.18323
author:
  - Binfeng Xu
  - Zhiyuan Peng
  - Bowen Lei
  - Subhabrata Mukherjee
  - Yuchen Liu
  - Dongkuan Xu
site: arXiv
venue: arXiv 2023
pages:
topic:
  - agent
  - reasoning
  - planning
  - tool-use
  - evaluation
created: 2026-05-21
updated: 2026-05-21
last_checked: 2026-05-21
freshness: stable
conflicts: []
status: seed
source: https://arxiv.org/abs/2305.18323
related:
  - "[[ReWOO]]"
  - "[[ReAct]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[Observation]]"
  - "[[Tool Use]]"
  - "[[Agent Loop]]"
---

# ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models

## 原文信息

- 论文标题：ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models
- 作者：Binfeng Xu, Zhiyuan Peng, Bowen Lei, Subhabrata Mukherjee, Yuchen Liu, Dongkuan Xu
- 发表位置 / 年份：arXiv 2023
- URL：<https://arxiv.org/abs/2305.18323>
- PDF：<https://arxiv.org/pdf/2305.18323>
- 本地 PDF：未保存；本页先用 arXiv / ar5iv 作为 source-level evidence。
- extracted：未生成本地 extracted；后续精读如需页码级证据再下载 PDF 并抽取。

边界：这一页是 raw source note，只回答“论文原文说了什么、哪些概念可由它支持”。稳定理解写入 [[ReWOO]]；不要把本页当成生产 Agent 架构建议。

## 为什么收

ReWOO 值得收，是因为它给 [[ReAct]] 的 action-observation 交替范式提供了一个清晰反面切口：有些任务可以先规划证据槽，再集中调用工具取证，最后让 solver 合成答案，从而减少多轮 observation-dependent prompting 的 token 重复。

它也给现代 Agent 工程一个很小但重要的判断：**观察反馈不是越多越好，也不是越少越好**。如果中间证据可以预先枚举，ReWOO 式 Plan-Work-Solve 能节省成本；如果任务强依赖环境状态、工具失败、几何/图像/数据库中间结果，移除 observation feedback 会损伤可靠性。

## 一句话

ReWOO 是一种把规划、工具取证和最终求解拆开的 Plan-Work-Solve prompting / ALM 范式，用预先生成的 evidence slots 替代 ReAct 式每一步观察后再继续推理。

## 先读什么

1. Abstract：确认 ReWOO 的问题定义是降低 observation-dependent ALM 的 prompt redundancy。
2. Figure 1 / Introduction：看 Planner、Worker、Solver 的分工。
3. Section 2.1：确认 Plan-Work-Solve 与 `Plan, #E` evidence slot 的机制。
4. Experiments：只把结果当作论文条件下的证据，不外推成通用最优 scaffold。
5. 现代对照：回看 DORA 的 scaffold ablation，理解 ReWOO 在数据/几何中间反馈强依赖任务中的失败边界。

## 需要我读的内容

### 必读

> 使用规则：本节只放短摘和学习概括；原文页码、表格和公式若要精读，需要回 PDF / ar5iv 核对。

#### 必读块 1：Abstract / ReWOO 定义

- 位置：Abstract
- 为什么必读：这段定义 ReWOO 的名字、问题对象和核心目标。
- 原文短摘：
  > ReWOO (Reasoning WithOut Observation) ... detaches the reasoning process from external observations.
- 中文概括：
  - 论文把 ReWOO 定义为 Reasoning WithOut Observation，即把推理规划从外部 observation 中解耦。
  - 目标不是禁止工具，而是减少每轮拿到 observation 后重新喂入全部历史上下文造成的 prompt redundancy。
  - 论文报告了 HotpotQA 上的 token efficiency 和准确率提升，但这些数字只说明论文设置下有效，不是通用 Agent 结论。
- 我需要理解的机制：
  1. ReWOO 对照的是 interleaved thought-action-observation ALM。
  2. 它优化的是 token / prompt redundancy 和模块化。
  3. 它牺牲或限制的是执行中根据 observation 动态改计划的能力。
- 支撑概念：
  - [[ReWOO]]
  - [[ReAct]]
  - [[Observation]]
  - [[Tool Use]]
- 证据边界：
  - Abstract 支持定义和作者自报结果；不能证明 ReWOO 是生产系统默认范式，也不能证明所有工具任务都适合移除 observation feedback。

#### 必读块 2：Figure 1 / Planner-Worker-Solver

- 位置：Figure 1 / Introduction
- 为什么必读：这里给出 ReWOO 的最小结构：Planner 先写蓝图，Worker 调工具收证据，Solver 合成答案。
- 原文短摘：
  > Planner composes a comprehensive blueprint ... Worker ... collect evidence.
- 中文概括：
  - Planner 在看到工具返回之前先写出互相关联的计划蓝图。
  - Worker 根据蓝图调用外部工具，填充 evidence。
  - Solver 同时读计划和 evidence，生成最终答案。
- 我需要理解的机制：
  1. ReWOO 不是纯 [[Plan-and-Solve Prompting]]，因为它有 Worker / tool evidence。
  2. ReWOO 也不是标准 [[ReAct]]，因为 observation 不驱动下一轮 thought。
  3. 它更像把 tool-use 任务拆成 plan artifact、evidence collection、answer synthesis 三段。
- 支撑概念：
  - [[ReWOO]]
  - [[Plan-and-Solve Prompting]]
  - [[Tool Use]]
  - [[Agent Loop]]
- 证据边界：
  - Figure 1 支持结构分工；不说明每个现代 framework 都应采用三个独立模型或进程。

#### 必读块 3：Section 2.1 / Plan-Work-Solve

- 位置：Section 2.1, ReWOO with Plan-Work-Solve Paradigm
- 为什么必读：这里说明 `Plan, #E` evidence slot 如何把后续 worker evidence 引入 solver。
- 原文短摘：
  > Planner leverages the foreseeable reasoning of LLMs to compose a solution blueprint.
- 中文概括：
  - Planner 生成连续的 plan 和 evidence slot，例如 `#E1`、`#E2`。
  - Worker 用工具调用把这些 slot 填成真实 evidence / observations。
  - Solver 读完整计划和 evidence，必要时谨慎处理错误 evidence。
- 我需要理解的机制：
  1. `#E` 是计划里预留的证据占位符，不是长期记忆。
  2. Worker 仍然接触外部环境；“without observation”指的是 planner reasoning 不在每步 observation 后继续展开。
  3. Solver 是最后的合成器，不是中途动态重规划器。
- 支撑概念：
  - [[ReWOO]]
  - [[Reasoning Trace]]
  - [[Observation]]
  - [[Tool Calling]]
- 证据边界：
  - Section 2.1 支持机制描述；是否适合某类任务仍要看任务是否能预先规划证据需求。

### 选读

- Prompt Redundancy Reduction：用于理解为什么 interleaved prompting 的输入 token 会随步骤变多而重复增长。
- Experiment / robustness：用于核对作者在 NLP benchmark 和 tool-failure 场景下的结果。

### 可以先跳过

- 完整公式推导和所有 benchmark 数字；第一轮只需要把机制边界和现代吸收方式写清。

### 读完要能回答

- ReWOO 为什么不是 ReAct？
- ReWOO 为什么又不只是 Plan-and-Solve？
- 什么任务适合先规划 evidence slots，什么任务必须保留 observation feedback？

### 读完要更新

- 已新增概念卡：[[ReWOO]]
- 可能更新的概念卡：[[ReAct]], [[Plan-and-Solve Prompting]], [[Agent Evaluation Benchmark]]
- 可能更新的 topic / map：[[ReAct Plan-and-Solve Reflexion 对比]], [[Agent 知识地图]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| ReWOO 将推理规划从外部 observation 中解耦，以减少 ALM 多轮工具交互中的 prompt redundancy。 | Abstract / Section 2.1 | high | [[ReWOO]] |
| ReWOO 由 Planner、Worker、Solver 三段组成：先生成计划和 evidence slots，再调用工具填证据，最后综合答案。 | Figure 1 / Section 2.1 | high | [[ReWOO]] |
| ReWOO 的收益依赖任务是否能预先规划证据需求；在强中间反馈任务中可能失去 observation 校正能力。 | 论文机制 + DORA scaffold ablation | medium | [[Agent Evaluation Benchmark]] |

边界：前两条是论文内机制 claim；第三条是把 ReWOO 原机制和 [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations#实验 / 证据]] 的 scaffold ablation 对照后的学习判断。

## 方法 / 机制

- 核心方法：Plan-Work-Solve。Planner 先产出 interdependent plans 和 `#E` evidence slots；Worker 调用工具填充 evidence；Solver 合成最终答案。
- 输入 / 输出：输入是任务目标和可用工具语境；中间输出是 plan blueprint 与 evidence；最终输出是答案或任务状态。
- 关键步骤：
  1. Planner 在没有工具 observation 的情况下，一次性规划步骤和证据需求。
  2. Worker 按每个 evidence slot 的指令调用工具，填入外部证据。
  3. Solver 结合任务、计划和 evidence 输出答案。
- 和相邻方法的差别：
  - vs [[ReAct]]：ReAct 用每轮 Observation 改变下一步 thought / action；ReWOO 把观察反馈限制在 evidence filling 与最终 solve。
  - vs [[Plan-and-Solve Prompting]]：Plan-and-Solve 通常没有外部工具 evidence；ReWOO 有 Worker 调工具。
  - vs 现代 planner-executor workflow：ReWOO 的 plan 主要是 prompt/evidence blueprint；现代系统还会加入 state、权限、trace、replan 和 evaluator。

## 实验 / 证据

- 数据集 / benchmark：论文报告多项 NLP benchmark 和一个 curated dataset；第一轮不细抄所有分数。
- 指标：重点看 token efficiency、accuracy、tool-failure robustness。
- 关键结果：作者报告 HotpotQA 上 token efficiency 和 accuracy 提升；这只作为论文内实验结果，不作为所有 Agent 任务的普遍结论。
- 现代对照：DORA scaffold ablation 中 ReWOO 平均得分低于 ReAct，作者解释为移除 observation feedback 会伤害由中间 masks / geometries 驱动的数据密集任务。
- 作者给出的局限：本轮只读到 Abstract / method-level evidence；limitations 需后续精读。

## 现代性 / 前沿性初判

- 判定：transitional / current-practice-adjacent。
- 今天仍然稳定的部分：先规划证据需求、把工具取证和最终合成拆开，是现代 Agent / RAG / research workflow 中仍有价值的设计思想。
- 已被现代系统吸收或替代的部分：现代系统通常用 state graph、typed tool call、trace、eval、replan、approval 和 budget 管理来实现类似分层，而不是只靠一个 ReWOO prompt 模板。
- 需要 freshness 复查的部分：ReWOO 是否作为具体 scaffold 在新 benchmark 中有效，取决于任务反馈结构、工具失败率、模型能力和成本模型。

## 已提取文件

- PDF：未本地保存；外部 PDF 为 <https://arxiv.org/pdf/2305.18323>。
- Extracted Markdown：未生成本地 extracted。
- 抽取质量提醒：本页基于 arXiv / ar5iv 首轮阅读；若后续需要页码、表格或公式级引用，再下载 PDF 并生成 extracted Markdown。

## Ingest 摘要

- 已沉淀到 wiki 的概念：[[ReWOO]]
- 已更新的 topic / map：[[ReAct Plan-and-Solve Reflexion 对比]], [[Agent 知识地图]], [[Agent 主题]]
- 还没处理的证据：完整实验表、limitations、代码仓库复现情况。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[ReWOO]] | 作为 ReAct / Plan-and-Solve 之间的 observation-feedback 边界卡，有明确论文证据和现代评测反例。 | [[ReWOO - Decoupling Reasoning from Observations for Efficient Augmented Language Models#需要我读的内容]] | P1 |

## 我的疑问

- 哪些任务的 evidence needs 能被 Planner 可靠预判，哪些必须动态读取 observation 后重规划？
- Solver 的“with caution”提示能多大程度抵消 Worker evidence 错误？
- 在现代 state graph / planner-executor 框架里，ReWOO 更像一种 cost-saving mode，还是一种独立 agent scaffold？

## 边界提醒

- ReWOO 不是“不用工具”，而是 planner reasoning 不在每轮 observation 后继续展开。
- ReWOO 不是 [[ReAct]] 的替代品；它牺牲的是中途 observation feedback 的动态校正。
- ReWOO 不是 [[Plan-and-Solve Prompting]] 的同义词；它包含 Worker 调工具和 evidence slots。
- 论文内效率收益不能外推到所有 Agent 任务；DORA 这类数据/几何中间反馈强依赖 benchmark 已显示它可能显著掉分。

## 原文摘录

> 原文短摘已分散写入 `## 需要我读的内容` 的各个必读块；后续精读再补 PDF page / section / figure/table anchor。
