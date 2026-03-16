# Extraction Coordinator — Retrospective Protocol

## Purpose

The coordinator runs the meta-retrospective: evaluating how the entire pipeline is improving across runs. This implements the Data Flywheel pattern (Eugene Yan): measure → adjust → measure again. The coordinator owns the system-level view.

## Post-Batch Retrospective (Required after every batch)

### 1. Pipeline Health Dashboard

```markdown
## Pipeline Health — {date} — After Batch {N}

| Metric | Batch 1 | Batch 2 | ... | This Batch | Trend |
|--------|---------|---------|-----|-----------|-------|
| Triage accuracy (%) | | | | | ↑↓→ |
| Miner yield (candidates/file) | | | | | ↑↓→ |
| Writer acceptance rate (%) | | | | | ↑↓→ |
| End-to-end yield (vault notes/file) | | | | | ↑↓→ |
| Flags for Randy review | | | | | ↑↓→ |
| Errors | | | | | ↑↓→ |
| Processing time (relative) | | | | | ↑↓→ |
```

### 2. Cross-Bot Feedback Analysis
- Is the triage bot scoring accurately? (Compare triage scores to actual miner yield)
- Is the miner's acceptance rate improving? (Writer feedback is being absorbed?)
- Is the writer finding fewer schema errors? (Miner is learning the schema?)
- Are fewer items being flagged for Randy? (Bots are handling more autonomously?)

### 3. Throughput Analysis
- How many files were processed this batch vs. target?
- What bottlenecks slowed processing? (Large files? Complex transcripts? MCP latency?)
- Can batch size be increased safely?

### 4. Cumulative Impact Assessment
- Total new vault notes created across all batches
- Total enrichments to existing notes
- Total new relationships wired
- Vault growth rate (notes/week)
- Percentage of 861 files processed

### 5. Randy's Feedback Integration
When Randy reviews `outputs/needs-review.md` and provides feedback:
- Which items did he accept? → Those extraction patterns are validated
- Which items did he reject? → Update miner patterns to avoid similar extractions
- Which items did he modify? → The delta between bot output and Randy's edit is the learning signal
- Add Randy's feedback patterns to `_bots/knowledge-miner/patterns.md`

## System Improvement Protocol

After every 3 batches (approximately 30 files), conduct a system review:

### Protocol Version Check
1. Read all four bots' `run-protocol.md` files
2. Check version comments — have they been updated since last review?
3. If any bot hasn't improved its protocol in 3 batches, investigate why

### Pattern Library Audit
1. Read all pattern libraries (`patterns.md` files)
2. Are patterns being added regularly?
3. Are any patterns contradictory?
4. Merge insights across bots where applicable

### Quality Gate Calibration
1. Read `_bots/vault-writer/quality-gates.md`
2. Is the accept/reject threshold well-calibrated?
3. Adjust based on cumulative acceptance rate data

### Triage Re-Scoring
After 50+ files are processed:
1. Re-examine remaining queue against what we've learned
2. Re-score files if new patterns suggest different priorities
3. Update `outputs/extraction-queue.md` with revised scores

## Improvement Targets

| Metric | Batch 1 Target | Batch 5 Target | Batch 10 Target |
|--------|---------------|----------------|-----------------|
| Triage accuracy | 60% | 80% | 90% |
| Miner yield (candidates/file) | 2+ | 3+ | 3+ |
| Writer acceptance rate | 70% | 85% | 95% |
| End-to-end yield (notes/file) | 1+ | 2+ | 2+ |
| Randy review items | 50% of notes | 30% of notes | 15% of notes |

## Retrospective Format

```markdown
## System Retrospective — {date} — After Batch {N}

**Progress:** {X} of 861 files ({percentage}%)
**Cumulative vault impact:** {X} new notes, {X} enrichments, {X} relationships

### Pipeline Health Trend
{dashboard table}

### Cross-Bot Improvement Signals
- Triage → Miner accuracy: {improving/stable/degrading}
- Miner → Writer quality: {improving/stable/degrading}
- Writer → Miner feedback: {being absorbed/not being absorbed}

### System-Level Insights
- {insight about the overall pipeline}

### Protocol Changes Made This Cycle
- {bot}: {change} (reason: {why})

### Next Batch Plan
- Batch size: {N}
- Focus: {category or specific files}
- Any special instructions: {e.g., "process all quick-wins this batch"}
```
