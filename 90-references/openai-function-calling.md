---
title: "OpenAI Function Calling and Tools"
type: reference
status: verified
confidence: high
depth: deep
source:
  - title: "Function calling"
    type: official-doc
    url: "https://developers.openai.com/api/docs/guides/function-calling"
    accessed: "2026-06-08"
  - title: "Using tools"
    type: official-doc
    url: "https://developers.openai.com/api/docs/guides/tools"
    accessed: "2026-06-08"
  - title: "Migrate to the Responses API"
    type: official-doc
    url: "https://developers.openai.com/api/docs/guides/migrate-to-responses"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["openai", "tool-calling", "official-doc", "source-review"]
---

# OpenAI Function Calling and Tools

## 来源信息

- 标题：Function calling；Using tools；Migrate to the Responses API
- 作者或机构：OpenAI
- 类型：官方 API 文档
- URL：
  - https://developers.openai.com/api/docs/guides/function-calling
  - https://developers.openai.com/api/docs/guides/tools
  - https://developers.openai.com/api/docs/guides/migrate-to-responses
- 发布时间：页面未明确标注
- 访问日期：2026-06-08

## 一句话结论

OpenAI 官方文档把 function calling 视为 tool calling 的一种核心形式：模型提出工具调用请求，应用侧执行真实代码或能力，再把工具输出回传给模型生成后续回复。

## 核心观点

- Tool calling 是模型与应用通过 API 进行的多步骤交互，不是模型自己直接执行外部代码。
- Function tool 使用 JSON Schema 描述输入参数；OpenAI 也支持内置工具、远程 MCP、自定义工具等更广义的 tools。
- Responses API 是 OpenAI 当前面向 agent-like 应用的统一接口，支持内置工具、自定义函数、多轮状态、工具上下文等能力。
- 模型可能在一次响应里返回零个、一个或多个工具调用，应用实现应按多个调用处理。
- `tool_choice` 可控制工具选择行为；`parallel_tool_calls` 可限制并行函数调用。
- `strict: true` 让函数调用更可靠地遵守 schema，但 schema 需要满足额外约束。
- 流式工具调用可以展示参数生成过程，有利于做 AI-native 的可见进度和调试体验。

## 资料可信度评估

- 来源层级：Tier 1
- 作者或机构可信度：OpenAI 官方文档，适合支持 OpenAI API 行为判断。
- 是否为一手资料：是。
- 是否有实验、数据、代码或可复现证据：有 API 示例和事件结构说明；本卡未做本地复现实验。
- 是否可能过时：是。工具类型、模型支持范围、API 默认值和限制可能变化。
- 是否存在商业宣传、立场偏差或上下文缺失：存在平台文档天然偏向 OpenAI 平台能力的可能；跨厂商抽象需要另查其他来源。

## 可引用事实

- OpenAI 文档将 function calling 又称为 tool calling，并说明它让模型连接应用提供的数据和动作。
- 工具调用流通常包含：请求模型并提供工具、收到工具调用、应用侧执行、回传工具输出、收到最终回复或更多工具调用。
- Function tool 由 schema 定义，custom tool 可使用自由文本输入输出。
- OpenAI tools 覆盖 function calling、web search、file search、remote MCP、computer use、code interpreter 等能力。
- Responses API 使用 Items 表达 message、function_call、function_call_output 等不同上下文单元。

## 关键主张表

| 主张 | 原始证据位置 | 可引用程度 | 局限 | 适合写入哪里 |
| --- | --- | --- | --- | --- |
| Tool calling 是模型请求工具、应用执行工具、再把输出回传模型的多步骤流程 | Function calling guide: tool calling flow | 高 | 适用于 OpenAI API；其他平台命名和封装可能不同 | `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md` |
| Function tool 是 JSON Schema 驱动的 tool 类型 | Function calling guide: Functions versus tools | 高 | schema 支持范围和严格模式默认值可能随 API 变化 | `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md` |
| 模型可能一次返回多个函数调用 | Function calling guide: Handling function calls | 高 | 具体模型和参数会影响行为 | `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md` |
| Strict mode 提高 schema 遵循可靠性，但要求 `additionalProperties: false` 且字段都 required | Function calling guide: Strict mode | 高 | 文档指出 Responses 与 Chat Completions 默认行为不同，需要按当前 API 确认 | `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md` |
| Responses API 更适合 agent-like 应用和工具循环 | Migrate to the Responses API guide | 中高 | 这是 OpenAI 平台内比较，不等于所有平台的通用结论 | `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md` |

## 机制解释

Tool calling 的关键机制不是“模型执行工具”，而是“模型生成结构化调用意图”。应用侧读取调用名和参数，根据本地权限、schema、业务规则和运行环境执行函数或工具，再把结果作为新的上下文项返回模型。模型基于工具结果继续推理、生成最终回答，或继续提出下一轮工具调用。

这个机制把自然语言决策与确定性系统能力连接起来：模型负责判断何时需要外部能力和如何填参数，应用负责验证、授权、执行、审计和错误处理。

## 适用范围

- 支持 OpenAI tool calling / function calling 概念卡。
- 支持 agents 架构中 tool router、permission boundary、response parser、trace logger 等模块设计。
- 支持 AI-native UI 中工具执行状态、流式参数、取消、重试、错误提示的交互设计。

## 局限与风险

- 本资料主要覆盖 OpenAI 平台，不足以代表 Anthropic、Google、LangGraph、AutoGen 等生态。
- 文档示例不等于生产安全策略；高风险工具仍需权限、确认、审计和回滚设计。
- 模型生成的参数即使符合 schema，也可能在业务语义上错误。
- 并行工具调用可能引入顺序、幂等性、资源锁和错误聚合问题。

## 与已有知识关联

- `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md`
- `tags.md`: `tool-calling`, `schema`, `permissions`, `streaming`, `observability`

## 短摘录

不保留长摘录。使用时引用官方文档，并在知识卡中用自己的话重建机制、边界和实践判断。

## 待验证问题

- 对当前常用 OpenAI SDK 版本，Responses API 与 Chat Completions 在 strict mode 默认行为上是否完全符合文档描述。
- 在真实项目中，多工具并行调用的错误聚合和幂等策略应如何设计。
- 跨厂商工具调用抽象是否能保持统一 schema、权限和审计模型。

## 变更记录

- 2026-06-08：创建官方资料引用卡。
