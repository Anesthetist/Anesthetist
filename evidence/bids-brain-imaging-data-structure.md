---
clinical_interpretation: Pending review
created: '2026-03-21'
creator: randy
dc:creator:
- Gorgolewski et al.
dc:date: '2016'
dc:identifier: https://bids.neuroimaging.io
dc:subject:
- neuroimaging
- data-standard
- metadata
- MRI
- eeg
- meg
dc:type: standard
id: urn:srl:evidence:bids-brain-imaging-data-structure
modified: '2026-03-21'
status: draft
title: BIDS — Brain Imaging Data Structure
type: evidence
---

# BIDS — Brain Imaging Data Structure

Gold standard for organizing neuroimaging data (MRI, EEG, MEG, fNIRS, motion capture). Rigorous file/folder naming conventions, JSON metadata sidecars, community-driven extension proposals (BEPs). Recent extensions: MRS-BIDS (spectroscopy, 2025), Motion-BIDS (2024).

## Relevance to SRL

BIDS organizes brain images but has **no schema for therapeutic interventions**. No concept of a "session protocol" tied to neurophysiological targets, no outcome tagging. If you ran a breathing protocol during an fMRI scan, BIDS would organize the brain images but have no structured way to tag what the protocol was, what it targeted, or what shift it produced.

## Neurotagging Gap

BIDS covers Layer 0 (data structure) but not the intervention ↔ target ↔ outcome triad that [[neurotagging]] addresses. Neurotagging is complementary — sits on top, does not compete.

**Full text:** [BIDS Specification](https://bids.neuroimaging.io)
