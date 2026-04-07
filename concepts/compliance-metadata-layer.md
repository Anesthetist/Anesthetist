---
created: '2026-03-16'
creator: randy+claude
id: urn:srl:concept:compliance-metadata-layer
modified: '2026-03-16'
prov:wasDerivedFrom:
- urn:srl:evidence:zuboff-age-surveillance-capitalism
status: review
subjects:
- compliance
- FDA
- IRB
- CE-accreditation
- intellectual-property
- due-diligence
- HIPAA
- data-classification
title: 'SRL Compliance Metadata Layer: FDA, IRB, CE, IP, and Data Classification'
type: concept
---

# SRL Compliance Metadata Layer

## Purpose

Every concept and evidence note in the vault can carry structured compliance metadata. This ensures that when an investor, clinical partner, regulatory body, or legal counsel asks a compliance question, the answer is a query — not a research project.

---

## 1. FDA Classification

Applied to **concepts** that describe interventions or products.

```yaml
fda:
  classification: "general-wellness" | "non-device" | "class-I" | "class-II" | "exempt" | "not-applicable"
  boundary_notes: "Free text describing regulatory positioning"
  last_reviewed: "2026-03-16"
  reviewed_by: "regulatory-counsel" | "internal" | "pending-review"
```

### Current FDA Position by Concept

| Concept | Classification | Boundary Notes |
|---------|---------------|----------------|
| Gap Moment Training | general-wellness | Training methodology; no diagnostic or treatment claims. Educational content. |
| NeuroMinute | general-wellness | 60-second guided practice; general stress management framing |
| Resonant Breathing Frequency | general-wellness | Breathing technique; no specific disease claims |
| HRV Biofeedback (SRL implementation) | general-wellness | General wellness biofeedback; does not diagnose, treat, cure, or prevent disease |
| Anterocept | not-applicable | Theoretical framework; no product or intervention |
| Pausality App | general-wellness | Software for general wellness; must maintain wellness framing in all claims |
| NeuroHarmonics | not-applicable | Research framework only at this stage |
| Clinician Durability | not-applicable | Conceptual framework; interventions underneath carry their own classifications |

### FDA Boundary Rules for Marketing/Communications

- **NEVER claim:** diagnosis, treatment, cure, prevention of any disease or condition
- **SAFE claims:** "supports general wellness," "promotes relaxation," "helps manage everyday stress," "supports focus and attention"
- **GRAY ZONE (requires counsel):** "reduces burnout" (burnout is in ICD-11), "improves clinical performance" (implies medical outcome)
- **Reference:** FDA General Wellness Policy (2019); see `urn:srl:observation:fda-wellness-boundary`

---

## 2. IRB Status

Applied to **evidence notes** that involve human subjects research, and to **concepts** that have associated research protocols.

```yaml
irb:
  status: "not-required" | "exempt" | "expedited" | "full-review" | "approved" | "pending" | "planned" | "not-applicable"
  protocol_number: "VCU-IRB-2026-XXX"
  institution: "Virginia Commonwealth University"
  pi: "Dr. Hunnicutt"
  approval_date: "YYYY-MM-DD"
  expiration_date: "YYYY-MM-DD"
  amendments: []
  data_safety_monitoring: true | false
```

### Current IRB Status by Research Activity

| Activity | Status | Institution | Notes |
|----------|--------|-------------|-------|
| 459-CRNA UXR Survey | exempt | — | Anonymous survey; no intervention; no PHI |
| Diaphragmatic Blindness Assessment | planned | VCU (proposed) | Observational; likely exempt |
| VCU Clinician Durability Study | planned | VCU | Full protocol in development; see `urn:srl:observation:honeycutt-vcu-research-agenda` |
| Mayo Clinic Field Use | not-required | Mayo Clinic | Wellness program use; not research protocol |
| MUSC Pediatric Surgery Pilot | planned | MUSC | See `urn:srl:observation:musc-pediatric-surgery-pilot` |
| Vigilance & Field-Coherence Studies | planned | TBD | See `urn:srl:observation:vigilance-field-coherence-study-methods` |

---

## 3. CE Accreditation

Applied to **output notes** and **concepts** that map to continuing education content.

```yaml
ce_accreditation:
  body: "AANA" | "ANCC" | "AMA" | "other"
  category: "A" | "B" | "other"
  status: "approved" | "application-submitted" | "in-preparation" | "planned" | "not-applicable"
  credit_hours: 4.0
  application_date: "YYYY-MM-DD"
  approval_date: "YYYY-MM-DD"
  expiration_date: "YYYY-MM-DD"
  curriculum_mapping: ["list of concept URNs this CE content covers"]
```

### Current CE Status

| Program | Body | Category | Status | Credit Hours |
|---------|------|----------|--------|-------------|
| Pausality Interoceptive Training Program | AANA | A | application-submitted | 4.0 |
| Inside-Out Performance (WANA Lecture) | — | — | planned | TBD |
| Somnistics Certification Program | AANA (target) | A | in-preparation | 20+ (modular) |

### CE Evidence Requirements

AANA Category A requires that educational content be:
- Based on peer-reviewed evidence (Level 1-3 preferred)
- Mapped to established learning objectives
- Assessed with pre/post evaluation

The evidence grading framework (see `urn:srl:concept:evidence-grading-framework`) directly feeds this requirement. Every CE module maps to concepts, which map to graded evidence.

---

## 4. Intellectual Property Status

Applied to **concepts** with IP implications.

```yaml
ip:
  patents:
    - filing: "US Provisional"
      filing_date: "2025-04-03"
      title: "AI-Guided Neuroadaptive Biometric Feedback System"
      status: "filed" | "pending-examination" | "granted" | "abandoned"
      claims_covered: ["list of concept URNs"]
  trademarks:
    - mark: "Gap Moment Training"
      status: "filed" | "registered" | "intent-to-use" | "planned"
      class: "IC 041 — Education and entertainment services"
    - mark: "NeuroMinute"
      status: "filed"
  trade_secrets:
    - description: "Diaphragmatic blindness assessment protocol"
      protection_measures: "NDA required; not published"
    - description: "28/30 clinician field data"
      protection_measures: "Internal only until publication"
  copyright:
    - work: "NeuroMinute scripts"
      status: "automatic"
      registration: "planned"
  data_rights:
    - dataset: "459-CRNA survey responses"
      ownership: "Somnistics Research Labs"
      usage_restrictions: "Internal research and product development"
```

### Current IP Portfolio Summary

| IP Type | Count | Status |
|---------|-------|--------|
| Provisional Patent | 1 | Filed April 2025 |
| Trademarks | 35+ | Various (filed, planned, intent-to-use) |
| Trade Secrets | 5+ | Protected by NDA |
| Copyright | 10+ | Automatic; registration planned |
| Proprietary Datasets | 3+ | Internal; NDA protected |

### IP-Critical Concepts (Require Confidentiality Controls)

These concepts contain proprietary SRL contributions that should NOT be fully disclosed in public-facing materials without IP counsel review:

- Anterocept (novel predictive interoception framework)
- Neuro-Ouroboros (patent architecture)
- Gap Moment Detection Engine (technical specification)
- Multi-Phase Interoceptive Coupling (novel measurement approach)
- PAS-ME: Predictive Autonomic State Modeling Engine
- Anterocept Four-Layer Architecture

---

## 5. Data Classification

Applied to **all notes** to control access and disclosure.

```yaml
data_classification: "public" | "internal" | "confidential" | "restricted"
```

| Level | Who Can See | Examples |
|-------|-------------|---------|
| **Public** | Anyone; safe for website, presentations, publications | Published evidence summaries; general concept descriptions |
| **Internal** | SRL team + authorized collaborators | KRL assessments; gap analyses; market intelligence |
| **Confidential** | SRL team only; NDA required for external sharing | IP-critical concepts; proprietary field data; financial models |
| **Restricted** | Named individuals only | Patient-adjacent data; partnership terms; investor details |

### Classification Rules

- All **evidence notes** from published literature: `public`
- All **SRL-P proprietary field data**: `confidential` until published
- All **SRL-O original frameworks**: `internal` (shareable with NDA)
- All **observation notes with financial/investor data**: `confidential`
- All **audience profiles**: `internal`
- All **market intelligence**: `internal`
- All **patent-related technical details**: `restricted`

---

## 6. HIPAA Relevance

```yaml
hipaa:
  phi_present: false
  phi_notes: "No protected health information in this note"
  de_identification_method: "N/A" | "safe-harbor" | "expert-determination"
```

**Current position:** The SRL Knowledge Vault contains NO protected health information (PHI). All clinical observations are de-identified and aggregated. The 459-CRNA survey was anonymous. Field testing observations reference roles, not individuals (except Randy's own clinical experience, which is self-disclosed).

**If PHI is ever introduced** (e.g., from a clinical trial with identifiable data), it MUST be:
- Flagged as `restricted` data classification
- De-identified using Safe Harbor or Expert Determination methods
- Stored in a separate, access-controlled partition
- Covered by a BAA with any data processor

---

## 7. Audit Trail Extension

Every compliance-relevant note carries:

```yaml
audit:
  created_by: "randy" | "claude" | "weekly-hpo-scan" | "manual-import"
  created_at: "2026-03-16T09:00:00-07:00"
  last_modified_by: "claude"
  last_modified_at: "2026-03-16T09:00:00-07:00"
  review_history:
    - reviewer: "randy"
      date: "2026-03-16"
      action: "approved"
      notes: "Confirmed clinical accuracy"
  compliance_review:
    - reviewer: "ip-counsel"
      date: "pending"
      scope: "Patent claims alignment"
```

---

## Due Diligence Query Examples

| Question | Query |
|----------|-------|
| "What's your FDA position?" | Filter concepts by `fda.classification`; return table |
| "Do you have IRB approval?" | Filter by `irb.status`; return approved + planned pipeline |
| "What's your IP portfolio?" | Aggregate `ip` fields across all concepts |
| "Is any PHI involved?" | Filter by `hipaa.phi_present = true`; expect empty set |
| "What's your CE accreditation status?" | Filter by `ce_accreditation.status`; return table |
| "What's confidential vs. public?" | Group by `data_classification`; return counts and examples |
| "Show me the evidence chain for [concept]" | Traverse concept → evidence links, return with grades and provenance |

Each of these queries should return structured, timestamped, auditable answers — not a narrative somebody wrote last month.
