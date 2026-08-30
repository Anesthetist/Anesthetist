---
title: "Notes from the Lab: The Same Error, Again — What Anesthesia Safety Science Tells Us About Building AI Agents That Actually Learn"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-30
word_count: 1521
core_claim: "AI agents repeat the same classes of errors for the same structural reason that human clinical teams do — corrections reach individual working memory but bypass institutional memory — and the taxonomic-feedback-injection approach that transformed anesthesia safety science can be directly applied to multi-agent coordination systems."
related_concepts:
  - agent-error-log-protocol
  - neural-sovereignty
  - agent-quartet-framework
  - saturday-flight-check-ritual
  - token-efficiency-protocol
  - signal-to-noise-protocol
  - no-one-off-work-rule
evidence_used:
  - lingard-2004-or-communication-failures
  - jeffrey-2021-surgical-trainee-reporting
  - moon-2025-event-reporting-optimization
  - mahmoud-2023-psls-barriers-facilitators
  - mausz-2016-paramedic-deliberate-practice
  - causer-2014-expert-performance-simulation
pubmed_citations_verified: 6
gertrude_status: pass
---

# Notes from the Lab: The Same Error, Again — What Anesthesia Safety Science Tells Us About Building AI Agents That Actually Learn

*AI agents repeat the same classes of errors for the same structural reason that human clinical teams do — corrections reach individual working memory but bypass institutional memory — and the taxonomic-feedback-injection approach that transformed anesthesia safety science can be directly applied to multi-agent coordination systems.*

## The Observation

A scheduled agent completes a task. A formatting error slips through — heading levels wrong, bullet structure inconsistent, word cap violated. The user corrects it. The agent acknowledges. The following Tuesday, the same agent runs the same task. Same error.

This is not a capability failure. When corrected, the agent knows exactly what it did wrong. The correction reaches the agent's working context and is understood. It does not reach next Tuesday's instance of that agent. The two are not the same agent in any meaningful sense — they share a prompt and a model, but not a memory of what went wrong.

This is an institutional memory failure. It is structurally identical to what anesthesia quality improvement research spent three decades studying before it understood how to fix it.

## The Mechanism

Lingard and colleagues observed 48 surgical procedures across 90 hours and documented every communication event among OR team members. Of 421 communication events, 129 — nearly one in three — were failures [PMID: 15465935]. What made the finding remarkable was not the frequency but the taxonomy: failures fell into just four categories regardless of procedure type, team composition, or time of day. Occasion: timing was poor. Content: information was missing or inaccurate. Purpose: issues were unresolved. Audience: key individuals were excluded.

The OR is not producing random chaos. It is producing patterned failures from a small set of recurring structural weaknesses.

Agent systems produce the same kind of pattern. In the SRL multi-agent architecture, error events cluster into six categories: **drift** (scope creep, unauthorized actions), **scoring** (calculation errors, reverse-scoring failures), **routing** (file saved to wrong location, wrong model tier used), **hallucination** (fabricated citations, invented capabilities), **efficiency** (token waste, polling loops), and **integration** (MCP failures, auth errors not handled gracefully). Like Lingard et al.'s four OR failure types, these six categories account for nearly all observed errors — not because agents are incapable of novel failures, but because most failures arise from a small set of structural weaknesses baked into the architecture.

The critical finding from Lingard's team: 36.4% of communication failures produced visible effects on system processes — inefficiency, tension, resource waste, delay, procedural error. The invisible failures, by implication, were accumulating without signal. The same is true of agent errors. A token efficiency error that wastes 3,000 tokens on Tuesday is invisible. It happens again Thursday. The aggregate cost is real; no single instance triggers response.

### The Feedback Loop That Healthcare Had to Learn to Close

Jeffrey and colleagues interviewed 612 core surgical trainees and found that 83.2% had personally witnessed a near-miss event. Only 13.2% had ever filed a safety report [PMID: 34926092]. The barrier was not access — reporting systems existed. The barrier was culture: 87.6% of trainees characterized safety reports as "negative" or "seriously negative." Of those who did report, only 11.1% received any meaningful feedback or follow-up.

This is the closed-loop failure. When errors are filed and disappear — when no preventive rule emerges, no system change is documented, no agent receives the corrected instruction — reporting stops. The system becomes performative. The people who could feed it stop.

Moon and colleagues demonstrated the repair [PMID: 41056330]. After implementing a redesigned patient safety event system at Mayo Clinic — streamlined reporting, centralized analysis, enhanced transparency — overall event reporting rose from approximately 60% to 80%, with disproportionate gains in near-miss and no-harm events. The critical design features were not mandate or incentive. They were architecture: making reports easy to submit, making outcomes visible, making the connection between report and change legible.

Mahmoud and colleagues' systematic review of patient safety learning systems confirmed the pattern [PMID: 37012003]. The top barriers to effectiveness: inadequate organizational support, complex reporting systems, lack of feedback, blame culture. The enablers: simple interfaces, anonymous reporting, tangible improvements, continuous training. These are not psychological findings — they are systems design requirements. The same requirements apply when the reporters are agents and the institution is a prompt template library.

The feedback loop must close. Every logged error must produce either a preventive rule or an explicit acknowledgment that it was below threshold for one. This is the agent error log protocol's "graduation" concept: errors that recur two or more times from the same category and agent graduate to injected preventive rules in the relevant prompt template. The loop closes. The institution learns.

### What Experience Alone Cannot Do

Mausz and colleagues studied paramedics managing airways in simulation, testing whether years of experience predicted performance [PMID: 27653215]. Thirty participants with a mean of 7.2 years of experience showed no correlation between experience and error rate, number of procedural mistakes, or time to achieve ventilation. The finding was consistent across two scenarios (r=0.13 and r=-0.10). Experience without feedback and deliberate practice does not build expertise — it entrenches idiosyncratic patterns.

The implication for agent systems is direct: an agent accumulating hundreds of task completions without a structured error correction mechanism is not becoming more reliable. It is becoming more consistently itself, including its failure modes. The token efficiency error present in run one will be present in run one hundred if no feedback loop intercepts it.

Causer, Barach, and Williams defined deliberate practice in the clinical context as "a structured and reflective activity designed to develop a critical aspect of performance," requiring error detection and correction, repetition, and access to feedback [PMID: 24528394]. An agent error log is the technical substrate for deliberate practice at the system level. The agent does not self-reflect — but the system that maintains its prompt does. When a pattern graduates to a preventive rule, the agent's next instance is a structurally better version. The learning happens in the architecture, not in the agent.

## The Protocol

The Agent Error Log Protocol operates in five steps:

1. **Classification.** Each error is tagged by type (drift, scoring, routing, hallucination, efficiency, integration) in a structured log entry, including root cause and fix applied.
2. **Logging.** Entries append to a persistent vault record — not the agent's active context, which resets per session, but the institutional store that persists across instances.
3. **Graduation.** Errors recurring twice or more in the same category from the same agent are promoted to preventive rules and injected into the relevant prompt template under a "Known Failure Modes" section.
4. **Integration.** The Saturday Flight Check Ritual includes an error pattern digest: top three types by frequency, which agents produced them, which preventive rules were added, whether prior rules reduced recurrence.
5. **Measurement.** Weekly metrics: total errors logged, errors by type, repeat vs. novel, time-to-fix.

The system does not punish agents — they are stateless. It punishes the system for failing to institutionalize a correction.

## The Failure Mode

The agent error log fails in exactly one way: when errors are logged but never graduate to preventive rules. When the log becomes a ledger rather than a learning system. This happens when the classification threshold is too high — only catastrophic failures get logged — or when the graduation threshold is too low, creating noise that gets ignored. Or most commonly: the weekly review doesn't happen, and the log silently fills without ever feeding back.

The Mahmoud review shows that complexity and absence of feedback are the top two killers of safety learning systems in hospitals. The minimum viable intervention is not comprehensive — it is closed. Two error types logged, one preventive rule written, one instance of measurable recurrence reduction. That is the proof of life that keeps the system running.

## The Test

**Population:** Three SRL scheduled agents running weekly tasks over 30 days.
**Measurement:** Error counts by type, weeks 1–2 vs. weeks 3–4.
**Success criterion:** >50% reduction in recurrence of any error type that graduated to a preventive rule by end of week 2.
**Untestable at small scale:** Whether preventive rule injection reduces hallucination-type errors — hallucinations are low-frequency and high-variance, requiring more runs than a 30-day window allows to assess statistically.

## The Connection

This connects to [[neural-sovereignty]]: who owns the agent's error record owns the agent's learning trajectory. The log is the locus of institutional memory — an asset entirely distinct from any individual session.

It connects to [[agent-quartet-framework]]: the error log is the fifth layer the quartet doesn't name — the longitudinal learning substrate that makes the four static specification files dynamic over time. Without it, the quartet defines what the agent should be; the log tracks where it actually fails.

It connects to the [[saturday-flight-check-ritual]]: the Hard Thing section is where system failures that couldn't be fixed automatically escalate to the founder. The error log routes mechanically correctable patterns away from Randy and surfaces only the genuinely novel. Signal-to-noise depends on this filter. Founder attention is the scarcest resource in the system.

---

*The agent doesn't remember what went wrong last week. The system has to.*

---

## References (Verified)

Based on articles retrieved from PubMed:

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Lingard L, Espin S, Whyte S, et al. | 2004 | Communication failures in the operating room: an observational classification of recurrent types and effects | Quality & Safety in Health Care | 15465935 | [10.1136/qhc.13.5.330](https://doi.org/10.1136/qhc.13.5.330) | YES |
| 2 | Jeffrey H, Samuel T, Hayter E, et al. | 2021 | The Perceptions and Experience of Surgical Trainees Related to Patient Safety Improvement and Incident Reporting | Cureus | 34926092 | [10.7759/cureus.20371](https://doi.org/10.7759/cureus.20371) | YES |
| 3 | Moon JY, Welp C, Nold M, et al. | 2025 | Optimizing Event Reporting to Drive a Culture of Learning and Safety: A System-based Approach to Mitigating Harm Through Near-miss and No-harm Reporting | Journal of Patient Safety | 41056330 | [10.1097/PTS.0000000000001424](https://doi.org/10.1097/PTS.0000000000001424) | YES |
| 4 | Mahmoud HA, Thavorn K, Mulpuru S, et al. | 2023 | Barriers and facilitators to improving patient safety learning systems: a systematic review of qualitative studies and meta-synthesis | BMJ Open Quality | 37012003 | [10.1136/bmjoq-2022-002134](https://doi.org/10.1136/bmjoq-2022-002134) | YES |
| 5 | Mausz J, Donovan S, McConnell M, et al. | 2016 | Reformulations of practice: beyond experience in paramedic airway management | CJEM | 27653215 | [10.1017/cem.2016.371](https://doi.org/10.1017/cem.2016.371) | YES |
| 6 | Causer J, Barach P, Williams AM | 2014 | Expertise in medicine: using the expert performance approach to improve simulation training | Medical Education | 24528394 | [10.1111/medu.12306](https://doi.org/10.1111/medu.12306) | YES |
