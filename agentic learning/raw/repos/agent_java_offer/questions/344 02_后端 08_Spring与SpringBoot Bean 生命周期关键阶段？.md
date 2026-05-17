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
sha256: 905194481a8a42ccf5ca85bfe7a9f905db04dca7ff7529c5aa5004dc026e8bf4
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# Bean 生命周期关键阶段？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 1. Bean 生命周期关键阶段？

典型阶段是实例化、属性注入、`Aware` 回调、`BeanPostProcessor` 前后处理、初始化方法、容器销毁。理解这个顺序有助于定位初始化失败和增强逻辑失效问题。

1. 实例化（new 对象）

Spring 先通过构造器创建 Bean 实例，但这时依赖还没注入，功能还不完整。

1. 属性注入（依赖注入）

把 `@Autowired@Value` 等依赖和配置注入进来。  

1. BeanPostProcessor 前置处理

执行 `postProcessBeforeInitialization`。  

常用于通用增强、校验、字段处理。

1. 初始化阶段

按顺序可能触发：  

- `@PostConstruct`  
- `InitializingBean.afterPropertiesSet()`  
- 自定义 `init-method`

这一步通常做资源初始化、参数校验、缓存预热。

1. BeanPostProcessor 后置处理

执行 `postProcessAfterInitialization`。  

AOP 代理（事务、日志切面等）很多在这一步包装出来。  

所以你拿到的 Bean 可能已经是代理对象。

1. 运行期使用

Bean 正常参与业务调用。

1. 容器关闭 -> 销毁阶段

会触发：  

- `@PreDestroy`  
- `DisposableBean.destroy()`  
- 自定义 `destroy-method`

用于释放连接、线程池、文件句柄等资源。

一句话收口：  

Bean 生命周期本质是“创建 -> 注入 -> 增强 -> 初始化 -> 使用 -> 销毁”，AOP 和很多框架能力都挂在这个链路上。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
