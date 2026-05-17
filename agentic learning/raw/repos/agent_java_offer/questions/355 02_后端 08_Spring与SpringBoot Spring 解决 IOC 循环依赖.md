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
sha256: 3b03c0a1c762512328ec34026955054d541a69480de0abb8230c517bf5143c4d
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Spring 解决 IOC 循环依赖?

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 10.Spring 解决 IOC 循环依赖?

Spring 解决 IOC 循环依赖，核心是 **“三级缓存 + 提前暴露对象引用”**，但主要只对 **单例 + setter/字段注入** 生效。

1. 三个缓存

- `singletonObjects`：一级缓存，完整初始化好的单例。  
- `earlySingletonObjects`：二级缓存，提前暴露的“早期对象”。  
- `singletonFactories`：三级缓存，能生成早期引用的工厂（关键用于 AOP 代理）。

1. 典型流程（A 依赖 B，B 依赖 A）

- 创建 A（先实例化，还没注入）  
- 把 A 的 `ObjectFactory` 放入三级缓存  
- A 注入 B，触发创建 B  
- B 注入 A 时，从三级缓存拿到 A 的早期引用（必要时是代理）  
- B 完成初始化进一级缓存  
- 回到 A，注入 B，A 完成初始化进一级缓存

1. 为什么要三级缓存

二级缓存只能放“对象”，三级缓存能“按需生成早期引用”，这样可以保证 AOP 场景下注入的是正确代理对象，而不是原始对象。

1. 实战建议

优先改设计解耦；必要时用 `@Lazy`、`ObjectProvider`、中间服务拆分来打断依赖环。

<a id="toc-distributed-design"></a>

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
