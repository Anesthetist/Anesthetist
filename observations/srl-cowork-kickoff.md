# SRL Knowledge Vault — Cowork Kickoff Brief

**Owner:** Randy Graybeal, MSN, CRNA — CEO & Co-Founder, Somnistics Research Labs
**Date:** March 14, 2026
**Purpose:** This document carries forward the full context from a Claude.ai project conversation into Cowork and Code for persistent, agentic execution. It defines the architecture, inventories the source material, and specifies the build plan for two parallel workstreams: (1) a standards-based knowledge vault, and (2) a real-time biofeedback research tool.

---

## WHO IS RANDY GRAYBEAL

Randy is a CRNA with 28 years of clinical anesthesia experience across transplant, pediatric trauma, and cardiac cases. He co-founded Somnistics Research Labs (SRL) in 2024 in Seattle with Jason Fields (former Head of Design at Amazon/Audible). SRL's product is Pausality, a biometric-verified stress training app that transforms 30-40 daily micro-transitions into one-minute evidence-based breathing sessions with real-time Apple Watch feedback.

Randy's competitive differentiation is applied clinical logic — his multi-domain expertise (anesthesia pharmacology, polyvagal theory, cognitive neuroscience, Vedantic kosha architecture, interpersonal neurobiology, real-time biometrics) is genuinely rare in the corporate wellness market.

### Key People
- **Jason Fields** — co-founder, Head of Product & Technology
- **Livio Marcheschi** — growth PM, Reforge alumnus
- **Ahmed Husain** — UHNW family office network
- **Rob Ashton** — early SAFE investor

### Self-Knowledge Instruments
- CliftonStrengths top 5: Learner, Strategic, Achiever, Maximizer, Ideation
- Enneagram: Type 5 with strong 8 fixation
- PRINT 3-1 assessment on file
- Behavioral Tendencies Analysis on file

---

## THE FIVE RED ARROWS TO PROFITABILITY

Randy uses category theory as a working decision tool. Five composed morphisms (red arrows) must chain sequentially — breaking any one breaks the composition:

1. **Clinical Credibility → Consumer App Downloads** (complete — Pausality live on App Store)
2. **Consumer Traction → Enterprise Proof** (in progress — 88 downloads, 13.9% conversion, 5 countries)
3. **Enterprise Pilot → Enterprise Contract** (next — Mayo Clinic conversations active)
4. **Enterprise Data → Clinical LLM Moat** (planned — the defensive moat)
5. **Platform + CEU → Multi-Stream $1M ARR** (target — B2C + enterprise + ~$100/course CEU)

If an action doesn't advance a red arrow, it's not a priority.

---

## WORKSTREAM 1: KNOWLEDGE VAULT

### The Problem

Randy has 100+ Google Docs, ChatGPT transcripts, and conversation histories containing the most comprehensive, evidence-grounded knowledge base on applied nervous system training that exists anywhere. It's scattered across:
- A "Chatgpt Migration files" Google Drive folder (60+ docs)
- A "MANUALLY COPIED" Google Drive folder
- An "00_ARCHIVE_Original_BLIP_Structure" folder (20+ docs dating to Dec 2024)
- Active SRL Google Drive documents
- Claude.ai conversation histories
- His own embodied clinical expertise from 28 years

Every new conversation requires re-explaining context. Ideas can't be linked or traversed. The manual copy-paste era must end.

### Architecture: Standards-Based, Interoperable, Agent-Ready

NOT a custom "Randy's special vault." A standards-compliant knowledge system that anyone can query via MCP.

**Standards:**
- **Dublin Core** — metadata for every note (title, creator, date, subject, source, relation)
- **SKOS (Simple Knowledge Organization System)** — concept relationships (broader/narrower/related)
- **PROV-O** — provenance chains tracing every claim to its source

**Four Layers:**

```
Layer 0: Evidence Base
  Studies, books, foundational texts
  + Randy's clinical interpretation of each
  = What the literature says (PubMed IDs, key studies, clinical trials)

Layer 0.5: Embodied Knowledge
  Clinical patterns observed in 28 years of practice
  Somatic markers and intuitive expertise
  Craft knowledge — the "how" behind the "what"
  Exemplar stories from transplant, cardiac, pediatric trauma
  = What the body knows that the literature doesn't

Layer 1: Concept Graph
  Original synthesis across disciplines
  Every concept traces to evidence AND embodied knowledge
  ~80-100 distinct concepts identified across the corpus
  = Randy's intellectual genome

Layer 2: Audience Templates
  Who you're speaking to + what evidence depth they need
  CRNAs, ED nurses, corporate executives, yoga teachers,
  investors, researchers, law students (BLIP Clinic)
  = The lens that shapes output

Layer 3: Output Factory
  NeuroMinutes, CEU courses, investor decks, product specs,
  creative content, IP documentation, enterprise proposals
  All generated from Layers 0-2
  = What gets shipped
```

### Vault Structure

```
vault/
  _schema/
    note-types.yaml        # defines all note types and required fields
    relations.yaml         # SKOS relationship types
    audiences.yaml         # registered audience profiles

  concepts/                # SKOS Concept notes
    gap-moment-training.md
    vagal-tone.md
    titration-to-effect.md
    polyvagal-theory.md
    resonant-breathing-frequency.md
    neurominute.md
    neurogating.md
    anterocept.md
    polyanchora.md
    neuro-ouroboros.md
    hemispheric-rebalancing.md
    relevance-realization.md
    self-remembering.md
    kosha-architecture.md
    minimum-effective-dose.md
    multi-phase-interoceptive-coupling.md
    cognitive-variability-analysis.md
    somnistics-field-definition.md
    ...

  evidence/                # Source notes (Dublin Core metadata)
    lehrer-2000-resonance-frequency.md
    porges-2011-polyvagal-theory.md
    van-der-kolk-2014-body-keeps-score.md
    mcgilchrist-2009-master-emissary.md
    vervaeke-relevance-realization.md
    zaccaro-2018-breathing-systematic-review.md
    ...

  observations/            # Clinical/embodied knowledge (Layer 0.5)
    intubation-pattern-recognition.md
    autonomic-shift-pre-monitor.md
    30-40-gap-moments-per-shift.md
    tattoo-grief-encounter-kauai.md
    ...

  audiences/               # Audience profiles
    crna.md
    ed-nurse.md
    corporate-executive.md
    yoga-breathwork-practitioner.md
    investor.md
    researcher.md
    law-student-blip.md
    ...

  outputs/                 # Generated artifacts (versioned)
    neurominutes/
    ceu-courses/
    decks/
    ...

  _index/                  # Auto-generated indexes
    by-subject.md
    by-evidence.md
    by-audience.md
```

### Frontmatter Schema (Every Note)

```yaml
---
id: "urn:srl:concept:gap-moment-training"
type: concept  # concept | evidence | observation | audience | output
title: "Gap Moment Training"
status: draft | review | canonical  # quality gate
creator: "Randy Graybeal"
created: 2026-03-14
modified: 2026-03-14
version: 1.0

# Dublin Core
dc:subject:
  - autonomic-regulation
  - workflow-integration
  - breathwork
dc:source: []

# SKOS relationships
skos:broader:
  - "urn:srl:concept:somnistics"
skos:narrower:
  - "urn:srl:concept:neurominute"
  - "urn:srl:concept:breathe-nudges"
skos:related:
  - "urn:srl:concept:titration-to-effect"
  - "urn:srl:concept:polyvagal-theory"

# Provenance
prov:wasDerivedFrom:
  - "urn:srl:evidence:porges-2011"
  - "urn:srl:evidence:lehrer-2000"
  - "urn:srl:observation:shift-transitions-30-40"
prov:reviewedBy: "Randy Graybeal"
prov:reviewDate: 2026-03-14
---
```

### MCP Server Interface (Target)

```
/concepts                    # list all concepts
/concepts/{id}               # get single concept with full metadata
/concepts/{id}/evidence      # get evidence chain
/concepts/{id}/related       # get SKOS relationships
/search?subject=X            # search by subject tag
/search?type=observation     # filter by note type
/search?status=canonical     # filter by quality gate
/audience/{id}/concepts      # concepts relevant to an audience
/provenance/{claim}          # trace a claim to its sources
```

### Source Document Inventory

**ChatGPT Migration Folder (Google Drive ID: 1hvqRLdZCh-OyKlP2XMrsqj0uzdEH8B9I):**
- 7 Powers / Order Levels analysis
- Mapping the Mind: Cognitive Atlas vs IFS
- ChatGPT Chat History (full export, edited by Mehra)
- Memory Export Requests (2 versions)
- Product for Stress Management
- Deep Dive Summary
- AI Lab Power Protection
- SOC 2 vs HIPAA Compliance
- Clever AI Uses
- ChatGPT Persona Summary
- Enneagram Type Analysis
- Summary of Today's Tasks
- Cross-Reference Report Request
- Curiosity and Burnout Prevention
- Tattoo Symbols and Grief (deeply personal exemplar)
- Bandwidth Saturation and Layers
- Personality Shifts and Life Events
- Clinical Wisdom as Asset
- Leverage vs Task Amplification
- Strategic Positioning Synthesis
- Funding Strategy for Pausality
- Behavioral Tendencies Analysis
- Neuroscience Mindfulness Article Creation
- CVA Framework Exploration
- Blinking Pattern Analysis (Muse 2 EEG)
- CRNA Tester Reward Ideas
- CRNA Stress Management Tools
- AI Neurophysiological Optimization Design
- Mindful Session Scripts (7-day beginner cycle)
- Breathing Basics for Professionals
- CliftonStrengths Insights Summary
- 10x Agency Operationalization

**MANUALLY COPIED Folder (Google Drive ID: 1feXo-ElZM0BfuGgb5QIBx-p3P3Q-7Lo9):**
- Contains additional hand-migrated ChatGPT conversations

**Archive — 00_ARCHIVE_Original_BLIP_Structure (Google Drive ID: 1HapfWLMO-w1bSNBiB4sFgUhC3Q3ZCxhc):**
- Somnistics Research Labs Glossary of Novel Concepts (2 versions, Dec 2024)
- Metadata for Engineers Somnistics
- SRL White Papers
- Telepathy Curriculum Draft (original 21-day design)
- Intellectual Property Somnistics Research Labs
- From the Lab: Binaural Beats
- 4/7/8 Layer Structure
- Somnistics: A Definition in Human Potential Optimization
- Third and Fourth Order Effects of the Koshas Framework
- Fast Improved Humans
- Impact Filter for MVP Development
- How We Differ: PTSD Prevention Frameworks Compared
- Encourage Me in the Path
- Defining Terms
- Randy's Priorities and Thought Process
- Non-tech Cofounder Version
- Details Flow
- Tension Awareness Loops

**Active SRL Drive (standalone docs, March 2026):**
- AANA Category A CEU Draft
- Resonance with Somnistics
- Somnistics Definition Request / Summary
- Pausality Venture Scale Investor Deck Blueprint
- Research for Pausality App
- Pausality Briefing Draft / Definition Summary
- Somnistics .md File / Research Overview
- Analyze Paper for Somnistics
- BLIP3-o for Mental Health
- BLIP Clinic: Engagement Summary, Ventures Summary, 7-Day Experience, Persona 2025
- Anesthesia Clinician GPT Creation
- Teaching Breathing to Clinicians
- Clinician Durability Meaning
- Interoception: multiple deep dives (Schandry Task, outcome strategy, high performers, survey, criticality + readiness model)
- Fascia and Nervous System Integration
- Nervous System Mastery Solution / Management Overview
- Somnistics and Interoception / Field Breathwork
- Vagalbeats and Nervous System Evolution
- Neuro-visionary Breathwork Architect
- SRL Interoception Research Bot Analysis (Sept 2025)
- Novel Concepts Project Summary
- Strategic Knowledge Comparison
- Mayo Clinic: Call Prep, Tech Assessment, Metrics & KPIs Framework, Sonsiel Meeting
- Freedom to Operate Analysis: Gap Moments
- Clinical One Pager (SRL)
- Somnistics Trademark Search Results
- Pausality Testimonial Optimization
- Tech-Driven Therapy Solutions
- ChatGPT is Not Specific / Sharing ChatGPT Dialogues
- Using ChatGPT API / Somnistics ChatGPT App / Traits for ChatGPT-5
- AI in Daily Workflows / Plugin Manifest Explanation
- ClickUp Migration Plan

### Migration Steps

1. **Define the schema** — create `_schema/` files (note-types.yaml, relations.yaml, audiences.yaml)
2. **Seed from Glossary of Novel Concepts** — extract ~50 core concepts with SKOS relationships
3. **Seed from Freedom to Operate analysis** — extract IP landscape as evidence notes
4. **Layer in Archive docs** — decompose conversations into concept/evidence/observation notes
5. **Layer in ChatGPT Migration docs** — same decomposition process
6. **Layer in active SRL docs** — same process
7. **Randy reviews and promotes** — draft → review → canonical quality gates
8. **Build MCP server** — standard query interface for any agent
9. **Connect to production** — Claude project, Pausality dev, CEU courses, investor materials

---

## WORKSTREAM 2: BIOFEEDBACK RESEARCH TOOL (Option C)

### Architecture

```
Muse 2 (EEG) → Mind Monitor app → OSC over WiFi → Mac Python Server
Polar H10 (HR/HRV) → BLE → Mac Python Server
Mac Python Server → WebSocket → iPad Safari (Dashboard)
```

Mac as local receiver. Both data streams from day one. Strict 60-second NeuroMinute format.

### Phase A (Week 1): "Does It Work?"
- Mac Python server with OSC receiver + BLE Polar connection via `bleak`
- Minimal iPad dashboard: connection status, live HR, live EEG band bars
- One breathing protocol (Coherent 5.0) with visual guide
- Basic baseline capture (60s eyes open)
- Simple score: HR drop + subjective rating
- Before/after comparison display

### Phase B (Week 2): "Compare Protocols"
- Protocol library (8-10 variants)
- Recommendation logic (suggest next based on previous scores)
- HRV coherence scoring (RR interval processing)
- EEG band power scoring (alpha change, theta/alpha ratio)
- Session summary with protocol comparison chart
- Session persistence (SQLite)

### Phase C (Weeks 3-4): "Enterprise-Ready Artifact"
- Polish to Pausality brand (Deep Navy #22253A, Soft Sage #5FC89B, Poppins)
- Exportable summary (PDF or screenshot-optimized)
- Multi-user support
- Refined scoring weights
- Demo mode with real data for live sales presentations

### Open Research Questions
1. Is 60 seconds enough for measurable EEG shifts via consumer-grade Muse 2?
2. How many protocols per sitting before fatigue corrupts data?
3. Optimal recovery window between protocol tests?
4. Does subjective rating correlate with biometric score?
5. Which EEG metrics move reliably during a 60-second breathing protocol?

---

## BREATHE NUDGES — CONTEXT FOR CLINICAL LLM EVAL SUITE

Jason Fields authored a PRD (v1.1, March 13 2026) for Breathe Nudges: opt-in background heart rate monitoring via Apple Watch with contextual session nudges. Three nudge types (elevated resting HR, high HR while inactive, session interval reminder), all default OFF.

The analytics events in this PRD (nudge_fired, nudge_opened, nudge_session_completed, nudge_dismissed) are the seed of the Clinical LLM eval suite:

| Eval Category | SRL Implementation | Grading Method |
|---|---|---|
| Task completion | Did recommended protocol produce >5 bpm HR drop? | Deterministic (biometric) |
| Tool use correctness | Did LLM select right protocol from 21-session curriculum? | Rule-based + clinical review |
| Reasoning quality | Is personalization rationale physiologically sound? | Randy-as-judge |
| Safety/guardrails | Does recommendation stay in wellness framing? No diagnostic language? | Rule-based FDA filter |
| Efficiency | Did personalization improve outcomes vs. default curriculum? | A/B comparison |
| Robustness | Handles missing HR data, Watch disconnection, incomplete sessions? | Multi-trial from production traces |

Randy's clinical review notes on the PRD:
- High HR While Inactive threshold floor (155 bpm) may be too high — consider adding 135 and 145 bpm
- "Heart rate spike detected" borders on diagnostic language — suggest "Your heart rate is higher than usual while you're at rest"
- Notification permissions: defer to first nudge enable, not onboarding
- Session selection from nudge: launch next uncompleted curriculum session (preserve progressive structure)
- Watch complication: yes, but post-v1 (scope creep)
- Nudge fatigue: build it — after 5 consecutive dismissals, prompt threshold adjustment (titration to effect applied to the notification system itself)
- Add "first nudge" special copy reinforcing Gap Moment Training framing

---

## BRAND SYSTEM

- **Colors:** Deep Navy #22253A, Soft Sage #5FC89B, Off-white #F5F5F0
- **Font:** Poppins only. Normal (400) headers, Light (300) body. Body tracking: -0.025em
- **Gradient** (logo only): 45deg, #3A61AD → #1479B6 → #5FC89B → #96F0BE
- **Trademarked terms:** Gap Moment Training™, NeuroMinute™, Pausality™
- **Key terminology:** somnistics, minimum effective dose, titration to effect, BOLT scores, MAIA-2, RMSSD, HRV coherence, resonant breathing frequency, vagal tone

---

## KEY PRINCIPLES

- If an action doesn't advance a red arrow, it's not a priority
- Evidence-based: every claim traces to a source through the provenance chain
- Embodied wisdom is captured through exemplars, contrast cases, and clinical stories — not just propositions
- Titration to effect applies to everything: protocols, nudge thresholds, curriculum progression, business strategy
- The moat isn't the AI. The moat is who defines the arena.
- Plan thoroughly before building. Randy has consistently redirected toward planning first.
- Team-based decisions on major choices — Randy, Jason, Livio commit together

---

## FIRST TASKS FOR COWORK

1. **Read this document completely.** It is the arena definition.
2. **Sync Google Drive locally** if not already done (Drive for Desktop).
3. **Create the `_schema/` files** — note-types.yaml, relations.yaml, audiences.yaml.
4. **Fetch and read the "Somnistics Research Labs Glossary of Novel Concepts"** from the Archive folder. Extract every concept into a skeleton note with SKOS frontmatter.
5. **Fetch and read the "Freedom to Operate Analysis"** from the SRL Drive. Extract IP landscape into evidence notes.
6. **Begin systematic document-by-document decomposition** of the Archive folder, then the ChatGPT Migration folder, then the active docs. For each: identify concepts, evidence citations, clinical observations, and audience-relevant framings. Create notes. Link them.
7. **After 50+ notes exist:** build the MCP server with the standard interface defined above.

## FIRST TASKS FOR CODE

1. **Read this document completely.**
2. **Set up the Python project** for the biofeedback tool (Option C architecture).
3. **Implement the OSC receiver** for Mind Monitor (Muse 2 EEG stream).
4. **Implement the BLE connection** for Polar H10 via `bleak`.
5. **Build the minimal WebSocket server** that pushes both streams to Safari.
6. **Build the Phase A iPad dashboard** — connection status, live HR, live EEG bands, one breathing protocol with visual guide.
