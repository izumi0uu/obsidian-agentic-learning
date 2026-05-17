---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - redis
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/02_Redis/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 02_Redis
last_checked: 2026-05-09
freshness: watch
sha256: 45d409e86fc020e424a24048e91ee0b05313c2c8f58e5d894f853ae5d204f95f
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# redis中的数据类型, 用于计数的HyperLogLog , 用于支持存储地理位置信息的Geo.

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/02_Redis/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/02_Redis/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `02_Redis`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 2. redis中的数据类型, 用于计数的HyperLogLog , 用于支持存储地理位置信息的Geo.

1. `HyperLogLog`（去重计数）

- 作用：做“基数统计”，比如 UV、独立设备数，结果是近似值。
- 优势：内存非常省（每个 key 大约固定 12KB），适合海量去重计数。
- 代价：有误差（标准误差约 `0.81%`），不能拿来做精确计费。
- 常用命令：`PFADD`、`PFCOUNT`、`PFMERGE`。

1. `Geo`（地理位置）

- 作用：存经纬度并做“附近的人/店/骑手”查询。
- 底层：基于 `Sorted Set` + `GeoHash` 编码。
- 常用命令：`GEOADD`、`GEODIST`、`GEOSEARCH`（新版推荐）。
- 场景：外卖附近商家、打车最近司机、门店距离排序。

面试一句话：
`HyperLogLog` 解决“海量去重计数省内存”，`Geo` 解决“经纬度存储和附近检索”。前者重统计，后者重空间查询。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
