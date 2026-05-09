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
entry_type: "supplement-section"
direction: "02_后端"
category: "03_Kafka"
last_checked: 2026-05-09
freshness: watch
sha256: 71a2dbf1811087d02787737411ba4e45ea8b544eb1d269bc1955b244aabdddfa
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Durable Execution]]"
---

# 补充原文：Kafka 高可用、重复消费与顺序性

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/03_Kafka/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/03_Kafka/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `03_Kafka`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Durable Execution]]

## 题目正文

## 补充原文：Kafka 高可用、重复消费与顺序性

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

### Kafka 的高可用

Kafka 是分布式的，topic 会被拆成多个 partition，分布在不同机器上。每个 partition 会有一个 leader 和多个 follower：
- 生产者只向 leader 写；
- follower 主动从 leader 拉数据；
- leader 宕机后，follower 中会重新选出新的 leader，继续提供服务。

写入流程可以这么理解：
1. 生产者把消息发给 leader；
2. leader 先写本地磁盘；
3. follower 从 leader 同步数据；
4. 当满足副本确认条件后，leader 才给生产者返回 ack。

如果要尽量避免 broker 故障导致的数据丢失，常见配置是：
- `replication.factor > 1`
- `min.insync.replicas > 1`
- `acks=all`
- `retries` 设为足够大

这套配置的核心思想是：**至少要有多个副本真正跟上，并且所有必要副本确认后，才把消息视为写成功。**

### 重复消费与幂等

Kafka 消费端可能重复消费，本质原因是：
- 业务已经处理成功；
- 但 offset 还没来得及提交；
- 消费者重启后又会从旧 offset 再拉一次。

所以常见工程做法是：
- 关闭自动提交 offset；
- 处理成功后手动提交；
- 同时在业务层做幂等。

业务幂等常见做法：
- 用数据库唯一键防重；
- 或者用 Redis / 内存 Set 做去重判断。

### Kafka 如何保障不丢消息

1. **生产端**
- 要拿到 broker 的成功确认；
- 失败时要自动重试。

2. **Broker 端**
- 做持久化和多副本复制；
- leader 切换时只从满足同步条件的副本中选举。

3. **消费端**
- 处理成功再提交 offset；
- 失败时允许重试，但业务必须幂等。

### Kafka 如何保证顺序性

Kafka 的顺序性是“分区内有序，不是全局有序”。
常见做法是：
- 生产时按业务 key（如订单 ID）路由到同一个 partition；
- 消费时避免同一个 key 被多个线程并发打乱；
- 如果消费者内部多线程处理，可再按 key hash 到本地内存队列，由单线程顺序消费。

所以面试里可以一句话总结：
**Kafka 能保证同一 partition 内的消息顺序；要把业务顺序映射到 Kafka 顺序，关键是分区键设计和消费端串行处理。**

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
