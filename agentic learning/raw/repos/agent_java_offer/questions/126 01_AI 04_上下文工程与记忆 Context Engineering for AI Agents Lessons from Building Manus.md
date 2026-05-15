---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "memory"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "04_上下文工程与记忆"
last_checked: 2026-05-09
freshness: watch
sha256: b1a6e39f021c54fc5afde56e49f8460c18cfaf300f22d5a0ea7f34c733ab9f01
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[Long-term Memory]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Context Engineering]]"
  - "[[Tool Calling]]"
  - "[[Durable Execution]]"
  - "[[Observation]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[RAG Evaluation]]"
  - "[[Top-K]]"
  - "[[Context Window]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
  - "[[Token]]"
---

# [[Context Engineering]] for AI Agents: Lessons from Building Manus

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Vector Database]]
- [[Embedding]]
- [[Long-term Memory]]
- [[Memory]]
- [[Agent State]]
- [[Context Engineering]]
- [[Tool Calling]]
- [[Durable Execution]]
- [[Observation]]
- [[Trace]]
- [[Observability]]
- [[RAG Evaluation]]
- [[Top-K]]
- [[Context Window]]
- [[Prompt]]
- [[Hallucination]]
- [[Token]]

## 题目正文

### 1) Context Engineering for AI Agents: Lessons from Building Manus

- 原文链接：
  - [https://manus.im/blog/context-engineering-for-ai-agents-lessons-from-building-manus](https://manus.im/blog/context-engineering-for-ai-agents-lessons-from-building-manus)
- 核心思想：
  - [[Context Window|上下文窗口]]不是“越大越好”，核心是**上下文工程**：如何挑选、组织、压缩、更新上下文。
  - 文章强调把 Agent [[Memory|记忆]]分层管理，而不是把历史对话全量塞给模型。
  - 提到需要控制无关噪声进入上下文，否则会直接拉低推理稳定性与[[Tool Calling|工具调用]]质量。
- 文章概述（约500~1000字）：
  - 这篇文章最重要的观点是：当我们从“聊天机器人”走向“可执行任务的 Agent”时，[[Prompt]] Engineering 已经不够用了，必须升级为 Context Engineering。原因在于 Agent 的上下文不再只是用户一句提问，而是一个持续演化的状态系统，里面包括工具调用结果、网页观察、代码执行反馈、阶段结论、失败重试历史以及[[Long-term Memory|长期记忆]]。文章把问题讲得很直接：很多团队不是模型不够强，而是把无关信息不断塞进上下文，导致注意力被稀释、推理漂移、成本失控、时延上升。Manus 的经验是把上下文当成“生命周期工程”来做：进入系统前先筛选，执行过程中持续重写和压缩，关键事实写入可检索记忆，低价值内容及时淘汰；并通过任务阶段切换控制上下文粒度，避免单一大上下文拖垮全链路。文章还强调“状态优先于文本”：模型每一步都应读到可执行状态，而不是冗长叙述。对面试最有价值的启发是，你可以把 Context Engineering 分解成四件事来回答：上下文采集、上下文选择、上下文压缩、上下文治理（预算/监控/回滚）。
- 面试可能问的点：
  - 问：你如何定义“上下文工程”？和 Prompt Engineering 的边界是什么？
  答：我会把 Prompt Engineering 定义为“单轮输出控制”，重点是角色、格式、约束；Context Engineering 是“多轮状态治理”，重点是信息进入、保留、淘汰和回取。前者解决“怎么说”，后者解决“基于什么说”，两者在 Agent 项目里必须同时做。
  - 问：长任务中如何做上下文裁剪、摘要和分层记忆？
  答：我一般用三层：运行态只保留当前决策必需字段；历史过程做阶段摘要；原始证据外部化到文件或[[Vector Database|向量库]]按需回取。每个阶段结束都产出结构化中间结果，避免把完整聊天记录持续塞给模型，既降噪又控成本。
  - 问：上下文变大后，如何平衡准确率、时延和成本？
  答：先设 [[Token|token]] 预算和 SLO，再做“高价值优先注入”：固定规则放 system，动态证据 [[Top-K|top-k]] 注入，低价值历史改摘要。并监控首 token 延迟、总 token、[[Task Success Rate|任务成功率]]和[[Hallucination|幻觉]]率，若成本上升但收益不显著，及时收缩上下文或切换小模型执行子步骤。

---

## 4. 补充材料：如何突破上下文窗口限制

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
