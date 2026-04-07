---
created: '2026-03-30'
creator: Claude (Vigil)
dc:creator:
- Garry Tan
dc:source: https://github.com/garrytan/gstack
id: urn:srl:evidence:garrytan-gstack-claude-code-skill-pack-2026
modified: '2026-03-30'
status: draft
subject:
- agent-architecture
- skill-design
- productivity
- claude-code
- open-source
- YC
title: 'Garry Tan gstack: 23-Skill Claude Code Virtual Engineering Team (March 2026)'
type: evidence
---

# Garry Tan gstack — Virtual Engineering Team via Claude Code Skills

## Source
GitHub: https://github.com/garrytan/gstack
MIT License, open source. 10K+ stars in 48 hours of release (March 2026).

## What It Is
Garry Tan (President/CEO of Y Combinator) open-sourced his personal Claude Code skill pack. 23 specialized slash commands that turn Claude Code into a virtual engineering team: CEO, Designer, Eng Manager, Release Manager, Doc Engineer, QA Lead, and Security Officer.

## Productivity Claims
- 600K+ lines of production code in 60 days (35% tests)
- 10-20K lines per day, part-time, while running YC full-time
- 140,751 lines added, 362 commits, ~115K net LOC in one week
- 10-15 parallel sprint sessions simultaneously

## Sprint Process Architecture
Skills run in deliberate order: **Think → Plan → Build → Review → Test → Ship → Reflect**

Each skill feeds into the next:
- /office-hours writes a design doc that /plan-ceo-review reads
- /plan-eng-review writes a test plan that /qa picks up
- /review catches bugs that /ship verifies are fixed

## Key Skills (SRL-Relevant)

### /office-hours — YC Office Hours
Six forcing questions that reframe the product before code: demand reality, status quo, desperate specificity, narrowest wedge, observation, and future-fit. Pushes back on framing, challenges premises, generates implementation alternatives. Design doc feeds all downstream skills.

### /plan-ceo-review — CEO/Founder Review
Rethinks the problem. Finds the "10-star product" hiding inside the request. Four modes: Expansion (dream big), Selective Expansion (cherry-pick expansions), Hold Scope (maximum rigor), Reduction (strip to essentials). User is 100% in control — no scope added without explicit approval.

### /plan-eng-review — Engineering Manager
Locks architecture, data flow, diagrams, edge cases, and tests. Forces hidden assumptions into the open. ASCII diagrams for data flow, state machines, error paths. Test matrix, failure modes, security concerns.

### /retro — Weekly Retrospective
Team-aware weekly retro with per-person breakdowns, shipping streaks, test health trends, growth opportunities. Saves JSON snapshots for trend tracking. /retro global runs across all projects and AI tools.

### /investigate — Systematic Debugger
Iron Law: no fixes without investigation. Traces data flow, tests hypotheses, stops after 3 failed fixes. Auto-freezes to the module being investigated.

### /cso — Chief Security Officer
OWASP Top 10 + STRIDE threat model. Zero-noise: 17 false positive exclusions, 8/10+ confidence gate, independent finding verification.

### /autoplan — Review Pipeline
One command, fully reviewed plan. Runs CEO → design → eng review automatically with encoded decision principles. Surfaces only taste decisions for approval.

### /learn — Memory System
Manages what gstack learned across sessions. Review, search, prune, export project-specific patterns. Learnings compound across sessions.

## Design Principles

1. **Process over tools** — Skills follow sprint order; every step knows what came before
2. **Parallel sprints** — 10-15 simultaneous sessions, each in isolated workspace
3. **Smart routing** — CEO doesn't review infra fixes, design review skips backend changes
4. **Proactive suggestions** — Detects work stage and suggests appropriate skill
5. **Safety guardrails** — /careful, /freeze, /guard for destructive command protection
6. **Real browser mode** — Playwright-controlled Chrome for QA, visible to user

## Relevance to SRL Vigil Architecture

Gstack validates the "virtual team of specialists" model that Vigil implements. Key structural parallels:
- gstack's 6 roles ↔ Vigil's 6 agents (Librarian, Researcher, Builder, Operator, Finance, Vigil)
- gstack's sprint process ↔ Vigil's ACLS code team coordination model
- gstack's /office-hours ↔ SRL's need for a structured product/strategy review skill
- gstack's /retro ↔ Vigil's heartbeat reports
- gstack's /learn ↔ SRL vault's knowledge persistence

Key differences:
- gstack is engineering-focused; Vigil is research/business-focused
- gstack assumes code output; Vigil produces knowledge artifacts, evidence, and business deliverables
- gstack runs on Claude Code; Vigil runs on Cowork/Dispatch with MCP integrations

**Adaptation opportunities:**
1. /office-hours → SRL /office-hours for product strategy sessions (Randy + Vigil)
2. /retro → Enhanced Vigil heartbeat with trend tracking and JSON snapshots
3. /plan-ceo-review four-mode scope framework → Vigil strategic planning
4. /investigate iron law → Researcher systematic evidence evaluation
5. /learn memory compound → Vault knowledge promotion pipeline
