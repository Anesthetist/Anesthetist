---
created: '2026-03-19'
creator: Randy Graybeal
dc:subject:
- ai-agents
- product-architecture
- commercialization
- agentic-systems
id: urn:srl:concept:agent-quartet-framework
modified: '2026-03-19'
skos:related:
- crna-shift-architect
- tacit-knowledge-extraction
- market-intelligence
- multi-llm-knowledge-construction
source: 'Cowork chat: Productizing domain expertise into agent systems (Feb 2026)'
status: draft
title: Agent Quartet Framework
type: concept
---

# Agent Quartet Framework

A lightweight operating system for building domain-specific AI agent products. Four structured files define everything needed to ship a specialist agent cleanly.

## The Four Files

**soul.md** — Identity and telos. Who the agent is, who it serves, what success looks like. Personality constraints. This is the character of the agent.

**agent.md** — Role, interfaces, and behavior. Scope of work. Input/output contracts. Handoff rules: when to escalate to another agent or a human.

**tools.md** — Instrumentation and integration. Which APIs and tools the agent can call, under what conditions, with what rate limits and data boundaries. What gets logged and what triggers alerts.

**ethics.md** — Constraints and governance. Red-line constraints (data use, consent, regulatory edges). Priority stack when values conflict (safety > speed > novelty). HITL checkpoints — when a human must approve before the agent proceeds.

An orchestrator agent (with its own soul.md) acts as: **planner → task splitter → router → judge**.

## SRL Agent Constellation

| Agent | Job |
|-------|-----|
| Signal Cartographer | Turns domain input into mechanism → behavior → market opportunity cards |
| Offer Architect | Takes a Signal Card, designs 1–3 monetizable offers |
| Experiment Designer | Converts offers into minimal GTM tests with success metrics |
| Clinical/Integrity Guard | Blocks drift into pseudo-medical claims or regulatory hazard |

Pipeline: *domain idea → mapped mechanism → monetizable offer → experiment → review*

## Starting Configuration

Build one narrow, high-value workflow first (e.g., [[crna-shift-architect]]). Deliver initially as high-touch retainer. Strip human time out incrementally until it's a self-serve product. Simultaneously explore one embedded/licensing path with a health-tech SaaS partner.

## Monetization Modes

Usage/seat SaaS · outcome-based pricing · agent-as-a-service retainer · embedded licensing/white label · agentic commerce (% of transactions driven)
