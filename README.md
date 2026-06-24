# Agents 学习知识库

这是一个 Markdown-first 的 agents 学习知识库。默认用法很简单：你告诉我最近学了什么，我帮你扩展相关知识，整理成一篇 Markdown 笔记，并按模块放进 `knowledge/`。

核心原则：
- 可靠优先于速度。
- 深度优先于堆资料。
- 明确事实、推断、经验和待验证问题。
- 每个重要知识点都要能追溯来源、边界、反例和实践判断。

## 目录

| 目录 | 用途 |
| --- | --- |
| `knowledge/` | 默认知识笔记文件夹，里面按“模块目录 -> 编号小节文件”分类 |
| `90-references/` | 必要时保存资料来源和官方文档评估 |
| `templates/` | 笔记模板和质检模板 |
| `INDEX.md` | 知识索引 |
| `tags.md` | 标签体系 |

## 推荐工作流

1. 你告诉我：最近学了什么。
2. 我判断主题，并搜索 `knowledge/` 里是否已有相关笔记。
3. 我把它扩展成一篇知识笔记：核心点、相关知识、机制、例子、适用场景、踩坑点、来源和未解问题。
4. 笔记统一写入 `knowledge/模块目录/编号-主题.md`。
5. 如果是重要主题，我再补充来源、关键主张和更深的边界分析。

## 当前模块

| 模块 | 目录 | 用途 |
| --- | --- | --- |
| 01 | `knowledge/01-大模型的使用与训练/` | 大模型基础、Prompt、推理部署、SFT、RLHF、模型对比 |
| 02 | `knowledge/02-Agent基础与工具调用/` | Agent 基础、tool calling、工具安全、MCP、评估 |
| 03 | `knowledge/03-RAG与知识库检索/` | RAG、embedding、语义搜索、文档切分、索引、失败模式 |
| 04 | `knowledge/04-神经网络训练与优化/` | 神经网络基础、因子组合、损失、梯度、优化器、训练执行 |

## 模板选择

| 模板 | 用途 |
| --- | --- |
| `templates/simple-learning-note.md` | 默认日常学习笔记 |
| `templates/knowledge-card.md` | 更严谨的深度知识卡 |
| `templates/experiment-log.md` | 实验、实践、调试记录 |
| `templates/source-review.md` | 资料、论文、官方文档评估 |
| `templates/ui-spec.md` | OpenAI-inspired UI 规范和界面方案 |
| `templates/claim-audit.md` | 关键主张逐条证据审查 |
| `templates/knowledge-review.md` | 知识卡完整性与深度质检 |

## 深度标准

普通学习笔记使用 `depth: standard`。

重要 agents 主题默认使用 `depth: deep`，尤其是：
- agent 架构
- tool calling
- RAG
- memory
- planning
- multi-agent
- evaluation
- safety
- model behavior
- AI-native UI

`depth: deep` 的笔记必须包含机制、边界、反例、替代方案、失败模式、关键主张证据和待验证问题。这个作为后台质量标准，不需要你手动指定格式。

## 入口规则

项目级规则见 `AGENTS.md`。以后让 AI 补充知识时，可以直接说：

```text
我最近学了 tool calling，帮我扩展一下相关知识。
```

如果来源不够清楚，知识点必须保持 `status: unverified`，不能因为解释流畅就标记为可靠。

## 当前入口

- 默认笔记文件夹：`knowledge/`
- 可视化浏览页：`viewer/index.html`
- 总索引：`INDEX.md`
- 标签体系：`tags.md`
- 第一张知识笔记：`knowledge/01-大模型的使用与训练/02-Prompt工程.md`
- Agent 工具调用模块：`knowledge/02-Agent基础与工具调用/`
- RAG 与知识库检索模块：`knowledge/03-RAG与知识库检索/`
- 神经网络训练与优化模块：`knowledge/04-神经网络训练与优化/`
- 部署说明：`DEPLOY.md`

## 打开可视化界面

推荐在 PowerShell 里运行：

```powershell
cd D:\agents学习
python -m http.server 8765 --bind 127.0.0.1
```

也可以直接运行项目里的脚本：

```powershell
cd D:\agents学习
.\run-viewer.ps1
```

然后访问：

```text
http://127.0.0.1:8765/viewer/
```

如果页面显示 `manifest.json 读取失败`，先确认命令是在 `D:\agents学习` 目录运行的，然后刷新浏览器页面。

新增知识笔记后，同步更新 `viewer/manifest.json`，界面就能展示新内容。

## 部署

这套知识库是静态网站，可以部署到 GitHub Pages、Vercel、Netlify 或任意静态文件服务器。

详情见 `DEPLOY.md`。
