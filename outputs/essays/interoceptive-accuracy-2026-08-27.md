---
title: "Notes from the Lab: The Three-Dimensional Body — Interoceptive Accuracy and the Miscalibration Problem"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-27
word_count: 1487
core_claim: "Interoceptive accuracy (objective cardiac detection), sensibility (self-report), and awareness (knowing how accurate you are) are genuinely dissociable dimensions of a single sense — and the clinical failure mode is not low accuracy, but the invisible gap between what the clinician's body actually detects and what they believe it detects."
related_concepts:
  - interoceptive-accuracy
  - interoceptive-literacy
  - anterocept
  - state-drift
  - maia-2-crna
evidence_used:
  - urn:srl:evidence:ali-awareness-exercise-relationship-cycles
  - urn:srl:observation:interoception-measurement-triangulation
pubmed_citations_verified: 6
gertrude_status: pass
---

# Notes from the Lab: The Three-Dimensional Body — Interoceptive Accuracy and the Miscalibration Problem

*Interoceptive accuracy, sensibility, and awareness are dissociable dimensions of a single sense — and in clinical practice, the catastrophic failure mode is not inaccuracy but miscalibration: the practitioner whose cardiac detection remains intact while metacognitive insight collapses cannot know what they cannot know.*

---

## The Observation

Hour three of a seven-hour posterior spinal fusion. The CRNA is running standard hemodynamics: MAP holding, end-tidal CO2 steady, blood loss tracked. Ask them how they feel. "Fine. A little tired, but fine."

Run a heartbeat detection task right now — ask them to count their own heartbeats for 25 seconds without touching their pulse. In a normative population, N=80, Garfinkel and colleagues found that performance on this objective task is essentially uncorrelated with how people *think* they perform it. The tired CRNA may detect their heartbeat accurately. The problem is they have no idea whether they do. That gap — between actual accuracy and metacognitive insight into it — is what Garfinkel called interoceptive awareness. And in sustained high-demand clinical work, it is the dimension most likely to erode first.

This is not about being numb to the body. It is about being confidently wrong about what the body is saying.

---

## The Mechanism

In 2015, Garfinkel, Seth, Barrett, Suzuki, and Critchley published the foundational dissociation study in *Biological Psychology*. In a normative sample of 80 participants, they empirically demonstrated that three proposed dimensions of interoception — accuracy, sensibility, and awareness — are genuinely, statistically dissociable. They do not track together. A person who scores high on objective heartbeat detection performance does not necessarily score high on self-report measures of bodily sensitivity, and neither predicts whether they have metacognitive insight into their own detection accuracy (Garfinkel et al., 2015 [PMID: 25451381]).

The three dimensions, precisely defined:

**Interoceptive accuracy** is the behavioral, objective dimension — performance on tasks like the Schandry heartbeat counting task or the Whitehead heartbeat discrimination task. It measures what the brain actually does with cardiac afferent signals.

**Interoceptive sensibility** is the self-report dimension — questionnaire measures of how aware and sensitive one believes oneself to be. The MAIA-2 captures this. It is a trait belief, not a performance measure.

**Interoceptive awareness** is the metacognitive dimension — the correspondence between accuracy and sensibility. High interoceptive awareness means knowing how accurate you are. Low awareness means your belief about your performance diverges from actual performance.

The clinical significance of the dissociation was clarified by Murphy, Catmur, and Bird in 2019, who argued in *Psychonomic Bulletin & Review* that even Garfinkel's three-dimensional model required further refinement: researchers need to distinguish not only *how* interoception is measured (objective vs. self-report) but *what* is measured — accuracy versus *attention*. The ability to detect a signal and the capacity to attend to that signal are separable (Murphy et al., 2019 [PMID: 31270764]). This matters for training design: if a practitioner's accuracy is intact but their attentional allocation to body signals is suppressed, the intervention target is attentional, not perceptual.

Garfinkel and colleagues also demonstrated that accuracy is modality-specific. In a 2017 study published in *Philosophical Transactions of the Royal Society B*, cardiac and respiratory interoceptive accuracy were dissociable — poor performance on one did not predict poor performance on the other. What transferred across modalities was metacognitive awareness: individuals who had good insight into their cardiac accuracy tended to have good insight into their respiratory accuracy. Critically, poor respiratory accuracy was associated with heightened anxiety, while good metacognitive awareness for cardiac signals was associated with *reduced* anxiety (Garfinkel et al., 2017 [PMID: 28080971]).

This last finding is pivotal for clinical contexts. It suggests that it is not the accuracy of signal detection that protects against affective dysregulation — it is knowing how accurate you are. A practitioner who is objectively good at detecting their cardiac state but lacks insight into that goodness has no usable information from which to calibrate their self-assessment. The body is accurate; the operator does not know to trust it.

What happens when these dimensions diverge in extreme ways was illustrated by a 2014 study in *PLoS One* examining depersonalization-derealization disorder. Michal and colleagues found that patients with depersonalization — who report overwhelming disconnection from their own bodies — performed equivalently to healthy controls on heartbeat detection tasks. Accuracy was intact. The body knew. But the phenomenological sense of embodiment was completely absent. The authors concluded that the deficit was in the integration of visceral signals into a unified sense of self, not in the detection of those signals (Michal et al., 2014 [PMID: 24587061]).

For CRNAs, the depersonalization study offers a mirror image of the clinical risk. DPD patients feel disembodied despite accurate detection. CRNAs under sustained occupational load may feel embodied and fine — sensibility is reporting "normal" — while the metacognitive layer that would allow them to *verify* that report has quietly degraded. The sensation remains. The self-monitoring of the sensation's reliability has gone offline.

Garfinkel's autism study reinforces the point from a different angle. In 2016, Garfinkel and colleagues found that individuals with autism spectrum conditions showed the opposite profile from what was expected: reduced objective accuracy alongside exaggerated subjective sensibility. The divergence — high self-report, low actual performance — correlated with emotion deficits and anxiety symptoms. The authors computed this discordance as a "trait prediction error": the gap between expected accuracy (based on sensibility beliefs) and actual accuracy (Garfinkel et al., 2016 [PMID: 26724504]).

Trait prediction error is exactly what goes unmeasured in CRNA fatigue assessments. Not "are you perceiving body signals?" but "is your belief about your perception accurate?"

The final measurement implication comes from Harrison, Garfinkel, and colleagues' 2021 *Biological Psychology* paper, which presented the Filter Detection Task — a breathing-interoception measure designed to quantify interoceptive sensitivity, decision bias, metacognitive bias, and metacognitive performance simultaneously. The task was developed precisely because clinical research requires tools that work within short sessions and noisy environments. The metacognitive outputs — not just accuracy scores — are where the clinical signal lives (Harrison et al., 2021 [PMID: 34487805]).

---

## The Protocol

The Pausality measurement framework, developed from the Garfinkel model, operationalizes all three dimensions at clinical scale:

1. **Interoceptive sensibility** — MAIA-2 short-form embedded in the app as weekly micro-check-ins. Baseline, monthly, and quarterly retest. Tracks subjective belief about body awareness across time.

2. **Interoceptive accuracy** — Heartbeat Detection Game: practitioner counts their own heartbeats against Apple Watch sensor ground truth across a 25-second window. Computable on device. Scales the Schandry task.

3. **Interoceptive awareness** — Confidence slider after each heartbeat detection trial: "How certain are you?" The correspondence between confidence and actual performance is the awareness score. This is the dimension that predicts whether the practitioner can self-correct.

The training prescription is specific: if accuracy is low but awareness is high, the practitioner knows they are struggling — the signal is available and they can act on it. If accuracy is adequate but awareness is low, no signal reaches the behavioral layer. This is the invisible state. This is what must be trained.

---

## The Failure Mode

The dangerous miscalibration pattern is high sensibility + low awareness.

Sensibility is a belief structure, and beliefs are sticky. A CRNA who has spent years trusting their body — appropriately — carries a strong prior that their body is reliable. Under occupational stress, when interoceptive accuracy begins to degrade and state drift begins, the high-sensibility prior protects the belief ("I feel fine") while the metacognitive layer that would update the prior has already gone offline.

This is not a failure of the body. It is a failure of the feedback loop. The body continues to send signals. The decoder remains convinced of its accuracy. Nothing corrects.

A secondary failure mode: training interoceptive sensibility (the standard wellness-app approach — "notice how you feel") without training interoceptive accuracy or awareness. Raising sensibility beliefs without grounding them in better detection performance or metacognitive calibration produces precisely the inflated-sensibility, low-accuracy profile that Garfinkel documented in autism. It feels like progress. It does not produce it.

---

## The Test

**Minimal viable experiment — 14 days, 12 practitioners:**

- Practitioner baseline: MAIA-2 sensibility, 5-trial heartbeat detection accuracy, confidence-accuracy correspondence score
- Daily: two heartbeat detection trials with confidence slider, 3-item MAIA micro-check-in
- Outcome: Does daily accuracy measurement (with immediate feedback) shift confidence-accuracy correspondence? Does awareness improvement predict self-reported state drift episodes?
- Confound declared: this doesn't control for circadian variation in cardiac signal strength; measure at consistent time-of-day relative to shift start
- Success criterion: ≥30% improvement in confidence-accuracy correspondence over 14 days; correlation r > 0.30 between awareness gain and MAIA subscale shifts

The hypothesis is trainable: metacognitive awareness is not a fixed trait. Garfinkel's own data showed it was only robustly present in the highest-accuracy individuals — which implies that accuracy training drives awareness, not the reverse.

---

## The Connection

Every SRL protocol assumes that practitioners can read themselves. [[interoceptive-accuracy]] is the empirical test of that assumption. It connects directly to [[interoceptive-literacy]] — the translational bridge from raw detection to usable clinical signal — and to [[anterocept]], whose training specifically targets the sensory-motor layer where detection failures originate. The three-dimension framework also grounds [[maia-2-crna]]: if MAIA measures sensibility, not accuracy, then using MAIA alone as an outcome measure systematically overstates practitioner capability while missing the metacognitive failure that precedes state drift.

The vault's fundamental claim is that the clinician is a sensor. This essay specifies what that means with precision: the sensor has three settings, they dissociate from each other, and only one of them — awareness — tells you whether the other two can be trusted.

---

*Three hours into a seven-hour case, the heartbeat runs beneath everything — felt and not-felt, known and unknown, steady until it isn't. Calibration is not a metaphor. It is the measurement problem.*

---

## References (Verified)

Based on articles retrieved from PubMed, the following citations have been verified via PMID metadata lookup. All fields confirmed.

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Garfinkel SN, Seth AK, Barrett AB, Suzuki K, Critchley HD | 2015 | Knowing your own heart: distinguishing interoceptive accuracy from interoceptive awareness | Biological Psychology | 25451381 | [10.1016/j.biopsycho.2014.11.004](https://doi.org/10.1016/j.biopsycho.2014.11.004) | YES |
| 2 | Garfinkel SN, Tiley C, O'Keeffe S, Harrison NA, Seth AK, Critchley HD | 2016 | Discrepancies between dimensions of interoception in autism: Implications for emotion and anxiety | Biological Psychology | 26724504 | [10.1016/j.biopsycho.2015.12.003](https://doi.org/10.1016/j.biopsycho.2015.12.003) | YES |
| 3 | Garfinkel SN, Manassei MF, Hamilton-Fletcher G, In den Bosch Y, Critchley HD, Engels M | 2017 | Interoceptive dimensions across cardiac and respiratory axes | Philosophical Transactions of the Royal Society B | 28080971 | [10.1098/rstb.2016.0014](https://doi.org/10.1098/rstb.2016.0014) | YES |
| 4 | Murphy J, Catmur C, Bird G | 2019 | Classifying individual differences in interoception: Implications for the measurement of interoceptive awareness | Psychonomic Bulletin & Review | 31270764 | [10.3758/s13423-019-01632-7](https://doi.org/10.3758/s13423-019-01632-7) | YES |
| 5 | Harrison OK, Garfinkel SN, et al. | 2021 | The Filter Detection Task for measurement of breathing-related interoception and metacognition | Biological Psychology | 34487805 | [10.1016/j.biopsycho.2021.108185](https://doi.org/10.1016/j.biopsycho.2021.108185) | YES |
| 6 | Michal M, Reuchlein B, Adler J, et al. | 2014 | Striking discrepancy of anomalous body experiences with normal interoceptive accuracy in depersonalization-derealization disorder | PLoS One | 24587061 | [10.1371/journal.pone.0089823](https://doi.org/10.1371/journal.pone.0089823) | YES |
