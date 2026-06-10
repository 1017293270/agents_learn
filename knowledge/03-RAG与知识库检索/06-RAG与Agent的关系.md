---
title: "RAG 与 Agent 的关系"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "RAG 与知识库检索参考资料"
    type: reference
    url: "../../90-references/rag-knowledge-retrieval-references.md"
    accessed: "2026-06-10"
  - title: "Agent 基础与工具调用参考资料"
    type: reference
    url: "../../90-references/agent-basics-tools-references.md"
    accessed: "2026-06-10"
  - title: "Building effective agents"
    type: article
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    accessed: "2026-06-10"
created: "2026-06-10"
updated: "2026-06-10"
tags: ["rag", "agent", "tool-calling", "memory", "workflow", "agent-architecture", "beginner"]
---

# RAG 与 Agent 的关系

## 一句话结论

RAG 是给模型补充外部知识的能力，tool calling 是让模型请求外部动作的机制，agent 则是把模型、知识、工具、状态、权限和评估组织起来完成任务的系统。

## 概念定位

- 它是什么：解释 RAG 在 agent 架构中的位置，以及它和 tool calling、memory、workflow 的边界。
- 它不是什么：不是把所有检索问答都叫 agent，也不是把所有 agent 都做成 RAG。
- 相邻概念：agent、tool calling、memory、planning、workflow、MCP、knowledge base。
- 前置知识：RAG 基础、agent 基础、tool calling、权限、eval。

初学者可以先记住：

```text
RAG 让模型“查资料”。
Tool calling 让模型“请求做事”。
Agent 让系统“围绕目标组织查资料和做事”。
```

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| RAG | Retrieval-Augmented Generation | 检索增强生成 | 让模型基于外部资料回答 |
| AI | Artificial Intelligence | 人工智能 | 让机器表现出智能行为的技术总称 |
| LLM | Large Language Model | 大语言模型 | agent 的推理和生成核心之一 |
| API | Application Programming Interface | 应用程序编程接口 | agent 调用工具或服务的接口 |
| MCP | Model Context Protocol | 模型上下文协议 | 标准化连接工具、资源和提示模板 |
| UI | User Interface | 用户界面 | 用户看到 agent 搜索、调用工具和回答的地方 |
| UX | User Experience | 用户体验 | 用户是否清楚 agent 在做什么、能否取消和信任 |
| Eval | Evaluation | 评估 | 检查 agent 和 RAG 是否真的可靠 |
| ACL | Access Control List | 访问控制列表 | 控制用户能看哪些资料或调用哪些工具 |

Workflow 不是缩写，指预先规定好的工作流程。Agent 不是缩写，在 AI 语境里指能围绕目标做决策和行动的系统单元。

## 核心概念

### 1. RAG 解决“知道什么”

RAG 主要回答：

```text
系统应该从哪些资料里找到依据？
这些资料是否支持答案？
答案应该引用哪里？
```

比如：

```text
“根据我的知识库，RLHF 是什么？”
```

这主要是 RAG 问题。

### 2. Tool calling 解决“调用什么能力”

Tool calling 主要回答：

```text
模型是否需要调用外部工具？
调用哪个工具？
参数是什么？
应用侧是否允许执行？
```

比如：

```text
“帮我把这篇笔记提交到 GitHub。”
```

这不是 RAG 本身，而是工具调用和权限问题。

### 3. Agent 解决“如何推进任务”

Agent 主要回答：

```text
为了完成目标，下一步应该查资料、调用工具、追问用户、还是停止？
```

比如：

```text
“帮我学习 RAG，并把知识补进我的知识库，再同步到网页。”
```

这个任务可能需要：

- 读取现有知识库。
- 搜索可靠来源。
- 写 Markdown 笔记。
- 更新索引。
- 校验 viewer manifest。
- 提交并推送 GitHub。

这就是 agent 风格任务：多步骤、多工具、有状态、有验证。

## 机制与原理

RAG 可以作为 agent 的一个工具或子系统。

```text
用户目标
  -> agent 判断需要知识
  -> 调用 retrieve_context 工具
  -> RAG 系统检索知识库
  -> 返回相关资料和来源
  -> agent 基于资料继续规划或回答
```

在这个结构里：

- RAG 不直接决定整个任务流程。
- Agent 不应该凭空回答知识问题。
- Tool calling 负责把 `retrieve_context`、`read_file`、`search_web` 等能力暴露出来。
- 权限系统负责决定 agent 能不能读取某些资料。
- Eval 负责检查检索和最终任务是否成功。

### 三种组合模式

#### 模式 1：普通 RAG 问答

```text
用户问题 -> 检索资料 -> 生成答案
```

适合：知识库问答、文档助手。

#### 模式 2：RAG as a tool

```text
agent -> 调用 retrieve_context -> 拿资料 -> 决定下一步
```

适合：代码助手、研究助手、复杂任务 agent。

#### 模式 3：Agentic RAG

```text
agent 分解问题
  -> 多轮检索
  -> 判断证据是否足够
  -> 必要时改写 query 或换工具
  -> 汇总答案
```

适合：复杂研究、多跳问答、跨文档推理。

风险：更慢、更贵、更难评估，也更容易走偏。

## 适用场景

- 个人知识库助手：根据你的 Markdown 笔记回答问题。
- 编程助手：先读项目文档、代码和测试，再提出修改。
- 研究助手：多轮检索论文、比较观点、记录证据。
- 客服 agent：先查知识库，再查订单工具，必要时人工转接。
- 企业内部助手：按权限检索文档，再执行流程工具。

## 不适用场景

- 只需要固定问答，不需要动态规划，用普通 RAG 就够。
- 只需要执行固定流程，不需要模型选择步骤，用 workflow 更稳。
- 只需要数据库精确查询，不需要 RAG。
- 高风险动作没有权限、确认和审计，不应交给 agent 自主决定。
- 资料质量差却想让 agent 自动做权威判断。

## 前提、边界与反例

- 必要前提：RAG 检索结果可追溯，agent 工具权限可控，任务目标可验证。
- 适用边界：RAG 能补知识，但不能替代工具执行；agent 能组织流程，但不能替代权限系统。
- 反例或例外：一个简单 FAQ 网站不一定需要 agent；一个自动转账流程不应该靠 RAG 判断是否付款。
- 结论可能失效的条件：知识库无来源、检索不可靠、工具权限过大、agent 无停止条件、eval 缺失。

## 对比与替代方案

| 概念 | 主要解决 | 典型问题 | 不擅长 |
| --- | --- | --- | --- |
| Prompt | 怎么问模型 | “请按这个格式总结” | 外部知识和真实动作 |
| RAG | 从哪里找资料 | “根据文档回答” | 执行动作、长期状态 |
| Tool calling | 怎么请求工具 | “查订单、读文件、发请求” | 判断资料是否完整 |
| Memory | 记住什么 | “记住用户偏好和历史状态” | 大规模知识检索 |
| Workflow | 固定流程怎么走 | “审核通过后发通知” | 开放式任务规划 |
| Agent | 如何围绕目标推进 | “查资料、调用工具、校验、交付” | 无边界高风险自治 |

## 示例或最小实验

任务：

```text
用户：帮我解释 RAG，并把解释写进我的 agents 学习知识库。
```

一个 agent 可能这样做：

```text
1. 读取 INDEX.md，判断是否已有 RAG 章节。
2. 如果没有，创建第三章目录。
3. 检索 RAG 可靠来源。
4. 写 RAG 基础笔记。
5. 更新 viewer/manifest.json。
6. 校验 manifest JSON。
7. 提交并推送。
```

其中：

- 第 1 步和第 5-7 步是工具调用和文件操作。
- 第 3 步是检索来源，属于 RAG/资料检索。
- 第 4 步是生成知识卡。
- 整体任务编排是 agent 行为。

如果只是问：

```text
RAG 是什么？
```

那普通 RAG 问答就够，不需要复杂 agent。

## 失败模式与风险

- 把 RAG 当 agent：只会检索回答，却声称能完成任务。
- 把 agent 当 RAG：agent 凭模型常识回答，不查知识库。
- 工具和检索混淆：应该查数据库，却去文档里猜。
- Memory 和 RAG 混淆：把大量知识塞进长期 memory，导致污染和难维护。
- Agentic RAG 过度复杂：简单问题也多轮检索，成本高、延迟大。
- 权限断裂：RAG 检索绕过了 agent 的用户权限。
- 评估不完整：只评估答案，不评估工具调用和检索证据。
- UI 不透明：用户不知道 agent 是在查资料还是在执行动作。

## 常见误区

- 误区：RAG 就是 agent。
  - 修正：RAG 是知识检索增强能力，agent 是任务执行系统。
- 误区：agent 有 memory 就不需要 RAG。
  - 修正：memory 适合保存偏好和状态，RAG 适合检索大量外部知识。
- 误区：只要有 tool calling，就不需要 RAG。
  - 修正：工具能查数据或执行动作，但知识问答仍需要检索、引用和证据判断。
- 误区：Agentic RAG 一定比普通 RAG 高级。
  - 修正：复杂任务才需要多轮检索；简单问答应保持简单。
- 误区：RAG 可以替代权限系统。
  - 修正：检索前就要按用户权限过滤资料。

## 实践判断

- 什么时候用普通 RAG：问题是知识问答，资料范围明确，不需要多步工具。
- 什么时候用 RAG as a tool：agent 在执行任务时需要查资料作为中间依据。
- 什么时候用 agentic RAG：问题复杂，需要多轮检索、比较、澄清或跨文档推理。
- 什么时候不用 RAG：需要精确业务数据、实时状态或真实动作时，优先 API/tool。
- 落地时最先验证什么：agent 是否在该查资料时查资料，在该调用工具时调用工具，在证据不足时停止或追问。

## 来源与证据

- 来源：`90-references/rag-knowledge-retrieval-references.md`；`90-references/agent-basics-tools-references.md`；Anthropic Building effective agents。
- 证据摘要：RAG 资料支持检索增强生成的知识访问角色；agent 资料支持模型动态决定流程和工具使用；本卡对 RAG/tool/memory/workflow/agent 的边界划分是工程综合判断。
- 可信度判断：RAG、tool calling、agent 的职责差异可信度高；agentic RAG 是否值得引入取决于任务复杂度、评估能力和成本约束。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| RAG 主要解决外部知识访问 | RAG 原论文与 RAG 工程文档 | RAG references | high | 现代系统还会加入多步推理 |
| Agent 组织模型、工具、状态和流程 | OpenAI Agents SDK 与 Anthropic 工程文章 | Agent references | high | 框架定义不同 |
| Tool calling 与 RAG 可以组合 | RAG 检索可作为 agent 工具 | 工程推断 | high | 具体接口需设计 |
| Agentic RAG 更复杂且需要 eval | 多轮检索增加成本和失败路径 | 工程推断 | medium | 复杂任务可能收益明显 |

## 待验证问题

- 本知识库未来是否需要做一个 `retrieve_note` 工具，让 agent 先查自己的笔记再回答。
- RAG 检索结果是否应该进入 agent memory，还是只作为当前任务上下文。
- 简单问答和复杂研究任务如何自动路由到普通 RAG 或 agentic RAG。
- UI 是否应该区分“正在检索资料”和“正在执行工具动作”。

## 变更记录

- 2026-06-10：创建深度初稿，补充 RAG、tool calling、memory、workflow、agent 的关系、组合模式和边界。
