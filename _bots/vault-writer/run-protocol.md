<!-- v1.0 — initial creation 2026-03-15 -->
# Vault Writer Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/vault-writer/soul.md` — internalize the persona
2. Read `_bots/vault-writer/skills.md` — know the tools and rules
3. Read `_bots/vault-writer/quality-gates.md` — know the decision rules
4. Read `_bots/vault-writer/learning-log.md` — know what was learned from prior runs
5. Read `_schema/note-types.yaml` — know required fields
6. Read the extraction report to process from `outputs/extractions/`
7. Check `outputs/vault-write-log.md` for recent writes to avoid duplicates

## Execution Steps

### Step 1: Load Extraction Report

Read the extraction report produced by the knowledge-miner:
```
outputs/extractions/{source-slug}-extraction.md
```

Parse all candidates: new concepts, enrichments, evidence, observations, relationships.

### Step 2: Process New Concept Candidates

For each new concept candidate:

1. **Duplicate check:**
   - `mcp__srl-vault__search_vault` with title
   - `mcp__srl-vault__search_vault` with slug
   - `mcp__srl-vault__search_vault` with 2-3 key terms
   - If duplicate found → convert to enrichment, skip creation

2. **Schema validation:**
   - Verify all required fields per `_schema/note-types.yaml`
   - Verify URN format: `urn:srl:concept:{slug}`
   - Verify slug is kebab-case
   - If validation fails → flag in needs-review, skip creation

3. **Create note:**
   ```
   mcp__srl-vault__create_note
     note_type: concept
     slug: {slug}
     frontmatter: {validated JSON}
     body: {markdown content}
   ```

4. **Wire relationships:**
   - For each `skos:broader` → `mcp__srl-vault__add_skos_relation`
   - For each `skos:related` → `mcp__srl-vault__add_skos_relation`
   - For each `prov:wasDerivedFrom` evidence → `mcp__srl-vault__add_evidence_link`

5. **Log the action**

### Step 3: Process Enrichment Candidates

For each enrichment:

1. **Read existing note:** `mcp__srl-vault__get_note`
2. **Identify genuinely new content** — skip anything already in the note
3. **Update frontmatter** if new fields needed: `mcp__srl-vault__update_note`
4. **Add evidence links:** `mcp__srl-vault__add_evidence_link`
5. **Add SKOS relations:** `mcp__srl-vault__add_skos_relation`
6. **Log the action**

### Step 4: Process Evidence Candidates

Same flow as concepts but with evidence-specific validation:
- Must have `dc:creator` and `dc:date`
- Must have `dc:identifier` (DOI, URL, ISBN) — if missing, flag for verification
- `dc:type` must be valid

### Step 5: Process Observation Candidates

Same flow but with observation-specific validation:
- Must have `observation_type`
- Should have `clinical_context` if available

### Step 6: Process Relationship Discoveries

For each discovered relationship:
1. Verify both concepts exist in vault
2. Check relationship doesn't already exist: `mcp__srl-vault__get_relationships`
3. Add via `mcp__srl-vault__add_skos_relation`
4. Log the action

### Step 7: Update Needs Review

Append to `outputs/needs-review.md` any items that:
- Failed validation and were skipped
- Need `clinical_interpretation` filled by Randy
- Had uncertain evidence citations
- Had ambiguous concept boundaries

### Step 8: Post-Run Summary

Report to user:
- Notes created (by type)
- Notes enriched
- Relationships added
- Items flagged for review
- Any errors encountered

## Error Handling

- If `create_note` fails (file exists), try `update_note` instead
- If a referenced concept doesn't exist for relationship wiring, log it and continue
- If MCP server is unreachable, stop and report — never fall back to direct file writes
- If an extraction candidate is ambiguous, err on the side of flagging rather than writing

## Step 9: Run Retrospective

After completing the write batch, execute the retrospective protocol per `_bots/vault-writer/retrospective.md`:
1. Calculate acceptance/rejection metrics
2. Analyze schema compliance patterns
3. Assess duplicate detection effectiveness
4. Produce feedback for the knowledge-miner (append to `_bots/knowledge-miner/learning-log.md`)
5. Append retrospective entry to `_bots/vault-writer/learning-log.md`
6. Update `quality-gates.md` if new validation rules are needed
7. Increment version comment at top of this file
