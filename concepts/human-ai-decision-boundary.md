---
created: '2026-04-01'
creator: vigil
dc:source:
- urn:srl:evidence:ismail-organizational-singularity-2026
dc:subject:
- organizational-design
- agentic-workflows
- decision-architecture
- AI-transformation
id: urn:srl:concept:human-ai-decision-boundary
modified: '2026-04-01'
prov:wasDerivedFrom:
- urn:srl:evidence:ismail-organizational-singularity-2026
skos:broader:
- organizational-singularity
skos:narrower: []
skos:related:
- fiduciary-wedge
- intelligence-stack
- agent-specification
- neurogating
status: draft
title: Human/AI Decision Boundary
type: concept
---

# Human/AI Decision Boundary

The dynamic line that determines what routes to agents and what routes to humans. The operating logic of the Organizational Singularity (Ismail et al., 2026).

## Definition

Every decision decomposes into prediction (AI) and judgment (human), following Agrawal, Gans & Goldfarb's framework. Routing logic determines which side each decision falls on — not as a one-time classification but as a continuous calibration that shifts as AI capabilities evolve.

**High-sigma decisions** → route to humans: ambiguous, high-stakes, value-laden, irreversible
**Low-sigma decisions** → route to agents: routine, well-defined, prescriptive, reversible

## Routing Frameworks

- **Snowden's Cynefin:** Simple and complicated domains route to agents; complex and chaotic domains route to human judgment
- **Mollick's jagged frontier:** The boundary is irregular — AI excels at some tasks and fails at adjacent ones. Must be mapped empirically, not theoretically assumed

## Boundary Velocity

A decision that requires human judgment today may be safely delegable in six months. Organizations must track how fast the boundary is moving and recalibrate quarterly.

## Scoring (1-5)
- **1:** Decisions made by whoever happens to be there. No mapping. No routing logic.
- **3:** Key decision domains mapped. Some routing logic. Boundary reviewed annually.
- **5:** Every decision domain mapped. Routing logic explicit and documented. Boundary reviewed quarterly. Escalation protocols clear. Boundary velocity tracked.

## SRL Relevance — Clinical Decision Routing

The Human/AI Decision Boundary maps powerfully to clinical practice:
- **SRL's vault architecture** implements this: clinical_interpretation fields are reserved for Randy (human judgment), while bots handle extraction, citation, and formatting (AI prediction)
- **Pausality app design:** The app provides autonomic data (SENSE + INTERPRET) but the clinician decides how to act on it (DECIDE). The boundary is explicit in the product.
- **Neurogating parallel:** SRL's [[neurogating]] concept describes a physiological version of the Human/AI Decision Boundary — the body's own routing logic for which signals get conscious attention vs. automatic processing
- **Enterprise pitch frame:** "We've already mapped the decision boundary for clinical performance. Here's what the AI handles, here's what your clinicians handle, here's how we track boundary velocity."

## clinical_interpretation

Pending review
