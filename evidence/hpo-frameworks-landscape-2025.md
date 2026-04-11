---
created: '2025-01-25'
creator: Randy Graybeal
dc:creator:
- Randy Graybeal
dc:date: '2025'
dc:description: Survey of HPO frameworks across military, elite sports, NASA, and
  clinical domains. Includes polyvagal theory application to HRV measurement and Apple
  Watch data flow architecture.
dc:identifier: chatgpt-export:hpo-frameworks-overview
dc:subject:
- human-performance-optimization
- autonomic-regulation
- military-wellness
- sports-science
- polyvagal-theory
dc:type: report
id: urn:srl:evidence:hpo-frameworks-landscape-2025
modified: '2026-04-11'
status: draft
title: Human Performance Optimization Frameworks — Landscape Survey (2025)
type: evidence
---

# Human Performance Optimization Frameworks — Landscape Survey

## Frameworks Surveyed

### Military / DoD
1. **Total Force Fitness (TFF)** — 8 domains: physical, nutritional, mental, spiritual, social, medical/dental, environmental, behavioral. Holistic readiness beyond physical conditioning.
2. **Comprehensive Soldier and Family Fitness (CSF2)** — 5 Dimensions of Strength: physical, emotional, social, spiritual, family. Master Resilience Training program.

### Elite Sports
3. **Long-Term Athlete Development (LTAD)** — staged approach from early skill development to elite performance. Progressive overload, periodization, mental training.
4. **Integrated Sports Performance Model** — blends S&C, sports psychology, nutrition, recovery. Real-time biometrics monitoring (HRV, sleep quality).

### Space / Extreme Environments
5. **NASA Behavioral Health and Performance (BHP)** — behavioral medicine, psychosocial adaptation, cognitive performance metrics under isolation and microgravity.
6. **Fatigue Risk Management Systems (FRMS)** — systematic fatigue monitoring and intervention for high-consequence operations.

### Clinical / Therapeutic
7. **Polyvagal-Informed Approaches** — Porges's three hierarchical response circuits (VVC, sympathetic, DVC) applied to clinical regulation and performance.

## Polyvagal Theory and HRV Measurement

### The Ventral vs. Dorsal Problem
Standard HRV measures (HF power, RMSSD, pNN50) reflect overall parasympathetic influence but cannot directly separate ventral vagal (social engagement, calm connection) from dorsal vagal (immobilization, freeze) activation.

- **VVC activation:** Rhythmic RSA oscillations, high HF power — the healthy regulatory signal
- **DVC activation:** Global HR drop, flattened HRV — potentially dangerous "freeze" pattern
- A snapshot of HRV alone cannot tell the ratio of ventral to dorsal

### Experimental Approaches
- Respiratory Sinus Arrhythmia (RSA) as primary VVC index
- Combined HRV + behavioral markers (facial affect, vocalization, social engagement)
- Cardiac vagal tone during controlled breathing vs. spontaneous breathing
- HEP (heartbeat-evoked potentials) as objective interoceptive marker

## Apple Watch HRV Data Flow

1. **Collection:** PPG (green LEDs + photodiodes) on wrist. Periodic sampling at rest, continuous during workouts. ECG available on Series 4+ but manual 30-second snapshots only.
2. **On-device processing:** Raw PPG → heart rate (BPM) + HRV (RMSSD during Breathe/Mindfulness sessions)
3. **Sync:** Bluetooth/WiFi to paired iPhone
4. **HealthKit storage:** Timestamped HKQuantitySample records tagged with source and context
5. **Third-party access:** HealthKit APIs provide discrete samples with user authorization
6. **Reliability:** RMSSD from PPG correlates well with ECG in controlled conditions but PPG introduces ~1-3ms jitter in R-R interval estimation

## SRL Relevance

This landscape survey maps where Pausality sits relative to established HPO paradigms:
- **SRL's niche:** None of these frameworks deliver micro-dose autonomic training via wearable biofeedback in 60-second units. The military frameworks are comprehensive but heavy. The sports models require coaching infrastructure. Pausality is the minimum effective dose approach — self-administered, trackable, scalable.
- **Measurement strategy:** Apple Watch HRV (RMSSD) as the primary objective biomarker, with MAIA-2 as the subjective complement. This dual-channel approach aligns with Campo 2026 showing simultaneous improvement in both.

## Concepts Derived

- [[autonomic-regulation]] — core training target across all HPO frameworks
- [[minimum-effective-dose]] — SRL's differentiation from comprehensive HPO programs
- [[interoceptive-literacy]] — the skill layer that HPO frameworks lack
- [[cardiac-anchored-breathing]] — the delivery mechanism for Pausality's HPO intervention
