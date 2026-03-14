---
id: "urn:srl:concept:neurogating"
type: concept
title: "Neurogating"
status: canonical
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
version: 1.1
dc:subject:
  - somnistics
  - novel-concept
  - AI-driven
  - anomaly-detection
  - sensor-fusion
  - cognitive-load
  - adaptive-intervention
dc:source:
  - "chatgpt-export:cognitive-emotional-state-interface"
  - "chatgpt-export:novel-concepts-catalog"
  - "chatgpt-export:review-of-professional-profile"
skos:broader:
  - somnistics
skos:narrower:
  - readyscore
skos:related:
  - state-transition
  - gap-moment-training
  - cognitive-variability-analysis
  - neurominute
  - anterocept
prov:wasDerivedFrom:
  - "urn:srl:evidence:porges-2011-polyvagal-theory"
  - "urn:srl:observation:neurogating-clinical-triggers"
aliases:
  - "Neurogating(TM)"
  - "Neurogating™"
  - "NeurogatingTM"
  - "NeuroGating™"
trademarked: true
---

# Neurogating™

An AI-driven algorithmic model and adaptive system that integrates stochastic anomaly detection for psychophysiological training. Neurogating gates (triggers/modulates) micro-interventions based on real-time biometric patterns — it is the intelligence layer that determines *when* and *what* to deliver.

## Definition

Neurogating™ is the closed-loop detection-and-response engine within the Pausality stack. It watches multimodal biometric streams, classifies cognitive workload states in real-time, detects anomalous patterns indicating overload or disengagement, and automatically cues the appropriate [[neurominute]] intervention. The core innovation is integrated stochastic anomaly detection for closed-loop psychophysiological training.

## Core Functions

1. **Multimodal Sensor Fusion** — Integrates HRV, pupillometry, EEG, GSR (galvanic skin response), speech pattern analysis, and keystroke dynamics
2. **Real-Time Cognitive Load Detection** — Machine learning (RNNs, transformers, anomaly detection) classifies cognitive workload states with >90% accuracy
3. **Anomaly Detection** — Flags unusual biometric patterns indicating cognitive overload, stress, or disengagement (95% detection from eye movement data alone)
4. **Adaptive Triggering** — Automatically cues [[neurominute]] interventions when specific physiological thresholds are detected (e.g., HR spike >10bpm, HRV drop >10ms)

## Trigger Architecture

- **HR spike >10bpm** from baseline → cue calming protocol
- **HRV drop >10ms** sustained → cue vagal activation protocol
- **Respiration spike >4bpm** → cue breath regulation protocol
- **EEG theta/gamma coupling shift** → cue cognitive reset protocol
- **Context detection** (walking→standing, calendar transition) → cue gap moment protocol

## IP Strategy

Core patent-worthy innovation: integrated stochastic anomaly detection for closed-loop psychophysiological training. Filed as provisional patent focusing on real-time sensor fusion and predictive cognitive state modeling.

## Gap Moment Detection Engine

The inference layer within Neurogating that specifically identifies transition moments. It combines:
- **Biometric signals:** HRV drop, HR spike, respiratory rate change
- **Context signals:** Calendar transitions, location changes (walking→standing), time-of-day patterns
- **Behavioral signals:** Phone unlock patterns, movement cessation, posture change
- **Historical patterns:** Individual user's gap moment timing learned over days/weeks

When a gap moment is detected, the engine selects and delivers the appropriate [[neurominute]] protocol based on the user's current state, time of day, and intervention history. Neuroception ([[porges-2011-polyvagal-theory]]) is the biological precedent — Neurogating is its technological analog.

## ReadyScore (Output Layer)

ReadyScore is the user-facing output of Neurogating: a simplified color-coded indicator (green/yellow/red) that tells the clinician whether they are in an optimal autonomic state for the next task. Architecture:
- **Inputs (hidden layer):** HRV (RMSSD), respiratory rate, heart rate, movement data, context signals
- **Processing:** ML model classifies autonomic state, applies personalized thresholds
- **Output:** Single ReadyScore value with color coding
- **Decision rule:** If ΔReadyScore >= +12% threshold after a [[neurominute]] → "ready"; else run alternate protocol

Design principle: the user sees only the minimum information needed to act. The AI sees the full multi-modal data.

## Evidence Base

- [[porges-2011-polyvagal-theory]] — neuroception as the biological precedent for automated threat/safety detection; Neurogating is the technological analog
- Machine learning literature: RNN/GRU hybrid networks achieving >90% accuracy in cognitive load classification
- Eye movement data achieving 95% specificity in anomaly detection for high-workload events

## Clinical Observations

- In anesthesia, experienced CRNAs develop unconscious "gating" — noticing autonomic shifts in patients before monitors alarm. Neurogating systematizes this pattern for self-regulation.
- The system models the clinical decision-making pattern: detect state → classify urgency → select intervention → confirm response

## Related Concepts

- [[somnistics]] (broader)
- [[state-transition]] — Neurogating detects the transition point and triggers intervention
- [[gap-moment-training]] — Neurogating identifies gap moments automatically via biometric patterns
- [[cognitive-variability-analysis]] — CVA provides the real-time cognitive state data that feeds Neurogating's adaptive logic
- [[neurominute]] — the intervention format that Neurogating selects and delivers
- [[anterocept]] — the sensory training modality that Neurogating may recommend based on detected state
