---
title: "LLM 使用与训练参考资料"
type: reference
status: verified
confidence: high
depth: deep
source:
  - title: "Attention Is All You Need"
    type: paper
    url: "https://arxiv.org/abs/1706.03762"
    accessed: "2026-06-08"
  - title: "OpenAI Models"
    type: official-doc
    url: "https://platform.openai.com/docs/models"
    accessed: "2026-06-08"
  - title: "OpenAI Supervised fine-tuning"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/supervised-fine-tuning"
    accessed: "2026-06-08"
  - title: "OpenAI Fine-tuning best practices"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/fine-tuning-best-practices"
    accessed: "2026-06-08"
  - title: "OpenAI Reinforcement fine-tuning"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/reinforcement-fine-tuning"
    accessed: "2026-06-08"
  - title: "Training language models to follow instructions with human feedback"
    type: paper
    url: "https://arxiv.org/abs/2203.02155"
    accessed: "2026-06-08"
  - title: "Hugging Face Transformers text generation"
    type: official-doc
    url: "https://huggingface.co/docs/transformers/llm_tutorial"
    accessed: "2026-06-08"
  - title: "Hugging Face Text Generation Inference"
    type: official-doc
    url: "https://huggingface.co/docs/text-generation-inference/index"
    accessed: "2026-06-08"
  - title: "Claude models overview"
    type: official-doc
    url: "https://platform.claude.com/docs/en/about-claude/models/overview"
    accessed: "2026-06-08"
  - title: "Gemini models"
    type: official-doc
    url: "https://ai.google.dev/gemini-api/docs/models"
    accessed: "2026-06-08"
  - title: "Mistral AI documentation"
    type: official-doc
    url: "https://docs.mistral.ai/"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["llm", "transformer", "inference", "sft", "rlhf", "model-comparison", "official-doc", "paper"]
---

# LLM 使用与训练参考资料

## 一句话结论

大模型学习需要同时理解三层：模型是什么、如何使用和部署、如何通过 SFT/RLHF/RFT 等方法让模型更适合任务。

## 资料可信度评估

- 来源层级：Tier 1 为主，包含经典论文和官方文档。
- 适用范围：适合支持 `01-大模型的使用与训练` 模块的基础概念、推理部署、SFT、RLHF 和模型对比。
- 时效风险：模型列表、上下文窗口、价格、支持能力变化很快；涉及具体模型名称和能力时必须记录访问日期。
- 局限：OpenAI、Anthropic、Google、Mistral 等官方文档各自偏向本平台；跨平台判断应写成“选择维度”，不要写成永久排名。

## 可引用事实

- Transformer 论文提出了只基于 attention 的序列建模架构，是现代大语言模型的重要基础。
- 自回归语言模型在生成时通常逐 token 预测后续内容。
- OpenAI SFT 文档强调先做 eval，再投入微调；SFT 需要示例输入和理想输出。
- OpenAI fine-tuning best practices 强调数据质量、覆盖失败点、数据平衡和多样性。
- InstructGPT 论文展示了用人类反馈训练指令跟随模型的典型 RLHF 流程。
- OpenAI RFT 文档说明 RFT 使用可编程 grader 作为反馈信号，适合更复杂的专家任务。
- Hugging Face TGI 和 vLLM/SGLang 等推理服务生态说明，部署大模型不仅是加载权重，还涉及吞吐、延迟、显存和服务接口。
- OpenAI、Claude、Gemini、Mistral 模型文档都按能力、速度、成本、模态、上下文和工具能力区分模型。

## 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| Transformer 是现代 LLM 的关键基础架构之一 | 原始论文提出 Transformer 架构并展示序列任务效果 | Attention Is All You Need | high | 现代模型已在 Transformer 基础上做大量工程改造 |
| LLM 推理通常是逐 token 生成 | Hugging Face text generation 文档说明生成过程 | Hugging Face Transformers | high | 多模态和非自回归模块可能有不同机制 |
| SFT 适合用示例教模型固定风格、格式和任务行为 | OpenAI SFT 文档说明用示例输入和理想输出训练 | OpenAI SFT | high | 不适合补充模型完全不知道的新事实 |
| RLHF 通过偏好数据和奖励模型对齐人类偏好 | InstructGPT 论文给出流程 | InstructGPT paper | high | 偏好数据和标注者偏差会影响结果 |
| 模型对比必须看任务、成本、延迟和平台约束 | 多家官方模型文档按能力和使用场景分类 | OpenAI/Claude/Gemini/Mistral docs | high | 具体排名会快速过时 |

## 与已有知识关联

- `knowledge/01-大模型的使用与训练/01-大模型基础概念.md`
- `knowledge/01-大模型的使用与训练/03-模型推理与部署.md`
- `knowledge/01-大模型的使用与训练/04-SFT监督微调.md`
- `knowledge/01-大模型的使用与训练/05-RLHF人类反馈强化学习.md`
- `knowledge/01-大模型的使用与训练/06-常用大模型对比.md`

## 待验证问题

- 是否需要为开源模型单独建立 Hugging Face、vLLM、llama.cpp、Ollama 的部署实践卡。
- 是否需要把 RLHF、RFT、DPO、RLAIF 单独拆成一个模型对齐模块。
- 是否需要维护一个按月更新的“模型能力快照”。

## 变更记录

- 2026-06-08：创建统一资料引用卡。

