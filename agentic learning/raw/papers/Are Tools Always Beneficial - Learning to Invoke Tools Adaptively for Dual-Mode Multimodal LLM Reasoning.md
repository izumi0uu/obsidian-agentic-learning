---
type: source
source_type: paper
title: Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
url: https://arxiv.org/abs/2605.19852
pdf: assets/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.pdf
extracted: extracted/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.extracted.md
arxiv: https://arxiv.org/abs/2605.19852
doi: 10.48550/arXiv.2605.19852
author:
  - Qinghe Ma
  - Zhen Zhao
  - Yiming Wu
  - Jian Zhang
  - Lei Bai
  - Yinghuan Shi
site: arXiv
venue: arXiv 2026
pages:
topic:
  - agent
  - tool-use
  - multimodal
  - reasoning
  - evaluation
  - frontier
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: watch
conflicts: []
status: seed
source: https://arxiv.org/abs/2605.19852
related:
  - "[[Tool Use]]"
  - "[[Tool Calling]]"
  - "[[Tool Permissioning]]"
  - "[[Evaluation]]"
  - "[[LLM-as-Judge]]"
---

# Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning

## 原文信息

- 论文标题：Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
- 作者：Qinghe Ma, Zhen Zhao, Yiming Wu, Jian Zhang, Lei Bai, Yinghuan Shi
- 提交日期：2026-05-19
- 学科：arXiv cs.AI / cs.CL / related（以 arXiv 页面为准）
- URL：<https://arxiv.org/abs/2605.19852>
- PDF：<https://arxiv.org/pdf/2605.19852v1>
- 本地 PDF：`assets/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.pdf`（已本地保存；extracted 由 PDF 自动抽取）
- extracted：`extracted/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.extracted.md`
- 阅读优先级：P2

边界：这一页是 raw source note，只回答“论文原文目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把 Page 1 / Abstract 级判断写成论文全文结论。

## 为什么收

这篇纠正“能用工具就用工具”的默认冲动：工具调用有成本，也可能误导推理，适合写回工具选择策略和 orchestration 判断。

## 一句话

AutoTool 学习在 multimodal reasoning 中自适应决定是否调用工具，并在 tool-assisted 与 text-centric 两种模式之间权衡。

## 先读什么

1. Abstract / Page 1：确认问题定义、作者主张和方法对象。
2. Introduction：看它纠正的是哪个旧误解或工程痛点。
3. Method / Framework：抓住可复用机制，而不是只记论文名。
4. Experiments / Evaluation：判断任务、指标、baseline、成本和可复现性。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：本节已用本地 extracted Page 1 / Abstract 补足短摘；这些仍是 source 级 evidence，精读 claim 需要回 PDF 的 section / table / figure 校验。

#### 必读块 1：tool not always helpful

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：这是最值得迁移到 Agent orchestration 的边界句。
- 原文短摘：
  > tool usage is not always beneficial
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - 什么时候不用工具反而更可靠、更便宜或更少误导。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Tool Use]]
  - [[Tool Calling]]
  - [[Tool Permissioning]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

#### 必读块 2：adaptive invocation

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：说明它的核心不是工具执行，而是 invocation policy。
- 原文短摘：
  > adaptively decides whether to invoke tools
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - tool invocation policy 如何训练，能否映射到 web search / code execution / browser 工具选择。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Tool Use]]
  - [[Tool Calling]]
  - [[Tool Permissioning]]
- 证据边界：
  - 这条短摘只证明摘要 / Page 1 层面的 claim；写入概念卡前需要补正文页码、实验设置和 limitation anchor。

#### 必读块 3：dual-mode reward

- 位置：extracted Page 1 / Abstract（必要时连同 Introduction 交叉核对）
- 为什么必读：这决定 tool-assisted 和 text-centric 不是同一个 reward。
- 原文短摘：
  > dual-mode reasoning strategy with mode-specific reward functions
- 中文概括：
  - 这部分提供第一轮 source-level 证据，帮助判断论文主张属于问题定义、方法机制、评测协议还是应用场景。
  - 不同工具模式是否需要不同评价指标和成本惩罚。
  - 精读时需要回到正文 section、figure、table 和 limitations，不能只凭摘要外推成稳定工程标准。
- 我需要理解的机制：
  1. 论文对象、输入输出、运行时组件和验证边界分别是什么。
  2. 机制收益来自模型能力、系统结构、数据组织、训练策略还是评测协议。
  3. 结论是否依赖特定 benchmark、模型、工具、数据集或人工流程。
- 支撑概念：
  - [[Tool Use]]
  - [[Tool Calling]]
  - [[Tool Permissioning]]
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
- 可能更新的概念卡：[[Tool Use]]、[[Tool Calling]]、[[Tool Permissioning]]、[[Evaluation]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| 工具调用不是天然有益；冗余或不当调用会增加成本并误导预测。 | extracted Page 1 / Abstract | high | [[Tool Use]] |
| Agent 需要学习或实现自适应 tool invocation policy，而不是固定总是调用。 | extracted Page 1 / Abstract | medium | [[Tool Calling]] |

边界：这些 claim 当前主要来自本地 extracted Page 1 / Abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：AutoTool 学习在 multimodal reasoning 中自适应决定是否调用工具，并在 tool-assisted 与 text-centric 两种模式之间权衡。
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

- PDF：`assets/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.pdf`
- Extracted Markdown：`extracted/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.extracted.md`
- 抽取质量提醒：pypdf 自动抽取；公式、表格、图、伪代码、脚注和双栏阅读顺序可能有损失。

## Ingest 摘要

- 已沉淀到 wiki 的概念：暂不新建概念卡；先链接到相关已有概念。
- 已更新的 topic / map：[[资料收集索引]]、[[03 前沿追踪]]、[[04 页面目录]]。
- 还没处理的证据：Method、Evaluation、Limitations 的精读摘录和 page / figure anchor。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| Adaptive tool invocation | 可能值得更新 [[Tool 接口层对比]] 或 [[Tool Use]]，但先不建弱卡。 | extracted Page 1 / Abstract | P2 |
| Dual-mode reasoning | 偏论文方法，暂不建卡。 | extracted Page 1 / Abstract | P3 |

## 我的疑问

- AutoTool 的 multimodal tool policy 能否迁移到文本型 web search / browser / code execution？
- 工程系统中 tool cost、latency、risk 应该进入 verifier、router 还是 policy engine？

## 边界提醒

- 这是 arXiv preprint / frontier source；录入为 `status: seed` 和 `freshness: watch`。
- 当前只做 source-level 证据落地，不把论文标题里的方法名直接升格为稳定概念。
- 如果后续精读发现术语和现有概念卡同义、上下位或相邻，需要先做中英文术语 / canonical name 审计。
- 任何性能、benchmark、安全或医疗 claim 都要回到正文图表、实验设置和 limitation 后再写入概念卡。

## 原文摘录

- 摘录入口：[[Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.extracted#Page 1]]
- arXiv abstract：<https://arxiv.org/abs/2605.19852>
- 本页只保留短摘和定位；长段落查看本地 extracted 或 PDF。
