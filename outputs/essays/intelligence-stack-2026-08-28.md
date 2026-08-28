---
title: "Notes from the Lab: The Architecture You're Already Running"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-28
word_count: 1487
core_claim: "Every expert CRNA is already executing all six layers of the Intelligence Stack — SENSE → INTERPRET → DECIDE → ORCHESTRATE → LEARN → GOVERN — in real time during anesthesia care; AI clinical decision support keeps underperforming not because the tools are primitive but because they intervene at the SENSE layer while the clinician carries Layers 2 through 6 unaided."
related_concepts:
  - intelligence-stack
  - intelligence-density
  - human-ai-decision-boundary
  - vigil-coordination-architecture
  - neurogating
  - state-drift
evidence_used:
  - urn:srl:evidence:ismail-organizational-singularity-2026
pubmed_citations_verified: 7
gertrude_status: pass
---

# Notes from the Lab: The Architecture You're Already Running

*Every expert CRNA is already executing all six layers of the Intelligence Stack — SENSE → INTERPRET → DECIDE → ORCHESTRATE → LEARN → GOVERN — in real time during anesthesia care; AI clinical decision support keeps underperforming not because the tools are primitive but because they intervene at the SENSE layer while the clinician carries Layers 2 through 6 unaided.*

## The Observation

Third hour of a complex abdominal case. The blood pressure is drifting — 82/54 from a baseline of 118/74. You notice before the alarm sounds. You have been watching the trend, not the number, and something in the waveform quality told you this was coming four minutes ago.

You do not reach for phenylephrine immediately. You run through a list that you are not consciously aware of running: fluid status, surgical field activity, agent concentration, patient position, the last dose of vasodilating medication. You file a provisional interpretation — vasodilation, probably position-related, volume-responsive — and you move.

The intervention is precise. The dose is small. You watch for the response. You adjust.

This is not intuition. It is architecture.

## The Mechanism

In 2013, Schulz, Endsley, Kochs, Gelb, and Wagner published a landmark review in *Anesthesiology* describing situational awareness (SA) as the defining cognitive competency of expert anesthetic practice. Drawing on Endsley's three-tier model — Level 1: Perception (sensing elements of the environment), Level 2: Comprehension (understanding what they mean in context), Level 3: Projection (anticipating what they will mean in the next three minutes) — Schulz et al. argued that most anesthetic errors trace not to technical failure but to breakdown somewhere in this cognitive loop [PMID: 23291626].

In 2026, Salim Ismail and colleagues articulated the Intelligence Stack as the organizing framework of the AI-native organization: six cognitive layers (SENSE, INTERPRET, DECIDE, ORCHESTRATE, LEARN, GOVERN) plus one cross-cutting control plane. The organizational theorists and the anesthesiologists, working in entirely different domains a decade apart, arrived at structurally identical architectures.

They were both describing how intelligence works.

Endsley's three tiers map cleanly to the first half of the stack:
- **SENSE = Perception (Level 1):** What signals are present in the environment right now?
- **INTERPRET = Comprehension (Level 2):** What do those signals mean in this specific clinical context?
- **DECIDE = Projection (Level 3):** What is about to happen, and what action is required now?

Ismail adds three layers that Endsley's SA model locates outside formal situational awareness but that every clinician knows are equally operative:
- **ORCHESTRATE:** The physical execution — the drug drawn, the rate adjusted, the surgical team alerted
- **LEARN:** The retrospective evaluation — was the interpretation correct? Did the response match the expectation? What updates the model?
- **GOVERN:** The overarching control plane — what am I not allowed to get wrong? Where are the hard stops?

The CRNA is not using a framework. The CRNA *is* the framework. Every anesthetic case is a complete intelligence cycle, running continuously, simultaneously across all six layers. The expert clinician who notices the BP trend before the alarm fires is running a faster, more accurate SENSE layer than a novice. The clinician who correctly distinguishes vasodilation from hemorrhage on the same vital sign number is running a more context-rich INTERPRET layer. The clinician who correctly projects the next five minutes of physiological trajectory is running a trained DECIDE layer. These are learnable, trainable cognitive capacities — and they are degradable under load.

## The Framework

What makes the Intelligence Stack clinically useful is not the abstraction — it is the localization of failure.

Recent research illuminates where each layer is being augmented or abandoned.

Pinsky et al. (2024), reviewing AI deployment in critical care, identified a core limitation of current clinical decision support systems: they are sophisticated at SENSE (signal collection) and basic INTERPRET (pattern matching), but they have essentially no situational awareness in Endsley's sense — they cannot construct the patient-specific context that makes a signal meaningful [PMID: 38589940]. An algorithm that detects a hemodynamic change cannot distinguish the patient who just received spinal anesthesia from the patient who is hemorrhaging. The clinician can. The machine lists both as "hypotension detected" with equivalent alarm priority.

Pinsky et al. call this the "situational awareness gap" and describe it as the central obstacle to effective AI deployment in acute care. This is not an AI limitation waiting to be solved with better models. It is a structural problem: INTERPRET requires embodied context — what happened three minutes ago, what the surgical field looks like, what the patient's baseline was before induction, how the patient responded to the last intervention. No data stream captures that. The clinician carries it.

Hunn et al. (2025) are working directly on Level 3 SA — building AI systems that display predicted vital sign trajectories rather than only current values, to help anesthesiologists project rather than only perceive [PMID: 41469047]. Their multicentre trial across five academic centers tests whether displaying anticipated future states improves the DECIDE layer. This is meaningful work. It is also an acknowledgment that Level 3 — clinical projection — is currently almost entirely carried by individual clinicians with no systematic AI support.

Wingert et al. (2026), at UCLA, implemented a random forest model predicting postoperative mortality directly into the EHR, achieving an AUROC of 0.874 [PMID: 41549026]. The model tells anesthesiologists something about patient risk before surgery. It does not tell them what to do about it. DECIDE remains human. The model intervenes between SENSE and INTERPRET, providing a compressed signal — this patient is higher risk — that the clinician must still interpret and act on.

Singh and Nath (2022) surveyed the AI-in-anesthesia landscape and found that closed-loop pharmacological systems represent the most complete AI integration of the full cycle [PMID: 35261595]. For propofol delivery and hemodynamic management in narrow parameter spaces, the system handles SENSE (monitoring drug effect), INTERPRET (comparing to target), DECIDE (calculating dose adjustment), and ORCHESTRATE (executing the adjustment) autonomously. Outside those narrow boundaries, the clinician retakes control. GOVERN remains entirely human — the anesthesiologist is always the kill switch.

The pattern across the literature: AI is beginning to handle Layers 1 and 2 in restricted domains. Layer 3 (DECIDE) is partially addressed in closed-loop systems. Layers 4, 5, and 6 are overwhelmingly human. The expert CRNA carries the whole stack; current AI tools carry the beginning of it, in the conditions where the beginning is easiest.

## The Failure Mode

The Intelligence Stack fails when any layer is overwhelmed and the overload is not detected by the layers above it.

Catchpole et al. (2025), studying anesthesia medication errors at Johns Hopkins and MUSC using systems engineering methods, found that most errors were not knowledge failures — they were workflow failures that degraded SENSE and ORCHESTRATE simultaneously [PMID: 40622243]. The clinician could not see what they needed to see (SENSE failure) and could not perform the action safely in the physical environment (ORCHESTRATE failure). The decision was sound. The execution environment was not.

Frere et al. (2017), measuring situational awareness in medical training tools using Endsley's model, found that Level 1 SA (SENSE) was assessed far more frequently in clinical education than Level 2 (INTERPRET) or Level 3 (DECIDE) [PMID: 29786019]. The education system trains the layer most amenable to measurement. The layers that predict expert performance — context-dependent interpretation and accurate projection — receive a fraction of the training attention.

The failure mode that receives the least institutional attention is LEARN. Anesthesia practice provides constant outcome data — did the patient respond as predicted? — but the individual clinician has no systematic mechanism to close the loop. What gets learned is haphazard: dramatic events teach, routine cases slide by. The architecture has a LEARN layer; in most clinical practice it runs in low-fidelity mode because no infrastructure supports high-fidelity learning from routine events.

The second underattended failure mode is GOVERN. In an expert clinician's stack, GOVERN operates as non-negotiable commitments — interventions that require a second check, drugs that need verbal confirmation, situations that mandate calling for help. When GOVERN degrades under pressure (cognitive overload, fatigue, time constraint), the clinician takes shortcuts that a healthy GOVERN layer would refuse. This is the layer that fails last and causes the most harm when it fails. It is also the layer most invisible to observers from outside the clinician's own cognition.

## The Test

A minimum viable experiment:

Identify 20 CRNAs across experience levels. Use a validated anesthesia simulator with ten critical events embedded. Measure: time-to-signal-recognition (SENSE), accuracy of initial interpretation (INTERPRET), decision latency and option quality (DECIDE), execution error rate (ORCHESTRATE), post-hoc review accuracy (LEARN), and rate of GOVERN violations — defined as known safety-check shortcuts taken under scenario pressure.

The first hypothesis: experienced clinicians will show faster SENSE, more accurate INTERPRET, better-calibrated DECIDE, and lower GOVERN violation rates. ORCHESTRATE performance will be roughly equivalent across experience levels (motor skills plateau relatively early). LEARN accuracy will be *lower* in experienced clinicians than expected, because expertise compresses conscious reflection — the expert pattern-matches rather than explicitly reviewing.

The second hypothesis: fatigue will degrade GOVERN before it degrades SENSE. The clinician will detect the signal and still take the shortcut. This is the most dangerous failure pattern and the hardest to detect from outside the clinician's own cognition. HRV capture during the simulation provides a physiological correlate of GOVERN layer integrity — declining autonomic flexibility predicts increased shortcut rate.

Duration: the scenario suite runs in 90 minutes. Instrumentation: a simulator plus wrist-based HRV capture. This is a 14-day study with a two-site design. Failure criterion: no significant correlation between HRV-indexed autonomic state and GOVERN violation rate.

## The Connection

The Intelligence Stack gives SRL a structural vocabulary for every intervention in the [[vault]].

[[neurominute]] targets INTERPRET — the layer most likely to bottleneck under cognitive load before SENSE degrades. A sixty-second regulation break does not make the clinician perceive more accurately; it restores the context-building capacity that allows signals to be correctly understood.

[[gap-moment-training]] targets GOVERN — creating a non-negotiable pause at the moment of state transition that holds even when the rest of the stack is under pressure. This is GOVERN training in its most direct form.

[[anterocept]] targets SENSE — specifically the interoceptive channels that run parallel to the external monitoring stack. A clinician who cannot sense their own physiological state is operating SENSE with a channel missing.

The [[pausality]] app delivers LEARN feedback that clinical practice does not otherwise provide: a structured retrospective loop on autonomic state across a shift, creating the high-fidelity LEARN layer that routine anesthesia practice cannot generate on its own.

What SRL is building is not a collection of wellness tools. It is a complete Intelligence Stack upgrade for the clinician — each module targeting a specific layer, together covering the full architecture that every CRNA is already running.

The stack was always there. Now it has a name.

---

*In the third hour of a complex case, when the blood pressure drifts before the alarm sounds, the CRNA who notices is not more attentive — they are running a better stack.*

---

## References (Verified)

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Schulz CM, Endsley MR, Kochs EF, Gelb AW, Wagner KJ | 2013 | Situation awareness in anesthesia: concept and research | Anesthesiology | 23291626 | 10.1097/ALN.0b013e318280a40f | YES |
| 2 | Pinsky MR, Bedoya A, Bihorac A, Celi L, Churpek M, et al. | 2024 | Use of artificial intelligence in critical care: opportunities and obstacles | Critical Care | 38589940 | 10.1186/s13054-024-04860-z | YES |
| 3 | Hunn CA, Bruns H, Sahli S, et al. | 2025 | Evaluation of visual patient predictive for enhancing level 3 situation awareness: protocol for a multicentre randomised computer-based simulation and diagnostic accuracy study | BMJ Open | 41469047 | 10.1136/bmjopen-2025-109171 | YES |
| 4 | Singh M, Nath G | 2022 | Artificial intelligence and anesthesia: A narrative review | Saudi Journal of Anaesthesia | 35261595 | 10.4103/sja.sja_669_21 | YES |
| 5 | Wingert T, Williams T, Syed B, et al. | 2026 | Prospective validation and real-time implementation of an automated machine learning postoperative mortality prediction model | British Journal of Anaesthesia | 41549026 | 10.1016/j.bja.2025.11.042 | YES |
| 6 | Catchpole KR, Neyens DM, Abernathy JH, Biro J | 2025 | Rethinking Anesthesia Medication "Errors": The OR-SMART Patient Safety Learning Laboratory | Journal of Patient Safety | 40622243 | 10.1097/PTS.0000000000001384 | YES |
| 7 | Frere M, Tepper J, Fischer M, Kennedy K, Kropmans T | 2017 | Measuring situation awareness in medical education objective structured clinical examination guides | Education for Health | 29786019 | 10.4103/efh.EfH_306_16 | YES |
