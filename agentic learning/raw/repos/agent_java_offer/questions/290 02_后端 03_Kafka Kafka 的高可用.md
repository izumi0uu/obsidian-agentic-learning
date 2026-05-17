---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - kafka
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/03_Kafka/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/03_Kafka/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 03_Kafka
last_checked: 2026-05-09
freshness: watch
sha256: 0d277e832e89486df21ed8699f58003b569771b71d448c9e8f84c562a08c2692
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Kafka 的高可用

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/03_Kafka/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/03_Kafka/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `03_Kafka`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

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

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
