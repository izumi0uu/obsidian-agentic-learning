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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "09_RPC与网关治理"
last_checked: 2026-05-09
freshness: watch
sha256: b32a546b8a9b671b739a6385113b384d96c924980dcc03d7ed14530ea8eb3db2
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# ZooKeeper

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `09_RPC与网关治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

### ZooKeeper

ZooKeeper 是典型的分布式协调系统，常见用途包括：
- 分布式锁；
- 集群元数据存储；
- Master 选举；
- 分布式协调与通知。

集群角色通常有三种：
- `Leader`：负责写；
- `Follower`：同步数据并提供读；
- `Observer`：只读，不参与选举。

客户端和 ZooKeeper 之间会建立 TCP 长连接，也就是一个 `session`。只要客户端在 `sessionTimeout` 内重新连回任一台 ZK 节点，就可以延续原来的 session；否则临时节点会失效。

ZK 的数据模型是 `znode` 树：
- **持久节点**：适合放元数据；
- **临时节点**：连接断开就消失，适合分布式锁、服务在线状态、协调通知。

Watcher 是 ZK 非常核心的能力：客户端可以对 znode 注册监听，节点变化时收到回调通知。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
