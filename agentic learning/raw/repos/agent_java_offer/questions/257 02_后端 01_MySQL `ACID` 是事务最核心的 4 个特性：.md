---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "mysql"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/01_MySQL/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "01_MySQL"
last_checked: 2026-05-09
freshness: watch
sha256: 5b563547d0c730693ec51bcf5ae8ef1996fa3958fef9e32f3b89374c60a26fb6
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# `ACID` 是事务最核心的 4 个特性：

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/01_MySQL/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `01_MySQL`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

### 8. `ACID` 是事务最核心的 4 个特性：

原子性(Atomic):

- 事务包含的所有操作要么全部执行,要么全部不执行.

一致性(Consistency):

- 事务应确保数据库状态从一个一致的状态转变为另外一个一致的状态, 比如A和B无论怎么转账,两者的金额之和不变.

隔离性(Isolation):

- 多个事务并行执行时,一个事务的执行不能影响其他事务的执行.

持久性(Durability):

- 一个事务一旦提交它对数据库的修改应该永久性的保存在数据库中,即当数据库发生故障时,确保已经提交的事务不能丢失.

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
