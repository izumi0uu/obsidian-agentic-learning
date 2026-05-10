---
type: map
topic:
  - agent
  - evaluation
  - observability
  - comparison
status: active
created: 2026-05-10
updated: 2026-05-10
source:
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
related:
  - "[[Agent 主题]]"
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Replay]]"
---

# Trajectory Trace 类型对比

这页专门回答：Trajectory、Trace、Reasoning Trace 到底差在哪里。

核心边界：Trajectory 是任务路径本身；Trace 是系统记录下来的过程数据；Reasoning Trace 是模型显式推理文字。三者经常一起出现，但不是同一层。

## 一张表先抓住

| 类型 | 核心含义 | 主要解决什么问题 | 最适合的场景 | 它不是什么 |
|---|---|---|---|---|
| [[Trajectory]] | Agent 实际走过的任务路径 | 理解一次任务是怎么成功或失败的 | 调试、复盘、训练数据、反思记忆 | 不是日志格式，也不只是推理文字 |
| [[Trace]] | 对 trajectory 的观测记录 | 把过程保存下来，便于调试、重放和评测 | observability、故障排查、成本/延迟分析 | 不是过程本身，也不是质量评分 |
| [[Reasoning Trace]] | 模型显式写出的推理文字 | 理解模型中间判断、计划和解释 | ReAct、调试推理错误、人工复盘 | 不是模型真实内心，也不是完整 trajectory |
| [[Trajectory Evaluation]] | 对行动路径进行评分 | 判断过程是否安全、合规、有效、经济 | Agent 评测、权限审计、工具调用质量检查 | 不是 trace 本身，也不是只看最终答案 |
| [[Replay]] | 用保存的记录重放过程 | 复现失败、比较修复前后行为 | 回归测试、线上故障定位、评测 harness | 不是新的任务执行策略 |

## 生活类比

把一次 Agent 任务想成“你从家出发去一家陌生餐厅吃饭”：

| Agent 概念 | 生活中的对应物 | 为什么这样类比 |
|---|---|---|
| [[Trajectory]] | 你真实走过的路线：出门、坐地铁、换乘、走错路、问路、最后到店 | 它是实际发生的行动路径，不管有没有被记录 |
| [[Trace]] | 手机地图的定位记录、地铁刷卡记录、聊天记录、付款记录 | 它是系统留下的可查看记录，可能完整，也可能漏掉某些细节 |
| [[Reasoning Trace]] | 你一路上的自言自语：“这条路堵，我换另一条”“这家店可能在二楼” | 它是显式想法，不等于所有行动，也不一定完全解释真实原因 |
| [[Trajectory Evaluation]] | 事后评价这趟行程：是否准时、是否绕路、是否安全、是否花太多钱 | 它不是记录本身，而是对这条路径好不好的判断 |
| [[Replay]] | 根据地图记录重新复盘：在哪站换错、哪里多走了十分钟 | 它用记录重现过程，帮助找问题 |

这个类比里最关键的一刀是：你走过的路是 trajectory；手机里留下的轨迹记录是 trace；你脑中或嘴上说出的理由只是 reasoning trace。

## 按问题选型

### 我想知道 Agent 到底怎么走到这个结果

看 [[Trajectory]]。

你关心的是完整路径：

```text
用户目标 -> 模型判断 -> 工具调用 -> Observation -> 状态变化 -> 下一步动作 -> 最终结果
```

### 我想调试系统，定位哪一步出错

看 [[Trace]]。

trace 应该告诉你：输入是什么、调用了哪个工具、参数是什么、工具返回什么、模型下一步做了什么、耗时和成本是多少。

### 我想理解模型为什么这么想

看 [[Reasoning Trace]]。

但要记住：它只是模型显式输出的推理文本，不一定等于模型内部真实原因，也不一定应该暴露给最终用户。

### 我想评价这个过程是不是好

看 [[Trajectory Evaluation]]。

一个 Agent 最终答对了，也可能中间越权访问、重复调用高成本工具、泄露数据，或者绕了很远的路才碰巧成功。

### 我想复现一次失败

看 [[Replay]]。

Replay 依赖 trace，但目标是重放过程，而不是只读日志。

## 最容易混淆的边界

- [[Trajectory]] vs [[Trace]]：前者是任务路径本身，后者是路径的记录。
- [[Trajectory]] vs [[Reasoning Trace]]：前者包含行动、观察、工具结果和状态变化；后者只是显式推理文字。
- [[Trace]] vs [[Audit Log]]：Trace 偏调试和观测，可能很细；Audit Log 偏合规和关键动作留痕。
- [[Trace]] vs [[Evaluation]]：Trace 记录发生了什么；Evaluation 判断好不好。
- [[Trajectory Evaluation]] vs final answer evaluation：前者评价过程，后者评价最终输出。

## 对我的学习建议

当前阶段可以这样背：

1. 先记一句：trajectory 是路线，trace 是路线记录，reasoning trace 是路上的想法。
2. 学 [[ReAct]] 时，看 `Thought -> Action -> Observation` 如何形成 trajectory。
3. 学 [[Reflexion]] 时，看 trajectory 如何进入 evaluator，再变成 reflection / experience。
4. 学 [[Observability]] 时，看 trace 如何支撑调试、重放和评测。
5. 学 [[Trajectory Evaluation]] 时，练习“不只看答没答对，还看过程是否安全和经济”。

## 相关链接

- [[Agent 主题]]
- [[Trajectory]]
- [[Trace]]
- [[Reasoning Trace]]
- [[Trajectory Evaluation]]
- [[Replay]]
- [[Observability]]
- [[Evaluation]]
