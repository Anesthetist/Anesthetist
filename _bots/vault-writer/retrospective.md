# Vault Writer Bot — Retrospective Protocol

## Purpose

The vault-writer is the quality gate. Its retrospective focuses on schema compliance, duplicate detection accuracy, and the feedback signal it sends back to the miner. This implements the Evaluator-Optimizer pattern (Anthropic): the writer evaluates the miner's output, and that evaluation improves both bots.

## Post-Run Retrospective (Required after every batch)

### 1. Acceptance/Rejection Analysis

```markdown
| Metric | This Batch | Running Average |
|--------|-----------|----------------|
| Candidates received | X | X.X |
| Accepted as-is | X (Y%) | X.X% |
| Accepted with corrections | X (Y%) | X.X% |
| Rejected (duplicate) | X (Y%) | X.X% |
| Rejected (quality) | X (Y%) | X.X% |
| Flagged for review | X (Y%) | X.X% |
```

### 2. Schema Compliance Analysis
- What schema errors appeared most frequently?
- Were there patterns in which required fields the miner missed?
- Should the quality-gates.md be updated with new validation rules?

### 3. Duplicate Detection Analysis
- How many duplicates did the vault search catch?
- Were there near-duplicates that required judgment calls?
- Were there false positives (flagged as duplicate but actually new)?
- Should search strategies be adjusted?

### 4. Enrichment Quality
- When enriching existing notes, was new content genuinely additive?
- Were there cases where the enrichment degraded the existing note?
- Should the "add, never replace" rule be refined?

### 5. Miner Feedback
For each rejection or correction, produce feedback for the knowledge-miner:

```markdown
### Feedback to Knowledge Miner — {date}

**Accepted:** {N} of {total} candidates ({percentage}%)

**Common issues this batch:**
1. {issue} — occurred {N} times — suggest: {improvement}
2. {issue} — occurred {N} times — suggest: {improvement}

**Specific corrections made:**
- {slug}: {what was wrong} → {what was fixed}

**Patterns to add to miner's pattern library:**
- {pattern discovered during validation}
```

This feedback is appended to `_bots/knowledge-miner/learning-log.md` so the miner loads it on next run.

## Retrospective Format

```markdown
## Retrospective — {date} — Batch {N}

**Candidates processed:** {count}
**Acceptance rate:** {percentage}%
**Schema error rate:** {percentage}%
**Duplicate catch rate:** {percentage}%

### What Worked
- {validation approach that was effective}

### What Didn't Work
- {missed duplicate, wrong rejection, schema gap}

### Quality Gate Adjustments
- [ ] {specific change to quality-gates.md}

### Miner Feedback Sent
- {summary of feedback provided}
```

## Feedback Integration

After writing the retrospective:
1. Update `quality-gates.md` if new validation rules are needed
2. Append miner feedback to `_bots/knowledge-miner/learning-log.md`
3. If duplicate detection missed >10% of duplicates, tighten search strategy in `run-protocol.md`
4. If acceptance rate >95%, the miner is well-calibrated — note this
5. If acceptance rate <70%, the miner needs recalibration — flag urgently
6. Increment protocol version in `run-protocol.md`
