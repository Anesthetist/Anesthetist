---
title: "Notes from the Lab: The CRNA as Closed-Loop Physiological Controller"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-25
word_count: 1410
core_claim: "A CRNA's autonomic nervous system is not a bystander in the operating room — it is the primary sensor, integrating instrument, and recovery mechanism for everything happening at the table, which means calibrating it is not self-care; it is patient safety."
related_concepts:
  - crna-as-closed-loop-controller
  - sensor-calibration-as-patient-safety
  - closed-loop-biofeedback
  - interoceptive-literacy
  - clinician-durability
  - interoception
evidence_used:
  - craig-2009-interoception-awareness
  - feldman-2017-prebotc-locus-coeruleus-arousal
  - balban-huberman-2023-cyclic-sighing
pubmed_citations_verified: 6
gertrude_status: pass
---

# Notes from the Lab: The CRNA as Closed-Loop Physiological Controller

*A CRNA's autonomic nervous system is not a bystander in the operating room — it is the primary sensor, integrating instrument, and recovery mechanism for everything happening at the table, which means calibrating it is not self-care; it is patient safety.*

---

## The Observation

During laryngoscopy, experienced CRNAs routinely hold their breath. Nobody teaches this. Nobody tracks it. Across 28 years and thousands of intubations, Randy Graybeal noticed it about himself: the moment the blade goes in, the breath stops.

The patient is apneic — pharmacologically paralyzed, metabolism suppressed, CO₂ dropping. The provider is the opposite: sympathetically activated, physically moving, cognitively loaded, CO₂ rising faster than at rest. Two nervous systems in opposite metabolic states, one of which has temporarily taken over regulation of the other.

And the clinician synchronizes to the patient's apnea anyway.

This is not anxiety. It is not a breathing tic. It is the signal-channel between two nervous systems becoming briefly audible — if anyone is listening. The CRNA's breath-hold during intubation is a measurable data stream hiding in plain sight, and it contains information about clinical state that no monitor in the room is capturing.

---

## The Mechanism

Control theory describes any system where outputs are continuously monitored and fed back to adjust subsequent inputs. The thermostat is the textbook case: sensor reads temperature, compares to set point, adjusts heat output, loops again in seconds. The controller is distinct from the system it regulates.

The CRNA during an anesthetic is not an analogy to a closed-loop controller. It is one.

**Inputs** arrive continuously: patient vitals on the monitors, the surgical field's behavior, the surgeon's cadence, the ventilator compliance, the pharmacokinetic clock ticking on every agent on board. **Integration** happens in the clinician's nervous system — the biological layer that weighs all inputs simultaneously and produces a clinical judgment. **Output** is titration: of anesthetic depth, of vasoactives, of ventilatory support, of communication, of when to act and when to wait. **Feedback** loops back in seconds to minutes, unbroken across the case.

The load-bearing implication arrives immediately: in any control system, the quality of the output is bounded by the fidelity of the sensor. A thermostat with a degraded temperature sensor doesn't know it's reading high. It continues adjusting outputs with full confidence, based on corrupt data.

A.D. Craig, in a landmark 2009 review in *Nature Reviews Neuroscience*, described the anterior insular cortex as the brain's real-time representation of the body's physiological condition — a continuously updated interoceptive map of everything happening in the body, available to higher-order cognition for decision-making Craig (2009) [PMID: 19096369]. This is the CRNA's primary sensor. Not the SpO₂ probe. The insula reading the provider's own body.

When that sensor degrades — from cumulative stress, sleep deficit, post-case adrenaline residue, or the fourth pediatric airway of a shift — the clinician does not receive an error message. The insula continues producing signal. It is simply noisier. Every downstream decision inherits that noise.

Breath is the fastest voluntary handle on this system. Yackle and colleagues (2017), publishing in *Science*, demonstrated that a subpopulation of neurons in the mouse preBötzinger complex — the brainstem's primary respiratory rhythm generator — projects directly to the locus coeruleus, the brain's principal arousal hub Yackle et al. (2017) [PMID: 28360327]. Breath pace modulates arousal state through a direct anatomical pathway. This is not belief-mediated. It is structural.

Zaccaro and colleagues (2018), in a systematic review of 15 controlled studies examining slow breathing techniques (<10 breaths/minute), found consistent increases in heart rate variability and respiratory sinus arrhythmia, parallel decreases in EEG theta power, and elevated alpha activity — the electrophysiological signature of calm, alert readiness Zaccaro et al. (2018) [PMID: 30245619]. Two mechanisms were identified: voluntary regulation of internal bodily states via interoceptive pathways, and nasal mechanoceptor stimulation that modulates olfactory bulb activity and tunes the cortical mantle broadly.

The practical translation: a CRNA who takes three slow, exhale-extended breaths between induction and intubation is not "calming down." They are recalibrating the sensor before taking the most consequential measurement of the case. The language of self-care is the wrong frame. The language of instrument maintenance is exact.

---

## The Protocol: Instrument Calibration in Three Phases

If the CRNA is a closed-loop controller, calibration is a professional responsibility, not a personal wellness choice. The maintenance cycle has three phases:

**1. Pre-Shift Baseline (2–3 minutes)**
Before the first case, measure resting HRV — three minutes of quiet breathing, RMSSD or HF-power capable wearable. This establishes today's operating point: the sensor's reference coordinate against which all case-related variance will be interpreted. A provider with an RMSSD of 38ms today is a different instrument than the same provider at 62ms last Thursday. Both providers can intubate. They cannot be treated identically by a responsible system.

**2. Transition-Point Micro-Calibration (60 seconds)**
At natural workflow gaps — patient positioned and draped before first cut, post-induction stabilization, pre-handoff — use a single exhale-extended breath cycle or a five-breath resonant sequence. Balban and colleagues (2023), in a randomized controlled trial published in *Cell Reports Medicine*, showed that five minutes of daily cyclic sighing (exhale-emphasized breathing) produced significantly greater improvements in mood and reduction in respiratory rate compared to mindfulness meditation Balban et al. (2023) [PMID: 36630953]. One minute at workflow gaps is not conservative protocol. It is optimized by the fastest-acting breath intervention currently in the RCT literature.

**3. Post-Case Recovery Measurement (2 minutes)**
After patient transfer to PACU, repeat HRV measurement and log BOLT score (body oxygen level test: maximum comfortable breath-hold duration following a normal exhale). Compare to pre-shift baseline. This number tells the provider — and their system, if the system is paying attention — what the sensor returned to between cases, and whether sequential caseloads are producing compounding degradation or genuine recovery.

Track three numbers per shift: pre-shift RMSSD, post-case RMSSD, BOLT score. Over two weeks, a pattern emerges. Not a wellness journal. An autonomic map — the anti-fragility curve nobody has ever drawn on a CRNA.

Success looks like: delta-RMSSD recovers to within 15% of pre-shift baseline between cases. Failure looks like: progressive decline across a shift with no recovery above 60% of morning baseline. Both are actionable information. Neither is currently being captured.

---

## The Failure Mode: The Corrupted Sensor Reports Itself as Clean

The most dangerous failure mode of a degraded sensor is not that it reads nothing. It is that it reads confidently and incorrectly.

Zafiriou and colleagues (2026), in a prospective simulation study published in *PLoS One*, enrolled 34 anesthesia professionals — including nurse anesthetists — in a high-fidelity pediatric laryngospasm simulation Zafiriou et al. (2026) [PMID: 42228700]. Resilience was measured using the Connor-Davidson Resilience Scale (CD-RISC 10). Heart rate variability was the primary physiological endpoint.

Result: no significant association was found between resilience scores and physiological response to acute crisis (p = 0.085 for HRV; p = 0.621 for self-reported stress). What providers believed about their resilience did not track what their bodies did under simulated emergency.

The clinician who scores high on the resilience instrument is not necessarily the clinician whose HRV holds under a hypoxic infant. These are measuring different things. One is a belief about the self. The other is the sensor's operating state.

This is the failure mode: **the provider's subjective assessment of readiness is not a reliable proxy for sensor fidelity**. The corrupted sensor is the one reporting its own calibration status. A clinician who "feels fine" after three consecutive complex cases may simply be past the threshold where degradation registers as felt experience. The signal is gone. The instrument reports silence as calm.

This is why objective measurement is not optional. Self-report is not a substitute for HRV. The body knows before the clinician does — or it stops knowing, and the clinician doesn't notice that either.

---

## The Test

**Population:** 10 active CRNAs, any setting.
**Equipment:** HRV-capable wearable (Polar H10 or equivalent), BOLT protocol.
**Protocol:** Pre-shift RMSSD, post-case RMSSD + BOLT after each case, end-of-shift log.
**Primary hypothesis:** Average RMSSD shows statistically detectable within-shift decline across sequential cases (repeated measures, within-person design).
**Secondary hypothesis:** BOLT score correlates with post-case RMSSD delta more strongly than self-reported case complexity ratings.
**Duration:** 14 working days.
**Failure condition:** No measurable within-shift HRV trend in the majority of participants — hypothesis is not supported; rethink the model.

This is not a clinical trial. It is a two-week instrument characterization study. The goal is not to publish. The goal is to know whether the sensor degrades in the pattern the model predicts.

---

## The Connection

Every SRL training protocol is, mechanistically, an instrument maintenance procedure: [[gap-moment-training]] is a scheduled recalibration window. [[neurominute]] is the minimum-dose protocol for a mid-case reset. [[resonant-breathing-frequency]] is the personalized tuning frequency for each provider's sensor. [[cardiac-anchored-breathing]] is the advanced protocol for real-time tracking of the calibration result.

[[sensor-calibration-as-patient-safety]] is the political translation of this frame — shifting the budget category from wellness (discretionary) to clinical operations (structural). [[clinician-durability]] is the longitudinal outcome: a calibrated sensor over a 28-year career versus one that degrades silently and fails a patient at year 22.

The controller is the care. Maintaining it is not a favor to the clinician. It is a debt owed to every patient on the table.

---

*The instrument is held in the provider's chest. It is measuring right now. The question is whether anyone is reading it.*

---

## References (Verified)

Based on articles retrieved from PubMed, the following citations were verified via PMID metadata lookup — title, authors, journal, year, DOI, and abstract confirmed prior to inclusion.

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Craig A.D. | 2009 | How do you feel—now? The anterior insula and human awareness | Nat Rev Neurosci | 19096369 | [10.1038/nrn2555](https://doi.org/10.1038/nrn2555) | YES |
| 2 | Yackle K, Schwarz LA, Kam K, Sorokin JM, Huguenard JR, Feldman JL, Luo L, Krasnow MA | 2017 | Breathing control center neurons that promote arousal in mice | Science | 28360327 | [10.1126/science.aai7984](https://doi.org/10.1126/science.aai7984) | YES |
| 3 | Zaccaro A, Piarulli A, Laurino M, Garbella E, Menicucci D, Neri B, Gemignani A | 2018 | How Breath-Control Can Change Your Life: A Systematic Review on Psycho-Physiological Correlates of Slow Breathing | Front Hum Neurosci | 30245619 | [10.3389/fnhum.2018.00353](https://doi.org/10.3389/fnhum.2018.00353) | YES |
| 4 | Balban MY, Neri E, Kogon MM, Weed L, Nouriani B, Jo B, Holl G, Zeitzer JM, Spiegel D, Huberman AD | 2023 | Brief structured respiration practices enhance mood and reduce physiological arousal | Cell Rep Med | 36630953 | [10.1016/j.xcrm.2022.100895](https://doi.org/10.1016/j.xcrm.2022.100895) | YES |
| 5 | Zafiriou Y, Evain JN, Bertrand B, Archer G, Botton J, Crozet J, Khediri I, Lefevre M, Marcel C, Sery C, Ego A, Albaladejo P, Picard J | 2026 | Is resilience linked to stress response among anesthesia professionals? A prospective simulation-based study | PLoS One | 42228700 | [10.1371/journal.pone.0350343](https://doi.org/10.1371/journal.pone.0350343) | YES |
| 6 | Craig A.D. | 2010 | The sentient self | Brain Struct Funct | 20512381 | [10.1007/s00429-010-0248-y](https://doi.org/10.1007/s00429-010-0248-y) | YES |
