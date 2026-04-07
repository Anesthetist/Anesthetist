---
created: '2026-03-16'
creator: randy+claude
id: urn:srl:concept:vault-architecture-v2
modified: '2026-03-16'
status: canonical
subjects:
- knowledge-management
- information-architecture
- compliance
- due-diligence
- evidence-grading
- ontology
title: 'SRL Knowledge Vault Architecture v2: Compliance-Ready Evidence Infrastructure'
type: concept
---

# SRL Knowledge Vault Architecture v2: Compliance-Ready Evidence Infrastructure

## Design Principle

Every claim traceable. Every concept graded. Every modification timestamped. Due diligence is a query, not a project.

---

## 1. Epistemic Unit: The Claim

**Current state:** Evidence notes summarize papers. A note may contain 3-5 findings, all linked to a concept with equal weight.

**Target state:** The atomic unit of knowledge is the **claim** — a single, falsifiable assertion extracted from a source, carrying its own provenance, confidence grade, and concept linkages.

**Schema:**
```yaml
type: claim
id: urn:srl:claim:{slug}
assertion: "HRV biofeedback produces clinically significant reductions in substance use craving"
source_evidence: urn:srl:evidence:jama-2025-hrv-biofeedback-substance-use-rct
evidence_grade: 1b  # Oxford CEBM level
confidence: high
direction: supports  # supports | challenges | extends | qualifies
linked_concepts:
  - urn:srl:concept:autonomic-regulation
  - urn:srl:concept:vagal-tone
claim_scope: "Substance use disorder population; 8-week intervention window"
limitations: "Phase 2 trial; single-site; replication needed"
extracted_by: weekly-hpo-scan
extraction_date: 2026-03-14
```

**Why it matters for compliance:** When a clinical partner asks "what evidence supports Gap Moment Training?", the system returns specific, graded claims with full provenance — not a reading list. When an investor asks "how defensible is your science?", you can show that 60% of your claims carry Level 1-2 evidence and the rest have a clear pathway to validation.

---

## 2. Evidence Grading: Oxford CEBM + GRADE Hybrid

Every evidence link carries a quality grade using the Oxford Centre for Evidence-Based Medicine (CEBM) levels, adapted for SRL's context:

| Grade | Description | Example |
|-------|-------------|---------|
| **1a** | Systematic review of RCTs | HRV biofeedback cardiovascular meta-analysis (13 RCTs) |
| **1b** | Individual RCT (high quality) | JAMA Psychiatry HRV biofeedback substance use trial |
| **2a** | Systematic review of cohort studies | — |
| **2b** | Individual cohort study | — |
| **3a** | Systematic review of case-control studies | — |
| **3b** | Individual case-control study | — |
| **4** | Case series, poor-quality cohort/case-control | Meditation CSF fluid dynamics (small N) |
| **5a** | Expert opinion with clinical data | Randy's 28-year clinical observations; 459-CRNA survey |
| **5b** | Expert opinion / mechanistic reasoning | SRL framework observations; cross-traditional analysis |
| **SRL-P** | SRL proprietary field data (pre-publication) | Diaphragmatic blindness 28/30 finding; Mayo Clinic field use |
| **SRL-O** | SRL original observation (not yet validated) | Gap moment philosophical anchors; Neuro-Ouroboros design |

**Additional GRADE dimensions on each link:**
- **Consistency:** Does this align with other evidence? (consistent / mixed / contradicted)
- **Directness:** Does this directly test the SRL concept, or is it inferred? (direct / indirect / extrapolated)
- **Freshness:** Publication date + decay score (current / aging / historical)
- **Replication status:** (replicated / awaiting replication / single study)

**Compliance value:** This grading system allows SRL to honestly represent its evidence maturity to any audience — clinical, investor, regulatory, or academic — without overstating or understating. It also makes the FDA wellness-vs-medical boundary concrete: SRL can point to exactly which claims are supported at which level, and which are aspirational.

---

## 3. Controlled Vocabulary and Thesaurus

**Structure:** Every subject tag in the vault maps to a controlled term with:
- **Preferred term** (canonical label used in the vault)
- **Synonyms** (alternative labels that resolve to the preferred term)
- **Broader term** (parent in the hierarchy)
- **Narrower terms** (children in the hierarchy)
- **Related terms** (non-hierarchical associations)
- **Scope note** (definition and usage guidance)
- **External identifiers** (MeSH, SNOMED-CT, UMLS CUI, NeuroLex where applicable)

**Example entry:**
```yaml
preferred_term: heart-rate-variability
synonyms: [HRV, cardiac autonomic function, beat-to-beat variability, R-R interval variability]
broader: autonomic-regulation
narrower: [RMSSD, SDNN, LF-HF-ratio, respiratory-sinus-arrhythmia, coherence-ratio]
related: [vagal-tone, resonant-breathing-frequency, biofeedback, polyvagal-theory]
scope_note: "The variation in time intervals between consecutive heartbeats. Primary non-invasive marker of autonomic nervous system function. SRL uses HRV as both a measurement tool and a biofeedback target."
external_ids:
  mesh: D006339
  snomed: "251670001"
  umls: C0018810
```

**Compliance value:** Standard identifiers make the vault interoperable with PubMed, clinical research databases, CE accreditation systems, and patent filings. When AANA reviews SRL's CE application, terms map directly to their ontology. When a patent examiner searches prior art, SRL's terminology matches the standard databases.

---

## 4. Faceted Classification

Every note is classifiable along independent axes. This replaces flat tagging with structured, queryable dimensions.

### Axis 1: Mechanism
`autonomic` | `cognitive` | `somatic` | `metabolic` | `circadian` | `social-relational` | `consciousness`

### Axis 2: Modality
`breathwork` | `biofeedback` | `neurofeedback` | `meditation` | `movement` | `auditory` | `pharmacological` | `environmental` | `relational` | `AI-guided`

### Axis 3: Population
`crna` | `nurse` | `physician` | `surgeon` | `executive` | `military` | `athlete` | `family` | `general-adult` | `adolescent` | `elder`

### Axis 4: Evidence Quality
`meta-analysis` | `rct` | `cohort` | `case-control` | `case-series` | `expert-clinical` | `mechanistic` | `proprietary-field` | `market-intelligence`

### Axis 5: Temporal Window
`acute` (seconds-minutes) | `session` (single training) | `protocol` (multi-week) | `developmental` (months-years) | `career-longitudinal`

### Axis 6: Readiness Level (adapted from NASA TRL)
- **KRL 1:** Basic observation — phenomenon noticed
- **KRL 2:** Concept formulated — hypothesis stated
- **KRL 3:** Proof of concept — initial evidence supports the claim
- **KRL 4:** Validated in controlled setting — lab/clinical study confirms
- **KRL 5:** Validated in real-world setting — field data confirms
- **KRL 6:** Demonstrated at scale — multi-site or multi-population
- **KRL 7:** Standardized and reproducible — protocol documented, trained practitioners can replicate
- **KRL 8:** Accredited or certified — recognized by external body (AANA, institutional partner)
- **KRL 9:** Industry standard — widely adopted reference framework

**Compliance value:** KRL (Knowledge Readiness Level) gives investors and partners a single number to understand how mature any given SRL concept is. "Gap Moment Training is at KRL 5 — validated in real-world clinical settings with 459 CRNAs and field use at Mayo Clinic. We're working toward KRL 6 with the VCU study." That's the kind of sentence that makes due diligence a conversation, not an interrogation.

---

## 5. Provenance and Audit Trail

Every note and every modification carries:
```yaml
provenance:
  created_by: "randy" | "claude" | "weekly-hpo-scan" | "manual-import"
  created_at: ISO-8601 timestamp
  modification_log:
    - date: 2026-03-16
      author: claude
      action: "created"
      reason: "Weekly HPO scan — March 2026"
    - date: 2026-03-20
      author: randy
      action: "promoted to review"
      reason: "Verified against primary source"
  review_chain:
    - reviewer: randy
      date: 2026-03-20
      decision: "approve"
      notes: "Confirmed clinical relevance from personal practice"
```

**Compliance value:** Full audit trail means any external reviewer can see exactly when knowledge entered the system, who validated it, and what decisions were made along the way. This is table stakes for clinical research partnerships, IRB submissions, and investor due diligence.

---

## 6. Compliance Metadata Layer

Each concept and evidence note can optionally carry:
```yaml
compliance:
  fda_classification: "general-wellness" | "non-device" | "class-I" | "class-II" | "not-applicable"
  fda_boundary_notes: "This concept describes a general wellness practice. No diagnostic or treatment claims."
  irb_status: "not-required" | "exempt" | "approved" | "pending" | "planned"
  irb_protocol: "VCU-IRB-2026-XXX"
  ce_accreditation:
    body: "AANA"
    category: "A"
    status: "application-submitted"
    credit_hours: 4.0
  ip_status:
    patent: "US Provisional 2025-04-03"
    trademark: ["Gap Moment Training", "NeuroMinute", "Pausality"]
    trade_secret: false
  hipaa_relevance: "No PHI involved in concept definition or evidence chain"
  data_classification: "public" | "internal" | "confidential" | "restricted"
```

**Compliance value:** When a hospital system's legal team does a vendor review, or when an investor's counsel runs due diligence, the answers are already structured in the metadata. "Is this FDA-regulated?" → query the vault. "Do you have IRB approval?" → query the vault. "What's your IP position?" → query the vault.

---

## 7. Contradiction and Confidence Tracking

When new evidence contradicts existing evidence:
```yaml
contradiction:
  claim_a: urn:srl:claim:polyvagal-phylogenetic-hierarchy-valid
  claim_b: urn:srl:claim:grossman-2026-pvt-untenable
  status: "active-debate"  # resolved-in-favor-of-a | resolved-in-favor-of-b | active-debate | superseded
  srl_position: "Clinical interventions derived from PVT remain effective regardless of evolutionary mechanism debate. SRL references measurable autonomic outcomes, not phylogenetic claims."
  last_reviewed: 2026-03-14
  next_review: 2026-06-14
```

**Compliance value:** Proactively tracking scientific disagreements — and documenting SRL's reasoned position — demonstrates intellectual honesty. An investor who discovers the polyvagal debate independently will be reassured that SRL already accounted for it, rather than being blindsided by it.

---

## 8. Knowledge Gap Analysis

Automated quarterly analysis that cross-references:
- **Concepts × Evidence Grade:** Which concepts lack Level 1-3 evidence?
- **Concepts × Population:** Which concepts are validated only for CRNAs but claimed for executives?
- **Concepts × KRL:** Where are the bottlenecks in readiness progression?
- **Evidence × Freshness:** Which evidence chains rely on studies older than 3 years?
- **Audience × Evidence Density:** Which target audiences have thin evidence support?

Output: A ranked list of **research priorities** — the specific studies, partnerships, or data collection efforts that would most efficiently strengthen the weakest links in the evidence infrastructure.

**Compliance value:** Shows investors and partners that SRL has a systematic, honest assessment of what it knows and doesn't know — and a plan to close the gaps. This is the opposite of hand-waving.

---

## Implementation Priority

| Phase | What | Why First | Timeline |
|-------|------|-----------|----------|
| **1** | Evidence grading on all existing evidence notes | Instant credibility upgrade; enables KRL scoring | Week 1-2 |
| **2** | Controlled vocabulary + thesaurus (top 50 terms) | Eliminates duplicate tags; enables faceted search | Week 2-3 |
| **3** | Faceted classification on existing notes | Makes vault queryable by mechanism, population, quality | Week 3-4 |
| **4** | KRL scoring on all 46 concepts | Gives every concept a maturity number | Week 4-5 |
| **5** | Compliance metadata on IP-relevant concepts | Due diligence readiness for SAFE round | Week 5-6 |
| **6** | Claim extraction pilot (top 10 evidence notes) | Proves the claim-level architecture | Week 6-8 |
| **7** | Contradiction tracking (polyvagal, HRV debate) | Demonstrates intellectual honesty | Week 8 |
| **8** | Knowledge gap analysis v1 | First automated gap report | Week 9-10 |

---

## The Promise

When this architecture is complete, the following scenarios become trivial:

- **Investor due diligence:** "Show me your evidence for autonomic regulation interventions." → Filtered query returns 14 claims, graded 1a through 5b, with full provenance chains and a KRL-5 maturity score.

- **Clinical partner review:** "What's your IRB status and FDA position?" → Compliance metadata layer returns structured answers per concept.

- **AANA CE application:** "Map your curriculum to established science." → Controlled vocabulary with MeSH identifiers links every training module to peer-reviewed evidence.

- **Patent defense:** "Demonstrate the novelty of Gap Moment Training." → Claim extraction shows the specific novel combination that doesn't exist in prior art, supported by SRL-P level proprietary field data.

- **Competitive differentiation:** "Why are you different from Calm, Headspace, or Whoop?" → KRL scores show SRL operating at levels 5-7 on concepts that competitors address at levels 1-2.

Due diligence becomes a query. Compliance becomes a byproduct. Predictability becomes the default.
