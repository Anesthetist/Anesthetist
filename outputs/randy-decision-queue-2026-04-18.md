---
title: Randy Decision Queue, Apr 18 2026
type: output
status: active
created: 2026-04-18
creator: Vigil
subject:
  - extraction-pipeline
  - clinical-interpretation
  - needs-review
purpose: One-sitting decision queue to unblock the extraction pipeline and five stuck clinical concepts
---

# Randy Decision Queue, 2026-04-18

The extraction pipeline has been idle since 2026-03-15 because five concepts carry `clinical_interpretation: Pending review`. Those fields are yours alone. Once you answer the six questions below, the pipeline restarts, the bots pick up their learning logs, and 858 ChatGPT sources release into batch 2.

Estimated time: 30 minutes. Answer inline or verbally; I will apply via `update_note`.

---

## 1. Gap Moment Detection Engine, entry thresholds

File: [[gap-moment-detection-engine]]
Current spec: **HRV drop >10ms, respiration spike >4bpm**, Apple Watch skin conductance.

**Question.** Are these absolute thresholds, or should they be personalized against a rolling baseline (e.g., >10ms below the user's 7-day median RMSSD)?

**Secondary.** Does respiration spike cleanly separate from artifact (motion, speech) in practice, or does it need a confidence gate before the engine fires?

Your answer:
> 

---

## 2. Neurotagging, top 5 required tags per NeuroMinute session

File: [[neurotagging]]
Current body: strategic framing, no schema definition yet.

**Question.** Of the candidate tag classes below, which five are non-negotiable for every session write?

- neurotarget (e.g., vagal-tone, CO₂-tolerance, insula-engagement)
- context (pre-case, between-cases, post-code, commute, pre-sleep)
- protocol-version (breath ratio + I:E + modality stack)
- pre-state snapshot (HR, short-window HRV, subjective stress 0 to 10)
- post-state snapshot (same triad)
- user-role (CRNA, RN, surgeon, EMS, executive, other)
- environment (motion, noise, time-of-day)
- adherence-fidelity (did the user complete the full protocol)
- subjective-readiness delta
- location class (hospital, home, vehicle, other)

Your top 5, in order:
> 

---

## 3. Diaphragmatic Literacy, definition lock

File: [[diaphragmatic-literacy]]
Current 4-skill definition: **perceive**, **distinguish** (chest vs. diaphragmatic), **control** (depth/rate/ratio), **maintain** (under stress without monitoring).

**Question.** Does this match how you teach it? Specifically:

- Is there a fifth skill (e.g., **recover** diaphragmatic pattern after it breaks)?
- Should "maintain under stress without conscious monitoring" be the canonical ceiling, or is there a higher tier (e.g., **teach** it to another clinician)?

Your answer:
> 

---

## 4. Somnistics Readiness Battery (SRB-60), sign-off

File: [[somnistics-readiness-battery]]
Current spec: **5 domains** (Gap Moment Literacy, Micro-Interoceptive Skill, Protocol Selection/Fidelity, Measured State Delta, Return-to-Task Readiness) × **4 tiers** (Bronze, Silver, Gold, Platinum).

**Question.** Are the 5 domains final, or is one missing? Candidates not yet in the battery: CO₂ tolerance via BOLT, co-regulation with a second person, recovery from an induced stressor.

**Secondary.** Pass criteria per tier. Should Bronze require all 5 domains at a minimum threshold, or 4 of 5? What disqualifies from Platinum (e.g., fidelity <90%, state delta <1 SD)?

Your answer:
> 

---

## 5. Gap Moment Literacy, canonical state list

File: [[gap-moment-literacy]]
Current list: **hyperarousal, hypoarousal, cognitive tunnel, dyspnea loop, task-ready**.

**Question.** Is this the canonical five? Specifically missing from polyvagal would be:

- **shutdown / dorsal vagal collapse** (distinct from hypoarousal)
- **freeze** (co-activation)
- **fawn / appeasement** (social engagement override)

Do any of these belong in the SRB-60 classification set, or do they fold into the existing five?

Your answer:
> 

---

## 6. Thayer & Lane citation, RESOLVED

No action needed. PubMed verification (2026-04-18):

- [[thayer-lane-2000-neurovisceral-integration]] correctly attributed to *J Affect Disord* 61(3): 201 to 216, PMID 11163422.
- [[thayer-lane-2009-neurovisceral-integration]] correctly attributed to *Neurosci Biobehav Rev* 33(2), DOI 10.1016/j.neubiorev.2008.08.004.

The year/journal confusion in `needs-review.md` was against the 2000 paper. Both notes are accurate. Closing this item.

---

## Research Queue (not a decision, tasks for Vigil)

These three need literature scans before vault treatment. Not blocking extraction.

- **Kegan Developmental Stages (3 to 5).** Stage theory of adult meaning-making. Question: where it intersects with autonomic state capacity.
- **Spiral Dynamics.** Value systems and stages. Question: where it maps onto CRNA identity arcs and Somnistics audience segmentation.
- **Springett Consciousness Stairway.** 9-stage model. Fold into the Somnistics protocol concept (to be created) once vault treatment is ready.

On your word, I spin these as three Explore-agent literature scans and return evidence notes plus draft concept stubs for your review.

---

## What unblocks when you finish

- `needs-review.md` backlog collapses from 5 pending to 0 pending clinical decisions.
- Extraction coordinator resumes batch 2 (858 remaining ChatGPT sources).
- Five concepts promote from draft to review.
- Five bot learning-logs get their first new entry in 34 days.
- The `clinical_interpretation` field gets cleared across the five files.
