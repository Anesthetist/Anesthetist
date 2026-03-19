# Needs Review — Randy's Queue

Items flagged by the extraction pipeline that need Randy's clinical judgment, interpretation, or verification.

## Clinical Interpretations Needed

*Items where extracted content suggests a clinical interpretation but only Randy can provide it*

- [ ] **gap-moment-detection-engine** — clinical_interpretation pending; Randy to validate detection thresholds (HRV drop >10ms, resp spike >4bpm)
- [ ] **neurotagging** — clinical_interpretation pending; Randy to confirm metadata schema priorities
- [ ] **diaphragmatic-literacy** — clinical_interpretation pending; Randy to validate definition against clinical practice
- [ ] **somnistics-readiness-battery** — clinical_interpretation pending; Randy to validate five competency domains and performance tiers
- [ ] **gap-moment-literacy** — clinical_interpretation pending; Randy to validate state classification categories

## Enrichments Needing Manual Application

*The vault-writer bot was denied update_note permission. These enrichments need manual application.*

- [ ] **somnistics** — Add PubMed-tightened definition (v1.1), Three Pillars formulation, "What Somnistics Is NOT" boundary language, state attractor model, platform architecture (NeuroFlow Platform four layers). Source: somnistics-definition-request-extraction and multi-phase-interoceptiv-analysis-extraction
- [ ] **somnistics** — Add JTBD statements: (1) "When the user faces intense and emotionally charged challenges..." (2) "When patients require the user to be at their absolute best..." Source: anterocept-spectrum-overview-extraction
- [ ] **gap-moment-training** — Add Randy's canonical definition: "A structured way of using micro-transitions as the primary training surface..." Source: somnistics-definition-request-extraction
- [ ] **neurominute** — Add Randy's canonical definition: "A 60-second, metadata-tagged micro-intervention that combines breath, attention, and multimodal cues..." Source: somnistics-definition-request-extraction
- [ ] **anterocept** — Add heart rate as "minimum effective sensor" philosophy. Source: anterocept-spectrum-overview-extraction

## Evidence Needing Verification

*Studies or papers mentioned without enough citation detail to create a proper evidence note*

- [ ] **Thayer & Lane (2009)** — "A model of neurovisceral integration in emotion regulation and dysregulation" — cited as Journal of Affective Disorders 61(3), 201-216 but year/journal combination may be incorrect. Needs PubMed verification before creating evidence note
- [ ] **Damasio (1999)** — "The Feeling of What Happens" — vault already has damasio-1996-somatic-marker (different work). Verify if this book needs a separate note

## Concept Boundary Questions

*Cases where two extractions might be the same concept, or where a concept's scope is unclear*

- [ ] **Interoceptive Flow OS** — ChatGPT proposed this name; Randy used it without objection but did not explicitly coin it. Is this an adopted concept name or just marketing language? Source: multi-phase-interoceptiv-analysis-extraction
- [ ] **Neuroadaptive Training System** — Randy classifies as "System architecture" type in his concept catalog. Is this a vault concept or better suited to a product architecture document? Source: anterocept-spectrum-overview-extraction
- [ ] **Micro-Interoceptive Regulation** — The operational verb for what Somnistics does. Better as a standalone concept or an enrichment to the somnistics definition? Recommendation: enrichment. Source: somnistics-definition-request-extraction
- [ ] **Bio-Adaptive Stress Reset** — ChatGPT marketing language, not Randy's coined term. Likely skip. Source: anterocept-spectrum-overview-extraction
- [ ] **Somnistics Certified Professional (SCP)** — Randy to confirm naming convention and Bronze/Silver/Gold/Platinum tier structure. Source: somnistics-definition-request-extraction

## Concept Boundary Decisions — Developmental / Epistemological Layer (2026-03-18)

*External frameworks Randy uses extensively. Do they get concept notes or stay as evidence-only references?*

- [ ] **Kegan Developmental Stages (3-5)** — Academic scaffolding mapped to SRL's developmental model and neurophysiology. 4+ conversations reference it. Recommendation: evidence note (already being created), with key mappings captured as enrichments to existing concepts.
- [ ] **Spiral Dynamics** — Used for SRL positioning ("Tier 2 for Tier 1"). Recommendation: evidence note, enrichment to somnistics concept.
- [ ] **Springett Consciousness Stairway (9-stage model)** — External framework but deeply integrated into Stairway Meta-Awareness Protocol. Recommendation: captured within the protocol concept, not standalone.
- [ ] **Springett Ice→Steam Model** — Kundalini as transformative continuum. Recommendation: evidence note enrichment, not standalone concept.
- [ ] **Did 5-Minute Miracle influence NeuroMinute design?** — Miners flagged the parallel. Randy to confirm lineage.

## Personal/Private Observations — Requires Randy Permission

- [ ] **Mother relationship observation** — Flagged as potentially too personal. From kundalini extraction.
- [ ] **Intergenerational case-control parallel** — Personal family pattern. From kundalini extraction.

## Other Flags

*Anything else the bots couldn't resolve autonomously*

- [ ] **Patent evidence notes** — Three patents identified (Solace US 11,090,459 B2, Phoeb-X US 11,779,275 B2, Brain.fm US 7,674,224 B2). Decision needed: create evidence notes or track in separate IP register?
- [ ] **Pausality code review observation** — Operationally significant but potentially sensitive (includes engineering grades, cost figures). Randy to decide if this belongs in the research vault. Source: multi-phase-interoceptiv-analysis-extraction
- [ ] **VagalBeats** — Referenced as product alongside Pausality. Is it a concept worth tracking or a deprecated product name?
- [ ] **Somnistics Definition upgrade** — The PubMed-tightened definition is arguably more precise than the current canonical definition. Randy to decide whether to upgrade
- [ ] **"One breath is likely the minimum effective dose of therapy"** — Powerful Randy quote. Should be captured in somnistics or minimum-effective-dose note
- [ ] **State attractor names** — "Hyperarousal, hypoarousal, cognitive tunnel, dyspneic panic loops" as named suboptimal attractors. Could each become concept stubs or be listed in state-transition
- [ ] **Jared Bruder and Jason Fields** — Named as curriculum collaborators. Should they be tracked as contributors in the vault?
