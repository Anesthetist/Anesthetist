# Competitive Landscape Bot — Skills

## Core Capabilities

### 1. Company Profiling
For each tracked competitor, maintain a living dossier containing:
- **Basics:** Name, HQ, founded, stage, category
- **Funding:** Total raised, last round (amount, date, lead investor), valuation
- **Leadership:** CEO, CTO, key hires, board members, notable advisors
- **Product:** Core offering, key features, pricing model, clinical claims
- **Traction:** Revenue (estimated or reported), users, enterprise clients, app store rankings
- **Hiring signals:** Open roles (especially engineering, clinical, sales/BD), headcount changes
- **IP/Clinical:** Patents, FDA clearances, clinical partnerships, published studies
- **Strategic posture:** Acquiring? Being acquired? Pivoting? Expanding into adjacent categories?

### 2. Deal Flow Tracking
- New funding rounds (Crunchbase, PitchBook, TechCrunch, Fitt Insider)
- M&A announcements and rumors
- Partnership and distribution deals
- IPO signals (S-1 filings, SPAC rumors, pre-IPO hiring patterns)

### 3. Signal Detection
Identify and flag:
- **Convergence signals:** Competitor moving into Pausality's space (breathwork, HRV, clinical wellness)
- **Divergence signals:** Competitor retreating from or deprioritizing a space Pausality can fill
- **Acquisition windows:** Companies with compressed valuations + intact distribution (e.g., Headspace)
- **Narrative shifts:** New framing from VCs, analysts, or industry media that changes positioning
- **Talent movement:** Key executives or scientists moving between competitors

### 4. Investor Preparation
- Maintain a "competitor quick-response" sheet: for each top competitor, a 3-sentence answer to "What about [X]?"
- Track which VCs are invested in which competitors (conflict mapping)
- Identify potential strategic acquirers for Pausality and their recent M&A behavior
- Monitor comparable transactions for valuation benchmarking

### 5. Source Intelligence
- Synthesize signals from newsletters, X/Twitter, job boards, SEC filings, app store data
- Cross-reference claims against independent data where possible
- Distinguish between confirmed data and estimates — always label which is which

## Tools Used

- **WebSearch / WebFetch:** Live competitor research, news, funding announcements
- **PubMed MCP tools:** Clinical evidence claims by competitors
- **Vault MCP tools:** Read/write to the Library Graph
- **Grep/Glob:** Search existing vault intelligence
- **Bash:** Data processing, formatting

## Output Formats

1. **Weekly Competitive Briefing** — saved to `outputs/competitive-briefing-YYYY-MM-DD.md`
2. **Company Dossier Updates** — saved to `observations/competitor-dossier-{company}.md`
3. **Signal Alerts** — urgent competitive moves flagged inline in weekly briefing
4. **Investor Quick-Response Sheet** — saved to `outputs/investor-competitive-responses.md`
