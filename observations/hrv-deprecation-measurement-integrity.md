---
id: "urn:srl:observation:hrv-deprecation-measurement-integrity"
type: observation
title: "HRV Deprecation: Measurement Integrity Over Theoretical Elegance"
status: draft
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
dc:subject:
  - measurement
  - Apple-Watch
  - HRV
  - product-design
  - clinical-humility
observation_type: contrast-case
clinical_context: "Product evolution — deprecating real-time HRV feedback in Pausality despite theoretical validity"
years_of_evidence: 2
prov:wasDerivedFrom:
  - "urn:srl:evidence:lehrer-2000-resonance-frequency"
skos:related:
  - vagal-tone
  - neurogating
  - minimum-effective-dose
  - cognitive-variability-analysis
---

# HRV Deprecation: Measurement Integrity Over Theoretical Elegance

## Observation

The first version of Pausality was built around real-time HRV biofeedback. The theory was sound — HRV is a legitimate autonomic marker with strong research support. But in practice, Apple Watch PPG-based HRV readings weren't consistent enough for real-time feedback. Too much variability between readings, too much noise. The feature was deprecated.

This decision reflects a core somnistics principle: **measurement integrity over theoretical elegance.**

### Why Real-Time HRV Feedback Failed

1. **Sensor noise:** Apple Watch PPG introduces artifacts from motion, tattoos, dark skin tones, cold exposure, wrist position
2. **Attentional capture:** Users fixated on HRV waveforms instead of their task, creating the opposite of regulation
3. **Cognitive load:** For CRNAs in high-acuity moments, watching HRV trends introduces load rather than reducing it
4. **False feedback loops:** Inconsistent readings broke user trust and caused practice abandonment

### The Replacement Signal Hierarchy

1. What the user needs to **feel** (heartbeat rhythm, breath pace) — somatic
2. What the provider needs to **see** (color-coded readiness: green/yellow/red) — simplified
3. What the AI needs to **know** (full HRV, complexity, entropy) — hidden layer

HRV moved from user-facing feedback to background inference. The AI model consumes it; the user never sees raw data. Simple heart rate became the visible metric: "Whose heart rate is higher?" (clinician vs. patient) outperforms watching HRV trends.

## Significance

This is a contrast case between theoretical correctness and clinical utility. The pharmacological analog: a drug that works perfectly in vitro but has too many side effects in vivo. Randy's clinical training — "does this actually work at the bedside?" — drove a product decision that a pure-tech team might not have made.

The observation also establishes the signal hierarchy for [[neurogating]]: AI sees everything, the user sees only what helps.

## Related Concepts

- [[vagal-tone]] — HRV remains the gold standard measure, just moved to the hidden layer
- [[neurogating]] — the AI layer that consumes HRV for decision-making
- [[minimum-effective-dose]] — simplest effective feedback (HR) over most theoretically elegant (HRV)
- [[cognitive-variability-analysis]] — full HRV analysis continues in the AI layer
