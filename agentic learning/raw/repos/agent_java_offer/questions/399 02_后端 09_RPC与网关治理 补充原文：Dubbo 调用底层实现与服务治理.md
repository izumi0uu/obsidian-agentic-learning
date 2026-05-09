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
sha256: caa72360e8c48403797a893d469ac3df80b507d99af69e1250f14e6fee23ddf1
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Durable Execution]]"
---

# 补充原文：Dubbo 调用底层实现与服务治理

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/09_RPC与网关治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/09_RPC%E4%B8%8E%E7%BD%91%E5%85%B3%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `09_RPC与网关治理`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Durable Execution]]

## 题目正文

## 补充原文：Dubbo 调用底层实现与服务治理

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

### Dubbo调用底层实现

消费者侧通常会经历这些层次：
1. **动态代理**：调用方面向接口编程，底层通过代理对象拦截方法调用。
2. **负载均衡**：从服务列表里选一台机器，例如 random、consistent hash 等策略。
3. **协议层**：决定走 dubbo / rmi / hessian / http 等协议。
4. **网络通信**：底层常基于 Netty / Mina 做 NIO 异步通信。
5. **序列化**：把请求编码成二进制后发出去。

服务端则做反序列化、协议解析、网络收包，再通过代理调到真正的本地服务实现。

Dubbo 常见集群容错策略：
- `failover`：失败自动切换并重试，常用于读操作；
- `failfast`：失败立刻返回，常用于非幂等写操作；
- `failsafe`：失败忽略，适合日志这类非关键调用；
- `failback`：失败后后台重发，适合消息通知类；
- `forking`：并行调用多个 provider，一个成功就返回，换时延但更耗资源。

Dubbo 的 SPI 机制本质是：运行时按配置动态装配接口实现类。比如协议、序列化、代理、负载均衡这些扩展点，都可以通过 SPI 替换。

服务治理重点：
- 自动生成调用链路；
- 统计访问量、时长、可用率；
- 监控失败率并报警；
- 做服务分层，避免循环依赖；
- 配置超时、重试和降级策略。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
