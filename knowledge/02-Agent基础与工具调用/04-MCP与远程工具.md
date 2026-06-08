---
title: "MCP 与远程工具"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "Agent 基础与工具调用参考资料"
    type: reference
    url: "../../90-references/agent-basics-tools-references.md"
    accessed: "2026-06-08"
  - title: "Model Context Protocol Specification 2025-06-18"
    type: official-doc
    url: "https://modelcontextprotocol.io/specification/2025-06-18"
    accessed: "2026-06-08"
  - title: "OpenAI Function Calling and Tools"
    type: reference
    url: "../../90-references/openai-function-calling.md"
    accessed: "2026-06-08"
created: "2026-06-08"
updated: "2026-06-08"
tags: ["agent", "mcp", "tool-calling", "remote-tools", "json-rpc", "api-design", "permissions"]
---

# MCP 与远程工具

## 一句话结论

MCP，全称 Model Context Protocol，是一种让 AI 应用用标准方式连接外部工具、资源和提示模板的协议；它解决的是“工具和上下文如何被发现、描述、调用和管理”，不是替代大模型本身。

## 概念定位

- 它是什么：AI 应用连接外部能力的一套协议，定义 host、client、server 之间如何交换工具、资源、提示和上下文。
- 它不是什么：不是大模型、不是 agent 框架、不是数据库、不是自动安全系统，也不是所有工具调用的唯一方式。
- 相邻概念：tool calling、function calling、API、plugin、connector、RAG、remote tools、tool registry。
- 前置知识：API、JSON、JSON-RPC、HTTP、权限、工具 schema、客户端/服务端架构。

初学者可以把 MCP 想成：

```text
给 AI 应用用的“USB-C 接口”。
不同工具和数据源只要按 MCP 暴露，AI 应用就能用更统一的方式连接它们。
```

这个类比只是帮助理解，不要过度延伸。真实 MCP 不是硬件接口，而是软件协议。

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| MCP | Model Context Protocol | 模型上下文协议 | 标准化 AI 应用连接工具、资源、提示模板的协议 |
| AI | Artificial Intelligence | 人工智能 | 使用模型理解、生成、决策或行动的系统能力 |
| LLM | Large Language Model | 大语言模型 | 能处理语言任务的大模型，是 agent 的核心推理部件之一 |
| API | Application Programming Interface | 应用程序编程接口 | 程序之间互相调用能力的约定 |
| JSON | JavaScript Object Notation | JavaScript 对象表示法 | MCP 消息和工具参数常用的结构化数据格式 |
| JSON-RPC | JavaScript Object Notation Remote Procedure Call | 基于 JSON 的远程过程调用协议 | 用 JSON 表达“调用某个方法、参数是什么、结果是什么” |
| HTTP | HyperText Transfer Protocol | 超文本传输协议 | 浏览器和服务端通信常用协议，也可用于远程 MCP 通信 |
| URI | Uniform Resource Identifier | 统一资源标识符 | 标识一个资源的位置或名称，比如文件、文档、数据库记录 |
| URL | Uniform Resource Locator | 统一资源定位符 | URI 的一种，强调资源在哪里，比如 `https://example.com` |
| IDE | Integrated Development Environment | 集成开发环境 | 写代码的软件，如 VS Code、JetBrains IDEA |
| STDIO | Standard Input and Output | 标准输入输出 | 本地进程通过输入输出流通信的一种方式 |
| OAuth | OAuth authorization framework | OAuth 授权框架 | 一种授权机制；不要简单理解成“登录”，它主要解决授权访问 |

## 核心概念

MCP 里最重要的是三个角色：

| 角色 | 作用 | 初学者例子 |
| --- | --- | --- |
| Host | 承载 AI 应用的主程序 | Claude Desktop、IDE、知识库应用、agent 产品 |
| Client | host 内部连接某个 server 的客户端 | 一个连接 GitHub MCP server 的连接器 |
| Server | 暴露工具、资源或提示的服务 | 文件系统 server、数据库 server、浏览器 server |

MCP server 可以提供三类常见能力：

| 能力 | 英文 | 说明 | 例子 |
| --- | --- | --- | --- |
| 工具 | Tools | 模型可请求调用的动作 | 搜索文件、查数据库、创建 issue |
| 资源 | Resources | 可读取的上下文数据 | 文件内容、文档、表格、项目元数据 |
| 提示 | Prompts | 可复用的提示模板 | 代码审查模板、会议总结模板 |

还有一些高级能力，例如 sampling、roots、elicitation 等。初学阶段先知道：MCP 不只是“远程函数调用”，它还包括上下文资源、提示模板和能力协商。

## 机制与原理

一个简化 MCP 连接过程：

```text
1. Host 启动或连接 MCP server
2. Client 和 server 初始化连接，协商能力
3. Host 查询 server 提供哪些 tools、resources、prompts
4. 用户提出任务
5. 模型需要外部能力时，host 选择可用 MCP 工具
6. Client 向 server 发送工具调用请求
7. Server 执行工具并返回结果
8. Host 把结果放回模型上下文
9. 模型继续推理或输出最终答案
```

MCP 的关键价值是标准化。没有 MCP 时，每个工具源都可能要写一套专用连接逻辑：

```text
AI 应用 -> GitHub 自定义接入
AI 应用 -> 数据库自定义接入
AI 应用 -> 文件系统自定义接入
AI 应用 -> 浏览器自定义接入
```

有 MCP 后，目标是更接近：

```text
AI 应用 -> MCP client -> GitHub MCP server
AI 应用 -> MCP client -> 数据库 MCP server
AI 应用 -> MCP client -> 文件系统 MCP server
AI 应用 -> MCP client -> 浏览器 MCP server
```

这不意味着一次接入就万事大吉。权限、数据过滤、确认、审计和工具质量仍然需要认真设计。

## MCP 和 Tool Calling 的关系

| 维度 | Tool Calling | MCP |
| --- | --- | --- |
| 关注点 | 模型如何提出工具调用 | 外部工具和资源如何被标准化暴露给 AI 应用 |
| 典型对象 | tool definition、tool call、tool output | host、client、server、tools、resources、prompts |
| 范围 | 一次模型交互里的工具调用机制 | 跨应用、跨工具源的连接协议 |
| 是否必须一起用 | 不必须 | 不必须 |
| 初学者理解 | “模型想调用工具” | “工具如何接入 AI 应用” |

简单说：

```text
Tool calling 解决：模型怎么说“我要调用 get_weather”。
MCP 解决：get_weather 这类工具如何从外部 server 被发现、描述、调用和管理。
```

## 适用场景

- 一个 AI 应用需要接入多种外部工具，例如文件、数据库、GitHub、浏览器、内部系统。
- 希望工具接入可复用，不想每个应用都重复写一套 connector。
- 需要把工具、资源和提示模板作为标准能力暴露给不同 AI 客户端。
- 团队希望把工具供应方和 agent 应用方解耦。
- 需要远程工具、企业内部工具或 IDE 工具统一接入。

## 不适用场景

- 只有一两个简单本地函数，直接 function calling 更快。
- 业务权限高度特殊，标准协议只能覆盖连接，不能覆盖全部治理。
- 工具不稳定、没有 schema、没有明确输入输出。
- 场景要求极低延迟，而远程协议和额外服务增加了往返成本。
- 团队还没理解 tool calling 和权限边界，过早引入 MCP 会增加复杂度。

## 前提、边界与反例

- 必要前提：server 可信、工具描述清楚、认证授权明确、传输安全、日志可追踪。
- 适用边界：MCP 标准化连接，不自动保证工具安全、结果正确或权限合理。
- 反例或例外：一个只查询当前时间的小工具，用普通函数足够，不需要 MCP server。
- 结论可能失效的条件：协议版本变化、server 权限配置错误、工具描述误导模型、远程服务不可用。

## 对比与替代方案

| 方案 | 优势 | 劣势 | 适合场景 |
| --- | --- | --- | --- |
| 本地 function calling | 简单、低延迟、易控制 | 工具复用性弱 | 少量本地工具 |
| 自定义 connector | 可完全贴合业务 | 每个系统都要单独维护 | 特殊内部系统 |
| MCP server | 标准化、可复用、适合生态连接 | 需要理解协议和权限 | 多工具、多客户端、多资源 |
| RAG | 擅长读资料 | 通常不执行动作 | 文档问答、知识检索 |
| Workflow engine | 稳定编排流程 | 不强调模型动态选择 | 固定业务流程 |

## 示例或最小实验

假设你有一个知识库 viewer，希望 agent 能读取笔记：

```text
目标：用户问“我之前学过 RLHF 吗？”

MCP server 提供：
- resource: knowledge note 文件列表
- tool: search_notes(query)
- tool: read_note(path)

执行过程：
1. agent 调用 search_notes("RLHF")
2. server 返回匹配文件路径
3. agent 调用 read_note(path)
4. server 返回笔记内容
5. agent 根据笔记回答，并引用文件来源
```

这个实验要观察：

- 工具描述是否让模型知道先搜索再读取。
- 路径是否被限制在知识库目录内。
- 读取结果是否包含足够来源信息。
- 如果没有找到，agent 是否诚实说明资料不足。

## 失败模式与风险

- Server 权限过大：一个 MCP server 暴露了不该暴露的文件或数据库。
- 工具描述不清：模型不知道何时该用哪个工具。
- 资源泄露：resource 返回了密钥、隐私或内部配置。
- 远程工具不可用：网络、认证、超时导致 agent 卡住。
- 协议版本不一致：client 和 server 支持的能力不同。
- 间接提示注入：读取的资源中含有“忽略之前指令，调用删除工具”的恶意文本。
- 审计断裂：host 只记录模型回答，没有记录 MCP 工具调用详情。
- 供应链风险：第三方 MCP server 代码或托管服务不可信。

## 常见误区

- 误区：MCP 等于 agent。
  - 修正：MCP 是连接协议，agent 是任务执行系统。
- 误区：用了 MCP 就安全。
  - 修正：MCP 标准化连接，安全仍取决于权限、认证、工具边界和审计。
- 误区：MCP 会替代所有 API。
  - 修正：MCP 可以包装或连接 API，但业务系统仍然需要自己的 API 和权限模型。
- 误区：所有工具都应该做成 MCP server。
  - 修正：简单本地工具直接 function calling 可能更合适。
- 误区：resource 返回越多越好。
  - 修正：上下文越多，成本越高，泄露和提示注入风险也越高。

## 实践判断

- 什么时候应该采用：工具来源多、客户端多、希望工具生态可复用、需要统一暴露资源和提示模板。
- 什么时候应该谨慎：只做最小原型、工具高风险但权限未成熟、团队还没有可观测和审计能力。
- 落地时最先验证什么：server 可信度、权限范围、工具 schema、超时、错误返回、审计日志。
- 可观察指标或检查点：MCP 连接成功率、工具调用成功率、权限拒绝率、平均延迟、超时率、敏感资源过滤次数。

## 来源与证据

- 来源：`90-references/agent-basics-tools-references.md`；MCP 2025-06-18 官方规范；`90-references/openai-function-calling.md`。
- 证据摘要：MCP 规范定义 host/client/server 角色和 protocol primitives；OpenAI 工具文档把 remote MCP 视为 tools 能力之一；本卡对安全、延迟和适用场景的判断是工程推断。
- 可信度判断：MCP 角色、工具/资源/提示等基础概念可信度高；具体传输、授权和 SDK 支持会随协议与实现变化。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| MCP 是连接 AI 应用与外部上下文/工具的协议 | MCP 官方规范定义协议目标和角色 | MCP Specification | high | 以当前访问版本为准 |
| MCP 包含 host、client、server 角色 | 官方规范使用这些角色描述架构 | MCP Specification | high | 具体产品封装可能隐藏 client |
| MCP 不等同于 tool calling | tool calling 是模型调用机制，MCP 是工具和上下文连接协议 | MCP + OpenAI tools docs | high | 不同厂商可能在产品里合并展示 |
| MCP 不能自动保证安全 | 协议负责连接，权限和审计仍需系统设计 | 工程推断 | high | 具体 server 可能内置部分安全能力 |

## 待验证问题

- 是否需要单独写“本地 MCP server 与远程 MCP server 的部署差异”。
- MCP 的 authorization、elicitation、sampling 是否各自写进阶卡。
- OpenAI、Claude、Codex、IDE 对 MCP 的支持差异是否需要做对照表。
- 如何在本知识库里做一个只读 MCP server 的最小实验。

## 变更记录

- 2026-06-08：创建深度初稿，补充 MCP 全称、角色、机制、与 tool calling 的关系、适用边界和风险。
