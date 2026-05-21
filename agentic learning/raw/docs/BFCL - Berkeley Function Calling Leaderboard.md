---
type: source
source_type: docs
title: Berkeley Function Calling Leaderboard
url: https://gorilla.cs.berkeley.edu/leaderboard.html#leaderboard
author: UC Berkeley Gorilla / LMSYS
site: gorilla.cs.berkeley.edu
topic:
  - agent
  - tool-use
  - benchmark
  - evaluation
created: 2026-05-21
updated: 2026-05-21
last_checked: 2026-05-21
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[BFCL]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Benchmark]]"
  - "[[Eval Harness]]"
  - "[[Evaluation]]"
---

# BFCL - Berkeley Function Calling Leaderboard

## 为什么收

BFCL 是理解 [[Tool Calling]] 能力评估的代表性来源。它把函数/工具调用从“模型能不能输出 JSON”推进到可执行评估、并行/多函数调用、多轮多步调用，以及 V4 的 agentic web search / memory / format sensitivity。

## 一句话

BFCL 是 UC Berkeley Gorilla 团队维护的 function/tool calling benchmark 和评测工具链，用来评估 LLM 选择函数、填参数、处理相关/无关工具、执行多步工具路径和生成可判定调用结果的能力。

## 关键事实

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| BFCL 以 function calling / tool calling 能力为核心评估对象。 | 官方 README / Introduction | high | [[BFCL]], [[Tool Calling]] |
| BFCL v1 覆盖 simple、multiple、parallel、parallel-multiple 等调用形态，并使用 AST evaluation / executable evaluation / relevance detection 等判定方式。 | BFCL v1 blog / Evaluation Methodology | high | [[BFCL]], [[Benchmark]] |
| BFCL v3 增加 multi-turn / multi-step function calling，并把 state-based 和 response-based checks 结合起来。 | BFCL v3 blog / Evaluation Metrics | high | [[Trajectory Evaluation]], [[Eval Harness]] |
| BFCL v4 把 web search、memory、format sensitivity 纳入 agentic evaluation 方向，并在 changelog 中引入 agentic domain / format_sensitivity 等目录结构。 | BFCL V4 blog series + official GitHub changelog | medium-high | [[Agent Robustness]], [[Evaluation]] |
| 官方评测工具把 generation 和 evaluation 分开，输出 result 与 score 文件，并汇总 overall / live / non-live / multi-turn 分数。 | 官方 GitHub README / Running Evaluations | high | [[Eval Harness]] |

边界：BFCL 不是完整生产 Agent 评测。它强在 tool/function calling 轨道，尤其是调用结构、参数、相关性、多步执行和部分 agentic tool path；但真实产品还要额外评估权限、用户目标、业务副作用、隐私、成本、human approval 和线上 trace。

## 需要我读的内容

目标：理解 BFCL 如何把工具调用能力拆成可判定的 benchmark，而不是只看模型是否“说自己要调用工具”。

### 必读

#### 必读块 1：官方 README / Introduction

- 位置：GitHub README / Introduction / last checked 2026-05-21
- 为什么必读：这里说明 BFCL 的总体定位和工具链入口。
- 原文短摘：
  > comprehensive and executable function call evaluation
- 中文概括：
  - BFCL 强调可执行 function call evaluation，而不是只靠文本相似度判断工具调用是否合理。
  - README 还把生成模型响应和评估响应分成两个 CLI 阶段，这是 eval harness 的典型分工。
- 支撑概念：
  - [[BFCL]]
  - [[Eval Harness]]
  - [[Tool Calling]]
- 证据边界：
  - README 支持 BFCL 的工程评测定位；具体榜单分数会随模型和版本变化。

#### 必读块 2：BFCL v1 blog / AST 与可执行评估

- 位置：BFCL v1 blog / Evaluation Methodology / last checked 2026-05-21
- 为什么必读：这里解释 AST evaluation 为什么出现，以及 simple / multiple / parallel 等类别如何判定。
- 原文短摘：
  > AST evaluation and Executable evaluation
- 中文概括：
  - AST evaluation 关注调用结构、函数名、参数键和值类型等是否匹配。
  - executable evaluation 更贴近真实 API 结果，但受外部服务、返回结构和状态影响；AST 常作为补充。
- 支撑概念：
  - [[BFCL]]
  - [[Tool Calling]]
  - [[Benchmark]]
- 证据边界：
  - AST 适合检查结构化工具调用，不等于验证真实业务动作一定正确。

#### 必读块 3：BFCL v3 / 多轮多步

- 位置：BFCL v3 blog / Evaluation Metrics / last checked 2026-05-21
- 为什么必读：这里把 BFCL 从单步调用推进到更像 Agent trajectory 的多轮多步调用评估。
- 原文短摘：
  > state-based evaluation and response-based evaluation
- 中文概括：
  - 多轮任务不能只比对某条固定调用序列，因为模型可能通过不同路径到达正确状态。
  - state-based check 更像终态验证，response-based check 则补充必要调用是否发生。
- 支撑概念：
  - [[Trajectory Evaluation]]
  - [[Eval Harness]]
- 证据边界：
  - state-based check 能覆盖部分行动结果，但仍不自动检查权限、成本或安全。

#### 必读块 4：BFCL V4 / Agentic 方向

- 位置：BFCL V4 blog series + GitHub changelog / last checked 2026-05-21
- 为什么必读：这里说明 BFCL 已从函数调用专项榜扩展到 agentic web search、memory 和 format sensitivity，并在工具链中体现为 agentic / format_sensitivity 相关评测目录。
- 原文短摘：
  > holistic agentic evaluation
- 中文概括：
  - V4 把工具调用放进更接近真实 Agent 的信息获取、记忆读写和格式鲁棒性场景。
  - 官方 changelog 说明 V4 引入 agentic domain，并把 Web Search、Memory Management 作为其中两类；format sensitivity 则作为独立的 agentic format sensitivity 方向进入 V4 系列。
  - 但它仍是特定 benchmark 轨道，不等同于评估完整业务 Agent。
- 支撑概念：
  - [[Evaluation]]
  - [[Agent Robustness]]
  - [[Tool Use]]
- 证据边界：
  - V4 的 agentic 方向说明 benchmark 覆盖面扩大；具体类别、榜单和 API 需求需要按 freshness 复查。

## 可以拆成概念卡

- [[BFCL]]
- [[Tool Calling]]
- [[Eval Harness]]
- [[Trajectory Evaluation]]

## 我的疑问

- BFCL V4 的 agentic 类别和 GAIA / WebArena / OSWorld 的评估边界如何横向比较？
- BFCL 的 official leaderboard 是否把 format sensitivity 计入总分，还是仅作为诊断类类别？
- 对自建 Agent，BFCL 的哪些类别最适合作为工具调用回归测试样本？

## 边界提醒

- BFCL 测 tool/function calling 能力，不等于完整 Agent reliability。
- AST 匹配、state-based check、response-based check 是评分器/判定方法，不是 benchmark 本身。
- 如果本地跑 BFCL 评估 API 模型，电脑压力通常不大；如果跑本地 OSS 模型，则成本主要转移到本地 GPU / vLLM / SGLang 后端。

## 外部链接

- Leaderboard: <https://gorilla.cs.berkeley.edu/leaderboard.html#leaderboard>
- GitHub README: <https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard>
- Test categories: <https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/TEST_CATEGORIES.md>
- BFCL V1 blog: <https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html>
- BFCL V3 blog: <https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html>
- BFCL V4 web search blog: <https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html>
- BFCL V4 memory blog: <https://gorilla.cs.berkeley.edu/blogs/16_bfcl_v4_memory.html>
- BFCL V4 format sensitivity blog: <https://gorilla.cs.berkeley.edu/blogs/17_bfcl_v4_prompt_variation.html>
- Changelog: <https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/CHANGELOG.md>
