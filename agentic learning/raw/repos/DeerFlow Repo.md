---
type: source
source_type: repo
title: bytedance/deer-flow
url: https://github.com/bytedance/deer-flow
author: ByteDance
site: github.com
topic:
  - agent
  - harness
  - workflow
  - memory
  - sandbox
  - frontier
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: volatile
conflicts:
  - DeerFlow 1.x 偏 Deep Research framework；2.0 README 明确为 ground-up rewrite，当前卡片以 2.0 super agent harness 为准。
status: seed
source:
  - https://github.com/bytedance/deer-flow
  - https://deerflow.tech/
related:
  - "[[DeerFlow]]"
  - "[[Agent Harness]]"
  - "[[Agent Framework]]"
  - "[[LangChain DeepAgents]]"
  - "[[LangGraph]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Sandbox Workspace]]"
  - "[[Context Engineering]]"
  - "[[Long-term Memory]]"
---

# DeerFlow Repo

## 为什么收

DeerFlow 是 ByteDance 开源的 super agent harness。它适合进入这个 vault，是因为它把 sub-agents、memory、sandbox、skills、filesystem、IM channels、tracing 和 LangGraph/LangChain runtime 组合成一个长任务 Agent 运行底座。

这份 source 主要用于观察“deep research 项目如何演进成更通用的 Agent harness”：项目不只回答研究问题，还试图承载报告、幻灯片、网页、数据分析、代码和多步骤内容工作流。

## 主源

- GitHub repo: <https://github.com/bytedance/deer-flow>
- Official website: <https://deerflow.tech/>
- README checked on 2026-05-18: project describes DeerFlow 2.0 as an open-source super agent harness that orchestrates sub-agents, memory, sandboxes and extensible skills.

## 一句话

DeerFlow 是一个面向长任务的 Agent harness：它把 lead agent、sub-agents、skills、filesystem、sandbox、memory、context compression、IM gateway 和 tracing 组织成可运行的 Agent 产品底座。

## 关键事实

- README 把 DeerFlow 解释为 Deep Exploration and Efficient Research Flow，并将 2.0 定位为 open-source super agent harness。
- README 明确说明 2.0 是 ground-up rewrite，与 1.x 没有共享代码；原 Deep Research framework 留在 `1.x` branch。
- From Deep Research to Super Agent Harness 一节说明：DeerFlow 2.0 不再只是 research framework，而是 built on LangGraph and LangChain 的 batteries-included harness。
- Core features 包括 skills & tools、sub-agents、sandbox & file system、context engineering、long-term memory。
- Sub-agents 由 lead agent 按需生成，每个有 scoped context、tools 和 termination condition，可并行执行后汇总。
- Sandbox & File System 说明每个任务有自己的 execution environment、filesystem、uploads、workspace、outputs；支持 Docker / Kubernetes 风格隔离，也保留 trusted local 模式。
- Context Engineering 强调 isolated sub-agent context、summarization、filesystem offloading 和 tool-call recovery。
- Long-Term Memory 强调跨会话保存 profile、preferences 和 accumulated knowledge，但这属于产品实现，需要定期复查。
- Security Notice 明确提醒：DeerFlow 具备 system command execution、resource operations 和 business logic invocation 等高权限能力，默认应部署在 local trusted environment。

## 可以拆成概念卡

- [[DeerFlow]]
- [[Agent Harness]]
- [[Multi-agent Orchestration]]
- [[Sandbox Workspace]]
- [[Context Engineering]]
- [[Long-term Memory]]
- [[LangGraph]]
- [[LangChain DeepAgents]]

## 学习时先看

1. 先读 README 顶部定位和 From Deep Research to Super Agent Harness，确认 2.0 边界。
2. 再读 Core Features，把 skills、sub-agents、sandbox、context engineering、memory 拆成 harness 组成部分。
3. 再读 Quick Start / Configuration / Security Notice，理解运行环境、部署边界和权限风险。
4. 最后看 backend docs / architecture，只在需要研究具体实现时深入。

## 边界提醒

DeerFlow 不是 [[RAG]] 框架，也不是知识库问答平台。它可以用搜索、爬取、文件和记忆，但中心问题是“Agent 如何持续执行复杂任务”，不是“文档如何入库并被检索”。

DeerFlow 也不是 [[LangGraph]] 本身。README 说它 built on LangGraph and LangChain；LangGraph 更底层，DeerFlow 是上层 harness / product runtime。

不要把 DeerFlow 2.0 直接等同于 Deep Research。1.x 的历史语境重要，但 2.0 官方定位已经扩大为 super agent harness。

## 证据锚点候选

- `README.md`：项目定位、2.0 rewrite、From Deep Research to Super Agent Harness、Core Features、Security Notice。
- `backend/docs/CONFIGURATION.md`：sandbox / MCP / provider / runtime config。
- `backend/README.md` / `backend/CLAUDE.md`：需要看实现架构时再读。
- Official website：演示和产品定位，作为 README 的补充。

## 我的疑问

- DeerFlow 的 sub-agent 并行和 context summarization 如何在长任务里避免 evidence loss？
- 它的 skills 体系和 Claude/Codex skill 概念有哪些兼容点，哪些只是同名不同边界？
- 在 public deployment 中，sandbox、authentication gateway、IP allowlist 和 artifact download policy 如何共同控制副作用风险？
