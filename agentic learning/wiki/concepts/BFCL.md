---
type: concept
topic:
  - evaluation
  - agent
  - tool-use
  - benchmark
status: seed
created: 2026-05-21
updated: 2026-05-21

up:
  - "[[Agent Evaluation Benchmark]]"

last_checked: 2026-05-21
freshness: watch
conflicts: []
aliases:
  - Berkeley Function Calling Leaderboard
  - Berkeley Function-Calling Leaderboard
  - BFCL 工具调用评测
  - Function Calling Leaderboard
source:
  - "[[BFCL - Berkeley Function Calling Leaderboard]]"
evidence:
  - "[[BFCL - Berkeley Function Calling Leaderboard#关键事实]]"
  - "[[BFCL - Berkeley Function Calling Leaderboard#必读块 1官方 README  Introduction]]"
  - "[[BFCL - Berkeley Function Calling Leaderboard#必读块 2BFCL v1 blog  AST 与可执行评估]]"
  - "[[BFCL - Berkeley Function Calling Leaderboard#必读块 3BFCL v3  多轮多步]]"
  - "[[BFCL - Berkeley Function Calling Leaderboard#必读块 4BFCL V4  Agentic 方向]]"
related:
  - "[[Agent Evaluation Benchmark]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Benchmark]]"
  - "[[Eval Harness]]"
  - "[[Trajectory Evaluation]]"
  - "[[Agent Robustness]]"
  - "[[GAIA Benchmark]]"
relations:
  - type: representative_of
    target: "[[Agent Evaluation Benchmark]]"
    note: "BFCL 是工具/function calling 方向的代表性 Agent evaluation benchmark；代表关系不等于 AST、state check 或 harness 组件本身。"
---

# BFCL

## 一句话

BFCL 是 Berkeley Function Calling Leaderboard，用固定工具调用任务、可执行检查、AST / state / response 等判定方式评估 LLM 的 function/tool calling 能力。

## 概念详解

BFCL 出现的原因，是工具调用不能只靠“模型输出了一段像 JSON 的文本”来判断。一个模型可能格式正确但函数选错，函数选对但参数漏了，参数看似合理但执行后状态不对，或者在多轮任务里反复调用无效工具。BFCL 把这些问题拆进 benchmark：任务集定义用户请求和可用函数，模型生成调用，评测器再用 AST、可执行结果、相关性、多轮状态或路径检查来判断是否通过。

从 v1 的单轮 simple / multiple / parallel / parallel-multiple function calls，到 v3 的 multi-turn / multi-step function calling，再到 v4 的 web search、memory、format sensitivity，BFCL 的范围逐渐从“调用函数”扩展到更 agentic 的工具路径。但它的核心仍然是工具调用能力评估：能否选择正确工具、填对参数、处理无关工具、根据 observation 继续调用，并最终让可检查状态或答案符合预期。

它和 [[GAIA Benchmark]] 的边界很重要。GAIA 更像通用 AI assistant 能力 benchmark，任务常需要推理、网页、文件、多模态和工具组合，最终通常用短答案判定；BFCL 更聚焦工具调用接口和工具路径本身。一个系统 BFCL 很强，说明它更可能稳定地产生正确 tool call；但这不自动说明它能完成任意开放式 Agent 任务、遵守业务权限、做好证据引用或控制成本。

对工程学习来说，BFCL 最值得吸收的是“工具调用评测要分层”：单步结构匹配、执行后状态、相关/无关工具选择、多轮上下文、长上下文、memory、web search 和格式敏感性都可能成为独立失败面。把这些失败面放进 eval harness，比只问模型“你会不会用工具”可靠得多。

## 它解决什么问题

BFCL 解决的是工具调用能力如何可复现评估的问题。它让团队能比较不同模型在函数选择、参数生成、并行/多函数调用、多轮工具使用和部分 agentic 场景里的稳定性。

它也帮助定位工具型 Agent 的失败原因：到底是函数名错、参数错、schema 不稳、无关工具干扰、多轮状态丢失，还是 web search / memory 这类更 agentic 的工具路径失败。

## 它不是什么

BFCL 不是完整生产 Agent 评估。

它不直接替代 [[Trajectory Evaluation]]、[[Agent Robustness]]、权限检查、人工审批、线上 observability 或业务成功指标。一个模型在 BFCL 上分数高，仍可能在真实业务里因为权限、数据污染、工具副作用、上下文装配或成本控制失败。

BFCL 也不是 [[Tool Calling]] 本身。Tool Calling 是接口/能力；BFCL 是评估这类能力的 benchmark 和 harness。

## 最小例子

一个工具调用题给模型三个函数：`get_weather(city)`、`book_flight(origin, dest)`、`send_email(to, body)`。用户问“查一下上海今天的天气”。模型应该只调用：

```json
{"name": "get_weather", "arguments": {"city": "Shanghai"}}
```

AST 评估会看函数名、参数键和值是否匹配；可执行评估会进一步执行工具，看返回结果或状态是否满足预期；多轮场景还会看模型是否能根据前一轮工具结果继续走。

## 常见误解 / 风险

- 误解：BFCL 高分等于 Agent 强。实际它主要说明工具调用轨道强，不能覆盖全部任务完成、权限、安全和业务效果。
- 误解：AST 匹配就是工具调用评估全部。AST 适合结构匹配，但执行状态、多轮路径和外部环境仍需要其他 checker。
- 误解：工具调用类别越多，评估越接近真实业务。类别增加会提高覆盖面，但真实业务还需要自己的工具、权限、数据和失败样本。
- 风险：本地复跑 BFCL 时，API 模型主要消耗 API 成本；本地 OSS 模型会引入 GPU、vLLM / SGLang 和环境配置成本。

## 边界细节

图层位置：

```text
BFCL = benchmark / task set + evaluator + harness tooling for tool/function calling
Tool Calling = 被测能力
AST / executable / state-based / response-based checks = 评分器或判定方法
Eval Harness = 跑 BFCL、记录 result/score、汇总报告的工程外壳
```

和相邻 benchmark 的区别：

- [[GAIA Benchmark]]：通用 assistant 真实任务能力，通常关注最终答案或任务完成。
- [[SWE-bench]]：代码修复任务，核心产物是 patch，通过测试判定。
- BFCL：工具调用能力，核心是函数选择、参数、执行结果和多轮工具路径。

对自建 Agent 的迁移方式：不要直接把 BFCL 当产品上线门槛；更好的做法是借鉴它的类别设计，把自己的内部工具调用失败样本做成小型 BFCL-style regression suite。

层级边界：BFCL 是 [[Agent Evaluation Benchmark]] 的工具调用专项成员；AST / executable / state-based / response-based checks 是评分器或 checker，不是 BFCL 的父概念。[[Eval Harness]] 可以运行 BFCL，但 harness 是工程外壳，不是 BFCL 的严格上位。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 为什么：function/tool calling 已经是现代 Agent 系统地基；BFCL 是这条能力线上有代表性的公开评测。但 V4 的 agentic web search、memory、format sensitivity 和 leaderboard 口径仍会继续变化。
- 稳定部分：工具调用评测需要检查函数选择、参数、相关性、执行结果和多轮状态。
- 易变部分：具体类别、排行榜分数、官方总分权重、模型支持和本地评测命令。
- 复查点：当 BFCL V4/V5 类别或 leaderboard scoring 变化时，优先更新 raw source note 和本卡边界。

## 现代系统怎么吸收 BFCL 的价值 / 局限

现代系统可以把 BFCL 当作工具调用能力的外部参考，同时建立自己的业务工具调用回归集：

- 从 BFCL 学分类：simple、multiple、parallel、irrelevance、multi-turn、memory、web search、format sensitivity。
- 从 BFCL 学 checker：AST 结构匹配、可执行验证、state-based check、response-based check。
- 在自家 Agent 中加入 trace：记录 tool schema、model call、tool arguments、tool result、重试和最终 outcome。
- 对高风险工具另加权限、approval gate、幂等、sandbox 和人工验证。

局限是：BFCL 的工具和任务分布不一定等于你的业务；公开榜单也不能说明某个 Agent 在你的权限、数据、用户目标和成本预算下可靠。

## 证据锚点

- Source: [[BFCL - Berkeley Function Calling Leaderboard]]
- Anchors: [[BFCL - Berkeley Function Calling Leaderboard#关键事实]], [[BFCL - Berkeley Function Calling Leaderboard#需要我读的内容]]
- Evidence type: official leaderboard / GitHub README / official release blogs + engineering synthesis.
- Confidence: medium-high for tool-calling benchmark boundary; medium for V4 agentic scoring details because leaderboard categories and weights may change.
- Boundary: 本卡沉淀 BFCL 的评测边界，不记录当前模型排名或分数。

## 复习触发

- 为什么 BFCL 高分不等于完整 Agent 可靠？
- AST evaluation、executable evaluation、state-based evaluation 分别能发现什么问题？
- 如果要给自己的 Hermes 工具调用做小型 BFCL-style 回归集，第一批样例应该覆盖哪些失败面？

## 相关链接

- [[Tool Calling]]
- [[Tool Use]]
- [[Agent Evaluation Benchmark]]
- [[Benchmark]]
- [[Eval Harness]]
- [[Trajectory Evaluation]]
- [[Agent Robustness]]
- [[Evaluation 层次对比]]
