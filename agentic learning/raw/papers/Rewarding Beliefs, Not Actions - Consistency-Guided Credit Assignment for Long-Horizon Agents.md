---
type: source
source_type: paper
title: "Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents"
url: https://arxiv.org/abs/2605.20061
pdf: assets/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.pdf
extracted: extracted/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.extracted.md
arxiv: https://arxiv.org/abs/2605.20061
doi: 10.48550/arXiv.2605.20061
author:
  - Wenjie Tang
  - Minne Li
  - Sijie Huang
  - Liquan Xiao
  - Yuan Zhou
site: arXiv
venue: arXiv 2026
pages:
topic:
  - agent
  - rl
  - credit-assignment
  - long-horizon
  - belief-state
  - frontier
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: watch
conflicts: []
status: seed
source: https://arxiv.org/abs/2605.20061
related:
  - "[[Agent State]]"
  - "[[Trajectory Evaluation]]"
  - "[[Evaluation]]"
  - "[[Planning]]"
  - "[[Agent Robustness]]"
---

# Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents

## 原文信息

- 论文标题：Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents
- 作者：Wenjie Tang, Minne Li, Sijie Huang, Liquan Xiao, Yuan Zhou
- 提交日期：2026-05-19
- 学科：arXiv cs.AI / cs.CL / related（以 arXiv 页面为准）
- URL：<https://arxiv.org/abs/2605.20061>
- PDF：<https://arxiv.org/pdf/2605.20061v1>
- 本地 PDF：`assets/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.extracted.md`
- 阅读优先级：P2

边界：这一页是 raw source note，只回答“论文原文目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把 Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇偏 agent RL / post-training，但它切中长程 agent 的 credit assignment：失败不一定来自某一步 action，而可能来自中间 belief/state 漂移。

## 一句话

ReBel 用结构化 belief state 和 belief-consistency supervision 给长程 agent 提供更密集的过程级训练信号。

## 先读什么

1. Abstract / Page 1：确认问题定义、作者主张和方法对象。
2. Introduction：看它纠正的是哪个旧误解或工程痛点。
3. Method / Framework：抓住可复用机制，而不是只记论文名。
4. Experiments / Evaluation：判断任务、指标、baseline、成本和可复现性。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted Page 1 / Abstract 补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：belief consistency

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：这是从 reward action 转向 reward belief 的核心机制。
- 原文短摘：
  > ReBel introduces belief-consistency supervision
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - belief state 如何表示，以及和 Agent State / Observation 的边界。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Agent State]]
  - [[Trajectory Evaluation]]
  - [[Evaluation]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

#### 必读块 2：feedback discrepancy

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：说明 dense signal 来自预测 belief 与环境反馈的差异。
- 原文短摘：
  > converting discrepancies between predicted beliefs and observed feedback
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - 这种自监督信号是否需要外部 verifier，能否用于 tool agent trace。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Agent State]]
  - [[Trajectory Evaluation]]
  - [[Evaluation]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

#### 必读块 3：belief-aware grouping

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：这是降低 advantage 方差和比较轨迹的机制。
- 原文短摘：
  > belief-aware grouping to compare trajectories under similar belief states
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - 相似 belief state 下的 trajectory 比较是否能迁移到 WebShop / ALFWorld 外。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Agent State]]
  - [[Trajectory Evaluation]]
  - [[Evaluation]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

### 选读

- 相关工作：看作者如何定位相邻方向，避免把方法名误当通用概念。
- 附录 / implementation details：只在需要复现、写 topic 对比或更新概念卡时细读。

### 可以先跳过

- 过细的 dataset appendix、长引用列表和非主线 ablation，除非后续要写评测或复现细节。

### 读完要能回答

- 这篇论文真正改变的是 Agent 的 runtime、memory、tool policy、evaluation，还是某个垂直应用流程？
- 它的关键证据来自实验、系统设计、benchmark 构造、案例分析，还是作者的框架性定义？
- 哪些结论可以迁移到 Hermes / Obsidian / Agent 工程，哪些只能留在论文任务设定里？

### 读完要更新

- [[02 问题池]]：记录精读后仍不确定的边界。
- [[05 Query 写回队列]]：沉淀可以回答面试/工程判断的问题。
- 可能更新的概念卡：[[Agent State]]、[[Trajectory Evaluation]]、[[Evaluation]]、[[Planning]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 长程 agent 的 credit assignment 可从 action-level 转向 belief-state consistency。 | extracted Page 1 / Abstract | medium | [[Trajectory Evaluation]] |
| 部分可观测环境中，belief drift 会让延迟奖励更难归因。 | extracted Page 1 / Abstract | medium | [[Agent State]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：ReBel 用结构化 belief state 和 belief-consistency supervision 给长程 agent 提供更密集的过程级训练信号。
- 输入 / 输出：以论文任务设定为准，精读时补充数据、工具、轨迹、reward、verifier 或 memory object 的具体格式。
- 关键步骤：当前先记录 Page 1 / Abstract 的机制入口；后续精读 Method / Framework 时补 section、figure、table anchor。
- 和相邻方法的差别：先通过 `related` 概念卡校准，不把标题名直接当作新稳定概念。

## 实验 / 证据

- 数据集 / benchmark：待精读 Experiments / Evaluation 后补充。
- 指标：待精读后补充任务成功率、过程指标、成本、安全、faithfulness 或 risk 指标。
- 关键结果：当前只保留摘要级 claim，不写成稳定结论。
- 作者给出的局限：需要优先读 Limitations / Discussion。

## 现代性 / 前沿性初判

- frontier / watch：这是 2026-05 arXiv preprint，适合作为前沿 evidence，不直接当成工程标准。
- 今天仍然稳定的部分：它提出的问题边界能帮助检查现有 Agent / RAG / LLM 系统的失败模式。
- 已被现代系统吸收或替代的部分：待和框架文档、复现实验、后续论文、开源实现或社区实践对齐。
- 需要 freshness 复查的部分：术语命名、benchmark 可用性、代码/数据开放、后续正式版本和社区采用情况。

## 已提取文件

- PDF：`assets/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.pdf`
- Extracted Markdown：`extracted/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.extracted.md`
- 抽取质量提醒：pypdf 自动抽取；公式、表格、图、伪代码、脚注和双栏阅读顺序可能有损失。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂不新建概念卡；先链接到相关已有概念。
- 已更新的 topic / map：[[资料收集索引]]、[[03 前沿追踪]]、[[04 页面目录]]。
- 还没处理的证据：Method、Evaluation、Limitations 的精读摘录和 page / figure anchor。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| Belief-state credit assignment | 先放 P2；等 agent RL / post-training 专题再考虑建卡。 | extracted Page 1 / Abstract | P2 |
| ReBel | 方法名先停在 source。 | extracted Page 1 / Abstract | P3 |

## 我的疑问

- belief state 在工程 Agent 里是 explicit state schema、模型隐状态，还是 trace summary？
- 这种训练方法对非 RL 的 Hermes 任务诊断有什么可迁移边界？

## 边界提醒

- 这是 arXiv preprint / frontier source；录入为 `status: seed` 和 `freshness: watch`。
- 当前只做 source-level 证据落地，不把论文标题里的方法名直接升格为稳定概念。
- 如果后续精读发现术语和现有概念卡同义、上下位或相邻，需要先做中英文术语 / canonical name 审计。
- 任何性能、benchmark、安全或医疗 claim 都要回到正文图表、实验设置和 limitation 后再写入概念卡。

## 原文摘录

- 摘录入口：[[Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.extracted#Page 1]]
- arXiv abstract：<https://arxiv.org/abs/2605.20061>
- 本页只保留短摘和定位；长段落查看本地 extracted 或 PDF。
