# Vault Writer Bot — Quality Gates

<!-- v1.1 — 2026-04-18 governance update: URN-only IDs, extraction_depth, prov semantics, duplicate-detection rigor, subjects.yaml vocabulary gate -->

## Governance Rules (load-bearing — never violate)

### ID Scheme (effective 2026-04-18)
- **Evidence IDs MUST use `urn:srl:evidence:{author-year-slug}`**
- **Concept IDs MUST use `urn:srl:concept:{slug}`**
- **Observation IDs MUST use `urn:srl:observation:{slug}`**
- **Instrument IDs MUST use `urn:srl:instrument:{slug}`**
- `EVD-YYYYMMDD-NNN` and any other date-sequence IDs are **deprecated**. If seen in the wild, flag for migration. Never emit a new one.

### Duplicate Detection (mandatory before any CREATE)
Run **at least four** vault searches before creating any new note:
1. `search_vault` with the proposed title
2. `search_vault` with the proposed slug
3. `search_vault` with 2–3 key terms from the content
4. `search_vault` with alternate phrasings (e.g. "non-technical" + "nontechnical", "CRNA" + "nurse anesthetist")

Narrow search coverage is the primary cause of duplicate records. If any search returns a candidate match, convert to enrichment.

### Subjects Vocabulary Gate
- `dc:subject` values MUST resolve to entries in `_schema/subjects.yaml` once that file exists.
- Until `subjects.yaml` ships, continue using existing tag conventions but prefer existing tags over coining new ones. Check `_index/by-subject.md` for live usage.

### Extraction Depth (effective 2026-05-01 for new notes)
- Every evidence note MUST carry `extraction_depth: abstract | partial | full`.
- `abstract` = title + abstract only.
- `partial` = abstract + key figures/tables/findings but not full methods or discussion.
- `full` = complete paper read.
- Backfill existing notes with `partial` (conservative default) during the next sweep.

### Provenance Link Semantics
- `prov:wasDerivedFrom` — the source directly supports the concept's claim. Use for primary citations.
- `prov:wasInformedBy` — the source informs or positions the concept interpretively but does not make the claim. Use for framing/context links.
- Do not use `wasDerivedFrom` for interpretive links. Overclaiming provenance damages evidence-chain integrity.

### Dublin Core Field Expectations (evidence)
- Required: `dc:creator`, `dc:date`, `dc:subject`, `dc:identifier`, `dc:type`, `extraction_depth`
- Strongly encouraged: `dc:isPartOf` (journal/book title), `dc:language`, `dc:rights`
- `dc:publisher` = publisher organization (e.g. "BioMed Central"), NOT the journal name. Journal goes in `dc:isPartOf`.
- `dc:relation` = URNs of parent instruments, prior versions, related works. Use when the paper validates an instrument, extends prior work, or is part of a series.

## Decision: Create vs. Update vs. Skip vs. Flag

```
Is this concept/evidence/observation already in the vault?
├── YES → Does the extraction add genuinely new content?
│   ├── YES → UPDATE (enrich the existing note)
│   └── NO → SKIP (log as "already covered")
└── NO → Does it meet the quality bar?
    ├── YES → CREATE (new vault note)
    └── NO → What's missing?
        ├── Missing required fields → FLAG for miner revision
        ├── Uncertain attribution → FLAG for Randy's review
        ├── Too thin (just a mention, not a concept) → SKIP
        └── Possible duplicate with different name → FLAG for review
```

## Quality Bar: Concepts

**Must have ALL of:**
- [ ] Clear definition (at least 2-3 sentences)
- [ ] At least one `dc:subject` tag
- [ ] At least one relationship to an existing vault concept
- [ ] At least one `prov:wasDerivedFrom` link (to source chat or evidence)
- [ ] Body content beyond just a definition (mechanism, evidence, clinical observation, or related concepts section)

**Nice to have:**
- Multiple evidence links
- Clinical observations from Randy's practice
- Cross-references to other vault concepts

## Quality Bar: Evidence

**Must have ALL of:**
- [ ] Author name(s)
- [ ] Year of publication
- [ ] Title (or reasonable approximation)
- [ ] At least one key finding relevant to SRL
- [ ] `dc:type` classification

**If missing `dc:identifier` (DOI/URL/ISBN):**
- Create the note anyway (with identifier field empty)
- Add to needs-review: "Evidence note {slug} needs DOI/URL verification"

## Quality Bar: Observations

**Must have ALL of:**
- [ ] Clear description of the pattern or knowledge
- [ ] `observation_type` classification
- [ ] Connection to at least one vault concept
- [ ] Attribution to Randy's clinical experience (not textbook knowledge)

**Reject if:**
- It's common clinical knowledge any CRNA would know
- It's a restatement of published evidence (should be an evidence note instead)
- It contains no specific clinical context

## Evidence Quality Thresholds

| Level | Description | Action |
|-------|-------------|--------|
| High | Full citation available (author, year, title, DOI) | Create immediately |
| Medium | Partial citation (author + year + key finding) | Create with flag for DOI lookup |
| Low | Vague reference ("studies show...") | Do NOT create — flag for verification |

## Enrichment Rules

When enriching an existing note:
- **Add, never replace** — append new evidence links, add new related concepts, extend body sections
- **Preserve existing content** — never overwrite Randy's existing text
- **Update `modified` date** — set to today
- **Increment version** — if the enrichment is substantial (new section, new evidence chain)
- **Don't touch `status`** — leave quality gate as-is; only Randy promotes notes

## Flagging Rules

Flag for Randy's review when:
1. A concept's clinical_interpretation field is empty and the extraction contains clinical content
2. An evidence citation can't be verified
3. Two extraction candidates might be the same concept with different names
4. A concept crosses disciplinary boundaries in ways that need clinical judgment
5. An observation contains potentially sensitive clinical details
