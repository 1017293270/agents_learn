---
title: "Agent 基础与工具调用参考资料"
type: reference
status: verified
confidence: high
depth: deep
source:
  - title: "Agents - OpenAI Agents SDK"
    type: official-doc
    url: "https://openai.github.io/openai-agents-python/agents/"
    accessed: "2026-06-08"
  - title: "Agent - OpenAI Agents SDK reference"
    type: official-doc
    url: "https://openai.github.io/openai-agents-python/ref/agent/"
    accessed: "2026-06-08"
  - title: "Guardrails - OpenAI Agents SDK"
    type: official-doc
    url: "https://openai.github.io/openai-agents-python/guardrails/"
    accessed: "2026-06-08"
  - title: "Agent evals"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/agent-evals"
    accessed: "2026-06-08"
  - title: "Trace grading"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/trace-grading"
    accessed: "2026-06-08"
  - title: "Model Context Protocol Specification 2025-06-18"
    type: official-doc
    url: "https://modelcontextprotocol.io/specification/2025-06-18"
    accessed: "2026-06-08"
  - title: "Building effective agents"
    type: article
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["agent", "tool-calling", "mcp", "evaluation", "guardrails", "official-doc", "source-review"]
---

# Agent 基础与工具调用参考资料

## 来源信息

- 标题：OpenAI Agents SDK；OpenAI Agent evals；OpenAI Trace grading；Model Context Protocol Specification；Anthropic Building effective agents
- 作者或机构：OpenAI、Model Context Protocol、Anthropic
- 类型：官方文档、工程文章
- URL：
  - https://openai.github.io/openai-agents-python/agents/
  - https://openai.github.io/openai-agents-python/ref/agent/
  - https://openai.github.io/openai-agents-python/guardrails/
  - https://platform.openai.com/docs/guides/agent-evals
  - https://platform.openai.com/docs/guides/trace-grading
  - https://modelcontextprotocol.io/specification/2025-06-18
  - https://www.anthropic.com/engineering/building-effective-agents
- 访问日期：2026-06-08

## 一句话结论

Agent 不是“会聊天的大模型”这么简单，而是由模型、指令、工具、状态、权限、护栏、评估和追踪共同组成的可执行系统；MCP 可以标准化模型应用连接外部工具和上下文的方式，eval 与 trace grading 用来检验 agent 是否真的可靠。

## 核心观点

- OpenAI Agents SDK 把 agent 描述为配置了 instructions、tools、guardrails、handoffs 等能力的 AI model。
- Anthropic 的工程文章强调区分 workflow 和 agent：workflow 走预定义代码路径，agent 更强调模型动态决定执行路径和工具使用。
- Tool calling 的安全边界在应用侧：模型提出调用意图，真实执行必须经过 schema、权限、确认、审计和错误处理。
- Guardrails 不应只理解为提示词里的“不要做什么”，更应落实为输入检查、输出检查、工具前检查、权限策略和人工升级路径。
- MCP，全称 Model Context Protocol，是连接 AI 应用与外部工具、资源和提示模板的协议；它不是模型，也不是单个工具平台。
- Agent eval 需要覆盖最终答案、工具调用、参数、权限、轨迹、延迟、成本和失败恢复，而不是只问“回答看起来对不对”。
- Trace grading 是对 agent 端到端轨迹进行结构化评分，有助于定位工具选择、步骤顺序、权限、引用和恢复策略中的问题。

## 资料可信度评估

- 来源层级：OpenAI 与 MCP 官方文档属于 Tier 1；Anthropic 工程文章属于 Tier 2，但来自模型厂商工程团队，适合支持 agent 架构判断。
- 是否为一手资料：OpenAI 与 MCP 是一手资料；Anthropic 文章是一手工程经验总结。
- 是否有实验、数据、代码或可复现证据：OpenAI 文档包含 SDK/API 概念和示例；MCP 规范包含协议对象；Anthropic 文章提供架构分类和工程判断。本文档尚未做本地复现实验。
- 是否可能过时：是。Agents SDK、API、MCP 协议版本、eval 工具和平台能力都会变化。
- 适合引用范围：适合支持 agent 基础概念、工具调用边界、MCP 角色、guardrails 和 eval 结构；不适合直接断言某个产品最新价格、模型支持范围或 SDK 细节。

## 可引用事实

- Agent 可以被理解为“配置了模型、指令、工具、护栏、交接和运行状态的系统单元”。
- Workflow 与 agent 的关键区别在于控制流来源：workflow 的路径主要由代码预先规定，agent 的路径更多由模型根据上下文动态决定。
- Guardrails 可以放在输入、输出、工具调用、交接和业务执行边界上。
- MCP 通过 host、client、server 的角色拆分，把工具、资源和提示模板暴露给 AI 应用。
- Agent eval 应该看最终结果，也应该看过程轨迹。

## 关键主张表

| 主张 | 原始证据位置 | 可引用程度 | 局限 | 适合写入哪里 |
| --- | --- | --- | --- | --- |
| Agent 是配置了 instructions、tools、guardrails、handoffs 等能力的模型系统 | OpenAI Agents SDK Agent reference | 高 | 属于 OpenAI SDK 语境，不是所有框架的唯一标准定义 | `knowledge/02-Agent基础与工具调用/02-Agent基础概念.md` |
| Workflow 和 agent 应区分控制流是否主要预定义 | Anthropic Building effective agents | 中高 | 工程分类，不是学术统一定义 | `knowledge/02-Agent基础与工具调用/02-Agent基础概念.md` |
| 工具安全需要应用侧权限和护栏，不应只依赖模型判断 | OpenAI Guardrails + Function calling docs | 高 | 具体策略取决于项目权限模型 | `knowledge/02-Agent基础与工具调用/03-工具安全与权限.md` |
| MCP 是 AI 应用连接外部上下文与工具的协议 | MCP Specification | 高 | 协议版本会变化，具体传输和能力支持需看版本 | `knowledge/02-Agent基础与工具调用/04-MCP与远程工具.md` |
| Agent eval 应覆盖轨迹而不只是最终回答 | OpenAI Agent evals + Trace grading docs | 高 | eval 设计仍需结合业务任务和可接受风险 | `knowledge/02-Agent基础与工具调用/05-Agent评估.md` |

## 机制解释

第二章的核心机制可以串成一条链：

```text
用户目标
  -> agent 接收指令和上下文
  -> 模型判断下一步
  -> 需要外部能力时产生 tool call
  -> 应用侧验证、授权、执行工具
  -> 工具结果回到 agent
  -> agent 继续推理或给出最终输出
  -> trace 与 eval 记录质量、风险和改进点
```

MCP 位于“应用侧连接外部工具和上下文”的标准化层；guardrails 位于输入、输出和工具执行边界；eval 位于开发和上线后的质量闭环。

## 适用范围

- 支持 `knowledge/02-Agent基础与工具调用/` 下所有概念卡。
- 支持初学者理解 agent、tool calling、MCP、guardrails、eval 的关系。
- 支持以后把本知识库扩展到 RAG、memory、planning、多 agent、工作流编排和可观测性。

## 局限与风险

- OpenAI SDK 的对象命名不等于所有平台通用命名。
- Anthropic 的 workflow/agent 分类是很有用的工程判断，但不是唯一标准。
- MCP 规范版本会演进，不能把某个版本里的对象和行为永远视为固定不变。
- Agent eval 没有通用万能指标；指标必须回到具体任务、工具、权限和用户风险。

## 与已有知识关联

- `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md`
- `knowledge/02-Agent基础与工具调用/02-Agent基础概念.md`
- `knowledge/02-Agent基础与工具调用/03-工具安全与权限.md`
- `knowledge/02-Agent基础与工具调用/04-MCP与远程工具.md`
- `knowledge/02-Agent基础与工具调用/05-Agent评估.md`

## 短摘录

不保留长摘录。使用时引用官方文档或工程文章，并在知识卡里用自己的话重建定义、机制、边界和实践判断。

## 待验证问题

- OpenAI Agents SDK 当前版本中 guardrails、handoffs、sessions、tracing 的默认行为是否需要单独复现实验。
- MCP 2025-06-18 版本与后续 draft 版本在授权、传输和能力对象上有哪些差异。
- 不同供应商对 agent、tool、function calling、connector、MCP server 的命名差异是否需要单独做对照表。

## 变更记录

- 2026-06-08：创建第二章统一引用卡。
