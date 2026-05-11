---
type: concept
topic:
  - llm
  - infrastructure
  - observability
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[LLM]]"
  - "[[Observability]]"
  - "[[Policy Engine]]"
  - "[[Evaluation]]"
---

# LLM Gateway

## 一句话

LLM Gateway 是统一管理模型调用的网关层，负责路由、重试、fallback、限流、成本、日志、策略和供应商切换。

## 概念详解

生产 Agent 往往不会直接把每次请求硬编码到一个模型供应商。不同任务对模型能力、延迟、价格、上下文长度、地区合规、结构化输出、工具调用和可用性有不同要求。LLM Gateway 把这些调用治理放到统一层：请求先进网关，再由网关根据策略选择模型、记录成本、处理重试或 fallback。

它在架构上像“模型调用入口”，但不是模型本身。对 Agent 来说，gateway 还会影响 tool calling 的稳定性、trace 的完整性、prompt 日志的隐私边界、评测数据的采集，以及不同供应商行为差异带来的回归风险。

社区常把 LiteLLM、Portkey、OpenRouter、Vercel AI Gateway 这类产品放在同一类里，但它们的定位并不完全相同：有的偏 provider 兼容和路由，有的偏日志与治理，有的偏模型市场入口。概念上不要把“能转发请求”误认为“能保证质量”；gateway 最多提供可控入口，质量仍要靠评测、prompt/tool schema、数据和人工边界验证。

在现代 Agent 系统中，gateway 往往是 observability、policy、evaluation 和 cost control 的连接点。它记录每次模型调用的 metadata，让团队知道哪个任务用了哪个模型、花了多少钱、失败在哪里，也让模型升级可以通过灰度、A/B 和回滚，而不是一次性替换全系统。

对 learning vault 来说，LLM Gateway 是理解“模型不是孤立 API 调用”的入口。它把模型选择、供应商失败、成本预算、审计日志和数据边界显式化；但它不会自动理解业务目标，也不会替代 Agent 的 planning、tool permissioning 或 final verification。
## 它解决什么问题

生产 Agent 往往不只调用一个模型。不同任务需要不同模型、价格、延迟、上下文长度和可用性。Gateway 把这些策略集中管理。

它还让团队能统一记录 token、成本、延迟、错误、供应商状态和 fallback 结果，而不是每个业务模块各自散落一套模型调用逻辑。

## 它不是什么

LLM Gateway 不是模型本身，也不会自动让弱模型变强。

它也不能自动保证回答质量。它解决的是调用治理，不是推理正确性；质量仍需要 [[Evaluation]]、prompt / tool schema 设计、数据质量和人工校验。

它也不等于 [[Policy Engine]]。Policy Engine 负责规则和决策；Gateway 可以执行或调用这些策略，但二者不是同一层。

## 最小例子

```text
agent request
-> gateway receives model intent and metadata
-> policy chooses provider/model
-> gateway applies retry/fallback/rate limit
-> logs cost/latency/error/trace id
-> returns model response
```

如果主模型超时，gateway 可以 fallback 到备用模型；但如果备用模型不支持同样的 tool schema，Agent 行为可能改变。

## 常见误解和风险

- fallback 到弱模型可能改变行为。
- 日志里可能包含敏感 prompt、用户数据或 tool result。
- 多供应商路由需要处理数据合规和模型差异。
- 只看成功率不够；还要看结构化输出、工具调用兼容性和评测回归。

## 边界细节

和 [[Observability]] 的边界：gateway 可以产生调用日志和指标，但 observability 还包括 trace、span、业务事件和评估结果。

和 [[Evaluation]] 的边界：gateway 能把请求分流给不同模型，evaluation 才能判断哪种路由更好。没有评测，fallback 只是可用性策略，不是质量保证。

和 [[Agent Harness]] 的关系：harness 负责 agent loop 和工具执行；gateway 负责模型调用入口。两者在 trace id、tool schema、retry 和错误处理上需要对齐。

## 现代性状态

LLM Gateway 是当前工程实践，带有前沿 / 易变实现层。

- 基础地基：API gateway、rate limiting、routing、retry 和 logging 是成熟基础设施思想。
- 当前工程实践：多模型 Agent 系统会用 gateway 管理 provider、cost、latency、fallback 和 tracing。
- 前沿 / 易变：不同供应商的 tool calling、structured output、reasoning controls、batch / realtime API 和合规字段变化快，gateway 适配层需要持续复查。

## 现代系统怎么吸收 LLM Gateway 的价值

现代系统把模型调用从业务代码里抽出来，使 agent 可以按任务选择模型、按风险记录审计、按成本设置预算、按错误做 fallback，并把调用数据接入 observability / evaluation。

这也让模型升级更可控：不是全系统同时换模型，而是通过 gateway 做灰度、A/B、回滚和评测对比。

## 证据锚点

- Evidence type: engineering source note / infrastructure source — [[Agent 工程基础设施主源]]。
- Boundary: source note 支持 LLM Gateway 作为基础设施主题和代表生态；具体 LiteLLM、Portkey、OpenRouter、Vercel AI Gateway 的最新能力、隐私策略和 API 字段需要查各自官方文档。
- Engineering synthesis: “gateway 连接 observability、evaluation、policy 和 agent harness”是架构层总结，不应当当作某个产品的官方承诺。
- Confidence: medium。

## 复习触发

- LLM Gateway 解决的是质量问题还是调用治理问题？
- fallback 为什么可能带来行为回归？
- Gateway、Policy Engine、Observability、Evaluation 分别处在哪一层？

## 相关链接

- [[LLM]]
- [[Observability]]
- [[Policy Engine]]
- [[Evaluation]]
