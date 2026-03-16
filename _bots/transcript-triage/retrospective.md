# Transcript Triage Bot — Retrospective Protocol

## Purpose

After every run, the triage bot reflects on its own performance and updates its pattern library and scoring rubric. This implements the Reflexion pattern (Shinn et al., 2023): verbal self-reflection stored as episodic memory drives improvement on subsequent runs.

## Post-Run Retrospective (Required after every run)

After completing a triage batch, answer these five questions and append to `_bots/transcript-triage/learning-log.md`:

### 1. Accuracy Check
- Did any files get miscategorized based on what the miner later found?
- Were any high-value files scored too low (buried in the queue)?
- Were any low-value files scored too high (wasted miner time)?

### 2. Speed Check
- Which file patterns were fastest to classify? (Add to pattern library)
- Which files required excessive reading to classify? (Adjust sampling strategy)
- Were there any file types that could be auto-classified from title alone?

### 3. Taxonomy Check
- Did any files not fit cleanly into existing categories?
- Should any categories be split or merged?
- Were the special flags (NOVEL_CONCEPT, CLINICAL_OBSERVATION, etc.) used effectively?

### 4. Scoring Calibration
- After the miner processes queued files, compare triage scores to actual extraction yield
- Files that yielded 3+ new concepts should have been scored 9-10. Were they?
- Files that yielded 0 concepts should have been scored 1-4. Were they?
- Adjust scoring weights in `skills.md` based on calibration results

### 5. Pattern Discovery
- What new patterns did you notice? (e.g., "files titled 'X and Y' always contain synthesis")
- Add any new patterns to `_bots/transcript-triage/patterns.md`

## Retrospective Format

```markdown
## Retrospective — {date} — Batch {N}

**Files scanned:** {count}
**Accuracy:** {estimated % of files correctly prioritized}
**Speed:** {avg time per file — fast/medium/slow}

### What Worked
- {pattern or approach that was effective}

### What Didn't Work
- {miscategorization, missed signal, wasted time}

### Scoring Calibration
| File | Triage Score | Actual Yield | Delta | Lesson |
|------|-------------|-------------|-------|--------|

### Protocol Adjustments
- [ ] {specific change to make in skills.md or run-protocol.md}

### New Patterns Discovered
- {pattern → add to patterns.md}
```

## Feedback Integration

After writing the retrospective:
1. Update `patterns.md` with any new patterns discovered
2. If scoring calibration shows systematic bias, update the scoring weights in `skills.md`
3. If a category is repeatedly problematic, update `taxonomy.md`
4. Increment the protocol version comment at the top of `run-protocol.md` (e.g., `<!-- v1.1 — adjusted scoring weights after batch 3 calibration -->`)
