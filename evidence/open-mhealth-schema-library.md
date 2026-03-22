---
clinical_interpretation: Pending review
created: '2026-03-21'
creator: randy
dc:creator:
- Open mHealth
dc:date: '2015'
dc:identifier: https://www.openmhealth.org/documentation/schema-docs/schema-library/
dc:subject:
- mobile-health
- data-schema
- patient-generated-data
- biometrics
dc:type: standard
id: urn:srl:evidence:open-mhealth-schema-library
modified: '2026-03-21'
status: draft
title: Open mHealth Schema Library
type: evidence
---

# Open mHealth Schema Library

Precursor to IEEE 1752. 88+ clinically meaningful schemas for patient-generated health data. Header metadata covers acquisition provenance (where data came from, when collected, how collected). Schema design principles emphasize clinical meaningfulness and composability.

## Relevance to SRL

Same coverage as IEEE 1752 — measurement-side metadata only. The "how it was collected" provenance tracks the sensor and method, not the therapeutic protocol running when data was captured. Composable schema design is a useful model for [[neurotagging]] schema architecture.

## Neurotagging Gap

Open mHealth provides the data representation patterns. [[Neurotagging]] extends with intervention semantics.

**Full text:** [Open mHealth Schemas](https://www.openmhealth.org/documentation/schema-docs/schema-library/)
