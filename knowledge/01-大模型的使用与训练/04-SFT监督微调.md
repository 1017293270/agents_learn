---
title: "SFT 监督微调"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "LLM 使用与训练参考资料"
    type: reference
    url: "../../90-references/llm-use-training-references.md"
    accessed: "2026-06-08"
  - title: "OpenAI Supervised fine-tuning"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/supervised-fine-tuning"
    accessed: "2026-06-08"
  - title: "OpenAI Fine-tuning best practices"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/fine-tuning-best-practices"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["sft", "fine-tuning", "training-data", "evaluation", "beginner"]
---

# SFT 监督微调

## 我学到的核心点

SFT 是用“输入 -> 理想输出”的示例继续训练模型，让模型更稳定地学会某种任务格式、回答风格或业务行为。它不是给模型安装一个知识库，也不是修复所有 hallucination 的万能药。

## SFT 是什么

SFT 全称 Supervised Fine-Tuning，监督微调。监督的意思是：训练数据里有明确示范，告诉模型“遇到这种输入，应该输出这样的答案”。

最小样子：

```json
{
  "input": "用户问：退款多久到账？",
  "output": "退款通常会在 3-5 个工作日内原路返回，具体以支付渠道为准。"
}
```

对于聊天模型，训练数据通常会保留多轮 messages 格式，让模型学习对话里的角色、上下文和理想回复。

## SFT 适合解决什么

| 需求 | 是否适合 SFT | 原因 |
| --- | --- | --- |
| 固定输出格式 | 适合 | 示例能教模型稳定格式 |
| 特定语气和文风 | 适合 | 示例能体现风格 |
| 业务分类或抽取 | 适合 | 有稳定标签和答案 |
| 工具调用参数习惯 | 可能适合 | 需要高质量工具调用示例 |
| 让模型知道最新事实 | 不优先 | 更适合 RAG 或数据库 |
| 解决权限和安全 | 不适合单独靠 SFT | 应由系统策略控制 |

## SFT 和 Prompt 的关系

先 prompt，后 SFT。

如果只是 prompt 没写清楚，不要急着微调。先用 prompt、结构化输出、RAG、工具和 eval 解决。只有当你发现“同类任务长期重复，prompt 已经优化，但模型仍不稳定”时，SFT 才更值得考虑。

一个判断：

```text
如果你能写出 50 个高质量示例，并且这些示例代表真实业务输入输出，
SFT 才可能有明显价值。
```

OpenAI 官方 SFT 文档也强调先做 eval，再投入微调；没有 eval，就不知道微调是否真的变好。

## SFT 流程

```text
确定任务
  -> 建立 eval
  -> 收集真实样例
  -> 清洗和标注数据
  -> 切分训练集/验证集
  -> 选择基础模型
  -> 创建微调任务
  -> 评估微调模型
  -> 与基础模型对比
  -> 迭代数据
```

关键不是“跑一次训练”，而是反复改数据。

## 数据质量比数量更重要

一条好数据应该：

- 输入真实，像线上用户会问的话。
- 输出准确，不能把错误教给模型。
- 风格一致，避免同类问题有矛盾答案。
- 覆盖边界情况，不只覆盖简单问题。
- 标注规则清楚，让不同标注者能给出一致答案。

坏数据会直接把模型带坏。比如训练集中很多回答都说“我可以帮你预约会议”，但产品实际上没有预约工具，微调后的模型就可能更频繁承诺做不到的事。

## 示例数据设计

### 任务：客服意图分类

输入：

```text
我昨天买的会员怎么还没到账？
```

理想输出：

```json
{
  "intent": "membership_not_received",
  "urgency": "medium",
  "need_human": false
}
```

需要补充的边界样例：

- 用户同时问两个问题。
- 用户情绪激烈。
- 用户描述不完整。
- 用户要求退款但不提供订单号。
- 用户说了和业务无关的话。

## 常见风险

- 数据偏差：训练集里某种答案太多，模型上线后过度输出。
- 过拟合：模型只会训练集风格，遇到新表达就不稳。
- 错误固化：错误示例会被模型学习。
- 成本失控：微调、评估、上线维护都需要时间和费用。
- 版本漂移：基础模型更新或业务规则变化后，微调模型可能过时。
- 安全错觉：微调不能替代权限、审计和敏感操作确认。

## SFT 不适合什么

- 频繁变化的知识：用 RAG 或数据库。
- 严格计算：用工具或程序。
- 强权限控制：用后端策略。
- 极少样例的任务：先收集数据。
- 需求还没稳定的产品：先用 prompt 和 eval 快速迭代。

## 初学者实践路线

1. 先选一个小任务，比如“客服反馈分类”。
2. 写 prompt baseline。
3. 准备 30-50 条真实样例。
4. 建一个简单 eval：准确率、格式错误率、人工评分。
5. 再考虑 SFT。
6. 微调后必须和基础模型 + prompt baseline 对比。

## 来源与证据

- 来源：OpenAI Supervised fine-tuning；OpenAI Fine-tuning best practices；`90-references/llm-use-training-references.md`。
- 证据摘要：官方文档说明 SFT 用示例输入和理想输出训练，强调先建立 eval、构造代表性数据，并通过数据质量迭代提升效果。
- 可信度判断：SFT 概念和流程来自官方文档，可信度高；具体样例数量和收益取决于任务，需要实验验证。

## 还没搞清楚的问题

- 是否要为 OpenAI、Hugging Face PEFT/LoRA、国产平台分别写微调流程。
- 是否需要建立一个小型 SFT 实验数据集。
- 微调和 RAG 的边界是否需要单独成文。

## 变更记录

- 2026-06-08：补充正式内容，覆盖定义、适用场景、流程、数据质量、风险和实践路线。

