# Extraction Coordinator Bot — Run Protocol

<!-- v1.0 — initial creation 2026-03-15 -->

## Pre-Run Checklist

1. Read `_bots/extraction-coordinator/soul.md`
2. Read `_bots/extraction-coordinator/progress.md` — know current state
3. Read `_bots/extraction-coordinator/learning-log.md` — know system-level trends and Randy's feedback history
4. Check if `outputs/extraction-queue.md` exists:
   - If NO → run the transcript-triage bot first
   - If YES → proceed to batch processing

## Execution Steps

### Step 1: Load State

Read `progress.md` to determine:
- How many files have been processed
- What the next file in the queue is
- Any errors or flags from previous runs

### Step 2: Select Batch

From `outputs/extraction-queue.md`, select the next N files (default: 10):
- Skip files already marked as `extracted` in progress.md
- Process in priority order (highest score first)

Report the batch to the user:
```
Processing batch: files {X} through {Y} of 861
Files in this batch:
1. multi-phase-interoceptiv-analysis.md (score: 10, clinical)
2. cognitive-emotional-state-interface.md (score: 9, clinical)
...
```

### Step 3: For Each File in Batch

#### 3a. Invoke Knowledge Miner

Read the source file and execute the knowledge-miner run-protocol:
- Read `_bots/knowledge-miner/soul.md`
- Read `_bots/knowledge-miner/run-protocol.md`
- Process the file per protocol
- Produce extraction report at `outputs/extractions/{slug}-extraction.md`

#### 3b. Invoke Vault Writer

Read the extraction report and execute the vault-writer run-protocol:
- Read `_bots/vault-writer/soul.md`
- Read `_bots/vault-writer/run-protocol.md`
- Process candidates per protocol
- Update `outputs/vault-write-log.md`
- Update `outputs/needs-review.md` if needed

#### 3c. Update Progress

Update `progress.md`:
- Mark file as `extracted`
- Record: concepts created, enriched, evidence added, observations added
- Note any errors or flags

### Step 4: Batch Summary

After processing all files in the batch, report:

```markdown
## Batch Summary — {date}

**Files processed:** {N} of 861 ({percentage}%)
**Cumulative progress:** {total processed} of 861

### This Batch
| Metric | Count |
|--------|-------|
| New concepts created | X |
| Existing concepts enriched | X |
| New evidence notes | X |
| New observations | X |
| SKOS relationships added | X |
| Evidence links added | X |
| Items flagged for review | X |
| Errors | X |

### Next Batch Preview
1. {next-file} (score: X, category)
2. {next-file} (score: X, category)
...

### Action Items for Randy
- {items from needs-review.md}
```

## Batch Sizing Guidelines

| Context | Batch Size | Reasoning |
|---------|-----------|-----------|
| First run (verification) | 3-5 | Validate pipeline works correctly |
| Normal operation | 10 | Good throughput, manageable review |
| Sprint session | 20-30 | When Randy has time to review a larger batch |
| Quick wins only | All files <20K chars | Fast extraction of small, single-concept files |

## Resume Protocol

When resuming after a break:
1. Read `progress.md` — find last completed file
2. Read `outputs/vault-write-log.md` — verify last writes succeeded
3. Read `outputs/needs-review.md` — check if Randy addressed any flags
4. Continue from the next unprocessed file in the queue

## Step 5: Invoke Review Accelerator

After the vault-writer completes and `outputs/needs-review.md` has new items:

1. Read `_bots/review-accelerator/soul.md` and `run-protocol.md`
2. Execute the review-accelerator protocol:
   - Auto-resolve Tier 1 items (citation lookups via citation-resolver, schema fixes)
   - Auto-resolve Tier 2 items with audit trail
   - Pre-draft Tier 3 items for Randy's quick review
   - Escalate Tier 4 items with full context
3. Produce `outputs/review-dashboard.md` for Randy
4. Report: "{N} items auto-resolved, {N} items ready for Randy's quick review, {N} escalations"

## Step 6: Run System Retrospective

After completing the batch, execute the retrospective protocol per `_bots/extraction-coordinator/retrospective.md`:
1. Update the pipeline health dashboard with this batch's metrics
2. Analyze cross-bot feedback signals (is each bot improving?)
3. Capture Randy's feedback on any reviewed items
4. After every 3 batches, conduct a full system review (protocol versions, pattern libraries, quality gate calibration)
5. Update `learning-log.md` with system health trend data
6. Adjust next batch plan based on what was learned
7. Increment version comment at top of this file

## Error Recovery

- If miner fails on a file → mark as `error` in progress.md, skip to next file
- If writer fails on a candidate → log error, continue with remaining candidates
- If MCP server is down → stop batch, report error, save state
- If a file is too large to process in one pass → split into segments, note in progress.md
