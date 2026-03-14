---
id: "urn:srl:observation:pas-me-autoresearch-engine"
type: observation
title: "PAS-ME: Predictive Autonomic State Modeling Engine (5-State Classification)"
status: draft
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
dc:subject:
  - machine-learning
  - autonomic-classification
  - edge-computing
  - Apple-Watch
  - autoresearch
observation_type: craft-knowledge
clinical_context: "AI research — autonomous ML pipeline for real-time autonomic state classification on Apple Watch"
years_of_evidence: 1
prov:wasDerivedFrom: []
skos:related:
  - neurogating
  - readyscore
  - cognitive-variability-analysis
  - state-transition
---

# PAS-ME: Predictive Autonomic State Modeling Engine (5-State Classification)

## Observation

The somnistics-autoresearch program defines PAS-ME — a closed-loop neuroadaptive biofeedback system running on Apple Watch/iPhone that classifies autonomic state into 5 categories in real-time.

### 5-State Classification Model

1. **calm** — baseline parasympathetic dominance
2. **focused_flow** — optimal performance state
3. **cognitive_strain** — "Pre-Oops" moment before errors occur (NOVEL: early detection trigger)
4. **acute_stress** — sympathetic surge
5. **recovery** — post-stress parasympathetic rebound

### Input Features (15 Biometric Channels)

- HRV: RMSSD, SDNN, pNN50, LF/HF ratio, Poincaré SD1/SD2
- Heart rate, respiratory rate estimate
- Accelerometer: jerk magnitude, micro-tremor power (8-12Hz), posture variance
- Skin temperature

### Deployment Constraints

- <100ms inference latency (real-time)
- <500K parameters (fits Apple Neural Engine)
- >90% weighted F1 score target
- Architecture search: MLP → CNN → LSTM → TCN → hybrid with quantization-aware training

### Autonomous Research Loop

Human writes directives → AI agent modifies train.py → trains 5 min → evaluates → keeps/reverts → repeats (~12x/hour, ~100 experiments overnight). Adapted from Karpathy's autoresearch pattern.

### "Pre-Oops" State (cognitive_strain)

The most novel classification: detecting the state BEFORE errors occur — not acute stress (obvious) but the subtle cognitive strain that precedes mistakes. This maps directly to QRC error archetype #4 (fatigue + small slips that stack) and enables truly preventive intervention.

## Significance

PAS-ME is the technical implementation of [[neurogating]] and [[readyscore]] — the AI engine that converts raw biometrics into actionable state classification. The "Pre-Oops" detection is the key differentiator: intervening before errors, not after stress.

## Related Concepts

- [[neurogating]] — PAS-ME is the core detection algorithm
- [[readyscore]] — 5-state output feeds the readiness indicator
- [[cognitive-variability-analysis]] — the analytical framework PAS-ME implements
- [[state-transition]] — PAS-ME tracks transitions between all 5 states
