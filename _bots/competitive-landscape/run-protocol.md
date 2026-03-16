# Competitive Landscape Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/competitive-landscape/soul.md` — internalize the persona
2. Read `_bots/competitive-landscape/watchlist.md` — know who to track
3. Read `_bots/competitive-landscape/sources.md` — know where to look
4. Read the most recent `outputs/competitive-briefing-*.md` — know what's already known
5. Read `observations/competitive-intelligence-briefing-*.md` — baseline intelligence

## Execution Steps

### Step 1: Live Intelligence Gathering

For each Tier 1 company on the watchlist:
```
WebSearch: "[Company Name]" AND ("funding" OR "raised" OR "launch" OR "partnership" OR "acquisition" OR "hiring") 2026
WebSearch: "[Company Name]" AND ("breathwork" OR "HRV" OR "biofeedback" OR "wellness" OR "enterprise")
```

For market-level signals:
```
WebSearch: "breathwork startup" OR "HRV startup" AND ("funding" OR "raised") 2026
WebSearch: "wellness tech" AND ("acquisition" OR "M&A") 2026
WebSearch: site:insider.fitt.co [this week's date range]
WebSearch: "digital therapeutics" AND ("clinical trial" OR "FDA" OR "clearance") 2026
```

### Step 2: Delta Analysis

Compare findings against the most recent briefing:
- What is NEW since last report?
- What has CHANGED (funding, leadership, product)?
- What is CONFIRMED (rumors now verified)?
- What is DEAD (companies quiet, pivoted, shut down)?

### Step 3: Output Generation

1. **Weekly Briefing** → `outputs/competitive-briefing-YYYY-MM-DD.md`
   - Use frontmatter matching vault schema
   - Tag with subjects: competitive-landscape, market-intelligence, wellness-tech, deal-flow
   - Link to related vault notes via `skos:related`

2. **Dossier Updates** → `observations/competitor-dossier-{company}.md`
   - Only create/update if material changes detected
   - Each dossier is a living document, updated in place

3. **Quick-Response Updates** → `outputs/investor-competitive-responses.md`
   - Format: "What about [X]?" → 3-sentence answer
   - Update only when the answer would change

### Step 4: Vault Integration

- Ensure all new notes have proper frontmatter
- Link to `concepts/market-intelligence.md` via `skos:related`
- Update `_index/` if new companies or categories added

### Step 5: Post-Run Summary

Output a brief summary to the user:
- Number of signals detected
- Top 3 most important findings
- Any urgent flags
- Recommendation for follow-up actions

## Error Handling

- If a source is unreachable, note it and continue with other sources
- If data conflicts between sources, note the conflict and cite both
- If no new signals are found for a company, that IS a signal (they may be going quiet)
- Always distinguish between "no news found" and "confirmed no news"
