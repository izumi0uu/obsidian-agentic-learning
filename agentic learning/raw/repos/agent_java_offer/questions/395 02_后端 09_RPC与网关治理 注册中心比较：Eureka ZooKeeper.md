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
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 09_RPC与网关治理
last_checked: 2026-05-09
freshness: watch
sha256: bcb17ca82ebe646e6f1517c5145f68e6ea2f23b7f7fb3e8396aed11b4ae1a2cc
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 注册中心比较：Eureka / ZooKeeper

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `09_RPC与网关治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 注册中心比较：Eureka / ZooKeeper

1. **ZooKeeper**
- 偏 `CP`，强调一致性；
- 服务列表变更可通过 watcher 快速通知客户端；
- 缺点是服务实例很多时，推送压力会很大。

2. **Eureka**
- 偏 `AP`，优先保证可用；
- 节点间 peer 同步，消费者周期性拉取注册表；
- 默认配置下变更感知偏慢，但可通过缩短缓存同步、心跳和拉取周期来优化。

3. **大规模注册中心优化思路**
- 服务注册表做分片存储；
- 节点主从备份，保证高可用；
- 消费者通过代理层按需拉取部分注册信息；
- 避免所有节点保存全量数据导致同步风暴。

## 补充原文：网关选型与职责

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
