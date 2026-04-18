---
created: '2026-04-01'
creator: vigil
dc:source:
- urn:srl:evidence:ismail-organizational-singularity-2026
dc:subject:
- organizational-design
- agentic-workflows
- intelligence-stack
- ai-transformation
id: urn:srl:concept:intelligence-stack
modified: '2026-04-01'
prov:wasDerivedFrom:
- urn:srl:evidence:ismail-organizational-singularity-2026
skos:broader:
- exo-3-mtp-drive-shape
skos:narrower:
- agent-specification
skos:related:
- intelligence-density
- agent-specification
- human-ai-decision-boundary
- recursive-workflow-improvement
- somnistics-agentic-lab
- vigil-coordination-architecture
status: draft
title: Intelligence Stack
type: concept
---

# Intelligence Stack

The operating system of the AI-native organization. Six cognitive layers with one cross-cutting control plane, replacing the traditional human-centric departmental model (Ismail et al., 2026).

## Definition

The Intelligence Stack replaces functional organization (sales, ops, finance) with cognitive organization. The company is organized around six cognitive layers and one cross-cutting control plane. Each layer has a distinct function, produces a distinct output, and is governed by GOVERN/ASSURE.

80%+ of AI deployments fail to deliver intended business value because they build point-solution agents within human-to-human workflows. The Intelligence Stack constrains this chaos.

## The Six Layers

### 1. PURPOSE / POLICY / RISK APPETITE
Defines what the system is optimizing for, what it must never optimize away, and which decisions are non-delegable. The MTP three-layer model (Human, Constraint, Decision) lives here.
**Core Metric:** Alignment Fidelity

### 2. SENSE — Environmental Intelligence
Collect signals from environment, internal operations, customers, markets, regulation, models, and workflows. Compress signal-to-noise.
**Core Metric:** Signal-to-Noise Compression Ratio

### 3. INTERPRET — Contextual Intelligence
Turn raw signals into usable context: retrieval, memory, provenance, anomaly triage, state estimation, scenario framing. The layer most organizations skip.
**Core Metric:** Context Accuracy Rate

### 4. DECIDE — Strategic Architecture
Generate options, simulate consequences, rank tradeoffs, allocate resources, recommend or commit to action. Operates within PURPOSE delegation boundaries.
**Core Metric:** Decision Half-Life

### 5. ORCHESTRATE / ACT — Execution
Execute through tools, workflows, APIs, humans, robots, and other agents inside bounded permissions. The Human/AI Decision Boundary operates here.
**Core Metric:** Execution Latency

### 6. LEARN — Evolution Engine
Evaluate outcomes, compare expected vs. actual, detect drift, update prompts/playbooks/models, decide what gets promoted, rolled back, or escalated. The recursive workflow improvement engine.
**Core Metric:** Improvement Velocity

### GOVERN / ASSURE (Control Plane)
Not a layer — a cross-cutting control plane spanning all layers. Identity, permissions, approval thresholds, audit trails, kill switches, drift detection. Monitors the entire flow in real time. When SENSE violates privacy policy, Govern intercepts. When DECIDE exceeds permission envelope, Govern escalates. When LEARN degrades performance, Govern rolls back.

## The Flow

PURPOSE sets constraints → SENSE collects signals → INTERPRET builds context → DECIDE commits to action → ORCHESTRATE executes → LEARN evaluates and improves → GOVERN assures every step.

The stack is a loop, not a pipeline. Every cycle makes the next cycle faster, sharper, and more autonomous within PURPOSE boundaries.

## SRL Implementation

SRL's bot architecture maps to the Intelligence Stack:
- **PURPOSE** = CLAUDE.md + Five Red Arrows + Communication Philosophy
- **SENSE** = competitive-landscape bot, transcript-triage bot
- **INTERPRET** = knowledge-miner bot (context extraction)
- **DECIDE** = Vigil (orchestrator routing)
- **ORCHESTRATE** = vault-writer, citation-resolver bots
- **LEARN** = bot retrospectives, pattern libraries, learning logs
- **GOVERN** = schema enforcement, quality gates (draft → review → canonical), clinical_interpretation reserved for Randy

## clinical_interpretation

Pending review
