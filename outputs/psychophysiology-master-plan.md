# Psychophysiology Master Map — Execution Plan

**Version:** 1.0
**Status:** Approved by Randy 2026-04-16
**Owner:** Vigil (orchestrator)
**Scope:** Dissertation-scale literature review across all disciplines of psychophysiology, ingested into the SRL knowledge vault as durable substrate for future content and CE course creation.

---

## Grand ambition

Build a complete, evidence-chained, graph-connected map of what is known about psychophysiology across every contributing discipline. Randy will master the material and layer it into his embodied wisdom; the vault becomes the substrate for future NeuroMinutes, CE courses, white papers, and clinical LLM training data (Red Arrow 4).

Not for any single live deliverable. Optimize for durability, graph density, and evidence integrity.

---

## Scope — 30 disciplines, 3 tiers

Tier determines depth budget. Total enrichment budget is split roughly 70/20/10.

### Tier 1 — Central to SRL (full dissertation-chapter depth)

Direct feed into HRV-BF, Pausality, interoception, and the clinical LLM moat.

1. Autonomic neuroscience (incl. polyvagal)
2. Cardiovascular psychophysiology (HRV, RSA, baroreflex, resonance)
3. Respiratory psychophysiology (BOLT, Buteyko, pranayama, CO₂ tolerance)
4. Interoceptive neuroscience (Craig, Damasio, Critchley, Khalsa, Barrett)
5. Clinical psychophysiology (MAIA-2, biofeedback, HRV-BF, neurofeedback, AAPB)
6. Affective neuroscience (Panksepp, Barrett, LeDoux, Damasio)
7. Trauma neuroscience (Porges, van der Kolk, Levine, Schore, Ogden)
8. Stress neuroendocrinology (Selye, McEwen, HPA, allostatic load)
9. Contemplative neuroscience (Davidson, Lutz, Goyal, Kabat-Zinn)

### Tier 2 — Supporting (half-chapter depth)

Important adjacent context, not SRL's home ground.

10. Cognitive neuroscience
11. Embodied cognition / enactivism (Varela, Thompson, Noë)
12. Predictive processing / active inference (Friston, Clark, Seth)
13. Sleep / chronobiology
14. Exercise physiology
15. Pain psychophysiology (Moseley, central sensitization)
16. Health psychology / behavioral medicine
17. Placebo & mind-body medicine (Benson, Kaptchuk, expectancy)
18. Wearables / digital psychophysiology (emerging)
19. Psychophysics of time, space, self (Wittmann already deep, bridge out)

### Tier 3 — Survey depth (orientation only)

Know it exists, map key figures, flag seminal work, create one MOC.

20. PNI / immunology
21. Developmental psychobiology / attachment (Ainsworth, Schore)
22. Social psychophysiology / dyadic coregulation (Decety, Rilling, Feldman)
23. Psychopathology psychophysiology (anxiety/depression/PTSD markers)
24. Pharmacology (psychedelics, anxiolytics, anesthesia)
25. Philosophy of mind (IIT, HOT, global workspace)
26. Psychosomatics history (Alexander, Dunbar, Chicago Institute)
27. Cybernetics & systems theory (Wiener, Bateson, Ashby)
28. Somatic psychotherapy (Reich, Lowen, Gendlin, Hakomi)
29. Body-cultivation traditions (yoga, qigong, tai chi, Feldenkrais — textual/lineage)
30. Psychophysiological methods (EEG, fMRI, fNIRS, MEG, peripheral measures)

### Bridging spines (cross-cutting themes, not disciplines)

Organizing threads that cut across tiers. Phase 4 synthesis work is organized around these.

- **Interoception spine** — autonomic → affective → contemplative → clinical → trauma
- **Allostasis spine** — stress neuroendocrinology → cardiovascular → health psychology → developmental
- **Predictive processing spine** — cognitive → affective → interoceptive → philosophy
- **Embodiment spine** — enactivism → somatic traditions → developmental → phenomenology
- **Regulation spine** — autonomic → clinical → contemplative → trauma → wearables

---

## 5-phase execution

### Phase 0 — Scoping alignment (this plan doc)

- Output: this document
- Cost: ~10k tokens
- Status: **Complete (2026-04-16)**

### Phase 1 — Corpus audit (data-driven, no vault writes)

One pass through existing 176 concepts, 523 evidence, 341 observations. Tag each by discipline(s). Produce gap-scored matrix.

- Output: `outputs/psychophysiology-corpus-audit.md`
- Method: MCP `list_concepts`, `search_by_subject` per discipline, `search_vault` for key figures; Obsidian CLI for graph stats
- Cost: ~30k tokens, one session
- Deliverable: per-discipline coverage matrix with (existing concepts, existing evidence, existing observations, gap score 0–10, canonical-text coverage %)
- Rule applied: `feedback_data_driven_first` — data first, then ask

### Phase 2 — Discipline dossiers (lightweight planning docs, 30 × small)

For each discipline write a dossier holding:
- Working definition (2-3 sentences)
- Sub-questions / chapter outline (5-10 items)
- Existing vault coverage from Phase 1
- Canonical reading list (seminal texts + 2024-2026 papers)
- Gap list
- Tier confirmation
- Status field

- Output: `outputs/psychophysiology-dossiers/<slug>.md` (one per discipline)
- Cost: ~80-120k tokens total, 4-6 sessions
- Deliverable: 30 dossiers. No vault writes yet.

Dossiers are planning artifacts. Every Phase 3 session on a discipline starts by reading its dossier (~3k tokens), never the vault.

### Phase 3 — Per-discipline deep enrichment (the bulk of the work)

For each discipline, following its dossier:

1. Commission literature scan (delegate to `_bots/knowledge-miner/`)
2. Verify DOIs (delegate to `_bots/citation-resolver/`)
3. Create/enrich evidence notes (delegate to `_bots/vault-writer/`)
4. Create/enrich concept notes (vault-writer, with SRL-original vs. scientific filter per `feedback_concept_boundaries`)
5. Wire SKOS relations (`skos:broader`, `skos:narrower`, `skos:related`)
6. Build discipline MOC at completion
7. Commit with lab-notebook message (action: what — why/context)

Per-discipline session structure:
- Session start: read dossier + last handoff note
- Delegate bot work
- Synthesis (orchestrator holds the picture)
- Update dossier status
- Write handoff note
- Commit

- Output: evidence/, concepts/, observations/ notes + `Maps/psychophysiology-<discipline>.md`
- Cost: ~600-800k tokens total, ~16 full sessions for Tier 1 + batch sessions for Tier 2/3
- Tier 1: one discipline per session (9 sessions)
- Tier 2: two disciplines per session (5 sessions)
- Tier 3: three-four disciplines per session (3-4 sessions)

### Phase 4 — Cross-cutting synthesis

Organized around the 5 bridging spines. One synthesis session per spine.

- Output: `Maps/psychophysiology-spine-<name>.md` × 5
- Cost: ~50k tokens, 3-5 sessions
- Deliverable: intellectual lineage, where fields disagree, where SRL sits

### Phase 5 — Master MOC + gap report

Reader's entry point to the whole map.

- Output: `Maps/psychophysiology-master-map.md` (living doc, versioned)
- Output: `outputs/psychophysiology-final-gap-report.md` (what's still thin after all the work — feeds future sessions)
- Cost: ~10k tokens, 1 session

---

## Token-efficiency protocol

Randy's explicit constraint. These rules are binding on every future session.

1. **One big audit, then reference.** Phase 1 artifact is read by every subsequent session. Vault is not re-walked.
2. **Dossier-first, never fresh.** Every Phase 3 session starts by reading a ~3k-token dossier, not the vault.
3. **Bots do IO, Vigil does synthesis.** Knowledge-miner pulls literature; vault-writer writes notes; citation-resolver verifies DOIs. Vigil stays in orchestration and bridging.
4. **Batch writes.** 10+ evidence notes per bot run, never one at a time.
5. **Obsidian CLI for graph queries.** `orphans`, `unresolved`, `backlinks` — zero-overhead vs. grep.
6. **Committed = frozen.** Once a dossier/MOC is committed, reference by path, never re-summarize.
7. **Per-session handoff note.** Each session ends with a 1-paragraph state-of-the-map committed to `outputs/psychophysiology-map-progress.md`. Next session picks up cold.
8. **Extraction reports, not raw pulls.** Read bot outputs in `outputs/extractions/`, not source transcripts.

---

## Decisions locked

- **Tier allocation:** T1 70% / T2 20% / T3 10% of total enrichment budget
- **Pacing:** 90% serialized (one discipline per session for T1, batched for T2/T3), 10% opportunistic when other work intersects
- **Live deliverable dependencies:** none (substrate build)
- **Architecture:** no structural vault changes; files only within existing `concepts/`, `evidence/`, `observations/`, `Maps/`, `outputs/`
- **Clinical interpretations:** default "Pending review" per existing rule; may add batch-review mechanism if volume demands
- **All vault writes through MCP tools or vault-writer bot.** Never direct Writes to `concepts/`, `evidence/`, `observations/`, `audiences/`

---

## Decisions deferred

- **Canonical vs. emerging weighting:** decide after Phase 1 shows where vault is thin
- **Batch-review mechanism for clinical interpretations:** decide when Phase 3 volume hits ~100 new evidence notes without Randy-review
- **Opportunistic 10% allocation policy:** decide as other work (Huberman outreach, S.T.E.P. 2.0, CE sessions 8-14) surfaces intersections

---

## Red arrow alignment

- **Arrow 4 (Enterprise Data → Clinical LLM Moat):** primary beneficiary. The master map is the substrate a domain-specific LLM would train on.
- **Arrow 5 (Platform + CEU → $1M ARR):** secondary beneficiary. CE course content sources from this map.
- **Arrows 1-3:** indirect credibility layer.

If a phase or discipline stops advancing an arrow, re-scope.

---

## Handoff protocol

Every session touching this work ends with:

1. Update dossier status fields for any discipline worked
2. Commit with lab-notebook message
3. Append 1-paragraph state-of-the-map to `outputs/psychophysiology-map-progress.md`
4. Identify next session's target discipline

Every session starts with:

1. Read this plan doc
2. Read `outputs/psychophysiology-map-progress.md` tail
3. Read target discipline's dossier (if Phase 3+)
4. Execute

---

## Next session

**Phase 1 — Corpus audit.** Single session, ~30k tokens. Produces the gap-scored discipline matrix that unlocks every downstream decision.

Randy does not need to do anything between now and the next session. When he opens the next one, he says "Phase 1" and Vigil executes.
