---
type: concept
topic:
  - agent
  - workflow
  - safety
  - verification
  - framework
status: growing
created: 2026-05-14
updated: 2026-05-14
last_checked: 2026-05-14
freshness: watch
conflicts: []
source:
  - "[[Agentproof - Static Verification of Agent Workflow Graphs]]"
  - "[[Agent Workflow]]"
evidence:
  - "[[Agentproof - Static Verification of Agent Workflow Graphs#需要我读的内容]]"
  - "[[Agentproof - Static Verification of Agent Workflow Graphs#论文主张]]"
  - "[[Agentproof - Static Verification of Agent Workflow Graphs#边界提醒]]"
related:
  - "[[Agent Workflow]]"
  - "[[LangGraph]]"
  - "[[Agent Framework]]"
  - "[[Guardrails]]"
  - "[[Policy Engine]]"
  - "[[Human-in-the-loop]]"
  - "[[Tool Permissioning]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
---

# Agent Workflow Static Verification

## 一句话

Agent Workflow Static Verification 是在 Agent workflow 部署或运行前，对显式 workflow graph 的节点、边、可达性、终止性、人类审批路径和时序安全策略做静态检查，提前发现 runtime guardrails 只有在路径被触发后才可能看到的结构缺陷。

## 概念详解

Agent workflow 变成 graph 之后，系统多了一种以前 prompt-only Agent 没有的检查面。节点可能代表 LLM 调用、工具调用、router、人类审批、subgraph 或 exit；边代表条件跳转、循环、并行或 handoff。只要这些结构能从框架 API 中抽出来，一部分安全问题就不再依赖模型是否刚好走到那条路径，而可以在部署前通过图算法或时序策略检查发现。

[[Agentproof - Static Verification of Agent Workflow Graphs]] 给了这个方向的具体样本：它从 LangGraph、CrewAI、AutoGen 和 Google ADK 抽取统一的 typed workflow graph，再做六类结构检查，包括 exit reachability、reverse reachability / livelock、dead-end detection、router shape、human-in-the-loop presence / coverage 和 tool declaration。失败时它生成 witness trace，让开发者看到哪条路径导致死路、不可达或绕过审批。

更进一步，它把一部分安全策略写成 temporal policy DSL，并编译为 DFA。静态模式下，workflow graph 与 DFA 状态做乘积搜索，检查所有拓扑路径是否可能违反策略；运行时模式下，同一类 DFA 可以监控 event trace。这个思路把 [[Guardrails]] 和 [[Trace]] 的边界切得更清楚：guardrail 主要在运行时拦截具体内容或动作，static verification 则检查 graph topology 和路径级 policy。

但这个概念不能被误读成“形式化证明 Agent 安全”。它只覆盖能从 workflow graph 和事件抽象中表达出来的问题。LLM 输出是否真实、是否有毒、工具参数是否业务上合理、用户意图是否被正确理解，仍然需要 runtime guardrails、policy engine、human-in-the-loop、evaluation、red-team 和业务测试。

## 它解决什么问题

它解决的是 Agent workflow 里的“未触发路径风险”。如果一个条件分支只有在少数输入下才会进入，普通测试和 runtime guardrail 可能永远看不到它；但图上如果存在 dead-end、不可达 exit、绕过 human gate 的敏感工具路径，静态验证可以先把它标出来。

它还让高风险流程更接近软件工程里的 CI lint：workflow 定义变更后，先通过结构检查和策略检查，再部署或放行。

## 它不是什么

它不是 [[Guardrails]] 的替代品。Guardrails 仍然需要处理 prompt injection、内容安全、输出格式、运行时工具参数和上下文依赖风险。

它不是 [[Evaluation]] 的替代品。Evaluation 要回答任务成功率、质量、安全率、成本和回归效果；static verification 只回答某些图结构和时序策略是否存在可违反路径。

它也不是完整 formal verification of AI。它不证明模型内部推理正确，不证明生成文本事实正确，也不保证业务后果安全。

## 最小例子

```text
email intake
-> classify intent
-> router
   -> urgent path -> human review -> send
   -> normal path -> draft response
```

如果 `draft response` 没有连到 `send` 或 `exit`，运行时 guardrail 只有在 normal path 被触发时才可能暴露问题。静态检查可以直接发现 normal path 是 dead end，并生成类似 `intake -> classify -> router -> normal -> draft` 的 witness trace。

另一个例子：

```text
customer request -> router -> delete_account_tool
```

如果 policy 要求 sensitive tool 前必须经过 human gate，那么检查可以删除所有 human 节点后再看 sensitive tool 是否仍可达；仍可达就说明存在绕过审批的路径。

## 常见误解 / 风险

- 误解：图检查通过就代表 Agent 安全。实际只能说明某些 topology / policy 属性通过。
- 误解：runtime guardrail 和 static verification 二选一。实际是互补关系。
- 风险：条件边在运行时可能不可达，但静态分析把它当可达，带来 false positive。
- 风险：workflow 动态修改后不重新验证，部署前保证会失效。
- 风险：extractor 依赖框架 API 和命名/annotation 习惯，框架升级或项目风格不同会影响分类准确性。
- 风险：human gate 被检查到“存在”，不代表人类真的看到了足够上下文、风险和回滚方式。

## 边界细节

适合静态验证的属性通常有三个特征：

- 能从 graph topology 表达：例如可达性、死路、livelock、是否绕过某类节点。
- 能从节点/边类型表达：例如 tool node、router node、human node、exit node。
- 能从有限事件抽象表达：例如某动作发生后必须在后续有限步骤内出现 approval。

不适合静态验证的属性通常依赖语义：

- 模型生成内容是否真实。
- router 条件在自然语言语义上是否合理。
- tool 参数是否满足业务策略。
- human approval 是否基于充分上下文。
- 检索证据是否支持最终答案。

和相邻概念的区别：

- [[Agent Workflow]] 是流程结构本身；本概念是检查这个结构的安全/可靠性方法。
- [[Guardrails]] 是运行时防护层；本概念偏部署前或执行前的结构层检查。
- [[Policy Engine]] 决定 allow / deny / require approval 等策略；本概念可以把其中一部分路径策略变成可验证规则。
- [[Trace]] 记录已发生路径；static verification 检查可能路径。两者结合后，可以用 trace 发现真实失败，用 static check 防止同类 topology 缺陷回归。

## 现代性状态

- 判定：frontier / watch。
- 稳定地基：reachability、dead-end detection、automata、model checking、workflow soundness 都是成熟 formal methods / software verification 地基。
- 当前工程吸收：Agent framework 已经把 workflow、state、node、edge、tool、human gate 和 trace 显式化，因此具备被检查的结构面。
- 前沿部分：把这些方法自动接入 LangGraph / CrewAI / AutoGen / Google ADK 等 Agent framework，并把 policy DSL、extractor、witness trace、CI gate 组合成开发者工具，仍是新方向。
- 复查点：关注 Agentproof artifact、LangGraph / CrewAI / AutoGen / ADK 是否出现内置 graph lint / policy verification / CI safety check 能力。

## 现代系统怎么吸收 Agent Workflow Static Verification 的价值 / 局限

现代 Agent 系统可以把它吸收到四个位置：

- PR / CI gate：workflow 定义变更时运行 graph lint 和 policy checks。
- framework compile step：把节点、边、tool metadata、human gate annotation 编译成可检查模型。
- observability / replay：从 trace 中发现真实失败，再写成静态 policy 防止回归。
- safety review：对高风险工具路径做 human gate coverage、tool declaration 和 witness trace 检查。

局限是它只能验证抽象模型。如果 extractor 看不到真实执行路径，或者 policy 没写出真实风险，检查通过也可能只是“模型太粗”。高风险系统仍要配合权限隔离、sandbox、runtime guardrails、human review、audit log 和任务级 evaluation。

## 证据锚点

- Source: [[Agentproof - Static Verification of Agent Workflow Graphs]]
- Anchor: [[Agentproof - Static Verification of Agent Workflow Graphs#需要我读的内容]]
- Anchor: [[Agentproof - Static Verification of Agent Workflow Graphs#论文主张]]
- Anchor: [[Agentproof - Static Verification of Agent Workflow Graphs#边界提醒]]
- Evidence type: arXiv paper source note + extracted PDF / HTML synthesis.
- Confidence: medium-high for the graph/topology verification framing; medium for tool maturity because Agentproof is a 2026 arXiv research artifact and extractor robustness needs more real-world validation.
- Boundary: 本卡不声称 Agentproof 是生产标准；沉淀的是“显式 Agent workflow graph 可以被静态验证”的学习边界。

## 复习触发

1. 为什么 dead-end path 可能被 runtime guardrail 漏掉，却能被 static verification 抓到？
2. Agent Workflow Static Verification 和 Guardrails 的最小区别是什么？
3. 如果一个 LangGraph workflow 运行时会动态加节点，部署前静态验证的保证哪里会失效？
4. “human gate 存在”为什么不等于高风险动作已经安全？

## 相关链接

- [[Agentproof - Static Verification of Agent Workflow Graphs]]
- [[Agent Workflow]]
- [[LangGraph]]
- [[Agent Framework]]
- [[Guardrails]]
- [[Policy Engine]]
- [[Human-in-the-loop]]
- [[Tool Permissioning]]
- [[Trace]]
- [[Evaluation]]
