---
title: "Notes from the Lab: The Category Nobody's Building"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-29
word_count: 1680
core_claim: "Interoceptive technology — devices that sense, represent, and close the loop on the body's internal signals — constitutes a categorically distinct product category from content-delivery wellness apps, and the evidence now shows that the feedback modality and adaptivity of that loop determines whether autonomic regulation actually changes."
related_concepts:
  - interoceptive-technology
  - closed-loop-biofeedback
  - haptic-biofeedback
  - neuroadaptive-training-system
  - somnistics
  - resonant-breathing-frequency
evidence_used:
  - schoeller-2019-interoceptive-technologies
  - dobrushina-2024-haptic-heartbeat-feedback
  - mensinger-2024-hrv-biofeedback-healthcare-workers
  - zhang-2023-interoceptive-neurofeedback-insula
  - vaschillo-lehrer-2006-resonance-characteristics
  - burlacu-2026-autonomic-non-responsiveness
pubmed_citations_verified: 6
gertrude_status: pass
---

# Notes from the Lab: The Category Nobody's Building

*Interoceptive technology — devices that sense, represent, and close the loop on the body's internal signals — constitutes a categorically distinct product category from content-delivery wellness apps, and the evidence now shows that the feedback modality and adaptivity of that loop determines whether autonomic regulation actually changes.*

---

## The Observation

A CRNA finishes her third case of the day. Between rooms, she opens a wellness app and breathes along with an animated circle for four minutes. Somewhere on her wrist, a fitness tracker records a drop in heart rate variability. Neither device knows the other exists. The app delivered content. The tracker generated data. No loop closed. Her nervous system received a fixed protocol regardless of its actual state on that particular afternoon — regardless of whether she was activated, shut down, or somewhere in the middle.

This is the current architecture of the wellness technology market: devices that measure and apps that prescribe, operating in separate silos, producing what might be called wellness theater. The user feels as though something happened. Physiologically, the evidence increasingly suggests: it depends entirely on whether the feedback matched the state.

The category that does something different barely exists. It has a name — interoceptive technology — and a small but rapidly growing literature. Understanding it changes how SRL's product is positioned, what it needs to do, and why fixed-rate breathing protocols are structurally inadequate.

---

## The Mechanism

In 2019, Schoeller, Haar, Jain, and Maes published a review in *Physics of Life Reviews* that named the category: interoceptive technology. Their definition is specific: somatosensory interfaces and emotion prostheses that modulate body perception and human emotions through interoceptive illusions — devices that, in their words, exploit "the constant feedback loop between actual and expected sensations during interoceptive processing" to intervene on higher cognitive functioning Schoeller et al. (2019) [PMID: 31757602].

The category has three definitional components, all required:
1. **Sense** — capture physiological signals from the body's interior
2. **Represent** — translate those signals into a form the user can perceive
3. **Modulate** — create a feedback loop that enables the user to shift their internal state

A fitness tracker satisfies (1) only. A meditation app timer satisfies none. A closed-loop HRV biofeedback device with adaptive pacing satisfies all three.

The distinction matters because interoception is not a passive read-out. The anterior insula — the brain's primary interoceptive cortex — is a predictive organ: it constantly generates predictions about what the body's signals will be, and then updates those predictions based on incoming data. Zhang and colleagues demonstrated this directly in a randomized sham-controlled trial: using heartbeat detection as a regulation strategy, participants trained to up-regulate left anterior insula (LAI) activity during real-time fMRI neurofeedback, with the capacity maintained in a transfer session conducted without feedback Zhang et al. (2023) [PMID: 37952779]. The LAI regulation was associated with strengthened functional connectivity with cognitive control, memory, and salience networks — precisely the networks whose degradation is tracked in [[state-drift]] and [[neural-transition-failure]]. The interoceptive loop, once trained, persisted.

The second mechanism discovery concerns *how* the feedback is delivered, not just *whether* it is delivered. In a randomized controlled trial involving sixty adults, Dobrushina, Tamim, Wald, Maimon, and Amedi compared real-time haptic heartbeat feedback to real-time visual heartbeat feedback. A single session of haptic — but not visual — feedback increased interoceptive accuracy and confidence, as measured by the heart rate discrimination task, and produced a measurable shift of attention toward the body Dobrushina et al. (2024) [PMID: 39152653]. Their explanation is structural: haptic feedback matches the sensory modality of the natural bodily prototype (the heartbeat is felt, not seen). Representing a heartbeat as a light on a screen is a translation. Representing it as vibration on the skin is an amplification. One is a metaphor; the other is a signal in the body's native format.

The third mechanism is individualization. Vaschillo, Vaschillo, and Lehrer documented that resonant frequency — the breathing rate at which heart rate oscillations are maximally amplified through baroreflex engagement — is physiologically individual. It varies negatively with height, differs between men and women, but remains stable across ten training sessions and appears to be determined by blood volume Vaschillo, Vaschillo, & Lehrer (2006) [PMID: 16838124]. This is not a population statistic to be prescribed; it is a physiological parameter to be discovered. A fixed-rate app that prescribes 5.5 breaths per minute is approximating the average. The average is not the body in front of you.

In a clinical population — healthcare workers during the COVID-19 pandemic — Mensinger, Weissinger, Cantrell, Baskin, and George piloted an HRV biofeedback mobile app and found preliminary evidence of improved interoceptive sensibility, mindful self-care, resilience, and stress reduction Mensinger et al. (2024) [PMID: 38502516]. Participants reported that the app helped them "connect better to their body's signals." This is not a metaphor. It is a description of the feedback loop closing.

---

## The Framework

Three tiers define the current technology landscape for autonomic health. They look superficially similar but are mechanistically distinct:

**Tier 1 — Content Delivery Platforms.** Apps that provide audio, video, or guided instructions designed to promote calm. They deliver the same content regardless of the user's physiological state. Calm, Headspace, and the majority of the app store wellness category operate here. Input: user opens app. Output: content plays. No body reading occurs.

**Tier 2 — Monitoring Platforms.** Wearables and trackers that capture physiological signals (HRV, heart rate, SpO2, temperature) and present them to the user as data. Garmin, Apple Watch, Oura Ring operate primarily here. Input: body generates signals. Output: data displayed. Some apps layer Tier 1 content on top of Tier 2 data, but the feedback loop does not close — the content does not change based on the data.

**Tier 3 — Interoceptive Technology.** Devices where the body's signal becomes the input to a feedback loop that adapts the output in real time. The loop must actually close: what the body does determines what the device does next, which determines what the body does next. This is the category Schoeller et al. defined. It is the category SRL's Pausality™ architecture is designed to occupy.

The distinction between Tier 2 and Tier 3 is the loop closure. A wearable that shows you your HRV is not interoceptive technology. A system that reads your HRV, determines your current resonant state, and adapts the breathing guidance to approach your individual resonant frequency in real time — that is.

---

## The Failure Mode

The loop closure requirement is also where the category breaks. Burlacu and colleagues reviewed the literature on HRV biofeedback non-responsiveness — cases where the expected autonomic engagement is weakened, absent, or fails to produce clinical benefit Burlacu et al. (2026) [PMID: 42356115]. Their findings are direct: reduced autonomic flexibility, impaired baroreflex function, fatigue, stress-related overload, and dysfunctional breathing patterns all produce non-response to fixed HRV biofeedback protocols. The protocol that works when the user is moderately activated may fail entirely when they are in dorsal vagal shutdown or sympathetic flood. A fixed protocol cannot read the room.

This is the structural argument for adaptive systems — and the structural indictment of most existing interoceptive technology products. A system that prescribes 5.5 BPM regardless of today's state is a Tier 1 tool wearing Tier 3 clothing. The feedback loop appears to close (the heart rate data is being read) but the output does not adapt (the pacing stays fixed). Burlacu et al.'s proposed solution — AI-guided closed-loop adaptive systems that recognize non-responsiveness and adjust in real time — is precisely the architecture required.

The second failure mode is subtler: training interoception without transferring the skill. Zhang et al.'s finding that anterior insula regulation persisted without feedback is the benchmark. A product that produces regulation only during active biofeedback sessions has taught the user nothing. The goal is not ongoing feedback dependency; the goal is training the interoceptive prediction system to operate correctly without external scaffolding. Haptic feedback, in Dobrushina et al.'s terms, may accelerate this transfer by using the body's native signal format.

---

## The Test

Minimum viable experiment: 10 CRNAs, 14 days, two-arm crossover design.

**Arm A:** Adaptive closed-loop breathing guidance that reads RMSSD in real time and adjusts pacing toward individual resonant frequency (estimated from session 1 baseline). Four minutes between surgical cases.

**Arm B:** Fixed 5.5 BPM breathing app, same time windows, same population.

**Measurements:**
- Pre- and post-case RMSSD (wearable)
- Interoceptive accuracy scores (heartbeat discrimination task, administered week 1 and week 3)
- Self-reported state accuracy ("how activated do you feel?" vs. RMSSD actual state — the gap between these is the interoceptive literacy metric)

**Success criteria:** Arm A produces greater RMSSD recovery between cases; Arm A produces greater improvement in self-report / RMSSD alignment at week 3.

**Failure criteria:** No difference between arms — which would suggest the pacing adaptation adds no value over a well-calibrated fixed rate, and would require re-examining whether the resonant frequency individualization effect is clinically significant at the 4-minute dose.

This experiment is testable at small scale with a wrist-based HRV sensor and the existing Pausality™ architecture. The heartbeat discrimination task can be administered digitally in under 5 minutes.

---

## The Connection

This essay names the product category SRL occupies — not "meditation app," not "wellness platform," not "biofeedback device" in the generic sense, but interoceptive technology: Tier 3, loop-closed, adaptive, using the body's native signal modality (haptic, cardiac-anchored) rather than metaphorical representations. It directly enriches [[closed-loop-biofeedback]], [[haptic-biofeedback]], and [[neuroadaptive-training-system]]. It grounds [[resonant-breathing-frequency]]'s individuality claim in the hardware argument: you cannot use a fixed frequency because the frequency is individual. It provides the category language that distinguishes SRL from the Tier 1 and Tier 2 landscape in investor, clinical, and research contexts. The vault gap this essay exposes: no evidence note exists for Schoeller et al. 2019 — the paper that defines the category SRL inhabits.

---

*The body is already in conversation with itself — generating predictions, updating them, generating corrections. The question is not whether to join that conversation but whether the technology in the clinician's hand is actually listening, or merely talking.*

---

## References (Verified)

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Schoeller F, Haar AJH, Jain A, Maes P | 2019 | Enhancing human emotions with interoceptive technologies | Physics of Life Reviews | 31757602 | 10.1016/j.plrev.2019.10.008 | YES |
| 2 | Dobrushina O, Tamim Y, Wald IY, Maimon A, Amedi A | 2024 | Interoceptive training with real-time haptic versus visual heartbeat feedback | Psychophysiology | 39152653 | 10.1111/psyp.14648 | YES |
| 3 | Mensinger JL, Weissinger GM, Cantrell MA, Baskin R, George C | 2024 | A Pilot Feasibility Evaluation of a Heart Rate Variability Biofeedback App to Improve Self-Care in COVID-19 Healthcare Workers | Applied Psychophysiology and Biofeedback | 38502516 | 10.1007/s10484-024-09621-w | YES |
| 4 | Zhang Y, Zhang Q, Wang J, et al. | 2023 | "Listen to your heart": A novel interoceptive strategy for real-time fMRI neurofeedback training of anterior insula activity | NeuroImage | 37952779 | 10.1016/j.neuroimage.2023.120455 | YES |
| 5 | Vaschillo EG, Vaschillo B, Lehrer PM | 2006 | Characteristics of resonance in heart rate variability stimulated by biofeedback | Applied Psychophysiology and Biofeedback | 16838124 | 10.1007/s10484-006-9009-3 | YES |
| 6 | Burlacu A, Brinza C, Iftene A, Bogdan-Goroftei RE, Geman O | 2026 | Autonomic Non-Responsiveness in HRV Biofeedback: A Narrative Conceptual Review and Future Directions for AI-Guided Closed-Loop Adaptive Systems | Medicina | 42356115 | 10.3390/medicina62061102 | YES |
