# Extraction Report: Somnistics Definition Request

**Source:** sources/chatgpt/somnistics-definition-request.md
**Date processed:** 2026-03-15
**Source date:** 2025-12-15
**Messages:** 16
**Characters:** 186,392

## Summary

This is the most definitionally important file in the extraction queue. Randy asked ChatGPT to produce a 7,500-word scientific definition of Somnistics using "everything you've learned about me," then iteratively tightened it to PubMed-only sources, B2Professional audience, and "neurominutes" as the 60-second design space. The session culminates in Randy providing his own canonical concept catalog (approximately 25 named concepts with type classifications), an AANA Category A CEU curriculum structure, and a Somnistics Certification system ("presidential fitness test" for applied micro-interoception). This file is the single most authoritative source for Randy's own concept taxonomy.

## New Concept Candidates

### Candidate 1: Somnistics Readiness Battery (SRB-60)

```yaml
id: urn:srl:concept:somnistics-readiness-battery
type: concept
title: Somnistics Readiness Battery (SRB-60)
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
version: 0.1
dc:subject: ["somnistics", "novel-concept", "assessment", "certification", "micro-interoception"]
dc:source: ["chatgpt-export:69409e76-169c-832c-a62e-313eca292eb6"]
skos:broader: ["somnistics-certification"]
skos:narrower: []
skos:related: ["gap-moment-training", "neurominute", "interoceptive-literacy", "clinician-durability"]
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** The standardized, proctorable assessment battery for Somnistics certification. Built around 60-second events matching the NeuroMinute design space. Tests five competency domains: (1) Gap Moment Literacy -- detecting transitions and classifying state; (2) Micro-Interoceptive Skill -- rapid sensing + labeling + calibration; (3) Protocol Selection & Fidelity -- choosing the right NeuroMinute for state + context; (4) Measured State Delta -- producing measurable change; (5) Return-to-Task Readiness -- regulating without sedation.

**Randy's voice (direct quote):** "Let's create a Somnistics Certification process, a presidential fitness test of applied micro-interoception gap moment training."

**Extraction confidence:** High -- Randy explicitly commissioned this with a vivid metaphor ("presidential fitness test") and the five competency domains were developed in response to his direction.

---

### Candidate 2: Gap Moment Literacy

```yaml
id: urn:srl:concept:gap-moment-literacy
type: concept
title: Gap Moment Literacy
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
version: 0.1
dc:subject: ["somnistics", "novel-concept", "gap-moment-training", "assessment", "state-classification"]
dc:source: ["chatgpt-export:69409e76-169c-832c-a62e-313eca292eb6"]
skos:broader: ["gap-moment-training"]
skos:narrower: []
skos:related: ["interoceptive-literacy", "state-transition", "somnistics-readiness-battery"]
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** The first competency domain in the SRB-60: the ability to detect transitions and classify likely autonomic state (hyperarousal / hypoarousal / cognitive tunnel / dyspnea loop / ready). This is the "pattern recognition" skill -- knowing when a gap moment is occurring and what state you're in. Distinct from interoceptive literacy (which is about body signal perception) -- gap moment literacy is about transition detection and state classification.

**Extraction confidence:** High -- emerges directly from Randy-commissioned certification framework. Clean relationship to existing concepts.

---

### Candidate 3: Somnistics Certified Professional (SCP)

```yaml
id: urn:srl:concept:somnistics-certified-professional
type: concept
title: Somnistics Certified Professional (SCP)
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
version: 0.1
dc:subject: ["somnistics", "certification", "professional-development", "credentialing"]
dc:source: ["chatgpt-export:69409e76-169c-832c-a62e-313eca292eb6"]
skos:broader: ["somnistics-certification"]
skos:narrower: []
skos:related: ["clinician-durability", "somnistics-readiness-battery", "gap-moment-training"]
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** The credential architecture for Somnistics certification. SCP demonstrates competence in detecting Gap Moments, selecting and executing NeuroMinute protocols with high fidelity, and producing measurable state deltas while maintaining task readiness and safety. Four performance tiers: Bronze / Silver / Gold / Platinum. Advanced credentials: Somnistics Certified Instructor (SCI) and Somnistics Certified Examiner (SCE).

**Extraction confidence:** Medium -- the credential system was developed by ChatGPT in response to Randy's direction. Randy should confirm the naming convention and tier structure.

---

### Candidate 4: Micro-Interoceptive Regulation

```yaml
id: urn:srl:concept:micro-interoceptive-regulation
type: concept
title: Micro-Interoceptive Regulation
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
version: 0.1
dc:subject: ["somnistics", "novel-concept", "interoception", "regulation", "micro-intervention"]
dc:source: ["chatgpt-export:69409e76-169c-832c-a62e-313eca292eb6"]
skos:broader: ["interoception"]
skos:narrower: []
skos:related: ["neurominute", "gap-moment-training", "anterocept", "autonomic-regulation"]
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** The tightened PubMed-only definition describes Somnistics as "the applied science and professional practice of micro-interoceptive regulation." This term captures the mechanism: deploying standardized, repeatable 60-second protocols that deliberately couple respiratory mechanics, cardiac-autonomic dynamics, and interoceptive attention to shift state under pressure. It is the operational verb for what Somnistics does.

**Randy's voice:** Randy directed this tightened definition: "Let's tighten up the sources. Pubmed, highly acclaimed studies only... Micro interoception training for gap moments. For professionals."

**Extraction confidence:** Medium -- the exact phrase "micro-interoceptive regulation" was synthesized by ChatGPT, but it captures Randy's directed intent precisely. May be better as an enrichment to the somnistics concept than a standalone concept.

## Enrichment Candidates

### Enrichment 1: somnistics

**Addition -- PubMed-Only Definition (v1.1):**

The tightened definition from this session is more precise than the current vault note's definition:

> "Somnistics is the applied science and professional practice of micro-interoceptive regulation: deploying standardized, repeatable 60-second protocols ('Neurominutes') that deliberately couple respiratory mechanics, cardiac-autonomic dynamics (vagally mediated HRV), and interoceptive attention (insula-cingulate-brainstem integration) to shift state, preserve executive control, and stabilize performance during 'gap moments' in real-world professional workflows."

This should be considered as a candidate replacement for the current definition, or added as "Clinical-Performance Definition v1.1."

**Randy's voice:** Randy explicitly directed this version: "Pubmed, highly acclaimed studies only, fundamental research and latest findings in our usual multispecialty approach. Micro interoception training for gap moments. For professionals."

### Enrichment 2: somnistics

**Addition -- Three Pillars formulation:**
1. Breathing as a controllable oscillator that entrains autonomic and cardiovascular dynamics
2. HRV as a measurable readout of regulatory capacity and adaptability
3. Interoception as a trainable signal-processing skill supported by insula-cingulate systems

This is a cleaner formulation than the current note's structure. The existing note organizes around "Core Insight" and "Disciplinary Boundaries" but does not have this clean three-pillar framing.

### Enrichment 3: somnistics

**Addition -- What Somnistics is NOT:**
- Not a replacement for diagnosis, psychotherapy, medication, or acute medical management
- Not a promise that one minute "fixes" anything
- Not generic relaxation or "wellness"

This boundary-setting language is clinically important and should be in the vault note.

### Enrichment 4: somnistics

**Addition -- State attractors language:** "Move a nervous system from suboptimal attractors (hyperarousal, hypoarousal, cognitive tunnel, dyspneic panic loops) toward task-ready regulation." This dynamical-systems framing (attractors, state transitions) adds theoretical depth.

### Enrichment 5: somnistics-certification

**Addition:** The existing somnistics-certification note should be enriched with the SRB-60 battery details, the five competency domains, the Bronze/Silver/Gold/Platinum tier system, and the SCI/SCE advanced credentials. This session contains the most complete articulation of the certification system.

### Enrichment 6: gap-moment-training

**Addition -- Randy's canonical definition from his concept catalog:** "A structured way of using micro-transitions as the primary training surface -- teaching people to recognize gap moments, run 60-second protocols, and capture biometric deltas so readiness becomes a habit, not an event. Explicitly positioned as a new category distinct from 'mindfulness apps' or generic wellness."

### Enrichment 7: neurominute

**Addition -- Randy's canonical definition from his concept catalog:** "A 60-second, metadata-tagged micro-intervention that combines breath, attention, and multimodal cues (audio, haptics, visual) with a clear neurotarget (e.g., vagal tone, CO2 tolerance, insula engagement) and tracked biometric response."

## New Evidence Candidates

### Evidence 1: AANA CE Standards and Guidelines

- **Title:** AANA Continuing Education Standards and Approval Guidelines
- **dc:type:** report
- **Relevance:** Regulatory framework for Somnistics CEU course approval; defines Class A CE credit requirements
- **Status:** Operational reference, not scientific evidence. May not need an evidence note but should be tracked for the certification concept.

### Evidence 2: NBCRNA MAC Ed Requirements

- **Title:** NBCRNA Modular Assessment of Competence (MAC Ed) Requirements
- **dc:type:** report
- **Relevance:** Defines Class A requirements (prior approval + assessment component + relevance to nurse anesthesia practice)
- **Status:** Same as above -- operational/regulatory reference.

## New Observation Candidates

### Observation 1: Randy's Canonical Concept Catalog (25+ terms)

```yaml
id: urn:srl:observation:randy-concept-catalog-v0
type: observation
title: "Randy's First-Pass Canonical Concept Catalog"
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
dc:subject: ["somnistics", "concept-inventory", "ip-catalog", "taxonomy"]
observation_type: craft-knowledge
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** Randy provided his own structured concept catalog organized into categories:

**A. Core Category & Product Concepts:** Somnistics, SRL, Gap Moment, Gap Moment Training, Pausality/PAUSE II, NeuroMinute

**B. Neuroadaptive / Data / IP Constructs:** Gap Moment Detection Engine, Neuroadaptive Training System for CRNAs

**C. Framework/Method Concepts (implied from the full list):** Anterocept, ExterOryx, MPIC, NeuroHarmonics, PolyAnchora, SomnoAffinity, TransMetachora, Neurogating, Neuro-Ouroboros

Randy classified each with a "Type" (Field, Methodology, Brand, Product, Engine, Training Modality, Content Unit, etc.) and provided tight definitions. This is the ground-truth registry for which concepts Randy considers his own.

**Randy's voice (direct quote):** "Here's a first-pass catalog of the distinctive / 'only-in-Randy-land' concepts that show up across this conversation and the attached docs."

**Extraction confidence:** Very High -- this is Randy speaking directly about his own concept taxonomy.

### Observation 2: AANA CEU Curriculum Architecture

```yaml
id: urn:srl:observation:aana-ceu-curriculum-somnistics
type: observation
title: "Somnistics AANA Category A CEU Curriculum Design"
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
dc:subject: ["somnistics", "ceu", "aana", "curriculum-design", "crna", "certification"]
observation_type: craft-knowledge
clinical_context: "AANA-compliant CE course for CRNAs"
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** Randy directed the creation of a 6.0 Class A CE credit course titled "Somnistics for CRNAs: Gap Moment Training & NeuroMinutes for Autonomic Readiness Under Clinical Load." Randy specified the role ("world famous curriculum designer working with the team of Jared Bruder and Jason Fields") and the compliance standard (AANA Category A). The resulting curriculum includes AANA CE Content Codes (01.12.02 Strategies to Limit Practitioner Stress, 01.12.01 Promote Practitioner Health, 01.13 Culture of Safety, 01.09.02 EBP). Course description emphasizes: "This is intentionally not a 'mindfulness class.' It is a performance-and-safety curriculum."

**Randy's voice (direct quote):** "Role: world famous curriculum designer working with the the team of Jared Bruder and Jason Fields. Teach these concepts in an AANA category A CEU approved manner."

**Extraction confidence:** High -- Randy directed the entire structure and named real collaborators.

### Observation 3: "State Control as Operational Capability"

```yaml
id: urn:srl:observation:state-control-operational-capability
type: observation
title: "Somnistics as State Control, Not Relaxation"
status: draft
creator: Randy Graybeal
created: 2026-03-15
modified: 2026-03-15
dc:subject: ["somnistics", "positioning", "state-transition", "clinical-philosophy"]
observation_type: pattern
prov:wasDerivedFrom: ["urn:srl:chat:chatgpt-somnistics-definition-request"]
```

**Body:** A core positioning insight from the tightened definition: "Somnistics is not 'relaxation' as an aesthetic; it is state control as an operational capability." This single sentence distinguishes Somnistics from the entire wellness/meditation app market and positions it as a professional performance tool. The framing -- "operational capability" -- comes from military/aviation/clinical language and signals the target audience.

**Extraction confidence:** High -- this is the most load-bearing positioning sentence in the entire definition. While synthesized by ChatGPT in response to Randy's direction, it precisely captures Randy's counter-positioning philosophy.

## Relationship Discoveries

| Source Concept | Relation | Target Concept | Evidence |
|---|---|---|---|
| somnistics-certification | skos:narrower | somnistics-readiness-battery (new) | SRB-60 is the assessment instrument within the certification |
| somnistics-certification | skos:narrower | somnistics-certified-professional (new) | SCP is the credential issued through certification |
| gap-moment-training | skos:narrower | gap-moment-literacy (new) | Gap Moment Literacy is the first competency domain of GMT assessment |
| somnistics | skos:related | micro-interoceptive-regulation (new) | The operational mechanism Somnistics employs |
| interoceptive-literacy | skos:related | gap-moment-literacy (new) | Body signal perception vs. transition detection -- related but distinct skills |
| clinician-durability | skos:related | somnistics-readiness-battery (new) | SRB-60 measures the capacity that clinician durability describes |

## Flagged for Review

1. **Somnistics Definition v1.1** -- The PubMed-tightened definition is arguably better than the current vault note's definition. Randy should decide whether to upgrade the canonical definition.
2. **SCP credential naming** -- ChatGPT proposed "Somnistics Certified Professional"; Randy should confirm this is the name he wants.
3. **SRB-60 five competency domains** -- These were developed collaboratively; Randy should validate each domain name and description.
4. **Micro-Interoceptive Regulation** -- Better as a standalone concept or as an enrichment to the somnistics definition? Recommend enrichment.
5. **Jared Bruder and Jason Fields** -- Named as curriculum collaborators; should they be tracked in the vault as contributors?
6. **"One breath is likely the minimum effective dose of therapy"** -- Powerful Randy quote from the definition session. Should be captured somewhere prominent (somnistics note? minimum-effective-dose note?).
7. **State attractor language** -- "Hyperarousal, hypoarousal, cognitive tunnel, dyspneic panic loops" as named suboptimal attractors. These could each become concept stubs or be listed in the state-transition concept.

## Verification Batch Retrospective

### What worked well
- Randy's concept catalog is a gold mine -- it provides an authoritative, first-person index of which terms are his
- The iterative tightening process (broad definition -> PubMed-only -> B2Professional -> neurominutes) produces progressively better content at each step
- The certification/SRB-60 content is highly structured and nearly ready to be committed to the vault as-is

### What was challenging
- The ChatGPT "clarification questions" add noise -- multiple messages are just ChatGPT asking Randy to confirm obvious things
- Randy's concept catalog appears in this file but references concepts defined in other files (anterocept-spectrum-overview, multi-phase-interoceptiv-analysis) -- cross-file tracing is necessary
- Some of the strongest content (the v1.1 definition, the three pillars) was generated by ChatGPT under Randy's direction; attribution requires careful judgment about what's "Randy's" vs. "AI-assisted"

### Patterns discovered for future runs
- **"Tighten it up" instructions from Randy produce the highest-quality content** -- when Randy pushes back on ChatGPT's first draft, the revision is almost always more extractable
- **Randy's role-play prompts reveal his aspirational positioning** -- "world famous curriculum designer" and "advanced library scientist" show how Randy wants these concepts to be perceived
- **Concept catalogs provided by Randy are extraction gold** -- if other files contain similar self-inventories, they should be prioritized
- **Certification/assessment frameworks are highly structured** -- they map cleanly to the vault's concept architecture and produce multiple concept candidates per framework
