---
type: source
source_type: web
title: Workflow Guardrails Primary Sources
url:
author: multiple
site: multiple
topic:
  - agent
  - workflow
  - security
  - guardrails
  - frontier
created: 2026-05-14
updated: 2026-05-14
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: growing
source:
related:
  - "[[Workflow Guardrails]]"
  - "[[Guardrails]]"
  - "[[Agent Workflow]]"
  - "[[Policy Engine]]"
  - "[[Agent Workflow Static Verification]]"
---

# Workflow Guardrails 主源

## 为什么收

这组资料的学习价值不在于“guardrails”这个词本身新，而在于多个框架和厂商文档都在把 guardrails 放到 workflow / agent execution 的具体控制点上：input、output、tool call、retrieval、execution、callback、filter、validator、state hook、transaction 和 automation。

这能补上当前 wiki 里 [[Guardrails]] 卡的一个边界：guardrails 不只是最终回答过滤器，也不只是某个 SDK 的功能名；它正在变成 [[Agent Workflow]] 里的节点/边/中间件/状态边界。

## 一句话

Workflow guardrails 是把安全、质量、权限、格式和副作用控制放在 workflow 的关键边界上，而不是只在最终回答上做一次检查。

## 主源阅读顺序

| 来源 | 链接 | 支撑什么 | 学习用途 |
|---|---|---|---|
| OpenAI Agents SDK Guardrails | <https://openai.github.io/openai-agents-python/guardrails/> | 明确 input guardrails、output guardrails、tool guardrails 的 workflow boundaries；input 只跑第一层，output 只跑最终输出，tool guardrails 包在自定义 function tool 调用周围。 | 高优先级；支撑 [[Workflow Guardrails]] 的“不是只看 agent 输入输出”边界。 |
| LangChain Guardrails | <https://docs.langchain.com/oss/python/langchain/guardrails> | 把 guardrails 作为 middleware 放在 before agent、after agent、around model/tool calls；区分 deterministic 和 model-based guardrails，并有 PII / HITL 方向。 | 高优先级；支撑 middleware / execution control point 视角。 |
| NVIDIA NeMo Guardrails Configuration Guide | <https://docs.nvidia.com/nemo/guardrails/0.12.0/user-guides/configuration-guide.html> | 把 rails 分成 input、output、dialog、retrieval、execution；retrieval rails 在检索后触发，execution rails 在 action 前后触发。 | 高优先级；支撑“guardrail 可以在 retrieval / execution 边上”的分类。 |
| AWS Bedrock ApplyGuardrail API | <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html> | `ApplyGuardrail` 可在应用流程中独立评估输入或输出，不必绑定 foundation model 调用。 | 高优先级；对 Bedrock / service workflow 架构有工程启发。 |
| Guardrails AI - The Guard | <https://guardrailsai.com/docs/concepts/guard> | `Guard` 返回 raw LLM output、validated output 和 validation success。 | 中高；支撑“LLM 输出不能直接写 DB，要先变成 validated output”。 |
| Guardrails AI - Validators | <https://guardrailsai.com/docs/concepts/validators/> | validator 是质量控制单元，可组合到输入/输出检查。 | 中高；支撑 schema、格式、PII、业务字段校验的组合模型。 |
| Guardrails AI - Validator OnFail Actions | <https://guardrailsai.com/guardrails/docs/concepts/validator_on_fail_actions> | `REASK`、`FIX`、`FILTER`、`REFRAIN`、`EXCEPTION` 等失败动作。 | 中高；适合映射成 workflow failure policy。 |
| Microsoft Semantic Kernel Filters | <https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/filters> | Function invocation filter、prompt render filter、auto function invocation filter，类似 middleware。 | 中高；支撑“不要把 guardrail 散落在业务代码里”的拦截层思路。 |
| Google ADK Callbacks | <https://google.github.io/adk-docs/callbacks/> | before/after agent、model、tool 等 callback 控制点，可观察或干预 agent 行为。 | 中；支撑 callback 控制点，但具体 API 快速变化。 |
| Anthropic - Building Effective Agents | <https://www.anthropic.com/research/building-effective-agents> | parallelization workflow 可让一个模型处理请求、另一个模型筛查不当内容。 | 中；支撑 guardrail 可以是并行 workflow 分支。 |
| IBM Research - Guardrails in generative AI workflows via orchestration | <https://research.ibm.com/publications/guardrails-in-generative-ai-workflows-via-orchestration> | 通过 orchestration 编排 detector/model server；强调 production-ready 要考虑 performance、scalability、extensibility、maintainability。 | 中；支撑 workflow orchestration 视角。 |
| Agentproof - Static Verification of Agent Workflow Graphs | <https://arxiv.org/abs/2603.20356> | runtime guardrails 只能对执行路径反应；显式 workflow graph 可在部署前做结构/时序检查。 | 已沉淀；用于切开 runtime guardrails 与 static verification。 |

## 可以拆成概念卡

- [[Workflow Guardrails]]：值得做成 durable 概念卡。稳定部分是“控制点放在 workflow 边界”，不是某个 SDK 参数名。
- Guardrail failure policy：暂不单独建卡，先并入 [[Workflow Guardrails]] 和 [[Workflow Guardrails 与 Prefect 控制点映射]]。如果以后某个具体项目 / Prefect 实践里出现稳定模式，再拆。
- Tool guardrail / execution rail：暂不单独建卡，先作为 [[Workflow Guardrails]] 的边界细节。

## 不值得单独成卡

- OpenAI Guardrails API、LangChain guardrails middleware、ADK callback 类型、Semantic Kernel filter 类型：它们是 volatile 产品/API 能力，不应直接升级成稳定概念卡。
- `REASK` / `FIX` / `FILTER` / `REFRAIN` / `EXCEPTION`：适合做 failure policy 枚举，不必每个动作建页。
- Prefect state hooks、transactions、automations：更适合记录为 workflow control points source note，再映射到 guardrail 承载方式。

## 我的疑问

- Agent workflow graph 是否会在主流框架里内置 compile-time guardrail lint，还是继续交给外部安全工具？
- tool guardrail 应该放在 model tool call 之前、内部 API 之前、DB 写入之前，还是三层都要放？
- model-based guardrails 与 deterministic guardrails 的成本/延迟/误判怎么在生产 workflow 中组合？

## 边界提醒

- 本页是来源聚合，不是“所有来源都同等权威”。官方 SDK/docs 支撑工程控制点；Anthropic/IBM 支撑 workflow 叙事；Agentproof 支撑静态验证互补关系。
- “workflow 使用 guardrails 是主流工程方向”可以写入 [[Workflow Guardrails]]；但具体产品 API、版本、命名、内置能力都应保持 `freshness: watch`。
- 具体项目 / Prefect 映射属于工程综合，不是这些文档直接声明某个业务系统应该这样实现。
