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
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/05_%E7%BC%93%E5%AD%98%E4%B8%8E%E4%B8%80%E8%87%B4%E6%80%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/05_缓存与一致性/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: supplement-section
direction: 02_后端
category: 05_缓存与一致性
last_checked: 2026-05-09
freshness: watch
sha256: dc0e93989ec23394c15f380aef2b18b9466adbff99d77b3da298393085f872f8
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 补充原文：Redis / ZooKeeper 分布式锁与高并发优化

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/05_缓存与一致性/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/05_%E7%BC%93%E5%AD%98%E4%B8%8E%E4%B8%80%E8%87%B4%E6%80%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `05_缓存与一致性`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

## 补充原文：Redis / ZooKeeper 分布式锁与高并发优化

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

### Redis 最普通的分布式锁

最常见的 Redis 分布式锁写法是：

```redis
SET key my_random_value NX PX 30000
```

含义：
- `NX`：只有 key 不存在时才能设置成功；
- `PX 30000`：设置 30 秒自动过期，防止死锁。

释放锁时不能直接 `DEL key`，而是要比对 value 后再删，通常用 Lua 做原子校验：

```lua
if redis.call("get",KEYS[1]) == ARGV[1] then
    return redis.call("del",KEYS[1])
else
    return 0
end
```

这里要用 `random_value` 的原因是：
- 客户端 A 拿到锁后如果卡了很久，锁可能已经过期并被客户端 B 重新拿到；
- 如果 A 醒来后直接删 key，就会把 B 的锁误删掉；
- 所以必须用“值匹配 + Lua”保证只删除自己的锁。

但这种最原始实现也有明显问题：
- Redis 单实例会有单点风险；
- 主从异步复制下，如果主节点挂了而锁还没同步到从节点，新主节点可能再次把锁发给别人，产生双持锁问题。

### Redisson 的价值

Redisson 在工程上更常用，因为它补齐了很多手写锁的坑：
- 支持单机、哨兵、Cluster、主从等多种部署；
- 加锁解锁逻辑封装在 Lua 里，天然原子；
- 支持可重入；
- 有 watchdog 自动续期，避免业务没执行完锁就先过期；
- 提供更完整的锁模型和更成熟的工程实现。

### ZooKeeper 分布式锁

ZooKeeper 的锁思路和 Redis 不一样，常见做法是基于**临时顺序节点**：
1. 客户端在某个锁目录下创建临时顺序节点；
2. 如果自己是最小节点，说明拿到锁；
3. 如果不是最小节点，就监听排在自己前面的那个节点；
4. 前驱节点删除后，再尝试拿锁。

这种做法的优点：
- 客户端挂掉后，临时节点会自动删除，锁自动释放；
- 通过监听前驱节点而不是监听锁根节点，可以减少羊群效应；
- 更容易实现公平锁语义。

### Redis 锁 vs ZooKeeper 锁

两者各有取舍：
- Redis 锁性能高，实现轻，适合高频短锁，但底层复制一致性要格外注意；
- ZooKeeper 锁一致性更强、自动释放更自然，但性能和复杂度成本更高；
- 如果业务是高并发热点资源竞争，很多时候更好的方向不是“把锁做得更重”，而是先从业务上拆分资源、降低热点。

### 分布式锁抗高并发

如果一个热点资源每秒有上万请求去抢同一把锁，单把锁会成为瓶颈。常见优化思路是：
- **分段加锁**：把一个大资源拆成多个小分段，每个分段独立加锁；
- **合并扣减**：一个分段不够时，再去锁别的分段做组合扣减；
- **实在极端高并发时，尽量往无锁化演进**：例如直接在 Redis / Tair 这类 KV 里原子扣减，再通过 MQ 异步回写关系型数据库，而不是让所有请求都先抢一把重锁。

面试里可以一句话总结：
**分布式锁是兜底手段，不是高并发系统的首选主路径；能拆热点、能异步、能原子扣减，就尽量不要把吞吐压在一把锁上。**

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
