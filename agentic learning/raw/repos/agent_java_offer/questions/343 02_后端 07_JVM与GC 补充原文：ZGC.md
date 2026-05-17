---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - jvm
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: supplement-section
direction: 02_后端
category: 07_JVM与GC
last_checked: 2026-05-09
freshness: watch
sha256: e00caf5d031f3859b3e76322b25cd09e624e41463d771ce38e4ae7bcf4e15538
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 补充原文：ZGC

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `07_JVM与GC`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

## 13. 补充原文：ZGC

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

#### 2.3.2 ZGC

ZGC（The Z Garbage Collector）是 JDK 11 中推出的一款低延迟垃圾回收器，它的设计目标包括：
- 停顿时间不超过 10ms；
- 停顿时间不会随着堆的大小，或者活跃对象的大小而增加；
- 支持 8MB~4TB 级别的堆（未来支持 16TB）。

ZGC 几乎所有暂停都只依赖于 GC Roots 集合大小，停顿时间不会随着堆的大小或者活跃对象的大小而增加。与 ZGC 对比，G1 的转移阶段完全 STW 的，且停顿时间随存活对象的大小增加而增加。

ZGC 关键技术：ZGC 通过着色指针和读屏障技术，解决了转移过程中准确访问对象的问题，实现了并发转移。并发转移中“并发”意味着 GC 线程在转移对象的过程中，应用线程也在不停地访问对象。假设对象发生转移，但对象地址未及时更新，那么应用线程可能访问到旧地址，从而造成错误。而在 ZGC 中，应用线程访问对象将触发“读屏障”，如果发现对象被移动了，那么“读屏障”会把读出来的指针更新到对象的新地址上，这样应用线程始终访问的都是对象的新地址。JVM 判断对象是否被移动过，就是利用对象引用地址中的着色指针。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
