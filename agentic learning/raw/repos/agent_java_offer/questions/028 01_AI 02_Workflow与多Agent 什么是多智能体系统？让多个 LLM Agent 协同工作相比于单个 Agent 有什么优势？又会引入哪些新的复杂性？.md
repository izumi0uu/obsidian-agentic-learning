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
sha256: 75729afec298ec73b053b65740f022615607ae478f151205f940f1578d76a777
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent State]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Planning]]"
  - "[[Agent]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
---

# 什么是多[[Agent|智能体]]系统？让多个 [[LLM]] Agent 协同工作相比于单个 Agent 有什么优势？又会引入哪些新的复杂性？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Agent State]]
- [[Multi-agent Orchestration]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Planning]]
- [[Agent]]
- [[LLM Training Pipeline]]
- [[LLM]]

## 题目正文

### 3. 子问题：什么是多智能体系统？让多个 LLM Agent 协同工作相比于单个 Agent 有什么优势？又会引入哪些新的复杂性？

答：
多智能体系统就是把一个复杂目标拆成多个角色协同完成，例如[[Planning|规划]]、执行、审校分工。从而提高复杂[[Task Success Rate|任务成功率]].

优势是:

 1.专业化:可以为每个Agent设定不同的角色和专长。例如，在一个软件开发团队中，可以有一个“产品经理Agent”负责需求分析，一个“程序员Agent”负责编写代码，一个“测试工程师Agent”负责编写测试用例。每个Agent都可以基于专门的知识和工具进行微调，从而在各自领域达到更高的专业水平。

2.并行化:复杂任务可以被分解成多个子任务，并分配给不同的Agent同时处理，这大大缩短了解决问题的总时间

新增复杂性:

1.通信协议: Agent之间如何有效沟通？需要设计一套标准化的通信协议和消息格式，确保它们能够相互理解意图、状态和知识

2.任务协调、状态一致性：谁负责、谁失败、谁回滚都要定义清楚。没有明确编排规则时，多 Agent 反而会比单 Agent 更不稳定。

多agent的框架: LangGraph, OpenAI Agents SDK, AutoGen, CrewAI, claude agent sdk 的agent team.

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
