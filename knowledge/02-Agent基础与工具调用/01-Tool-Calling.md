---
title: "Tool Calling"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "OpenAI Function Calling and Tools"
    type: official-doc
    url: "../../90-references/openai-function-calling.md"
    accessed: "2026-06-08"
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
tags: ["agent", "tool-calling", "openai", "schema", "permissions", "streaming", "observability"]
---

# Tool Calling

## 一句话结论

Tool calling 是让模型提出“要调用什么工具、带什么参数”的结构化请求，由应用侧验证、授权、执行并回传结果，从而把语言模型连接到外部数据、代码和行动能力的 agent 基础机制。

## 概念定位

- 它是什么：一种模型和应用协作的控制协议。模型生成工具调用意图，应用执行真实工具，模型再基于工具结果继续回答或继续调用工具。
- 它不是什么：不是模型直接拥有外部系统权限，也不是让模型绕过业务校验执行任意代码。
- 相邻概念：function calling、structured output、RAG、actions、MCP、agent tool router、workflow engine。
- 前置知识：JSON Schema、API request/response、权限模型、错误处理、幂等性、日志与审计。

## 核心概念

Tool calling 通常包含四类对象：

- Tool definition：应用暴露给模型的工具说明，包括名称、描述、参数 schema、返回格式和调用边界。
- Tool call：模型在响应中生成的工具调用请求，通常包括工具名、调用 ID 和参数。
- Tool executor：应用侧负责验证参数、检查权限、执行函数、处理错误和记录审计的代码。
- Tool output：应用把执行结果绑定到对应调用 ID 后回传给模型的上下文。

Function calling 是 tool calling 的一种常见形式：工具参数由 JSON Schema 定义，模型按 schema 生成参数，应用解析并执行本地函数。更广义的 tools 还可以包括内置 web search、file search、computer use、remote MCP、自定义自由文本工具等。

## 机制与原理

一个最小 tool calling 循环如下：

1. 应用向模型发送用户输入和可用工具列表。
2. 模型判断是否需要工具；如果需要，返回一个或多个 tool call。
3. 应用解析 tool call，校验 schema、权限、业务约束和风险等级。
4. 应用执行真实工具，例如查数据库、调用 API、搜索文件、发起业务动作。
5. 应用把工具输出与调用 ID 一起回传给模型。
6. 模型基于工具输出生成最终回答，或继续请求更多工具调用。

关键点是职责分离：模型负责“选择和组织意图”，应用负责“能否执行、如何执行、执行后如何审计”。这让系统既能利用模型的自然语言理解和规划能力，又能把真实副作用保留在可控代码边界内。

## 适用场景

- 需要访问模型训练数据之外的信息，例如实时天气、库存、订单、内部知识库。
- 需要执行确定性业务逻辑，例如计算价格、查询权限、生成报表、更新任务状态。
- 需要把 agent 拆成工具生态，例如搜索、读取文件、写代码、运行测试、调用专家子系统。
- 需要可观察和可审计的 AI 行动，而不是让模型只输出自然语言建议。
- 需要用户界面展示“模型正在调用哪个工具、参数是什么、结果是什么”的 AI-native 过程。

## 不适用场景

- 纯文本生成已经足够，外部数据或动作不会改善答案。
- 工具副作用高风险，但没有权限、确认、审计和回滚机制。
- 参数语义复杂到 schema 无法表达，且应用侧也没有额外验证。
- 对延迟极端敏感，工具循环的额外往返不可接受。
- 只需要固定工作流，不需要模型动态选择工具；此时普通后端流程或 workflow engine 更稳定。

## 前提、边界与反例

- 必要前提：工具描述清晰，schema 可验证，执行器可信，权限边界明确，错误形态可回传。
- 适用边界：tool calling 只提高模型连接外部能力的能力，不保证工具选择一定正确。
- 反例或例外：如果系统只需要“每天固定拉取数据并生成摘要”，定时任务加模板可能比 tool calling 更简单。
- 结论可能失效的条件：模型选择错误工具、参数符合 schema 但业务语义错误、工具结果被恶意内容污染、工具调用缺少审计。

## 对比与替代方案

| 方案 | 优势 | 劣势 | 适合场景 |
| --- | --- | --- | --- |
| Tool calling | 动态、可扩展、能连接外部数据和动作 | 需要 schema、权限、错误处理和审计 | agent、动态问答、复杂操作 |
| Structured output | 输出格式稳定，易解析 | 不执行外部能力 | 分类、抽取、生成结构化 JSON |
| RAG | 引入外部知识，通常无副作用 | 主要解决信息访问，不解决行动执行 | 文档问答、知识检索 |
| 固定 workflow | 稳定、可测试、可预测 | 不灵活，难处理开放式用户意图 | 明确业务流程 |
| 纯自然语言建议 | 实现简单 | 不可执行、不可审计，用户需手动操作 | 低风险解释和建议 |

## 示例或最小实验

最小伪代码：

```typescript
const tools = [{
  type: "function",
  name: "get_order_status",
  description: "Query an order status by order id.",
  parameters: {
    type: "object",
    properties: {
      order_id: { type: "string" }
    },
    required: ["order_id"],
    additionalProperties: false
  },
  strict: true
}];

const response = await model.respond({ input: userMessage, tools });

for (const call of response.output.filter(item => item.type === "function_call")) {
  assertAllowedTool(call.name);
  const args = parseAndValidate(call.arguments);
  await assertUserCanAccessOrder(currentUser, args.order_id);
  const result = await executeTool(call.name, args);
  input.push({
    type: "function_call_output",
    call_id: call.call_id,
    output: JSON.stringify(result)
  });
}

const finalResponse = await model.respond({ input, tools });
```

这个实验要观察四件事：模型是否选择了正确工具、参数是否能通过 schema、业务权限是否被应用拦住、工具输出是否能让模型生成可用最终回答。

## 失败模式与风险

- 工具选择错误：模型选择了不适合当前任务的工具。
- 参数幻觉：参数格式正确，但实体 ID、时间范围、用户意图错误。
- Schema 过宽：`additionalProperties` 未限制，导致多余字段进入执行器。
- 权限绕过：工具执行前没有按用户身份做授权。
- 间接提示注入：检索结果或网页内容诱导模型调用高风险工具。
- 高风险副作用：删除、付款、发消息、发布生产变更等动作没有二次确认。
- 并行调用冲突：多个工具调用同时改同一资源，产生顺序和幂等问题。
- 错误不可恢复：工具失败后只把异常抛给模型或用户，没有重试、降级和可理解错误。
- 审计缺失：无法追踪模型为什么调用、调用了什么、参数是什么、执行结果是什么。

## 常见误区

- 误区：用了 tool calling，模型就能安全执行动作。
  - 修正：安全来自应用侧权限、确认、审计、幂等和回滚，不来自模型本身。
- 误区：schema 正确就代表业务语义正确。
  - 修正：schema 只能约束形状，业务语义需要服务层校验。
- 误区：工具越多越强。
  - 修正：工具太多会增加选择错误、上下文成本和维护复杂度。
- 误区：工具调用失败就是模型失败。
  - 修正：失败可能来自工具超时、权限、外部 API、schema、网络或业务规则。

## 实践判断

- 什么时候应该采用：用户意图开放，外部数据或动作对答案质量关键，且可以定义清楚工具边界。
- 什么时候应该谨慎：工具有高风险副作用、参数难验证、权限模型不成熟、缺少审计。
- 落地时最先验证什么：工具选择准确率、参数 schema 遵循率、权限拦截、错误恢复、审计完整性。
- 可观察指标或检查点：工具调用成功率、参数校验失败率、权限拒绝率、平均工具延迟、重试率、用户取消率、人工确认通过率。

## 来源与证据

- 来源：`90-references/openai-function-calling.md`；OpenAI Function calling、Using tools、Migrate to Responses API 官方文档。
- 证据摘要：官方文档说明 tool calling 的五步流程、function tool 与 custom tool 的区别、Responses API 的工具能力、`tool_choice`、并行调用和 strict mode 配置。
- 可信度判断：核心机制来自 Tier 1 官方来源，可信度高；生产安全策略部分是工程推断，来自本知识库全局安全规则和常见后端边界实践，仍需项目实验验证。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| Tool calling 是模型请求工具、应用执行工具、结果回传模型的多步骤流程 | OpenAI 官方 guide 列出请求、接收 tool call、应用执行、回传输出、收到最终响应的流程 | OpenAI Function calling | high | OpenAI 平台表述，其他平台可能有不同对象名 |
| Function tool 是 JSON Schema 驱动的 tool 类型 | 官方文档区分 function tools、custom tools 和 built-in tools | OpenAI Function calling | high | schema 支持范围和默认 strict 行为可能随 API 更新 |
| 模型可能返回多个工具调用 | 官方文档建议假设响应中可能有 zero、one 或 multiple calls | OpenAI Function calling | high | 并行行为受模型、API 和参数影响 |
| `strict: true` 有助于 schema 遵循 | 官方文档建议启用 strict mode，并说明其 schema 要求 | OpenAI Function calling | high | strict 只保证形状更可靠，不保证业务语义正确 |
| 高风险工具必须由应用侧控制 | 模型只生成调用请求，真实执行发生在应用侧；安全要求来自权限和审计边界 | OpenAI docs + 工程推断 | medium | 需要结合具体项目权限模型验证 |

## 待验证问题

- 在当前 OpenAI SDK 和目标模型下，strict mode、parallel tool calls、Responses API 默认 schema 归一化的真实行为是否与官方文档一致。
- 多工具场景下，工具数量和描述质量如何影响工具选择准确率。
- 高风险工具的确认策略应该由模型提示、服务端策略还是 UI 交互共同决定。
- 工具返回错误时，哪些错误适合让模型继续推理，哪些错误应该直接给用户或触发人工处理。

## 变更记录

- 2026-06-08：创建 `depth: deep` 初稿，基于 OpenAI 官方文档建立机制、边界、风险和关键主张表。
