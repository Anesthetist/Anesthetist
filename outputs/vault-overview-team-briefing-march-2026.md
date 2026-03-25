# Somnistics Research Labs: The Library Graph Vault System

## Internal Team Briefing — March 2026

**Prepared for:** Jason Fields (Co-Founder, Head of Product & Technology), Livio Marcheschi (Growth PM), SRL Team
**Prepared by:** Randy Graybeal, MSN, CRNA — CEO & Co-Founder
**System built with:** Claude Code (Anthropic), agentic build session

---

## Executive Summary

We built a **standards-based knowledge vault** that captures everything SRL knows — Randy's 28 years of clinical anesthesia, all 10 trademarked frameworks, 87 clinical observations, 12 peer-reviewed evidence sources, and the strategic IP behind Pausality — in a structured, machine-readable, agent-queryable system.

This is not documentation. This is the **ontology moat** described in our 6-pillar IP strategy. Every claim traces to evidence. Every concept links to related concepts. Every observation connects to the clinical experience that produced it. The vault is shared state between human editing (Obsidian) and AI processing (Claude, Gemini, Perplexity) via MCP.

**By the numbers:**
- 133 structured notes across 4 layers
- 34 concept definitions (24 promoted to "canonical" by Randy)
- 10 trademarked novel frameworks fully documented
- 87 clinical observations from 28 years of practice
- 861 ChatGPT conversations + 65 Google Drive docs imported as source material
- 9 MCP server tools for any AI agent to query the vault
- 21 git commits tracking every change

---

## The Problem This Solves

Randy has the most comprehensive, evidence-grounded knowledge base on applied nervous system training that exists anywhere. Before the vault, it was scattered across:

- 100+ Google Docs
- 861 ChatGPT conversation histories
- Claude.ai project conversations
- Google Drive folders (personal + SRL)
- His own embodied expertise from 28 years

Every new conversation required re-explaining context. Ideas couldn't be linked or traversed. The same questions got re-answered. The IP was real but not defensible because it wasn't structured. AI agents couldn't access the knowledge without Randy manually copying it in.

**The vault ends the manual copy-paste era.**

---

## Architecture: Four Layers + Sources

The vault follows a layered architecture where each layer builds on the ones below it:

```
Layer 0:   EVIDENCE BASE (12 notes)
           Studies, books, foundational texts with Dublin Core metadata
           Porges, Lehrer, McGilchrist, Balban, Siegel, etc.
           = What the literature says

Layer 0.5: EMBODIED KNOWLEDGE (87 notes)
           Clinical patterns observed across 28 years
           Somatic markers, craft knowledge, exemplar stories
           = What the body knows that the literature doesn't

Layer 1:   CONCEPT GRAPH (34 notes)
           Original synthesis across disciplines
           Every concept traces to evidence AND embodied knowledge
           10 trademarked novel frameworks
           = Randy's intellectual genome

Layer 2:   AUDIENCE PROFILES (7 notes)
           Who you're speaking to + evidence depth they need
           CRNAs, executives, investors, researchers, law students
           = The lens that shapes output

Layer 3:   OUTPUT FACTORY (future)
           NeuroMinutes, CEU courses, investor decks, product specs
           All generated from Layers 0-2 with full provenance
           = What gets shipped
```

**Source Layer:** 861 ChatGPT conversations + 65 Google Drive documents serve as the raw material that was systematically mined to create Layers 0-1.

---

## Three International Standards

The vault uses three established standards for interoperability — this isn't "Randy's special system," it's a standards-compliant knowledge architecture that any tool can query.

### Dublin Core (ISO 15836) — Metadata for Every Note

Every note carries Dublin Core metadata: title, creator, date, subject tags, source references, identifier (URN format). This means every note is discoverable, sortable, and citable using the same standard that libraries, museums, and academic databases use worldwide.

**Example:**
```yaml
id: "urn:srl:concept:gap-moment-training"
title: "Gap Moment Training"
creator: "Randy Graybeal"
dc:subject: [somnistics, intervention-timing, state-transitions, breathwork]
dc:source: ["chatgpt-export:gap-moments-across-philosophies"]
```

### SKOS (Simple Knowledge Organization System) — Concept Relationships

Every concept note has SKOS relationships defining how it connects to other concepts:
- **broader:** Parent concept (Gap Moment Training is broader than NeuroMinute)
- **narrower:** Child concept (NeuroMinute is narrower than Gap Moment Training)
- **related:** Lateral association (Gap Moment Training is related to Titration to Effect)

This creates a **traversable concept graph** — you can start at any concept and navigate the entire knowledge network through its relationships. Obsidian's graph view renders this visually.

**Example:**
```yaml
skos:broader: [somnistics]
skos:narrower: [neurominute]
skos:related: [titration-to-effect, polyvagal-theory, vagal-tone, anterocept]
```

### PROV-O (Provenance Ontology) — Evidence Chains

Every claim traces back to its source through PROV-O provenance links. When the vault says "slow breathing activates the ventral vagal pathway," it points to Porges 2011, Lehrer 2000, and Zaccaro 2018 as the evidence. When it says "CRNAs experience 30-40 gap moments per shift," it points to Randy's 28-year clinical observation.

**Example:**
```yaml
prov:wasDerivedFrom:
  - "urn:srl:evidence:porges-2011-polyvagal-theory"
  - "urn:srl:evidence:lehrer-2000-resonance-frequency"
  - "urn:srl:observation:shift-transitions-30-40"
```

**Why this matters:** No competitor can replicate this provenance depth. When a hospital asks "what's the evidence for this?", the vault answers with specific citations, clinical observations, and the chain connecting them. This is the clinical credibility moat in structured form.

---

## Quality Gates: Draft, Review, Canonical

Every note has a status field tracking its verification level:

| Status | Meaning | Who Decides |
|--------|---------|-------------|
| **draft** | Initial extraction — content captured but not verified | AI agents |
| **review** | Enriched with definitions, evidence, and SKOS links — ready for human review | AI agents |
| **canonical** | Randy has verified the definition is accurate and complete | Randy only |

Currently: **24 concepts are canonical** (Randy-verified), 10 are at review status, and all 87 observations + 12 evidence notes are awaiting review. Only Randy can promote to canonical — this is the quality gate that ensures the vault represents his actual knowledge, not AI interpretation.

---

## The 10 Trademarked Frameworks

These are SRL's core IP — each fully documented with definitions, mechanisms, evidence chains, and clinical applications:

| Framework | What It Does |
|-----------|-------------|
| **Gap Moment Training** | Repurposes 30-40 daily micro-transitions into 60-second training reps for nervous system regulation |
| **NeuroMinute** | The 60-second protocol format: breath + interoception + binaural beats + biometric feedback |
| **Anterocept** | Progressive interoceptive spectrum from simple breath awareness to multi-layered sensory integration. 4-layer architecture with predictive modeling. |
| **Neurogating** | AI-driven adaptive triggering — watches multimodal biometrics, classifies autonomic state, delivers the right intervention at the right moment |
| **Polyanchora** | Multi-anchor attentional scaffolding — 7 simultaneous sensory channels within 60 seconds |
| **Neuro-Ouroboros** | Recursive 21-day curriculum. Full patent spec: Kalman filtering, PWTT, dopaminergic cueing, gamified loop structure. |
| **ExterOryx** | Interoceptive-exteroceptive toggling — trains dynamic attention switching between internal body signals and external environment |
| **SomnoAffinity** | Self-referential voice affirmation timed to exhalation — activates mPFC-PCC identity circuits + ventral striatum reward coupling |
| **NeuroHarmonics** | 3-layer adaptive audio architecture: frequency alignment, breath-rhythm integration, adaptive soundscaping. Includes gamma (40Hz) for task-positive focus. |
| **TransMetachora** | Cultural priming funnel for cross-cultural onboarding — reduces novelty-related cognitive load before training begins |

All 10 are connected via SKOS relationships, forming a coherent ecosystem where each framework serves a specific function within the larger somnistics architecture.

---

## The MCP Server: Any AI Agent Can Query the Vault

The vault includes a **Model Context Protocol (MCP) server** — a standard interface that allows any AI agent (Claude, ChatGPT, Gemini, custom agents) to query the knowledge graph programmatically.

### 9 Available Tools

| Tool | What It Does |
|------|-------------|
| `list_concepts` | List all concept notes with title, status, and ID |
| `get_note` | Get a single note's full metadata and body by slug or URN |
| `get_evidence_chain` | Trace prov:wasDerivedFrom links recursively to find all supporting evidence |
| `get_relationships` | Get SKOS relationships (broader, narrower, related) with resolved titles |
| `search_by_subject` | Find all notes tagged with a specific dc:subject |
| `search_by_type` | Filter notes by type (concept, evidence, observation, audience) |
| `search_by_status` | Filter notes by quality gate (draft, review, canonical) |
| `get_audience_concepts` | Get concepts relevant to a specific audience profile |
| `get_provenance` | Trace a claim's full provenance chain to its sources |

### What This Enables

1. **Randy talks to the vault through any AI.** "What evidence supports Gap Moment Training?" The AI queries `get_evidence_chain("gap-moment-training")` and returns Porges 2011, Lehrer 2000, plus the clinical observations.

2. **New team members onboard through the vault.** Instead of asking Randy to re-explain the concept architecture, they ask an AI connected to the MCP server.

3. **Content generation with provenance.** When generating a NeuroMinute script, investor deck, or CEU module, the AI pulls from canonical concepts with evidence chains — every claim is traceable.

4. **Enterprise sales with evidence.** When a hospital asks "what's the science behind this?", the vault provides structured, cited answers through any AI interface.

5. **The vault compounds.** Every new observation, evidence note, or concept enrichment makes the entire system more valuable. The knowledge graph grows and interconnects over time.

---

## What We Mined (Source Material Processed)

The vault was built by systematically mining every accessible source of SRL knowledge:

| Source | Volume | What We Found |
|--------|--------|---------------|
| ChatGPT conversations | 861 files | Concept definitions, clinical stories, IP frameworks, philosophical anchors |
| Google Drive (SRL account) | ~50 readable files | PRD, FDA guidance, competitive landscape, EXEC briefs, AANA application |
| Google Drive (personal) | BLIP Archive + SRL Library | Patent specs, neuroscientific framework PDFs, Moongate curriculum, glossary |
| Downloads folder | 590 files | Interoception Research Bot analysis, bibliographies, mathematical flow modeling |
| Local Drive mirror | 293 items | SOUL.md, agent ecosystem, strategy docs, market intelligence |
| Fresh .gdoc exports | ~30 files | Provisional patent, trademark portfolio, living scientific synthesis, grief practices |

### Key IP Discoveries During Mining

- **Provisional patent filed April 3, 2025:** AI-Guided Neuroadaptive Biometric Feedback System
- **35+ trademarkable terms** valued at $2-5M over 5 years
- **PAS-ME 5-state classifier** with "Pre-Oops" cognitive strain detection (<100ms on Apple Neural Engine)
- **20 novel sensor fusion combinations** — each patent-ready
- **Harvard NeuroSkill integration** mapped (11 Sacchet Lab papers, 2025-2026)
- **6-pillar IP moat:** patents + trademarks + trade secrets + data network effects + defensive publications + standardization leadership

---

## 87 Clinical Observations: Randy's Embodied Knowledge, Now Structured

The observation layer captures knowledge that doesn't exist in any textbook — patterns recognized across 28 years of clinical practice, personal transformation, and strategic insight. Organized by type:

### Craft Knowledge (56 observations)
The "how" behind the "what": protocol design logic, script craft, measurement architecture, training pedagogy.
- **Anesthetist's Breath 10/0/10/0** — protocol design with "spicy" dose-limiting feedback
- **Awareness before technique** — pedagogical sequencing (awareness first, never technique first)
- **8-layer VagalBeats slider** — user-controlled complexity unifying all 10 frameworks
- **Neuro-Ouroboros patent architecture** — Kalman filtering, PWTT, dopaminergic cueing
- **Category theory for state transitions** — formal composable morphism framework
- **Script design principles** — invitational language, sensory stacking, cultural neutrality

### Pattern Observations (23 observations)
Recurring patterns recognized across thousands of cases and years of practice.
- **"Most events aren't ignorance — they're state drift"** — 6 error archetypes from 10 years on QRC
- **Bandwidth saturation from cumulative micro-events** — not single traumas but accumulated unresolved activations
- **CRNA burnout: 12-72% prevalence, 39% COVID peak** — the enterprise sales numbers
- **Interoceptive suppression as burnout root cause** — medical education's hidden curriculum deliberately teaches body signal suppression
- **ADHD brains uniquely suited for gap moment training** — 60-second format matches attention architecture

### Exemplar Stories (4 observations)
Specific clinical incidents and personal transformation narratives.
- **Sleep → Code Blue → recovery without destabilization** — the paradigm case of state transition mastery
- **"Better at regulating patients than self"** — the founding insight of Pausality
- **Grief to vocation** — personal loss integrated into the discipline's foundation
- **Maria scenario** — 21-day training produces precise epidural at 4 AM after 12-hour shift

### Contrast Cases (3 observations)
Comparisons that illuminate what's different about SRL's approach.
- **HRV deprecation** — measurement integrity over theoretical elegance
- **BLIP Clinic** — gap moments are universal across professions (not just CRNAs)
- **Focal-panoramic paradox** — simultaneous precision + broad awareness (Castle-Field Vision)

---

## What This Unlocks

### For Product (Jason)
- **Every Pausality feature traces to evidence.** The 60-second format isn't arbitrary — it's validated by Lehrer 2000, Balban 2023, and amygdala deactivation timing. The MCP server provides this on demand.
- **The 8-layer VagalBeats slider** unifies all 10 trademarked frameworks into one UX control. The vault documents how each layer maps to a framework.
- **Script production has systematic specifications.** Invitational language rules, sensory stacking progressions, breath-phase attentional targets, binaural frequency mappings — all documented.
- **PAS-ME's 5-state classifier** and the 20 sensor fusion combinations provide the technical roadmap for adaptive biofeedback.

### For Growth (Livio)
- **Enterprise sales deck writes itself.** CRNA burnout prevalence (12-72%), $80-150K replacement cost, 25% medical error reduction with autonomic training, "9/10 CRNAs want peer support" — all sourced and structured.
- **5 high-burnout verticals** beyond CRNAs (vet staff, first responders, dispatchers, social workers, ATC) with specific tactical messaging for each.
- **Competitive positioning:** Pausality's moat is latency (seconds-to-intervention in real workflows). Calm/Headspace built for bedrooms, not operating rooms.
- **AEO strategy** for LLM discoverability — schema-marked pages that position Pausality in AI assistant answers.

### For Clinical Credibility (Randy)
- **AANA Category A CE** backed by structured evidence chains tracing to peer-reviewed sources.
- **Patent defensibility** strengthened by documented provenance — every claim in the provisional patent traces to evidence in the vault.
- **The vault IS the trade secret.** Proprietary therapy metadata tagging, diaphragmatic literacy scoring, and intervention-to-outcome mappings documented here constitute trade secret IP under the 6-pillar moat strategy.

### For the Moat
- **Ontology valley of death.** Competitors face prohibitive upfront costs to build equivalent structured knowledge. SRL has already crossed this barrier.
- **Three compound reinforcement loops:** Clinical validation → branding → network → more validation. Ontology → switching costs → adoption → network effects → stronger ontology. IP → cornered resource → counter-positioning → market share → more R&D.
- **The vault compounds.** Every new observation, evidence note, and concept enrichment raises the barrier to competitive entry.

---

## How It Works Day-to-Day

### For Humans (Obsidian)
Open the vault in Obsidian. Browse concept notes. See the graph visualization of how everything connects. Edit notes, add observations, promote concepts to canonical. The vault is just Markdown files with YAML frontmatter — no proprietary format, no lock-in.

### For AI Agents (MCP)
Any AI agent connects to the MCP server and gets structured access to the entire knowledge graph. Ask questions, trace evidence chains, find concepts by subject or audience, generate content with provenance. The vault is the AI's knowledge base.

### For Git (Version Control)
Every change is committed to git with descriptive messages. The full history is preserved. Nothing is lost. The vault syncs to GitHub for backup and collaboration.

### For the Team
The vault is shared state. Randy's knowledge is no longer trapped in his head or scattered across platforms. The team can query it, build on it, and use it to generate outputs — all with full provenance back to the source.

---

## Current Status

| Metric | Count |
|--------|-------|
| Total notes | 133 |
| Canonical concepts | 24 |
| Review concepts | 10 |
| Evidence notes | 12 |
| Observations | 87 |
| Audience profiles | 7 |
| Trademarked frameworks | 10 |
| MCP server tools | 9 |
| Git commits | 21+ |
| Sources mined | 861 ChatGPT + 65 Drive + 590 Downloads + 2 Google Drives |

### Remaining Work
1. Export ~30 patent .gdoc files (last major untapped source)
2. Promote remaining 10 concepts to canonical
3. Create evidence notes for Harvard/Sacchet Lab 11 papers
4. Build additional concepts (pausality product note, vagalbeats, breathe-nudges, interpause-certification)
5. Connect vault to production workflows (content generation, CE courses, investor materials)

---

## The Bottom Line

The Library Graph vault transforms SRL's scattered knowledge into a **structured, defensible, compounding asset.** It's not a wiki. It's not documentation. It's the ontology that creates switching costs, enables clinical credibility, and compounds the IP flywheel.

Every note is a brick in the moat.

*The arena is defined.*
