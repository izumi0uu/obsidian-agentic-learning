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
sha256: a84fdc0d16a604a30bc1b6706d308dfacd2e9b16a5a908550f7efc9704ff5fc0
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# `ApplicationContext` 与 `BeanFactory` 区别？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 6. `ApplicationContext` 与 `BeanFactory` 区别？

`

1. 定位区别`

`- BeanFactory：最底层 IOC 容器接口，核心是“注册、获取、管理 Bean”。`  

`- ApplicationContext：在 BeanFactory 之上的完整企业容器，功能更全。`

`

1. 功能区别`

`BeanFactory 主要有：`  

`- 依赖注入`  

`- Bean 生命周期管理`  

`- 基础作用域支持`

`ApplicationContext 额外提供：`  

`- 国际化MessageSource）`  

`- 事件发布/监听ApplicationEventPublisher）`  

`- 资源加载ResourceLoader）`  

`- 环境与配置体系Environment）`  

`- 自动注册 BeanPostProcessor，更好集成 AOP、事务等`

`

1. Bean 加载时机（常考）`

`- BeanFactory：偏延迟加载（getBean 时才创建）。`  

`- ApplicationContext：默认容器启动时预实例化单例 Bean。`  

`这使得 ApplicationContext 启动更“重”，但错误能更早暴露。`

`

1. 为什么生产几乎都用 ApplicationContext`

`因为现代 Spring 应用要用到事件、配置、AOP、事务、自动装配等能力ApplicationContext 开箱即用，开发和治理成本更低。`

`

1. 一句话总结`

`BeanFactory 是“能用的最小容器”ApplicationContext 是“企业级完整容器”；实际项目默认选 ApplicationContext。`

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
