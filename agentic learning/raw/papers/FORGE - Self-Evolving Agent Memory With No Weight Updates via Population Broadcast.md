---
type: source
source_type: paper
title: "FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast"
url: https://arxiv.org/abs/2605.16233
pdf: assets/FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.pdf
extracted: extracted/FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.extracted.md
arxiv: https://arxiv.org/abs/2605.16233
doi: 10.48550/arXiv.2605.16233
author:
  - "Igor Bogdanov"
  - "Chung-Horng Lung"
  - "Thomas Kunz"
  - "Jie Gao"
  - "Adrian Taylor"
  - "Marzia Zaman"
site: arXiv
venue: arXiv 2026
pages:
topic:
  - agent
  - memory
  - self-improvement
  - trajectory
  - reflexion
  - frontier
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
status: seed
source: https://arxiv.org/abs/2605.16233
related:
  - "[[Memory Reflection]]"
  - "[[Long-term Memory]]"
  - "[[Trajectory]]"
  - "[[ReAct]]"
  - "[[Agent Robustness]]"
  - "[[Evaluation]]"
---

# FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast

## 原文信息

- 论文标题：FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
- 作者：Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
- 提交日期：2026-05-15
- 学科：cs.AI, cs.CL, cs.LG, cs.MA, eess.SY
- URL：<https://arxiv.org/abs/2605.16233>
- PDF：<https://arxiv.org/pdf/2605.16233v1>
- 本地 PDF：`assets/FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.extracted.md`
- 阅读优先级：P1

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把 Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇关注 agent 如何从失败轨迹中提炼可复用 memory / rule / demo，而不更新模型权重，直接对应生产 Agent 的 failure-driven learning。

## 一句话

FORGE 研究通过 population broadcast 共享失败经验，让 Agent 在不微调权重的情况下积累可复用记忆。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent / RAG / reasoning 误读。
3. Method / Framework：抓住可复用机制，不急着抄结果数字。
4. Experiments / Evaluation：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用 arXiv metadata 和本地 extracted 文本补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：Abstract / 问题定位

- 位置：arXiv Abstract；本地 extracted Page 1 交叉核对
- 为什么必读：先确认作者把问题定义在哪一层，避免只按标题理解。
- 原文短摘：
  > Can LLM agents improve decision-making through self-generated memory without gradient updates?
- 中文概括：
  - 这段用来定位论文要解决的旧问题，以及它和现有 Agent / RAG / LLM 工程概念的关系。
  - 当前摘录只证明作者在摘要中如何界定问题；不能替代方法、实验和限制章节的精读。
- 我需要理解的机制：
  1. 原文里的系统对象、输入输出和约束分别是什么。
  2. 这条证据属于问题定义、方法机制、benchmark，还是结果 claim。
  3. 它能否外推到其他 Agent 场景，取决于正文实验设置、artifact 和 limitations。
- 支撑概念：
  - [[Memory Reflection]]
  - [[Long-term Memory]]
  - [[Trajectory]]
- 证据边界：
  - 这条短摘只证明摘要层的 claim；精读前不要把标题术语升格为稳定概念卡。

#### 必读块 2：方法 / 机制入口

- 位置：arXiv Abstract；后续精读 Method / Framework
- 为什么必读：抓住作者提出的核心机制或系统设计，而不是只记论文名。
- 原文短摘：
  > We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents.
- 中文概括：
  - 这段提供第一轮机制线索，用来决定后续精读时应看系统组件、算法步骤、数据流还是评价协议。
  - 如果正文方法和摘要表述不一致，以正文方法、图表和限制为准。
- 我需要理解的机制：
  1. 方法是否要求训练、运行时编排、检索、工具调用或人工介入。
  2. 机制收益来自模型能力、系统结构、数据组织，还是评测协议。
  3. 是否存在成本、权限、安全、复现或长期维护代价。
- 支撑概念：
  - [[Memory Reflection]]
  - [[Long-term Memory]]
  - [[Trajectory]]
- 证据边界：
  - 这条短摘不能证明方法已经优于所有 baseline；需要读 Evaluation / Ablation / Limitations。

#### 必读块 3：评测 / 外推边界

- 位置：arXiv Abstract；后续精读 Experiments / Limitations
- 为什么必读：确认论文 claim 的任务范围、指标和不可外推边界。
- 原文短摘：
  > FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed...
- 中文概括：
  - 这段帮助判断论文是 benchmark、system、training method、safety framework 还是应用场景评估。
  - 后续写入概念卡时，必须标明证据是否只是 arXiv preprint 和特定实验环境。
- 我需要理解的机制：
  1. benchmark / dataset / task 是否和真实 Agent 系统一致。
  2. 指标是否覆盖过程、成本、失败样本和安全边界。
  3. 结果是否依赖特定模型、工具、数据集或训练预算。
- 支撑概念：
  - [[Memory Reflection]]
  - [[Long-term Memory]]
  - [[Trajectory]]
- 证据边界：
  - 如果短摘包含数字、排名、benchmark、性能提升或用户研究，必须回正文图表核对后才能写成稳定结论。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Agent 可以从失败轨迹中提炼经验，而不一定要更新模型权重。 | Abstract / method | medium | [[Memory Reflection]] |
| 群体广播可能把个体失败经验扩散成共享 memory。 | Method | medium | [[Multi-agent Orchestration]] |

边界：没有读到 section/page/figure 时，先写 source note 小节，不要伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：从摘要看，论文围绕 `FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast` 提出一个前沿方向；具体机制待精读 Method / Framework。
- 输入 / 输出：先按论文任务设定理解，后续需要回到正文确认数据、工具、轨迹或 reward 的形式。
- 关键步骤：当前只记录摘要级机制入口；精读时补充 section、figure、table。
- 和相邻方法的差别：先通过 `related` 概念卡校准，不把标题名直接当作新稳定概念。

## 实验 / 证据

- 数据集 / benchmark：待精读 Experiments / Evaluation 后补充。
- 指标：待精读后补充任务成功率、过程指标、成本、安全或 fairness 指标。
- 关键结果：当前只保留摘要级 claim，不写成稳定结论。
- 作者给出的局限：需要优先读 Limitations / Discussion。

## 现代性 / 前沿性初判

- frontier / watch：这是 2026-05 arXiv preprint，适合做前沿 evidence，不直接当成工程标准。
- 今天仍然稳定的部分：它提出的问题边界能帮助检查现有 Agent / RAG / LLM 系统的失败模式。
- 已被现代系统吸收或替代的部分：待和框架文档、复现实验、后续论文对齐。
- 需要 freshness 复查的部分：术语命名、benchmark 可用性、代码/数据开放、后续正式版本和社区采用情况。

## 已提取文件

- PDF：`assets/FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.pdf`
- Extracted Markdown：`extracted/FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.extracted.md`
- 抽取质量提醒：pypdf 自动抽取；公式、表格、图、伪代码、脚注和双栏阅读顺序可能有损失。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂不新建概念卡；先链接到相关已有概念。
- 已更新的 topic / map：[[资料收集索引]]、[[03 前沿追踪]]、[[04 页面目录]]。
- 还没处理的证据：Method、Evaluation、Limitations 的精读摘录和 page / figure anchor。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| self-evolving memory | 与 Reflexion 和 memory reflection 相邻，需精读后判断是否建卡。 | Abstract / source note | P1 |
| [[Memory Reflection]] | 失败复盘如何变成下次可用规则。 | Abstract / source note | P1 |
| [[Trajectory]] | 失败轨迹作为学习材料。 | Abstract / source note | P1 |

## 我的疑问

- 生成的 rule / demo 如何验证不过拟合？
- population broadcast 是否会传播错误经验？
- 记忆冲突、版本和回滚机制如何设计？

## 边界提醒

- 这是 arXiv preprint / frontier source；录入为 `status: seed` 和 `freshness: watch`。
- 当前只做 source-level 证据落地，不把论文标题里的方法名直接升格为稳定概念。
- 如果后续精读发现术语和现有概念卡同义、上下位或相邻，需要先做中英文术语 / canonical name 审计。
- 任何性能、benchmark 或安全 claim 都要回到正文图表、实验设置和 limitation 后再写入概念卡。

## 原文摘录

- 摘录入口：[[FORGE - Self-Evolving Agent Memory With No Weight Updates via Population Broadcast.extracted#Page 1]]
- arXiv abstract：<https://arxiv.org/abs/2605.16233>
- 本页只保留短摘和定位；长段落查看本地 extracted 或 PDF。
