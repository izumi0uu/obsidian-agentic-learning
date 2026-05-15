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
entry_type: "supplement-section"
direction: "01_AI"
category: "02_Workflow与多Agent"
last_checked: 2026-05-09
freshness: watch
sha256: 9a5b5852b7428db9cc6b345da7e7fc31743267e39690422848699150e7d29615
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Retriever]]"
  - "[[RAG]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Planning]]"
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Trace]]"
  - "[[Observability]]"
---

# 补充材料：多步骤研究型[[Agent Workflow|工作流]]的产品化思路

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Retriever]]
- [[RAG]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Planning]]
- [[Agent]]
- [[Agent Loop]]
- [[Trace]]
- [[Observability]]

## 题目正文

## 2. 补充材料：多步骤研究型工作流的产品化思路

### 2) Introducing Wide Research

- 原文链接：
  - [https://manus.im/blog/introducing-wide-research](https://manus.im/blog/introducing-wide-research)
- 核心思想：
  - 提出 Wide Research 作为复杂研究任务的产品能力，目标是让 [[Agent]] 处理更宽、更深的任务。
  - 本质是把任务拆解与多源信息整合能力产品化，而不是只做一次性问答。
  - 强调在真实业务任务中，任务编排和可恢复执行比单次回答“聪明”更重要。
- 文章概述（约500~1000字）：
  - 这篇“Introducing Wide Research”本质是在回答一个问题：为什么传统对话式 AI 在真实研究任务里常常“看起来聪明、做起来不稳”。文章提出的解决方向不是再堆一个更长回复，而是把研究任务拆成可管理的多阶段流程。所谓“Wide”，一是信息覆盖面要广，能够跨来源、跨类型收集证据；二是分析深度要够，能从线索继续下钻，而不是停在表面总结。文章强调，研究型任务通常不是一次检索+一次生成就结束，而是“[[Planning|计划]]-执行-复核-修正”的循环，因此系统必须支持阶段状态、断点恢复和可追踪过程。Manus 在产品上把这些能力显式化：先给出任务框架，再并行收集材料，然后做证据整合与结论生成，最后输出可交付结果。文章传达的核心不是“回答更长”，而是“流程更完整、过程更可靠”。从面试视角，你可以把它作为“Agent 从问答走向工作流”的案例：关注的指标从文本质量转向[[Task Success Rate|任务成功率]]、可解释性、时延和成本；关注的风险从“答错一句话”转向“流程中断、证据遗漏、结论失真”。因此它更像一个研究任务操作系统，而不只是一个会写字的模型壳。
- 面试可能问的点：
  - 问：多步骤研究型 Agent 的核心链路怎么设计？
  答：我会设计成“规划-并行采集-证据归并-结论校验-交付输出”五段。先把问题拆成子任务，再并行拉取多源信息，做去重和可信度排序，最后生成可追溯结论。每段都有输入输出契约和失败恢复点，避免长链路一步错全盘错。
  - 问：为什么复杂任务更依赖“编排能力”而非“单次模型能力”？
  答：复杂任务失败通常不在“某一句答错”，而在流程失控：顺序不对、依赖缺失、证据冲突没处理。编排能力决定任务能否按阶段收敛、能否回滚重试、能否追踪责任。模型再强，如果没有稳定编排，也很难在生产场景持续交付。
  - 问：Wide Research 和普通 [[RAG]] 问答的工程差异是什么？
  答：普通 RAG 更像单跳检索增强，目标是回答一个问题；Wide Research 是任务型流程系统，要支持多轮规划、并行采集、阶段归纳和动态重规划。前者强调召回与生成质量，后者还要强调任务成功率、过程可解释性、执行可靠性与恢复能力。

---

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
