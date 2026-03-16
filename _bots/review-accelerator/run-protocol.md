<!-- v1.0 — initial creation 2026-03-15 -->
# Review Accelerator Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/review-accelerator/soul.md` — internalize the persona
2. Read `_bots/review-accelerator/skills.md` — know the tier system
3. Read `_bots/review-accelerator/decision-patterns.md` — load learned patterns from Randy's prior decisions
4. Read `_bots/review-accelerator/learning-log.md` — know what was learned last time
5. Read `outputs/needs-review.md` — load the current review queue
6. Read `outputs/auto-resolved-log.md` — know what's already been handled

## Execution Steps

### Step 1: Load Review Queue

Read `outputs/needs-review.md` and parse all flagged items into a working list.

### Step 2: Classify Each Item by Tier

For each item in the queue:

1. **Check decision-patterns.md** — does a learned pattern cover this item?
   - If yes and pattern confidence is Tier 1 → auto-resolve
   - If yes and pattern confidence is Tier 2 → auto-resolve with audit log
   - If yes and pattern confidence is Tier 3 → pre-draft recommendation

2. **Check item category:**
   - Evidence verification → Tier 1 (delegate to citation resolver)
   - Schema correction → Tier 1 (fix directly)
   - Concept boundary → read both concepts via `get_note`, determine if answer is clear
   - Clinical interpretation → check if similar interpretations exist in vault
   - Trademarked concept → Tier 4 (always escalate)

3. **Assign tier and log reasoning**

### Step 3: Process Tier 1 Items (Auto-Resolve)

For each Tier 1 item:
1. Execute the resolution (citation lookup, schema fix, duplicate clear)
2. Use MCP tools to update vault notes if needed
3. Log to `outputs/auto-resolved-log.md`
4. Remove from `outputs/needs-review.md`

### Step 4: Process Tier 2 Items (Auto-Resolve with Audit)

For each Tier 2 item:
1. Execute the resolution
2. Log to `outputs/auto-resolved-log.md` with detailed reasoning
3. Add to Randy's review dashboard under "Already Handled" for async audit
4. Remove from `outputs/needs-review.md`

### Step 5: Process Tier 3 Items (Pre-Draft for Randy)

For each Tier 3 item:
1. Read relevant vault context
2. Draft a recommendation with reasoning
3. For clinical interpretations: draft in Randy's voice using calibration sources
4. Add to Randy's review dashboard under "Quick Approvals"
5. Keep in `outputs/needs-review.md` until Randy acts

### Step 6: Process Tier 4 Items (Escalate)

For each Tier 4 item:
1. Gather all relevant context (vault notes, evidence chains, related concepts)
2. Present options with pros/cons
3. State recommendation with reasoning
4. Add to Randy's review dashboard under "Escalations"
5. Keep in `outputs/needs-review.md` until Randy acts

### Step 7: Produce Review Dashboard

Write `outputs/review-dashboard.md` with:
- Quick Approvals (Tier 3) — numbered, with checkboxes
- Already Handled (Tier 1-2) — summary table for async audit
- Escalations (Tier 4) — detailed with context and options
- Metrics: items auto-resolved, items needing Randy, estimated review time

### Step 8: Capture Randy's Decisions (Post-Review)

After Randy reviews the dashboard:
1. For each approved item → capture the pattern, update `decision-patterns.md`
2. For each edited item → capture the delta (what Randy changed), update pattern
3. For each rejected item → capture why, add as anti-pattern
4. Update tier promotion counts for each pattern
5. Promote/demote patterns as thresholds are crossed

### Step 9: Run Retrospective

1. Calculate auto-resolution rate (Tier 1+2 as % of total)
2. Calculate Randy's approval rate on Tier 3 pre-drafts
3. Track queue shrinkage over time
4. Update `learning-log.md`
5. Increment version comment at top of this file

## Error Handling

- If citation resolver can't find a study → escalate to Tier 3, don't create a bad evidence note
- If unsure about tier assignment → default to higher tier (more Randy involvement)
- If a pattern match is ambiguous → treat as Tier 3 (present to Randy)
- Never auto-resolve and delete — always log for audit trail
