---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "mysql"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/01_MySQL/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "01_MySQL"
last_checked: 2026-05-09
freshness: watch
sha256: 0d45d284a4a02a981e7e5c158c09f28a109b6609975499e8d83fef030d0bfcaf
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# OLAP, HTAP, OLTP; 现在生产场景业内都用哪些比较有代表性的数据库呀？这些都简单介绍一下吧。

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/01_MySQL/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `01_MySQL`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 2. OLAP, HTAP, OLTP; 现在生产场景业内都用哪些比较有代表性的数据库呀？这些都简单介绍一下吧。

**1) OLTP（事务型）常见数据库**

1. `MySQL`：最主流，生态成熟，互联网业务默认选型。
2. `PostgreSQL`：功能强（SQL能力、扩展性好），复杂业务很常见。
3. `TiDB`：MySQL 协议 + 分布式扩展，适合大规模在线事务。
4. `OceanBase`：金融/运营商等高要求场景较多。
5. `SQL Server / Oracle`：传统企业核心系统仍大量使用。

**2) OLAP（分析型）常见数据库/数仓**

1. `ClickHouse`：高并发实时报表、日志分析非常常见。
2. `Doris`：实时分析+明细查询，一体化体验好。
3. `StarRocks`：面向实时分析和湖仓查询，近年增长快。
4. `Trino/Presto`：联邦查询引擎，常做多源分析。
5. `Snowflake / BigQuery / Redshift`：云上数仓代表。

**3) HTAP（混合事务分析）代表**

1. `TiDB`：TP+AP 一体（行列混合能力）。
2. `OceanBase`：也在强化 HTAP 能力。
3. `SingleStore`：海外常见 HTAP 选型。
4. `PostgreSQL + 扩展方案`：部分公司通过扩展和架构组合实现“准 HTAP”。

**怎么区分选型（面试可说）**

1. 交易核心链路：优先 `OLTP`（一致性和延迟优先）。
2. 经营分析/报表：优先 `OLAP`（扫描和聚合性能优先）。
3. 既要实时写又要近实时分析：考虑 `HTAP`，但要评估成本和复杂度。

一句话总结：  
`OLTP` 负责“稳交易”，`OLAP` 负责“快分析”，`HTAP` 负责“同库兼顾，但架构和治理更复杂”。

---

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
