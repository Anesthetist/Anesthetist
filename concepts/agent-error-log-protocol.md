---
created: '2026-04-13'
creator: claude
id: concept-agent-error-log-protocol
modified: '2026-04-13'
related:
- concept-token-efficiency-protocol
- concept-signal-to-noise-protocol
- concept-no-one-off-work-rule
skos:related:
- token-efficiency-protocol
- signal-to-noise-protocol
- no-one-off-work-rule
- saturday-flight-check-ritual
status: draft
subjects:
- operational-intelligence
- agent-coordination
- quality-assurance
title: Agent Error Log Protocol
type: concept
---

# Agent Error Log Protocol

## Problem

Agents repeat the same classes of mistakes across sessions. Feedback memories capture corrections from Randy, but there is no structured system for logging *agent-originated* errors and auto-injecting preventive context into future prompts. This means:

- The same drift patterns recur (formatting slop, scope creep, wrong model tier, file-not-saved)
- Randy becomes the bottleneck for catching and correcting recurring errors
- No quantitative signal on which agents or task types are most error-prone

## Protocol

### 1. Error Classification

Each logged error gets a **type** tag:

- **drift** — agent wandered from instructions (scope creep, wrong tone, unauthorized subagent spawn)
- **scoring** — incorrect calculation, wrong reverse-scoring, bad data transformation
- **routing** — file saved to wrong location, output not accessible, wrong model tier used
- **hallucination** — fabricated citation, invented data, false capability claim
- **efficiency** — token waste, unnecessary screenshots, redundant tool calls, polling loops
- **integration** — MCP tool failure, API timeout, auth error not handled gracefully

### 2. Log Format

Each error is a short structured entry appended to a running log (vault observation note or dedicated file):

```
- **date**: 2026-04-13
- **task**: ProQOL + MAIA-2 Assessment
- **type**: routing
- **description**: JSX file written to task sandbox instead of /mnt/Claude/ workspace
- **root cause**: Task session lacks mount to dispatch workspace directory
- **fix applied**: Rebuilt file in dispatch session manually
- **preventive rule**: Always verify /mnt/Claude/ is writable before writing; if not, output file contents for parent to capture
```

### 3. Injection Into Future Prompts

Errors that recur 2+ times graduate to **preventive rules** that get injected into the relevant agent's prompt template:

- Scheduled task prompts: append `## Known Failure Modes` section
- Skill definitions: add `## Common Errors` section
- Memory feedback entries: create if the pattern is cross-cutting

### 4. Weekly Review (Saturday Flight Check Integration)

The Flight Check ritual includes a "Hard Thing" section. Agent error patterns from the week feed into this:

- Top 3 error types by frequency
- Which agents/tasks produced them
- Which preventive rules were added
- Whether prior preventive rules reduced recurrence

### 5. Metrics

Track per week:
- Total errors logged
- Errors by type
- Repeat vs. novel errors
- Time-to-fix (how many messages before resolution)

## Design Principle

This is not about punishing agents — it's about building institutional memory at the system level. The vault already captures *what we know*; this protocol captures *where we fail* so the system gets smarter over time.

## Relationship to Existing Protocols

- **Token Efficiency Protocol**: efficiency-type errors feed directly into token optimization
- **Signal-to-Noise Protocol**: error logs follow delta-only reporting — only new patterns or graduated rules surface to Randy
- **No One-Off Work Rule**: if the same error fix is applied manually twice, it must be codified as a preventive rule or skill patch
- **Saturday Flight Check**: weekly error digest integrates into the Hard Thing section
