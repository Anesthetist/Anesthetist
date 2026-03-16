---
created: '2026-03-15'
creator: Randy Graybeal
dc:source:
- chatgpt-export:684a5409-1ac0-8010-b0da-a6a2916d4698
dc:subject:
- somnistics
- gap-moment-training
- ai-inference
- context-awareness
- biometrics
id: urn:srl:concept:gap-moment-detection-engine
modified: '2026-03-15'
prov:wasDerivedFrom:
- urn:srl:chat:chatgpt-multi-phase-interoceptiv-analysis
skos:broader:
- gap-moment-training
skos:narrower: []
skos:related:
- neurominute
- neurogating
- minimum-effective-dose
status: draft
title: Gap Moment Detection Engine
type: concept
version: '0.1'
---

# Gap Moment Detection Engine

An inference layer that monitors biometrics and contextual signals (calendar, location, behavioral patterns) to detect when a user is entering a gap moment, classify the autonomic state, and surface the appropriate NeuroMinute protocol. The engine transforms the Somnistics app from a passive library into a context-aware co-pilot for nervous system regulation.

## Mechanism

The detection engine operates across three signal domains:

1. **Physiological signals** — HRV drop >10ms, respiration rate spike >4bpm, skin conductance changes detected via Apple Watch sensors
2. **Contextual signals** — Calendar transitions (between-case windows), location changes (walking to OR), time-of-day patterns, posture shifts (standing→sitting)
3. **Behavioral signals** — App usage patterns, historical response data, user-reported state classifications

When convergent signals indicate a gap moment, the engine selects and surfaces a NeuroMinute matched to the detected state (hyperarousal, hypoarousal, cognitive tunnel, dyspnea loop, or task-ready maintenance).

## Architectural Role

Randy classifies this as an "engine/inference layer" within the Somnistics stack — the computational bridge between raw sensor data and personalized protocol delivery. It is the intelligence that makes Gap Moment Training adaptive rather than scheduled.

## Relationship to Neurogating

While [[neurogating]] governs the adaptive triggering rules (when and how to intervene), the Gap Moment Detection Engine is the sensing apparatus — the pattern-recognition system that feeds state classifications to the gating logic.

## Clinical Interpretation

Pending review.

## Related Concepts

- [[gap-moment-training]] (broader — the training modality this engine serves)
- [[neurominute]] — the intervention unit the engine selects and delivers
- [[neurogating]] — the adaptive triggering system that uses engine output
- [[minimum-effective-dose]] — engine optimizes for smallest effective intervention
