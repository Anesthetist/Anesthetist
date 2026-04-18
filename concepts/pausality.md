---
aliases:
- Pausality(TM)
- Pausality™
clinical_interpretation: Pending review
created: '2026-04-18'
creator: Randy Graybeal
dc:source:
- https://apps.apple.com/us/app/pausality/id6743325009
- https://pausality.health
- urn:srl:observation:pausality-product-profile
- urn:srl:observation:pausality-ontology-map
- urn:srl:observation:pausality-b2b-motion
dc:subject:
- somnistics
- product
- consumer-app
- biometric-feedback
- closed-loop-autonomic-training
- clinician-durability
- autonomic-regulation
- apple-watch
- gap-moment-training
- state-transitions
id: urn:srl:concept:pausality
modified: '2026-04-18'
prov:wasDerivedFrom:
- urn:srl:evidence:lehrer-2000-resonance-frequency
- urn:srl:evidence:porges-2011-polyvagal-theory
- urn:srl:evidence:zaccaro-2018-breathing-systematic-review
- urn:srl:evidence:thayer-lane-2000-neurovisceral-integration
- urn:srl:evidence:prinsloo-2011-hrv-biofeedback-immediate
- urn:srl:evidence:awtry-2025-surgeon-autonomic-complications
- urn:srl:evidence:bordini-2025-cognitive-errors-difficult-airway
- urn:srl:evidence:milleville-2025-crna-decision-making
- urn:srl:evidence:voity-2025-or-distractions-cognitive-load
- urn:srl:evidence:brosschot-2006-perseverative-cognition
- urn:srl:evidence:sezer-2025-meditation-autonomic-nervous-system
- urn:srl:evidence:lopez-blanco-tyler-2025-vagus-performance-review
- urn:srl:evidence:kim-2026-humming-breathing-resonance
- urn:srl:evidence:nakamura-2025-respiration-rr-interval-attention
- urn:srl:evidence:wittmann-2011-moments-in-time
- urn:srl:observation:pausality-product-profile
- urn:srl:observation:pausality-ontology-map
- urn:srl:observation:pausality-b2b-motion
skos:broader:
- somnistics
skos:narrower:
- pausality-b2b-motion
- pausality-prime-referral-program
skos:related:
- gap-moment-training
- neurominute
- neurogating
- anterocept
- polyanchora
- minimum-effective-dose
- titration-to-effect
- state-transition
- clinician-durability
- resonant-breathing-frequency
status: review
title: Pausality
trademarked: true
type: concept
version: '1.0'
---

# Pausality™

A closed-loop autonomic training product that lives in the transitions. Pausality detects transition moments through biometric signals, delivers a 60-second [[neurominute]] intervention, and confirms the autonomic reset through the same biometric channels before the user moves on. The product exists where meditation apps do not: inside clinical workflow, between events, in the minute nobody thinks is trainable.

## Randy's Canonical Frame

> "You are not selling an app. You are introducing a new professional behavior."

Pausality is a professional behavior, delivered as a product. The behavior is the completion of an autonomic reset at a detected transition point. The product is the system that detects the transition, structures the reset, and confirms it completed.

## What Pausality Is

- A consumer app on iOS, iPadOS, and Apple Watch (see [[pausality-product-profile]]).
- A 60-second protocol format ([[neurominute]]) triggered at detected transition points ([[gap-moment-training]]).
- A closed-loop system: biometric detection, structured intervention, biometric confirmation.
- A shareable proof card generator at the peak emotional moment of biometric response.
- A clinical-first wedge into consumer health, counter-positioned against meditation and mindfulness.

## What Pausality Is Not

- Not a meditation app. Meditation apps ask for time the clinical workflow does not contain.
- Not a mindfulness app. Mindfulness frames regulation as self-awareness; Pausality frames it as autonomic state training.
- Not a relaxation app. Relaxation is one possible state. Pausality trains flexibility across states.
- Not an enterprise dashboard. Enterprise utility emerges from bottom-up clinical adoption, not top-down procurement (see [[pausality-b2b-motion]]).

## The Six-Stage Ontology

Per [[pausality-ontology-map]]: User, Context, Protocol, Session, Response, Learning.

| Stage | What | Why it matters |
|---|---|---|
| User | Profession, baseline HRV, CO₂ tolerance, stress profile | Tailors the protocol library to the operator |
| Context | Temporal window, load state, environment | Selects which transition is active |
| Protocol | Breath parameters, I:E ratio, nasal/oral, humming/sighing | Matches autonomic target to context |
| Session | 60-second delivery with pre-state snapshot and time series | The training rep |
| Response | ΔHR, ΔRMSSD, respiratory rate change, subjective readiness | The signal that confirms the reset |
| Learning | Per-user and per-role adaptation | Compounds into personal and population data |

If the ontology holds, everything else is instrumentation.

## Mechanism Stack

Pausality composes existing somnistics primitives:

- **Detection.** [[neurogating]] watches HRV drops, heart rate spikes, respiratory rate changes, and movement patterns for transition signatures.
- **Intervention.** The [[neurominute]] delivers 60 seconds of breath, interoceptive cues, and sensory scaffolding against a defined neurotarget.
- **Attentional scaffolding.** [[polyanchora]] layers multiple anchors so attention has somewhere to rest.
- **Sensor efficiency.** [[anterocept]] minimizes sensor count and cognitive load per session.
- **Sensitivity.** [[titration-to-effect]] adjusts dose to response; not every transition earns intervention.
- **Unit of dose.** [[minimum-effective-dose]] anchors the 60-second format as the floor of efficacy.

## Why Sixty Seconds

The 60-second format is the minimum at which a resonant-frequency breath practice produces a measurable HRV shift within a single session ([[lehrer-2000-resonance-frequency]], [[zaccaro-2018-breathing-systematic-review]], [[prinsloo-2011-hrv-biofeedback-immediate]]). It is also the approximate time for initial amygdala deactivation and prefrontal reactivation after sympathetic load. It fits inside the clinical workflow constraint: CRNAs cannot take ten-minute breaks, but they can access sixty-second windows between cases. It operates at the intersection of Wittmann's three temporal levels ([[wittmann-2011-moments-in-time]]), holding enough experienced moments for learning while fitting within the mental presence span.

## The Biometric Proof Moment

The session result card is the product's distribution mechanism. The card shows the pre-session baseline, the change across the 60 seconds, and a timestamp. It is shareable by single tap at the peak emotional moment of the session (see [[pausality-prime-referral-program]]). This is where private experience becomes public proof. No competitor in the meditation or wellness category has this because no competitor produces clinical-grade biometric proof in 60 seconds.

## Why This Works in Clinical Reality

- [[awtry-2025-surgeon-autonomic-complications]] showed that clinician autonomic state at transition into a procedure predicted major surgical complications across 793 cases. The transition is where the outcome is set.
- [[bordini-2025-cognitive-errors-difficult-airway]] found cognitive errors in 17.4% of 2,801 difficult airway cases, with fixation (a transition failure) as the dominant type.
- [[milleville-2025-crna-decision-making]] identified workflow transitions as the points where CRNA decisions are most vulnerable.
- [[voity-2025-or-distractions-cognitive-load]] counted 81 distractions per cesarean case. Each is a forced micro-transition the nervous system must either complete or carry as residue.
- [[brosschot-2006-perseverative-cognition]] named the carry-over mechanism: perseverative cognition extends sympathetic activation and HPA engagement past the event that triggered it.

Put together, the literature frames the transition as the performance surface. Pausality is the system that trains that surface.

## Evidence Base

- [[lehrer-2000-resonance-frequency]]. Single-session HRV shifts at resonance frequency.
- [[porges-2011-polyvagal-theory]]. Vagal mechanism for slow rhythmic breathing.
- [[zaccaro-2018-breathing-systematic-review]]. Autonomic and CNS effects of controlled breathing.
- [[thayer-lane-2000-neurovisceral-integration]]. HRV as structural index of self-regulation capacity.
- [[prinsloo-2011-hrv-biofeedback-immediate]]. Acute performance effects from single-session biofeedback.
- [[sezer-2025-meditation-autonomic-nervous-system]]. Brief repeated practice produces durable ANS changes.
- [[lopez-blanco-tyler-2025-vagus-performance-review]]. Vagal modulation as performance substrate.
- [[kim-2026-humming-breathing-resonance]]. Specific breath mechanisms for vagal activation.
- [[nakamura-2025-respiration-rr-interval-attention]]. Respiration-heart coupling gates attention.

## Related Concepts

- [[somnistics]] (broader).
- [[gap-moment-training]] (related). The method Pausality productizes.
- [[neurominute]] (related). The 60-second protocol format.
- [[neurogating]] (related). The detection layer.
- [[anterocept]] (related). The sensor philosophy.
- [[polyanchora]] (related). The attentional scaffolding.
- [[minimum-effective-dose]] (related). The dosing principle.
- [[titration-to-effect]] (related). The calibration principle.
- [[state-transition]] (related). The training surface.
- [[clinician-durability]] (related). The outcome.
- [[resonant-breathing-frequency]] (related). The breath target.
- [[pausality-b2b-motion]] (narrower). The clinical adoption motion.
- [[pausality-prime-referral-program]] (narrower). The consumer distribution engine.

## Related Observations

- [[pausality-product-profile]]. Current app state, pricing, platform coverage.
- [[pausality-ontology-map]]. The six-stage data model.
- [[pausality-moat-analysis-march-2026]]. 7 Powers structural defensibility.
- [[pausality-scientific-evidence-integration]]. Evidence-to-messaging integration map.
