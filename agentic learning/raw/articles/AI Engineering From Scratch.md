---
type: source
source_type: web
title: "AI Engineering From Scratch"
url: https://aiengineeringfromscratch.com/lesson.html
author: Rohit G.
site: aiengineeringfromscratch.com
topic:
  - agent
  - llm
  - learning-path
  - engineering-practice
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[LLM 主题]]"
  - "[[Agent 主题]]"
  - "[[Agent 知识地图]]"
  - "[[Tool Calling]]"
  - "[[Structured Outputs]]"
  - "[[RAG]]"
  - "[[Evaluation]]"
  - "[[Observability]]"
---

# AI Engineering From Scratch

## 为什么收

AI Engineering From Scratch 是一套从 AI 工程基础到 Agent / production 的开源课程和配套 GitHub 项目。对当前 vault 的学习价值不在于从 Phase 0 顺序刷完整课程，而在于提供一条课程型路线：先补齐 LLM Engineering、工具协议和 Agent Engineering，再按需补 autonomous systems、multi-agent、production infrastructure 和 safety。

这张总入口用于承接课程结构和快速 Agent 开发路线；具体 lesson 已经拆出的本地证据继续放在各自的 source note。

## 一句话

面向快速 Agent 开发时，这门课可以按 `Phase 11 -> Phase 13 -> Phase 14 -> 少量 Phase 15/16/17/18 -> Capstone` 使用，而不是从数学、深度学习、视觉、音频、扩散和从零训练 LLM 全量顺序学习。

## 主源

- Website: <https://aiengineeringfromscratch.com>
- Lesson app: <https://aiengineeringfromscratch.com/lesson.html>
- GitHub repo: <https://github.com/rohitg00/ai-engineering-from-scratch>
- GitHub README checked on 2026-05-24: repo presents the curriculum as 20 phases and 435 lessons, with each lesson producing reusable artifacts such as prompts, skills, agents, or MCP servers.

## 快速 Agent 开发路线

### 1. Phase 11 - LLM Engineering

先补 Agent 应用的 LLM 地基：

- Prompt Engineering
- Structured Outputs
- Context Engineering
- RAG / Advanced RAG
- Function Calling & Tool Use
- Evaluation & Testing
- Caching / Rate Limit / Cost
- Guardrails
- MCP
- Prompt Caching

边界：这一步不是为了研究 LLM 训练，而是让模型调用变成可约束、可评估、可组合的软件接口。Phase 11 已经本地拆出的入口包括 [[AI Engineering From Scratch - Prompt Engineering]]、[[AI Engineering From Scratch - Few-Shot CoT]]、[[AI Engineering From Scratch - Structured Outputs]] 和 [[AI Engineering From Scratch - Embeddings]]。

### 2. Phase 13 - Tools & Protocols

再补工具和协议层：

- Tool Interface
- Function Calling Deep Dive
- Parallel / Streaming Tool Calls
- Tool Schema Design
- MCP Fundamentals / Server / Client / Security
- OpenTelemetry GenAI
- LLM Routing Layer
- Skills and Agent SDKs

边界：Agent 的关键不是“会聊天”，而是能通过 schema、permission、trace 和 protocol 稳定连接外部系统。

### 3. Phase 14 - Agent Engineering

把核心 Agent 系统学扎实：

- Agent Loop
- ReWOO / Plan-and-Execute
- Tool Use and Function Calling
- Memory
- Anthropic Workflow Patterns
- LangGraph
- OpenAI Agents SDK
- Benchmarks
- Observability
- Failure Modes
- Prompt Injection
- Orchestration Patterns
- Eval-Driven Agent Development
- Agent Workbench 系列

边界：Phase 14 是主干。时间紧时，workbench / project-style lessons 往往比抽象论文名更接近实际工作，因为它们会逼迫 loop、tool、state、memory、eval 和 observability 一起落地。

### 4. Selective Phase 15/16/17/18

按生产能力缺口选择性补：

- Phase 15 - Autonomous Systems：Long-Horizon Agents、Durable Execution、Action Budgets、Kill Switches、HITL、Checkpoints / Rollback。
- Phase 16 - Multi-Agent & Swarms：Why Multi-Agent、Supervisor / Worker、Role Specialization、Handoffs、Shared Memory、Production Scaling、Failure Modes。
- Phase 17 - Infrastructure & Production：LLM Observability、Prompt / Semantic Caching、Model Routing、AI Gateways、Canary Deployment、Load Testing、Secrets / PII / Audit Logs、FinOps。
- Phase 18 - Safety：Indirect Prompt Injection、Red-Team Tooling、Moderation Systems、Model / System Cards。

边界：multi-agent 不应作为第一步。多数真实系统先需要 planner / executor / verifier / reviewer 的清晰责任边界，再决定是否扩大成更复杂的多 Agent 编排。

### 5. Capstone

最后用项目闭环检验：

- Terminal-Native Coding Agent
- RAG over Codebase
- GitHub Issue-to-PR Autonomous Agent
- Multi-Agent Software Engineering Team
- MCP Server with Registry and Governance

## 最小实战顺序

1. 用 Phase 11 + Phase 13 做一个 `RAG + tools + structured output + eval` 小应用。
2. 用 Phase 14 做一个 `agent loop + memory + tool calling + verifier`。
3. 用 Phase 15 / Phase 17 补 budget、logging、failure recovery、human-in-the-loop 和 observability。
4. 用 Capstone 把工具权限、trace、eval、部署和回滚一起压进真实项目。

## 暂不优先的部分

- Phase 1-3 数学 / 机器学习 / 深度学习：遇到 embedding、loss、evaluation 或训练问题时再按需补。
- Phase 4 Vision、Phase 6 Audio、Phase 8 Diffusion：除非目标是多模态、语音或图像生成 Agent。
- Phase 9 RL、Phase 10 LLMs from Scratch：对“开发 Agent 应用”不是第一生产力。
- Phase 12 Multimodal：只有在 computer-use、文档理解、视觉 QA 或多模态工具链成为项目需求时再补。

## 证据边界

这张 note 记录的是课程结构带来的学习路线判断，不是课程作者给出的唯一官方学习路径。Phase 编号、lesson 数量、lesson 名称和项目实现可能继续变化；涉及 API、模型、框架、MCP、安全建议和 provider-specific 能力时，需要回到最新官方文档或课程 repo 复查。

课程总数存在版本漂移风险：早前网页和 repo 展示过不同 lesson 数量；2026-05-24 复查 GitHub README 时显示 20 phases / 435 lessons。因此本 vault 不把 lesson 总数当成稳定知识，只把 Phase 11/13/14/15/16/17/18 的能力块作为学习导航。

## 相关本地来源

- [[AI Engineering From Scratch - Prompt Engineering]]
- [[AI Engineering From Scratch - Few-Shot CoT]]
- [[AI Engineering From Scratch - Structured Outputs]]
- [[AI Engineering From Scratch - Embeddings]]
