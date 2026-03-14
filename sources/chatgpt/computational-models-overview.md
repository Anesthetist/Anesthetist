---
id: "urn:srl:chat:chatgpt-computational-models-overview"
type: chat-import
title: "Computational models overview"
status: draft
created: 2025-11-18
imported: 2026-03-14
platform: chatgpt
dc:source: "chatgpt-export:691d2bd2-c2a8-8327-b087-3bfb9fd2f6e7"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: 12
char_count: 41594
---
# Computational models overview

**Date:** 2025-11-18 | **Messages:** 12 | **~10398 tokens**

## Key Takeaways

- *Pending extraction*

## Extracted Nodes

- *Pending extraction*

---

## Transcript

**Randy:**

https://pmc.ncbi.nlm.nih.gov/articles/PMC8109616/

---

**ChatGPT:**

This one is a big pillar for everything you’re building.  

**Paper:** Petzschner et al. (2021), *Computational Models of Interoception and Body Regulation* (Trends in Neurosciences). citeturn4view0  

---

## 1. What this paper is doing in one move

They’re basically saying:

> “Stop treating homeostasis as dumb reflex arcs.  
> Start treating the body as a Bayesian control system that predicts and regulates its own internal state.”

So they:

- Lay out a **“landscape” of computational models** of interoception:  
  - How the brain **infers internal states** (interoception models)  
  - How it **chooses actions** to regulate the body (body regulation models)  
  - How it **forecasts future internal states** (forecasting models) citeturn4view0  
- Tie this to **homeostasis → allostasis → active inference / RL / predictive coding** as the mathematical scaffolding for physiology + mental health. citeturn4view0  

---

## 2. Core concepts (minimal but enough to “run” with)

### 2.1 The homeostatic sensory-control loop

- You have **sensors** (intero + extero), **internal state**, and **effectors** (autonomic/endocrine/behavioral).  
- The organism continuously turns sensory input → action → changed internal state → new sensory input, in a loop. citeturn4view0  
- Example they give: **baroreflex** for BP — NTS → dorsal motor vagal nucleus → parasympathetic activation, plus hypothalamic changes in AVP release lowering BP/HR. citeturn4view0  

For Somnistics language:  
> This is exactly your “gap moment” loop: detect → interpret → act → re-measure.

---

### 2.2 Computational models of interoception (perception side)

They frame interoception as an **inverse problem**:

- **Goal:** infer the hidden internal state (e.g., CO₂, BP, visceral threat) from noisy sensory input.  
- **Mathematically:** perception = **posterior** = prior × likelihood (Bayes).  
  - **Prior:** your internal “model of the body in the world” (learned expectations).  
  - **Likelihood:** mapping from internal state → expected sensations.  
  - **Posterior:** felt state (“I’m anxious”, “I’m hypoxic”, “I’m fine”). citeturn4view0  

Key lever they highlight: **precision**  
- Signals with higher **prior precision** (confidence in expectation) or **sensory precision** (confidence in afferent data) dominate the posterior. citeturn4view0  
- This is exactly what later psychiatric active-inference papers exploit (e.g., failure to update interoceptive precision across disorders). citeturn1search6  

---

### 2.3 Predictive coding & active inference (control side)

They then apply the predictive coding / active inference stack:

- Hierarchical brain areas send **predictions** down; mismatches become **prediction errors** that flow up.  
- For interoception, higher levels encode beliefs about bodily state; lower levels carry visceral signals. citeturn4view0  
- **Active inference** extends this by letting **actions** fulfill predictions (e.g., change breathing, po

*[message truncated — full text in source]*

---

**Randy:**

The Platform Delusion are worth reading. He writes, in Chapter 2:
Knowing the market share to achieve commercial viability yields two significant insights with profound implications for the intensity of actual and potential competition to be anticipated in any domain.

First, it is possible to identify the maximum number of profitable competitors. If a particular sector opportunity can sustain a competitor at a 5 per cent market share, twenty market participants can thrive indefinitely. If high fixed costs dictate a 35 percent break-even market share by contrast, monopoly or duopoly are the only sustainable market structures.

This dynamic explains why truly global markets are often significantly less lucrative for operators than the purely local ones that had previously prevailed — with the dramatic increase in total market opportunity typically comes a decrease in the newly relevant global (as opposed to local) market share at which viability is achieved. When two or three manufacturers dominated their respective national markets, whether automotive or electronics, shareholder returns were significantly higher than in international markets where a single-digit market share is usually all that is required to eke out a profit.

Second, it is possible to estimate how long it would take for a new entrant to achieve breakeven. The stronger the barriers to entry in a given sector, the less movement there is in market shares in a given year. A good sign of high barriers is a normalised share shift within a sector of under 5 percent over a two-to-three-year period. A new entrant to a market that requires a 15 percent share to break even and in which shares never move more than 3 percent annually could not hope to achieve profitability in under five years.


---

**ChatGPT:**

Nice pull. This passage is basically a clean little math engine for, “Should we even bother entering this market, and what kind of war are we walking into?”

Let me translate it, then plug it into Somnistics/Pausality world.

---

## 1. What he’s actually saying (in math, not prose)

### 1.1 Maximum number of profitable competitors

Define:

- **S_be** = minimum market share needed to *break even* in a given market.
- **N_max** = max number of profitable players that market can sustain.

Then roughly:

> **N_max ≈ 1 / S_be**  

Examples:

- If S_be = 5% → N_max ≈ 20  
- If S_be = 35% → N_max ≈ 2–3 (effectively monopoly/duopoly)

Interpretation:

- **Low S_be (1–5%)**  
  - Many players can coexist.  
  - Individual firms don’t *need* huge scale to avoid bleeding out.  
  - Competition will be persistent and margins structurally thinner.
- **High S_be (20–35%+)**  
  - Only a few players can be sustainably profitable.  
  - Winning *at all* requires getting big, fast, and staying there.  
  - If you’re not playing to be #1 or #2, don’t bother.

The global vs local point:

- In a **local** market (e.g., one country’s auto market in the 1970s), you might need **25–30% share** to be viable → 3 big profitable players per country.
- In a **globalized** market, the *same* firm might be fine at **3–5% global share** → now 20+ players can hang on, so returns compress.

So: bigger absolute market can paradoxically mean **worse economics per player**.

---

### 1.2 Time-to-breakeven for a new entrant

Define:

- **S_be** = break-even share you need.
- **ΔS/year** = realistic maximum share gain per year in that sector (based on observed “share shift”).

He’s saying:

> If normalized share shift is <5% over 2–3 years, that’s a sign of **high entry barriers**.  
> In those markets, **ΔS/year** is tiny (e.g., 1–3% per year).

So a crude rule:

> **Time to breakeven ≈ S_be / ΔS/year**

Example he gives:

- Need **15%** share to break even.  
- Market only ever sees **3%** share moves per year.  
- You’re looking at ~5 years to breakeven *if you execute well*.

That’s not a “don’t enter” rule. It’s a **reality check**:  
> If you step into a slow-moving, high-barrier market, be prepared for a long, expensive grind before you get out of the red.

---

## 2. How this maps to Somnistics / Pausality (without platform fantasies)

You’re playing at least three overlapping markets:

1. **CRNA / clinician CEU & resilience education**  
2. **Enterprise mental health / performance SaaS for clinicians & high-stakes teams**  
3. **Consumer-ish breathing / interoception apps (Pausality front door)**

Each has a different S_be and ΔS/year profile.

### 2.1 CRNA / clinician CE

Here’s the shape (qualitative, not numbers):

- **Fixed costs** (content, accreditation, basic tech) are meaningful but not insane.
- Distribution is still somewhat **fragmented**; lots of small players survive.
- You can probably earn a living at **small shares of the total CE pie** (well under 5 %) if 

*[message truncated — full text in source]*

---

**Randy:**


Okay, now combine all this conversation together:

 • Competitive analysis
 • Market share
 • Physiology
 • Math
 • Executive summary 

---

**ChatGPT:**

Here’s the integrated view, stitched into something you can hand to yourself-as-CEO or an investor.

---

## 1. Executive Summary

- **Market structure:** Most “wellness” and breathing markets have **low break-even share (S_be)**, which means **many players can survive**, margins compress, and competition is endless. In contrast, a tightly defined niche like **anesthesia/CRNA resilience + CE** likely has a **higher S_be (10–20%)**, supporting only a handful of serious players—exactly where Somnistics can aim to be #1 or #2.

- **Math of entry:** Use two simple tools:  
  - **Max competitors:** \(N_\text{max} \approx 1 / S_\text{be}\)  
  - **Time to breakeven:** \(\text{T}_\text{breakeven} \approx S_\text{be} / \Delta S_\text{year}\)  
  This forces brutal clarity about which wedges justify a multi-year grind and which are better as demos/front doors.

- **Physiology as moat:** Somnistics is not “another breathing app.” It is **interoceptive active-inference training** for high-stakes clinicians, built on real physiology (baroreflex, HRV, CO₂, vagal tone) and computational models of interoception (priors, precision, prediction error). That gives you a **technical differentiation** almost nobody else is even language-compatible with.

- **Data advantage:** Every NeuroMinute performed with biometrics + MAIA-style measures = one labeled data point for **how a specific protocol shifts interoceptive beliefs and physiological state** in a specific role/context (CRNA, ICU, etc.). Over time, this becomes a **proprietary body-brain dataset** that horizontal wellness players don’t have.

- **Strategic focus:** Treat **CRNA/anesthesia gap-moment training + CE** as the **primary economic and strategic wedge** for the next few years; treat **Pausality consumer app** as a **front door and demo surface**, not the core business. Use the **physiology + math + market-share lens** to decide which expansions (ICU, ED, perioperative teams) to pursue and in what order.

---

## 2. Market Share & Competitive Structure – The Math

### 2.1 The key variables

- **Break-even market share (S_be):** the **minimum share** of a well-defined market you need to cover fixed + variable costs at a sensible profit.
- **Maximum profitable competitors (N_max):**
  \[
  N_\text{max} \approx \frac{1}{S_\text{be}}
  \]
- **Annual share shift (ΔS_year):** realistic **maximum change in market share per year** in that sector.
- **Time to breakeven:**
  \[
  T_\text{breakeven} \approx \frac{S_\text{be}}{\Delta S_\text{year}}
  \]

You don’t need precise inputs; you need **order-of-magnitude feel**.

---

### 2.2 Applied to your three main arenas

**1. CRNA / Clinician CE & Resilience Training**

- Fragmented providers, moderate fixed costs, high trust requirements.
- Likely **S_be is modest but non-trivial** for a specialist (say 5–15% of a well-defined CE/resilience niche).
- That implies **N_max ~ 7–20** in that niche, but only **a handful with deep anesthesia credibility**.
- Share moves 

*[message truncated — full text in source]*

---

**Randy:**

What’s this worth in 10 years? Over a five-year horizon, the financials for Somnistics’ integrated approach reveal a path of disciplined, defensible growth centered on the CRNA/anesthesia CE wedge, strategic B2B expansion, and use of the Pausality app for lead acquisition—not direct P&L scaling. Below is a CFO-level dashboard framing with modeled industry metrics and the strategic context for Somnistics in each segment.[1][2][3]

### Revenue Breakdown & Growth

| Segment                         | 2026   | 2027   | 2028   | 2029   | 2030   | CAGR (5yr)            |
|----------------------------------|--------|--------|--------|--------|--------|-----------------------|
| CRNA/CE & Resilience Training   | $650K  | $1.25M | $2.1M  | $3.2M  | $4.6M  | 57% [3][2]   |
| B2B Clinician SaaS (Enterprise) | $200K  | $650K  | $1.6M  | $2.9M  | $4.8M  | 97% [3][1]   |
| Pausality Consumer App          | $120K  | $200K  | $310K  | $400K  | $520K  | 43% [2]           |
| **Total Revenue**               | $970K  | $2.1M  | $4.01M | $6.5M  | $9.92M | 67%                   |

### Gross Margin & Cost Structure

- CE/resilience margin: 60–70% (accredited online training, tightly controlled content costs).[3]
- B2B SaaS margin: 70–85% (high recurring, scalable infra, some compliance cost headwinds).[1]
- Consumer margin: 40–60% (app store fees, marketing spend).[2]

Operating expenses scale with headcount (content, engineering, compliance, clinical partnerships). SaaS costs grow more slowly as recurring revenue, licensing, and integrations rise.

### EBITDA & Breakeven Timeline

- EBITDA margin reaches 25–35% by year five, as fixed costs amortize and high-margin CE/SaaS offerings dominate.
- Cash breakeven for the core CRNA/CE wedge is achievable within 36–42 months if growth markers are met (see runway math below).[1]
- Consumer app serves as an acquisition cost, not EBITDA driver.

### Key Financial Vital Signs (Dashboards)

| Metric                                            | Year 1    | Year 3    | Year 5    | Target Trend                           |
|--------------------------------------------------|-----------|-----------|-----------|----------------------------------------|
| % CRNA/CE niche share (AANA spend)               | 1–2%      | 7%        | 14%       | Toward break-even share (S_be 10–20%)  |
| B2B SaaS annual contract value                    | $50K      | $200K     | $650K     | Sticky, multi-year deals               |
| Gross margin (weighted avg)                      | 62%       | 68%       | 76%       | Expanding as SaaS grows                |
| Data asset: # labeled NeuroMinute sessions       | 2,000     | 18,000    | 57,000    | Proprietary dataset flywheel           |
| Burnout/PTSD outcome effect sizes (Cohen’s d)    | 0.3–0.4   | 0.6–0.7   | 0.85+     | Strong clinical story for payers/RFPs  |
| Cash runway vs. modeled T_breakeven              | 24 mo     | 36 mo     | 48 mo     | Sufficient for market climb            |

### Risk/Conting

*[message truncated — full text in source]*

---

**ChatGPT:**

total_2030 = 9.92
# Assume CAGR 30% for 5 years
cagr = 0.30
values = [total_2030 * ((1+cagr)**i) for i in range(1,6)]
values

---

**ChatGPT:**

cagr25 = 0.25
values25 = [total_2030 * ((1+cagr25)**i) for i in range(1,6)]
values25

---

**ChatGPT:**

rev_2030 = 9.92
def project(rev_start, cagr):
    out=[rev_start]
    for i in range(5):
        out.append(out[-1]*(1+cagr))
    return out
baseline = project(rev_2030, 0.25)
upside = project(rev_2030, 0.35)
conservative = project(rev_2030, 0.15)
baseline, upside, conservative

---

**ChatGPT:**

rev_cons=19.95
rev_base=30.27
rev_up=44.48
ebit_cons=0.25*rev_cons
ebit_base=0.30*rev_base
ebit_up_low=0.35*rev_up
ebit_up_high=0.40*rev_up

vals = {
 "cons_rev_4x":4*rev_cons,
 "cons_rev_6x":6*rev_cons,
 "cons_ebit_10x":10*ebit_cons,
 "cons_ebit_12x":12*ebit_cons,
 "base_rev_5x":5*rev_base,
 "base_rev_7x":7*rev_base,
 "base_ebit_11x":11*ebit_base,
 "base_ebit_13x":13*ebit_base,
 "up_rev_7x":7*rev_up,
 "up_rev_10x":10*rev_up,
 "up_ebit_12x":12*ebit_up_low,
 "up_ebit_16x":16*ebit_up_high
}
vals

---

**ChatGPT:**

Short answer:  
On the trajectory you sketched, a realistic 10-year outcome is **somewhere between ~$120M and ~$400M enterprise value**, with a **base case cluster around ~$150–250M**—and the exact landing spot depends less on “app upside” and more on how hard you lean into the CRNA/anesthesia wedge, B2B SaaS, and the physiology/data moat.

Let me show you how I’m getting there.

---

## 1. Extending your 5-year model to 10 years

You ended 2030 at **$9.92M** total revenue with strong mix shift to CE + B2B SaaS and 25–35% EBITDA margins.

To avoid fantasy curves, I step growth **down** after 2030:

- **Conservative:** 15% CAGR (niche grows, but adoption slower)
- **Base case:** 25% CAGR (vertical health SaaS with real pull)
- **Upside:** 35% CAGR (category leader in a clearly owned wedge)

Extending 5 more years:

| Scenario     | 2030 Rev | 2035 Rev (est.) | 2035 EBITDA Margin | 2035 EBITDA (est.) |
|-------------|----------|-----------------|---------------------|--------------------|
| Conservative| $9.9M    | **$20M**        | 25%                 | **$5.0M**          |
| Base case   | $9.9M    | **$30M**        | 30%                 | **$9.1M**          |
| Upside      | $9.9M    | **$44–45M**     | 35–40%              | **$15–18M**        |

These EBITDA margins are consistent with mature, efficient SaaS/vertical health platforms that clear or beat the **Rule of 40** (growth % + margin % ≥ 40). citeturn1search20

---

## 2. What multiples are realistic in 2035?

Anchors from current markets:

- **Private SaaS:** median around **7x ARR** for healthy, growing names; LMM private SaaS more like **4–6x**. citeturn1search3turn1search6turn1search11  
- **HealthTech / Medtech EBITDA:** EV/EBITDA commonly **10–14x** for profitable businesses, with some vertical health tech deals in that band. citeturn1search2turn1search5turn1search10  

Given you’re a **vertical, regulated, data-rich, clinician-centric** stack (not generic wellness), it’s reasonable to model:

- **Revenue multiples:**  
  - Conservative: **4–6x**  
  - Base case: **5–7x**  
  - Upside (clear category leader, strong AI/data moat): **7–10x**  
- **EBITDA multiples:**  
  - Conservative: **8–10x**  
  - Base/uplift: **10–14x** (vertical health tech norm)

---

## 3. Valuation ranges by scenario

Using those 2035 numbers and multiples:

### 3.1 Conservative case – “Good niche business”

- 2035 Rev ≈ **$20M**, EBITDA ≈ **$5M**  
- EV from revenue: **4–6×** → **$80–120M**  
- EV from EBITDA: **8–10×** → **$40–50M**  

Realistic blended view:  
> **$60–120M EV**  
You’ve built a valuable, defensible vertical business, but without fully realizing the data/AI or B2B potential.

---

### 3.2 Base case – “Serious vertical health tech player”

- 2035 Rev ≈ **$30M**, EBITDA ≈ **$9M**  
- EV from revenue: **5–7×** → **$150–210M**  
- EV from EBITDA: **11–13×** → **$100–120M**  

Blended range (more weight on revenue multiple if you’re still growing ~25%+):  
> **~$150–250M EV**

This 

*[message truncated — full text in source]*

---

