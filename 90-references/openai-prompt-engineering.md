---
title: "OpenAI Prompt Engineering References"
type: reference
status: verified
confidence: high
depth: deep
source:
  - title: "Prompt engineering"
    type: official-doc
    url: "https://developers.openai.com/api/docs/guides/prompt-engineering"
    accessed: "2026-06-08"
  - title: "Prompting fundamentals"
    type: official-doc
    url: "https://openai.com/academy/prompting/"
    accessed: "2026-06-08"
  - title: "Reasoning best practices"
    type: official-doc
    url: "https://developers.openai.com/api/docs/guides/reasoning-best-practices"
    accessed: "2026-06-08"
  - title: "Safety best practices"
    type: official-doc
    url: "https://developers.openai.com/api/docs/guides/safety-best-practices"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["openai", "prompt-engineering", "official-doc", "source-review", "safety"]
---

# OpenAI Prompt Engineering References

## 来源信息

- 标题：Prompt engineering；Prompting fundamentals；Reasoning best practices；Safety best practices
- 作者或机构：OpenAI
- 类型：官方文档和官方学习资料
- URL：
  - https://developers.openai.com/api/docs/guides/prompt-engineering
  - https://openai.com/academy/prompting/
  - https://developers.openai.com/api/docs/guides/reasoning-best-practices
  - https://developers.openai.com/api/docs/guides/safety-best-practices
- 访问日期：2026-06-08

## 一句话结论

OpenAI 官方资料把 Prompt 工程定义为编写和迭代有效指令的过程，核心不是背模板，而是清楚表达目标、上下文、约束、示例和验证标准。

## 核心观点

- Prompt 工程是设计和改进输入，使模型更稳定地产生符合要求输出的过程。
- 没有唯一完美的 prompt；有效 prompt 需要结合任务、模型和输出要求反复测试。
- Markdown 标题、列表、XML 标签等结构可以帮助模型识别不同信息边界。
- Few-shot 示例能让模型学习输入输出模式，但示例要覆盖有代表性的情况。
- 对 reasoning models，简单直接的提示通常更好；强行要求“think step by step”不一定有帮助，甚至可能降低效果。
- Prompt 可以约束主题和语气，但不能替代输入校验、权限控制、安全策略和人工审查。

## 资料可信度评估

- 来源层级：Tier 1
- 作者或机构可信度：OpenAI 官方资料，适合支持 OpenAI 模型和 API 的提示建议。
- 是否为一手资料：是。
- 是否有实验、数据、代码或可复现证据：有示例和建议；本卡未做本地模型实验。
- 是否可能过时：是。模型系列、最佳实践和 API 参数会变化。
- 是否存在商业宣传、立场偏差或上下文缺失：存在平台文档偏向 OpenAI 生态的可能；跨模型通用结论需要谨慎。

## 可引用事实

- OpenAI 文档明确建议复杂应用要固定模型版本，并建立测试或 eval 来监控 prompt 行为。
- OpenAI 文档建议用 message roles 或 `instructions` 表达不同权威层级的指令。
- OpenAI 文档建议用 Markdown 和 XML 等结构划分 prompt 里的逻辑边界。
- OpenAI 文档说明 few-shot 是通过在 prompt 中加入少量输入输出示例来引导模型。
- OpenAI reasoning best practices 建议对推理模型保持提示简单直接，并避免不必要的 chain-of-thought 提示。
- OpenAI safety best practices 说明 prompt engineering 能帮助约束主题和语气，但还需要输入范围、输出长度、用户验证等安全措施。

## 关键主张表

| 主张 | 原始证据位置 | 可引用程度 | 局限 | 适合写入哪里 |
| --- | --- | --- | --- | --- |
| Prompt 工程是编写有效指令以稳定得到目标输出的过程 | OpenAI Prompt engineering guide | 高 | 定义来自 OpenAI API 语境 | `knowledge/01-大模型的使用与训练/02-Prompt工程.md` |
| Markdown/XML 分隔结构有助于区分指令、示例和上下文 | OpenAI Prompt engineering guide: Message formatting | 高 | 不是万能，仍需测试 | `knowledge/01-大模型的使用与训练/02-Prompt工程.md` |
| Few-shot 示例适合教模型输入输出模式 | OpenAI Prompt engineering guide: Few-shot learning | 高 | 示例质量差会误导模型 | `knowledge/01-大模型的使用与训练/02-Prompt工程.md` |
| 对 reasoning models，强行要求“think step by step”未必有益 | OpenAI Reasoning best practices | 高 | 针对 reasoning models，不应无条件推广到所有模型 | `knowledge/01-大模型的使用与训练/02-Prompt工程.md` |
| Prompt 不能替代安全控制 | OpenAI Safety best practices | 高 | 具体安全策略需按产品风险设计 | `knowledge/01-大模型的使用与训练/02-Prompt工程.md` |

## 机制解释

Prompt 影响模型输出，是因为模型会基于输入里的任务、上下文、示例、格式约束和对话角色来预测最合适的后续文本。清晰的 prompt 能减少歧义，降低模型猜测空间；结构化的 prompt 能让模型更容易区分“规则”“资料”“例子”和“用户请求”；测试和迭代能发现 prompt 在不同输入下是否稳定。

## 适用范围

- Prompt 工程入门笔记。
- Agents 学习中的 instruction design、tool instruction、RAG prompt、system/developer/user role 设计。
- AI 产品中的可复用 prompt 模板设计和 eval。

## 局限与风险

- 这组资料主要来自 OpenAI，不足以覆盖所有模型厂商。
- 官方建议会随模型变化而更新，具体模型上线前仍需测试。
- Prompt 优化不能解决所有问题；有些问题应该通过工具、检索、结构化输出、权限或微调解决。

## 与已有知识关联

- `knowledge/01-大模型的使用与训练/02-Prompt工程.md`
- `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md`
- `tags.md`: `prompt-engineering`, `few-shot`, `zero-shot`, `prompt-injection`, `evaluation`

## 短摘录

不保留长摘录。使用时引用官方链接，并用自己的话解释机制、边界和实践方法。

## 待验证问题

- 对当前常用 OpenAI 模型，不同 prompt 结构对输出稳定性的具体影响需要本地实验。
- 中文 prompt 与英文 prompt 在复杂指令遵循上是否存在可观察差异。
- 对多轮对话，哪些信息应放在系统/开发者指令，哪些应放在用户输入，需要结合具体 API 和产品设计验证。

## 变更记录

- 2026-06-08：创建官方资料引用卡。
