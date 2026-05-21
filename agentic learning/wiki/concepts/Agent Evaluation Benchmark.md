---
type: concept
topic:
  - evaluation
  - agent
  - benchmark
status: growing
created: 2026-05-21
updated: 2026-05-21

up:
  - "[[Benchmark]]"

last_checked: 2026-05-21
freshness: watch
conflicts: []
aliases:
  - 智能体评估基准
  - Agent Benchmark
  - Agentic Benchmark
  - Agentic Evaluation Benchmark
source:
  - "[[BFCL - Berkeley Function Calling Leaderboard]]"
  - "[[GAIA Benchmark]]"
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research]]"
  - "[[Do Androids Dream of Breaking the Game - BenchJack]]"
  - "[[OpenComputer - Verifiable Software Worlds for Computer-Use Agents]]"
evidence:
  - "[[BFCL - Berkeley Function Calling Leaderboard#关键事实]]"
  - "[[GAIA Benchmark#需要我读的内容]]"
  - "[[GAIA Benchmark#Ingest 摘要]]"
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research#实验 / 证据]]"
  - "[[Do Androids Dream of Breaking the Game - BenchJack#为什么收]]"
  - "[[Do Androids Dream of Breaking the Game - BenchJack#边界提醒]]"
  - "[[OpenComputer - Verifiable Software Worlds for Computer-Use Agents#为什么收]]"
related:
  - "[[Benchmark]]"
  - "[[Evaluation]]"
  - "[[BFCL]]"
  - "[[Eval Harness]]"
  - "[[LLM-as-Judge]]"
  - "[[Task Success Rate]]"
---

# Agent Evaluation Benchmark

## 一句话

Agent Evaluation Benchmark 是专门评估智能体在工具调用、真实环境交互、多步任务、多智能体协作或通用助手任务中表现的 benchmark 家族。

## 概念详解

普通 [[Benchmark]] 可以是静态问答、数学题、代码题或模型知识测试；Agent Evaluation Benchmark 的特点是把“会回答”推进到“能行动、能使用工具、能在环境里完成任务”。它通常不只给模型一个 prompt，而是定义任务目标、可用工具或环境、运行协议、评分 checker、报告指标和失败样本复现方式。

这个概念出现的原因，是 Agent 的能力边界更容易被 demo 掩盖。一个 Agent 可能能说出正确计划，但不会构造工具参数；可能能调用工具，但不读 observation；可能能完成最终答案，但路径越权、成本失控或利用了 benchmark 漏洞。Agent Evaluation Benchmark 要把这些失败面放进固定任务协议里，让不同系统能在相对一致的环境下比较。

可以按被测能力粗分成几类：

| 类别 | 代表项 | 主要测什么 | 当前 vault 处理 |
|---|---|---|---|
| 工具调用能力评估 | [[BFCL]], ToolBench, API-Bank | 工具选择、参数构造、多工具/多轮调用、无关工具干扰 | [[BFCL]] 已有 source + concept；ToolBench / API-Bank 先作为待补来源的代表项 |
| 通用 Agent / Assistant 能力评估 | [[GAIA Benchmark]], AgentBench, WebArena | 多步推理、网页/文件/工具组合、环境交互、任务完成 | GAIA 已有 raw source；AgentBench / WebArena 先作为待补来源的代表项 |
| 多智能体 / 社交协作评估 | ChatEval, SOTOPIA, 自定义协作场景 | 多角色沟通、协作质量、社交互动或群体判断 | 暂不建弱卡；等 source note 或具体项目需要时再拆 |
| 计算机使用 / 可验证软件世界 | OpenComputer, WebArena, OSWorld 等 | GUI/浏览器/桌面环境中的可验证任务成功 | 已有 [[OpenComputer - Verifiable Software Worlds for Computer-Use Agents]] raw source 支撑方向边界 |

小边界：这张卡收的是“benchmark 家族”，不是把所有评估组件都当成子概念。[[LLM-as-Judge]] 是 evaluator，Win Rate 是 pairwise metric，AIME 数据集加载器是 [[Eval Harness]] 的 input adapter，AST / quasi-exact matching 是 checker / scorer。它们可以进入同一个评估报告，但不是 Agent Evaluation Benchmark 的子类。

## 它解决什么问题

它解决的是 Agent 能力如何用可复查任务协议评估的问题。对 Hermes 这类长期运行的 Agent，不能只问“模型回答质量如何”，还要问：

- 是否会选择正确工具并构造参数。
- 是否会根据 observation 继续推进。
- 是否能在网页、文件、软件环境或多源证据中完成任务。
- 是否能在多轮、多步骤、错误恢复和权限边界下保持稳定。
- 分数是否来自真正完成任务，而不是 exploit checker 或讨好 judge。

## 它不是什么

它不是 [[Evaluation]] 的全部。Evaluation 还包括业务回归集、线上监控、人工复盘、安全评审、trace 复盘和发布门禁。

它也不是 [[Eval Harness]]。Benchmark 定义任务和评分协议；harness 负责加载数据、运行任务、记录 trace、执行 scorer、生成报告和复现失败。

它也不是 evaluator 或 metric。[[LLM-as-Judge]]、Win Rate、Accuracy、Exact Match、F1、AST matching、quasi-exact matching 都是判定或汇总方式，不是任务集本身。

## 最小例子

一个工具调用 Agent benchmark case 可以长这样：

```text
task: 订出下周三从上海到北京的最早航班
allowed tools: search_flights, book_flight, ask_user_confirmation
success checker: 是否选择正确航班，是否在支付前请求确认，是否没有调用无关工具
report metric: task success rate + tool-call accuracy + unsafe-action count
```

这里的 benchmark 是任务和协议；dataset loader 只是把 case 读进 runner；AST checker、规则 checker 或 LLM judge 负责判分；最终报告再汇总 success rate、win rate、失败类型和 trace。

## 常见误解 / 风险

- 误解：把 BFCL、GAIA、AIME、LLM Judge、Win Rate 画在同一张图里，就说明它们是同一类对象。实际它们分属任务层、评估器层、指标层和 harness 层。
- 误解：Agent benchmark 高分等于生产可靠。真实生产还要看权限、隐私、成本、稳定性、用户目标和业务数据。
- 误解：LLM Judge 可以替代 benchmark。Judge 可以评分，但它不定义任务分布。
- 风险：benchmark 本身也有攻击面。BenchJack 这类工作提醒我们，Agent 可能优化分数而不完成真实任务。
- 风险：环境 benchmark 如果 checker 太弱，Agent 可能通过字符串匹配、状态漏洞或 evaluator prompt injection 获得虚高分。

## 边界细节

可写入本卡 `up` 子类的对象，必须满足三个条件：

1. 它本身是 benchmark / task set / environment protocol，而不是单个指标、评分器、加载器或报告。
2. 它的任务目标明显评估 Agent / assistant 的行动能力、工具能力、环境交互、多步任务或协作能力。
3. 它有 source note、官方/论文证据或已精读证据，能说明任务、环境和评分协议。

因此 [[BFCL]] 可以作为工具调用方向的子概念；[[GAIA Benchmark]] 当前在 vault 中是 raw source 标题，暂不创建同名 concept 以避免 Obsidian 标题碰撞；ToolBench、API-Bank、AgentBench、WebArena、ChatEval 和 SOTOPIA 先记录为代表项，不在本轮强行建弱卡。

和相邻概念的边界：

- [[Benchmark]]：更宽，包含所有固定任务/评分协议；Agent Evaluation Benchmark 是其中面向 Agent 的一支。
- [[Evaluation]]：更宽的质量判断过程；可以包含 benchmark、业务样例、线上监控和人审。
- [[Eval Harness]]：运行 benchmark 的工程外壳，不是 benchmark 家族。
- [[LLM-as-Judge]]：语义评估器，不是 benchmark。
- [[Task Success Rate]]：结果指标，不是 benchmark。
- [[Trajectory Evaluation]]：过程评估方法，可用于 Agent benchmark，但不是任务集本身。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 为什么：Agent benchmark 已经是当前工程和研究比较模型/系统能力的基本入口；但 web、GUI、computer-use、多智能体、可验证软件世界和 reward-hacking 防护仍在快速变化。
- 稳定部分：任务、环境、工具边界、checker、报告口径必须明确。
- 易变部分：具体 benchmark 版本、leaderboard、数据污染情况、模型排名、运行预算和 checker 安全性。
- 复查点：当 ToolBench / AgentBench / WebArena / SOTOPIA 等进入正式 source note 后，再决定是否拆独立概念卡并挂到本卡下。

## 现代系统怎么吸收 Agent Evaluation Benchmark 的价值 / 局限

现代系统不应该只拿外部榜单当结论，而应该把它们转成内部评估设计启发：

- 从 BFCL 学工具调用类别和 checker。
- 从 GAIA 学真实助手任务和短答案可验证设计。
- 从 WebArena / OpenComputer 类方向学可验证软件环境和任务终态检查。
- 从 BenchJack 学 benchmark 也需要 threat modeling、checker hardening 和失败样本复盘。
- 从 Rollout Cards 类工作学记录环境、依赖、agent scaffold、运行预算和可复现 trace。

它的局限也很清楚：公开 benchmark 的任务分布不等于你的产品任务，leaderboard 分数不等于权限安全，成功率也不说明失败原因。对自建 Agent，最好的吸收方式是建立自己的小型 benchmark + eval harness + trace/replay 回归集。

## 证据锚点

- Source: [[BFCL - Berkeley Function Calling Leaderboard]]
- Source: [[GAIA Benchmark]]
- Source: [[Rollout Cards - A Reproducibility Standard for Agent Research]]
- Source: [[Do Androids Dream of Breaking the Game - BenchJack]]
- Source: [[OpenComputer - Verifiable Software Worlds for Computer-Use Agents]]
- Anchors: [[BFCL - Berkeley Function Calling Leaderboard#关键事实]], [[GAIA Benchmark#需要我读的内容]], [[GAIA Benchmark#Ingest 摘要]], [[Rollout Cards - A Reproducibility Standard for Agent Research#实验 / 证据]], [[Do Androids Dream of Breaking the Game - BenchJack#为什么收]], [[Do Androids Dream of Breaking the Game - BenchJack#边界提醒]], [[OpenComputer - Verifiable Software Worlds for Computer-Use Agents#为什么收]]
- Evidence type: benchmark source notes + paper source notes + engineering synthesis.
- Confidence: medium-high for layer boundary; medium for individual benchmark examples without local source notes.
- Boundary: 本卡不记录最新 leaderboard 排名；未建 source note 的 benchmark 只作为分类代表项，不能作为强事实展开。

## 复习触发

- 为什么 Agent Evaluation Benchmark 不是 [[LLM-as-Judge]] 或 Win Rate？
- BFCL 为什么适合挂在这张卡下，而 AIME 数据集加载器不适合？
- 如果我要评估 Hermes 的信息雷达 Agent，哪些任务该借鉴 GAIA，哪些该借鉴 BFCL？
- 为什么 benchmark 本身也要做 reward-hacking / checker 安全审计？

## 相关链接

- [[Benchmark]]
- [[Evaluation]]
- [[BFCL]]
- [[Eval Harness]]
- [[LLM-as-Judge]]
- [[Task Success Rate]]
- [[Evaluation 层次对比]]
