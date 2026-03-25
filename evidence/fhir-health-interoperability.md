---
clinical_interpretation: Pending review
created: '2026-03-21'
creator: randy
dc:creator:
- HL7 International
dc:date: '2014'
dc:identifier: https://hl7.org/fhir/
dc:subject:
- healthcare-data
- interoperability
- EHR
- wearables
- data-standard
dc:type: standard
id: urn:srl:evidence:fhir-health-interoperability
modified: '2026-03-21'
status: draft
title: HL7 FHIR — Fast Healthcare Interoperability Resources
type: evidence
---

# HL7 FHIR — Fast Healthcare Interoperability Resources

Healthcare data exchange standard. Resources for Patient, Observation, Procedure, Device, DiagnosticReport. Can ingest wearable biometric data (HR, HRV, SpO2, BP). Growing adoption for digital therapeutics platforms connecting to EHRs.

## Relevance to SRL

FHIR is a transport and interoperability standard, not a therapeutic metadata schema. It can move HRV data from an Apple Watch to an EHR, but has no opinion about how to tag the relationship between a breathing intervention and the HRV response. **Neurotagging data could ride on FHIR resources** — making SRL data EHR-interoperable from day one.

## Neurotagging Gap

FHIR is the transport layer. [[neurotagging]] is the semantic layer that gives meaning to what FHIR carries. Complementary, not competing.

**Full text:** [FHIR Specification](https://hl7.org/fhir/)
