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
sha256: 196f6f89daeef6aaa63cf7e9a0044ddde078cab239dbe477d910055d7625bca6
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# mmap 与 sendfile / 零拷贝

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/10_网络I_O与发布治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/10_%E7%BD%91%E7%BB%9CI_O%E4%B8%8E%E5%8F%91%E5%B8%83%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `10_网络I_O与发布治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### mmap 与 sendfile / 零拷贝

普通 I/O 读取磁盘文件再发网络，通常涉及：
- 用户态/内核态多次切换；
- 内核缓冲区 -> 用户缓冲区 -> Socket 缓冲区的多次拷贝。

`mmap` 的核心是把内核缓冲区和用户缓冲区建立映射，减少一次数据拷贝。

`sendfile` 的核心是：
- 数据从磁盘到内核缓冲区；
- 再直接从内核缓冲区交给网卡发送；
- 省掉“先拷到用户态再写回内核”的过程。

所以 Kafka、Tomcat 这类高吞吐系统会大量利用零拷贝来降低上下文切换和 CPU 拷贝成本。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
