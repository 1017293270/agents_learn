# Agents Learning Knowledge Base Instructions

## 0. Project Purpose

This repository is a Markdown-first knowledge base for learning AI agents.

Primary goals:
- Keep agent-related knowledge clear, source-aware, and easy to extend.
- Turn loose notes into reliable evidence cards.
- Preserve uncertainty instead of rewriting guesses as facts.
- Help the user gradually build a structured, reviewable learning system.
- Keep the user-facing workflow simple: the user says what they learned, and the assistant expands it into a useful note.

Default language: Chinese.

Default assistant role: organizing and quality-checking assistant. The assistant should classify,
normalize, supplement, and verify notes. It should not casually expand content without provenance.

## 1. Rule Hierarchy

Project-level instructions in this file extend, but do not weaken, the global standards.

Always follow:
- `~/.claude/rules/common/coding-style.md`
- `~/.claude/rules/common/patterns.md`
- `~/.claude/rules/common/security.md`
- `~/.claude/rules/common/testing.md`

For UI, frontend, dashboard, or interaction work, also follow:
- `~/.claude/rules/web/design-quality.md`
- `~/.claude/rules/web/coding-style.md`
- `~/.claude/rules/web/patterns.md`
- `~/.claude/rules/web/performance.md`
- `~/.claude/rules/web/security.md`
- `~/.claude/rules/design/motion-philosophy.md`

For this knowledge base:
- Do not invoke Superpowers, subagents, or multi-agent workflows unless the user explicitly asks.
- Do not create a documentation site, database, build system, or large toolchain unless requested.
- Prefer small, readable Markdown files over complex automation.
- When a claim may be current or time-sensitive, verify it before marking it as reliable.

## 2. Simple Learning Workflow

Default workflow:

1. The user says what they recently learned.
2. The assistant identifies the core topic and related knowledge.
3. The assistant expands it with definitions, mechanisms, examples, boundaries, risks, and sources.
4. The assistant writes or updates one Markdown note in the right module under `knowledge/`.
5. The assistant updates `INDEX.md`, `tags.md`, and `viewer/manifest.json` only when useful.

Default target folder:
- Put expanded learning notes under a numbered module folder inside `knowledge/`.
- Use `knowledge/MM-模块名/NN-小节标题.md`, for example `knowledge/01-大模型的使用与训练/02-Prompt工程.md`.
- If the learned topic belongs to a new major category, create the next numbered module folder first.
- The first required module is `knowledge/01-大模型的使用与训练/`.
- Do not ask the user to choose a folder unless the topic is genuinely ambiguous.

What "expand related knowledge" means:
- Add the main concept the user learned.
- Add neighboring concepts that are necessary to understand it.
- Add common patterns, failure modes, and practical judgment.
- Add sources when claims depend on current or external facts.
- Keep uncertainty visible when evidence is incomplete.

Do not create parallel topic-type folders at the repository root. Keep learning notes inside
numbered module folders under `knowledge/`.

## 3. Module Router

Before adding or editing knowledge, decide the target module and numbered lesson file under `knowledge/`.

| Module | Purpose | Use When |
| --- | --- | --- |
| `knowledge/01-大模型的使用与训练/` | LLM use and training | Model basics, prompt engineering, inference, deployment, SFT, RLHF, model comparison |
| `knowledge/02-Agent基础与工具调用/` | Agent basics and tool use | Agent basics, tool calling, tool schemas, tool safety, tool execution |
| `knowledge/MM-新模块名/` | New learning category | Create when the user's topic does not fit existing modules |
| `90-references/` | Source index | Papers, official docs, articles, courses, books, videos |
| `templates/` | Reusable templates | Note templates, claim audits, and quality review templates |
| `viewer/` | Local visual browser | Static UI for browsing notes by section, tag, status, and search |

If the correct module is unclear, create a short module README that explains the category, or ask
the user only when multiple module choices would materially change how the knowledge is organized.

## 4. File Naming

Use stable, searchable names.

- Concept and pattern notes inside modules: `NN-小节标题.md`, for example `01-Tool-Calling.md`.
- Default learning notes: `knowledge/MM-模块名/NN-小节标题.md`, for example `knowledge/01-大模型的使用与训练/02-Prompt工程.md`.
- Practice notes: `YYYY-MM-DD-short-topic.md`, for example `2026-06-08-agent-memory-test.md`.
- Reference notes: `source-title-or-topic.md`, for example `openai-agents-sdk-docs.md`.
- UI specs: `ui-short-topic.md`, for example `ui-agent-chat-workspace.md`.
- Keep the filename concise. Put the full Chinese title in frontmatter.

## 5. Required Frontmatter

Every knowledge file must start with this frontmatter shape:

```yaml
---
title: ""
type: concept
status: draft
confidence: unknown
depth: standard
source: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
tags: []
---
```

Allowed `type` values:
- `inbox`
- `concept`
- `pattern`
- `practice`
- `project`
- `ui`
- `reference`

Allowed `status` values:
- `inbox`: captured but not organized
- `draft`: organized but not fully checked
- `verified`: source-backed and reviewed
- `unverified`: source unclear or claim not checked
- `deprecated`: kept for history but no longer recommended

Allowed `confidence` values:
- `high`: official source, primary source, or reproduced experiment supports the claim
- `medium`: credible secondary source or partial experiment supports the claim
- `low`: plausible but weakly supported
- `unknown`: not assessed yet

Allowed `depth` values:
- `capture`: raw intake, not organized yet
- `standard`: reliable reusable note with source, boundary, example, and risks
- `deep`: research-grade card with mechanism, comparisons, counterexamples, claim-level evidence, and verification questions

Use `source: []` only when no source is known. In that case, set `status: unverified` and
`confidence: unknown`.

When sources exist, prefer this shape:

```yaml
source:
  - title: ""
    type: official-doc
    url: ""
    accessed: "YYYY-MM-DD"
```

Useful source types:
- `official-doc`
- `paper`
- `book`
- `article`
- `course`
- `video`
- `experiment`
- `personal-note`
- `unknown`

## 6. Required Knowledge Card Structure

Every concept or pattern note should include these sections:

```markdown
## 一句话结论

## 概念定位

## 核心概念

## 机制与原理

## 适用场景

## 不适用场景

## 前提、边界与反例

## 对比与替代方案

## 示例或最小实验

## 失败模式与风险

## 常见误区

## 实践判断

## 来源与证据

## 待验证问题

## 变更记录
```

Practice and project notes may use the experiment template, but they still need source, confidence,
observations, conclusions, and unresolved questions.

## 7. Rigor and Depth Standard

Knowledge additions must be rigorous and deep enough to support future learning, implementation,
and review. Depth does not mean long text. It means clear mechanisms, boundaries, evidence, and
decision value.

Default depth:
- For raw capture, use `depth: capture`, place it in the closest numbered section, and keep the original uncertainty.
- For normal concept or pattern additions, use `depth: standard`.
- For important agents topics, implementation patterns, safety, evaluation, memory, RAG, tool calling, planning, or model behavior, use `depth: deep`.
- If the user says "严谨", "深入", "系统", "完整", "研究", "可复用", or asks to supplement an existing knowledge point, default to `depth: deep`.

A deep note must include:
- Clear definition and neighboring concepts it is not.
- Key terms and prerequisites.
- Mechanism or workflow: what happens step by step, and why it works.
- Inputs, outputs, assumptions, and dependencies.
- Applicable and non-applicable cases.
- At least one concrete example, minimal experiment, or implementation sketch.
- Failure modes, risks, and common misconceptions.
- Comparison with at least one alternative or adjacent pattern when relevant.
- Evidence quality assessment, not just a source list.
- Open questions that would change the conclusion if answered differently.

Do not mark a note as `verified` unless:
- The core claims are backed by primary sources, official docs, papers, or reproducible experiments.
- Date-sensitive claims have an access date.
- Conflicting evidence has been checked or explicitly recorded.
- The note explains its own boundaries and failure modes.

## 8. Evidence Card Rules

Treat every knowledge point as an evidence card.

Required behavior:
- Separate fact, inference, personal experience, and open question.
- Do not present guesses as confirmed knowledge.
- Cite sources for source-backed claims in `来源与证据`.
- Mark source-free claims as `unverified`.
- Record date-sensitive claims with an access date.
- For experiments, record environment, steps, expected result, actual result, and reproduction notes.
- For important claims, add a claim-level evidence note: claim, evidence, source, confidence, and limitation.
- If source quality is weak, keep `confidence: low` or `unknown` even if the explanation sounds plausible.

Reliability guidance:
- Official documentation and primary papers are preferred for definitions and API behavior.
- Blog posts, videos, and social posts can inspire notes, but should not become `verified` alone.
- Personal experiments can raise confidence only when steps and environment are reproducible.
- If sources conflict, preserve both views and add a conflict note instead of silently merging them.
- For AI agents, prioritize official docs, research papers, benchmark/eval reports, source code, and reproducible local experiments over summaries.
- When current product behavior matters, verify against the latest official documentation or source before updating confidence.

Source depth tiers:
- Tier 1: official docs, primary papers, standards, source code, reproducible experiments.
- Tier 2: engineering blogs from credible teams, conference talks, detailed technical articles.
- Tier 3: tutorials, newsletters, videos, social posts, unsourced summaries.
- Tier 4: personal intuition, model-generated text, memory-only claims.

Use Tier 3 and Tier 4 sources only as leads unless the note is explicitly marked `unverified`.

## 9. Assistant Workflow

When asked to add, update, or organize knowledge:

1. Inspect `knowledge/`, `INDEX.md`, and `tags.md` with `rg` or file search before creating a new note.
2. Choose the module and lesson topic, then default to `knowledge/MM-模块名/NN-小节标题.md`.
3. Use `templates/simple-learning-note.md` by default, or `templates/knowledge-card.md` when the user asks for rigorous deep expansion.
4. Fill all required frontmatter fields.
5. Add clear `来源与证据` and `待验证问题` sections.
6. Expand depth until the note explains mechanism, boundary, example, failure modes, and evidence quality.
7. For `depth: deep`, use `templates/claim-audit.md` for important claims when evidence is non-obvious.
8. If updating an existing note, preserve the original meaning and add a short entry to `变更记录`.
9. If duplicate or conflicting notes are found, report them and recommend a merge or split.
10. Keep edits scoped to the requested topic.

When the user provides raw material without a source:
- Put it in the closest numbered section and mark the destination note as `unverified`.
- Use cautious language such as "可能", "待验证", or "基于当前材料".
- Add concrete questions needed to verify it later.

When the user asks for learning help:
- Prefer turning the answer into one or more reusable cards.
- Add examples and misconceptions only when they clarify the concept.
- Do not invent a full course structure unless requested.

When supplementing an existing note:
- First identify what is missing: definition, mechanism, boundary, example, evidence, comparison, or risk.
- Add new material under the most specific section instead of appending a vague "补充" section.
- Preserve previous conclusions unless evidence clearly changes them.
- If the supplement changes the conclusion, record why in `变更记录` and lower confidence if evidence is incomplete.

Deep supplement protocol:
1. Scope the topic: define the exact question, excluded questions, and target directory.
2. Scan existing notes: identify duplicates, related concepts, unresolved questions, and stale claims.
3. Decompose claims: split the topic into definitions, mechanisms, practical claims, risks, and open questions.
4. Assess evidence: classify sources by tier and record limitations for important claims.
5. Rebuild the mechanism: explain the causal chain, data flow, control flow, or decision logic.
6. Test boundaries: add non-applicable cases, counterexamples, failure modes, and safer alternatives.
7. Integrate carefully: update the most specific sections and keep uncertainty visible.
8. Review with `templates/knowledge-review.md` when the note is important, long-lived, or likely to guide implementation.

## 10. Quality Checklist

Before finishing a knowledge-base edit, verify:

- The note is in the correct directory.
- Frontmatter includes `title`, `type`, `status`, `confidence`, `depth`, `source`, `created`, `updated`, and `tags`.
- Unsupported claims are marked as `unverified` or moved to `待验证问题`.
- Source-backed claims include source title, source type, URL when available, and access date.
- The note has a concise one-sentence conclusion.
- The note explains when the idea does and does not apply.
- The note explains mechanism, workflow, or causal logic when the topic is non-trivial.
- The note includes boundaries, counterexamples, risks, and common misconceptions.
- Important claims have evidence quality notes and confidence rationale.
- `depth: deep` notes include mechanism, comparison, counterexample, failure mode, and claim-level evidence.
- Important or high-impact notes have been checked with `templates/knowledge-review.md`.
- Duplicates or conflicts were checked.
- Any change to an existing note has a `变更记录` entry.

## 11. What Not To Do

- Do not dump long copied source text into notes.
- Do not overwrite an existing note just to make it cleaner.
- Do not remove uncertainty labels unless the claim has been checked.
- Do not create broad folder structures before the content needs them.
- Do not add dependencies, scripts, or automation for simple Markdown maintenance.
- Do not claim a tool, model, framework, or API behavior is current without checking when recency matters.
- Do not confuse fluent explanation with verified knowledge.
- Do not mark a knowledge point as deep if it lacks mechanism, boundary, example, and evidence.
- Do not spread one everyday learning topic across many folders unless the user asks.
- Do not place learning notes directly under `knowledge/`; use a numbered module folder and a numbered lesson file.

## 12. UI Standards: OpenAI-Inspired

Use an OpenAI-inspired design direction for UI work: calm, clear, precise, human, and deeply usable.
This is an inspiration rule, not permission to copy OpenAI branding.

Reference source:
- `90-references/openai-design-guidelines.md`

Core principles:
- One primary focus per screen.
- Quiet hierarchy before decoration.
- Generous whitespace, stable layout, and readable density.
- Neutral base colors with restrained semantic accents.
- Typography should feel precise and approachable. Prefer a high-quality sans stack; use OpenAI Sans only if it is legitimately available for the project.
- Motion should communicate state, continuity, or progress. It must respect `prefers-reduced-motion`.
- AI interactions must expose processing, streaming or progressive output, retry, cancel, error, timeout, and empty states.

OpenAI brand boundaries:
- Do not use OpenAI logos, wordmarks, Blossom marks, or similar marks unless the UI directly relates to OpenAI services and follows OpenAI's published terms.
- Do not imply endorsement, sponsorship, or partnership with OpenAI.
- Do not put OpenAI model names in app, product, project, or company titles.
- If referencing OpenAI APIs or models, be precise and accurate.

Visual direction:
- Use off-white, ink, graphite, soft gray, and subtle border colors as the default foundation.
- Use accent colors sparingly for state, focus, and key actions rather than decoration.
- Prefer crisp surfaces, thin borders, strong text contrast, and measured shadows.
- Avoid purple-blue gradient templates, orb backgrounds, glassmorphism for its own sake, and busy hero art.
- Keep cards to real repeated items, modals, or framed tools. Do not nest cards inside cards.

Interaction direction:
- Primary actions should be obvious without explanatory helper text.
- Every generated or AI-assisted output area needs a visible lifecycle: idle, loading, streaming, success, empty, error, cancelled, and retrying when applicable.
- Long-running tasks need a stop or cancel control.
- High-risk AI actions need confirmation, audit language, and a reversible path where possible.
- Keyboard focus must be visible and useful.

UI documentation:
- Put reusable UI rules, screen specs, and design reviews in the most relevant numbered section under `knowledge/`.
- Use `templates/ui-spec.md` for new UI specs.
- A UI spec must describe audience, screen purpose, state model, accessibility, responsive behavior, and verification steps.
- If a UI decision is inspired by OpenAI's public design guidance, cite `90-references/openai-design-guidelines.md`.

## 13. UI Quality Checklist

Before finishing meaningful UI work, verify:

- The screen has one clear primary task.
- Loading, empty, error, success, disabled, cancelled, and retry states are represented where applicable.
- Text does not overflow or overlap on mobile or desktop.
- Color is semantic and contrast is readable.
- Motion is purposeful and reduced-motion safe.
- AI output is traceable enough for user trust.
- Brand usage does not imply OpenAI affiliation.
- The UI has been checked against `templates/ui-spec.md` when a spec exists.
