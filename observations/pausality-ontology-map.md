---
clinical_context: Core data ontology for Pausality app and recommendation engine
created: '2026-03-14'
creator: Randy Graybeal
dc:subject:
- ontology
- data-model
- pausality
- product-architecture
- recommendation-engine
id: urn:srl:observation:pausality-ontology-map
modified: '2026-03-14'
observation_type: strategic-insight
prov:wasDerivedFrom: []
skos:related:
- somnistics
- somnistics-taxonomy-sit
- noosphere-graph-architecture
status: draft
title: 'Pausality Minimal Ontology: User → Context → Protocol → Session → Response
  → Learning'
type: observation
---

# Pausality Minimal Ontology: User → Context → Protocol → Session → Response → Learning

## Observation

A minimal but complete ontology has been defined for reasoning about Pausality's product and science:

### Entity Graph

**User**
- Profession: CRNA, RN, surgeon, EMS, trader, etc.
- Traits: baseline HRV, CO₂ tolerance proxy, stress profile

**Context**
- Temporal: pre-case, between cases, post-code, commute, pre-sleep
- Load: acute stress vs simmering chronic load
- Environment: motion/noise from Watch, time of day, shift type

**Protocol**
- Parameters: breathing rate (~6 breaths/min vs faster), I:E ratio (4:6 vs 4:4)
- Features: exhale bias, brief holds, sighs, humming, nasal/oral
- Intended outcome: downshift (calm), upshift (focus), reset (interrupt rumination)

**Session**
- Duration: ~60 seconds
- Pre-state snapshot: HR, short HRV window, self-rated stress
- Time series: HR, HRV, respiratory cadence proxy

**Response**
- Acute: ΔHR, Δshort-window HRV (RMSSD), respiratory rate change
- Subjective: perceived calm, focus, "readiness"

**Learning / Adaptation**
- Per-user: "which protocol works best for me in this context?"
- Population: which protocols work best for *this role* / shift pattern?

### Design Principle

"If you lock this ontology, everything else is just instrumentation, UX, and study design."

## Significance

This ontology is the backbone for Pausality's recommendation engine and data science strategy. It maps cleanly to both the clinical research design (each entity = a variable) and the product UX (each entity = a screen or data flow).

## Source

- Google Drive: "Pausality definition summary"

## Related Concepts

- [[somnistics]] — the broader framework this ontology serves
- [[somnistics-taxonomy-sit]] — complementary classification system
- [[noosphere-graph-architecture]] — biometric states as first-class nodes in the graph
