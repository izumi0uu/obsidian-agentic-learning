---
type: map
topic:
  - query
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-12
related:
  - "[[LLM Wiki 工作流]]"
  - "[[02 问题池]]"
  - "[[04 页面目录]]"
---

# 05 Query 写回队列

这页收集“聊天里已经产生了有用理解，但还没写回 wiki”的内容。

## 使用规则

- 如果回答产生了新定义、新边界、新对比、新操作流程，必须进入这里或直接写进概念卡。
- 每周维护时处理 pending 项。
- 写回后把状态改成 `done`，并链接目标页面。

## 队列

| 日期 | 状态 | 问题 | 应写入 | 处理 |
|---|---|---|---|---|
| 2026-05-07 | done | “我现在这个项目践行了 LLM Wiki 吗？” | [[Obsidian + LLM Wiki]], [[LLM Wiki 工作流]] | 已写回“早期可用版 / 人工监督的 LLM 学习 wiki”边界 |
| 2026-05-07 | done | “$ralplan 底层是在做什么？” | [[Oh My Codex (OMX)]], [[oh-my-codex 使用教程]] | 已写回 prompt routing + state + plan artifact + stop hook |
| 2026-05-08 | done | “现在的 agent 都在使用 ReAct 范式吗？ReAct 的局限现在怎么解决？” | [[ReAct]], [[Agent Loop]], [[Agent Harness]] | 已写回 ReAct 作为行动循环思想、不是所有 Agent 固定模板的边界 |
| 2026-05-08 | done | “现在框架是怎么更好地接管 ReAct / Plan-and-Solve 这类 prompt pattern？” | [[Agent Framework]], [[Agent Harness]], [[Tool Calling]] | 已写回框架接管 prompt loop 的工具、状态、流程、执行、权限、观测六层 |
| 2026-05-09 | done | “现在的 LLM 模型是怎么被训练得越来越强的？” | [[LLM]], [[Evaluation]], [[LLM Training Pipeline]] | 已写回：预训练 scaling、数据质量、SFT、偏好优化/RLHF/RLAIF、推理强化、工具/代码/多模态训练、评测闭环和 Agent 框架兼容性 |
| 2026-05-11 | done | “Deep Agent 是什么？” | [[LangChain DeepAgents]], [[03 前沿追踪]] | 已写回 LangChain / LangGraph `deepagents` 作为具体 SDK / harness；边界区分通用 deep agent 形态和 RUC-NLPIR DeepAgent 论文/项目名 |
| 2026-05-12 | done | “建立概念对比 / 类比 topic 机制，并以 ReAct / Plan-and-Solve / Reflexion 做样板” | [[LLM Wiki 工作流]], [[ReAct Plan-and-Solve Reflexion 对比]], [[概念对比页]] | 已写回准入标准、证据边界、模板、样板页和候选队列 |

## 写回模板

```md
| YYYY-MM-DD | pending | 问题 | `目标页面` | 处理动作 |
```


## 概念对比候选队列

准入规则见 [[LLM Wiki 工作流#概念对比 / 类比 topic 页写法]]。候选只代表“值得排查 / 可能值得写”，不是自动新建页面；执行前仍要确认每个概念有足够证据锚点。

| 优先级 | 状态 | 候选概念组 | 为什么值得对比 | 下一步 |
|---|---|---|---|---|
| P1 | done | [[ReAct]] / [[Plan-and-Solve Prompting]] / [[Reflexion]] | 都改善复杂任务可靠性，但分别介入行动前、行动中、行动后；混淆风险高且 paper source note 充分 | 已写入 [[ReAct Plan-and-Solve Reflexion 对比]] |
| P1 | pending | [[Agent Framework]] / [[Agent Harness]] / [[Agent Workflow]] / [[Agent State]] | 都描述 Agent 工程承载层，但边界分别是框架、运行支架、流程图/步骤和状态数据；容易混成“框架万能” | 先核对四张卡证据，再决定是否新建工程分层对比页 |
| P1 | pending | [[Tool Use]] / [[Tool Calling]] / [[Tool Registry]] / [[Tool Permissioning]] | 都和工具有关，但分别是能力范畴、结构化调用契约、工具发现/注册和权限边界 | 先核对 [[Toolformer]] raw / docs 证据，避免把历史 tool-use 论文和现代 schema 混写 |
| P2 | pending | [[Memory]] / [[Long-term Memory]] / [[Semantic Memory]] / [[Episodic Memory]] / [[Memory Reflection]] | 都是 Agent memory 线索，但分别是总类、长期保存、事实/语义、事件经验和反思生成 | 适合在 memory 主题小批量复查后写对比页 |
| P2 | pending | [[Prompt Injection]] / [[Indirect Prompt Injection]] / [[Tool Poisoning]] / [[Data Exfiltration]] | 都是安全风险，但攻击入口、传播路径和防护边界不同 | 先确认 OWASP / MCP threat-model source anchors 后再写 |
| P2 | existing | [[Trajectory]] / [[Trace]] / [[Reasoning Trace]] / [[Trajectory Evaluation]] / [[Replay]] | 已有高价值边界页，说明 trajectory、trace 和 reasoning trace 的层级差异 | 见 [[Trajectory Trace 类型对比]]；后续只做维护 |
| P2 | existing | [[RAG]] / [[Agentic RAG]] / [[Corrective RAG]] / [[Self-RAG]] | 已有 RAG 类型比较入口，适合继续补 evidence / modernity | 见 [[RAG 类型对比]]；后续只做维护 |
