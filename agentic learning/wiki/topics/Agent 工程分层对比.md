---
type: map
topic:
  - agent
  - framework
  - workflow
  - infrastructure
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Agent Framework]]"
  - "[[Agent Harness]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Agent Loop]]"
  - "[[Agent 工程基础设施主源]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Agent Framework#框架怎样接管 prompt loop]]"
  - "[[Agent Framework#现代系统怎么吸收 Agent Framework 的价值 / 局限]]"
  - "[[Agent Harness#生命周期 hook 如何增强 Harness]]"
  - "[[Agent Workflow#证据锚点]]"
  - "[[Agent State#证据锚点]]"
  - "[[Agent Loop#证据锚点]]"
related:
  - "[[Agent 主题]]"
  - "[[Agent Framework]]"
  - "[[Agent Harness]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
  - "[[Durable Execution]]"
---

# Agent 工程分层对比

## 一句话总览

这页把 [[Agent Framework]]、[[Agent Harness]]、[[Agent Workflow]]、[[Agent State]] 和 [[Agent Loop]] 切成五个工程层次：framework 是开发抽象工具箱，harness 是让 Agent 真正运行并受控的外壳，workflow 是任务路径，state 是当前运行事实，loop 是行动后根据 [[Observation]] 继续决策的反馈循环。

最小边界：framework 负责“用什么搭”；harness 负责“在哪里安全地跑”；workflow 负责“按什么路径跑”；state 负责“跑到哪里了”；loop 负责“看到反馈后下一步怎么变”。

## 为什么这组值得对比

- 混淆风险高：工程讨论里常把 framework、harness、workflow、state、loop 都简称成“Agent 框架能力”。
- 共同问题域清楚：它们都在把脆弱的 prompt loop 变成可运行、可恢复、可观测、可评估的系统。
- 不同介入点明显：有的提供软件抽象，有的定义运行边界，有的组织流程，有的保存运行事实，有的描述反馈循环。
- 证据密度足够：五张概念卡都有 `## 证据锚点`，并回到 Agent 工程主源、Anthropic / OpenAI 实践材料、LangGraph 和 OpenAI Agents SDK source note。
- 复习价值高：如果分不清这些层，就容易把“选框架”“写 workflow”“加状态”“跑测试/trace”“做安全边界”混成同一个动作。

边界：这页不是框架选型指南，也不评价具体 SDK 优劣；它只训练工程责任分层。

## 共同问题域

共同问题是：真实 Agent 不能只靠模型在 prompt 里自觉遵守格式、记住进度、判断权限、处理失败并声明完成。现代系统会把这些责任拆到 runtime、workflow、state、trace、eval 和 human-in-the-loop 里。

```text
model intention
  -> loop decides next action from current state / observation
  -> workflow constrains allowed path and handoff / approval
  -> framework provides agent/tool/state/workflow abstractions
  -> harness executes inside sandbox / permissions / trace / eval boundary
  -> state records progress, errors, approvals and next-step basis
```

这组概念适合一起学，是因为它们回答的是同一条工程化路径上的不同问题，而不是互相替代的名词。

## 核心区别表

| 概念 | 主要介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Agent Framework]] | 开发抽象和编排工具箱 | 设计和运行前后都参与：定义 agent、tools、state、workflow、handoff、trace | 任务需求、模型配置、工具、状态结构、流程设计 | 可复用 Agent 工程抽象和运行入口 | [[Agent Framework#框架怎样接管 prompt loop]] |
| [[Agent Harness]] | 运行外壳、权限、沙箱、trace、评测和停止边界 | 运行时包住模型动作，把意图变成可控执行事件 | 用户目标、工作区、工具权限、测试/评测协议、hook | patch、工具结果、trace、评测结果、阻断或完成状态 | [[Agent Harness#生命周期 hook 如何增强 Harness]] |
| [[Agent Workflow]] | 任务路径、节点、分支、循环、approval、handoff | 运行路径层：决定哪些步骤固定、哪些节点交给模型判断 | 输入、路由规则、状态、审批条件、异常分支 | 可执行流程、下一节点、交接或停止 | [[Agent Workflow#证据锚点]] |
| [[Agent State]] | 当前 run 的结构化运行事实 | 每轮 loop 前后被读写；可 checkpoint / resume | 目标、阶段、工具结果、错误、审批状态、中间产物 | 下一步依据、恢复点、可注入上下文的状态片段 | [[Agent State#证据锚点]] |
| [[Agent Loop]] | 行动反馈循环 | 贯穿执行：observe / decide / act / observe / stop | 目标、当前 state、上下文、上一步 observation | 下一步 action、停止判断、状态更新需求 | [[Agent Loop#证据锚点]] |

## 最容易混淆的边界

- [[Agent Framework]] vs [[Agent Harness]]：framework 偏“开发者用什么抽象搭系统”；harness 偏“这个系统在什么边界里安全、可复现、可评测地运行”。一个 SDK 可能同时提供两者的一部分，但学习时要分开责任。
- [[Agent Framework]] vs [[Agent Workflow]]：framework 是工具箱；workflow 是用工具箱搭出的任务路径。选了框架，不等于 workflow 已经设计好。
- [[Agent Workflow]] vs [[Agent Loop]]：workflow 组织多个步骤、分支、审批和交接；loop 强调每次 action 后 observation 影响下一步。一个 workflow 可以包含多个 loop，也可以大部分是固定流程。
- [[Agent State]] vs context window：state 是 runtime 保存的结构化事实；context window 只是某次模型调用能看到的投影。把全部历史都塞给模型不是好的 state 设计。
- [[Agent Harness]] vs [[Evaluation]]：harness 可以运行测试和收集证据，但 evaluation 是对结果或 trajectory 的判断层；运行壳不自动保证评分标准正确。
- [[Agent Loop]] vs 多轮聊天：只有 action、observation 和状态更新形成闭环，才接近 Agent Loop；单纯让模型多说几轮不是工程闭环。

## 执行时序 / 机制差异

```text
1. 设计期：Agent Framework 提供 agent / tool / state / workflow / tracing 等抽象。
2. 编排期：Agent Workflow 把任务拆成固定节点、动态节点、审批节点和交接节点。
3. 运行期：Agent Harness 准备工作区、权限、沙箱、hook、trace、eval 和停止条件。
4. 每轮执行：Agent Loop 读取目标 + 必要 state，产生 action 或停止判断。
5. 工具 / 环境返回 Observation，runtime 把结果写回 Agent State，并记录 Trace。
6. 如果任务中断或需要等待，State / checkpoint / Durable Execution 支持恢复。
7. Evaluation / human review 判断是否完成、失败、回滚或继续。
```

这个机制说明：framework、workflow、state、loop 和 harness 不是线性替代关系，而是嵌套关系。一个失败的 Agent 可能不是“模型不聪明”，而是 workflow 没有异常分支、state 没保存 observation、harness 没跑验证或 framework 抽象使用过度。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

把一次复杂任务想成“拍一部电影”：

| Agent 工程概念 | 类比 | 类比边界 |
|---|---|---|
| [[Agent Framework]] | 摄影棚和制作工具箱：摄影机、灯光、剪辑软件、协作系统 | 工具箱本身不决定电影质量 |
| [[Agent Harness]] | 片场管理：安全规则、预算、场地、日志、验收标准 | 运行边界不是创作灵感来源 |
| [[Agent Workflow]] | 拍摄流程：分镜、场次、审批、补拍、交接 | 流程可包含临场调整，但不等于演员即兴本身 |
| [[Agent State]] | 场记板和进度表：拍到哪、哪里 NG、下一场是什么 | 记录事实，不等于长期影史知识 |
| [[Agent Loop]] | 每拍一条后看回放再调整下一条 | 回放反馈要进入下一步才构成闭环 |

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[Agent Framework]] 和相关 source note 支持：现代框架把 agent、tools、state、workflow、handoff、guardrails 和 tracing 做成显式工程对象。
- [[Agent Workflow]] 支持：很多任务不需要最大自主性，而需要可控步骤、分支、循环和审批。
- [[Agent State]] 支持：当前任务进度、工具结果、错误和审批状态需要结构化保存，而不只是放在上下文窗口。
- [[Agent Loop]] 支持：action 后的 observation 会改变下一轮决策；现代系统通常用 runtime、tool calling、state 和 trace 承载这个循环。
- [[Agent Harness]] 支持：工具执行、沙箱、hook、trace、测试和评测让“模型说完成”变成可验证事件。

### 工程综合 / inference

现代 Agent 系统通常把“自由 loop”压进多层边界：framework 降低工程样板，workflow 限制任务路径，state 保持恢复能力，harness 管住权限和证据，evaluation 判断是否值得继续。这个分层是基于多张概念卡和 source note 的工程综合，不是任一单篇文档逐字给出的标准架构。

### 仍需警惕的外推

具体框架 API、state schema、checkpoint store、trace 字段、approval gate 和 SDK 名称都属于易变实现层。学习时应该记住责任分层，不要把某个产品的对象名当成长期概念边界。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 讨论“我们该用 LangGraph、Agents SDK 还是自研” | [[Agent Framework]] | 这是开发抽象和生态选型问题 | 不要把选框架误认为完成运行治理 |
| 讨论“模型能不能改文件、联网、跑测试、越权写入” | [[Agent Harness]] | 这是运行边界、权限、沙箱和 evidence 问题 | 没有 harness 时高能力模型会放大副作用 |
| 讨论“哪些步骤固定，哪些步骤交给模型判断” | [[Agent Workflow]] | 这是任务路径和控制粒度问题 | workflow 过窄会卡异常，过宽会失控 |
| 讨论“中断后从哪里恢复、哪些工具结果已看过” | [[Agent State]] | 这是当前 run 的结构化事实和 checkpoint 问题 | 把 state 当 memory 会污染长期知识 |
| 讨论“下一步是否应根据测试/网页/工具返回调整” | [[Agent Loop]] | 这是 observation 是否回流决策的问题 | 多轮聊天不等于真实闭环 |
| 讨论“最终是否完成、过程是否安全经济” | [[Evaluation]] / [[Trace]] | 分层概念提供证据，评价层判断好坏 | trace 记录事实，不自动给质量结论 |

## 它们共同不是什么

- 都不是模型权重、模型真实内心或“智能来源”本身。
- 都不是单独的生产可靠性保证；还需要权限、数据治理、测试、eval、observability 和 human-in-the-loop。
- 都不是完整产品边界。一个 coding agent 产品可能同时包含 framework、harness、UI、计费、团队权限、审计和部署策略。
- 都不应该替代任务需求澄清。分层越清楚，越能暴露“到底是 workflow 缺口、state 缺口、harness 缺口，还是 eval 缺口”。

## 证据锚点

- Concept anchors: [[Agent Framework#证据锚点]], [[Agent Harness#证据锚点]], [[Agent Workflow#证据锚点]], [[Agent State#证据锚点]], [[Agent Loop#证据锚点]]。
- Source examples: [[Agent 工程基础设施主源]], [[Anthropic - Building Effective Agents]], [[OpenAI - A Practical Guide to Building Agents]], [[LangGraph 官方文档]], [[OpenAI Agents SDK 文档]]。
- Direct working anchors: [[Agent Framework#框架怎样接管 prompt loop]], [[Agent Framework#现代系统怎么吸收 Agent Framework 的价值 / 局限]], [[Agent Harness#生命周期 hook 如何增强 Harness]], [[Agent State#现代系统怎么吸收 Agent State 的价值 / 局限]], [[Agent Loop#现代系统怎么吸收 Agent Loop 的价值 / 局限]]。
- Evidence type: concept-card synthesis + official/practice source notes + engineering synthesis + learning analogy.
- Confidence: medium-high for responsibility boundaries; medium for modern stack layering because具体框架实现会变化。
- Boundary: 本页不新增 raw 事实，不声称某个 SDK 的最新 API；学习类比只帮助记忆，不作为证据。

## 复习触发

1. 一个 Agent 能调用工具但每次重启都忘记进度：这是 framework、harness、workflow、state 还是 loop 缺口？为什么？
2. 为什么“用了 Agent Framework”不等于“有好的 Agent Harness”？
3. 如果测试失败日志没有进入下一轮决策，这个系统缺的是 loop 还是 evaluation？
4. 设计一个三步任务，标出 workflow、state、loop、harness 分别在哪里出现。
5. 举一个反例，说明什么时候固定 workflow 比开放式 Agent Loop 更可靠。

## 相关链接

- [[Agent 主题]]
- [[Agent Framework]]
- [[Agent Harness]]
- [[Agent Workflow]]
- [[Agent State]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[Observation]]
- [[Trace]]
- [[Evaluation]]
- [[Durable Execution]]
- [[Handoff]]
