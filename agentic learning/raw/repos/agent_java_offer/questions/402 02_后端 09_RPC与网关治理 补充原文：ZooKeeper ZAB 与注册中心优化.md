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
entry_type: "supplement-section"
direction: "02_后端"
category: "09_RPC与网关治理"
last_checked: 2026-05-09
freshness: watch
sha256: 65ff59a795fa7b0c461a972ba5766be8801011c587926fa11a7fcc23774a8c91
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# 补充原文：ZooKeeper / ZAB 与注册中心优化

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `09_RPC与网关治理`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

## 补充原文：ZooKeeper / ZAB 与注册中心优化

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

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

### ZAB 协议

ZAB（ZooKeeper Atomic Broadcast）可以理解成“带顺序保证的主从同步协议”：
- Leader 收到事务请求后，先写本地日志；
- 再把事务 proposal 按顺序同步给 follower；
- follower 先写磁盘日志，再返回 ack；
- Leader 收到过半 ack 后发出 commit；
- follower 收到 commit 后才真正让新数据可见。

这里的关键点：
- proposal 会带全局递增的 `zxid`，保证顺序；
- 采用过半写机制；
- Leader 崩溃后，只要超过半数节点存活，就能重新选主并恢复服务。

从一致性角度看，ZooKeeper 不是“严格强一致”，更准确地说是**顺序一致性优先、最终收敛**。如果业务强依赖强一致读，可以主动调用 `sync()`。

### 注册中心选型与优化

1. **ZooKeeper vs Eureka**
- ZK 偏 `CP`，一致性更强、变更感知快；
- Eureka 偏 `AP`，可用性更强，但默认感知较慢；
- Eureka 可以通过缩短缓存同步、心跳、拉取周期来把感知延迟从几十秒压到几秒。

2. **大规模注册中心优化**
当服务实例规模上万时，常见优化思路是：
- 注册表做分片存储，不让每台机器存全集；
- 每个分片再做主从备份保证高可用；
- 消费者通过代理层按需拉取局部注册信息；
- 避免每次变更都在全集上广播和同步。

3. **Redis 能不能当注册中心**
可以，但更像工程折中方案：
- Provider 把实例信息写到 Redis Hash，并设置 TTL；
- 周期性刷新过期时间作为心跳；
- Consumer 周期性扫描服务前缀拉取列表；
- 多集群部署时再通过路由逻辑分摊写入和读取压力。

适合轻量级、内部可控场景；如果要求强一致注册发现和丰富 watcher 语义，ZooKeeper / etcd 仍然更标准。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
