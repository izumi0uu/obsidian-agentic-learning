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
sha256: 864607e2f8efea87dc05067c5b1cd4a289aa60175c1b1a5b990c9b0c527d4383
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Agent State]]"
---

# ZGC是什么?

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/07_JVM与GC/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/07_JVM%E4%B8%8EGC/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `07_JVM与GC`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Agent State]]

## 题目正文

### 4. ZGC是什么?

ZGC 是 JDK 提供的低延迟垃圾回收器，核心目标是把 GC 停顿压到毫秒级甚至亚毫秒级，并且停顿时间对堆大小不敏感。它的关键思路是把大部分标记、重定位工作放到并发阶段，Stop-The-World 只保留很短的根扫描等必要步骤。  

实现上，ZGC 用了着色指针（colored pointers）和读屏障（load barrier）：对象地址里带状态位，线程在读对象时通过屏障感知对象是否被移动并完成自愈跳转，这样对象迁移可以和业务线程并发进行。  

**着色指针（Colored Pointers）**：在指针里带状态信息，GC 能快速判断对象状态。

**读屏障（Load Barrier）**：线程读对象时，若对象已搬迁，屏障会把引用“修正到新地址”。

所以它适合对延迟非常敏感的服务，比如交易链路、实时推荐、网关核心路径；代价是吞吐可能略低、CPU开销更高，调优和观测也更复杂。工程上通常是‘先 G1，延迟 SLA 很严再上 ZGC’。”

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
