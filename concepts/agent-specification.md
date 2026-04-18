---
created: '2026-04-01'
creator: vigil
dc:source:
- urn:srl:evidence:ismail-organizational-singularity-2026
dc:subject:
- agentic-workflows
- intelligence-stack
- organizational-design
- ai-transformation
id: urn:srl:concept:agent-specification
modified: '2026-04-01'
prov:wasDerivedFrom:
- urn:srl:evidence:ismail-organizational-singularity-2026
skos:broader:
- intelligence-stack
skos:narrower: []
skos:related:
- human-ai-decision-boundary
- recursive-workflow-improvement
- vigil-coordination-architecture
- somnistics-agentic-lab
- goose-block-open-source-agent
status: draft
title: Agent Specification (8 Properties)
type: concept
---

# Agent Specification (8 Properties)

The eight properties every agent in the Intelligence Stack requires to operate as an enterprise system rather than a demo. The difference between a cool demo and a robust operating model is whether all eight are defined (Ismail et al., 2026).

## The Eight Properties

| Property | What It Specifies |
|----------|-------------------|
| **Charter** | What this agent is for — its scope, purpose, and boundaries |
| **Human Owner** | Who is accountable. Every agent has a human principal behind the Fiduciary Wedge |
| **Autonomy Tier** | Decision authority: advise, recommend, execute-with-approval, or execute-within-bounds |
| **Permission Envelope** | What tools, data, budgets, and actions the agent may use |
| **Memory Boundary** | What the agent can retain, retrieve, and update — and what it must forget |
| **Escalation Rules** | When the agent must stop, ask, or hand off. The Human/AI Decision Boundary made explicit per agent |
| **Eval Suite** | What good performance means — the fitness functions that determine whether this agent is improving or drifting |
| **Telemetry / Audit Trail** | What is logged for review, compliance, and the Govern/Assure control plane |

## SRL Bot Architecture Mapping

SRL's bot system (soul.md + run-protocol.md + patterns.md + learning-log.md) maps directly to this specification:

| Agent Spec Property | SRL Bot Equivalent |
|--------------------|--------------------|
| Charter | soul.md (identity, purpose, boundaries) |
| Human Owner | Randy (all bots report to Randy via Vigil) |
| Autonomy Tier | run-protocol.md (execution steps, what requires Randy's review) |
| Permission Envelope | MCP tools available, vault write access rules |
| Memory Boundary | patterns.md + learning-log.md (what persists between runs) |
| Escalation Rules | clinical_interpretation = "Pending review", needs-review.md queue |
| Eval Suite | retrospective.md (post-run self-assessment), cross-bot feedback |
| Telemetry / Audit Trail | vault-write-log.md, git commit history |

SRL's architecture was built independently but converges with the Agent Specification. This convergent validation strengthens the case for both SRL's approach and the ExO 3.0 framework.

## clinical_interpretation

Pending review
