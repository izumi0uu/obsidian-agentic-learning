---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "redis"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/02_Redis/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "supplement-section"
direction: "02_后端"
category: "02_Redis"
last_checked: 2026-05-09
freshness: watch
sha256: a927c72c80d63941a6c0358ac2b49985ace547e93f50046ea01b8d452267d065
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 补充原文：Redis Hash 扩容

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/02_Redis/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `02_Redis`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

## 14. 补充原文：Redis Hash 扩容

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

#### 2.7.1 Redis Hash扩容

Redis 的 hash 结构扩容：
- 扩容：当 hash 内部的元素比较拥挤时（hash 碰撞比较频繁），就需要进行扩容。扩容需要申请新的两倍大小的数组，然后将所有的键值对重新分配到新的数组下标对应的链表中（rehash）。如果 hash 结构很大，比如有上百万个键值对，那么一次完整 rehash 的过程就会耗时很长。这对于单线程的 Redis 来说压力很大，所以 Redis 采用了渐进式 rehash 的方案。它会同时保留新旧两个 hash 结构，在后续的定时任务以及 hash 结构的读写指令中，将旧结构的元素逐渐迁移到新结构中。这样就可以避免因扩容导致的线程卡顿现象。
- 缩容：Redis 的 hash 结构不但有扩容还有缩容，从这一点出发，它要比 Java 的 HashMap 更完整。缩容原理和扩容一致，只不过新的数组大小要比旧数组小一倍。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
