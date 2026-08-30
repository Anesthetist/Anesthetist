---
title: "Notes from the Lab: The Correction Is the Training — Recursive Workflow Improvement and the Biology of Clinical Expertise"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-30
word_count: 1461
core_claim: "Clinical expertise is not experience — it is corrected experience: each performance cycle must generate structured information that modifies the next cycle, and without this recursive loop, a decade of practice produces habit, not mastery."
related_concepts:
  - recursive-workflow-improvement
  - intelligence-stack
  - intelligence-density
  - somnistics-agentic-lab
  - deliberate-practice
evidence_used:
  - urn:srl:evidence:ismail-organizational-singularity-2026
pubmed_citations_verified: 6
gertrude_status: pass
---

# Notes from the Lab: The Correction Is the Training — Recursive Workflow Improvement and the Biology of Clinical Expertise

*Clinical expertise is not experience — it is corrected experience: each performance cycle must generate structured information that modifies the next cycle, and without this recursive loop, a decade of practice produces habit, not mastery.*

---

## The Observation

An anesthesia provider who has run 8,000 cases runs them faster than one with 200. The muscle memory is there. Drug names come without effort. The induction checklist runs silently in the background. And yet — watch the eyes. The gaze pattern during a difficult airway has not changed since year three. The interoceptive read before a hemodynamic crisis hasn't sharpened. The same hesitation appears in the same equipment-patient configuration, case after case. Volume accumulated. Mastery didn't.

This is not a failure of work ethic. It is a structural failure. Practice without feedback is practice without correction. And correction is the actual training.

The body that has run 8,000 uncorrected cases has not built expertise — it has deepened grooves. Habit is self-confirming. The recursive loop is what converts experience into compounding skill.

---

## The Mechanism

Ericsson — the architect of deliberate practice theory — and colleagues made this precise in 2022. Clark, Harwell, Ericsson, and Boot studied low-performing participants in a complex manual control task. They designed a 90-minute intervention embedding the structural elements of deliberate practice: video demonstrations targeting specific behaviors, continuous auditory feedback, and clear correction of patterns correlated with poor performance. After just 4 hours of total task exposure, the low-performing participants who received the structured intervention significantly outperformed those who simply practiced more without feedback. Critically, the behavioral improvements were durable — they persisted after all feedback was removed. Clark et al. (2022) [PMID: 35763961] showed that the correction-and-modify loop — signal → evaluate → adjust → repeat — is the operative mechanism, not time on task.

McLeod, Chuan, and McKendrick (2024) brought this directly to anesthesia. Writing in the British Journal of Anaesthesia, they argued that clinical competency — as mapped by the Dreyfus and Dreyfus model of skill acquisition — is effectively unachievable through current training approaches. The reason is structural: existing programs rely on volume (case counts, hours, procedures) rather than on quantitative measurement of the specific cognitive and psychomotor components that expertise actually requires: perception, attention, visuospatial function, kinesthetics. McLeod et al. (2024) [PMID: 38960830] proposed what Ericsson's framework demands — measure the specific constituents of expert performance, deliver precise feedback on each, and iterate.

The mechanism is neurobiological. Each corrective signal — "your gaze moved too early," "your autonomic read of patient distress was two seconds behind the SpO2 drop" — activates the same synaptic modification pathways as motor learning: long-term potentiation at circuits that performed correctly, long-term depression at circuits that erred. The correction is the training. Without a signal specifying what to correct, the nervous system maintains the existing circuit configuration. Experience alone confirms existing patterns. Deliberate feedback modifies them.

Daza-Beltrán, Fajardo Escolar, Caro, and Suárez (2026) demonstrated this in anesthesia residents. Their multimodal Situation Awareness Assessment for Anesthesia Residents (SAAAR) system combined a 16-item behavioral marker scale with structured eye-tracking debriefing. After implementing the feedback system in simulation-based training, they found significant improvements across all situation awareness domains (Wilcoxon signed-rank test), p < 0.05. Daza-Beltrán et al. (2026) [PMID: 41482731] showed that signal specificity mattered — broad evaluations produced less behavioral change than targeted behavioral marking tied to observable actions.

Jaffrelot, Boet, and colleagues (2024) ran a randomized controlled trial in 61 medical students testing whether peer-led debriefing could substitute for instructor-led debriefing in simulated crisis scenarios. Non-technical skill scores (Ottawa Global Rating Scale) improved by 15–18 points across all groups, with no significant difference between modalities (p = 0.147). Skills were retained at the 2-month follow-up test. Crucially, the peer debriefer also improved — running the recursive feedback loop from the evaluator position produces its own learning. Jaffrelot et al. (2024) [PMID: 38556779] found that the specific person administering the correction mattered less than the presence of structured, specific, evaluative feedback itself.

Lee, O'Neill, and colleagues (2026) operationalized recursion at the governance level. Their emergency department airway quality improvement program used four sequential PDSA (Plan-Do-Study-Act) cycles — each cycle producing data that modified the next intervention. They maintained first-pass intubation success above 90% and complication rates below 15% across 156 intubations over 18 months, despite staff turnover and progressive intervention complexity. Lee et al. (2026) [PMID: 41856552] showed that the recursive cycle design was the mechanism of sustained performance — not any single checklist or protocol, but the loop that evaluated each cycle and adjusted the next.

Kelly, Duignan, Booth, Gangadharan, and Clifford (2025) extended this to AI augmentation. Writing in Pediatric Radiology, they showed that AI can identify diagnostic errors in real time and create personalized feedback loops aligned with deliberate practice principles — curating learning experiences based on individual error patterns rather than generic exposure. Kelly et al. (2025) [PMID: 41258969] argued that AI's value is not in replacing expert judgment but in shortening the correction loop: detect the error, feed it back immediately, adjust the next learning experience.

One confound worth stating explicitly: in all six studies above, the feedback signal must be specific to the behavior targeted. Generic performance scores produce no meaningful circuit modification. The loop requires precision: which behavior, at which moment, diverged from the target pattern, by how much. Vague feedback — "good job" or "needs improvement" — is not feedback in the Ericsson sense. It is noise.

---

## The Protocol

SRL's bot system implements recursive workflow improvement as explicit infrastructure:

1. **Bot retrospectives** (`retrospective.md`) — post-run self-reflection: what succeeded, what failed, what needs structural adjustment in the next run
2. **Pattern libraries** (`patterns.md`) — accumulated heuristics updated each cycle; the system learns from its own performance history
3. **Learning logs** (`learning-log.md`) — tracking which search strategies worked, which citations were unverifiable, which quality gates required the most revision
4. **Cross-bot feedback** — vault-writer evaluates knowledge-miner output quality; the extraction-coordinator tracks system-level trends; Randy's clinical interpretations feed back to every bot in the next run
5. **Vigil as LEARN layer** — orchestrating improvements across the entire bot system, translating Randy's decisions into protocol updates

Each execution cycle produces outputs AND modifications to the next cycle's execution. The improvement is not accidental. It is structural.

For a CRNA implementing personal recursive improvement:
1. After each case, name one specific moment where your read was late or your response suboptimal
2. State the correction explicitly: what would the target behavior have been?
3. Track recurrence across 30 cases
4. In your next Gap Moment, mentally rehearse the corrected pattern under realistic conditions
5. Use RMSSD recovery slope after cases containing that pattern as your proxy for autonomic cost — faster recovery suggests the correction is taking hold at the autonomic level, not just the cognitive level

---

## The Failure Mode

Goodhart's Law at machine speed: when a measure becomes a target, it ceases to be a good measure. Recursive systems optimizing toward the wrong objective get dramatically better at the wrong thing.

In clinical training: if the feedback signal is "pass the checklist," the skill acquired is checklist completion, not clinical judgment. If the feedback signal is "maintain SpO2 above 95%," the skill is number management, not patient monitoring. Volume-based training uses case count as its implicit feedback signal, and what it reliably produces is case completion.

The recursive system breaks when the objective function is misspecified. Every improvement cycle must be tested against an independent evaluation metric — something the training doesn't directly optimize — as the validity check. For SRL bots: versioned outputs, A/B testing before deployment, automatic rollback if performance on the independent eval suite degrades. For CRNAs: a separate interoceptive accuracy measure (MAIA-2-CRNA adapted) tracked independently of the clinical outcome metric being refined.

A second failure mode: recursion without range. A system that only refines what it already does will optimize toward a local maximum. Some portion of each cycle must be exploratory — testing new configurations, deliberately introducing novel cases, exposing the system to its failure edges. Habit is what you get when recursion runs without exploration.

---

## The Test

Fourteen CRNAs. Seven assigned to a structured post-case reflection protocol (one specific behavior named per case, target pattern defined, tracked across 30 cases). Seven continuing standard practice. Duration: 60 days.

Primary measurement: interoceptive accuracy score (MAIA-2-CRNA adapted measure) at baseline and day 60. Secondary: RMSSD recovery slope after high-complexity cases. Tertiary: time-to-correct-intervention on standardized video review cases at day 60.

Failure signal: if the reflection protocol produces no MAIA-2 improvement but does produce RMSSD improvement, the interpretation is that motor-level habits are modifying but cognitive pattern recognition is not — the reflection prompts are too broad. Narrow the specificity of the named behavior and rerun.

This is testable at small scale with a wearable, a structured reflection form, and two video review sessions. It does not require a clinical trial.

---

## The Connection

Recursive workflow improvement is the operating mechanism behind every SRL concept that compounds over time: [[cardiac-anchored-breathing]] compounding into stronger autonomic home base, [[gap-moment-training]] compounding into faster state transition speed, [[interoceptive-literacy]] compounding into earlier clinical signal detection. The recursion is what converts technique into biology. Without the feedback loop, each practice stays isolated. With it, the system builds infrastructure.

This connects directly to [[intelligence-density]]: an organization — or a clinician — that has embedded recursive improvement into its daily workflows produces more high-value cognitive output per hour than one running on experience alone. The correction is the competitive moat.

---

*Feel the difference between practicing and practicing correctly: one is the hands moving through familiar territory, the other is the nervous system rebuilding its own map.*

---

## References (Verified)

Based on articles retrieved from PubMed, all citations below were verified via PMID metadata lookup. DOIs confirmed.

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Clark B, Harwell K, Ericsson KA, Boot WR | 2022 | Applying aspects of deliberate practice to help low performers improve manual control in a complex task | Acta Psychologica | 35763961 | [10.1016/j.actpsy.2022.103656](https://doi.org/10.1016/j.actpsy.2022.103656) | YES |
| 2 | McLeod G, Chuan A, McKendrick M | 2024 | Attaining expertise in regional anaesthesia training using a multifactorial approach incorporating deliberate practice | British Journal of Anaesthesia | 38960830 | [10.1016/j.bja.2024.06.003](https://doi.org/10.1016/j.bja.2024.06.003) | YES |
| 3 | Jaffrelot M, Boet S, Floch Y, et al. | 2024 | Learning with our peers: peer-led versus instructor-led debriefing for simulated crises, a randomized controlled trial | Korean Journal of Anesthesiology | 38556779 | [10.4097/kja.23317](https://doi.org/10.4097/kja.23317) | YES |
| 4 | Daza-Beltrán C, Fajardo Escolar AP, Caro M, Suárez DR | 2026 | Situation Awareness Assessment for Anesthesia Residents (SAAAR): Development and Preliminary Evaluation of a Multimodal System | Human Factors | 41482731 | [10.1177/00187208251413484](https://doi.org/10.1177/00187208251413484) | YES |
| 5 | Lee J, O'Neill L, Mulchrone E, et al. | 2026 | The infusion after the bolus: a quality improvement programme to support emergency department airway governance in Ireland | Emergency Medicine Journal | 41856552 | [10.1136/emermed-2025-215350](https://doi.org/10.1136/emermed-2025-215350) | YES |
| 6 | Kelly BS, Duignan S, Booth CC, Gangadharan S, Clifford SM | 2025 | From volume to value: leveraging artificial intelligence and deliberate practice to foster precision learning in radiology | Pediatric Radiology | 41258969 | [10.1007/s00247-025-06470-5](https://doi.org/10.1007/s00247-025-06470-5) | YES |
