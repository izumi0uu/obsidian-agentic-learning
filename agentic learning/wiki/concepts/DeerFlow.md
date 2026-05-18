---
type: concept
topic:
  - agent
  - harness
  - framework
  - workflow
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: volatile
aliases:
  - deer-flow
  - Deep Exploration and Efficient Research Flow
source:
  - "[[DeerFlow Repo]]"
evidence:
  - "[[DeerFlow Repo#一句话]]"
  - "[[DeerFlow Repo#关键事实]]"
  - "[[DeerFlow Repo#边界提醒]]"
related:
  - "[[Agent Harness]]"
  - "[[Agent Framework]]"
  - "[[LangChain DeepAgents]]"
  - "[[LangGraph]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Sandbox Workspace]]"
  - "[[Context Engineering]]"
  - "[[Long-term Memory]]"
  - "[[Tool Permissioning]]"
relations:
  - type: concrete-harness-for
    target: "[[Agent Harness]]"
  - type: built-on
    target: "[[LangGraph]]"
---

# DeerFlow

## 一句话

DeerFlow 是 ByteDance 开源的 super agent harness：它在 LangGraph / LangChain 之上，把 lead agent、sub-agents、skills、sandbox、filesystem、memory、context compression 和 messaging gateway 组合成长任务 Agent 运行底座。

## 概念详解

DeerFlow 的关键边界在于它不是单个 prompting 方法，也不是普通 RAG 平台，而是一个让 Agent 持续执行复杂任务的 harness。官方 README 说 DeerFlow 2.0 是 open-source super agent harness，可以编排 sub-agents、memory 和 sandboxes，并通过 extensible skills 扩展能力。这里的核心词是 harness：它给 Agent 准备工作区、工具、文件系统、沙箱、记忆、上下文压缩、子任务分派和结果汇总。

它的历史边界也很重要。DeerFlow 1.x 更偏 Deep Research framework；2.0 README 明确说是 ground-up rewrite，不和 v1 共享代码，活跃开发已经移到 2.0。From Deep Research to Super Agent Harness 一节解释了这个转向：社区把它用于数据管道、幻灯片、dashboard、内容工作流等研究之外的任务，因此 2.0 被重建为 batteries-included harness。

从工程分层看，DeerFlow built on LangGraph and LangChain。[[LangGraph]] 更像底层 state graph runtime，LangChain 提供模型和工具生态；DeerFlow 在上层预装 lead agent、sub-agents、skills、sandbox-aware execution、filesystem、memory 和 UI/API/gateway。这个结构和 [[LangChain DeepAgents]] 相邻：两者都体现“长任务 Agent 需要 harness”，但 DeerFlow 更像完整产品化 runtime，DeepAgents 更像 LangChain 生态里的 SDK / harness 模板。

DeerFlow 的学习价值在于看到一个长任务 Agent 系统如何把“模型想做事”变成“在受控环境里做事”。Sub-agents 有自己的 scoped context、tools 和 termination conditions；sandbox 给每个任务 uploads、workspace、outputs；context engineering 通过 summarization 和 filesystem offloading 控制上下文；long-term memory 跨会话保存偏好和知识；security notice 明确提醒系统命令、资源操作和业务调用带来的部署风险。

## 它解决什么问题

- 长任务不能只靠聊天上下文推进：需要文件系统、计划、子任务、状态保存和中间产物。
- 单个 Agent 上下文容易膨胀：需要 sub-agent 隔离、摘要、文件系统 offloading 和结果汇总。
- 工具执行有真实副作用：需要 sandbox、权限配置、trusted deployment 和安全边界。
- 研究、报告、网页、幻灯片、数据分析等任务需要技能化工作流：需要按需加载 skill，而不是把所有流程塞进 prompt。

## 它不是什么

DeerFlow 不是 [[RAGFlow]]。RAGFlow 的中心是 RAG / 知识库 / context layer；DeerFlow 的中心是长任务 Agent harness。

DeerFlow 不是 [[RAG]] 框架。它可以使用搜索、爬取、文件和记忆，但它的第一问题不是文档入库和检索质量，而是 Agent 如何计划、分派、执行、压缩上下文和生成交付物。

DeerFlow 也不是 [[LangGraph]] 本身。它建在 LangGraph / LangChain 之上，提供更上层的 runtime、skills、sandbox、memory 和产品入口。

DeerFlow 2.0 也不能简单等同 Deep Research。Deep Research 是历史来源和重要用例；2.0 的官方定位已经扩大到 super agent harness。

## 最小例子

```text
用户要求：研究一个市场并生成报告
-> lead agent 规划任务
-> 按主题 spawn 多个 sub-agents
-> sub-agents 在隔离 context 中搜索、抓取、写文件
-> sandbox workspace 保存 uploads / workspace / outputs
-> lead agent 汇总证据并生成报告
-> trace / memory / artifacts 留下可复查结果
```

这个例子说明 DeerFlow 的中心不是单轮回答，而是多步任务执行和交付物生成。

## 常见误解 / 风险

- 误解：DeerFlow 是 Deep Research 的同义词。更准确地说：1.x 是 Deep Research 语境，2.0 是更宽的 super agent harness。
- 误解：有 sub-agents 就更可靠。子 Agent 会增加上下文分裂、成本、trace 长度和汇总错误，需要清晰任务边界和终止条件。
- 误解：有 sandbox 就一定安全。README 提醒 LocalSandboxProvider / local trusted environment 有边界；公网或局域网部署需要认证、IP allowlist 和隔离。
- 风险：skill 太强会把错误工作流、越权工具或供应链风险带进执行循环。
- 风险：长期记忆如果没有 TTL、去重和人工复核，可能把过期偏好或错误事实固化。

## 边界细节

和 [[Agent Harness]] 的关系：DeerFlow 是 Agent Harness 的具体实现样本。[[Agent Harness]] 是通用概念，DeerFlow 是产品化开源项目。

和 [[LangChain DeepAgents]] 的关系：二者都在长任务 harness 层。DeepAgents 更像 SDK / template，DeerFlow 更像完整 app / gateway / sandbox / skills / memory 的运行底座。

和 [[Multi-agent Orchestration]] 的关系：DeerFlow 的 sub-agents 是多 Agent 编排的一种实现。真正多 Agent 可靠性还取决于任务拆分、上下文隔离、结果合并、停止条件和最终验证。

和 [[Context Engineering]] 的关系：DeerFlow 的 context engineering 是 runtime 策略，包括 isolated sub-agent context、summarization、filesystem offloading 和 tool-call recovery；这不是单纯 prompt 排版。

## 现代性状态

- 判定：frontier / volatile 的具体开源 harness；背后的长任务 harness 模式属于 current-practice。
- 稳定部分：长任务 Agent 需要 workspace、sub-agents、skills、sandbox、memory、context compression、trace 和安全部署边界。
- 易变部分：DeerFlow 的 API、默认模型推荐、skills 格式、sandbox provider、IM channels、memory 行为和 security defaults 会快速变化。
- 复查策略：优先更新 [[DeerFlow Repo]] 的 `last_checked` 和本卡的 2.0 边界；不要把 1.x Deep Research 行为混进 2.0 harness 定义。

## 现代系统怎么吸收 DeerFlow 的价值 / 局限

现代 Agent 系统会把复杂任务拆成可执行、可记录、可恢复的运行过程。DeerFlow 的价值在于把这些运行责任放进一个可试用的 harness：任务有 workspace，子任务有隔离上下文，工具有执行环境，长上下文通过摘要和文件系统缓解，最终输出以 artifacts 交付。

局限是：harness 只能提供结构，不会自动保证任务成功。真正可靠仍需要 [[Evaluation]]、[[Trace]]、权限审计、sandbox 隔离、人工验收、成本预算和失败回放。

## 证据锚点

- Source: [[DeerFlow Repo]]
- Anchor: [[DeerFlow Repo#一句话]], [[DeerFlow Repo#关键事实]], [[DeerFlow Repo#边界提醒]]
- Evidence type: official GitHub README / website source note + engineering synthesis.
- Confidence: medium-high
- Boundary: “DeerFlow 2.0 是 super agent harness”由 README 支撑；“它体现长任务 Agent harness 模式”是本 vault 的工程综合。

## 复习触发

- 为什么 DeerFlow 不是 RAGFlow，也不是 RAG 框架？
- DeerFlow 的 sub-agents、sandbox、filesystem、memory 分别解决什么问题？
- 如果把 DeerFlow 部署到局域网或公网，哪些安全边界必须补上？

## 相关链接

- [[Agent Harness]]
- [[Agent Framework]]
- [[LangChain DeepAgents]]
- [[LangGraph]]
- [[Multi-agent Orchestration]]
- [[Sandbox Workspace]]
- [[Context Engineering]]
- [[Long-term Memory]]
- [[Tool Permissioning]]
- [[DeerFlow Repo]]
