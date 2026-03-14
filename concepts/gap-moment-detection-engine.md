---
id: "urn:srl:concept:gap-moment-detection-engine"
type: concept
title: "Gap Moment Detection Engine"
status: review
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
version: 1.0
dc:subject:
  - somnistics
  - AI-driven
  - context-awareness
  - biometric-inference
dc:source:
  - "chatgpt-export:novel-concepts-catalog"
  - "chatgpt-export:novel-concept-registry"
skos:broader:
  - neurogating
skos:narrower: []
skos:related:
  - gap-moment-training
  - cognitive-variability-analysis
  - state-transition
prov:wasDerivedFrom:
  - "urn:srl:evidence:porges-2011-polyvagal-theory"
  - "urn:srl:observation:shift-transitions-30-40"
aliases: []
trademarked: false
---

# Gap Moment Detection Engine

A model that watches biometrics + context (calendar, location, behavior patterns) to infer when a user is entering a gap moment, tags it, and surfaces the right [[neurominute]] — effectively turning the app into a context-aware co-pilot for nervous system regulation.

## Definition

The Gap Moment Detection Engine is the inference layer within [[neurogating]] that specifically identifies transition moments. It combines:
- **Biometric signals:** HRV drop, HR spike, respiratory rate change
- **Context signals:** Calendar transitions, location changes (walking→standing), time-of-day patterns
- **Behavioral signals:** Phone unlock patterns, movement cessation, posture change
- **Historical patterns:** Individual user's gap moment timing learned over days/weeks

When a gap moment is detected, the engine selects and delivers the appropriate [[neurominute]] protocol based on the user's current state, time of day, and intervention history.

## Evidence Base

- [[porges-2011-polyvagal-theory]] — neuroception as biological precedent for automated threat/safety detection
- [[shift-transitions-30-40]] — empirical observation of gap moment frequency and timing

## Related Concepts

- [[neurogating]] (broader — the detection engine is a component of Neurogating)
- [[gap-moment-training]] — the engine automates gap moment identification
- [[cognitive-variability-analysis]] — cognitive state data informs detection logic
- [[state-transition]] — the engine detects the transition point
