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
entry_type: question
direction: 02_后端
category: 07_JVM与GC
last_checked: 2026-05-09
freshness: watch
sha256: 645b86cc30791738296f9f4e686d13a21334d78f17ce959421e9aa5991041303
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# OOM 定位第一步？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `07_JVM与GC`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki


## 题目正文

### 8. OOM 定位第一步？

第一步确实是你写的那句：**先判 OOM 类型**。  

因为不同类型，抓证据和排查工具完全不同。

可以这样面试回答：

1. 先看报错文本，快速分类

- `Java heap space`：堆内存问题  
- `GC overhead limit exceeded`：堆快满且回收效率极差  
- `Metaspace`：类元数据区问题  
- `Direct buffer memory`：堆外直接内存问题  
- `unable to create new native thread`：线程数/系统资源问题

1. 为什么这一步最关键

如果把 `Direct buffer memory` 当成堆泄漏去看 Heap Dump，方向会跑偏，浪费时间。

1. 分类型抓现场

- 堆问题`HeapDump` + GC 日志（MAT 看 Dominator Tree、引用链）  
- Metaspace：看类加载量、ClassLoader 统计（常见类加载器泄漏）  
- Direct Memory：看 NMT/Netty buffer 使用`MaxDirectMemorySize`  
- Native Thread：看线程数`jstack`、系统 `ulimit` 和 `-Xss`

1. 再做根因归类

最后归到三类之一：  

- 泄漏（对象不释放）  
- 突增（流量/任务峰值）  
- 配置不合理（堆、元空间、线程栈、直接内存参数太小）

一句话收口：  

**OOM 定位不是先调参数，而是先“判类型”，再用对应证据链定位是泄漏、突增还是配置问题。**

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
