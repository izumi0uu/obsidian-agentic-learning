---
type: source
source_type: paper
title: "OpenComputer: Verifiable Software Worlds for Computer-Use Agents"
url: https://arxiv.org/abs/2605.19769
pdf: assets/OpenComputer - Verifiable Software Worlds for Computer-Use Agents.pdf
extracted: extracted/OpenComputer - Verifiable Software Worlds for Computer-Use Agents.extracted.md
arxiv: https://arxiv.org/abs/2605.19769
doi: 10.48550/arXiv.2605.19769
author:
  - Jinbiao Wei
  - Qianran Ma
  - Yilun Zhao
  - Xiao Zhou
  - Kangqi Ni
  - Guo Gan
  - Arman Cohan
site: arXiv
venue: arXiv 2026
pages:
topic:
  - agent
  - computer-use
  - benchmark
  - evaluation
  - gui
  - frontier
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: watch
conflicts: []
status: seed
source: https://arxiv.org/abs/2605.19769
related:
  - "[[Computer Use]]"
  - "[[Benchmark]]"
  - "[[Eval Harness]]"
  - "[[Trajectory Evaluation]]"
  - "[[Task Success Rate]]"
  - "[[GUI Grounding]]"
---

# OpenComputer: Verifiable Software Worlds for Computer-Use Agents

## 原文信息

- 论文标题：OpenComputer: Verifiable Software Worlds for Computer-Use Agents
- 作者：Jinbiao Wei, Qianran Ma, Yilun Zhao, Xiao Zhou, Kangqi Ni, Guo Gan, Arman Cohan
- 提交日期：2026-05-19
- 学科：arXiv cs.AI / cs.CL / related（以 arXiv 页面为准）
- URL：<https://arxiv.org/abs/2605.19769>
- PDF：<https://arxiv.org/pdf/2605.19769v1>
- 本地 PDF：`assets/OpenComputer - Verifiable Software Worlds for Computer-Use Agents.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/OpenComputer - Verifiable Software Worlds for Computer-Use Agents.extracted.md`
- 阅读优先级：P1-A

边界：这一页是 raw source note，只回答“论文原文目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把 Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇补 computer-use agent 评测的可验证环境层：不是只问 agent 能不能点按钮，而是软件世界能不能给出结构化状态、partial credit、trajectory 和自动 verifier。

## 一句话

OpenComputer 用 app-specific verifiers、任务生成和 evaluation harness 构造可机器检查的软件世界，帮助评估 computer-use agent 的真实状态完成度。

## 先读什么

1. Abstract / Page 1：确认问题定义、作者主张和方法对象。
2. Introduction：看它纠正的是哪个旧误解或工程痛点。
3. Method / Framework：抓住可复用机制，而不是只记论文名。
4. Experiments / Evaluation：判断任务、指标、baseline、成本和可复现性。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted Page 1 / Abstract 补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：app-specific verifier

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：这是 verifiable software world 的基础，不是单纯 LLM-as-judge。
- 原文短摘：
  > app-specific state verifiers that expose structured inspection endpoints
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - 每个应用如何暴露可检查状态，以及 verifier 的信任边界。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Computer Use]]
  - [[Benchmark]]
  - [[Eval Harness]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

#### 必读块 2：self-evolving verifier

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：说明评测环境本身也需要改进和校准。
- 原文短摘：
  > a self-evolving verification layer that improves verifier reliability
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - verifier 可靠性如何用 execution-grounded feedback 改进，避免自动判定本身漂移。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Computer Use]]
  - [[Benchmark]]
  - [[Eval Harness]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

#### 必读块 3：trajectory + partial credit

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：这和普通 pass/fail benchmark 的区别最大。
- 原文短摘：
  > records full trajectories and computes auditable partial-credit rewards
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - partial credit 如何避免掩盖失败，也如何帮助训练或诊断。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Computer Use]]
  - [[Benchmark]]
  - [[Eval Harness]]
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
- 可能更新的概念卡：[[Computer Use]]、[[Benchmark]]、[[Eval Harness]]、[[Trajectory Evaluation]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| computer-use agent 评测需要应用状态 verifier，而不能只依赖最终截图或 LLM-as-judge。 | extracted Page 1 / Abstract | high | [[Computer Use]] |
| 可验证软件世界应记录完整轨迹并支持可审计 partial-credit reward。 | extracted Page 1 / Abstract | high | [[Trajectory Evaluation]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：OpenComputer 用 app-specific verifiers、任务生成和 evaluation harness 构造可机器检查的软件世界，帮助评估 computer-use agent 的真实状态完成度。
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

- PDF：`assets/OpenComputer - Verifiable Software Worlds for Computer-Use Agents.pdf`
- Extracted Markdown：`extracted/OpenComputer - Verifiable Software Worlds for Computer-Use Agents.extracted.md`
- 抽取质量提醒：pypdf 自动抽取；公式、表格、图、伪代码、脚注和双栏阅读顺序可能有损失。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂不新建概念卡；先链接到相关已有概念。
- 已更新的 topic / map：[[资料收集索引]]、[[03 前沿追踪]]、[[04 页面目录]]。
- 还没处理的证据：Method、Evaluation、Limitations 的精读摘录和 page / figure anchor。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| Verifiable software world | 可能值得建 evaluation 子概念，但要先和 [[Eval Harness]] / [[Benchmark]] 对齐。 | extracted Page 1 / Abstract | P1 |
| App-specific state verifier | 可能作为 computer-use eval 的机制候选。 | extracted Page 1 / Abstract | P2 |

## 我的疑问

- OpenComputer 的 verifier 覆盖 33 个桌面应用，但哪些状态检查仍需要人工判定？
- 它与 OSWorld / WebArena / MiniWoB 的差异能否沉淀成 computer-use benchmark 对比？

## 边界提醒

- 这是 arXiv preprint / frontier source；录入为 `status: seed` 和 `freshness: watch`。
- 当前只做 source-level 证据落地，不把论文标题里的方法名直接升格为稳定概念。
- 如果后续精读发现术语和现有概念卡同义、上下位或相邻，需要先做中英文术语 / canonical name 审计。
- 任何性能、benchmark、安全或医疗 claim 都要回到正文图表、实验设置和 limitation 后再写入概念卡。

## 原文摘录

- 摘录入口：[[OpenComputer - Verifiable Software Worlds for Computer-Use Agents.extracted#Page 1]]
- arXiv abstract：<https://arxiv.org/abs/2605.19769>
- 本页只保留短摘和定位；长段落查看本地 extracted 或 PDF。
