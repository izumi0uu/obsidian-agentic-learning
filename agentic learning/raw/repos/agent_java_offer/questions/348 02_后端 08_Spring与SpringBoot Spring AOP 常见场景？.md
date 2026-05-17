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
sha256: 9842cc19a5e243437755565e54e81b4ee3470b8d0c71a8486e985f7cc09c0755
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
---

# Spring AOP 常见场景？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Audit Log]]
- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]

## 题目正文

### 5. Spring AOP 常见场景？

**一、Spring AOP 常见场景**

1. 日志与链路追踪

统一记录接口入参、耗时、[[Trace|traceId]]，不污染业务代码。统计方法 RT、[[Task Success Rate|成功率]]、异常率，上报 Prometheus 等[[Observability|监控]]系统。

1. 事务管理

`@Transactional` 本质就是 AOP 在方法前后做事务开启/提交/回滚。

1. 权限与鉴权

在 Controller/Service 入口做统一权限校验，失败直接拦截。

1. [[Audit Log|审计与合规]]

对敏感操作统一留痕（谁在什么时候做了什么）。

**二、AOP 实现原理（面试重点）**

1. 核心思想

Spring 给目标对象“套代理”，调用先进入代理，再执行切面逻辑，最后再调用目标方法。

1. 关键概念

- `JoinPoint`：可被拦截的位置（Spring 里主要是方法执行）  
- `Pointcut`：匹配哪些方法  
- `Advice`：增强逻辑（Before/After/Around/AfterThrowing）

1. 代理方式

- 有接口：默认常用 JDK 动态代理（基于接口）  
- 无接口：用 CGLIB 生成子类代理

（Spring Boot 里很多场景会走 CGLIB）

1. 执行链路（最常考）

外部调用 -> 代理对象 -> 拦截器链（多个 Advice） -> 目标方法 -> 返回/异常处理。  

`@Around` 可以决定是否继续执行目标方法`proceed()`）。

一句话收口：  

Spring AOP 是“代理 + 拦截器链”机制，把日志、事务、鉴权等横切能力从业务代码里抽出来统一治理。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
