---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - mysql
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/01_MySQL/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: supplement-section
direction: 02_后端
category: 01_MySQL
last_checked: 2026-05-09
freshness: watch
sha256: 84a79046909f2beab57c6a710b48fca04ad085c8a225178ac3a0342a7efef42d
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 补充原文：MySQL 深分页

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/01_MySQL/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `01_MySQL`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

## 13. 补充原文：MySQL 深分页

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

#### 2.6.1 MySQL深分页

MySQL 的深分页：
- 执行流程：
  1. 通过普通二级索引树 `idx_update_time`，过滤 `update_time` 条件，找到满足条件的记录 ID。
  2. 通过 ID，回到主键索引树，找到满足记录的行，然后取出展示的列（回表）。
  3. 扫描满足条件的 `100010` 行，然后扔掉前 `100000` 行，返回结果。
- 变慢原因：
  - `limit` 语句会先扫描 `offset + n` 行，然后再丢弃掉前 `offset` 行，返回后 `n` 行数据。也就是说 `limit 100000,10` 会扫描 `100010` 行，而 `limit 0,10` 只扫描 `10` 行。
  - `limit 100000,10` 扫描更多的行数，也意味着回表更多的次数。
- 解法：
  - 通过子查询优化，先根据 `update_time` 条件找到主键 ID，同时把 `limit 100000` 也转移到子查询中，然后再根据主键 ID 回表查具体字段。
  - 示例：`select id,name,balance from account where id >= (select a.id from account a where a.update_time >= '2020-09-19' limit 100000, 1) limit 10;`

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
