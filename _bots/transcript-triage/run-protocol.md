<!-- v1.0 — initial creation 2026-03-15 -->
# Transcript Triage Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/transcript-triage/soul.md` — internalize the persona
2. Read `_bots/transcript-triage/taxonomy.md` — know the categories
3. Read `_bots/transcript-triage/patterns.md` — load accumulated heuristics from prior runs
4. Read `_bots/transcript-triage/learning-log.md` — know what was learned last time
5. Run `mcp__srl-vault__list_concepts` — know what concepts already exist
6. Run `mcp__srl-vault__search_by_status` for "draft" — know which concepts are thin and need enrichment
7. Check if `outputs/extraction-queue.md` exists — if resuming, pick up where you left off

## Execution Steps

### Step 1: Inventory

```bash
ls sources/chatgpt/*.md | wc -l
```

Get the full file list with metadata:
```bash
cd sources/chatgpt && for f in *.md; do
  chars=$(grep "^char_count:" "$f" | head -1 | sed 's/char_count: //')
  msgs=$(grep "^message_count:" "$f" | head -1 | sed 's/message_count: //')
  date=$(grep "^created:" "$f" | head -1 | sed 's/created: //')
  title=$(grep "^title:" "$f" | head -1 | sed 's/title: //' | tr -d '"')
  echo "$chars|$msgs|$date|$title|$f"
done | sort -rn
```

### Step 2: Batch Scan

Process files in batches of 50. For each file:

1. **Read frontmatter** — extract metadata fields
2. **Read first 100 lines** — capture Randy's opening prompt and ChatGPT's initial response
3. **Classify** — assign primary + secondary categories per taxonomy.md
4. **Score** — apply priority scoring rubric from skills.md
5. **Map targets** — for files scoring 7+, list vault nodes that would benefit

### Step 3: Build Queue

Sort all scored files by priority (descending). Output format:

```markdown
## Priority 9-10 (Must Extract)

| File | Score | Category | Chars | Msgs | Target Nodes | Notes |
|------|-------|----------|-------|------|-------------|-------|
| multi-phase-interoceptiv-analysis.md | 10 | clinical | 383K | 35 | multi-phase-interoceptive-coupling | Novel concept development |
```

### Step 4: Build Manifest

Complete inventory with all files, including low-priority ones:

```markdown
| File | Score | Primary Category | Secondary | Chars | Msgs | Date | Status |
|------|-------|-----------------|-----------|-------|------|------|--------|
```

Status values: `queued` | `in-progress` | `extracted` | `skip`

### Step 5: Duplicate Clustering

Group files that cover the same topic:
```markdown
## Topic Clusters (Potential Duplicates)

### Somnistics Definition
- somnistics-definition-request.md (186K, 2025-09-15) — PRIMARY
- somnistics-definition-refinement.md (108K, 2025-10-02) — refinement
- somnistics-definition-summary.md (6K, 2025-10-15) — summary
- somnistics-framework-explanation.md (12K, 2025-11-01) — explanation
→ Mine PRIMARY first; others are supplementary
```

### Step 6: Post-Run Summary

Report to user:
- Total files scanned
- Distribution by category
- Top 20 highest-priority files with one-line descriptions
- Number of duplicate clusters identified
- Recommended first batch for knowledge-miner

## Batch Processing

If running incrementally (not all 861 at once):
- Process 50 files per invocation
- Append results to existing queue/manifest
- Track progress: "Scanned X of 861 (Y%)"
- Always process highest-char-count files first (more content = more to classify)

## Step 7: Run Retrospective

After completing the batch, execute the retrospective protocol per `_bots/transcript-triage/retrospective.md`:
1. Answer the five reflection questions
2. Append retrospective entry to `learning-log.md`
3. Update `patterns.md` with any new heuristics discovered
4. Adjust scoring weights in `skills.md` if calibration data warrants it
5. Increment version comment at top of this file

## Error Handling

- If a file has no frontmatter, note it as "malformed" and skip
- If a file is empty, mark as "empty" with score 0
- If char_count is missing, estimate from file size
