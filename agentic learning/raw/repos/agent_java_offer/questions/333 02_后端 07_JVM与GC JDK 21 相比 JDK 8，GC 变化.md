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
sha256: 371588024380a94eb9714387e4f678ce87d113ae6adaf0a7084dc0f67ef4a51f
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# JDK 21 相比 JDK 8，GC 变化

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `07_JVM与GC`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 3. JDK 21 相比 JDK 8，GC 变化

我会从三点讲。

第一，默认收集器从 Parallel GC变成 G1，目标从纯吞吐转向吞吐和停顿时间平衡；低延迟场景可以选 ZGC/Shenandoah，JDK 21 里这些方案成熟度更高；

第二，G1 在 JDK 9 到 21 之间持续优化，比如并行 Full GC、回收策略和内存归还机制更完善，线上稳定性和停顿可预测性都更好。

总结为：JDK 8 更偏吞吐优先，JDK 21 提供了更强的低延迟能力和更成熟的工程可用性。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
