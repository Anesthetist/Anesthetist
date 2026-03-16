# Review Accelerator — Decision Patterns

Learned patterns from Randy's review decisions. Each pattern captures how Randy handles a specific type of review item, enabling the bot to handle similar items autonomously over time.

## Tier Promotion Thresholds

```
1-2 approvals  → Tier 3 (present to Randy)
3-5 approvals  → Tier 2 (auto-resolve, Randy audits async)
6-10 approvals → Tier 2 (auto-resolve, log only)
10+ approvals  → Tier 1 (auto-resolve, minimal logging)
1 rejection    → demote to Tier 3
```

## Clinical Interpretation Patterns

*How Randy writes clinical interpretations — voice, depth, structure*

| Pattern ID | Category | Randy's Pattern | Tier | Approvals | Rejections | Added |
|-----------|----------|----------------|------|-----------|------------|-------|
| *populated after Randy's first review cycle* | | | | | | |

## Concept Boundary Patterns

*How Randy resolves "is this one concept or two?" questions*

| Pattern ID | Situation | Randy's Decision | Tier | Count | Added |
|-----------|-----------|-----------------|------|-------|-------|
| *populated after Randy's first review cycle* | | | | | |

## Evidence Quality Patterns

*How Randy assesses evidence quality and what level of citation detail he requires*

| Pattern ID | Situation | Randy's Standard | Tier | Count | Added |
|-----------|-----------|-----------------|------|-------|-------|
| *populated after Randy's first review cycle* | | | | | |

## Anti-Patterns (Randy Rejected These)

*Decisions the bot made that Randy overrode — learn from these to avoid repeating*

| Pattern ID | What Bot Did | What Randy Said | Lesson | Added |
|-----------|-------------|----------------|--------|-------|
| *populated after Randy's first rejection* | | | | |

---

*Last updated: initial creation — no decisions captured yet*
*Total patterns: 0 (system learns from Randy's first review cycle)*
