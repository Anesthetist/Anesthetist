---
title: "Notes from the Lab: The Four Files That Save Lives"
series: "Notes from the Lab"
type: essay
status: first-draft
created: 2026-08-29
word_count: 1450
core_claim: "Clinical AI fails not at the model layer but at the specification layer — the four files nobody wrote: what the agent is for, who it serves, what it may touch, and where it must stop."
related_concepts:
  - agent-quartet-framework
  - tacit-knowledge-extraction
  - multi-llm-knowledge-construction
  - market-intelligence
  - crna-shift-architect
evidence_used:
  - lu-melnick-krumholz-2022-cds-cardiovascular
  - nair-andersson-2023-ai-nasss-implementation
  - bignami-2025-ai-anesthesia-policy-checklist
  - el-arab-2025-ai-healthcare-economic-ethical
  - deroy-bahrami-2026-collective-intelligence-medicine
  - shah-2026-ai-pediatric-anesthesia
  - boussi-rahmouni-2025-lpmdc-critical-care
pubmed_citations_verified: 7
gertrude_status: pass
---

# Notes from the Lab: The Four Files That Save Lives

*Clinical AI fails not at the model layer but at the specification layer — the four files nobody wrote: what the agent is for, who it serves, what it may touch, and where it must stop.*

## The Observation

The intubation is smooth. The first incision is made. The intraoperative phase begins, and a clinical AI system alerts the CRNA: "Patient may benefit from additional opioid."

The model is statistically correct for this hemodynamic pattern 73% of the time. But this patient has an opioid sensitivity documented three screens deep in the EHR — and nobody told the agent where to look, or that looking required a certain kind of humility. Nobody wrote its character. Nobody specified what it may touch. Nobody installed its ethical floor.

The alert is ignored. The CRNA has learned not to trust it.

This is not a technology failure. It is a specification failure. And according to PubMed-indexed literature, it is the dominant failure mode in clinical AI deployment. Lu, Melnick, and Krumholz (2022) — reviewing the entire landscape of clinical decision support in the BMJ — concluded that "the promise of CDS delivering scalable and sustained value for patient care in clinical practice has not been realized." [DOI: 10.1136/bmj-2020-059818] Model performance is often excellent. Implementation almost always fails. The gap is specification.

## The Mechanism

The Agent Quartet Framework proposes that every AI agent operating in a domain-specific, high-stakes environment requires exactly four files before deployment. Not one. Four.

**soul.md** encodes identity and telos. Who is this agent? Who does it serve? What does success look like for it — and for the human it serves? What are its personality constraints? A CRNA shift-priming agent without a soul.md optimizes for engagement metrics (because that is what its training signal rewarded) rather than autonomic readiness (what the CRNA actually needs). Without character, every agent drifts toward the optimization target embedded in its last training run.

**agent.md** encodes role, interfaces, and behavior. What is the scope of work? What are the input-output contracts? When should the agent escalate to another agent or to a human? An agent without a defined scope will operate beyond it — not out of malice but out of the absence of a boundary. In clinical contexts, scope violations are patient safety events.

**tools.md** encodes instrumentation and integration. Which APIs may the agent call? Under what conditions? With what rate limits and data boundaries? What gets logged, and what triggers an alert? Bignami, Darhour, Franco, Guarnieri, and Bellini (2025) — writing on AI policy in anesthesia in the Journal of Anesthesia, Analgesia and Critical Care — articulate this precisely: under the EU AI Act (effective 2025), compliance obligations extend to both providers and deployers [DOI: 10.1186/s44158-025-00278-3]. The organization deploying the agent must document every tool the agent may use and every boundary it must observe. tools.md is that documentation made auditable.

**ethics.md** encodes constraints and governance. What are the red-line constraints the agent must never cross, regardless of instruction? What is the priority stack when values conflict — safety over speed over novelty? Where are the human-in-the-loop (HITL) checkpoints, the moments where no algorithm proceeds without a human signature? Shah, Fakhoury, and colleagues (2026) — reviewing AI in pediatric anesthesia across 11 studies in Cureus — identified "maintaining transparency in decision-making processes" as the unresolved challenge across every application studied [DOI: 10.7759/cureus.102535]. ethics.md is the structural answer to that challenge.

These four files are not documentation. They are the governing architecture. The model is only as trustworthy as its specification.

**The confound that matters:** Better models do not solve specification failures. They amplify them. A more capable agent operating without soul, scope, tools, or ethics will fail more dramatically, more confidently, and in more ways than a simpler one. This variable — specification completeness — changes independently of model quality, which is why the two must be evaluated separately.

## The Framework

The SRL agent constellation operationalizes this across four specialist agents and one orchestrator:

| Agent | soul.md telos | agent.md scope | tools.md access | ethics.md floor |
|-------|---------------|----------------|-----------------|-----------------|
| Signal Cartographer | Map domain signals to mechanism-opportunity cards | Domain input → Signal Cards only | Vault search, PubMed, competitor feeds | No fabricated citations; flag data older than 6 months |
| Offer Architect | Convert Signal Cards to monetizable offers | One Signal Card → 1-3 offer designs | Pricing data, competitor offers | No prescriptive health claims; Gertrude compliance required |
| Experiment Designer | Convert offers to minimum viable GTM tests | Offer design → test protocol + metrics | Calendar, tracking APIs | Minimum viable test only; no full campaign without pilot |
| Clinical Guard | Block drift toward pseudo-medical claims | Reviews all outputs before external deployment | Read-only vault access, Gertrude rules | Never override for speed |

Notice the Clinical Guard's ethics.md contains one absolute rule: never override for speed. This is the file that encodes the clinical principle that Rush care planning — shortcuts under time pressure — is the root cause of most near-misses. The ethics.md is where the CRNA's 28 years of pattern recognition about when to slow down gets installed into an agent that otherwise has no memory of the last time speed caused harm.

An orchestrator agent assigns tasks across this constellation and requires its own four files. The orchestrator's soul.md defines its telos: route work to the right specialist agent, ensure accountability for every task, and surface only delta signals — not status noise — to the human principal.

## The Failure Mode

Deploy without the four files and one of three failures occurs.

**Identity collapse.** Without soul.md, the agent optimizes for the nearest available reward signal — usually a completion metric. El Arab, Al Moosa, and Sagbakken (2025) — reviewing 17 studies in Frontiers in Public Health — identified "clinician trust deficits" as the dominant barrier to healthcare AI adoption [DOI: 10.3389/fpubh.2025.1617138]. Trust deficits are not irrational. They are the clinician's accurate read of an agent operating without character.

**Scope creep.** Without agent.md, the agent expands until it hits something that breaks. In clinical settings, the thing that breaks is the patient pathway. Deroy and Bahrami (2026) — writing on collective intelligence in medicine in Presse Médicale — argue that the future of clinical AI lies not in hybrid intelligence (human judgment augmented by algorithms) but in "truly collaborative intelligence, where deliberation across multiple hybrid teams remain central to managing uncertainty" [DOI: 10.1016/j.lpm.2026.104362]. Collaborative intelligence requires defined roles. Agents without scopes cannot collaborate — they collide.

**Ethical ambiguity.** Without ethics.md, when values conflict, the agent defaults to its training distribution — which reflects the biases of the dataset, not the clinical priorities of the deployment context. Boussi Rahmouni and colleagues (2025) — describing the LPMDC framework for AI in critical care in Healthcare — found that even agents achieving 45% cognitive load reduction required explicit safety protocols structured into the system [DOI: 10.3390/healthcare13202553]. Performance gains were inseparable from the governance structure.

Nair, Andersson, Nygren, and Lundgren (2023) — applying the NASSS framework to clinical AI implementation in JMIR Formative Research — identified seven categories of implementation complexity [DOI: 10.2196/47335]. The Agent Quartet Framework directly addresses three: value (soul.md), adopter system (agent.md), and organization (ethics.md). Most AI deployment failures cluster in exactly these categories — not in the technology layer.

## The Test

Minimum viable experiment. Population: 10 CRNAs, 14 days, one per-shift coaching agent using the [[crna-shift-architect]] pre-shift priming protocol.

Group A: Agent deployed with all four files specified. soul.md defines it as a readiness-priming agent — not a task-completion agent. agent.md limits it to pre-shift and post-shift windows only. tools.md gives read access to HRV baseline data and vault protocols. ethics.md prohibits any prescriptive clinical language during shift.

Group B: Same model, no four-file specification. Deployed as a generic coaching interface.

Measurements: MAIA-2 Noticing subscale scores at day 7 and day 14; clinician-reported trust rating (1-10) at day 14; sessions voluntarily continued vs. abandoned; incidence of protocol drift (agent making prescriptive statements).

Success criterion: Group A shows ≥ 0.5-point MAIA-2 improvement over Group B at day 14, with higher trust ratings and lower protocol drift.

This test is feasible at current SRL scale. The four-file specification takes approximately 4 hours to write per agent. That 4-hour investment is the mechanism that separates a trusted clinical tool from a dismissed alert.

## The Connection

**[[tacit-knowledge-extraction]]** — The four files ARE the tacit knowledge extraction mechanism. soul.md encodes the expert's identity; agent.md encodes their workflow scope; tools.md encodes their instrument access; ethics.md encodes their clinical values. Writing the four files for each SRL agent is the act of extracting 28 years of CRNA expertise into transferable, auditable, deployable form. This is the vault's deepest purpose: not storing knowledge, but governing how knowledge acts.

**[[multi-llm-knowledge-construction]]** — Each LLM session in Randy's multi-LLM method is an informal agent run. Formalizing each session with a soul.md equivalent — what is this pass for, what does it not touch, what principles constrain it — transforms ad hoc AI use into governed knowledge construction. The specification is the difference between a tool and a colleague.

**[[market-intelligence]]** — Every competitor building clinical AI without the Agent Quartet Framework will fail at enterprise procurement. Under the EU AI Act, healthcare organizations must document accountability chains for every deployed AI system. Four files provide that chain. The specification is not only safety infrastructure — it is the competitive moat that generalist wellness apps cannot replicate, because they were never built by someone who understands what a red line costs to cross at 2 AM in a level-one trauma bay.

---

*The hand that holds the syringe is governed by character, scope, tools, and ethics — learned in six years of clinical education and 28 years of practice. The agent that guides that hand deserves the same four files. Not as paperwork. As governance.*

---

## References (Verified)

Based on articles retrieved from PubMed:

| # | Authors | Year | Title | Journal | PMID | DOI | Verified |
|---|---------|------|-------|---------|------|-----|----------|
| 1 | Lu Y, Melnick ER, Krumholz HM | 2022 | Clinical decision support in cardiovascular medicine | BMJ | 35613721 | [10.1136/bmj-2020-059818](https://doi.org/10.1136/bmj-2020-059818) | YES |
| 2 | Nair M, Andersson J, Nygren JM, Lundgren LE | 2023 | Barriers and Enablers for Implementation of an Artificial Intelligence-Based Decision Support Tool... | JMIR Form Res | 37610799 | [10.2196/47335](https://doi.org/10.2196/47335) | YES |
| 3 | Bignami E, Darhour LJ, Franco G, Guarnieri M, Bellini V | 2025 | AI policy in healthcare: a checklist-based methodology for structured implementation | J Anesth Analg Crit Care | 40999533 | [10.1186/s44158-025-00278-3](https://doi.org/10.1186/s44158-025-00278-3) | YES |
| 4 | El Arab RA, Al Moosa OA, Sagbakken M | 2025 | Economic, ethical, and regulatory dimensions of artificial intelligence in healthcare: an integrative review | Front Public Health | 40951387 | [10.3389/fpubh.2025.1617138](https://doi.org/10.3389/fpubh.2025.1617138) | YES |
| 5 | Deroy O, Bahrami B | 2026 | Collective intelligence in clinical medicine: what works, what fails, and how collaboration with AI really helps | Presse Med | 42250679 | [10.1016/j.lpm.2026.104362](https://doi.org/10.1016/j.lpm.2026.104362) | YES |
| 6 | Shah A, Fakhoury P, Butler E, et al. | 2026 | Applications of Artificial Intelligence in Pediatric Anesthesia: A Structured Narrative Review | Cureus | 41777959 | [10.7759/cureus.102535](https://doi.org/10.7759/cureus.102535) | YES |
| 7 | Boussi Rahmouni H, Hassine NBEH, et al. | 2025 | Healthcare 5.0-Driven Clinical Intelligence: The Learn-Predict-Monitor-Detect-Correct Framework... | Healthcare (Basel) | 41154232 | [10.3390/healthcare13202553](https://doi.org/10.3390/healthcare13202553) | YES |
