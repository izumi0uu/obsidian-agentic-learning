---
type: concept
topic:
  - coding-agent
  - evaluation
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[SWE-bench]]"
evidence:
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Coding Agent]]"
  - "[[Evaluation]]"
  - "[[Agent Harness]]"
---

# Patch Validation

## 一句话

Patch Validation 是验证代码修改是否真正解决问题且没有破坏旧功能的过程。

## 概念详解

Patch Validation 是 coding agent 可靠性的核心环节。LLM 生成 patch 的能力很强，但 patch 是否能应用、能运行、能通过测试、能覆盖真实 bug、有没有引入回归，必须由验证流程证明。它把“看起来像正确代码”的主观判断，转成可执行证据。

在最小形态里，Patch Validation 包括应用 patch、安装依赖、运行相关测试、运行 lint/typecheck/build、检查 diff 范围，并阅读失败输出。更完整的 harness 还会复现原始 bug、确认修复前失败修复后通过、收集 trace、保存日志、隔离 sandbox、限制副作用，并把失败案例加入回归集。

它和 [[SWE-bench]] 的关系很直接：SWE-bench 用真实 issue 和测试结果判断 patch 是否 resolved。对日常 coding agent 来说，SWE-bench 是 benchmark；Patch Validation 是每次修改后都应该执行的工程纪律。


Patch Validation 还包含一个常被忽略的时间顺序：先理解目标失败，再证明修改改变了失败结果。最强证据是“修改前失败、修改后通过”的同一测试；次强证据是针对修改点的新测试和相关旧测试；最弱证据是只运行格式化或只人工扫 diff。Coding agent 的最终报告应该清楚说明自己拿到了哪一级证据。

在团队协作里，它也是边界控制机制。Agent 不应该为了让验证通过而扩大修改范围、跳过失败测试、删除断言或改变无关行为。验证失败时，正确动作是读输出、定位原因、最小修复、重跑，而不是把失败当作噪声。

## 它解决什么问题

LLM 生成的代码可能能读，但不一定能运行。Patch Validation 用测试、lint、typecheck 或人工审查来检查 patch 是否有效。

它还防止“修一个 bug 破三个功能”：没有回归验证，Agent 很容易只对当前错误日志过拟合。

## 它不是什么

Patch Validation 不只是“代码看起来对”。

它也不保证没有隐藏 bug。测试覆盖不足时，patch 通过测试仍可能有问题。

Patch Validation 也不是单纯跑全量测试。全量测试有价值，但还要知道验证目标是什么、失败是否相关、是否真的覆盖了修改行为。

## 最小例子

SWE-bench 把模型生成的 patch 应用到 repo，然后运行相关测试。测试通过才算 resolved。

日常最小流程可以是：

```text
reproduce failing test -> apply patch -> run targeted test -> run lint/typecheck -> inspect diff
```

如果无法复现原始失败，至少要说明验证缺口，并用最接近的测试或静态检查补证据。

## 常见误解 / 风险

- 只跑“容易过”的测试：没有覆盖修改点，不能证明修复。
- 测试通过就绝对正确：测试集可能缺边界、mock 可能太宽、环境可能和生产不同。
- 忽略失败输出：有时测试失败暴露的是真实回归，不是“环境问题”。
- 为了过测试改测试：除非需求就是更新预期，否则这是危险信号。

## 边界细节

Patch Validation 至少要切开三件事：

1. Correctness：patch 是否解决目标问题。
2. Regression：相关旧功能是否仍然正常。
3. Integration：代码是否符合类型、lint、构建和运行环境约束。

它和 [[Eval Harness]] 的关系：harness 可以自动化 patch validation，把 issue、repo、测试命令、日志和结果组织成可重复任务；patch validation 是其中针对代码修改的一类 evaluator。

它和 [[Trace]] 的关系：trace 记录 Agent 为什么改、改了哪些文件、运行了哪些测试、失败后怎么迭代；patch validation 的判定仍来自测试、静态分析、review 或人工验收。

## 现代性状态

- 判定：current-practice。
- 为什么：coding agent、CI、SWE-bench 和日常软件工程都依赖 patch 后验证；现代 Agent 只是把这件事纳入自动循环。
- 稳定部分：修改后必须有可执行或可审查证据，不能只凭生成文本。
- 易变部分：具体 harness、沙箱、测试选择、自动修复策略和 benchmark 会变化。

## 证据锚点

- Source: [[SWE-bench]]
- Anchor: [[SWE-bench#为什么收]]
- Evidence type: benchmark source note + coding-agent engineering synthesis.
- Confidence: medium
- Boundary: SWE-bench 是代表性 benchmark；本卡概括的是 patch 验证纪律，不等于某个 benchmark 的完整协议。

## 复习触发

- 为什么 Patch Validation 不能只看 diff 是否合理？
- 如果测试无法运行，你应该怎样报告验证缺口？
- Patch Validation 和 [[Task Success Rate]] 在 SWE-bench 里怎么连接？

## 相关链接

- [[Coding Agent]]
- [[Evaluation]]
- [[Agent Harness]]
