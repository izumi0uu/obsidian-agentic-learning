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
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/10_%E7%BD%91%E7%BB%9CI_O%E4%B8%8E%E5%8F%91%E5%B8%83%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/10_网络I_O与发布治理/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 10_网络I_O与发布治理
last_checked: 2026-05-09
freshness: watch
sha256: 6d8ad605417816c5dcd9730cce5cd9c25c8950b9afab412e589d00cc8d601ef6
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Netty 如何体现 Reactor 模型？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/10_网络I_O与发布治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/10_%E7%BD%91%E7%BB%9CI_O%E4%B8%8E%E5%8F%91%E5%B8%83%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `10_网络I_O与发布治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki


## 题目正文

### 3. 问：Netty 如何体现 Reactor 模型？

答：Netty 通常采用主从 Reactor：Boss 线程负责 accept，新连接分配给 Worker 线程处理读写事件。业务处理可再下沉到业务线程池，避免 I/O 线程被阻塞。这样实现了连接管理和业务计算解耦。  
追问：如果在 I/O 线程里做重计算，会出现什么线上表现？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
