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
sha256: 7f9c8593f2493e534f10b04cba0ecdb3fe0724b4db5c85a5f99a919de4c742d8
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent Workflow]]"
  - "[[Agent Framework]]"
  - "[[Durable Execution]]"
---

# LangGraph 如何防循环、防失控？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent Workflow]]
- [[Agent Framework]]
- [[Durable Execution]]

## 题目正文

### 3. 子问题：LangGraph 如何防循环、防失控？

答：

在图层面加条件边与终止条件，并配置最大步数、最大重试次数、超时和置信度阈值。

对高风险节点加人工审批或兜底节点，不允许无条件回环。

核心是把“结束条件”设计成硬约束，而不是靠模型自觉停机。

追问：线上出现死循环时，你第一步怎么止损？

第一步我会先做**流量止血**：立刻关闭该 LangGraph [[Agent Workflow|工作流]]入口（feature flag/路由开关），把请求切到降级路径（单轮回答或人工兜底），**先阻止新循环继续产生**。

然后才做两件事：

1. 批量中断在跑实例（按 run_id/thread_id 取消，必要时清理队列）。
2. 临时加硬阈值（max_steps/recursion_limit/timeout）再恢复小流量。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
