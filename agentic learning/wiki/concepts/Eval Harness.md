---
type: concept
topic:
  - evaluation
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-21
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[SWE-bench]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[LangSmith Evaluation and Observability#一句话]]"
  - "[[LangSmith Evaluation and Observability#边界提醒]]"
  - "[[Langfuse Observability and Evaluation#一句话]]"
  - "[[Langfuse Observability and Evaluation#边界提醒]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
  - "[[SWE-bench#为什么收]]"
  - "[[SWE-bench#Ingest 摘要]]"
related:
  - "[[Agent Harness]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Trace]]"
  - "[[Task Success Rate]]"
---

# Eval Harness

## 一句话

Eval Harness 是自动运行任务、记录过程、收集输出、打分并复现失败的评测外壳。

## 概念详解

Eval Harness 之所以需要单独成概念，是因为“知道要评估什么”和“稳定地把评估跑起来”不是同一件事。[[Evaluation]] 负责定义判断目标、样例和标准；Eval Harness 负责把这些东西变成可重复执行的工程系统。没有 harness，团队往往只能手动挑几个例子试 prompt、看一次输出、凭感觉判断；有了 harness，同一批任务可以在不同模型、prompt、工具版本和代码版本下重复运行，并留下可比较证据。

从组成上看，一个 eval harness 通常包含 dataset loader、dataset、runner、environment、instrumentation、evaluator / scorer、result store 和 report。dataset loader 把 AIME、GAIA、BFCL 或业务 JSONL 这类来源统一成可运行 case：题目、答案、split、metadata、允许工具、预算、评分配置；dataset 定义要跑哪些样例；runner 把每个样例交给模型、RAG pipeline 或 Agent；environment 固定工具、repo snapshot、检索索引、权限和随机性；instrumentation 记录 [[Trace]]、成本、延迟、工具调用、错误和中间状态；scorer 可以是规则、测试、人工、[[LLM-as-Judge]] 或业务指标；result store 和 report 负责比较版本、定位回归、沉淀失败样本。

[[LangSmith Evaluation and Observability]] 的 source note 把 trace、dataset、evaluator、experiment 和 production monitoring 组织成一个评测与观测闭环；[[Langfuse Observability and Evaluation]] 的 source note 则强调 trace、score、experiment、regression 这条工作流。它们支持一个重要判断：harness 不只是“跑分脚本”，而是把可观测过程和质量判断连接起来。[[OpenAI Agents SDK 文档]] 的 tracing 补充说明模型调用、工具调用、handoff、guardrail 等可以被组织成 trace，这给 Agent eval harness 的过程记录提供了现代工程证据。

[[SWE-bench]] 是理解 harness 的好例子：任务不是问模型一道题，而是给真实 GitHub issue 和 repo snapshot，让系统生成 patch，再应用 patch、运行测试、看 fail-to-pass 是否通过。这里 benchmark 定义任务和标准，但 harness 负责准备环境、运行 Agent、应用 patch、执行测试、保存 diff / trace / 日志和最终结果。这个边界很细：没有可复现执行环境，SWE-bench 只是一组任务描述；有了 harness，它才变成能比较模型和 Agent 系统的实验装置。

现代系统吸收 Eval Harness 的方式，通常是把它放进开发循环和发布门禁：小样本用于本地快速检查，回归集用于 CI，线上失败 trace 被转成新 eval case，高风险动作要额外检查 trajectory / permission / data leak。证据边界也要分清：LangSmith / Langfuse / OpenAI SDK source notes 支持 trace、dataset、evaluator、score、monitoring、tracing 等部件；“dataset-runner-environment-scorer-report”这个组件拆分是本 vault 的工程综合模型。

## Dataset Loader 边界

Dataset loader 是 harness 的输入适配器，不是评估器。它负责把不同来源整理成统一结构，例如：

```text
AIME loader:
  problem -> expected answer -> split/year -> metadata

BFCL loader:
  user request -> function docs -> expected call/state -> category

GAIA loader:
  question -> files/web/multimodal inputs -> expected short answer -> difficulty
```

Loader 的输出还没有被评估；它只是让 runner 可以批量执行。真正的评分发生在 scorer / checker 层：AIME 可能用 exact match 或数值答案检查，BFCL 可能用 AST / executable / state-based check，开放式数据生成质量可能用 [[LLM-as-Judge]]、Win Rate 或人工验证。

小边界：把 AIME 题目加载进系统，只说明 harness 能读数据；不说明模型会推理，也不说明 evaluator 可靠。很多评估 bug 其实出在 loader：答案字段读错、split 混淆、metadata 丢失、样本过滤不一致，都会让 report 看起来正常但结论失真。

## 它解决什么问题

Agent demo 成功一次不代表系统可靠。Eval Harness 让同一批任务能被重复运行，帮助比较不同模型、prompt、工具、检索策略和代码版本。

它通常包括数据集、执行器、工具环境、评分器、trace、结果存储和报告。

## 它不是什么

Eval Harness 不是单个 benchmark。

Benchmark 是任务集合或分数标准；Eval Harness 是把任务跑起来并能复现、比较、分析失败的系统。

## 现代性状态

Eval Harness 属于 current-practice。

现代 agent 系统通常把它做成 CI 里的评测流水线：固定数据集、固定版本的模型/提示词/工具环境、可回放 trace、可版本化评分器和失败归因。概念本身稳定，具体实现会随平台与工作流变化。

## 最小例子

代码 Agent 的 eval harness：

- 给定一个 GitHub issue 和 repo snapshot。
- 让 Agent 修改代码。
- 应用 patch。
- 跑测试。
- 保存 trace、diff、日志、回放所需状态和最终评分。

## 常见误解 / 风险

- 只看最终分数会丢掉失败原因。
- 只用 LLM-as-judge 评分会引入裁判偏差。
- 测试集太少会让 prompt 过拟合。
- 评测环境和生产环境差太远时，分数会虚高。

## 边界细节

- Eval Harness 负责“跑、记、比、复现”，不只是出一个分数。
- Dataset loader 负责“读入和标准化样例”，不负责判断答案好坏。
- Benchmark 负责定义任务和标准；Harness 负责执行、记录和回放。
- 对 agent 任务，最好同时保存数据集版本、工具版本、种子、trace、patch、judge 输出和失败归因。
- 只保存最终得分，通常不足以定位回归。

## 现代系统怎么吸收它的价值

- 把 eval 绑进 CI/CD 或模型发布门禁。
- 对失败样本做 replay 和 regression tracking。
- 用版本化 judge prompt / rubric 降低评分漂移。
- 将 harness 输出接到 observability 面板里，而不是只看排行榜。

## 证据锚点

- Platform / official-practice sources: [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]], [[OpenAI Agents SDK 文档]]
- Anchors: [[LangSmith Evaluation and Observability#一句话]], [[LangSmith Evaluation and Observability#边界提醒]], [[Langfuse Observability and Evaluation#一句话]], [[Langfuse Observability and Evaluation#边界提醒]], [[OpenAI Agents SDK 文档#Tracing 补充]]
- Benchmark source: [[SWE-bench]]
- Anchors: [[SWE-bench#为什么收]], [[SWE-bench#Ingest 摘要]]
- Evidence type: official/community platform docs + benchmark paper source note + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 trace/dataset/evaluator/experiment/score/tracing 和 SWE-bench 任务形态；harness 组件拆分与 CI/发布门禁用法是工程综合理解。

## 复习触发

- 什么时候一个系统更像 benchmark，什么时候更像 eval harness？
- 为什么只看最终分数不够？
- harness 里哪些部分更稳定，哪些部分更容易过期？

## 相关链接

- [[Agent Harness]]
- [[Evaluation]]
- [[Trace]]
- [[Replay]]
- [[Trajectory Evaluation]]
