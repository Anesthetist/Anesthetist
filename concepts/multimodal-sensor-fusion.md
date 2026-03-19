---
created: '2026-03-19'
creator: Randy Graybeal
dc:source:
- chatgpt-export:provisional-patent-draft
dc:subject:
- biofeedback
- sensors
- system-architecture
- patent
id: urn:srl:concept:multimodal-sensor-fusion
modified: '2026-03-19'
prov:wasDerivedFrom:
- urn:srl:chat:chatgpt-provisional-patent-draft
skos:broader:
- closed-loop-biofeedback
skos:narrower: []
skos:related:
- neuroadaptive-training-system
- haptic-biofeedback
status: draft
title: Multimodal Sensor Fusion
type: concept
version: '0.1'
---

Combining cardiac, respiratory, neural, and electrodermal signal streams into a unified physiological state representation. Rather than relying on a single biomarker, multimodal fusion produces a richer, more accurate picture of autonomic state.

## Signal Streams

- **Cardiac:** Heart rate, HRV (RMSSD, SDNN, LF/HF ratio), heart rate recovery
- **Respiratory:** Rate, depth, inhale/exhale ratio, regularity
- **Electrodermal:** Skin conductance level, skin conductance response (stress marker)
- **Neural:** Optional EEG/fNIRS for research contexts; not required for consumer product

## Minimum Effective Sensor

Randy's architectural decision: heart rate via Apple Watch is the minimum effective sensor for V1. Multimodal fusion is the target architecture, but the product ships with the simplest viable signal first and layers additional streams as hardware and user sophistication permit.

## Clinical Interpretation

Pending review.
