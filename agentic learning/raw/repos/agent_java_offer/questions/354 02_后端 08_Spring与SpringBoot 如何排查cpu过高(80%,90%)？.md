---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - spring
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 08_Spring与SpringBoot
last_checked: 2026-05-09
freshness: watch
sha256: f3ad151d185111d6683a33d708d30bf15bd55234d565263a9b9ab4bcb9f624d4
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 如何排查cpu过高(80%,90%)？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 9.如何排查cpu过高(80%,90%)？

top -c 查看所有的进程
在1的基础上键入P让cpu从高到底排序
选择2中cpu占比最高的pid进程
top -Hp pid 查看pid对应的线程对cpu的占比
在4的页面键入P让当前pid的线程cpu占比从高到低排序
获取第5步骤中的线程占比最高的线程id,由于linux打印的id是16进制的
将第6的线程id十六进制转为10进制 print "%xn" tid
打印指定pid下指定tid的jstack日志,jstack pid | grep tid -C 10 --color
根据堆栈信息找到代码块

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
