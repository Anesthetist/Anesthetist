---
clinical_interpretation: 'Three-class schema applied 2026-04-18 after Vigil literature
  scan of BIDS, NDA, FHIR R5, SNOMED-CT/LOINC, NBO, HPO, ICF, DSM-5, ConnectomeDB.
  Randy''s direction: targeted activity plus neuroanatomical target plus (third).
  Third class = Autonomic Response Class (the outcome metric that closes the loop).
  Top 5 required tags per session: modality, anatomical_target, primary_autonomic_metric,
  duration_sec, session_context. Gap the schema fills: no existing standard tags autonomic
  modality taxonomy, neuroanatomical target specificity at subsystem resolution, closed-loop
  dosimetry at the 60-second unit, or mechanism-phenotype binding in a single record.'
created: '2026-03-15'
creator: Randy Graybeal
dc:source:
- chatgpt-export:684a5409-1ac0-8010-b0da-a6a2916d4698
dc:subject:
- somnistics
- metadata
- neuroscience-data
- therapy-integration
- standards
id: urn:srl:concept:neurotagging
modified: '2026-04-18'
prov:wasDerivedFrom:
- urn:srl:chat:chatgpt-multi-phase-interoceptiv-analysis
- urn:srl:evidence:bids-brain-imaging-data-structure
- urn:srl:evidence:nwb-neurodata-without-borders
- urn:srl:evidence:cdisc-clinical-data-interchange
- urn:srl:evidence:fhir-health-interoperability
- urn:srl:evidence:ieee-1752-open-mobile-health
- urn:srl:evidence:open-mhealth-schema-library
- urn:srl:evidence:dht-metadata-framework-2022
- urn:srl:evidence:grawe-2007-neuropsychotherapy
- urn:srl:evidence:barrett-2017-epic-model
- urn:srl:evidence:stephan-2016-computational-psychiatry
- urn:srl:evidence:reber-1989-implicit-learning
skos:broader:
- somnistics
skos:narrower: []
skos:related:
- cognitive-variability-analysis
- neurominute
- embodied-metacognition
- structured-interoception-training
status: draft
title: Neurotagging
type: concept
version: '0.2'
---

# Neurotagging

Randy's coined term for a metadata tagging schema that integrates psychological and physiological training modalities with neuroscience datasets. Neurotagging is SRL's approach to a universal therapy-to-neuroscience metadata standard, a layer that does not yet exist in the field.

## Definition

Neurotagging is the practice of applying structured metadata tags to every [[neurominute]] session, breath protocol execution, and biometric capture so that the resulting data can be cross-referenced across psychological interventions, physiological measurements, and neuroscience research datasets.

## The Standards Gap (2026-04-18 landscape scan)

| Standard | What it captures | What it misses for a 60-second closed-loop autonomic intervention |
|---|---|---|
| BIDS | Imaging acquisition + task metadata | No intervention dosage, no autonomic response, no session-level tracking |
| NDA / NIMH | Clinical trial assessments | Designed for cross-sectional reports; no 60-second micro-intervention granularity |
| FHIR R5 (Observation, Procedure) | Encounter-level clinical events | Encounter-centric; no neuroanatomical target or autonomic modality specificity |
| SNOMED-CT / LOINC | General clinical ontology codes | No codes for autonomic training modalities or vagal-branch specificity |
| NBO (NeuroBehavior Ontology) | Behavioral phenotypes across species | Outcome phenotyping only; silent on intervention parameters |
| HPO (Human Phenotype Ontology) | What goes wrong | Intervention-blind; no autonomic subsystem detail |
| ICF | Functional capacity | Captures whether the patient can breathe, not how the intervention works |
| DSM-5 / ICD-10 | Diagnosis codes | Diagnosis-focused; no intervention mechanism or modality codes |
| ConnectomeDB / OpenNeuro | BIDS-compliant imaging repositories | Retrospective; no prospective closed-loop or real-time feedback |

The gap: no existing standard tags autonomic modality taxonomy, neuroanatomical target specificity at subsystem resolution, closed-loop dosimetry at the 60-second unit, or mechanism-to-phenotype binding in a single record.

## Three-Class Schema

Every NeuroMinute session is tagged across three orthogonal classes. Together they capture intervention-by-target-by-outcome in a single row.

### Class 1. Targeted Activity (what the user does)

The modality being executed. Examples:
`breath-resonant`, `breath-box`, `breath-4-7-8`, `humming`, `vagal-maneuver`, `attention-interoception`, `heart-rate-feedback`, `cold-exposure`, `micro-movement`.

### Class 2. Neuroanatomical Target (what circuit is engaged)

The intended target node or pathway. Examples:
`vagus-dorsal`, `vagus-ventral`, `nucleus-ambiguus`, `nucleus-tractus-solitarius`, `insula-anterior`, `insula-posterior`, `prefrontal-dorsolateral`, `prefrontal-ventromedial`, `amygdala`, `parabrachial-nucleus`, `locus-coeruleus`, `default-mode-network`.

### Class 3. Autonomic Response Class (what outcome is measured)

The physiological signature that confirms the intervention landed. Examples:
`parasympathetic-dominance`, `vagal-tone-shift`, `rmssd-delta`, `skin-conductance-decline`, `respiratory-sinus-arrhythmia`, `vagal-brake-engagement`, `polyvagal-state-shift`, `baroreflex-gain`.

This third class is what closes the loop. Interventions are the means. Neuroanatomy is the target. Outcome metrics are the evidence. A schema that captures all three makes each NeuroMinute a reproducible micro-experiment rather than a logged behavior.

## Top 5 Required Tags Per Session Write

These are non-negotiable for every [[neurominute]] session record.

1. **`modality`**. One or more values from Class 1. Distinguishes mechanism and enables mechanism-specific outcome studies.
2. **`anatomical_target`**. One or more values from Class 2. Maps intervention to vagal subsystem or limbic node. Required for neuroscience replicability.
3. **`primary_autonomic_metric`**. One or more values from Class 3. Real-time physiological proxy (RMSSD, SCL, RSA). Links intervention to autonomic state change.
4. **`duration_sec`**. Integer. Captures dosage precision. A 60-second NeuroMinute that drifts to 120 seconds is a different intervention. Enables micro-dose science.
5. **`session_context`**. Position in protocol (`baseline`, `post-stressor`, `recovery`, `maintenance`, `gap-moment-detected`). Confound control and clinical sequence logic.

## Randy's Framing

> "What open datasets are available to combine our concept of neurotagging metadata and integrating these tags with psychologic and physiologic training modalities?"

Randy uses "our concept of neurotagging" possessively. It is a coined SRL term and a strategic differentiator. The three-class schema above is the first public spec of what the tag layer should contain.

## Strategic Value

Neurotagging metadata becomes the connective tissue between:

- Individual session data (what protocol was run, what state was targeted, what metric moved).
- Longitudinal outcome tracking (how the user's autonomic profile changes across sessions).
- Population-level research (anonymized, tagged datasets for clinical validation and LLM training).

This is the substrate for the Clinical LLM Moat (Red Arrow 4).

## Related Concepts

- [[somnistics]] (broader). Neurotagging is SRL's metadata strategy.
- [[neurominute]]. Each NeuroMinute generates tagged data via the schema.
- [[cognitive-variability-analysis]]. Both involve metadata-driven analysis of neural and physiological state.
- [[pausality]]. The product that writes neurotagged records at session boundaries.
