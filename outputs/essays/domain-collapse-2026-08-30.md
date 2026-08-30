---
title: "Notes from the Lab: After Collapse — What Remains When Anesthesia Becomes Compute-Bound"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-30
word_count: 1590
core_claim: "Domain Collapse in anesthesia is already underway — autonomous systems handle the repetitive pattern-detection layer that once required expert vigilance, concentrating clinical value into three capacities no algorithm provides: interoceptive accuracy, out-of-loop recovery, and the ability to recognize when the machine is wrong."
related_concepts:
  - domain-collapse
  - intelligence-stack
  - intelligence-density
evidence_used: []
pubmed_citations_verified: 6
gertrude_status: pass
---

# Notes from the Lab: After Collapse — What Remains When Anesthesia Becomes Compute-Bound

*Domain Collapse in anesthesia is already underway — autonomous systems handle the repetitive pattern-detection layer that once required expert vigilance, concentrating clinical value into three capacities no algorithm provides: interoceptive accuracy, out-of-loop recovery, and the ability to recognize when the machine is wrong.*

## The Observation

In a contemporary operating room, a pharmacological robot manages propofol infusion, closing the loop between EEG depth-of-anesthesia monitoring and drug delivery. A hemodynamic algorithm watches for the pressure signature of impending hypotension — not on the monitor, where it would already be a problem, but in the arterial waveform's morphology six minutes before the number changes. A decision support overlay flags the patient's 83rd-percentile hemorrhage risk before the first incision.

The CRNA beside all of this is not idle. But they are different. They are watching machines that are watching patients. The cognitive labor that occupied the first two decades of their practice — the vigilant, full-attention monitoring of vital sign trends — is being absorbed into compute. What does this do to the clinician? What do they do with their hands, their attention, their nervous system, when the algorithm is handling what used to be the most demanding part of the job?

This is the phenomenology of Domain Collapse in clinical practice — not a future event, but a present condition.

## The Mechanism

Diamandis and Wissner-Gross identified the pattern [[domain-collapse]]: when intelligence infrastructure reaches threshold density in any domain, that domain doesn't improve incrementally. It collapses from craft to utility, the way electricity collapsed candlemaking. The craft isn't gone — candles still exist. But the economic center of gravity shifts, and with it, the question of where skill adds value.

In anesthesia, Zaouter et al. (2020) described three generations of autonomous systems already deployed: pharmacological robots using closed-loop drug titration, mechanical robots executing high-dexterity procedures with accuracy exceeding human hands, and cognitive robots — decision support systems that recognize critical clinical situations and propose (or sometimes execute) therapeutic options [PMID: 32287120]. By 2020, pharmacological robots were demonstrating they could "control hemodynamic parameters proficiently, outperforming manual control in the operating room." The collapse of the hemodynamic titration domain — from expert craft to compute — was already observable five years ago.

Giordano et al. (2021), writing from the Department of Anesthesiology at the University of Florida, described the next layer: AI detecting "early imperceptible patterns predicting subtle health deterioration" invisible to traditional vital sign monitoring [PMID: 34713115]. The pattern-detection layer, once the exclusive domain of trained clinical intuition — what CRNA instructors call "reading the room" — is being absorbed by compute. Giordano's team noted that physicians will need to "change their educational infrastructure to facilitate understanding AI platforms, modeling, and limitations." This is the educational system recognizing collapse and not yet knowing how to respond to it.

But Domain Collapse has a failure mode the literature is only beginning to name. Kücking et al. (2025) demonstrated it in 223 physicians and nurses making 1,338 diagnostic decisions under AI assistance [PMID: 41391283]. When the AI recommendation was correct, clinicians were ten times more likely to reach the right answer (OR = 10.0, p < 0.001). When the AI recommendation was wrong, clinician accuracy dropped proportionally. The AI's presence, regardless of accuracy, reorganized the cognitive field around the human decision. Clinicians didn't override the wrong answer — they absorbed it. Kücking called this "overreliance on the system" — a substantial safety risk that emerges not from AI failure but from human adjustment to AI presence.

Brunyé et al. (2026), reviewing the human-computer interface research, named the downstream consequence: skill decay [PMID: 41101774]. "Long-term reliance on AI may erode clinician skills, particularly for trainees and in low-prevalence contexts." The clinician who has managed hemodynamics with algorithmic assistance for five years — facing a system failure in a hemorrhagic emergency — is a different clinician than one who managed it manually. The automation created competence on the assisted workflow and degraded competence on the unassisted one. This is not a technology failure. It is the predictable response of a reasoning brain that incorporates a highly confident signal source into its priors.

The confound here is important to state: in Kücking's study, multiple variables changed simultaneously — AI presence, AI confidence, task complexity, and participant baseline skill all varied. What the study isolates is the directional relationship between AI confidence and human override capacity. High-confidence wrong AI > no AI, in terms of harm. That is the finding.

Alowais et al. (2023), in a comprehensive review, confirmed the net pattern: "AI tools can leverage large datasets and identify patterns to surpass human performance in several healthcare aspects" — while simultaneously noting that "challenges related to data privacy, bias, and the need for human expertise must be addressed for the responsible and effective implementation of AI in healthcare" [PMID: 37740191]. The "need for human expertise" here is not a diplomatic hedge. It is the fiduciary architecture that slows collapse: liability does not transfer to the algorithm. It stays with the clinician who signed the chart.

## The Framework: Three Irreducibles After Collapse

Domain Collapse in clinical practice does not flatten all clinical skill into a single compute-managed layer. It differentiates. It makes explicit what was previously bundled together — and what gets separated is exactly what a training system must now target.

**1. Interoceptive accuracy under algorithmic conditions.**
When an algorithm manages the monitoring layer, the CRNA's attention reorganizes around algorithmic output rather than direct physiological signal. The somatic signaling that operates below conscious awareness — the gut recognition that something is wrong before the numbers say so — competes with a highly confident algorithmic signal. Kücking showed that confident AI signals reshape human decisions even when wrong. Maintaining interoceptive accuracy in the presence of high-confidence algorithmic output requires active training, not passive exposure. This is the [[anterocept]] problem under technological conditions: the body's anticipatory signal must be preserved against a system that is designed to preempt it.

**2. Out-of-loop recovery capacity.**
Every autonomous system fails. The hemodynamic algorithm's model is trained on populations that may not include this patient. The pharmacological robot's sensor is occluded. The decision support system encounters a variable combination outside its training distribution. When collapse is incomplete — when the compute layer fails — a human must recover. The question is whether that human has been degraded by the system they depended on. Brunyé's skill decay finding is the evidence that the answer is often yes. Preserving out-of-loop recovery capacity requires deliberate maintenance of the autonomous skill — periodic manual practice in unassisted conditions — specifically to maintain the [[embodied-clinical-intelligence]] that compute would otherwise atrophy.

**3. Error recognition at high AI confidence.**
The most dangerous failure mode is not the algorithm giving wrong answers at random. It is the algorithm giving wrong answers with high confidence. Kücking's finding is not that AI reduces accuracy — it is that confident wrong AI guidance reduces accuracy more than no guidance at all. The clinician's capacity to recognize "the machine is wrong here" depends on a calibrated internal reference — a felt sense of physiological reality that is not downstream of the algorithm's output. Duarte-Medrano et al. (2025) argued for the hybrid model: "AI augments rather than replaces clinical judgment — combining computational efficiency with the irreplaceable contextual understanding and ethical reasoning of the anesthesiologist" [PMID: 41517028]. The "irreplaceable contextual understanding" they name is this: the body's independent read of what is happening, available for comparison against the algorithm's read.

## The Failure Mode

The catastrophic failure mode of Domain Collapse in clinical care is not inadequate algorithms. It is clinicians who cannot function when algorithms fail, because the training and workflow that built their competence assumed algorithmic support that will not always be present.

The fiduciary structure of clinical practice slows this collapse — liability stays with the clinician, not the algorithm — but slowing the collapse is not preventing it. A clinician who signs off on an AI-generated assessment without adequate override capacity has the liability without the competence. The legal system preserves the human decision-making structure long after the cognitive infrastructure underlying that decision has shifted.

Brunyé identified the specific populations at greatest risk: trainees (who may develop competence only on the assisted workflow) and clinicians operating in low-prevalence contexts (where manual skill has long periods of non-use). Both conditions describe anesthesia: trainees increasingly learn alongside AI systems, and many critical manual skills are invoked only in rare emergencies.

## The Test

Fourteen CRNAs. Two clinical sessions each — one AI-assisted (standard institutional protocols with decision support active), one manual (same case complexity with support systems observing but not displaying recommendations). HRV (RMSSD) measured continuously via wearable throughout both sessions. Hypothesis: AI-assisted sessions produce lower mean RMSSD and lower HRV variability, indicating a more passive autonomic profile consistent with reduced active-monitoring engagement. Secondary: post-session debriefing to assess subjective confidence in ability to manage without support.

This is not a clinical trial — it is a 14-day proof of concept. What it would demonstrate, if confirmed, is that the physiological cost of algorithmic assistance is measurable in the clinician's nervous system before it shows up in error rates. The body already knows what skill decay looks like.

## The Connection

Domain Collapse is not a threat to the SRL thesis. It is the argument for it.

If automation absorbs the pattern-detection layer in clinical practice, the irreducibles that remain — interoceptive accuracy, out-of-loop recovery, error recognition at high AI confidence — are precisely what the SRL training stack builds. The [[neurominute]] builds baseline interoceptive calibration. Gap Moment Training™ maintains the capacity to switch from assisted to unassisted states under time pressure. MAIA-2 measurement tracks drift in interoceptive accuracy over time. The autonomic training that looks like resilience maintenance is, in the domain-collapse frame, professional survival.

The collapse doesn't eliminate the clinician. It concentrates their value into the residual that compute cannot touch.

That residual is the body.

---

*Twenty years from now, the algorithm will manage more of the room. The clinician beside it will need to know, in their bones, when it is wrong — and that knowledge will not come from the screen.*

---

## References (Verified)

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Zaouter C, Joosten A, Rinehart J, Struys MMRF, Hemmerling TM | 2020 | Autonomous Systems in Anesthesia: Where Do We Stand in 2020? A Narrative Review | Anesthesia & Analgesia | 32287120 | 10.1213/ANE.0000000000004646 | YES |
| 2 | Giordano C, Brennan M, Mohamed B, et al. | 2021 | Accessing Artificial Intelligence for Clinical Decision-Making | Frontiers in Digital Health | 34713115 | 10.3389/fdgth.2021.645232 | YES |
| 3 | Alowais SA, Alghamdi SS, Alsuhebany N, et al. | 2023 | Revolutionizing healthcare: the role of artificial intelligence in clinical practice | BMC Medical Education | 37740191 | 10.1186/s12909-023-04698-z | YES |
| 4 | Kücking F, Busch DA, Przysucha M, et al. | 2025 | Impact of AI recommendation correctness on diagnostic accuracy in clinical decision-making | International Journal of Medical Informatics | 41391283 | 10.1016/j.ijmedinf.2025.106223 | YES |
| 5 | Duarte-Medrano G, Nuño-Lámbarri N, Paternò DS, et al. | 2025 | Advancing a Hybrid Decision-Making Model in Anesthesiology: Applications of AI in the Perioperative Setting | Healthcare (Basel) | 41517028 | 10.3390/healthcare14010097 | YES |
| 6 | Brunyé TT, Mitroff SR, Elmore JG | 2026 | Artificial intelligence and computer-aided diagnosis in diagnostic decisions: 5 questions for medical informatics and human-computer interface research | Journal of the American Medical Informatics Association | 41101774 | 10.1093/jamia/ocaf123 | YES |
