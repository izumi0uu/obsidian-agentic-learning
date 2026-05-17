---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - memory
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 04_上下文工程与记忆
last_checked: 2026-05-09
freshness: watch
sha256: d9d08aebcd692e471268ef32bdd98a6611165ce9386c8d3bb85e894510eb2eec
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[RAG]]"
  - "[[Context Engineering]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[Agent]]"
  - "[[Durable Execution]]"
  - "[[Observability]]"
  - "[[RAG Evaluation]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
  - "[[Agent 主题]]"
---

# 调优分层与[[Prompt]]工程协同

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
- [[RAG]]
- [[Context Engineering]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[Agent]]
- [[Durable Execution]]
- [[Observability]]
- [[RAG Evaluation]]
- [[Prompt]]
- [[Hallucination]]
- [[Agent 主题]]

## 题目正文

### 1. 子问题：调优分层与Prompt工程协同

主问题：[[LLM]] 效果不好时，如何分层调优并协同 Prompt/[[RAG]]/模型？

口述答案：
我采用“三层法”：先 Prompt 与[[Context Engineering|上下文工程]]，再检索/工具链路，再模型微调。原则是先改低成本高收益环节，再动模型参数。Prompt 要版本化、可测试、可回滚；核心指标是[[Task Success Rate|任务成功率]]、格式通过率、[[Hallucination|幻觉]]率、时延和成本。Prompt 与微调不是替代关系：前者负责快速可控，后者负责长期稳定。

常见追问：

1. 如何避免 Prompt 越写越长、成本失控？
2. 什么时候必须进入微调阶段？
3. 如何做 A/B 与灰度验证？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
