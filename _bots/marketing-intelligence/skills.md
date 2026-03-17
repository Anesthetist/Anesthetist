# Marketing Intelligence Bot — Skills

## Core Capabilities

### 1. Macro Stress Signal Monitoring

Track these indicators weekly:

| Signal | Source | Threshold for Alert |
|--------|--------|-------------------|
| VIX (volatility index) | Market data / WebSearch | >25 = elevated, >35 = spike |
| Oil price | Commodity news | >10% weekly move |
| Mass casualty / disaster | News feeds | Any major event |
| Healthcare policy news | HLTH, CMS, AANA | Staffing mandates, reimbursement changes, scope-of-practice battles |
| Geopolitical escalation | News feeds | Conflict affecting US/allied nations |
| Pandemic/epidemic signals | WHO, CDC | Any respiratory/infectious disease alert |
| Economic indicators | Jobs report, CPI, Fed | Recession signals, inflation spikes |

### 2. Search Demand Tracking

Monitor Google Trends and related signals for these term clusters:

**Stress/Anxiety cluster:**
- "how to manage stress" / "stress relief" / "anxiety help"
- "can't sleep" / "insomnia" / "racing thoughts"
- "burnout" / "feeling overwhelmed" / "compassion fatigue"

**Breathing/Regulation cluster:**
- "breathing exercises" / "breathwork" / "box breathing"
- "calm down" / "regulate nervous system" / "vagus nerve"
- "HRV" / "heart rate variability" / "biofeedback"

**Clinical/Professional cluster:**
- "nurse burnout" / "CRNA burnout" / "healthcare worker stress"
- "clinician wellness" / "physician burnout" / "moral injury healthcare"
- "continuing education" / "CEU" / "AANA CE credits"

**App/Product cluster:**
- "stress app" / "breathing app" / "meditation app" / "Apple Watch stress"
- Competitor names: Calm, Headspace, Breathwrk, WHOOP recovery
- "Pausality" / "somnistics" / "neurominute" (brand terms)

### 3. Social Listening

Monitor for SRL-relevant conversations:

**Platforms:** X/Twitter, Reddit (r/CRNA, r/nursing, r/anesthesiology, r/breathwork, r/biohacking), Instagram, TikTok, LinkedIn

**X Lists (Curated Signal Sources):**
Randy follows curated X lists that represent pre-filtered signal. These are higher-value than general search because the list curator (e.g., Brian Rommel) has already identified who matters. Monitor these lists for:
- Emerging trends before they hit mainstream
- Thought leader positioning shifts
- Conference/event signals
- Cross-pollination opportunities (someone in a wellness list discussing clinical applications)
- Language and framing that resonates in adjacent communities

**X List Monitoring Protocol:**
1. Identify Randy's followed X lists (Brian Rommel's lists + others)
2. For each list, scan weekly for: most-engaged posts, recurring themes, new voices, SRL-relevant discussions
3. Flag posts that align with SRL's thesis or create resonance opportunities
4. Track which list members have the most engagement on SRL-adjacent topics
5. Identify potential collaborators, podcast guests, or content partners from list activity
6. Note language patterns that work — how do respected voices in these communities talk about stress, breathing, performance, nervous system?

**Signal types:**
- Pain signals: clinicians describing burnout, stress, exhaustion
- Curiosity signals: questions about HRV, breathing, nervous system regulation
- Competitor mentions: what people say about Calm, Headspace, WHOOP
- SRL mentions: any mention of Pausality, somnistics, NeuroMinute
- Influencer activity: who's talking about breathwork, HRV, clinician wellness
- List-sourced signals: trends emerging from curated X lists before they go mainstream

### 4. Content Performance Tracking

For SRL's own content (Substack, LinkedIn, Instagram, app store):
- Which posts/articles get the most engagement?
- What language resonates? (exact phrases that get shared/saved)
- What time of day/week gets best engagement?
- What format works? (story vs. science vs. protocol vs. data visualization)
- App store reviews: what do users praise? What do they criticize?

### 5. Competitor Ad Intelligence

Track competitor advertising patterns:
- When do competitors increase ad spend? (seasonal? event-driven?)
- What messaging are they using? (features? outcomes? identity?)
- What channels are they on? (Instagram? TikTok? Google? podcast?)
- What's their CTA? (download? subscribe? free trial?)
- Where are they NOT advertising? (gaps SRL can fill)

### 6. Product-Market Fit Signals

Aggregate signals that indicate whether SRL is building the right thing:

| Signal | Where to Find It | What It Means |
|--------|------------------|---------------|
| Organic app downloads (no ad) | App Store Connect | People finding you without prompting |
| "Aha" moments in reviews | App Store, social | Users discovering value they didn't expect |
| Unprompted sharing | Social, referral data | Users becoming advocates |
| Feature requests | Reviews, support, social | What users want that you don't have |
| Churn reasons | Support, surveys | Why people leave |
| Competitor switching | Reviews, social | People coming FROM competitors |
| Enterprise inbound | Email, LinkedIn | Institutions finding you |
| Press/media mentions | Google Alerts, news | Organic credibility signals |

### 7. Resonance Windows

Synthesize all signals into actionable windows:

```markdown
## Resonance Window Detected — {date}

**Trigger:** {what happened — macro event, search spike, social moment}
**Demand signal:** {search volume data, social mentions, sentiment}
**Resonance score:** {1-10 based on alignment with SRL's message}
**Recommended action:**
- Ad spend: {increase/maintain/hold} by {percentage}
- Channel: {where to deploy — Google, Instagram, LinkedIn, podcast}
- Message: {specific angle that matches the moment}
- Duration: {how long this window likely lasts}
**Competitor response:** {what competitors are doing with this moment}
```

## Tools Used

- **WebSearch** — Google Trends, news, competitor research, market data
- **WebFetch** — Specific URLs for trend data, competitor landing pages, industry news
- **Vault MCP tools (read)** — Search vault for relevant content/evidence to reference in messaging
- **Grep/Glob** — Search existing outputs for content that matches the moment

## Output Formats

1. **Weekly Demand Signal Report** → `outputs/marketing/demand-signal-YYYY-MM-DD.md`
2. **Resonance Window Alerts** → `outputs/marketing/resonance-alert-YYYY-MM-DD.md` (as needed)
3. **Monthly Product-Market Fit Assessment** → `outputs/marketing/pmf-assessment-YYYY-MM.md`
4. **Quarterly Content Performance Review** → `outputs/marketing/content-review-YYYY-QN.md`
5. **Competitor Ad Intelligence** → `outputs/marketing/competitor-ads-YYYY-MM-DD.md`
