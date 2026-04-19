---
created: '2026-04-16'
creator: cross-pollination-agent
dc:subject:
- irb-pilot
- pediatric-anesthesia
- rhema
- hrv-longitudinal-study
- open-wearables
- fhir
- closed-loop-control
- pilot-design
id: urn:srl:concept:pediatric-dental-as-ideal-crna-hrv-pilot-environment
modified: '2026-04-16'
prov:wasDerivedFrom:
- urn:srl:concept:crna-as-closed-loop-controller
- urn:srl:concept:multiplatform-hardware-integration
- urn:srl:concept:sensor-calibration-as-patient-safety
skos:broader:
- crna-as-closed-loop-controller
skos:narrower: []
skos:related:
- sensor-calibration-as-patient-safety
- multiplatform-hardware-integration
- ai-vagal-tone-differentiation-spec
- clinician-durability
- vagal-tone
status: draft
title: Pediatric Dental Sedation as Ideal CRNA HRV Pilot Environment
type: concept
---

# Pediatric Dental Sedation as Ideal CRNA HRV Pilot Environment

## The Bridge

Randy's Rhema work at pediatric dental clinics (Little Pearls, Kid's Choice Dental, Federal Way) is not just clinical revenue that funds SRL runway — it is **the single best-controlled IRB pilot environment available for a longitudinal CRNA HRV cohort study**, because it minimizes the confounds that destroy statistical power in OR-based anesthesia research.

## Why Pediatric Dental Is Uniquely Pilot-Clean

Compared to general OR anesthesia:

1. **Case homogeneity** — narrow age band, predictable procedure mix, same drug protocols, similar case duration. OR work mixes laparoscopic, cardiac, ortho, and OB cases in one day, introducing uncontrollable variance.
2. **Predictable timing** — scheduled start, setup at 4:30, patient starts at 5:00. This enables pre/intra/post-case HRV segmentation without patch-work retrospective reconstruction.
3. **Consistent provider team** — Grace Abrokwah, Randy, Deshaun Dethman. Small N means inter-provider variance is manageable and comparable across cases.
4. **Consistent surgical field stressor** — pediatric dental is behaviorally predictable compared to emergent trauma. The stressor curve is repeatable.
5. **High case volume** — many short cases per clinical day produce more autonomic transitions per hour than long OR cases.
6. **Already-deployed workflow** — Randy is doing the work anyway. The only marginal cost is wearable instrumentation and data capture.

## Why This Matters Now (April 2026)

Randy is meeting the **Open Wearables / Momentum team** (Jan Kaminski, Bartosz Michalak, Piotr Ratkowski) at drinks after the Out-Of-Pocket Hardware Hackathon on **April 19, 2026** in San Francisco.

Open Wearables' Q2 2026 roadmap includes real-time data sync and FHIR mapping (see [[multiplatform-hardware-integration]]). If Randy pitches the pediatric-dental CRNA cohort as their **first FHIR mapping use case**, Open Wearables gets a clean, publishable demonstration of wearable-to-clinical-outcome linkage, and SRL gets:

- A ready-made IRB pilot dataset with unusually low confound load
- Real-time multiplatform HRV capture (not Apple-only)
- FHIR mapping that proves the enterprise health-system procurement story
- A co-authored publication pipeline with Momentum that satisfies CE and regulatory evidence standards

## What To Propose at Sunday's Dinner

A three-provider, 90-day pilot at Rhema contract sites:
- Open Wearables provides the multiplatform HRV capture layer (Garmin/WHOOP/Apple)
- SRL provides the clinical protocol, IRB framework, and CRNA cohort
- Momentum gets the first published FHIR-mapped wearable-to-EHR case study
- SRL gets the longitudinal data foundation for the [[crna-as-closed-loop-controller]] frame

## Decay Risk

This bridge is time-bound. If Randy does not raise it during the April 19 dinner, the conversation will default to the existing roadmap discussion and the pediatric-dental angle will not surface.

## Related Concepts

- [[crna-as-closed-loop-controller]] — the underlying frame
- [[sensor-calibration-as-patient-safety]] — the political reframe
- [[multiplatform-hardware-integration]] — the technical infrastructure
- [[ai-vagal-tone-differentiation-spec]] — the measurement architecture
- [[clinician-durability]] — the outcome category
