---
title: "SRL System Architecture — Complete"
type: output
status: current
created: 2026-03-25
modified: 2026-03-25
---

# Somnistics Research Labs — System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           RANDY GRAYBEAL, CRNA                         │
│                        Chairman · Clinical IP · Voice                   │
│                                                                         │
│   28 years OR observation → 861 ChatGPT conversations → Living Library  │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                              VIGIL                                      │
│                      Orchestrator · AI Chief of Staff                   │
│                                                                         │
│   Routes work to bots · Coordinates pipelines · Synthesizes answers     │
│   Tracks progress · Maintains vault integrity · Runs quality gates      │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
        ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
        │  MCP SERVERS  │  │   10 BOTS    │  │    TOOLS     │
        └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
               │                 │                  │
               ▼                 ▼                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         LIVING LIBRARY (VAULT)                          │
│                                                                         │
│   903 notes · 162 concepts · 450 evidence · 262 observations            │
│   Dublin Core + SKOS + PROV-O · Git versioned · Obsidian rendered       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## The Five Layers

```
Layer 0    EVIDENCE       450 notes    Studies, books, papers, data
           ─────────────────────────────────────────────────
Layer 0.5  OBSERVATIONS   262 notes    Embodied knowledge, field notes, external signals
           ─────────────────────────────────────────────────
Layer 1    CONCEPTS       162 notes    One atomic idea per file (SKOS)
           ─────────────────────────────────────────────────
Layer 2    AUDIENCES      10 profiles  Who we're talking to + how
           ─────────────────────────────────────────────────
Layer 3    OUTPUTS        145+ files   Essays, proposals, briefs, courses, book chapters
```

Every note has YAML frontmatter. Every claim traces to evidence (PROV-O). Every concept relates to others (SKOS). Every audience profile defines evidence depth and language register.

---

## Standards

| Standard | What It Does | Where |
|----------|-------------|-------|
| **Dublin Core** | Metadata on every note (title, creator, date, subject, source) | All frontmatter |
| **SKOS** | Concept relationships (broader/narrower/related) | concepts/ frontmatter |
| **PROV-O** | Provenance chains (every claim → evidence) | wasDerivedFrom fields |
| **SRL Custom** | clinicallyInformedBy, targetedAt, supportsRedArrow | _schema/relations.yaml |

---

## MCP Servers (3 Connected)

| Server | Type | Tools | Purpose |
|--------|------|-------|---------|
| **srl-vault** | Local Python | 18 tools | CRUD, search, graph queries, status promotion, SKOS wiring |
| **PubMed** | Claude.ai connector | 7 tools | Literature search, article metadata, related articles, full text |
| **openevidence** | Local Python | Clinical AI | Clinical evidence queries (when running) |

### srl-vault Tools
```
create_note          update_note          get_note
list_concepts        search_vault         search_by_subject
search_by_status     search_by_type       get_evidence_chain
get_relationships    get_audience_concepts add_evidence_link
add_skos_relation    promote_status
```

---

## Bot System (10 Specialized Agents)

```
┌─────────────────────────────────────────────────────────────────┐
│                        VIGIL (Orchestrator)                      │
│                                                                  │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│   │  EXTRACTION   │  │  KNOWLEDGE   │  │    VAULT WRITER      │  │
│   │  COORDINATOR  │──│    MINER     │──│  (schema enforcer)   │  │
│   └──────────────┘  └──────────────┘  └──────────────────────┘  │
│          │                                                       │
│   ┌──────┴──────────────────────────────────────────────────┐   │
│   │                    PIPELINE BOTS                         │   │
│   │                                                          │   │
│   │  transcript-triage → knowledge-miner → vault-writer      │   │
│   │       (scan)            (extract)        (write)         │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │                    QUALITY BOTS                           │   │
│   │                                                           │   │
│   │  citation-resolver    compliance-gertrude                 │   │
│   │  (DOI verification)   (FDA/FTC compliance gate)           │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │                  INTELLIGENCE BOTS                        │   │
│   │                                                           │   │
│   │  competitive-landscape   marketing-intelligence           │   │
│   │  (weekly market scan)    (demand signal monitoring)       │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │                   RESEARCH BOTS                           │   │
│   │                                                           │   │
│   │  cognitive-ethnographer  review-accelerator               │   │
│   │  (expert cognition)      (pre-process for Randy)          │   │
│   └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

Each bot has:
- `soul.md` — Identity, persona, mandate
- `run-protocol.md` — Step-by-step execution
- `patterns.md` — Accumulated heuristics (6 bots still need this)
- `learning-log.md` — Run-by-run self-reflection
- `retrospective.md` — Periodic self-assessment

---

## Automation Layer

### Hourly: Essay Engine
```
Every hour at :17 (local cron, session-bound)
│
├── Read essay-queue.md → pick next pending topic
├── Deep research: vault mining + PubMed (5+ verified citations)
├── Write: Notes from the Lab format (1000-2000 words)
├── Quality gates: 5 gates (claim, mechanism, failure mode, test, vault-deepening)
├── Gertrude compliance check
├── Citation verification table (every PMID confirmed)
├── Learning log append
├── Git commit + push
│
Queue: 24 topics → then auto-discovery of unwritten draft concepts
```

### Nightly: Mining Pipeline (launchd — currently stalled)
```
Every night at 2:00 AM (com.srl.mine-pipeline.plist)
│
├── mine-next-batch.sh
├── Batch of 3 files from sources/chatgpt/
├── transcript-triage → knowledge-miner → vault-writer
├── Progress tracked in extraction-coordinator/progress.md
│
Status: 858/861 files remaining. Pipeline stalled 10+ days.
```

### Monthly: Citation Health (launchd)
```
1st of month at 3:00 AM (com.srl.citation-health.plist)
│
├── check-citations.sh
├── Validate DOIs and PubMed IDs across evidence notes
├── Report: outputs/citation-health-report.md
│
Last run: Baseline scan showed 45% health (100 valid, 70 broken, 52 missing)
```

### Remote: Essay Engine (Anthropic CCR — not firing)
```
Every hour (trig_01V9vgkN7AXGUpmfEVtRsiFH)
│
├── Same protocol as local essay engine
├── PubMed MCP connected
├── Status: ENABLED but never successfully pushed
├── Likely cause: git push credentials not configured in CCR environment
│
Manage: https://claude.ai/code/scheduled
```

---

## Tools (14 files)

| Tool | Type | Purpose |
|------|------|---------|
| `muse-connect.py` | Python | Muse 2 EEG connection via BrainFlow — live stream, band power analysis, session export |
| `biomedical-query.py` | Python | Query 7 HuggingFace biomedical LLMs for mechanism explanations |
| `mine-next-batch.sh` | Bash | Execute extraction pipeline on next batch of ChatGPT files |
| `check-citations.sh` | Bash | Validate DOIs and PubMed IDs across vault |
| `add-citation-links.sh` | Bash | Wire evidence citations into concept notes |
| `evidence-brief.sh` | Bash | Generate evidence summaries from vault queries |
| `extract-review-data.py` | Python | Parse extraction reports into structured JSON |
| `generate-review-queue.py` | Python | Build review queue from extraction data |
| `review-gui.html` | HTML | Interactive review interface |
| `clinical-epistemology.html` | HTML | Concept relationship visualization |
| `competitive-landscape.html` | HTML | Market analysis dashboard |

---

## Hardware Integration

### Muse 2 EEG (via BrainFlow)
```
Muse 2 headband (Bluetooth BLED)
    │
    ├── 4 EEG channels: TP9, AF7, AF8, TP10
    ├── 256 Hz sampling rate
    │
    └── tools/muse-connect.py
         ├── Live stream mode (real-time band powers every 2s)
         ├── Recording mode (60s default, configurable)
         ├── Band power analysis (delta/theta/alpha/beta/gamma)
         ├── Alpha/theta ratio → state classification
         ├── Frontal alpha asymmetry (approach vs. withdrawal)
         └── Session export: CSV + JSON + PNG → outputs/eeg-sessions/
```

### Apple Watch (via Pausality app)
```
Apple Watch Series 4+
    │
    ├── Real-time heart rate during breathing sessions
    ├── HRV (RMSSD) daily morning readings
    ├── Session tracking and history
    │
    └── Pausality App (TestFlight build 508)
         ├── 21-session progressive breathing curriculum
         ├── Cardiac-anchored breathing (synced to heartbeat)
         ├── NeuroMinute™ 60-second sessions
         └── Privacy-first: data stays on device
```

---

## Source Migration Pipeline

```
sources/chatgpt/  (861 files, 23 MB)     ──┐
sources/google-drive/ (63 files)           ──┤
                                            │
     ┌──────────────────────────────────────┘
     │
     ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  TRANSCRIPT  │───▶│  KNOWLEDGE  │───▶│    VAULT    │
│   TRIAGE     │    │    MINER    │    │   WRITER    │
│  (classify)  │    │  (extract)  │    │  (schema)   │
└─────────────┘    └─────────────┘    └─────────────┘
                                            │
                                            ▼
                              concepts/ evidence/ observations/

Status: 3/861 processed (0.3%). Pipeline stalled.
At batch size 3: ~286 runs to clear queue.
```

---

## Content Production Pipelines

### Essay Engine (Notes from the Lab)
```
Queue → Research → Write → Quality Gates → Gertrude → Verify → Commit
  │                                                              │
  │  5 gates: claim, mechanism, failure mode, test, vault-deep   │
  │  PubMed: every PMID verified via metadata lookup              │
  │  Gertrude: FDA/FTC compliance scan                            │
  │  Learning log: accumulates patterns across runs               │
  │                                                              │
  └── 24 queued topics across 4 lanes:                           │
       Core IP (9) · Physiological (7) · Clinical (6) · Strategic (2)
```

### Book Pipeline (Inside Out: A CRNA's Field Guide)
```
/write-chapter skill
  │
  ├── Vault-sourced (concepts + evidence chains)
  ├── Gertrude compliance before output
  ├── Randy's voice (resonant nonfiction standard)
  │
  └── outputs/book/chapters/ch01-ch09 drafted
      14 chapters planned, 9 drafted
```

### Client Deliverables
```
Massimo Ferrari Driver Project:
  ├── audiences/elite-motorsport-driver.md (vault profile)
  ├── outputs/proposals/massimo-intake-protocol.html (2-hr assessment, 11 stations + SRB-60)
  ├── outputs/proposals/massimo-tools-showcase.html (client-facing arsenal)
  ├── outputs/proposals/massimo-training-plan.html (6-week program + race-day protocols)
  └── outputs/proposals/massimo-eeg-onepager.html (EEG brain mapping explainer)
```

---

## Shared State Files

| File | Purpose | Update Cadence |
|------|---------|---------------|
| `outputs/active-context.md` | Current priorities, open decisions | Every session |
| `outputs/needs-review.md` | Items requiring Randy's judgment | As generated |
| `outputs/vault-write-log.md` | Audit trail of bot-initiated changes | Every bot run |
| `outputs/essay-queue.md` | Essay engine topic queue | Every essay |
| `outputs/essays/essay-engine-learning-log.md` | Essay engine self-improvement | Every essay |
| `_bots/extraction-coordinator/progress.md` | Pipeline progress tracker | Every batch |

---

## Five Red Arrows (Priority Filter)

```
1. Clinical Credibility → Consumer App Downloads          [COMPLETE]
2. Consumer Traction → Enterprise Proof                   [IN PROGRESS]
3. Enterprise Pilot → Enterprise Contract                 [NEXT]
4. Enterprise Data → Clinical LLM Moat                    [PLANNED]
5. Platform + CEU → Multi-Stream $1M ARR                  [TARGET]
```

If an action doesn't advance a red arrow, it's not a priority.

---

## Vault Statistics (2026-03-25)

| Metric | Count |
|--------|-------|
| Total vault notes | 903 |
| Concepts | 162 (31 canonical, 12 review, 118 draft) |
| Evidence sources | 450 (57% need DOI verification) |
| Observations | 262 |
| Audience profiles | 10 |
| Output artifacts | 145+ |
| Bots | 10 |
| MCP servers | 3 configured, 2 reliably connected |
| Tools | 14 |
| Automation jobs | 3 (essay hourly, mining nightly, citations monthly) |
| Source files to migrate | 858 remaining of 924 |
| Book chapters drafted | 9 of 14 |
| Essay queue | 23 pending of 24 |
| Git commits (all time) | 100+ |
