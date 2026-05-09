---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "kafka"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/03_Kafka/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/03_Kafka/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "03_Kafka"
last_checked: 2026-05-09
freshness: watch
sha256: 57701b85b412d0ad77caeb0aaf2289c1d9acbbe2417d71bf77902d7fee37cf83
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Kafka为什么高性能

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/03_Kafka/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/03_Kafka/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `03_Kafka`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 9.Kafka为什么高性能

主要是在持久化的那个性能做了一些优化。
1.顺序写磁盘：避免随机 I/O，吞吐远高于随机写。
2.Page Cache：大量读写走操作系统缓存，减少磁盘真实访问。
3.零拷贝（sendfile/transferTo）：数据从内核缓存直接到网卡，减少用户态拷贝和 CPU 开销。
4.批量处理：生产端批量发送、Broker 批量落盘、消费端批量拉取，显著降低系统调用次数。


<a id="toc-jvm-gc"></a>

## 补充原文：Kafka 高可用、重复消费与顺序性

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
