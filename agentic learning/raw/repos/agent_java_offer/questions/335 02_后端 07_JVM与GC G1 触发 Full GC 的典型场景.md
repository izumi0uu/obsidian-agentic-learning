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
sha256: 603098a22eb103d8950b9b2a23ef19be7cd0bc22806b742d190376e41509311b
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# G1 触发 Full GC 的典型场景

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `07_JVM与GC`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 5. G1 触发 Full GC 的典型场景

- to-space exhausted / evacuation failure：复制存活对象时没有足够可用 Region。
- 老年代增长太快：并发标记还没完成就快打满（回收跟不上分配）。
- Humongous 大对象（超过 Region 一半）申请失败或碎片严重。
- 元空间（Metaspace）压力过大。

排查与优化方向

- 先看 Full GC 前后老年代占用曲线和分配速率，不只看停顿时间。
- 增加堆或预留空间：-Xmx、-XX:G1ReservePercent。
- 避免大对象/降低 Humongous 压力（必要时调 G1HeapRegionSize）。
- 限制显式 GC：-XX:+DisableExplicitGC 或 -XX:+ExplicitGCInvokesConcurrent。
- 检查是否有内存泄漏和晋升压力过高。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
