<!-- v1.0 — initial creation 2026-03-16 -->
# Marketing Intelligence Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/marketing-intelligence/soul.md` — internalize the persona
2. Read `_bots/marketing-intelligence/skills.md` — know the signal types
3. Read `_bots/marketing-intelligence/patterns.md` — load accumulated heuristics
4. Read `_bots/marketing-intelligence/learning-log.md` — know what was learned last time
5. Read the most recent demand signal report in `outputs/marketing/`
6. Check `_bots/competitive-landscape/` for recent competitive intelligence

## Weekly Execution Steps

### Step 1: Macro Signal Scan

Search for macro stress indicators:
```
WebSearch: VIX index current level this week
WebSearch: oil price this week change
WebSearch: major news events this week stress crisis
WebSearch: healthcare news this week staffing burnout policy
WebSearch: AANA news this week
```

Score each signal: 0 (no impact) to 3 (high stress event)
Calculate weekly Macro Stress Index (sum of scores, max 15)

### Step 2: Search Demand Scan

```
WebSearch: Google Trends "breathing exercises" past 7 days
WebSearch: Google Trends "burnout" past 7 days
WebSearch: Google Trends "HRV" OR "heart rate variability" past 7 days
WebSearch: Google Trends "nurse burnout" OR "healthcare burnout" past 7 days
WebSearch: Google Trends "stress app" OR "breathing app" past 7 days
```

Note: rising, falling, or stable for each cluster
Flag any >50% week-over-week increase as a demand spike

### Step 3: Social Listening Scan

```
WebSearch: site:reddit.com/r/CRNA OR site:reddit.com/r/nursing burnout stress this week
WebSearch: site:reddit.com/r/breathwork OR site:reddit.com/r/biohacking HRV breathing app
WebSearch: "Pausality" OR "somnistics" OR "neurominute" -site:somnistics.com
WebSearch: Twitter/X "nurse burnout" OR "CRNA burnout" this week
```

Capture: pain signals, curiosity signals, competitor mentions, SRL mentions

### Step 4: Competitor Activity Scan

```
WebSearch: Calm app news OR update OR launch this week
WebSearch: Headspace news OR update this week
WebSearch: WHOOP news OR update this week
WebSearch: breathwork app new launch 2026
WebSearch: "clinician wellness" app OR program launch
```

Note: new features, messaging changes, ad campaigns, partnerships

### Step 5: Resonance Analysis

Synthesize Steps 1-4:
- Is there a macro stress event that creates demand for what SRL offers?
- Is search volume spiking for SRL-relevant terms?
- Are clinicians talking about stress/burnout on social platforms?
- Are competitors responding to the same signals?

If resonance score ≥ 7/10: produce a Resonance Window Alert
If resonance score 4-6: note in weekly report, monitor
If resonance score ≤ 3: steady state, maintain baseline

### Step 6: Content Resonance Check

Review SRL's recent content performance:
- Which Substack posts got the most opens/engagement?
- Which LinkedIn posts got the most engagement?
- What language are people responding to?
- What format is working?

Cross-reference with demand signals: is what's resonating aligned with what people are searching for?

### Step 7: Product-Market Fit Pulse

Check for PMF signals:
- App store reviews this week (new reviews, sentiment)
- Any organic downloads or enterprise inbound?
- Any unprompted sharing or media mentions?
- User feedback or feature requests?

### Step 8: Produce Weekly Report

Write `outputs/marketing/demand-signal-YYYY-MM-DD.md`:

```markdown
# Demand Signal Report — {date}

## Macro Stress Index: {score}/15
{table of signals and scores}

## Search Demand
{rising/falling/stable for each cluster, any spikes}

## Social Signals
{pain signals, curiosity signals, mentions}

## Competitor Activity
{notable moves}

## Resonance Assessment
**Score:** {1-10}
**Window:** {open/closed/emerging}
**Recommended action:** {spend up/down/hold, channel, message}

## Content Performance
{what's working, what's not}

## PMF Signals
{organic indicators}

## Ad Spend Recommendation
| Channel | Current | Recommended | Reason |
|---------|---------|-------------|--------|

## Next Week Watch
{what to monitor closely}
```

### Step 9: Run Retrospective

Per `_bots/marketing-intelligence/retrospective.md`:
1. Were last week's predictions accurate?
2. Did we miss any signals?
3. Were resonance window recommendations acted on? What happened?
4. Update patterns.md with new heuristics
5. Increment version comment

## Monthly Execution (in addition to weekly)

### Product-Market Fit Assessment

Deep analysis of PMF indicators:
- Download trends (organic vs. paid)
- Retention curves
- NPS or review sentiment trajectory
- Feature request patterns
- Enterprise inquiry patterns
- Competitor switching indicators
- Content-to-download attribution

Write `outputs/marketing/pmf-assessment-YYYY-MM.md`

## Quarterly Execution (in addition to monthly)

### Content Performance Review

Full analysis of all SRL content across channels:
- Best-performing content by engagement and conversion
- Language and framing patterns that resonate
- Channel effectiveness comparison
- Content calendar optimization
- Competitor content strategy analysis

Write `outputs/marketing/content-review-YYYY-QN.md`
