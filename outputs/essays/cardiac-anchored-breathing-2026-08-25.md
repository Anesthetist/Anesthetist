---
title: "Notes from the Lab: The First-Mover Protocol"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-25
word_count: 1680
core_claim: "Every consumer breathwork app uses an external clock; cardiac-anchored breathing uses the body's own baroreflex oscillation — and this distinction matters because the heart's sensitivity to breath-pacing input varies continuously across the cardiac and respiratory cycle, meaning an external timer delivers cues at random points on the physiological response curve while a cardiac-anchored system delivers them at the moment of maximum autonomic leverage."
related_concepts:
  - cardiac-anchored-breathing
  - resonant-breathing-frequency
  - anterocept
  - interoceptive-literacy
  - neurominute
evidence_used:
  - lehrer-2000-resonance-frequency
  - dobrushina-2024-haptic-heartbeat-feedback-interoception
  - schillings-2022-heartbeat-perception-training-3-weeks
pubmed_citations_verified: 7
gertrude_status: pass
---

# Notes from the Lab: The First-Mover Protocol

*Every consumer breathwork app uses an external clock; cardiac-anchored breathing uses the body's own baroreflex oscillation — and this distinction matters because the heart's sensitivity to breath-pacing input varies continuously across the cardiac and respiratory cycle, meaning an external timer delivers cues at random points on the physiological response curve while a cardiac-anchored system delivers them at the moment of maximum autonomic leverage.*

---

## The Observation

Every monitor in the operating room is patient-specific. The waveform capnograph reads this patient's CO₂ curve, not a generic population average. The arterial line displays this patient's pressure oscillation. Nobody programs a standard anesthesia monitor to display a template waveform and asks the clinician to titrate toward it. The entire architecture of clinical monitoring is built on the assumption that the measurement must come from the individual body, not from a reference database.

Then the clinician goes home and opens a breathwork app. Inhale for four seconds. Hold for four. Exhale for four.

The app knows nothing about what the heart is doing. It doesn't know whether the baroreflex is primed for a breath-pacing cue at this moment or whether the cardiac cycle has just entered a phase where such a cue will produce minimal effect. It delivers the instruction on schedule, because a clock is what it has.

This is the gap that cardiac-anchored breathing addresses. Not a minor optimization — a categorical architectural shift. The clock is replaced by the body.

---

## The Mechanism

In 1980, Dwight Eckberg, Yonas Kifle, and Victoria Roberts published what remains one of the foundational mechanistic papers in cardiorespiratory physiology. Using precise carotid baroreceptor stimulation timed to different phases of the respiratory cycle, they established that baroreflex responsiveness is not constant — it oscillates continuously throughout the breath [PMID: 7441548]. Sinus node inhibition is maximal at late inspiration and early expiration. It is minimal during mid-inspiration. At 24 breaths per minute, the differential disappears entirely, because the cardiac cycle doesn't have time to distinguish between respiratory phases at that rate.

The implication is mechanistically direct: the heart has a response landscape across the respiratory cycle, and delivering a breath-pacing cue at the peak of that landscape produces a different physiological result than delivering the same cue at the trough. An external clock delivers cues at whatever point in the cardiac cycle happens to be current. A cardiac-anchored system delivers cues at the moment when the baroreflex is most responsive.

Benedikt Kralemann and colleagues (2013) pushed this further. Using coupled-oscillator analysis on continuous recordings from 17 healthy subjects, they extracted the cardiac phase response curve non-invasively for the first time — mapping precisely how each phase of the cardiac cycle responds to respiratory drive [PMID: 23995013]. Their finding: the heart's responsiveness to respiratory input has a definable shape, a peak, and a trough. This curve exists in every person. It can be measured. And it can, in principle, be used to time a breath-pacing cue to arrive at the peak.

Magne Elstad and colleagues (2018) clarified that the coupling is bidirectional [PMID: 29522373]. The literature had long described Respiratory Sinus Arrhythmia — the way breathing drives heart rate variability. What Elstad's review documented with precision is that the heart drives respiration too: during expiration, the next inspiratory onset tends to occur at a preferred latency after the preceding heartbeat, a phenomenon called cardioventilatory coupling. The heart, in other words, is already trying to time the breath. Cardiac-anchored breathing makes this coupling explicit and trainable rather than latent and uncontrolled.

Dirk Cysarz and Arndt Büssing (2005) tested what happens when low-frequency breathing produces genuine cardiac-respiratory phase locking. Using coupled-oscillator synchronization analysis on nine novice meditators practicing Zen and Kinhin meditation, they found high degrees of cardiorespiratory synchronization that were absent during spontaneous breathing [PMID: 15940533]. The key: the effect didn't require meditation expertise. It emerged from the low-frequency breathing rate itself. Any practitioner breathing below roughly 10 breaths per minute in a sustained pattern generates measurable phase locking between cardiac and respiratory oscillators. The capacity for synchronization is already present in the physiology. The question is whether the training architecture deliberately cultivates it or ignores it.

---

## The Protocol

Cardiac-anchored breathing as implemented in the NeuroMinute architecture operates through four components:

**1. Cardiac signal acquisition.**
Beat-to-beat R-R interval data from a wearable with clinical-grade accuracy (Polar H10, Apple Watch optical, Oura Ring). The signal must be real-time, not delayed — latency above 2-3 seconds compromises the phase-anchoring function.

**2. Phase extraction.**
The application identifies the user's current dominant low-frequency oscillation — the baroreflex-sensitive window that Eckberg and Kralemann characterized. As the user begins breathing slowly, this oscillation emerges in the HRV signal as an amplitude peak in the 0.05-0.15 Hz range. The peak location is the user's resonant window. The system anchors pacing cues to this window, not to a fixed timer.

**3. Adaptive cue delivery.**
Breath-pacing cues (haptic via Apple Watch taptic engine, or visual via expanding circle) arrive in synchrony with the cardiac phase that corresponds to peak baroreflex responsiveness — late inspiration to early expiration. As HRV amplitude increases within the session, the cue timing adjusts to the emerging resonant frequency. The system follows the user's physiology rather than leading it toward a target.

**4. Interoceptive transfer.**
Over repeated sessions, the user learns to anticipate the cue before it arrives — because the cardiac signal the cue is derived from is also available interoceptively. Dobrushina, Tamim, and Wald (2024) demonstrated this transfer in a randomized controlled trial: real-time haptic heartbeat feedback (vibration synchronized to each heartbeat) improved interoceptive accuracy in a single session, while visual feedback did not produce the same shift [PMID: 39152653]. The haptic channel is closer to the body's native signaling modality. Over a 21-day curriculum, Schillings and colleagues (2022) showed that sustained heartbeat-focused training produces longitudinal improvements in cardiac interoceptive ability [PMID: 35615275]. The device trains the capacity to eventually function without the device.

---

## The Failure Mode

The primary failure mode is the one this protocol is most vulnerable to: a corrupted cardiac signal. Motion artifact during physical transition (walking to the OR, body repositioning), atrial fibrillation or ectopic beats, and optical sensor placement failure all degrade the R-R interval stream. When the anchor is noise, the system is delivering cues timed to artifact rather than physiology.

This failure has a clear detection criterion — HRV coherence in the app drops, the low-frequency amplitude peak disappears, and the R-R intervals become erratic. The appropriate system response is graceful degradation: fall back to the user's previously identified resonant frequency (stored from calibration), notify the user of signal quality, and continue at a known-good approximation until signal recovery.

The second failure mode is tachycardic anchoring. A CRNA finishing a difficult case with a heart rate of 115 bpm has a compressed cardiac cycle with a different phase response landscape than the same clinician at 65 bpm resting. Anchoring to the high-rate cardiac signal without accounting for autonomic state would push breath pacing toward rates that don't match the underlying physiology. Burlacu and colleagues (2026) documented "autonomic non-responsiveness" in HRV biofeedback — cases where conventional resonance frequency training failed to produce expected gains — and identified elevated sympathetic tone and reduced baroreflex function as primary contributors [PMID: 42356115]. Cardiac-anchored breathing does not solve this problem by itself. A state detection layer (autonomic state classification before protocol selection) must precede the anchor to ensure the system isn't deploying a parasympathetic tool into a sympathetic environment that isn't ready for it.

The third failure mode is the one all breathwork training shares: skill without transfer. The cardiac anchor is a scaffold. If the user requires the device to regulate and has not developed the interoceptive capacity to sense the cardiac signal directly, the skill remains device-dependent. The Dobrushina single-session interoceptive gain and the Schillings three-week longitudinal improvement are both arguments that the scaffold can be internalized — but only if the training architecture explicitly designs for transfer. The NeuroMinute script for cardiac-anchored breathing should include a "without device" segment in which the user attempts to sustain the pace from felt cardiac rhythm, not from the haptic cue.

---

## The Test

**N = 14 CRNA participants.** **Design = 14-day within-subject crossover.** **Duration = two 7-day phases with one rest day between.**

Phase A: Standard resonant frequency breathing at individually calibrated rate (from prior assessment), external clock pacing. Phase B: Cardiac-anchored breathing at the same target frequency, cardiac-phase-timed pacing cues from wearable.

**Primary outcome:** Peak session RMSSD during each protocol phase.

**Secondary outcomes:** Within-session HRV coherence (time to stable sinusoidal oscillation in the 0.05-0.15 Hz band); MAIA-2 Noticing subscale at days 0, 7, 14; heartbeat detection task accuracy at days 0 and 14.

**Falsification criterion:** If peak session RMSSD does not differ between cardiac-anchored and external-clock conditions, the phase-timing mechanism does not produce measurable additional autonomic gain and the protocol offers no advantage beyond standard resonant frequency training. If it does differ, the magnitude of that difference is the size of the cardiac-phase optimization effect.

This design would be the first direct head-to-head comparison of cardiac-anchored and external-clock breathing at equivalent target frequencies, isolating the contribution of phase timing from the contribution of frequency.

---

## The Connection

Cardiac-anchored breathing is the product moat. Not a feature — an architectural requirement. Every breathwork app on the market (Calm, Headspace, Breathwrk, Oak) uses an external clock because it has no access to real-time cardiac data. Pausality has that data from wearable integration. The data already exists. The cardiac-anchored protocol is what transforms that data from a measurement into an intervention.

It connects to [[resonant-breathing-frequency]] because the anchor is not arbitrary — it finds the user's optimal frequency by listening to the cardiac signal rather than prescribing a target. It connects to [[anterocept]] because the haptic heartbeat feedback builds Anterocept Domain 2 (cardiac awareness) in every session. It connects to [[interoceptive-literacy]] because the end state is not a user who breathes well with the app — it is a user who breathes well from their own body signal, device or not.

Eckberg's 1980 finding established that the heart has phases of opportunity. Cardiac-anchored breathing is an architecture for arriving at those phases on purpose rather than by chance.

---

*The moment the app stops pacing and the body keeps the rhythm — that is when the tool has done its job.*

---

## References (Verified)

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Eckberg DL, Kifle YT, Roberts VL | 1980 | Phase relationship between normal human respiration and baroreflex responsiveness | Journal of Physiology | 7441548 | 10.1113/jphysiol.1980.sp013338 | YES |
| 2 | Kralemann B et al. | 2013 | In vivo cardiac phase response curve elucidates human respiratory heart rate variability | Nature Communications | 23995013 | 10.1038/ncomms3418 | YES |
| 3 | Elstad M et al. | 2018 | Cardiorespiratory interactions in humans and animals: rhythms for life | American Journal of Physiology: Heart and Circulatory Physiology | 29522373 | 10.1152/ajpheart.00701.2017 | YES |
| 4 | Cysarz D, Büssing A | 2005 | Cardiorespiratory synchronization during Zen meditation | European Journal of Applied Physiology | 15940533 | 10.1007/s00421-005-1379-3 | YES |
| 5 | Dobrushina O, Tamim Y, Wald IY et al. | 2024 | Interoceptive training with real-time haptic versus visual heartbeat feedback | Psychophysiology | 39152653 | 10.1111/psyp.14648 | YES |
| 6 | Schillings C, Karanassios G, Schulte N et al. | 2022 | The effects of a 3-week heartbeat perception training on interoceptive abilities | Frontiers in Neuroscience | 35615275 | 10.3389/fnins.2022.838055 | YES |
| 7 | Burlacu A et al. | 2026 | Autonomic non-responsiveness in HRV biofeedback: a narrative conceptual review and future directions for AI-guided closed-loop adaptive systems | Medicina (Kaunas) | 42356115 | 10.3390/medicina62061102 | YES |
