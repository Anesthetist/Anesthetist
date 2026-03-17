# Marketing Intelligence Bot — Schedule

## Weekly (Every Monday)

**Runtime:** 20-30 minutes
**Phases:**
1. Macro signal scan (5 min)
2. Search demand scan (5 min)
3. Social listening scan (5 min)
4. Competitor activity scan (5 min)
5. Resonance analysis + report (10 min)

**Output:** `outputs/marketing/demand-signal-YYYY-MM-DD.md`

## As-Needed (Resonance Window Alert)

**Trigger:** Macro Stress Index ≥ 10/15 OR search demand spike >50% week-over-week
**Runtime:** 10 minutes
**Output:** `outputs/marketing/resonance-alert-YYYY-MM-DD.md`

## Monthly (First Monday of month)

**Runtime:** 45-60 minutes
**Additional to weekly:** Product-Market Fit Assessment
**Output:** `outputs/marketing/pmf-assessment-YYYY-MM.md`

## Quarterly (First Monday of quarter)

**Runtime:** 60-90 minutes
**Additional to monthly:** Content Performance Review
**Output:** `outputs/marketing/content-review-YYYY-QN.md`

## Integration with Other Bots

| Bot | Feeds Into Marketing Intelligence | Marketing Intelligence Feeds |
|-----|----------------------------------|------------------------------|
| Competitive Landscape | Competitor funding, moves, hires | Competitor ad strategy, messaging gaps |
| Extraction Coordinator | — | Content ideas from vault discoveries |
| Review Accelerator | — | User feedback patterns for PMF |

## Automation (Mac Mini)

When the Mac Mini is set up:
```
# Weekly scan — Monday 7 AM
0 7 * * 1 claude --project Library-Graph --prompt "Run marketing intelligence weekly scan per _bots/marketing-intelligence/run-protocol.md"

# Resonance alerts — check daily at noon
0 12 * * * claude --project Library-Graph --prompt "Run marketing intelligence macro signal check. Alert only if Macro Stress Index >= 10."
```
