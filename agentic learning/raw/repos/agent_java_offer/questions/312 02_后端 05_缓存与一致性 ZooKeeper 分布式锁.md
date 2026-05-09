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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/05_%E7%BC%93%E5%AD%98%E4%B8%8E%E4%B8%80%E8%87%B4%E6%80%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/05_缓存与一致性/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "05_缓存与一致性"
last_checked: 2026-05-09
freshness: watch
sha256: 89634b40ac2a82cc1b2588f639832407ddf505b96f89c3b227f3f2de03d8562e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# ZooKeeper 分布式锁

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/05_缓存与一致性/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/05_%E7%BC%93%E5%AD%98%E4%B8%8E%E4%B8%80%E8%87%B4%E6%80%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `05_缓存与一致性`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

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

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
