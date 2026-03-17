# Marketing Intelligence Bot — Retrospective Protocol

## Purpose

After every weekly scan, the bot reflects on signal accuracy, missed opportunities, and pattern discovery. Over time, the bot learns when demand spikes, what language resonates, and how to time SRL's presence for maximum impact with minimum spend.

## Post-Run Retrospective

### 1. Signal Accuracy
- Did last week's macro signals produce the predicted demand response?
- Were search demand predictions accurate?
- Were any resonance windows identified that we missed?
- Were any false alarms flagged (predicted spike that didn't materialize)?

### 2. Missed Opportunities
- Did anything happen this week that should have triggered a resonance alert but didn't?
- Were competitors faster to respond to a moment than we were?
- Was there social conversation we should have participated in but didn't catch?

### 3. Content Performance Learning
- What content resonated this week and why?
- What fell flat?
- Any new language patterns discovered?
- Format or timing insights?

### 4. PMF Signal Trends
- Is product-market fit strengthening, weakening, or stable?
- Any new user segments emerging?
- Any unexpected use cases appearing?

### 5. Pattern Updates
- New macro-to-demand patterns discovered → add to patterns.md
- New resonance language discovered → add to patterns.md
- Seasonal calendar refinements → update patterns.md
- New anti-patterns discovered → add to patterns.md

## Retrospective Format

```markdown
## Retrospective — {date}

**Macro Stress Index:** {score} (vs. predicted: {score})
**Signal accuracy:** {percentage of predictions correct}
**Resonance windows identified:** {count}
**Missed opportunities:** {count}

### What Worked
- {signal or recommendation that was accurate/effective}

### What We Missed
- {signal or opportunity we didn't catch}

### New Patterns Discovered
- {pattern → add to patterns.md}

### Content Insights
- {what resonated, what didn't, why}

### PMF Trajectory
- {strengthening / weakening / stable — evidence}
```

## Feedback Integration

1. Update `patterns.md` with new heuristics
2. If a macro-to-demand pattern is confirmed 3+ times, upgrade confidence to "Validated"
3. If a predicted pattern fails 2+ times, downgrade or remove
4. Content language insights feed into Jared's social/brand work
5. PMF signals feed into product decisions and investor materials
6. Increment version comment in `run-protocol.md`
