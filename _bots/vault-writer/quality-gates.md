# Vault Writer Bot — Quality Gates

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
