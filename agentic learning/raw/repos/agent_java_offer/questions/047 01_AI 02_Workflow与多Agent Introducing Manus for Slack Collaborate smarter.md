---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "02_Workflow与多Agent"
last_checked: 2026-05-09
freshness: watch
sha256: 22943936625db4529e948db5441366ca59f5e3ed7e4439e6699716d985082fa0
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Permissioning]]"
  - "[[Approval Gate]]"
  - "[[Guardrails]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Context Engineering]]"
  - "[[Tool Calling]]"
  - "[[Human-in-the-loop]]"
  - "[[RAG Citation Faithfulness]]"
---

# Introducing Manus for Slack : Collaborate smarter

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Least Privilege Tools]]
- [[Tool Permissioning]]
- [[Approval Gate]]
- [[Guardrails]]
- [[Audit Log]]
- [[Trace]]
- [[Memory]]
- [[Agent State]]
- [[Context Engineering]]
- [[Tool Calling]]
- [[Human-in-the-loop]]
- [[RAG Citation Faithfulness]]

## 题目正文

### 7) Introducing Manus for Slack : Collaborate smarter

- 原文链接：
  - [https://manus.im/blog/introducing-manus-for-slack-collaborate-smarter](https://manus.im/blog/introducing-manus-for-slack-collaborate-smarter)
- 核心思想：
  - 把 Agent 接入团队协作平台（Slack），重点是线程级上下文和团队协作效率。
  - 相比单人会话，团队场景更依赖权限控制、上下文隔离与可追踪交互。
  - 文章展示了 Agent 从个人助手走向组织协作助手的落地方式。
- 文章概述（约500~1000字）：
  - 这篇文章展示的是 Agent 从个人工具走向团队生产力系统的关键一步：接入 Slack 等协作平台。看起来是“多一个入口”，本质上是上下文和权限模型都发生了变化。单人会话里，问题通常是连续且目标单一；团队协作里，一个频道可能并行多个任务、多个角色、多个优先级，如果没有线程级上下文隔离，很容易出现信息串台和指令污染。文章强调以 thread 作为上下文边界，把任务状态绑定到对话线程，并结合成员身份做权限映射，确保谁能触发什么动作、谁能看到什么结果都有明确规则。它还体现了协作场景的两个工程要求：一是可追踪，决策链和执行记录要可回放；二是可中断，关键节点允许[[Human-in-the-loop|人工介入]]确认，避免自动化操作越权。对面试来说，这篇文章能帮助你回答“企业里 Agent 为什么比个人场景难”：难在组织协作带来的权限、审计和责任边界，而不只是模型能力。你可以概括为：协作平台中的 Agent，本质是“流程参与者”，必须遵守团队的治理规则，才能真正被业务接受和长期使用。
- 面试可能问的点：
  - 问：团队协作场景下如何做会话隔离与权限控制？
  答：我会把上下文主键设计为“workspace/channel/thread/user”，线程内共享任务状态，线程间严格隔离。权限采用角色映射到动作级策略，例如谁可触发外部调用、谁可审批敏感动作。这样既能协同，又能避免跨任务串台和越权执行。
  - 问：群聊中的上下文污染如何治理？
  答：先限制上下文来源：默认只读当前线程和被@消息；再做消息分级，低价值闲聊不进入任务[[Memory|记忆]]；关键事实落结构化状态而非自然语言堆叠。发生冲突时以最近确认状态为准，并保留证据引用，避免模型被噪声对话带偏。
  - 问：为什么协作平台接入后，审计与追踪要求会更高？
  答：因为协作平台涉及多人协同和组织责任，任何自动动作都可能影响业务结果与合规边界。必须回答清楚“谁发起、谁审批、执行了什么、影响了什么”，并支持回放复盘。审计链完整，才能在事故、争议和监管场景下可追责、可证明。

---

## 5. 补充原问：[[Tool Calling|工具调用]]的业务流程如何串起来？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
