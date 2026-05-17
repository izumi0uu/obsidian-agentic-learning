---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/04_%E5%B9%B6%E5%8F%91%E4%B8%8E%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/04_并发与异步任务/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 04_并发与异步任务
last_checked: 2026-05-09
freshness: watch
sha256: 817b4b7202873f2f0b607349eda82340a6b14372231f499e6d67c395a110f277
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# `synchronized` vs `ReentrantLock`？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/04_并发与异步任务/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/04_%E5%B9%B6%E5%8F%91%E4%B8%8E%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `04_并发与异步任务`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

### 1. `synchronized` vs `ReentrantLock`？

`synchronized` 语法简单、JVM 优化成熟，适合大多数互斥场景。`ReentrantLock` 提供可中断、超时、公平锁和条件队列，适合需要精细控制并发行为的复杂场景。

可以按“原理 + 场景”这样答：

1. `synchronized` 底层原理

- JVM 内置监视器锁（Monitor）。  
- 对象头里有 `Mark Word`，记录锁状态（无锁/偏向/轻量/重量）。  
- 竞争低时走轻量路径（CAS + 自旋）；竞争高会膨胀成重量级 Monitor，线程阻塞/唤醒由 JVM/OS 协作完成。  
- `monitorenter/monitorexit` 保证互斥和内存可见性（happens-before）。

1. `ReentrantLock` 底层原理

- 基于 JUC 的 AQS（AbstractQueuedSynchronizer）。  
- 用 `state` 表示锁占用，CAS 抢锁。  
- 抢不到就进入 CLH 变种等待队列`LockSupport.park/unpark` 挂起唤醒。  
- 支持可重入、公平/非公平、可中断、超时、多 `Condition`。

1. 生产场景怎么选

`synchronized` 常见场景：  

- 方法级/代码块级简单互斥。  
- 业务内小临界区，逻辑简单，优先可读性和低心智负担。  
- 框架里很多简单线程安全封装。

`ReentrantLock` 常见场景：  

- 需要 `tryLock(timeout)` 防止长时间阻塞。  
- 需要 `lockInterruptibly()` 支持取消任务。  
- 需要公平锁避免饥饿（少量场景）。  
- 需要多个条件队列（生产者消费者多条件唤醒）。  
- 需要结合 AQS 能力做更精细并发控制。

一句话：  

`synchronized` 是 JVM 原生监视器锁，适合“简单可靠”`ReentrantLock` 是 AQS 可编排锁，适合“复杂控制”。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
