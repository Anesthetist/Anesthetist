---
audience:
- internal
created: '2026-04-12'
creator: randy-graybeal
id: urn:srl:concept:token-efficiency-protocol
modified: '2026-04-12'
skos:related:
- signal-to-noise-protocol
- no-one-off-work-rule
status: canonical
subject:
- operational-infrastructure
- ai-system-design
- resource-management
tags:
- vigil
- dispatch
- efficiency
- model-tiering
title: Token Efficiency Protocol
type: concept
---

# Token Efficiency Protocol

Usage limits are a hard constraint. Running out mid-task wastes all tokens spent reaching that point. Pacing beats throughput.

## Core Principles

### 1. Early-Exit on No-Signal
Every automated task checks for a delta BEFORE running a full cycle. No new vault writes + no HubSpot changes + no calendar events = exit in 30 seconds. Do not scan when nothing has changed.

### 2. Model Tiering
- **Sonnet (default):** All scheduled tasks, data parsing, research scans, routine operations, formatting
- **Opus (earned):** Clinical accuracy (care plans, protocols), investor-facing deliverables, complex knowledge graph wiring, anything where being wrong costs more than the tokens saved
- The test: if the task is primarily fetching, parsing, or formatting, it's Sonnet. If getting it wrong creates real-world damage, it's Opus.

### 3. Word Caps
Every task prompt includes a hard output limit: 200 words for status checks, 400 words for scans, 500 words for full orchestration. Uncapped output is never acceptable in automated tasks.

### 4. Serialization
One heavy task at a time. Queue the rest. Parallel launches burn quota simultaneously and risk both failing mid-task. Front-load high-value builds after usage reset; schedule lightweight tasks for end of window.

### 5. Notification Suppression
Scheduled tasks do not notify Dispatch on completion. Dispatch checks results on-demand or during the Saturday Flight Check. Duplicate notifications are deduplicated by session_id — read once, skip repeats.

### 6. No Subagent Spawning in Scheduled Tasks
Subagents inside scheduled tasks compete for API quota and cause rate-limit cascades. Sequential API calls only. Save progress incrementally so rate-limit kills don't lose work.

### 7. Git Commit Quick-Fail
The vault git sync cannot reach the host filesystem from the sandbox. Try once, fail fast, exit. Do not retry, do not write verbose error reports. Total runtime target: under 30 seconds.

## Application
This protocol governs all Vigil agents (Librarian, Researcher, Builder, Operator, Finance), all scheduled scans (HN intel, LinkedIn engine, vault-lint, X bookmarks), and Dispatch orchestration behavior. It is a standing operational constraint, not a temporary measure.
