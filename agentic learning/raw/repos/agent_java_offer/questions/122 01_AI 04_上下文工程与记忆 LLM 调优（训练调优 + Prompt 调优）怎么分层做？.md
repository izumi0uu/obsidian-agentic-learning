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
sha256: ee5e9a30996bb0b74ab1e902a4b99bc93073f3fc7b8e56e126bfb5e2313372e5
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Hybrid Search]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[Guardrails]]"
  - "[[Tool Calling]]"
  - "[[Durable Execution]]"
  - "[[Observation]]"
  - "[[RAG Evaluation]]"
  - "[[Query Rewrite]]"
  - "[[Context Engineering]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
---

# [[LLM]] 调优（训练调优 + [[Prompt]] 调优）怎么分层做？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Hybrid Search]]
- [[Retriever]]
- [[Reranking]]
- [[Chunking]]
- [[Document Ingestion]]
- [[Guardrails]]
- [[Tool Calling]]
- [[Durable Execution]]
- [[Observation]]
- [[RAG Evaluation]]
- [[Query Rewrite]]
- [[Context Engineering]]
- [[Prompt]]
- [[Hallucination]]
- [[LLM Training Pipeline]]
- [[LLM]]

## 题目正文

### 2. 子问题：LLM 调优（训练调优 + Prompt 调优）怎么分层做？

答：
调优要分层：第一层 Prompt 调优（成本最低，迭代最快）；第二层检索和工具链路/[[Context Engineering|上下文工程]]优化（提升事实性与可执行性）；第三层模型微调（提升领域表达和行为稳定性）。经验是“先提示词和工具链路，后动模型参数”。很多线上问题其实来自上下文构造和[[Evaluation|评估]]缺失，不是模型本身不够强。

**L1 Prompt 调优（先做）**

1. 定义执行协议: 明确角色、边界、输出格式、拒答策略。
2. 做结构化输出：JSON Schema/[[Tool Calling|函数调用]]，减少自由发挥。
3. 少量高质量 few-shot：给正例和反例，控制风格和步骤。
4. 做上下文工程：信息按 Gather-Select-Structure-Compress 组织，避免噪声。
5. 建评测集：准备 50-200 条真实样本，按准确率、格式通过率、[[Hallucination|幻觉]]率评估。
6. 提示词版本化：A/B 对比、灰度发布、可回滚。

**L2 检索与工具链路调优（第二层）**

1. RAG 数据治理：清洗、去重、切块策略、元数据标签。
2. 检索策略优化：[[Retriever|向量检索]] + 关键词检索 + 重排（hybrid + [[Reranking|rerank]]）。
3. [[Query Rewrite|查询改写]]：multi-query、HyDE、同义词扩展，提升召回。
4. 工具编排：路由器决定“直接答/检索/调工具”，设置信心阈值和兜底。
5. 结果校验：工具返回做 schema 校验、规则校验，失败自动重试或降级。
6. 观测闭环：看 检索命中率、工具[[Task Success Rate|成功率]]、端到端任务成功率、时延、成本。

**L3 训练调优（最后做）**

1. 触发条件：Prompt+RAG 已到瓶颈，仍有稳定性/领域表达问题。
2. 先做 SFT：用真实任务[[Trace|轨迹]]数据（输入、目标输出、工具轨迹）微调。
3. 参数高效微调：优先 LoRA/QLoRA，成本低、迭代快。
4. 再做偏好优化：DPO/RLHF 提升“答案质量与行为一致性”。
5. 训练数据重点：覆盖高频失败样本、难例、边界例；严格去重和标注规范。
6. 上线策略：影子流量 + 小流量灰度 + 回归评测，避免“微调后退化”。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
