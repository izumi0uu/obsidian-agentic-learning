---
type: map
topic:
  - evaluation
  - agent
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Eval Harness]]"
  - "[[LLM-as-Judge]]"
  - "[[Task Success Rate]]"
  - "[[RAG Evaluation]]"
  - "[[Trajectory Evaluation]]"
evidence:
  - "[[Evaluation#证据锚点]]"
  - "[[Benchmark#证据锚点]]"
  - "[[Eval Harness#证据锚点]]"
  - "[[LLM-as-Judge#证据锚点]]"
  - "[[Task Success Rate#证据锚点]]"
  - "[[RAG Evaluation#证据锚点]]"
  - "[[Trajectory Evaluation#证据锚点]]"
related:
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Replay]]"
  - "[[Patch Validation]]"
  - "[[Trajectory Trace 类型对比]]"
---

# Evaluation 层次对比

## 一句话总览

这页把 Agent 评测拆成层次：[[Evaluation]] 是总的判断过程，[[Benchmark]] 给固定任务协议，[[Eval Harness]] 把任务跑成可复现实验，[[Task Success Rate]] 是端到端结果指标，[[LLM-as-Judge]] 是一种语义评估器，[[RAG Evaluation]] 和 [[Trajectory Evaluation]] 分别把评测下沉到检索链路和行动轨迹。

最小边界：benchmark 不是 evaluation 全部；success rate 不是失败解释；judge 不是最终真理；harness 不是指标，而是把样例、运行、trace、score 和 replay 连接起来的工程外壳。

## 为什么这组值得对比

- 混淆风险：学习 Agent evaluation 时，很容易把“榜单分数”“一次 judge 打分”“任务成功率”“评测平台”混成同一个词。
- 共同问题域：它们都回答“系统是否真的完成任务、过程是否可接受、改动是否退化”。
- 不同介入点：有的定义任务，有的运行任务，有的给指标，有的评语义，有的评检索链路，有的评行动过程。
- 证据密度：相关概念卡已经沉淀了 GAIA、SWE-bench、LangSmith、Langfuse、OpenAI Agents SDK、Microsoft RAG 等 source anchors。
- 复习价值：这组概念能训练“看一个评测结果时，我到底该问哪个问题”。

边界：这页不是评测工具选型，也不追踪最新 leaderboard；具体工具和分数属于易变信息，需要单独复查。

## 共同问题域

共同问题是：LLM / Agent 的能力不能只靠 demo 或流畅回答判断。系统需要任务、样例、运行协议、过程记录、评分方法、失败归因和回归验证。

可以把 evaluation 链路粗略拆成：

```text
evaluation goal
  -> benchmark / business dataset / failure samples
  -> eval harness runner + environment
  -> trace / outputs / artifacts
  -> scorer: rules / tests / LLM-as-Judge / human / metrics
  -> report: success rate, failure taxonomy, regression evidence
  -> replay / new regression cases
```

不同概念的区别，不是“谁更高级”，而是它切入这条链路的哪一层。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Evaluation]] | 总体判断目标、样例和标准 | 贯穿开发、上线、复盘 | 任务目标、数据、rubric、trace、业务信号 | 是否有效/稳定/安全的判断 | [[Evaluation#证据锚点]] |
| [[Benchmark]] | 固定任务集和评分协议 | 评测前定义，运行后报告 | 标准任务、环境限制、评分规则 | 可比较分数或通过率 | [[Benchmark#证据锚点]] |
| [[Eval Harness]] | 运行、记录、评分和报告的工程外壳 | 批量执行任务并保存证据 | dataset、runner、environment、scorer | trace、score、diff、报告、失败样本 | [[Eval Harness#证据锚点]] |
| [[Task Success Rate]] | 端到端任务完成指标 | 任务执行后统计 | 成功判定、总任务数、通过样本 | 成功比例 | [[Task Success Rate#证据锚点]] |
| [[LLM-as-Judge]] | 语义质量评估器 | 输出后或轨迹后评分 | 被评内容、rubric、judge prompt | score、label、理由 | [[LLM-as-Judge#证据锚点]] |
| [[RAG Evaluation]] | 检索、上下文、引用和回答链路 | retrieve 前后、generate 后分层检查 | query、chunks、context、answer、citations | retrieval/context/generation/citation 分层结果 | [[RAG Evaluation#证据锚点]] |
| [[Trajectory Evaluation]] | Agent 行动路径是否可接受 | 执行后或运行中检查 trajectory | tool calls、observations、权限、trace、结果 | 过程安全/有效/合规/经济判断 | [[Trajectory Evaluation#证据锚点]] |

## 最容易混淆的边界

### Evaluation vs Benchmark

[[Evaluation]] 是更大的判断过程：它包括任务定义、数据、指标、评估器、运行机制、线上监控和回归样本。[[Benchmark]] 只是其中一类固定任务协议。Benchmark 高分不能自动证明真实产品可靠，因为真实任务分布、工具边界、权限和用户数据可能不同。

### Benchmark vs Eval Harness

[[Benchmark]] 提供“测什么、怎么判、怎么报告”；[[Eval Harness]] 负责“怎么稳定跑、怎么收集 trace、怎么保存 artifacts、怎么比较版本”。没有 harness，benchmark 容易变成一次性手动跑题；没有 benchmark 或业务 dataset，harness 又缺少稳定比较对象。

### Task Success Rate vs Evaluation

[[Task Success Rate]] 是入口指标，说明任务完成比例；[[Evaluation]] 还要解释失败原因、过程风险、成本、延迟、用户体验和回归情况。一个 Agent 可以 success rate 上升，但同时多次越权、成本暴涨或依赖偶然网页状态。

### LLM-as-Judge vs Evaluation

[[LLM-as-Judge]] 是 evaluator 家族中的一种，适合语义质量、忠实性、解释清晰度和弱监督筛查；它不替代规则、测试、人审、业务指标和安全检查。高风险任务应优先用确定性 checker，judge 作为辅助信号。

### RAG Evaluation vs Trajectory Evaluation

[[RAG Evaluation]] 的核心问题是证据链：有没有检到、上下文是否完整、引用是否支持答案。[[Trajectory Evaluation]] 的核心问题是行动路径：工具顺序、权限、观察读取、失败恢复和副作用是否可接受。Agentic RAG 可能同时需要两者。

## 执行时序 / 机制差异

```text
Benchmark:           define tasks + protocol -> run -> report comparable score
Eval Harness:        dataset -> runner/environment -> trace/artifacts -> scorer -> report/replay
Task Success Rate:   completed tasks / all tasks after checker
LLM-as-Judge:        output/trajectory + rubric -> judge model -> score/reason
RAG Evaluation:      query -> retrieve/context/citation/generation checks
Trajectory Eval:     trace/trajectory -> rules/judge/human -> process judgment
```

把它们放在现代 Agent 开发循环里：

```text
线上失败 trace -> dataset / replay case -> eval harness -> rules/tests/judge -> report -> release gate -> new production monitoring
```

这条闭环是工程综合，不是某个单一 source 的原文定义。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

像训练一个新司机：

| Agent 评测概念 | 类比 | 类比边界 |
|---|---|---|
| [[Benchmark]] | 固定驾考路线和评分规则 | 现实路况更复杂，不能只信驾考成绩 |
| [[Eval Harness]] | 考试组织系统：发车、记录路线、计时、保存违规证据 | harness 是运行装置，不是评分标准本身 |
| [[Task Success Rate]] | 有多少次成功到达终点 | 不说明是否闯红灯或耗油过高 |
| [[LLM-as-Judge]] | 教练根据录像评价驾驶习惯 | 教练会主观，仍需硬规则 |
| [[Trajectory Evaluation]] | 检查整条行驶路线是否安全合规 | 不只看是否到达 |
| [[RAG Evaluation]] | 检查导航资料是否准确、引用是否支持路线 | 只适合有外部证据链的任务 |

## 现代系统如何吸收或限制

- 来源支持：[[Evaluation]]、[[Eval Harness]]、[[LLM-as-Judge]]、[[RAG Evaluation]]、[[Trajectory Evaluation]] 的证据锚点共同支持 trace、dataset、evaluator、score、experiment、benchmark、RAG 分层检查和过程评估这些现代评测部件。
- 工程综合 / inference：成熟系统通常把 evaluation 拆成多信号组合：规则/测试先判硬条件，judge 处理语义，trace 解释失败，replay 固化回归，human review 覆盖高风险边界。
- 仍需警惕的外推：不要把某个平台的 UI、字段名或榜单当前分数写成长期稳定事实；具体 API、leaderboard 和模型表现需要按 source freshness 重新检查。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 想横向比较系统在固定任务上的能力 | [[Benchmark]] | 它定义任务集、协议和分数口径 | 可能被污染、刷分或不贴近真实业务 |
| 想稳定回归测试 prompt / model / workflow 改动 | [[Eval Harness]] | 它能批量运行、保存 trace、比较版本 | harness 配置变化会让结果不可比 |
| 想看用户任务端到端是否完成 | [[Task Success Rate]] | 它是任务完成的第一层指标 | 不解释失败原因，也不保证过程安全 |
| 想批量筛查回答是否忠实、清楚、符合 rubric | [[LLM-as-Judge]] | 适合语义质量和弱监督评分 | judge 偏差、漂移、诱导和隐私风险 |
| 想定位 RAG 是检索错还是生成错 | [[RAG Evaluation]] | 它把 retrieval/context/generation/citation 拆开 | 只看最终答案会混淆根因 |
| 想判断 Agent 工具路径是否安全合规 | [[Trajectory Evaluation]] | 它评估整条路径，而不只看输出 | 需要足够 trace；软 judge 不能替代硬规则 |

## 它们共同不是什么

- 都不是“模型自我感觉良好”的证明。
- 都不能单独保证生产可靠性；真实系统还需要监控、权限、回滚、人工升级和安全评审。
- 都不是静态一次性动作；有价值的 evaluation 会把失败样本持续写回 regression / replay。
- 都不是无证据的主观印象；至少应能回到任务、trace、source note、checker、rubric 或人工记录。

## 证据锚点

- Concept anchors: [[Evaluation#证据锚点]], [[Benchmark#证据锚点]], [[Eval Harness#证据锚点]], [[LLM-as-Judge#证据锚点]], [[Task Success Rate#证据锚点]], [[RAG Evaluation#证据锚点]], [[Trajectory Evaluation#证据锚点]]
- Source examples: [[GAIA Benchmark#为什么收]], [[SWE-bench#为什么收]], [[LangSmith Evaluation and Observability#一句话]], [[Langfuse Observability and Evaluation#一句话]], [[OpenAI Agents SDK 文档#Tracing 补充]], [[Microsoft RAG 官方文档#一句话]]
- Evidence type: existing concept-card synthesis + benchmark/docs/source notes + clearly labeled engineering synthesis + learning analogy.
- Confidence: medium-high for layer boundaries; medium for modern-system workflow details because platform能力和 judge 实践会变化。
- Boundary: “evaluation 闭环”是本页综合框架；具体 benchmark 分数、平台字段和最新 judge 能力需要另行复查。

## 复习触发

1. 为什么 benchmark 高分不等于真实业务 evaluation 通过？
2. 如果 Task Success Rate 上升但越权 tool call 增加，这算不算 Agent 可靠性提升？
3. LLM-as-Judge 适合判断什么？什么时候必须让规则、测试或人审优先？
4. RAG Evaluation 和 Trajectory Evaluation 分别会看 trace 里的哪些不同证据？
5. 把一次线上失败转成回归样本时，Eval Harness 至少要保存什么？

## 相关链接

- [[Evaluation]]
- [[Benchmark]]
- [[Eval Harness]]
- [[LLM-as-Judge]]
- [[Task Success Rate]]
- [[RAG Evaluation]]
- [[Trajectory Evaluation]]
- [[Trace]]
- [[Replay]]
- [[Observability]]
- [[Trajectory Trace 类型对比]]
- [[LLM Wiki 工作流]]
