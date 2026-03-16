---
created: '2026-03-14'
creator: Randy Graybeal
dc:subject:
- evidence-classification
- OCEBM
- metadata-updates
- evidence-quality
- gap-moment-training
id: urn:srl:output:gmt-evidence-chain-level-of-evidence-updates
modified: '2026-03-14'
output_type: changelog
status: draft
target_audience: internal
title: 'GMT Evidence Chain: Level of Evidence Classification and Proposed Metadata
  Updates'
type: output
---

# GMT Evidence Chain: Level of Evidence Classification

**Purpose:** Proposed metadata updates to each `prov:wasDerivedFrom` evidence note in the SRL vault, adding `evidence_level` and `evidence_quality_notes` fields.

## Classification Framework

Levels follow a modified Oxford Centre for Evidence-Based Medicine (OCEBM) hierarchy:

| Level | Description | Sources in Chain |
|-------|-------------|-----------------|
| **1b** | Individual RCT | Shalev 2012, Balban 2023 |
| **2a** | Systematic review of cohort/mechanistic studies | Zaccaro 2018 |
| **2b** | Individual cohort or mechanistic study | Lehrer 2000, Prinsloo 2011, Dillard 2023, Paul 2007, Putnam 2025 |
| **3** | Narrative review / integrative review | Brosschot 2006, McEwen 2007, Sezer 2025, Horvath 2021 |
| **4** | Qualitative / phenomenological research | Ehmann 2025 (mental health), Ehmann 2025 (cognition) |
| **5** | Expert opinion, books, theoretical frameworks | Porges 2011, Van der Kolk 2014, Vervaeke 2019, Iyengar 1981, Marcucci 2007, Ruskin 2015, Burchard 2017 |

## Proposed Updates Per Evidence Note

### Level 1b — Randomized Controlled Trials

**Shalev 2012** (`shalev-2012-ptsd-prevention`)
- Add `evidence_level: 1b`
- Add `evidence_quality_notes:` RCT in Archives of General Psychiatry (now JAMA Psychiatry). Strongest individual study in the GMT evidence chain. Directly tests early intervention timing.

**Balban 2023** (`balban-2023-cyclic-sighing`)
- Add `evidence_level: 1b`
- Add `evidence_quality_notes:` RCT from Stanford (Huberman + Spiegel labs) in Cell Reports Medicine. N=108, 1-month, ClinicalTrials.gov registered. Strongest direct evidence that brief exhale-focused breathing outperforms mindfulness meditation.

### Level 2a — Systematic Reviews

**Zaccaro 2018** (`zaccaro-2018-breathing-systematic-review`)
- Add `evidence_level: 2a`
- Add `evidence_quality_notes:` Systematic review of 15 studies in Frontiers in Human Neuroscience. Strongest aggregate evidence for breathing mechanism. Reviewed studies primarily mechanistic/cohort, not RCTs.

### Level 2b — Individual Mechanistic/Cohort Studies

**Lehrer 2000** (`lehrer-2000-resonance-frequency`) — `evidence_level: 2b`. Foundational protocol paper, 1000+ citations.

**Prinsloo 2011** (`prinsloo-2011-hrv-biofeedback-immediate`) — `evidence_level: 2b`. Small sample, clean design. Key: immediate single-session effects.

**Dillard 2023** (`dillard-2023-slow-breathing-vr`) — `evidence_level: 2b`. Objective biomarker (salivary alpha-amylase). MDPI journal — solid but not top-tier.

**Paul 2007** (`paul-2007-breathing-instruction-anxiety`) — `evidence_level: 2b`. Medical student population. Medical Education journal.

**Putnam 2025** (`putnam-2025-anesthesiology-stress-snapshot`) — `evidence_level: 2b`. Cross-sectional survey, descriptive. 83% stress incidence, 20% catastrophic.

### Level 3 — Narrative/Integrative Reviews

**Brosschot 2006** (`brosschot-2006-perseverative-cognition`) — `evidence_level: 3`. ~2000+ citations. Theoretical framework with strong subsequent validation.

**McEwen 2007** (`mcewan-2007-allostatic-load-brain`) — `evidence_level: 3`. Physiological Reviews (IF ~30+). Bruce McEwen was the leading authority. Extremely high credibility.

**Sezer 2025** (`sezer-2025-meditation-autonomic-nervous-system`) — `evidence_level: 3`. Recommend `dc:type` update from `journal-article` to `review`. Missing DOI — verify and add.

**Horvath 2021** (`horvath-2021-srna-pandemic-burnout`) — `evidence_level: 3`. AANA Journal — strategic value for target audience.

### Level 4 — Qualitative/Phenomenological

**Ehmann 2025 mental health** (`ehmann-2025-mental-health-advanced-meditators`) — `evidence_level: 4`. ⚠️ PREPRINT (OSF). N=28 qualitative. Monitor for journal acceptance.

**Ehmann 2025 cognition** (`ehmann-2025-mindfulness-cognition-ltm`) — `evidence_level: 4`. Published in Imaging Neuroscience. Missing DOI — verify and add.

### Level 5 — Books, Lectures, Theoretical Frameworks

**Porges 2011** — `evidence_level: 5`. Book. Theory extensively peer-reviewed elsewhere. Note academic criticism (Grossman 2017, Taylor 2022).

**Van der Kolk 2014** — `evidence_level: 5`. Book. Underlying research is peer-reviewed. Cite individual papers for scientific claims.

**Vervaeke 2019** — `evidence_level: 5`. ⚠️ LECTURE SERIES. Supplement with peer-reviewed papers (Vervaeke & Ferraro 2013; Vervaeke & Lillicrap 2012).

**Iyengar 1981** — `evidence_level: 5`. Foundational pranayama text. Techniques subsequently validated by Zaccaro, Kim, Balban, Lehrer.

**Marcucci 2007** — `evidence_level: 5`. Clinical reference. Error patterns map to Six Error Archetypes.

**Ruskin 2015** — `evidence_level: 5`. Clinical reference. Used as visualization scenario library.

**Burchard 2017** — `evidence_level: 5`. Popular press. Proto-gap moment. Prior art reference.

## Recommended Actions

1. Add DOIs to Sezer 2025 and Ehmann 2025 (cognition)
2. Monitor Ehmann 2025 (mental health preprint) for journal acceptance
3. Supplement Vervaeke with peer-reviewed papers
4. Note polyvagal criticism in Porges entry
5. Seek Level 1a source: systematic review of breathing interventions for healthcare worker resilience
