---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "redis"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/02_Redis/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "supplement-section"
direction: "02_后端"
category: "02_Redis"
last_checked: 2026-05-09
freshness: watch
sha256: d53f85f50e1a7a990f154168f773c215cef9d6cd391f57e84784d00e10d855b4
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 补充原文：Redis 限流实现

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/02_Redis/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `02_Redis`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

## 15. 补充原文：Redis 限流实现

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

#### 2.7.2 Redis限流实现

Redis 实现限流：
- 基于 `zset` 实现：限流最核心的是滑动窗口。可以把每次请求都写入一个 `zset`，其中 `value` 保持唯一（可用 UUID 生成），`score` 使用当前时间戳。
- 判断当前时间窗口内的请求数时，只需要统计两个时间戳之间的元素数量。
- 这种方案的优点是窗口平滑、精度高，适合做“最近 N 秒最多允许 M 次请求”的限流规则。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
