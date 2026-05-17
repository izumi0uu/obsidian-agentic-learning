---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - system-design
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/03_%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1/04_%E6%90%9C%E7%B4%A2%E6%8E%A8%E8%8D%90%E4%B8%8E%E8%81%8A%E5%A4%A9/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/03_系统设计/04_搜索推荐与聊天/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: supplement-section
direction: 03_系统设计
category: 04_搜索推荐与聊天
last_checked: 2026-05-09
freshness: watch
sha256: aa11d558c1f50ace2756da2a253231799abcd28fa256e51d7ef5fe585080a58c
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 补充原文：Elasticsearch 基础、查询与深分页

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/03_系统设计/04_搜索推荐与聊天/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/03_%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1/04_%E6%90%9C%E7%B4%A2%E6%8E%A8%E8%8D%90%E4%B8%8E%E8%81%8A%E5%A4%A9/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`03_系统设计` / `04_搜索推荐与聊天`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

## 补充原文：Elasticsearch 基础、查询与深分页

### 资料说明

- 本节内容来自个人面试资料的重组整理与公开资料归纳。
### 原文内容

#### 2.5.1 ES基础概念

ES 术语：
- `Index`：相当于数据库的 Table
- `Document`：相当于数据库的一行记录
- `Field`：相当于数据库的 Column
- `Mapping`：相当于数据库的 Schema
- `DSL`：相当于数据库的 SQL
- 中文分词器常用 IK

倒排索引：
- key 存储：ES 还有一层 `Term Index`，只存储部分词前缀，并常驻内存；在内存中通常以 `FST` 形式保存，节省内存。
- value 存储：`PostingList` 会用 `FOR` 压缩文档 ID，并用 `Roaring Bitmaps` 支持交并集运算。

#### 2.5.2 ES数据写入与查询

ES 数据写入：
- 协调节点负责路由。
- 数据先写内存缓冲区，每隔 1s 刷到文件系统缓存，所以 Query 是近实时的。
- 为防节点宕机，ES 还会写 `translog`，但 translog 落盘也有时间窗口，因此节点异常时存在短暂数据丢失风险。
- 主分片写成功后并行复制到副本，副本完成后返回 ack。

ES 查询：
- `Get`（按 ID 查）是实时的，会先查 translog；
- `Query`（按 query 匹配）是近实时的，主要查 segment。
- `QUERY_THEN_FETCH` 分两阶段：
  - Query Phase：每个分片先返回局部 topN doc id；
  - Fetch Phase：协调节点合并排序后，再向目标分片拉取完整文档。

#### 2.5.4 ES深分页

ES 深分页的问题本质是：每个分片都要先返回 `from + size` 条候选，再由协调节点做全局合并排序，页数越深，排序和内存成本越高。

常见解法：
- 业务上限制最大页数；
- `from/size` 只用于浅分页；
- 批处理任务用 `scroll`；
- 实时高并发深翻页用 `search_after`，用上一页最后一条记录作为游标。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
