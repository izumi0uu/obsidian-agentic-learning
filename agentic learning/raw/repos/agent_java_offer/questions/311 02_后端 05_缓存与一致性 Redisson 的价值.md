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
entry_type: question
direction: 02_后端
category: 05_缓存与一致性
last_checked: 2026-05-09
freshness: watch
sha256: d9f2985cfc012c42470d9f83b5a799d72be7dec7f2ec996b106f99b345a81c25
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Redisson 的价值

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/05_缓存与一致性/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/05_%E7%BC%93%E5%AD%98%E4%B8%8E%E4%B8%80%E8%87%B4%E6%80%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `05_缓存与一致性`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### Redisson 的价值

Redisson 在工程上更常用，因为它补齐了很多手写锁的坑：
- 支持单机、哨兵、Cluster、主从等多种部署；
- 加锁解锁逻辑封装在 Lua 里，天然原子；
- 支持可重入；
- 有 watchdog 自动续期，避免业务没执行完锁就先过期；
- 提供更完整的锁模型和更成熟的工程实现。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
