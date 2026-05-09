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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/06_%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8%E4%B8%8E%E6%9E%B6%E6%9E%84%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/06_分库分表与架构治理/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "06_分库分表与架构治理"
last_checked: 2026-05-09
freshness: watch
sha256: 32abfe91b6896d81c452068795b930829a63acea803d5eb3a3375755bdfa7883
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 跨分片 join、分页、排序、count 怎么处理？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/06_分库分表与架构治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/06_%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8%E4%B8%8E%E6%9E%B6%E6%9E%84%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `06_分库分表与架构治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 4. 问：跨分片 join、分页、排序、count 怎么处理？

答：原则是尽量避免跨分片实时计算。常见做法是业务侧聚合、异步宽表、搜索引擎或OLAP承接复杂查询。分页走“先路由再聚合”，深分页用游标。count 用近实时汇总表，不做全量实时扫。  
追问：跨分片查询延迟高时，先改 SQL 还是先改架构？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
