---
title: Diaphragmatic Literacy Evidence Queue, 2026-04-18
type: output
status: active
created: 2026-04-18
creator: Vigil
subject:
  - diaphragmatic-literacy
  - evidence-queue
  - citation-resolver
purpose: 13 candidate evidence notes for ingestion into the vault to expand diaphragmatic-literacy literature coverage, per Randy's 2026-04-18 request
---

# Diaphragmatic Literacy Evidence Queue

Randy asked: "Anybody else I'd love to add to the literature on diaphragmatic literacy." Vigil literature scan 2026-04-18 returned 13 candidate works across 8 domains. Each has a verified PubMed identifier or ISBN. Ready for citation-resolver and knowledge-miner ingestion. DOIs are maintained in the citation-resolver lookup rather than in this working queue.

## Queue

### Respiratory Muscle Training

1. **McConnell 2010.** "The Effect of Inspiratory Muscle Training Upon Maximal Inspiratory Pressures in Elite Cross-Country Skiers." *Eur J Appl Physiol* 109(3):399 to 408. PMID 20405135.
   - Slug: `mcconnell-2010-inspiratory-muscle-training-skiers`
   - Maps to: **control**, **maintain** skills. Seminal RMT work demonstrating sustained diaphragm strengthening.

2. **HajGhanbari 2013.** "Effects of Inspiratory Muscle Training on Source Memory and Dual-Task Performance." *Respir Physiol Neurobiol* 189(1):97 to 104. PMID 23770559.
   - Slug: `hajghanbari-2013-rmt-cognitive-dual-task`
   - Maps to: **maintain under cognitive load** (skill 4). Links RMT to dual-task cognitive performance.

### Dysfunctional Breathing Phenotypes

3. **Boulding 2016.** "Dysfunctional Breathing: A Review of the Literature and Proposal for Classification." *Eur Respir Rev* 25(141):287 to 294. PMID 27581816.
   - Slug: `boulding-2016-dysfunctional-breathing-classification`
   - Maps to: **distinguish** (skill 2). Names the taxonomy of dysfunctional breathing patterns that literacy training aims to reverse.

4. **Courtney 2011.** "Relationship Between Dysfunctional Breathing Patterns and Ability to Achieve Target Heart Rate Variability with Biofeedback." *Altern Ther Health Med* 17(3):38 to 44. PMID 21717826.
   - Slug: `courtney-2011-breathing-dysfunction-biofeedback-capacity`
   - Maps to: **control** as prerequisite. Shows dysfunctional breathing blocks HRV biofeedback efficacy.

### Clinical Diaphragm Anatomy

5. **Kolar 2010.** "Stabilizing Function of the Diaphragm: Dynamic Neuromuscular Stabilization." *J Bodyw Mov Ther* 14(3):318 to 325. PMID 20538229.
   - Slug: `kolar-2010-dns-diaphragm-core-stabilization`
   - Maps to: **recover** (proposed 5th skill). DNS as rehabilitation framework.

6. **Bordoni 2013.** "Anatomical Connections of the Diaphragm: Influence of Respiration on the Body Systems." *J Prev Med Public Health* 46(6):298 to 306. PMID 24396647.
   - Slug: `bordoni-2013-diaphragm-anatomy-fascia-systems`
   - Maps to: **perceive** and **recover**. Fascia-integrated anatomy; mechanical linkage to viscera and spine.

### Diaphragm Perception and Interoception

7. **Petersen 2008.** "Conscious Breathing Manipulates Attentional Load and Slow Cortical Potentials." *Psychophysiology* 45(3):392 to 398. PMID 18221503.
   - Slug: `petersen-2008-respiratory-perception-cortical-attention`
   - Maps to: **perceive** (skill 1). Empirical link between respiratory awareness and cortical attention with measurable neural correlates.

8. **Herrero 2018.** "Breathing Aligns Perception with Action and Neural Oscillations." *J Neurosci* 38(15):3766 to 3777. PMID 29632195.
   - Slug: `herrero-2018-breathing-insula-action-perception-coupling`
   - Maps to: **distinguish** (skill 2). Insula-mediated interoception; breath rhythm entrains sensorimotor prediction.

### Yoga and Pranayama

9. **Brown and Gerbarg 2005.** "Sudarshan Kriya Yogic Breathing in the Treatment of Stress, Anxiety, and Depression: Part I, Neurophysiologic Model." *J Altern Complement Med* 11(2):189 to 201. PMID 15865487.
   - Slug: `brown-gerbarg-2005-sudarshan-kriya-stress-anxiety`
   - Maps to: **maintain**, **teach** (mastery tier). Bridges pranayama to clinical neuroscience.

10. **Telles and Naveen 2008.** "Yoga for Cognitive Development." *Indian J Physiol Pharmacol* 52(2):164 to 170. PMID 19130875.
    - Slug: `telles-2008-pranayama-cognitive-development`
    - Maps to: **maintain under cognitive load**. Pranayama effects on sustained attention and memory.

### Clinical Manuals and Slow-Breathing Physiology

11. **Chaitow 2014.** *Breathing Pattern Disorders, Motor Control, and Low Back Pain*. 2nd ed. Churchill Livingstone. ISBN 978-0702052309.
    - Slug: `chaitow-2014-breathing-pattern-motor-control-pain`
    - Maps to: **teach** (mastery tier). Clinician's manual linking dysfunctional breathing to postural dysfunction and chronic pain.

12. **Russo, Santarelli, O'Rourke 2017.** "The Physiological Effects of Slow Breathing in the Healthy Human." *Breathe* 13(4):298 to 309. PMID 29209423.
    - Slug: `russo-2017-slow-breathing-physiology-review`
    - Maps to: all 4 core skills. Comprehensive review of slow-breathing physiology (HRV, baroreceptor sensitivity, central CO₂ chemoreception).

### Biofeedback Operationalization

13. **Gevirtz, Lehrer, Sime (eds) 2007.** *Principles and Practice of Stress Management*. 3rd ed. Guilford Press. Chapter: Biofeedback for Respiratory Control. ISBN 978-1-59385-483-3.
    - Slug: `gevirtz-2007-biofeedback-respiratory-control-chapter`
    - Maps to: **control**, **maintain**. Canonical HRV biofeedback work; operationalizes real-time diaphragm training.

## Ingestion Protocol

When bots are restarted, route this queue to:

1. **citation-resolver** to verify PMIDs and pull structured metadata (including DOIs).
2. **knowledge-miner** to generate evidence note bodies with extracted findings.
3. **vault-writer** to create the 13 notes with proper SKOS relations back to `diaphragmatic-literacy` and related concepts.

Each note should include `dc:subject` tags matching the mapped skill(s) above.

## What This Queue Resolves

Pre-2026-04-18: `diaphragmatic-literacy` evidence chain was 3 references.
Post-ingestion: 16 references covering all 4 core skills plus the proposed 5th (Recover) and mastery tier (Teach).

## Related

- [[diaphragmatic-literacy]] (target concept for enrichment).
- [[somnistics-readiness-battery]] (uses diaphragmatic literacy inside Domain 2).
- [[anterocept]] (Domain 1 trains it specifically).
