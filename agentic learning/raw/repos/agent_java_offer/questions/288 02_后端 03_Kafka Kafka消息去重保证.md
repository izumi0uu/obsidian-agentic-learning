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
sha256: 9b4f9ab35e8ca97d96fcb35e062faaeb3f66d0469662b7519403c7533f3d1e34
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Durable Execution]]"
---

# Kafka消息去重保证

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/03_Kafka/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/03_Kafka/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `03_Kafka`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Durable Execution]]

## 题目正文

### 8.Kafka消息去重保证

Kafka 的“去重保证”要分三层理解。
第一层是生产端去重：开启 enable.idempotence=true，并配合 acks=all、合理重试，Kafka 会用生产者ID和序号在分区内去重，防止网络重试造成重复写入。
第二层是 Kafka 内部端到端一致：如果是“消费一条再生产一条”的链路，可用事务（transactional.id）加 read_committed，做到 Kafka 到 Kafka 的 Exactly-Once。
第三层是最容易被忽略的：一旦消费后要写数据库、发券、扣库存，Kafka 本身不能替业务系统去重，必须做业务幂等。常见做法是给每条消息带全局唯一 eventId，消费端落幂等表或用唯一索引（如订单号唯一），重复消息直接丢弃；并坚持“处理成功再提交 offset”。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
