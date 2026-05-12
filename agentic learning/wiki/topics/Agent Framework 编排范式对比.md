---
type: map
topic:
  - agent
  - framework
  - multi-agent
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[AutoGen]]"
  - "[[AgentScope]]"
  - "[[CAMEL]]"
  - "[[LangGraph]]"
  - "[[Microsoft Agent Framework]]"
  - "[[LangChain DeepAgents]]"
  - "[[AutoGen 官方文档]]"
  - "[[AgentScope 官方文档]]"
  - "[[CAMEL-AI 官方文档]]"
  - "[[LangGraph 官方文档]]"
  - "[[Microsoft Agent Framework 官方文档]]"
evidence:
  - "[[AutoGen 官方文档#必读块 1：Teams / group chat 抽象]]"
  - "[[AgentScope 官方文档#必读块 1：AgentScope 的平台定位]]"
  - "[[CAMEL-AI 官方文档#必读块 1：Role-playing / inception prompting]]"
  - "[[LangGraph 官方文档#一句话]]"
  - "[[Microsoft Agent Framework 官方文档#必读块 1：Agent vs workflow 边界]]"
  - "[[LangChain DeepAgents#概念详解]]"
related:
  - "[[Agent Framework]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
  - "[[Agent 工程分层对比]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Handoff]]"
---

# Agent Framework 编排范式对比

## 一句话总览

这些框架都在帮开发者构建 Agent，但抽象中心不同：[[AutoGen]] 从 conversation team 进入，[[CAMEL]] 从 role-playing / inception prompting 进入，[[AgentScope]] 从 message-centered application platform 进入，[[LangGraph]] 从 state graph runtime 进入，[[Microsoft Agent Framework]] 从微软 agent + workflow 统一 SDK 进入，[[LangChain DeepAgents]] 则是在 LangGraph 上封装长任务 harness。

最小边界：不要问“哪个最强”，先问“它把复杂性放在哪一层”：消息、角色、图状态、平台生命周期、企业 SDK，还是长任务脚手架。

## 为什么这组值得对比

- 混淆风险高：它们都可被叫作 Agent Framework / Multi-Agent Framework，但具体抽象中心不同。
- 共同问题域相近：都在把 LLM 从单轮调用扩展成能协作、调用工具、保持状态或执行长任务的系统。
- 不同介入点明显：conversation、role-playing、message platform、state graph、agent/workflow SDK、harness template 分别接管不同工程责任。
- 证据密度足够：本页每个主对象都有 concept card 或 raw official docs/source note 锚点。
- 现代工程价值高：框架选型错误会直接影响 state、permission、observability、deployment、migration 和团队长期维护成本。

边界：这页不是选型排行榜，也不评判哪个生态更“先进”；它训练的是框架范式辨析。更大范围的 13 框架选型比较见 [[Agent Framework 全量选型对比 2026-05]]。

## 共同问题域

共同问题可以概括为：LLM 应用从“单次模型调用”升级到“能执行任务的 Agent 系统”后，开发者必须处理多轮状态、工具、副作用、角色分工、协作消息、停止条件、人工确认、观测和部署。不同框架给这些问题的第一抽象不同。

```text
single LLM call
  -> agent with tools
  -> multi-step workflow / loop
  -> multi-agent collaboration
  -> state / memory / trace / eval
  -> deployment / enterprise governance
```

这些框架值得放在一起比较，是因为它们都在接管这条路径上的某些责任；但它们不是同一层的替代品。比如 [[LangGraph]] 可以作为底层 runtime，[[LangChain DeepAgents]] 可以作为其上的 harness；[[AutoGen]] 的 group chat 范式和 [[Microsoft Agent Framework]] 的继任路线也不能简单等同。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[AutoGen]] | conversation-first team / group chat 编排 | agent 轮流发言、选择 speaker、handoff、termination | 角色 agent、工具、team preset、任务目标 | 自动消息轨迹、协作结果、handoff / stop | [[AutoGen 官方文档#必读块 1：Teams / group chat 抽象]] |
| [[CAMEL]] | role-playing / inception prompting | 会话开始前注入角色与任务，多轮 communicative agents 协作 | 角色设定、共同任务、初始提示、互动约束 | role-playing 对话轨迹、任务结果、agent society 数据 | [[CAMEL-AI 官方文档#必读块 1：Role-playing / inception prompting]] |
| [[AgentScope]] | message-centered multi-agent platform | agent / user / tool 通过 Msg 交换，平台管理编排、部署、观测 | agent 定义、messages、tools、memory、deployment 配置 | 多 Agent 应用、消息流、观测/部署产物 | [[AgentScope 官方文档#必读块 1：AgentScope 的平台定位]] |
| [[LangGraph]] | state graph orchestration runtime | 节点执行、状态更新、边路由、循环、checkpoint / resume | state schema、nodes、edges、tools、approval/eval 节点 | 可恢复 workflow、state trace、human-in-the-loop 路径 | [[LangGraph 官方文档#一句话]] |
| [[Microsoft Agent Framework]] | Microsoft agent + workflow 统一 SDK / 继任路线 | 先判断 function / workflow / agent，再用 SDK 对象组织执行 | agent 或 workflow 定义、tools、middleware、telemetry、Azure/企业集成 | agent app / workflow、trace、middleware、迁移路径 | [[Microsoft Agent Framework 官方文档#必读块 1：Agent vs workflow 边界]] |
| [[LangChain DeepAgents]] | built on LangGraph 的长任务 Agent harness | planning、filesystem、subagents、memory、permissions 包成默认脚手架 | 任务、系统指令、tools、subagents、memory、filesystem | 长任务执行 harness、计划/文件/子任务/权限轨迹 | [[LangChain DeepAgents#概念详解]] |

## 最容易混淆的边界

### AutoGen vs CAMEL

[[AutoGen]] 更偏 team / group chat orchestration：哪些 agent 参与、谁发言、如何 handoff、什么时候终止。[[CAMEL]] 的地基更偏 role-playing / inception prompting：如何通过初始提示设定角色、任务和约束，让 communicative agents 协作。

一句话：AutoGen 先问“这组 agent 如何轮流协作”；CAMEL 先问“这些角色如何被设定成能协作”。

### LangGraph vs LangChain DeepAgents

[[LangGraph]] 是底层 state graph runtime；[[LangChain DeepAgents]] 是建立在 LangGraph 上的长任务 harness。前者让你直接设计 nodes / edges / state / checkpoint；后者把 planning、filesystem、subagents、memory、permissions 等常见结构预先包好。

一句话：LangGraph 是“自己搭图”；DeepAgents 是“用 LangGraph 上层模板跑长任务”。

### AutoGen vs Microsoft Agent Framework

[[AutoGen]] 是微软多 Agent conversation patterns 的重要历史路线；[[Microsoft Agent Framework]] 是官方当前强调的 AutoGen + Semantic Kernel 整合/继任框架。不要把 AutoGen 的 group chat 概念直接等同于 MAF 的 agent + workflow SDK。

### AgentScope vs LangGraph

[[AgentScope]] 更像多 Agent application platform，强调 message、orchestration、observability、deployment 和分布式运行。[[LangGraph]] 更像低层 state graph runtime，强调节点、边、状态和 durable execution。二者都能“编排”，但一个偏平台生命周期，一个偏状态图控制。

### Microsoft Agent Framework vs LangGraph

两者都重视 workflow，但 [[Microsoft Agent Framework]] 强调微软生态里的 agent / workflow 统一 SDK、Semantic Kernel / AutoGen 迁移和企业集成；[[LangGraph]] 强调 LangChain 生态里的 state graph orchestration runtime。

## 执行时序 / 机制差异

```text
CAMEL:
Role/task inception prompt -> Agent A/B role-playing turns -> task result / society trace

AutoGen:
Team config -> speaker selection / group chat -> handoff or termination -> result

AgentScope:
Agent definitions -> Msg exchange -> orchestration / tools / memory -> deploy / observe

LangGraph:
State -> Node -> Edge routing -> State update -> checkpoint / HITL / loop -> end

Microsoft Agent Framework:
Choose function vs workflow vs agent -> define SDK objects -> middleware / telemetry / workflow state -> run

LangChain DeepAgents:
Task -> planning/todo -> filesystem/subagents/tools/memory -> LangGraph runtime -> result
```

这组机制差异说明：框架不只是 API 包名不同，而是“谁负责下一步”和“状态在哪里”的答案不同。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

把框架想成不同类型的项目管理方式：

| 框架 | 类比 | 类比边界 |
|---|---|---|
| [[CAMEL]] | 先给两位专家写清角色卡和共同任务，让他们按角色对话 | 角色卡不能替代工具执行和评测 |
| [[AutoGen]] | 组织一个自动会议，有主持规则、发言顺序和停止条件 | 会议热闹不等于结果可靠 |
| [[AgentScope]] | 搭一个项目管理平台，消息、成员、工具、部署和看板都在里面 | 平台不自动保证业务决策正确 |
| [[LangGraph]] | 画一张状态机流程图，每一步产出写回 state | 流程图不自动写出正确节点逻辑 |
| [[Microsoft Agent Framework]] | 企业统一开发套件，先决定用函数、流程还是 agent | 生态整合不等于无迁移成本 |
| [[LangChain DeepAgents]] | 长任务脚手架模板，预装 todo、文件系统、子任务和权限中断 | 模板不等于底层 runtime 本身 |

## 现代系统如何吸收或限制

### 来源支持

- [[AutoGen 官方文档]] 支持 team / group chat preset、speaker selection、handoff 和 termination 这些 conversation-first 控制点。
- [[CAMEL-AI 官方文档]] 支持 role-playing / inception prompting 的论文地基和现代 CAMEL-AI 框架模块。
- [[AgentScope 官方文档]] 支持 message-centered platform、tools、memory、observability、deployment 和 distributed mode 边界。
- [[LangGraph 官方文档]] 支持 state graph、node/edge/state、durable execution、human-in-the-loop 和 runtime 分层。
- [[Microsoft Agent Framework 官方文档]] 支持 agent vs workflow 边界以及 AutoGen + Semantic Kernel 继任/整合路线。
- [[LangChain DeepAgents]] 支持 DeepAgents 是 built on LangGraph 的长任务 harness，而不是 LangGraph 本身。

### 工程综合 / inference

现代生产系统常常不是“选一个框架一把梭”，而是组合层次：state graph runtime 负责可恢复流程，harness 封装长任务常用部件，conversation/team pattern 处理协作，platform 处理部署观测，enterprise SDK 处理组织内集成。对比这些框架时，最重要的是看它接管哪层责任，而不是看 demo 中 agent 数量。

### 仍需警惕的外推

- 这些框架都处于快速演进生态，API、推荐路线、迁移指南和产品定位会变。
- Microsoft Agent Framework 当前官方文档仍有 preview/继任路线相关边界，不能把它写成已固定的长期标准。
- CAMEL paper 的 role-playing 结论不能自动证明现代 CAMEL-AI 每个模块的生产成熟度。
- AgentScope 的平台能力需要按版本和部署目标验证，不应只凭功能列表判断。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 想理解“多个角色如何自动对话协作” | [[AutoGen]] / [[CAMEL]] | 一个强调 team/group chat，一个强调 role-playing/inception prompting | 容易把对话轨迹误当可靠执行 |
| 想把流程变成可恢复、可审计的状态图 | [[LangGraph]] | state、node、edge、checkpoint 是核心抽象 | 图复杂度和状态 schema 仍需治理 |
| 想构建多 Agent 应用平台、服务化和观测部署 | [[AgentScope]] | message、orchestration、observability、deployment 是平台能力 | 平台能力不自动解决业务 eval |
| 在微软生态选 Agent 框架或从 AutoGen/Semantic Kernel 迁移 | [[Microsoft Agent Framework]] | 官方继任路线和 agent/workflow SDK 是关键 | preview/GA、API 和迁移成本需复查 |
| 想快速搭长任务 Agent，复用 planning/filesystem/subagents/memory/permissions | [[LangChain DeepAgents]] | 它把 LangGraph 上的常见长任务 harness 结构预装好 | 不要把 harness 当底层 runtime 或通用标准 |
| 任务简单、步骤固定、普通函数能解决 | 先不用这些框架 | framework 会增加延迟、成本和调试面 | “为了 Agent 而 Agent” |

## 它们共同不是什么

- 都不是基础模型，也不直接提升模型权重能力。
- 都不是完整安全保证；仍需要权限、沙箱、approval、trace、eval 和数据治理。
- 都不是同一层的直接替代品；有的是 runtime，有的是 harness，有的是 platform，有的是 conversation pattern。
- 都不应该替代需求澄清。框架越强，越容易掩盖“任务到底是 function、workflow 还是 agent”的基本问题。

## 证据锚点

- Concept anchors: [[AutoGen#证据锚点]], [[AgentScope#证据锚点]], [[CAMEL#证据锚点]], [[LangGraph#证据锚点]], [[Microsoft Agent Framework#证据锚点]], [[LangChain DeepAgents#证据锚点]]。
- Source anchors: [[AutoGen 官方文档]], [[AgentScope 官方文档]], [[CAMEL-AI 官方文档]], [[LangGraph 官方文档]], [[Microsoft Agent Framework 官方文档]], [[LangChain Deep Agents 官方文档]]。
- Evidence type: official docs/source notes + paper/source-note synthesis + engineering synthesis + learning analogy.
- Confidence: medium-high for framework abstraction centers; medium for product roadmap and API specifics because all relevant ecosystems are volatile.
- Boundary: 本页比较的是“编排范式和责任层”，不是框架性能、社区热度、最新 API 或生产可用性排名。

## 复习触发

1. 如果一个框架说自己支持多 Agent，你先问哪三个问题来判断它的抽象中心？
2. AutoGen 和 CAMEL 都是对话式多 Agent，为什么一个更像 team orchestration，一个更像 role-playing prompting？
3. LangGraph 和 DeepAgents 哪个是 runtime，哪个是 harness？错把两者等同会导致什么选型错误？
4. 为什么 Microsoft Agent Framework 的重要性不在“又一个框架”，而在 AutoGen + Semantic Kernel 的整合/继任路线？
5. 给一个医疗或金融 Agent 场景：哪些部分应该固定成 workflow，哪些部分才允许 agent 自主决策？

## 相关链接

- [[Agent Framework]]
- [[Agent Framework 全量选型对比 2026-05]]
- [[Agent 工程分层对比]]
- [[AutoGen]]
- [[AgentScope]]
- [[CAMEL]]
- [[LangGraph]]
- [[Microsoft Agent Framework]]
- [[LangChain DeepAgents]]
- [[Multi-agent Orchestration]]
- [[Agent Workflow]]
- [[Agent State]]
- [[Handoff]]
- [[Trace]]
- [[Evaluation]]
