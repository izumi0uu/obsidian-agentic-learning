---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - framework
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 08_框架协议与工程化
last_checked: 2026-05-09
freshness: watch
sha256: b865d4ed3b7a5e7c9dba8d1e1a67b4c811ca5cb3a295c604376eb3f08f8d536d
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Retriever]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[LLM]]"
---

# 你怎么做 LangChain 的可组合编排（LCEL）？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Retriever]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[LLM]]

## 题目正文

### 2. 子问题：你怎么做 LangChain 的可组合编排（LCEL）？

答：
我会把 Prompt、模型、解析器、检索器都抽成 Runnable，通过 LCEL 组合成可复用链路，并把输入输出标准化。这样便于做链路替换和 A/B 对比，也能把失败点定位到具体节点，而不是整条链“黑盒失败”。

追问：LCEL 和手写 if/else 调用代码相比，工程收益在哪？

核心收益是把 [[LLM]] 流程从‘过程代码’变成‘可组合的数据流组件’，在可维护性和可运营性上明显更好。

具体工程收益有 7 点：

1. **统一抽象**：Prompt/Model/[[Retriever]]/Parser 都是 Runnable，可插拔替换。
2. **可组合复用**：链路像搭积木，公共子链可复用，避免复制粘贴。
3. **[[Observability|可观测性]]更好**：节点级 [[Trace|trace]]、耗时、token、错误定位更清晰。
4. **内建运行能力**：天然支持 streaming、batch、并行、重试、fallback。
5. **测试更容易**：每个节点可单测/Mock，回归粒度比整段 if/else 更细。
6. **变更成本更低**：换模型、换检索器、加校验器通常只改局部节点。
7. **团队协作更稳**：流程结构显式，便于 code review 和规范治理。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
