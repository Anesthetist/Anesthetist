---
id: "urn:srl:observation:sensor-fusion-optimal-stack"
type: observation
title: "Optimal Sensor Fusion Stack for Autonomic State Classification"
status: draft
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
dc:subject:
  - sensor-fusion
  - multi-modal
  - biometrics
  - product-architecture
observation_type: craft-knowledge
clinical_context: "Product design — combining multiple biometric streams for robust autonomic state classification"
years_of_evidence: 2
prov:wasDerivedFrom: []
skos:related:
  - neurogating
  - cognitive-variability-analysis
  - polyanchora
  - vagal-tone
---

# Optimal Sensor Fusion Stack for Autonomic State Classification

## Observation

No single biometric sensor reliably classifies autonomic state in real-world environments. The optimal stack combines four channels, each providing a different "window" into the autonomic system:

### Four-Channel Fusion Architecture

1. **Pupillometry (LC-arousal window)** — Pupil dilation reflects locus coeruleus-norepinephrine (LC-NE) system activation. Highly sensitive to cognitive load changes. iPhone TrueDepth/LiDAR enables real-time tracking.

2. **HRV (vagal tone window)** — RMSSD and HF-HRV reflect parasympathetic capacity. Apple Watch PPG provides continuous monitoring (moved to background AI layer per [[hrv-deprecation-measurement-integrity]]).

3. **Respiratory Rate (CO₂ buffering window)** — Breath rate, depth, and regularity reflect both autonomic state and intervention effectiveness. Countable by the user (low cognitive load metric).

4. **Facial Microexpression (emotional intent window)** — Enhanced functional connectivity in frontal, occipital, temporal regions during micro-expressions. Correlates with EEG coherence patterns.

### Disambiguation Principle

Multi-modal fusion disambiguates physiological states — separating true autonomic shift from environmental noise or conscious control. A pupil dilation + HRV drop + respiratory acceleration = confirmed sympathetic activation. A pupil dilation alone might be lighting change.

### Apple Ecosystem Integration

HealthKit + on-device ML enables real-time fusion across Watch (HRV, HR, movement) + iPhone (pupillometry, facial analysis, respiratory rate from microphone) + AirPods (ambient sound, head movement).

## Significance

This fusion architecture is the technical backbone of [[neurogating]] — multiple redundant signals prevent false triggers and enable confident state classification even with noisy consumer sensors.

## Related Concepts

- [[neurogating]] — the AI layer that consumes fused sensor data
- [[cognitive-variability-analysis]] — the analytical framework for interpreting fused signals
- [[polyanchora]] — multi-modal sensing mirrors multi-anchor attention training
- [[vagal-tone]] — HRV as one channel in the fusion stack
