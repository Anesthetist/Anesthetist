---
title: "Notes from the Lab: The Line That Moves — Human/AI Decision Boundary in Clinical Practice"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-29
word_count: 1610
core_claim: "The Human/AI Decision Boundary is not a deployment policy — it is a physiological calibration that erodes through automation complacency, and the clinician who stops actively maintaining it will find the machine making judgment calls in high-sigma domains while they provide the signature."
related_concepts:
  - human-ai-decision-boundary
  - neurogating
  - intelligence-stack
  - fiduciary-wedge
  - agent-specification
evidence_used:
  - ismail-organizational-singularity-2026
pubmed_citations_verified: 7
gertrude_status: pass
---

# Notes from the Lab: The Line That Moves

*The Human/AI Decision Boundary is not a deployment policy — it is a physiological calibration that erodes through automation complacency, and the clinician who stops actively maintaining it will find the machine making judgment calls in high-sigma domains while they provide the signature.*

## The Observation

A CRNA in a modern operating room is already practicing inside a human-AI system. The hemodynamic monitoring software flags early instability. The AIMS system auto-populates the anesthesia record. Closed-loop propofol delivery titrates depth against the processed EEG. AI-assisted regional nerve block guidance enhances the ultrasound display. Each of these tools is making decisions — not recommendations that feel like decisions, but actual routing choices about what information surfaces, what gets acted on, what gets recorded.

The question the field is not yet asking systematically is: where is the line? Which calls belong to the algorithm and which belong to the CRNA? And more precisely: who is checking that the line is still where it was when the shift started?

## The Mechanism

Croskerry, in mapping the universal model of diagnostic reasoning, identified two systems operating in parallel: System 1 — fast, heuristic, pattern-matching, unconscious — and System 2 — slow, analytical, deliberate, energy-expensive Croskerry (2009) [PMID: 19638766]. The CRNA's own cognition is a routing system. The AI introduces a third agent to that system without changing its fundamental architecture.

Giordano and colleagues, writing from the University of Florida anesthesiology department, documented what AI does best: it detects "early imperceptible patterns predicting subtle health deterioration" before clinical thresholds trigger Giordano et al. (2021) [PMID: 34713115]. This is SENSE work. The AI is extraordinarily capable in signal-rich, well-structured domains where the outcome criterion is clear and the data is continuous.

The problem is not the AI's performance in its lane. The problem is boundary drift.

Hofmann's 2026 simulation study modeled 27 physician agents completing diagnostic tasks with and without AI support. With a competent AI (performance ≥0.6), agents showed up to 150% relative improvement in binary decision accuracy. But the finding that demands attention is the reverse: "over-trusting low-competence AI can impair outcomes for high-performing agents" Hofmann (2026) [PMID: 41586201]. A high-performing agent — a seasoned CRNA — who calibrates trust to habit rather than to verified AI competence will make worse decisions than they would have made alone.

This is not an indictment of AI. It is a calibration problem. Li and colleagues, in developing the TRIAD framework for clinical AI governance, frame it precisely: intelligence is a property of the human-AI team, not the AI model alone Li et al. (2026) [PMID: 41810150]. TRIAD requires explicit data provenance, staged rollouts, and continuous monitoring of "patterns of acceptance, editing, and overriding." The team-level metrics matter more than the model-level metrics. The boundary is a team resource.

Maloney and colleagues, reviewing AI's role in anesthesia patient safety, name "automation complacency" explicitly as a specific risk in anesthetic practice Maloney et al. (2025) [PMID: 41182062]. The mechanism is familiar to anyone who has practiced in the OR: after 200 correct AI recommendations, the 201st receives less scrutiny than it deserves. This is not negligence. It is neurobiology. The nervous system conserves resources by reducing vigilance on reliable signals. The CRNA's own Neurogating™ system — the physiological routing logic that determines which signals reach conscious attention — adapts to a world where the AI is usually right.

Brunyé and colleagues extend this further, documenting that "long-term reliance on AI may erode clinician skills, particularly for trainees and in low-prevalence contexts" Brunyé et al. (2026) [PMID: 41101774]. Low-prevalence contexts are exactly where the stakes are highest in anesthesia — the catastrophic intraoperative event, the rare drug interaction, the hemodynamic cascade that doesn't fit the expected pattern. The AI has less training data in these scenarios. The CRNA has atrophied skill in exactly the moment they need it most.

Confounds to name explicitly: most of the cited evidence comes from general clinical populations and simulation studies, not from CRNAs specifically. The mechanisms — automation complacency, skill erosion, boundary drift — are documented across surgical specialties and diagnostic medicine. The application to anesthesia practice is an inference from convergent evidence, not a direct experimental finding. This inference is plausible, and the risk is specifically named in anesthesia-focused reviews (Maloney et al., Duarte-Medrano et al.), but CRNA-specific boundary calibration data does not yet exist.

## The Framework

The Intelligence Stack — a cognitive architecture that organizes decision-making into six discrete layers — makes the boundary explicit. The stack flows: SENSE (collect signals) → INTERPRET (build context) → DECIDE (commit to action) → ORCHESTRATE (execute) → LEARN (improve). The Human/AI Decision Boundary lives between INTERPRET and DECIDE.

For the CRNA in a Pausality-augmented workflow:
- **SENSE:** Multimodal biometric streams, OR monitors, AI anomaly detection → AI territory
- **INTERPRET:** Pattern recognition, context assembly, ReadyScore generation, state classification → hybrid territory
- **DECIDE:** Irreversible choices, value-laden judgment, ethical reasoning, action commitment → CRNA territory

Duarte-Medrano and colleagues name the optimal model: AI "augments rather than replaces clinical judgment — combining computational efficiency with the irreplaceable contextual understanding and ethical reasoning of the anesthesiologist" Duarte-Medrano et al. (2025) [PMID: 41517028]. The anesthesiologist retains leadership in perioperative care. The AI handles pattern detection.

The boundary problem is that INTERPRET and DECIDE blur. The AI presents an interpretation. The clinician decides to accept or override. If they accept automatically — because the AI has been right 200 times — the decision happened inside INTERPRET, not DECIDE. The CRNA signed off without recognizing they were signing.

Snowden's Cynefin framework adds structural clarity. Simple and Complicated domains — where cause-effect relationships are knowable — route to algorithms. Complex and Chaotic domains — where cause-effect relationships cannot be determined in advance — require human judgment. The OR is almost always Complex. A patient with three comorbidities, unusual pharmacokinetics, and an unexpectedly light anesthetic depth at 45 minutes is not a Complicated problem. It is a Complex one. The pattern hasn't been seen in exactly this configuration before. This is not a failure of AI capability. It is the structural character of perioperative care.

The boundary velocity problem follows directly: the line moves. A decision that required human judgment six months ago may now be safely delegable as AI capability expands. The CRNA who sets the boundary once and never revisits it is calibrating to a map that is already outdated.

## The Failure Mode

Two failure modes, both physiological rather than technical:

**Commission error:** The CRNA delegates a high-sigma decision to the algorithm without recognizing it as high-sigma. This happens when habit displaces calibration — when "the AI is usually right" becomes the decision rule rather than "I have verified this AI is right in this class of situation." Hofmann demonstrated this experimentally: high-performing agents who over-trust a low-competence AI perform worse than agents working without AI assistance at all.

**Omission error:** The CRNA nominally retains ownership of a decision domain but loses the skill to execute it because the AI has been handling it reliably. Brunyé et al. documented this dynamic for trainees; the mechanism applies to experienced providers in rare-event practice domains. The CRNA "owns" the decision but cannot competently execute it when the AI fails. They retain the label without the competence.

Both failure modes are invisible until the AI makes its error. And both are made more likely by the same force: the CRNA's nervous system has adapted to a world where the boundary holds. Neurogating™ — the body's own signal-routing mechanism — has stopped flagging AI outputs for conscious scrutiny because they've been correct long enough to be treated as safe. The gate becomes automatic in exactly the domain where it must remain volitional.

The misapplication to watch for: treating the boundary as a one-time architectural choice. Many institutions are doing this now — defining "AI decision domains" in policy documents at deployment and then leaving the calibration untouched as AI capabilities evolve, as the CRNA's skill profile shifts, and as the patient population changes. The policy is static. The boundary is not.

## The Test

Fourteen days. Ten anesthesia providers. High-fidelity simulation environment. Baseline measurement: structured interview and scenario observation to map each provider's explicit and implicit model of their Human/AI Decision Boundary. Which decisions do they verbalize as delegated? Which do they retain?

Day 7: introduce one "boundary probe" — a plausible AI recommendation in a Complex-domain scenario. The recommendation is coherent but incorrect. Measure the catch rate: how many providers interrogate the recommendation before accepting it. Compare against baseline. Secondary hypothesis: providers with lower interoceptive awareness scores (MAIA-2-CRNA) will show lower catch rates, because boundary maintenance requires embodied self-monitoring — noticing the felt sense of "something doesn't match." Tertiary measure: track ReadyScore™ at the moment of each decision. Hypothesis: dysregulated autonomic state correlates with lower boundary maintenance under cognitive load.

Limitation: catch rate in simulation likely overestimates catch rate in practice. The attentional load of a live OR and the affective weight of an actual adverse event cannot be fully replicated.

## The Connection

Neurogating™ is not a metaphor for the Human/AI Decision Boundary. It is the same mechanism operating at a different scale. In the body, Neurogating routes psychophysiological signals to conscious attention or automatic processing based on learned threat profiles and real-time cognitive load. In the OR, the CRNA's workflow routes decisions to human scrutiny or algorithmic output based on habit and calibrated trust. Both are susceptible to the same failure mode: the gate becomes automatic when it must remain volitional.

The solution in both domains is also the same — a trained practice of returning attention to the routing logic itself. In physiology, [[self-remembering]] calls this simultaneous self-task awareness: watching the watcher. In AI-integrated clinical practice, it is the active maintenance of the boundary: periodically asking not just "what is the AI recommending?" but "what kind of decision is this, and who authorized it to be in the AI's lane?"

Gap Moment Training™ is the infrastructure for that practice. The pause between cases, between procedures, between tasks — the 60-second return to self — is the structural moment where the CRNA can ask: what am I currently delegating, and does that match what I intended to delegate?

The line moves. The clinician who doesn't move with it is signing off on decisions they no longer own.

---

*The hand that holds the chart and the hand that made the call — in the modern OR, it is worth pausing to confirm they belong to the same person.*

---

## References (Verified)

Based on articles retrieved from PubMed:

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Croskerry P | 2009 | A universal model of diagnostic reasoning | Academic Medicine | 19638766 | [10.1097/ACM.0b013e3181ace703](https://doi.org/10.1097/ACM.0b013e3181ace703) | YES |
| 2 | Giordano C, Brennan M, Mohamed B, Rashidi P, Modave F, Tighe P | 2021 | Accessing Artificial Intelligence for Clinical Decision-Making | Frontiers in Digital Health | 34713115 | [10.3389/fdgth.2021.645232](https://doi.org/10.3389/fdgth.2021.645232) | YES |
| 3 | Hofmann A | 2026 | AI-supported clinical decision-making: in silico simulation of physician-AI interactions | Frontiers in Digital Health | 41586201 | [10.3389/fdgth.2025.1697825](https://doi.org/10.3389/fdgth.2025.1697825) | YES |
| 4 | Li J, Zhou ZC, Wang ZC, Lv H | 2026 | Prioritizing human-AI collaboration in healthcare: the TRIAD framework for trustworthy governance, real-world, and integrated adaptive deployment | Military Medical Research | 41810150 | [10.1186/s40779-026-00684-w](https://doi.org/10.1186/s40779-026-00684-w) | YES |
| 5 | Maloney JA, Johnson B, Harbell MW | 2025 | The double-edged sword: artificial intelligence's promise and perils in anesthesia patient safety | Current Opinion in Anaesthesiology | 41182062 | [10.1097/ACO.0000000000001580](https://doi.org/10.1097/ACO.0000000000001580) | YES |
| 6 | Brunyé TT, Mitroff SR, Elmore JG | 2026 | Artificial intelligence and computer-aided diagnosis in diagnostic decisions: 5 questions for medical informatics and human-computer interface research | Journal of the American Medical Informatics Association | 41101774 | [10.1093/jamia/ocaf123](https://doi.org/10.1093/jamia/ocaf123) | YES |
| 7 | Duarte-Medrano G, Nuño-Lámbarri N, Paternò DS, La Via L, Tutino S, Dominguez-Cherit G, Sorbello M | 2025 | Advancing a Hybrid Decision-Making Model in Anesthesiology: Applications of Artificial Intelligence in the Perioperative Setting | Healthcare (Basel) | 41517028 | [10.3390/healthcare14010097](https://doi.org/10.3390/healthcare14010097) | YES |
