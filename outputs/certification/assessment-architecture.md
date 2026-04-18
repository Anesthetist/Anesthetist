---
title: Somnistics Certification — Assessment Architecture
creator: Randy Graybeal
created: 2026-04-18
type: certification-spec
status: draft
source_brief: outputs/design-briefs/somnistics-certification-mockup-brief.md
---

# Somnistics Certification — Assessment Architecture

## Measurement philosophy

Certification through measurable change. Three rules.

1. Every competency has a numeric floor. No attendance-only pass.
2. Every floor has a canonical source. No threshold invented at will.
3. Every candidate walks away with their own longitudinal dataset. The portfolio is the proof.

## The assessment stack (six competencies × four specs)

Each competency below lists: instrument, protocol, floor, retest.

### 1. Interoceptive literacy

**Instrument:** MAIA-2 (Mehling et al. 2018) plus a field heartbeat-detection task.

**Protocol:**
- MAIA-2 self-report, 37 items, 8 subscales, administered at baseline, week 4, week 8.
- Heartbeat detection: silent count across three 25-second windows with ECG reference. Accuracy = 1 minus mean absolute percent error.

**Floor:**
- MAIA-2 Body Listening subscale ≥ 3.0 on the 0 to 5 scale.
- MAIA-2 Trusting subscale ≥ 3.0.
- Heartbeat detection accuracy > 0.60 (above chance, per Garfinkel 2015 benchmarks).

**Retest:** One retake of each instrument permitted at week 6. Missed floor on second attempt triggers a remediation module with targeted body-scan practice, then a final retest.

**Canonical anchor:** Mehling 2018 (MAIA-2 validation); Garfinkel 2015 (three-dimension framework); Schandry 1981 (heartbeat detection paradigm).

### 2. Attention regulation

**Instrument:** Breath Counting Task (Levinson et al. 2014) plus a field sustained-attention protocol.

**Protocol:**
- Breath Counting Task: count breaths to 9, repeat for 20 minutes, tap counter on each breath. Accuracy score = proportion of correct count cycles.
- Field protocol: 60-second body-focused attention through one controlled distractor event. Observer scores re-engagement latency.

**Floor:**
- Breath Counting Task accuracy ≥ 0.80.
- Re-engagement within 5 seconds of the distractor event.

**Retest:** Weekly practice required between attempts. Two retakes permitted.

**Canonical anchor:** Levinson 2014 (breath counting validation); Lutz 2008 (attention regulation in meditation); Creswell 2017 (brief attention training effects).

### 3. Voluntary breath control

**Instrument:** BOLT score (McKeown) plus a monitored resonant breathing trial.

**Protocol:**
- BOLT: three quiet breaths, controlled pause after normal exhale, stop at first physiological demand to breathe. Three trials, take the median.
- Resonant breathing identification: test 4.5, 5.0, 5.5, 6.0, 6.5, 7.0 breaths per minute with HRV amplitude capture. Identify individual peak frequency per Lehrer protocol.
- Sustained performance: 5 minutes of diaphragmatic breathing at identified resonant frequency under HRV observation.

**Floor:**
- BOLT ≥ 25 seconds.
- Resonant frequency identified within ±0.5 bpm reliability across two trials.
- Sustained 5-minute protocol with breath rate variance under 10 percent and visible HRV amplitude increase.

**Retest:** Unlimited. CO₂ tolerance is trainable; the floor is a fitness threshold, not a fixed trait.

**Canonical anchor:** Lehrer 2013 (resonant breathing mechanism); Zaccaro 2018 (slow breathing systematic review); McKeown (BOLT methodology); Russo 2017 (slow breathing physiology).

### 4. Autonomic state literacy

**Instrument:** Paired self-report and HRV classification across a clinical shift.

**Protocol:**
- Candidate labels autonomic state at 10 discrete moments during one clinical shift, using a three-state rubric: ventral vagal, sympathetic, dorsal vagal.
- HRV segment captured at each moment (30-second windows).
- Concordance scored against expert review of the HRV data paired with context notes.

**Floor:**
- 70 percent concordance (7 of 10 states labeled correctly).
- Candidate can articulate the physiological signature used to classify each state.

**Retest:** One retake across a separate shift. Missed floor on second attempt triggers a state-recognition module and a third shift attempt.

**Canonical anchor:** Porges 2011 (polyvagal theory and neuroception); Thayer and Lane 2000 (neurovisceral integration); Thayer 2012 (HRV and prefrontal function); Grossman 2023 (polyvagal critiques and clinical utility).

### 5. Closed-loop feedback

**Instrument:** Eight-week candidate-owned trajectory project.

**Protocol:**
- Candidate selects one metric from RMSSD, BOLT, or MAIA-2.
- Weekly measurement, logged with timestamp and condition notes.
- Week 8 submission: data series, one-page interpretation, identification of at least one confound or measurement artifact.

**Floor:**
- Eight weekly data points submitted.
- Interpretation document demonstrates correct identification of trend direction, measurement noise, and at least one contextual driver (sleep, shift load, training intensity).
- Change direction is not the pass criterion. Mastery of the feedback loop is.

**Retest:** Rolling. Trajectory project extends into week 9 if data quality fails at week 8 review.

**Canonical anchor:** Schwartz and Andrasik (biofeedback textbook); Yucha and Montgomery 2008 (evidence-based biofeedback practice); Tan 2016 (HRV biofeedback efficacy review); Lehrer 2020 (stress management and closed-loop training).

### 6. Safety and contraindication literacy

**Instrument:** Five-scenario written and practical exam.

**Protocol:**
- Five scenarios drawn from a standardized pool. Each presents a patient or self-training situation with one or more contraindicated actions.
- Candidate identifies the risk, describes the physiological mechanism, and specifies the correct abort or modification.

**Sample scenario pool:**
- Asthmatic patient requesting Buteyko-style reduced breathing during acute wheeze.
- First-trimester pregnancy candidate requesting kapalabhati or breath retention.
- Cardiovascular disease patient attempting maximal breath hold.
- Recognition and response to hyperventilation-induced tetany.
- Vasovagal syncope risk in seated breath-hold training.
- Recent concussion and Valsalva maneuver risk.
- Anxiety disorder with panic history and CO₂ provocation.

**Floor:**
- Correct identification and abort or modification on 4 of 5 scenarios.
- All correct on the two scenarios flagged as high-acuity (tetany, vasovagal).

**Retest:** One retake with a fresh scenario set. Missed floor on second attempt triggers a safety module and a third attempt after a minimum 2-week interval.

**Canonical anchor:** Meuret 2008 (CART protocol and respiratory safety); breathing pattern disorder literature (Nijmegen Questionnaire); Buteyko method safety reviews; standard CRNA contraindication literature.

## Sequencing across the 8-week program

| Week | Baseline | Attention | Breath | State | Feedback | Safety |
|------|----------|-----------|--------|-------|----------|--------|
| 0 | MAIA-2 full | BCT baseline | BOLT + RF finding | State rubric intro | Metric selected | Scenario pool review |
| 2 | . | BCT practice | Daily RF practice | State labeling drill | Weekly data point | . |
| 4 | MAIA-2 mid | BCT assessment | BOLT retest | First shift assessment | Midpoint review | Module 1 |
| 6 | . | Field attention test | RF sustained protocol | State labeling practice | Weekly data point | Module 2 |
| 8 | MAIA-2 final | BCT final | BOLT final + RF + sustained | Shift assessment | Trajectory submission | 5-scenario exam |

## What the candidate walks away with

- Baseline and week 8 MAIA-2 scores with subscale deltas.
- BOLT trajectory across 8 weeks.
- Identified resonant breathing frequency with HRV evidence.
- Documented state-classification reliability score.
- Eight-week personal trajectory portfolio on one self-selected metric.
- Safety certification record with scenario-by-scenario rationale.

This portfolio is the credential artifact. The candidate carries it into clinical practice, into annual recertification, and into any downstream Somnistics trainer track.

## Maintenance and recertification

- **Monthly:** one RMSSD measurement and a MAIA-2 mini submission.
- **Quarterly:** BOLT check.
- **Annually:** five-scenario safety recert plus MAIA-2 full battery.

Lapse protocol: missed annual recert triggers a 30-day grace period, then credential suspension until a condensed recert module is completed.

## What this does not cover

- Pricing and platform delivery.
- CE credit allocation against AANA Category A requirements.
- Instructor credentialing (a separate trainer-track spec).
- Data infrastructure for longitudinal data capture.

Those specs come next in the build order.
