---
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
modified: '2026-03-15'
prov:wasDerivedFrom:
- urn:srl:chat:chatgpt-multi-phase-interoceptiv-analysis
- urn:srl:evidence:bids-brain-imaging-data-structure
- urn:srl:evidence:nwb-neurodata-without-borders
- urn:srl:evidence:cdisc-clinical-data-interchange
- urn:srl:evidence:fhir-health-interoperability
- urn:srl:evidence:ieee-1752-open-mobile-health
- urn:srl:evidence:open-mhealth-schema-library
- urn:srl:evidence:dht-metadata-framework-2022
skos:broader:
- somnistics
skos:narrower: []
skos:related:
- cognitive-variability-analysis
- neurominute
status: draft
title: Neurotagging
type: concept
version: '0.1'
---

# Neurotagging

Randy's coined term for a metadata tagging schema that integrates psychological and physiological training modalities with neuroscience datasets. Neurotagging is SRL's approach to creating a universal therapy-neuroscience metadata standard — a layer that does not yet exist in the field.

## Definition

Neurotagging is the practice of applying structured metadata tags to every NeuroMinute session, breath protocol execution, and biometric capture so that the resulting data can be cross-referenced across psychological interventions, physiological measurements, and neuroscience research datasets.

## Standards Gap

Current neuroscience data standards (BIDS for neuroimaging, NDA/NIMH archives for clinical data) do not natively support therapy session metadata. There is no universal schema for tagging therapeutic interventions with their corresponding neurophysiological targets and outcomes. This gap represents a foundational infrastructure opportunity for SRL.

## Randy's Framing

> "What open datasets are available to combine our concept of neurotagging metadata and integrating these tags with psychologic and physiologic training modalities?"

Randy uses "our concept of neurotagging" possessively, indicating he considers this a coined SRL term and a strategic differentiator.

## Strategic Value

Neurotagging metadata could become the connective tissue between:
- Individual session data (what protocol was run, what state was targeted)
- Longitudinal outcome tracking (how the user's autonomic profile changes over time)
- Population-level research (anonymized, tagged datasets for clinical validation)

## Clinical Interpretation

Pending review.

## Related Concepts

- [[somnistics]] (broader — neurotagging is SRL's metadata strategy)
- [[cognitive-variability-analysis]] — both involve metadata-driven analysis of neural/physiological state
- [[neurominute]] — each NeuroMinute generates tagged data via neurotagging schema
