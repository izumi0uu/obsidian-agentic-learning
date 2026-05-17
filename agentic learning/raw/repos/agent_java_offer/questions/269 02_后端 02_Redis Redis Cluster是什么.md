---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - redis
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/02_Redis/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 02_Redis
last_checked: 2026-05-09
freshness: watch
sha256: 858f7b1922cfb91ac88f89d4716c3bb613c84ebcd38b56bbb7ba6be326bd45f2
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Redis Cluster是什么

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/02_Redis/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `02_Redis`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 5. Redis Cluster是什么

Redis Cluster 是 Redis 官方的分布式方案，核心目标是同时解决横向扩容和高可用, 更适合大数据量和高并发场景. 将不同的key通过某个规则分散存储在多个redis节点上,即数据分片.redis-client采用无中心结构,每个节点都和其他节点连接,采用Gossip协议传播信息和发现新的节点.

如何将不同的key均匀放在不同的redis集群节点? 
一致性哈希算法: 对2^32取模,将哈希值空间组成虚拟的圆环.按顺时针组织,选用服务的ip或者主机名作为关键字,来进行hash,来确定每台服务器在hash环上的位置, key 顺时针找到第一个节点作为归属, 新增或下线一个节点时，只影响它相邻区间的数据，迁移量显著降低. 
哈希环的数据倾斜问题:在节点很少时会因为节点分布不均匀而造成大量数据集中缓存到某一台服务器上, 为每台服务器计算虚拟节点,均匀分布到环上,多了一步虚拟节点到实体节点的映射,数据定位算法不变.这样相对较少的数据节点也能实现数据的均匀分布.实际应用中将虚拟节点设置为32.

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
