---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "jvm"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "07_JVM与GC"
last_checked: 2026-05-09
freshness: watch
sha256: 897824e6fb2ed85204a56304fe527d496629855731d01dff232dcc3437a5e260
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# STW 完全避免吗？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `07_JVM与GC`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 10. STW 完全避免吗？

不能。即使是低停顿收集器，也有根扫描、重标记等阶段需要短暂停顿。工程目标不是“零 STW”，而是把停顿压到业务可接受范围并保持可预测。

G1 会有 STW，因为有些阶段必须“冻结世界”才能保证一致性和安全。

核心原理：

1. GC 不是全都能并发做

G1 虽然大量工作并发（并发标记等），但以下关键步骤仍需 STW：

- 根对象快照（Root Scan）  
- Young/Mixed 回收中的对象复制（Evacuation Pause）  
- 引用关系修正的关键切换点（remark/cleanup 的一部分）

1. 为什么这些必须停

GC 线程要搬对象、改引用；业务线程也在同时读写对象。  

如果不停顿做关键切换，会出现“对象被搬走但引用还没统一修正”的不一致风险。  

STW 的作用就是在短时间内拿到一个安全、一致的内存视图。

1. G1 的目标不是“无停顿”，而是“可控停顿”

它通过 Region 粒度回收和回收集预测，把每次停顿控制在目标内（如 `MaxGCPauseMillis`），而不是像传统 Full GC 那样一次长暂停。

一句话：  

**G1 会 STW 是因为对象移动和引用一致性需要原子切换；它做的是“把必须停的阶段做短、做可预测”，而不是完全不暂停。**

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
