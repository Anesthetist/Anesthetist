---
clinical_interpretation: Pending review
created: '2026-03-21'
creator: randy
dc:creator:
- IEEE Standards Association
dc:date: '2021'
dc:identifier: https://standards.ieee.org/ieee/1752.1/6982/
dc:subject:
- mobile-health
- wearables
- data-standard
- HRV
- sleep
- biometrics
dc:type: standard
id: urn:srl:evidence:ieee-1752-open-mobile-health
modified: '2026-03-21'
status: draft
title: IEEE 1752 — Open Mobile Health Data Standard
type: evidence
---

# IEEE 1752 — Open Mobile Health Data Standard

Published standard (IEEE 1752.1-2021) for mobile health data representation — sleep, physical activity, metadata. IEEE P1752.2 (in development) extends to cardiovascular, respiratory, and metabolic measures. Grew from Open mHealth schemas (88+ schemas for clinical health data).

## Relevance to SRL

Covers the biometric measurement layer well. Standardizes how HRV is represented, how sleep stages are tagged, how physical activity is quantified. **But no intervention schema.** Tells you what the body did, not what was done to the body or why. Metadata is about the measurement, not the therapeutic act.

## Neurotagging Gap

IEEE 1752 handles the biometric output layer. [[neurotagging]] adds the intervention input layer and the target mechanism layer. SRL's biometric data could be formatted per IEEE 1752 while carrying neurotagging metadata on top.

**Full text:** [IEEE 1752.1-2021](https://standards.ieee.org/ieee/1752.1/6982/)
