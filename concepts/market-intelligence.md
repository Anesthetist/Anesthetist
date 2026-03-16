---
created: '2026-03-14'
creator: randy@somnistics.com
id: urn:srl:concept:market-intelligence
modified: '2026-03-15'
prov:wasDerivedFrom:
- urn:srl:evidence:chin-2025-joy-of-small-markets
- urn:srl:observation:tam-keyword-intelligence-breathwork-demand
skos:narrower:
- competitive-moat-latency
- ip-six-pillar-moat
- network-audit-credibility-capital-gap
skos:related:
- fda-wellness-boundary
- rd-blueprint-market-segmentation
- wearable-sensor-limitations
- seven-powers-compound-loops
- autonomic-regulation
- clinician-durability
- crna-burnout-epidemiology
- executive-team-priorities-march-2026
- pausality-science-validation-roadmap
- acsm-wearables-top-trend-2026
- trend-clinician-burnout-ai-scribes-2026
- trend-wearable-sensors-2026-systematic-review
- high-burnout-verticals
- commoncog-operating-principles
- somnistics
status: canonical
subjects:
- competitive-landscape
- deal-flow
- acquisition-strategy
- newsletter-intelligence
- wellness-tech
title: Market Intelligence
type: concept
---

# Market Intelligence

The systematic, ongoing collection and synthesis of competitive signals, deal flow, hiring trends, and acquisition landscape data relevant to Pausality and Somnistics Research Labs.

## Structure

The SRL Market Intelligence system is built on four layers that feed into each other on a daily → weekly → monthly cadence:

### Layer 1: Daily Signals (automated)
The `daily-briefing` scheduled task runs each morning and:
- Ingests Gmail newsletters (Tier 1: HLTH Daily, AANA Network, Steven Kotler, Not Boring, Work-Bench; Tier 2: Vervaeke Foundation, MEA Wisdom, Every, Epsilon Theory)
- Searches Fitt Insider (insider.fitt.co) for latest wellness tech intelligence
- Saves output to `/mnt/outputs/daily-briefing-[DATE].md` and the SRL Vault

### Layer 2: Weekly Competitive Landscape (automated)
The `competitive-landscape` bot (`_bots/competitive-landscape/`) runs every Sunday and:
- Scans all tiered competitors for funding, hiring, product, M&A, and narrative signals
- Detects deltas from the prior week's intelligence
- Produces weekly briefing → `outputs/competitive-briefing-YYYY-MM-DD.md`
- Updates investor quick-response sheet → `outputs/investor-competitive-responses.md`
- Updates company dossiers as needed
- Protocol defined in `_bots/competitive-landscape/run-protocol.md`

### Layer 3: Weekly HPO Research (automated)
The `weekly-hpo-research-scan` task runs every Monday and populates the vault with the latest human performance optimization and neuroscience research relevant to SRL's scientific foundation.

### Layer 4: State of the Market (monthly)
The `update-state-of-market` scheduled task synthesizes all daily and weekly intelligence into a comprehensive report. Outputs a branded `.docx` report and updates the vault output note.

## Competitive Landscape (Updated March 15, 2026)

### Tier 1: Direct Competitors
Companies competing for the same buyer, budget, or physiological outcome.

| Company | Status | Key Signal |
|---------|--------|------------|
| Climatic | $10M seed, Lerer Hippeau + Mount Sinai | "Breathing as daily habit" thesis — narrative competitor |
| NEUROFIT | Pre-seed, 60K users | "Nervous System Trainer" positioning — closest narrative analog |
| Prana Labs (Vayu) | $150K seed | Apple Watch breathwork + haptics — closest product analog |
| HeartMath | Established | Original HRV coherence company; enterprise training programs |
| Moonbird | $1.74M seed | Handheld breathing device; expanding to US |
| Othership | Growth | Community-driven breathwork app |
| ~~Breathwrk~~ | **Acquired by Peloton for $2.2M (Oct 2025)** | Cautionary tale: breathing app without clinical moat sold for pennies |

### Tier 2: Platform Competitors
Compete for the wellness budget or user's attention at the moment stress hits.

| Company | Status | Key Signal |
|---------|--------|------------|
| Calm | $2B valuation, declining | Revenue -24% YoY (2025), lost 500K subscribers |
| Headspace | ~$320M (from $3B peak) | Multiple layoffs, pivoting to EAP/enterprise |
| WHOOP | $3.6B, pre-IPO | 600+ new hires, IPO 2026-2028, needs protocol IP |
| Oura | $11B, $900M Series E | Team USA/LA28 partnership, platform expansion |
| Ultrahuman | $60M+ Series B | Ring AIR, acquired viO HealthTech |
| Apollo Neuro | $30.7M, $100M+ valuation | 17 clinical studies, launching Apollo for Business |
| Ohm Health | $737K seed | Biofeedback breathing lamp, new round opening 2026 |

### Tier 3: Enterprise Gatekeepers
Own the procurement relationship with hospital/enterprise buyers.

| Company | Status | Key Signal |
|---------|--------|------------|
| Lyra Health | $910M+ raised, 20M+ lives | Acquired Bend Health (pediatric mental health) |
| Spring Health | $462M+, $3.3B valuation | Acquiring Alma (~10M mental health visits/yr combined) |
| Modern Health | $192M raised, $1.17B unicorn | Multi-modal enterprise wellness. Acquired Anvil Health (AI) |
| Grow Therapy | $150M Series D, $3B valuation (Mar 2026) | $1B revenue, 10M appointments. TCV + Goldman Sachs. Employer wellness expansion |

### Tier 4a: EHR Platforms
Own the hospital IT relationship. NOT building wellness — creating a distribution opportunity.

| Company | Status | Key Signal |
|---------|--------|------------|
| Epic Systems | ~$4.6B revenue, 38% US market | AI Charting, DAX Copilot, Art/Emmie/Penny AI suite. Reduces documentation burden but NOT active stress recovery. Epic App Market = Pausality distribution channel to 2/3 of US hospitals |
| Oracle Health (Cerner) | $28.3B acquisition | Clinical AI Agent (-40% doc time, 300+ orgs). Same gap: no clinician wellness tools |

### Tier 4b: Big Tech Health Platforms
Building the health data/AI layer. They need clinical protocols.

| Company | Status | Key Signal |
|---------|--------|------------|
| OpenAI / ChatGPT Health | Launched Jan 2026 | Apple Health + medical records integration. 230M weekly health queries. Health Q&A layer, not intervention |
| Google / Gemini Health Coach | Live on Fitbit + iPhone | Personal Health LLM + Large Sensor Model. 24/7 AI coaching |
| Samsung Brain Health | CES 2026 | AI cognitive health for Galaxy Watch/Ring. Dementia detection, stress monitoring |
| Meta "Malibu 2" | 2026 launch | Smartwatch with Meta AI + health tracking. Ray-Ban glasses companion |
| Amazon Health AI | Expanded Mar 2026 | From One Medical to Amazon.com. Personalized health assistant |
| Microsoft Copilot Health | Launched Mar 12, 2026 | Integrates Apple Health, Oura, Fitbit + 50K US EHRs via HealthEx. Harvard Health content. Provider directories |

### Tier 4c: Neurotech
Building the sensing layer. They need intervention protocols.

| Company | Status | Key Signal |
|---------|--------|------------|
| Merge Labs | $250M seed, $850M valuation | OpenAI-backed BCI. Sam Altman's personal bet |
| Neurable | $65M total, $35M Series A | Brain-sensing headphones. HyperX partnership. 5 OEM licenses 2026-2028 |
| Elemind | $20M total | Bezos/Hoffman/Gates backed neurostim. FSA/HSA eligible |
| Subsense | $27M total | Non-surgical BCI via nanoparticles |

### Tier 5: Strategic Acquirers
| Apple Health | Google/Fitbit | ResMed | Masimo | Garmin | Samsung Health |

### Removed Competitors (March 15, 2026)
- **Breathwrk** — Acquired by Peloton for $2.2M (Oct 2025). Investors took a loss on $7.7M raised.
- **Oxa** — Acquired by Myant. Consumer breathing wearable sunset by Oct 2026.

## Key Strategic Insight

The competitive landscape now has **three layers**, and Pausality sits at the intersection of all three:

1. **Big Tech builds the health data layer** (ChatGPT Health, Gemini, Samsung, Meta) — but they do not build clinical protocols
2. **Neurotech builds the sensing layer** (Merge Labs, Neurable, Elemind) — but they do not build interventions
3. **EHRs reduce administrative burden** (Epic, Oracle) — but they do not help clinicians recover from stress

**Pausality is the intervention layer.** The protocol engine that sits between the sensor and the outcome. The only company building clinically validated, biometrically-verified, workflow-embedded ANS regulation for healthcare professionals.

The Breathwrk acquisition ($2.2M) vs. Kaia Health ($285M) proves the thesis: the clinical moat is a 130x valuation multiplier.

## Related Vault Nodes
- `competitive-moat-latency` — Pausality's seconds-to-intervention advantage
- `ip-six-pillar-moat` — the six-pillar IP strategy underpinning defensibility
- `network-audit-credibility-capital-gap` — 102 credibility nodes vs. 19 capital nodes
- `clinician-durability` — core clinical concept that market intelligence validates
- `autonomic-regulation` — the scientific category that the market is discovering
- `tam-keyword-intelligence-breathwork-demand` — search demand signals validating market thesis
