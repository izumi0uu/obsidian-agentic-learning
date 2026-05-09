---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "09_RPC与网关治理"
last_checked: 2026-05-09
freshness: watch
sha256: 24768453c6009f7c1f0ec70125380c88d3f12e88dce4b5e865f0355eed435a90
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
---

# Sidecar 模式的收益与代价是什么？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `09_RPC与网关治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]

## 题目正文

### 2. 问：Sidecar 模式的收益与代价是什么？

答：收益是能力标准化、流量可编程、可观测统一；代价是资源开销增加、链路复杂度上升、排障层次变深。Sidecar 适合治理需求强且服务数量大的系统，小规模系统可能得不偿失。  
追问：如何量化 Sidecar 带来的时延和成本增量？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
