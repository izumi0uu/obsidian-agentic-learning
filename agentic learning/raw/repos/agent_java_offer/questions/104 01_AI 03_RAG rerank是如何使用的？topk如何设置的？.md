---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - rag
status: inbox
created: 2026-05-09
updated: 2026-05-16
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/03_RAG/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 03_RAG
last_checked: 2026-05-09
freshness: watch
sha256: 7a90ad1ae74629ec8e02807b656d2bed53b49ce0280a51af57679b2f376dfc94
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[Observation]]"
  - "[[Token]]"
  - "[[RAG 主题]]"
  - "[[Dense Retrieval]]"
---

# [[Reranking|rerank]]是如何使用的？topk如何设置的？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Reranking]]
- [[Retriever]]
- [[Vector Database]]
- [[Embedding]]
- [[LLM]]
- [[RAG]]
- [[Observation]]
- [[Token]]
- [[RAG 主题]]
- [[Dense Retrieval]]
## 题目正文

### 1. 子问题：rerank是如何使用的？topk如何设置的？

**口述答案（约300字）**：
Rerank我会放在“初召回之后、喂模型之前”。先用[[Dense Retrieval|向量检索]]召回较大候选集合，比如Top50或Top100，再用重排模型按query相关性重新打分，截断成最终TopK给[[LLM|大模型]]。这样做的价值是降低噪声上下文，提升答案稳定性。TopK不是固定拍板，我会按任务类型设区间：事实问答通常K小一点，复杂推理K稍大；然后通过离线评测和线上AB找最优点。常见方法是观察“正确率-时延-成本”三条曲线的拐点。若K过小会漏信息，K过大又会稀释注意力并拉高[[Token|token]]成本。我的实践是先保证召回，再通过重排把信息密度做上来，最后再调K而不是反过来。
**来源**：公开社区资料

## 9. 补充原问：[[Vector Database|向量库]]选型

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
