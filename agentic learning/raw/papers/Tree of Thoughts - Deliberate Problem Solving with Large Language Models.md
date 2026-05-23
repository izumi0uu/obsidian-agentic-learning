---
type: source
source_type: paper
title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
url: https://arxiv.org/abs/2305.10601
pdf: https://arxiv.org/pdf/2305.10601v2
arxiv: https://arxiv.org/abs/2305.10601
author:
  - Yao et al.
site: arXiv
venue: NeurIPS 2023
topic:
  - llm
  - reasoning
  - planning
  - prompting
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: stable
conflicts: []
status: seed
source: https://arxiv.org/abs/2305.10601
related:
  - "[[Tree of Thoughts]]"
  - "[[Zero-shot CoT]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[Reasoning Trace]]"
  - "[[Planning]]"
---

# Tree of Thoughts - Deliberate Problem Solving with Large Language Models

## 为什么收

这篇论文适合补齐 [[Zero-shot CoT]] 之后的一个关键边界：如果 CoT 只有一条推理链，走错方向时很难纠偏，那么能不能把推理过程显式组织成搜索空间，让模型生成候选思路、评估、剪枝、回溯，再选择更好的路径。

它也能帮助区分 prompt-time reasoning、搜索式推理和工程化 [[Agent Workflow]]：ToT 可以调用 LLM 多次并做搜索控制，但它解决的仍是“问题求解中的 reasoning path 选择”，不是完整的工具执行、状态持久化、权限治理或生产 workflow。

## 一句话

Tree of Thoughts 是把 CoT 的单条推理链扩展成多分支“思路树”的推理框架：生成候选 thought，评估候选，按搜索策略继续展开或回溯，最后得到答案。

## 需要我读的内容

目标：理解 Tree of Thoughts 为什么从“生成一条推理链”升级到“在 thought 空间里搜索”，以及它和 [[Zero-shot CoT]]、[[Plan-and-Solve Prompting]]、[[ReAct]]、[[Agent Workflow]] 的粒度边界。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / CoT 的左到右单路径限制

- 位置：arXiv abstract / 2305.10601v2 / last checked 2026-05-23
- 为什么必读：这里说明 ToT 要解决的不是普通 prompt 表达问题，而是 token-level left-to-right 推理在需要探索、lookahead 和关键初始决策时的局限。
- 原文短摘：
  > token-level, left-to-right decision-making
- 中文概括：
  - 普通语言模型推理默认按 token 从左到右生成，早期方向一旦选错，后面容易沿着错误路径继续展开。
  - ToT 的问题意识是：复杂任务可能需要探索多个候选方向，而不是只生成一条链。
- 我需要理解的机制：
  1. 单路径生成的路径依赖
  2. exploration / lookahead
  3. CoT 到搜索式 reasoning 的升级
- 支撑概念：
  - [[Tree of Thoughts]]
  - [[Zero-shot CoT]]
  - [[Reasoning Trace]]
- 证据边界：
  - 这段只支持 ToT 的问题背景；不能推出所有任务都应该使用多分支搜索。

#### 必读块 2：Method intuition / 多候选 thought 与自评估

- 位置：arXiv abstract / 2305.10601v2 / last checked 2026-05-23
- 为什么必读：这里支撑 ToT 的核心机制：thought 是比 token 更大的中间单位，模型可以比较多条候选路径并决定下一步。
- 原文短摘：
  > multiple different reasoning paths
- 中文概括：
  - ToT 把中间推理步骤组织成 coherent units of text，也就是 thought。
  - 系统在每一层生成多个候选 thought，再通过模型自评估或搜索策略决定保留、展开、回溯或丢弃哪些路径。
- 我需要理解的机制：
  1. thought as intermediate step
  2. candidate generation
  3. self-evaluation / pruning
- 支撑概念：
  - [[Tree of Thoughts]]
  - [[Planning]]
  - [[Task Success Rate]]
- 证据边界：
  - 这段支持 ToT 是 inference-time framework；不等于模型训练后“内置了 ToT”，也不等于返回完整真实思维。

#### 必读块 3：Result boundary / 成本换成功率

- 位置：arXiv abstract / 2305.10601v2 / last checked 2026-05-23
- 为什么必读：这里给出 ToT 的效果边界：论文展示了在 Game of 24、Creative Writing、Mini Crosswords 等需要规划或搜索的任务上改善问题求解能力。
- 原文短摘：
  > 4% of tasks
- 中文概括：
  - 论文摘要报告 Game of 24 上 GPT-4 + CoT 只解出 4%，ToT 方法达到 74%。
  - 这个结果说明多分支搜索可以显著提高某些搜索/规划任务的成功率，但代价是多次模型调用、评估和搜索控制。
- 我需要理解的机制：
  1. inference-time search
  2. success-rate vs cost tradeoff
  3. task selection boundary
- 支撑概念：
  - [[Tree of Thoughts]]
  - [[Task Success Rate]]
  - [[Evaluation]]
- 证据边界：
  - 这个结果来自特定任务和实验设置；不能泛化成所有问答、所有模型或所有生产场景都应启用 ToT。

### 选读

- Full paper 的 algorithm / prompt examples：用于理解 BFS / DFS、candidate generation 和 value prompt 的具体实现。
- Game of 24、creative writing、mini crossword 的实验细节：用于校准哪些任务真正需要搜索。
- 官方代码仓库：<https://github.com/princeton-nlp/tree-of-thought-llm>，用于查看 prompt 和搜索流程。

### 可以先跳过

- 具体任务的完整 prompt 模板和长表格；第一轮先抓机制和工程取舍。

### 读完要能回答

- ToT 和 Zero-shot CoT 的最小区别是什么？
- ToT 为什么不是 Agent Workflow？
- 什么任务值得用多分支搜索，什么任务只会浪费 token？
- ToT 和 GoT 的边界是什么？

### 读完要更新

- [[Tree of Thoughts]]
- [[Zero-shot CoT]]
- [[Plan-and-Solve Prompting]]
- [[LLM 主题]]
- [[Agent 知识地图]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| ToT 将 CoT 从单条推理链扩展为可探索、评估、回溯的 thought 搜索空间。 | Abstract / ToT framework description | high | [[Tree of Thoughts]] |
| ToT 在需要非平凡规划或搜索的任务上能显著提高问题求解表现。 | Abstract / Game of 24 result | medium | [[Task Success Rate]] |
| ToT 的价值来自 inference-time 多路径搜索，因此需要额外调用、评估和搜索控制成本。 | Abstract + engineering synthesis from method shape | medium | [[Evaluation]] |

边界：这张 source note 只记录论文证据与定位；稳定解释写入 `wiki/concepts/`，并回链到本页小节。未本地保存 PDF，精读页码和 section 需要以后补。

## 可以拆成概念卡

- [[Tree of Thoughts]]
- thought / reasoning state
- value prompt / self-evaluation
- search-based inference
- Graph of Thoughts（先保留相邻候选，不在本轮建弱卡）

## 我的疑问

- ToT 在现代 reasoning model 上的边际收益是否下降，还是只在可搜索任务上仍然明显？
- 什么时候应把 ToT 的搜索控制交给外部代码，什么时候只让模型一次性列多个方案并自评？
- GoT 是否值得单独成卡，还是先作为 ToT 的相邻边界保留？

## 边界提醒

ToT 不是给所有问题都加“复杂思考”。对“法国首都是什么”这类单跳事实题，多分支搜索基本只会增加延迟和 token 成本。它更适合答案空间需要探索、候选路径可评估、错误早期决策会显著影响最终结果的任务。

ToT 也不是 [[ReAct]] 或 [[Agent Workflow]]。它可以多次调用 LLM 并进行搜索，但核心仍是 reasoning path selection；没有天然的外部工具执行、Observation 回填、权限控制、持久 state、checkpoint、human approval 或生产级失败恢复。
