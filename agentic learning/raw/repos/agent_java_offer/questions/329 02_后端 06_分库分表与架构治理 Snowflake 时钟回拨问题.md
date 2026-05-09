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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/06_%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8%E4%B8%8E%E6%9E%B6%E6%9E%84%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/06_分库分表与架构治理/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "06_分库分表与架构治理"
last_checked: 2026-05-09
freshness: watch
sha256: 2bc80b30ccab6cdd0ed4176c142592bf069d8480ab01f6bbd95372aee2cff6db
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Snowflake 时钟回拨问题

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/06_分库分表与架构治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/06_%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8%E4%B8%8E%E6%9E%B6%E6%9E%84%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `06_分库分表与架构治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### Snowflake 时钟回拨问题

Snowflake 这类趋势递增 ID 方案强依赖机器时钟。如果机器和时间服务器校时后发生时钟回拨，就可能出现：
- 发号重复；
- 或者服务为了避免重复而短时间不可用。

一种工程化兜底思路是：
- 在内存里维护过去一段时间内（例如 1 小时）每一毫秒、每台机器已经发出的最大 ID；
- 如果检测到时钟回拨，就定位回拨到了之前的哪一毫秒；
- 然后在那一毫秒对应的最大序列号基础上继续自增，而不是直接重新从 0 开始发。

这样做的本质是：
**把“时间倒退”问题，转化成“同一毫秒内继续用更大的序列号发号”，从而降低重复 ID 风险。**

当然，工程上还可以结合：
- 小幅回拨时短暂等待；
- 大幅回拨时切换机器号 / 直接熔断告警；
- 结合监控观察时钟漂移和发号失败率。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
