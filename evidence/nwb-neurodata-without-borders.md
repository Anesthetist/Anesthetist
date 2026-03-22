---
clinical_interpretation: Pending review
created: '2026-03-21'
creator: randy
dc:creator:
- Rubel et al.
dc:date: '2022'
dc:identifier: https://nwb.org
dc:subject:
- neurophysiology
- data-standard
- electrophysiology
- behavior
dc:type: standard
id: urn:srl:evidence:nwb-neurodata-without-borders
modified: '2026-03-21'
status: draft
title: NWB — Neurodata Without Borders
type: evidence
---

# NWB — Neurodata Without Borders

Standard for neurophysiology data — spike trains, calcium imaging, behavioral tracking. Includes a dedicated behavior module and flexible tagging system (neural, behavior, stim, external tags). Strong metadata requirements for each neurodata type.

## Relevance to SRL

Designed for lab neurophysiology, not therapeutic interventions. Can tag that a stimulus occurred, but no schema for "this was a 60-second resonant breathing protocol targeting vagal activation with an expected HR drop of 5-10 bpm." The behavioral module tracks behavior during experiments, not therapeutic dosing.

## Neurotagging Gap

NWB handles the raw neurophysiology data layer. [[Neurotagging]] adds the intervention protocol and outcome layers that NWB does not address.

**Full text:** [NWB Documentation](https://nwb.org)
