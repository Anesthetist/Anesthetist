---
title: "Neurotagging: The Metadata Layer That Doesn't Exist Yet"
type: essay
status: first-draft
created: 2026-03-21
word_count: 1100
potential_use:
  - investor-pitch
  - patent-narrative
  - conference-paper
  - book-chapter-12
related_concepts:
  - neurotagging
  - neurominute
  - cognitive-variability-analysis
  - interoceptive-technology
  - closed-loop-biofeedback
gertrude_status: pass
---

# Neurotagging

## The Gap in the Infrastructure

There is no universal standard for tagging a therapeutic intervention with its neurophysiological target and its measured outcome.

That sentence should alarm you.

Neuroscience has BIDS — the Brain Imaging Data Structure — for tagging neuroimaging data. Clinical research has CDISC for interchange. Health systems have FHIR for interoperability. Mobile health has IEEE 1752 for wearable data schemas.

None of them answer this question: "What breathing protocol was used, what autonomic state was it targeting, what neurotransmitter system was it designed to modulate, and what happened to the user's HRV during and after?"

That question has no home in any existing data standard. The therapy metadata and the neuroscience data live in separate buildings with no hallway between them.

Neurotagging is the hallway.

## What It Is

**Technical definition:** A structured metadata schema that tags every intervention session with its psychological modality, physiological target, neuroscience correlates, and measured biometric outcome — creating a queryable dataset that bridges therapy and neuroscience.

**Human definition:** Every time you do a NeuroMinute, the system records not just that you practiced, but what you practiced, why the system chose it, what your body was doing before, during, and after, and how this session compares to every prior session you've ever done.

## The Tag Schema

Every NeuroMinute session generates a neurotagging record:

| Tag Category | Example Values |
|-------------|---------------|
| **Protocol ID** | five-breath-re-embodiment-v2, radiant-exhale, stability-snap |
| **Target state** | hyperarousal → task-ready |
| **Breathing parameters** | 4:7:8 ratio, 5.5 bpm, diaphragmatic |
| **Sensory modalities** | audio (binaural), haptic (watch), visual (none — silent mode) |
| **Neurotarget** | vagal tone increase, baroreflex engagement, alpha-theta shift |
| **Pre-session biometrics** | HR: 88, RMSSD: 22, RR: 18 |
| **Post-session biometrics** | HR: 74, RMSSD: 38, RR: 12 |
| **State delta** | HR -14, RMSSD +16, RR -6 |
| **Context** | between-cases, post-difficult-intubation, 14:32 EST |
| **User classification** | self-reported: "needed that one" / dismissed: no |

## Why This Matters

### For the Individual
Longitudinal neurotagging creates a personal autonomic profile. After 21 days, the system knows: this user responds best to extended exhale protocols in the afternoon, shows minimal delta from box breathing before 10 AM, and has a resonant frequency of 5.2 bpm (not the population average of 5.5). The protocols adapt because the data is tagged precisely enough to learn from.

### For Research
Anonymized, aggregated neurotagging data across thousands of users creates a dataset that does not exist anywhere in the world: intervention-outcome pairs tagged with physiological context, at population scale, with longitudinal depth. This is the clinical LLM training data. This is the moat.

### For the Field
If neurotagging becomes an adopted standard — if other breathing apps, wellness platforms, and clinical research tools adopt the schema — SRL becomes the company that defined how the field talks about intervention metadata. The standards body, not just a product company.

## What Exists Today vs. What's Missing

| Standard | What It Tags | What It Doesn't Tag |
|----------|-------------|-------------------|
| BIDS | Brain imaging sessions | Therapeutic interventions |
| FHIR | Clinical health records | Breath protocol specifications |
| IEEE 1752 | Wearable sensor data | Why the data was collected (intervention context) |
| Open mHealth | Mobile health schemas | Neuroscience correlates of interventions |
| **Neurotagging** | All of the above, linked | — |

## The Failure Mode

**Over-tagging:** So many metadata fields that the schema becomes burdensome and clinicians stop using the system. Solution: automatic tagging. The user breathes. The system tags. No manual data entry.

**False precision:** Tags imply causal certainty that doesn't exist. "Neurotarget: vagal tone increase" doesn't mean the protocol caused the increase — it means the protocol was designed to target it. The tag must distinguish *intended target* from *measured outcome*. Gertrude watches this.

**Proprietary lock-in:** If neurotagging only works inside Pausality, it's a feature. If it works across platforms, it's a standard. The strategic decision: open the schema (like FHIR) or keep it proprietary (like Epic). Randy's instinct — open. Standards win.

## The Testable Claim

**Hypothesis:** Tagged intervention data produces more effective protocol personalization than untagged data over a 21-day training period.

**Test:** 40 users, 21 days. Group A: standard progressive curriculum (same protocol sequence for everyone). Group B: neurotagging-adaptive curriculum (protocol selection informed by prior session tags — state delta, time-of-day response, protocol-specific HRV patterns). Measure: RMSSD trend, adherence, user satisfaction, session-over-session state delta improvement.

[RANDY: You asked the question that started this: "What open datasets are available to combine our concept of neurotagging metadata?" — was there a moment in the ChatGPT archive or in a conversation where you realized nobody had built this? 100 words.]

---

*Every NeuroMinute generates data. Neurotagging makes that data intelligent.*

*Not because the tag knows what happened. Because the tag remembers what was intended, what was measured, and what the difference was — so the next session can be better than the last.*
