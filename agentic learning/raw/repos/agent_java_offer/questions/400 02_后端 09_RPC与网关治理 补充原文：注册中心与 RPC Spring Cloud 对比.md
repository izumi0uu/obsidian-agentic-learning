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
entry_type: supplement-section
direction: 02_后端
category: 09_RPC与网关治理
last_checked: 2026-05-09
freshness: watch
sha256: 34c34f669d547d190a2d7936f23fac278608365b90c4e80589dc8abb7e3b3053
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
---

# 补充原文：注册中心与 RPC / Spring Cloud 对比

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `09_RPC与网关治理`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent Loop]]
- [[Agent]]

## 题目正文

## 补充原文：注册中心与 RPC / Spring Cloud 对比

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

### 如何设计一个 RPC 框架

最小闭环通常包括：
1. **动态代理**：把本地接口调用代理成远程调用；
2. **注册中心**：保存服务注册信息，并支持服务发现；
3. **负载均衡**：从多个 provider 中选路；
4. **协议与序列化**：定义请求格式和编解码；
5. **网络通信框架**：通常用 Netty 实现高并发连接处理。

### Dubbo 和 Spring Cloud 的差异

- Dubbo 更偏 **高性能 RPC 框架**，基于 TCP，调用更轻量；
- Spring Cloud 更偏 **整套分布式系统解决方案**，组件更全，和 Spring 生态结合更深；
- 关键差异在于：一个偏“RPC 框架”，一个偏“治理生态 + HTTP 体系”。

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

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
