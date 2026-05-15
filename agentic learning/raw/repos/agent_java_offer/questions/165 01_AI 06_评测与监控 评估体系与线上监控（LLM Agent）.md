---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "evaluation"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "06_评测与监控"
last_checked: 2026-05-09
freshness: watch
sha256: c767c685ca662dfffd222065622477c5493e348a52b70ec1182968ddf4b4aa7e
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
  - "[[LLM-as-Judge]]"
  - "[[Durable Execution]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[LLM]]"
---

# 评估体系与线上监控（LLM/Agent）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `06_评测与监控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[LLM-as-Judge]]
- [[Durable Execution]]
- [[Agent Loop]]
- [[Agent]]
- [[LLM]]

## 题目正文

### 1. 子问题：[[Evaluation|评估体系]]与[[Observability|线上监控]]（[[LLM]]/[[Agent]]）

主问题：如何设计一套可落地的 LLM/Agent 评估体系？

口述答案：
评估要“离线 + 在线 + 人评”三位一体。离线看能力覆盖（事实性、推理、安全、格式）；在线看业务指标（[[Task Success Rate|成功率]]、转化、时延、成本、稳定性）；人评校准自动评估偏差。对 Agent 还要看过程指标，如步数、工具成功率、重试率、中断率。上线后通过持续监控与坏例回流形成闭环，避免模型漂移无人感知。

常见追问：

1. 为什么 BLEU/ROUGE 评 LLM 不够？
2. [[LLM-as-Judge|LLM-as-a-Judge]] 的偏差怎么控制？
3. 线上成功率下降如何快速归因？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
