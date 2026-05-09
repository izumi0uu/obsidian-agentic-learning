---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "spring"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "followup-question"
direction: "02_后端"
category: "08_Spring与SpringBoot"
last_checked: 2026-05-09
freshness: watch
sha256: c902586c26418ca167e9441828b0f6fbbefcd605bc0bb04c56a54929ce86222c
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 问题2：jdk为什么要选择在链表长度大于8且数组长度大于64的时候转为红黑树，而在红黑树元素小于6时重新回归链表，这里面为什么时8和6呢？不是12，16等其他数字？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`followup-question`  
父级题组：Hashmap相关
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

追问题目：问题2：jdk为什么要选择在链表长度大于8且数组长度大于64的时候转为红黑树，而在红黑树元素小于6时重新回归链表，这里面为什么时8和6呢？不是12，16等其他数字？

出现位置：Hashmap相关

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
