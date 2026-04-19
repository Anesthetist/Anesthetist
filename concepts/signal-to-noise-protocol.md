---
audience:
- internal
created: '2026-04-12'
creator: randy-graybeal
id: urn:srl:concept:signal-to-noise-protocol
modified: '2026-04-12'
skos:related:
- saturday-flight-check-ritual
status: canonical
subject:
- operational-infrastructure
- communication-design
- attention-management
tags:
- vigil
- dispatch
- efficiency
- attention
title: Signal-to-Noise Protocol
type: concept
---

# Signal-to-Noise Protocol

Randy's attention is the scarcest resource in the system. Every notification that doesn't contain a delta degrades the signal. The system must protect the founder's attention with the same rigor it applies to clinical safety.

## Core Principles

### 1. Delta-Only Notifications
Heartbeats and status checks that find no change file silently to the vault. Randy hears about them only when there is a new signal, an escalation, or an error. "Nothing changed" is not a message — it is the absence of one.

### 2. Deduplication
If a task completion has already been read and reported, subsequent notifications for the same session_id are ignored. No repeated delivery of the same information.

### 3. Bundling
When multiple task completions arrive simultaneously, batch them into a single message. Lead with the highest-leverage finding. Separate blocks by priority, not by source.

### 4. Triage by Leverage
Not all completions deserve equal airtime. Rank by: (a) does Randy need to act on this? (b) is there a time-sensitive window? (c) does this change a decision he's about to make? If none of these, file silently.

### 5. Silent Filing
Tasks that file to vault without surfacing to Randy are not lost — they are indexed, searchable, and available on-demand. The Saturday Flight Check is the weekly reconciliation point where silently filed work gets reviewed.

## Application
This protocol governs Dispatch's communication with Randy across all channels. It applies to vigil heartbeats, scheduled task completions, agent status reports, and any system-initiated notification. The founder's attention is a clinical instrument — do not desensitize it with noise.
