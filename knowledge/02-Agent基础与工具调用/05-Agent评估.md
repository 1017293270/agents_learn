---
title: "Agent 评估"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "Agent 基础与工具调用参考资料"
    type: reference
    url: "../../90-references/agent-basics-tools-references.md"
    accessed: "2026-06-08"
  - title: "Agent evals"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/agent-evals"
    accessed: "2026-06-08"
  - title: "Trace grading"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/trace-grading"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["agent", "agent-evaluation", "evaluation", "trace", "testing", "observability", "beginner"]
---

# Agent 评估

## 一句话结论

Agent 评估不是只看最终回答像不像对，而是要同时检查目标是否完成、工具是否选对、参数是否正确、权限是否守住、过程是否可追踪、成本和延迟是否可接受。

## 概念定位

- 它是什么：用测试集、评分标准、轨迹审查和线上指标判断 agent 是否可靠的质量闭环。
- 它不是什么：不是临时问模型几个问题，也不是只凭“感觉回答不错”。
- 相邻概念：testing、QA、trace、grader、benchmark、regression、observability、red teaming。
- 前置知识：prompt 工程、tool calling、权限、日志、基础统计、产品验收标准。

初学者可以先记住：

```text
普通问答评估看“答案对不对”。
Agent 评估还要看“过程有没有安全地做对”。
```

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| Eval | Evaluation | 评估 | 判断模型或 agent 表现是否达到要求 |
| QA | Quality Assurance | 质量保证 | 通过流程和测试保证产品质量 |
| KPI | Key Performance Indicator | 关键绩效指标 | 用来衡量业务目标的核心指标 |
| SLA | Service Level Agreement | 服务等级协议 | 对可用性、响应时间等服务水平的承诺 |
| SLO | Service Level Objective | 服务等级目标 | 内部设定的可靠性目标，如 99.9% 可用 |
| P50 | 50th Percentile | 第 50 百分位 | 一半请求比这个值快，常用来看典型延迟 |
| P95 | 95th Percentile | 第 95 百分位 | 95% 请求比这个值快，常用来看尾部延迟 |
| MTTR | Mean Time To Recovery | 平均恢复时间 | 系统出问题后恢复正常平均要多久 |
| RAG | Retrieval-Augmented Generation | 检索增强生成 | 评估时要检查检索资料是否支持回答 |
| API | Application Programming Interface | 应用程序编程接口 | 工具调用、评估任务和日志查询常通过 API 完成 |
| JSON | JavaScript Object Notation | JavaScript 对象表示法 | eval 样例、工具参数、评分结果常用 JSON 存储 |
| CI | Continuous Integration | 持续集成 | 每次代码变更自动运行测试和 eval |
| CD | Continuous Delivery / Continuous Deployment | 持续交付 / 持续部署 | 自动把通过测试的变更交付或部署 |

## 核心概念

Agent eval 至少要覆盖六个层面：

| 层面 | 要评估什么 | 例子 |
| --- | --- | --- |
| 任务结果 | 用户目标是否完成 | 是否真的找到测试失败原因 |
| 工具选择 | 是否调用了正确工具 | 该读文件时是否读文件，而不是凭空猜 |
| 参数质量 | 参数是否正确 | 文件路径、订单号、日期范围是否正确 |
| 权限与安全 | 是否越权或执行高风险动作 | 是否拒绝查询他人订单 |
| 过程轨迹 | 步骤是否合理、可追踪 | 是否先检索、再读取、再总结 |
| 运行质量 | 成本、延迟、稳定性 | P95 延迟、工具失败率、重试次数 |

一个只看最终答案的 eval，很容易漏掉 agent 的过程错误。比如 agent 最终回答“已帮你删除草稿”，但它可能删除了错误文件。最终文本看起来没问题，真实系统已经出事故。

## 机制与原理

一个基本 agent eval 流程：

```text
1. 定义任务范围
2. 收集代表性样例
3. 为每个样例写清预期结果和禁止行为
4. 运行 agent
5. 记录完整 trace：输入、模型输出、工具调用、工具结果、最终回答
6. 用人工或 grader 评分
7. 分析失败类型
8. 修改 prompt、工具、权限、模型或流程
9. 重跑 eval，比较是否真的变好
```

### Trace 是什么

Trace 指 agent 的执行轨迹。它通常包含：

- 用户输入。
- 系统指令。
- 模型中间输出。
- 工具调用名称。
- 工具参数。
- 工具返回结果。
- 错误、重试、取消、超时。
- 最终回答。
- 时间、成本、模型版本、工具版本。

没有 trace，就只能看到“最后说了什么”。有 trace，才能知道“为什么这么说、用了什么工具、哪里失败了”。

### Grader 是什么

Grader 是评分器。它可以是：

- 人工评分：人按照 rubric 打分。
- 规则评分：代码检查字段、格式、工具调用、权限结果。
- 模型评分：另一个模型根据标准判断输出质量。
- 混合评分：规则先筛硬错误，模型或人工评估复杂质量。

Rubric 是评分细则，不是缩写。它的作用是把“好不好”变成可重复判断的标准。

## 适用场景

- Agent 需要调用工具、执行动作或访问私有资料。
- 任务有稳定质量要求，例如客服、代码修复、报告生成、知识检索。
- 系统要上线给真实用户使用。
- Prompt、模型、工具或权限规则会持续变化。
- 需要比较不同模型、不同工具描述或不同 workflow 的效果。

## 不适用场景

- 一次性探索、无真实用户、无副作用的极早期实验，可以先用人工观察。
- 创意写作、开放脑暴等任务，很难用单一正确答案衡量，但仍可用人工标准和偏好评估。
- 没有明确目标和用户价值的问题，不适合急着做复杂 eval，应先收敛任务定义。

注意：不适合复杂自动 eval，不等于不需要评估。至少要记录样例、失败和人工判断。

## 前提、边界与反例

- 必要前提：任务目标明确、样例代表真实场景、评分标准可执行、trace 可收集。
- 适用边界：eval 能降低回归风险，但不能穷尽所有未来输入。
- 反例或例外：只测 5 个最简单样例，可能让 agent 在真实复杂场景里崩掉。
- 结论可能失效的条件：样例过时、业务规则变化、模型版本变化、工具返回数据变化、grader 偏差。

## 对比与替代方案

| 方法 | 适合 | 优点 | 局限 |
| --- | --- | --- | --- |
| 人工 spot check | 初期探索 | 快速发现明显问题 | 不稳定，难回归 |
| Golden set | 稳定核心任务 | 可重复比较 | 需要维护样例 |
| Rule-based grader | 格式、权限、工具调用 | 稳定、便宜、可解释 | 难判断语义质量 |
| Model-based grader | 开放答案质量 | 灵活，能处理文本质量 | 也会出错，需要校准 |
| Trace grading | 多工具 agent | 能看过程问题 | 需要完整日志 |
| Online metrics | 上线后监控 | 反映真实用户 | 需要隐私和采样治理 |
| Red teaming | 安全压力测试 | 能发现极端风险 | 不能代表普通质量 |

## 示例或最小实验

任务：评估一个“知识库问答 agent”。

### 样例

```json
{
  "input": "RLHF 是什么？",
  "expected_behavior": [
    "先搜索知识库",
    "读取 RLHF 笔记",
    "回答必须包含 Reinforcement Learning from Human Feedback 全称",
    "不能编造知识库里没有的具体实验结果"
  ],
  "forbidden_behavior": [
    "不检索直接猜",
    "把 RLHF 说成普通监督微调",
    "给出没有来源的确定性结论"
  ]
}
```

### 评分维度

| 维度 | 通过标准 |
| --- | --- |
| 工具选择 | 调用了 search/read 类工具 |
| 来源 | 答案引用或说明来自 RLHF 笔记 |
| 概念 | 正确写出 Reinforcement Learning from Human Feedback |
| 边界 | 说明 RLHF 不能保证事实永远正确 |
| 安全 | 没有读取无关或敏感文件 |

### 最小结论

如果 agent 回答正确但没有检索知识库，对“知识库问答 agent”来说仍然应扣分。因为这个产品的目标不是“模型背得出来”，而是“基于你的知识资料回答”。

## 失败模式与风险

- 样例太少：只覆盖简单问题，真实任务失败。
- 样例偏差：测试集都是理想输入，没有口语、错别字、歧义。
- 只看最终答案：漏掉工具误选、越权读取、成本过高。
- Grader 偏差：模型评分器偏好长答案或漂亮格式。
- 指标冲突：速度更快但准确率下降，安全更严但拒答率上升。
- 数据泄露：eval 样例包含真实 PII。
- 过拟合 eval：prompt 专门适配测试集，真实用户表现不好。
- 版本不可追踪：不知道哪次模型、工具、prompt 改动导致质量变化。
- 线上反馈闭环缺失：用户报错没有回流到 eval 样例。

## 常见误区

- 误区：强模型不用 eval。
  - 修正：强模型也会在工具、权限、上下文污染和长任务中失败。
- 误区：eval 就是准确率。
  - 修正：agent eval 还要看过程、安全、成本、延迟和可恢复性。
- 误区：模型评分器一定客观。
  - 修正：模型 grader 也有偏差，需要用人工样本校准。
- 误区：通过 eval 就可以放心上线。
  - 修正：eval 只是降低风险，上线仍要监控、限流、回滚和人工兜底。
- 误区：失败样例越少越好。
  - 修正：早期收集失败样例是好事，它们能帮你补边界和提高鲁棒性。

## 实践判断

- 什么时候应该采用系统 eval：agent 有工具调用、用户真实依赖结果、任务会持续迭代。
- 什么时候应该谨慎：评分标准还没定义、样例不代表真实用户、trace 采集会泄露敏感信息。
- 落地时最先验证什么：核心任务成功率、工具调用正确率、权限违规率、幻觉率、P95 延迟。
- 可观察指标或检查点：
  - Task success rate：任务成功率。
  - Tool selection accuracy：工具选择准确率。
  - Parameter validity rate：参数有效率。
  - Permission violation rate：权限违规率。
  - Grounding accuracy：基于资料回答的准确率。
  - Hallucination rate：幻觉率。
  - Average cost per task：单任务平均成本。
  - P95 latency：95 百分位延迟。
  - Human escalation rate：人工接管率。

## 来源与证据

- 来源：`90-references/agent-basics-tools-references.md`；OpenAI Agent evals；OpenAI Trace grading。
- 证据摘要：OpenAI Agent evals 与 trace grading 文档支持对 agent 过程轨迹进行评估；本卡把工具选择、参数、权限、成本、延迟纳入 eval，是基于 agent 系统风险的工程扩展。
- 可信度判断：trace-based eval 和 grader 思路可信度高；具体指标阈值必须由项目目标和风险决定。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| Agent eval 应看过程轨迹 | OpenAI trace grading 关注 trace 级评分 | OpenAI Trace grading | high | 平台对象和 API 会变化 |
| 最终答案正确不代表 agent 可靠 | 工具和权限错误可能被最终文本掩盖 | 工程推断 | high | 需要具体 trace 支持 |
| Grader 可以是规则、模型或人工 | eval 实践中常见多种评分方式 | OpenAI Agent evals + 工程实践 | medium | 不同平台支持不同 |
| Eval 样例应代表真实任务 | 测试集偏差会导致上线表现失真 | 测试工程实践 | high | 代表性需要持续维护 |

## 待验证问题

- 是否需要为本知识库 viewer 做一个最小 agent eval 样例集。
- OpenAI Agent evals 当前 API 具体对象和限制是否需要单独复现实验。
- 模型 grader 在中文知识卡评估中是否偏好长答案，是否需要人工校准。
- Agent eval、RAG eval、tool eval 是否分三篇进阶卡。

## 变更记录

- 2026-06-08：创建深度初稿，补充 eval 全称、trace、grader、指标、样例、失败模式和实践判断。
