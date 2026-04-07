---
created: '2026-03-16'
creator: randy+claude
id: urn:srl:concept:faceted-classification-taxonomy
modified: '2026-03-16'
status: canonical
subjects:
- knowledge-management
- taxonomy
- classification
- compliance
- information-architecture
title: 'SRL Faceted Classification Taxonomy: Six-Axis Queryable Note Classification'
type: concept
---

# SRL Faceted Classification Taxonomy

Every note in the SRL Knowledge Vault is classifiable along six independent axes. This replaces flat tagging with structured, multi-dimensional classification that enables precise queries like: "Show me all RCT-level evidence about autonomic mechanisms in CRNA populations with acute temporal windows."

---

## Axis 1: Mechanism (What physiological system does this address?)

| Code | Label | Description |
|------|-------|-------------|
| `M-AUT` | Autonomic | Sympathetic/parasympathetic regulation, vagal tone, HRV |
| `M-COG` | Cognitive | Attention, memory, executive function, decision-making |
| `M-SOM` | Somatic | Musculoskeletal, fascial, proprioceptive, diaphragmatic |
| `M-MET` | Metabolic | Nutrition, glucose regulation, lactate, cortisol, hormonal |
| `M-CIR` | Circadian | Sleep-wake regulation, chronobiology, light-dark cycles |
| `M-SOC` | Social-Relational | Co-regulation, mirror neurons, team dynamics, attachment |
| `M-CON` | Consciousness | Altered states, meditation, jhana, nondual awareness, cessation |
| `M-NEU` | Neural-Structural | Neuroplasticity, gray matter, white matter, brain connectivity |
| `M-RES` | Respiratory | Breathing mechanics, gas exchange, respiratory drive |
| `M-IMM` | Immune-Inflammatory | Vagal anti-inflammatory pathway, cytokines, allostatic load |

*Notes may carry multiple mechanism codes.*

---

## Axis 2: Modality (What intervention or method is involved?)

| Code | Label | Description |
|------|-------|-------------|
| `D-BRE` | Breathwork | Any breathing-based intervention |
| `D-BIO` | Biofeedback | HRV biofeedback, respiratory biofeedback, thermal |
| `D-NFB` | Neurofeedback | EEG-based neurofeedback, real-time brain training |
| `D-MED` | Meditation | Mindfulness, focused attention, open monitoring, jhana |
| `D-MOV` | Movement | Yoga, exercise, somatic practices, tai chi |
| `D-AUD` | Auditory | Binaural beats, music therapy, sound-based entrainment |
| `D-PHA` | Pharmacological | Drug-based interventions (for reference/comparison) |
| `D-ENV` | Environmental | Light exposure, temperature, workspace design |
| `D-REL` | Relational | Co-regulation, peer support, coaching, team practices |
| `D-AIG` | AI-Guided | AI-driven personalization, adaptive protocols, digital delivery |
| `D-WRB` | Wearable | Wearable sensor-based monitoring or intervention |
| `D-VNS` | Vagal Stimulation | Transcutaneous VNS, auricular, non-invasive |

---

## Axis 3: Population (Who was studied or who is the target?)

| Code | Label | Description |
|------|-------|-------------|
| `P-CRN` | CRNA | Certified Registered Nurse Anesthetists |
| `P-NUR` | Nurse | RNs, NPs, other nursing professionals |
| `P-PHY` | Physician | MDs, DOs, residents |
| `P-SUR` | Surgeon | All surgical specialties |
| `P-AHP` | Allied Health | PAs, paramedics, respiratory therapists |
| `P-EXE` | Executive | C-suite, senior leadership, corporate professionals |
| `P-MIL` | Military | Active duty, veterans, special operations |
| `P-ATH` | Athlete | Competitive and elite athletes |
| `P-FAM` | Family | Parents, children, family units |
| `P-ADU` | General Adult | Non-specific adult population |
| `P-ADO` | Adolescent | Ages 12-18 |
| `P-ELD` | Older Adult | Age 60+ |
| `P-PAT` | Patient | Clinical patient populations (disease-specific) |
| `P-STU` | Student | SRNAs, nursing students, medical students |

---

## Axis 4: Evidence Quality (What type of study is this?)

| Code | Label | Oxford Level |
|------|-------|-------------|
| `E-MA` | Meta-Analysis | 1a |
| `E-SR` | Systematic Review | 1a-2a |
| `E-RCT` | Randomized Controlled Trial | 1b |
| `E-COH` | Cohort Study | 2b |
| `E-CC` | Case-Control Study | 3b |
| `E-CS` | Case Series / Case Report | 4 |
| `E-XS` | Cross-Sectional Survey | 4 |
| `E-EXP` | Expert Clinical Data | 5a |
| `E-THR` | Theoretical / Review | 5b |
| `E-SRL` | SRL Proprietary Data | SRL-P |
| `E-OBS` | SRL Original Observation | SRL-O |
| `E-MKT` | Market Intelligence | N/A |
| `E-PAT` | Patent / IP Filing | N/A |

---

## Axis 5: Temporal Window (What time scale does this operate on?)

| Code | Label | Duration | Example |
|------|-------|----------|---------|
| `T-ACU` | Acute | Seconds to minutes | Physiological sigh; single NeuroMinute |
| `T-SES` | Session | Single training session | One breathwork session; one biofeedback training |
| `T-PRO` | Protocol | Multi-week program | 21-day Moongate course; 8-week HRV biofeedback trial |
| `T-DEV` | Developmental | Months to years | Neuroplasticity changes; interoceptive skill development |
| `T-CAR` | Career-Longitudinal | Full career span | Clinician durability; GMT career arc |
| `T-CHR` | Chronobiological | Circadian / ultradian cycles | Circadian alignment; sleep architecture |

---

## Axis 6: Knowledge Readiness Level (How mature is this knowledge?)

| Code | KRL | Level Name |
|------|-----|-----------|
| `K-1` | 1 | Observation |
| `K-2` | 2 | Hypothesis |
| `K-3` | 3 | Proof of Concept |
| `K-4` | 4 | Controlled Validation |
| `K-5` | 5 | Real-World Validation |
| `K-6` | 6 | Multi-Site/Population |
| `K-7` | 7 | Standardized |
| `K-8` | 8 | Accredited |
| `K-9` | 9 | Industry Standard |

---

## Example Classification

**Note:** `jama-2025-hrv-biofeedback-substance-use-rct`
```
facets:
  mechanism: [M-AUT]
  modality: [D-BIO, D-WRB]
  population: [P-PAT]
  evidence_quality: E-RCT
  temporal_window: T-PRO
  knowledge_readiness: K-4
```

**Note:** `diaphragmatic-blindness-30-clinician-test`
```
facets:
  mechanism: [M-SOM, M-RES]
  modality: [D-BRE]
  population: [P-CRN]
  evidence_quality: E-SRL
  temporal_window: T-ACU
  knowledge_readiness: K-3
```

**Note:** `patapoutian-2025-nih-interoception-atlas`
```
facets:
  mechanism: [M-AUT, M-NEU]
  modality: []
  population: [P-ADU]
  evidence_quality: E-THR
  temporal_window: T-DEV
  knowledge_readiness: K-6
```

---

## Compound Queries This Enables

- "All Level 1a-1b evidence on autonomic mechanisms in healthcare populations" → `E-MA OR E-RCT` + `M-AUT` + `P-CRN OR P-NUR OR P-PHY OR P-SUR`
- "What breathwork evidence exists for executive populations?" → `D-BRE` + `P-EXE`
- "Which concepts have KRL ≥ 5 with direct RCT support?" → `K-5+` + `E-RCT` + directness: direct
- "What's our weakest evidence area for AANA accreditation?" → filter `P-CRN`, sort by `evidence_quality` ascending, identify gaps
- "Show me everything about consciousness and meditation with current freshness" → `M-CON` + `D-MED` + freshness: current

---

## Frontmatter Extension

```yaml
facets:
  mechanism: ["M-AUT", "M-RES"]
  modality: ["D-BRE", "D-BIO"]
  population: ["P-CRN"]
  evidence_quality: "E-RCT"
  temporal_window: "T-PRO"
  knowledge_readiness: "K-5"
```

## Migration Plan

Phase 1: Classify the 20 highest-traffic evidence notes (those linked to 3+ concepts)
Phase 2: Classify all evidence notes with Grade 1a-2b (highest quality first)
Phase 3: Classify remaining evidence notes
Phase 4: Classify observation notes
Phase 5: Automated classification in weekly HPO scan output
