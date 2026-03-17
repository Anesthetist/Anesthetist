---
created: '2026-03-16'
creator: Claude Scheduled Task
dc:subject:
- scheduled-task
- knowledge-management
- cowork
- vault-ingestion
- workflow-architecture
id: urn:srl:observation:cowork-vault-ingestion-architecture-finding
modified: '2026-03-16'
observation_type: process-finding
skos:related: []
status: draft
title: 'Cowork-to-Vault Ingestion Architecture: Scheduled Task Limitation and Best
  Practice'
type: observation
---

## Observation

On March 16, 2026, a scheduled task (`review-previous-chats-to-enter-into-the-mcp`) was executed with the intent to review recent Cowork conversations from the sidebar and ingest key insights into the SRL knowledge vault.

## Architecture Finding

Each Cowork conversation runs in its own isolated Linux sandbox session (e.g., `funny-pensive-galileo`, `admiring-sharp-heisenberg`, etc.). Only the **current session's** filesystem is accessible during any given task execution. Previous sessions are separate sandbox environments — their conversation JSONL files (stored under `.claude/projects/`) are not accessible cross-session.

**Result:** The scheduled task cannot programmatically read prior Cowork chat histories, because they live in isolated containers that don't share a filesystem with the task's execution environment.

## What IS Accessible

- The current session's `.claude/projects/` JSONL file (the task's own conversation)
- The mounted workspace folder (`mnt/`) — shared across sessions via the user's computer
- The SRL vault via MCP — accessible from any session
- Uploaded files in `mnt/uploads/`

## Current Vault State (March 16, 2026)

The vault is actively maintained and up to date:
- **45 concepts** — ranging from `draft` to `canonical` status
- **130+ observations** — most in `draft`, some in `review`, 3 in `current`
- **50+ evidence entries** — covering key literature
- **2 outputs** — comprehensive landscape reviews

Most recent entries (all March 16, 2026):
- `keaton-srna-ai-builder-first-meeting` — SRNA building AI anesthesia app
- `mayo-clinic-arnp-trauma-case-first-field-use` — First field use at Mayo Clinic, 2AM trauma
- `somatic-certification-curriculum-architecture` — Five-domain curriculum design
- `family-first-use-teenager-interoceptive-awakening` — Teenager's first biofeedback session

## Recommended Architecture: Real-Time Ingestion (Already Working)

The vault is being populated **during** conversations, not after. This is the correct and effective pattern:
- Vault entries are created in the moment when insights occur
- Scheduled batch review cannot substitute for real-time entry

## Recommended Improvement: Conversation Snapshot File

If batch-review is desired, conversations should export a summary to the shared workspace at session end, e.g., writing a `session-summary-YYYY-MM-DD.md` to `mnt/outputs/daily-summaries/`. This file would be accessible to subsequent sessions and scheduled tasks.

## Action Items

1. Consider adding a habit: at the end of any productive Cowork session, ask Claude to write a brief session summary to `mnt/outputs/` with key insights and vault entries created.
2. The scheduled task is best repurposed as a **vault maintenance check** (reviewing draft entries, promoting to review/canonical, identifying gaps) rather than a batch ingestion task.
3. Alternatively, modify the task to read any session-summary files from `mnt/outputs/daily-summaries/` if they exist.
