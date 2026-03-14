---
id: "urn:srl:source:gdrive-bot-qc-standards"
type: source
title: "Bot QC Standards"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:Bot-QC-Standards.md"
---

# QC-STANDARDS.md — Quality Control for Bot Outputs

*Pax is the QC layer. No report ships without review.*

---

## 🎯 The Rule

**Nothing ships to Randy or Jared without Pax review.**

Bots generate drafts → Pax reviews → Pax ships (or rejects and re-runs)

---

## 📋 Universal QC Checklist

Every bot output must pass these checks:

### Completeness
- [ ] All required sections present
- [ ] No placeholder text ("TBD", "TODO", "[INSERT]")
- [ ] Minimum word count met (varies by report type)
- [ ] All competitors/topics covered per spec

### Accuracy
- [ ] Dates are current (not stale news)
- [ ] URLs are included and likely valid
- [ ] Numbers/stats have sources cited
- [ ] No hallucinated information

### Actionability
- [ ] Recommendations are specific (not generic)
- [ ] Each recommendation has an owner
- [ ] Each recommendation has a timeframe
- [ ] "So what?" is answered for every insight

### Quality
- [ ] Writing is clear and scannable
- [ ] No repetition or filler
- [ ] Executive summary actually summarizes
- [ ] Would I be proud to ship this?

---

## 📊 Report-Specific Standards

### SRL Daily Market Insights

**Minimum Requirements:**
- [ ] 2+ actionable recommendations with URLs
- [ ] 3+ hot threads identified (with links)
- [ ] Competitor mentions section populated
- [ ] ICP language quotes included (direct quotes, not summaries)
- [ ] All 5 platforms scanned (Reddit, LinkedIn, X, Instagram, TikTok)

**Quality Bar:**
- Fresh content (last 24-48 hours)
- At least one "act today" opportunity
- Draft responses provided (not just "engage here")

**Red Flags (auto-reject):**
- No Reddit threads found
- Generic recommendations ("monitor social media")
- Missing platform coverage
- No direct user quotes

---

### Pausality Competitive Intelligence

**Minimum Requirements:**
- [ ] All 6 Tier 1 competitors covered individually
- [ ] 20+ web searches performed (check reasoning/logs)
- [ ] 7 Powers scorecard completed
- [ ] Direct user quotes from Reddit/Trustpilot
- [ ] TOP 3 recommendations with owners and timeframes
- [ ] Sources section with URLs
- [ ] Leaply specifically addressed

**Quality Bar:**
- Each competitor has: recent moves, sentiment, threat level
- Recommendations are strategic, not obvious
- Emerging competitors section has actual findings
- Executive summary is punchy (3-5 sentences max)

**Red Flags (auto-reject):**
- Missing any Tier 1 competitor
- No Leaply coverage
- Generic scorecard (all 3s)
- No user quotes
- Recommendations without owners
- "No news found" without explanation of what was searched

---

## 🔄 QC Workflow

### Step 1: Bot Generates Draft
Bot saves to: `/home/ubuntu/clawd/reports/drafts/[bot-name]/[filename].md`
Bot notifies Pax: "Draft ready for QC"

### Step 2: Pax Reviews
1. Read the draft
2. Run through checklist above
3. Score: PASS / NEEDS REVISION / REJECT

### Step 3: Action Based on Score

**PASS (8-10/10):**
- Move to final location
- Upload to Google Drive
- Share with Jared
- Notify Randy
- Delete draft

**NEEDS REVISION (5-7/10):**
- Note specific issues
- Either fix manually OR re-run bot with feedback
- Review again

**REJECT (< 5/10):**
- Note what went wrong
- Re-run bot with improved prompt
- If repeated failures, flag for bot improvement

### Step 4: Ship
Only Pax sends final reports to Randy/Jared.

---

## 📁 File Structure

```
/home/ubuntu/clawd/reports/
├── drafts/                          # Bot outputs land here first
│   ├── srl-market-insights/
│   │   └── [draft files]
│   └── competitive-analysis/
│       └── [draft files]
├── srl-market-insights/             # Approved reports
│   └── [final files]
└── competitive-analysis/            # Approved reports
    └── [final files]
```

---

## 🚨 Escalation

If a bot consistently produces sub-par output:
1. Review the bot's AGENTS.md and TOOLS.md
2. Identify the gap (instructions? sources? methodology?)
3. Fix the bot files
4. Test with manual run
5. Document the fix

---

## 📝 QC Log

Keep a running log of QC decisions:

```
/home/ubuntu/clawd/reports/QC-LOG.md
```

Format:
```
## [DATE]

### [Report Name]
- **Score:** X/10
- **Decision:** PASS / REVISION / REJECT
- **Issues:** [if any]
- **Action taken:** [what was done]
```

---

*Quality is not negotiable. Ship 10/10 or don't ship.*
