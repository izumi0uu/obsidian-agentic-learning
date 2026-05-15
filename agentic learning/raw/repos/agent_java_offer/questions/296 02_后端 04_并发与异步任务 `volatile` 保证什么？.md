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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/04_%E5%B9%B6%E5%8F%91%E4%B8%8E%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/04_并发与异步任务/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "04_并发与异步任务"
last_checked: 2026-05-09
freshness: watch
sha256: 5580852bbc13b15d6d5cac062ff7f2a6471bf3a89114590500b8d72e87a45c3b
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# `volatile` 保证什么？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/04_并发与异步任务/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/04_%E5%B9%B6%E5%8F%91%E4%B8%8E%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `04_并发与异步任务`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki


## 题目正文

### 2. `volatile` 保证什么？

volatile 保证写入对其他线程可见，并通过内存屏障约束指令重排保证顺序性。它不保证复合操作原子性，所以 i++ 这类读改写仍需锁或原子类

`可以把 volatile 记成两件事：**可见性 + 有序性**，不管原子性。`

`

1. 可见性`

`一个线程写 volatile 变量后，其他线程能尽快看到最新值。`  

`原因是写入会刷新到主内存，读取会从主内存重新取值，而不是长期用线程本地缓存。`

`

1. 有序性（禁止特定重排）`

`volatile 通过内存屏障建立 happens-before：`  

`- 对同一个 volatile 变量，线程 A 的写 happens-before 线程 B 的读。`  

`- 在 volatile 写之前的普通写，不会被重排到它之后。`  

`- 在 volatile 读之后的普通读，不会被重排到它之前。`  

`所以常用于“发布标志位”。`

`

1. 不保证原子性`

`

1. 典型使用场景`

`- 停止标志volatile boolean running。`  

`- 双重检查单例里的 volatile instance（防止指令重排导致半初始化对象可见）。`  

`- 状态位通知（一个线程写，多个线程读）。AQS中的state`

`一句话：`  

`volatile 让“看得见、顺序对”，但“改得准”还得靠锁或原子类。`

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
