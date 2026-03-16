# Competitive Landscape Bot — Schedule

## Weekly Cadence

**Run day:** Every Sunday (or first available day)
**Estimated runtime:** 30-45 minutes
**Trigger:** Manual invocation or cron job

### Weekly Run Protocol

#### Phase 1: Scan (15 min)
1. **Funding scan** — Search for new rounds in breathwork, HRV, wellness tech, digital therapeutics, neurostim
2. **Competitor news scan** — Check all Tier 1 and Tier 2 companies for news, announcements, product updates
3. **M&A scan** — Search for acquisitions, mergers, partnerships in the wellness/health-tech space
4. **Hiring scan** — Check Tier 1 competitor job boards/LinkedIn for notable hiring patterns
5. **Narrative scan** — Check Fitt Insider, HLTH, Rock Health for market framing shifts

#### Phase 2: Analyze (10 min)
1. **Delta detection** — What changed since last week? New funding? New hires? New products?
2. **Signal classification** — Is this a convergence signal, divergence signal, acquisition window, or narrative shift?
3. **Impact assessment** — How does each signal affect Pausality's competitive position?
4. **Investor readiness** — Would this come up in a pitch meeting? If yes, draft the response

#### Phase 3: Produce (15 min)
1. **Weekly Competitive Briefing** — Save to `outputs/competitive-briefing-YYYY-MM-DD.md`
2. **Dossier updates** — Update any company dossiers that changed
3. **Quick-response sheet** — Update `outputs/investor-competitive-responses.md` if needed
4. **Alert flags** — If any signal is urgent (major funding round, direct competitor launch), flag prominently

### Weekly Briefing Structure

```markdown
# Weekly Competitive Briefing — [Date]

## Headline Signal
[The single most important competitive development this week — 2-3 sentences]

## Funding & Deal Flow
[New rounds, M&A, partnerships — table format]

## Competitor Moves
[Product launches, pivots, hiring surges, leadership changes]

## Narrative Watch
[How is the market framing the wellness/breathwork/HRV category this week?]

## Pausality Positioning Impact
[What does this week's intelligence mean for Pausality's pitch?]

## Investor Quick-Hit Updates
[Any changes to the quick-response sheet]

## Sources
[Links to primary sources for all claims]
```

## Monthly Deep Dive (First Sunday of Month)

In addition to the weekly scan:
1. **Full watchlist review** — Promote/demote companies between tiers
2. **Valuation benchmarking** — Update comparable transaction data
3. **VC conflict map** — Update which investors are in which competitors
4. **TAM refresh** — Check for new market sizing data
5. **State of Market report** — Regenerate `outputs/state-of-market-YYYY-MM-DD.md`

## Quarterly Strategic Review (First Sunday of Quarter)

1. **Competitive positioning matrix** — Refresh the 2x2 (Cognitive Load vs. Physiological Precision)
2. **Threat reassessment** — Which competitor got stronger? Weaker? Who is new?
3. **Exit landscape** — Update acquirer list and probability assessments
4. **Board presentation deck data** — Package intelligence for investor updates

## Cron Setup

To automate weekly reminders:
```
# Run competitive landscape bot every Sunday at 9am
# Invocation: claude --project Library-Graph --prompt "Run the weekly competitive landscape scan per _bots/competitive-landscape/schedule.md"
```
