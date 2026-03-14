---
id: "urn:srl:concept:readyscore"
type: output
title: "ReadyScore"
status: review
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
version: 1.0
dc:subject:
  - biometric-composite
  - readiness-assessment
  - product-design
dc:source:
  - "chatgpt-export:mapping-gap-moments-with-category-theory"
skos:broader:
  - neurogating
skos:narrower: []
skos:related:
  - vagal-tone
  - cognitive-variability-analysis
  - state-transition
  - gap-moment-detection-engine
prov:wasDerivedFrom:
  - "urn:srl:observation:category-theory-state-transitions"
  - "urn:srl:observation:hrv-deprecation-measurement-integrity"
aliases:
  - readiness score
  - ready indicator
trademarked: false
---

# ReadyScore

A composite readiness metric that maps multi-dimensional biometric data (HRV, respiratory rate, pupil diameter, movement patterns) into a single actionable indicator — the functor F: Phys → Readiness in the [[category-theory-state-transitions]] framework.

## Definition

ReadyScore is the user-facing output of [[neurogating]]: a simplified color-coded indicator (green/yellow/red) that tells the clinician whether they are in an optimal autonomic state for the next task. It replaces the raw HRV waveform (deprecated per [[hrv-deprecation-measurement-integrity]]) with an actionable, low-cognitive-load readiness signal.

## Architecture

- **Inputs (hidden layer):** HRV (RMSSD), respiratory rate, heart rate, movement data, context signals
- **Processing:** ML model classifies autonomic state, applies personalized thresholds (natural transformation η: F ⇒ G)
- **Output:** Single ReadyScore value with color coding
- **Decision rule:** If ΔReadyScore >= +12% threshold after a [[neurominute]] → "ready"; else run alternate protocol

## Design Principle

The user sees only the minimum information needed to act. The AI sees the full multi-modal data. This signal hierarchy prevents attentional capture while maintaining clinical-grade assessment in the background.

## Related Concepts

- [[neurogating]] (broader — ReadyScore is the output layer)
- [[vagal-tone]] — primary input to ReadyScore calculation
- [[cognitive-variability-analysis]] — analytical framework behind the score
- [[state-transition]] — ReadyScore tracks transition completeness
