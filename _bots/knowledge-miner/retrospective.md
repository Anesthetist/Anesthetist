# Knowledge Miner Bot — Retrospective Protocol

## Purpose

After every extraction run, the miner reflects on extraction quality, signal-to-noise ratio, and attribution accuracy. This drives three improvement loops:

1. **Pattern Library** — "When Randy says X, extract Y" heuristics that speed up future runs
2. **Quality Scorecard** — Tracks extraction yield and accuracy across runs for calibration
3. **Protocol Refinement** — Specific changes to run-protocol.md based on what worked and what didn't

## Post-Run Retrospective (Required after every file processed)

### 1. Extraction Yield Analysis

```markdown
| Metric | This File | Running Average |
|--------|----------|----------------|
| New concepts extracted | X | X.X |
| Enrichments to existing concepts | X | X.X |
| Evidence notes identified | X | X.X |
| Observations captured | X | X.X |
| Relationships discovered | X | X.X |
| Items flagged for review | X | X.X |
| False positives (extracted but shouldn't have been) | X | X.X |
```

### 2. Signal-to-Noise Analysis
- What percentage of the transcript contained extractable knowledge?
- Where were the highest-density sections? (beginning? middle? end?)
- What types of Randy prompts produced the best extractable content?
- What types of ChatGPT responses contained useful vs. filler content?

### 3. Attribution Accuracy
- Were there cases where ChatGPT's words were mistakenly attributed to Randy?
- Were there cases where Randy's insights were buried in ChatGPT's expansion?
- Were corrections/redirections properly captured as insights?

### 4. De-Duplication Effectiveness
- How many vault searches were needed per extraction candidate?
- Were any near-duplicates missed? (discovered later by vault-writer)
- Were any non-duplicates incorrectly flagged as duplicates?

### 5. Vault-Writer Feedback Loop
After the vault-writer processes this extraction report:
- How many candidates were accepted as-is?
- How many needed schema corrections?
- How many were rejected as duplicates the miner missed?
- How many were flagged for Randy's review?

Use this data to calibrate future extraction thresholds.

## Retrospective Format

```markdown
## Retrospective — {date} — {source-file}

**Extraction yield:** {N} concepts, {N} evidence, {N} observations
**Signal-to-noise:** {percentage}% extractable content
**Attribution confidence:** {high/medium/low}
**Vault-writer acceptance rate:** {percentage}%

### What Worked
- {extraction approach that was effective}

### What Didn't Work
- {missed signal, false positive, attribution error}

### New Extraction Patterns
- When Randy says "{pattern}" → extract as {concept/evidence/observation}
- {pattern} → add to patterns.md

### Protocol Adjustments
- [ ] {specific change to make}

### Calibration Notes
- Triage score was {X}, actual yield was {Y} → {over/under/correctly rated}
```

## Feedback Integration

After writing the retrospective:
1. Update `_bots/knowledge-miner/patterns.md` with new extraction patterns
2. Update `_bots/knowledge-miner/memory.md` with processing log entry
3. If vault-writer rejection rate >20%, review and tighten extraction thresholds
4. If vault-writer acceptance rate >90%, consider loosening thresholds for efficiency
5. Feed triage calibration data back to `_bots/transcript-triage/learning-log.md`
6. Increment protocol version in `run-protocol.md`
