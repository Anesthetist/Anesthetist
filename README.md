# Somnistics Research Labs — Library Graph

A standards-based Obsidian vault serving as the living knowledge graph for [Somnistics Research Labs](https://somnistics.com). Connects GitHub, Obsidian, and AI agents into a single source of truth for the science, IP, and clinical reasoning behind somnistics.

## What is Somnistics?

> **Somnistics (n.)** — The applied science of training neural state transitions under pressure.

Somnistics bridges neuroscience, somatic intelligence, and behavioral design to transform naturally occurring "gap moments" into opportunities for nervous system regulation. Built on 28 years of clinical anesthesia expertise (CRNA), polyvagal theory, interoceptive neuroscience, and real-time biometrics.

## Vault Structure

```
_schema/          # Note-type definitions, relation types, audience schema
_index/           # Auto-generated indexes
concepts/         # Layer 1 — SKOS Concept notes (one atomic idea per file)
evidence/         # Layer 0 — Dublin Core source notes (studies, books, papers)
observations/     # Layer 0.5 — Embodied/clinical knowledge
audiences/        # Layer 2 — Audience profiles with evidence depth + language register
outputs/          # Layer 3 — Generated artifacts (NeuroMinutes, CEU courses, decks)
Templates/        # Note templates for each type
Maps/             # Maps of Content (MOCs)
mcp-server/       # MCP server for AI agent access to the vault
scripts/          # Utility scripts
```

## Standards

| Standard | Purpose |
|----------|---------|
| **Dublin Core** | Metadata on every note (title, creator, date, subject, source) |
| **SKOS** | Concept relationships (broader / narrower / related) |
| **PROV-O** | Provenance chains — every claim traces to evidence |

## Vault Statistics

| Layer | Count | Description |
|-------|-------|-------------|
| Canonical concepts | 24 | Fully defined, evidence-linked, peer-reviewed |
| Review concepts | 6 | Awaiting evidence strengthening |
| Evidence notes | 27 | Published research (Porges, Lehrer, Sacchet Lab, Van der Kolk, etc.) |
| Observations | 87 | Clinical knowledge from 28 years of CRNA practice |
| Audience profiles | 7 | CRNAs, investors, enterprise, researchers, etc. |
| Outputs | 3+ | NeuroMinute curriculum, slide decks, CEU course stubs |

## Canonical Concepts (24)

The controlled vocabulary of somnistics:

| Concept | Trademarked | Description |
|---------|:-----------:|-------------|
| Somnistics | | The discipline — training neural state transitions under pressure |
| Gap Moment Training | TM | Repurposing transitional moments as nervous system training reps |
| NeuroMinute | TM | 60-second micro-intervention with biometric verification |
| Anterocept | TM | Progressive interoceptive training spectrum (3 domains) |
| Neurogating | TM | AI-driven closed-loop detection and adaptive intervention |
| Neuro-Ouroboros | TM | 21-day recursive curriculum architecture |
| Polyanchora | TM | Multi-anchor attentional scaffolding system |
| Polyvagal Theory | | Three-tier autonomic hierarchy (Porges) |
| Interoception | | Sense of the internal state of the body |
| Autonomic Regulation | | Flexible shifting between sympathetic/parasympathetic states |
| State Transition | | The fundamental unit of change in the system |
| Vagal Tone | | Strength of vagus nerve parasympathetic activation |
| Resonant Breathing Frequency | | Individualized breathing rate for maximal HRV (~0.1 Hz) |
| Titration to Effect | | Pharmacological dosing principle applied to behavioral intervention |
| Minimum Effective Dose | | Smallest intervention producing measurable change |
| Co-Regulation | | Interpersonal autonomic entrainment via social engagement |
| Multi-Phase Interoceptive Coupling | | Simultaneous multi-signal internal awareness training |
| Self-Remembering | | Maintaining awareness of oneself while engaged in activity |
| Kosha Architecture | | Vedantic five-sheath model applied to progressive training |
| Relevance Realization | | How agents determine what is salient (Vervaeke) |
| Clinician Durability | | Sustaining performance across a multi-decade career |
| Diaphragmatic Blindness | | Inability to sense one's own diaphragmatic breathing |
| Neural Transition Failure | | Failed autonomic reset; residual sympathetic bleed |
| Interoceptive Literacy | | Clinical-grade self-monitoring of physiological state |

## Evidence Base (27 sources)

Includes peer-reviewed research from:

- **Harvard/MGH Meditation Research Program** (Sacchet Lab) — 15 papers covering autonomic nervous system effects, interoceptive biomarkers, neural correlates of mindfulness, advanced meditation neuroplasticity, and neurofeedback
- **Porges** — Polyvagal Theory
- **Lehrer** — Resonance frequency biofeedback
- **Van der Kolk** — Somatic trauma processing
- **Zaccaro** — Systematic review of slow breathing
- **Balban (Stanford)** — Cyclic sighing RCT
- **McGilchrist** — Hemispheric lateralization
- **Vervaeke** — Relevance realization
- **Thayer & Lane** — Neurovisceral integration

## Quality Gate

Every note progresses through a three-stage quality gate:

```
draft → review → canonical
```

- **Draft** — Created, minimal validation
- **Review** — Enriched with definitions, evidence links, SKOS relationships
- **Canonical** — Librarian-assessed, fully cross-referenced, controlled vocabulary term

## MCP Server

The vault includes an MCP (Model Context Protocol) server that gives AI agents structured access to the knowledge graph.

### Setup

```bash
cd mcp-server
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Tools (9)

| Tool | Description |
|------|-------------|
| `list_concepts` | List all concept notes with title, status, ID |
| `get_note` | Get full note by slug or URN ID |
| `get_evidence_chain` | Trace prov:wasDerivedFrom links recursively |
| `get_relationships` | Get SKOS relationships with resolved titles |
| `search_by_subject` | Find notes by dc:subject tags |
| `search_by_type` | Find notes by type |
| `search_by_status` | Find notes by quality gate |
| `get_audience_concepts` | Extract concepts linked from audience profiles |
| `search_vault` | Full-text search across titles, bodies, and subjects |

### Claude Code Integration

The `.mcp.json` at project root auto-registers the server with Claude Code.

## Workflow

```
Human (Obsidian) ←→ Vault (Git) ←→ AI Agents (Claude Code / MCP)
```

- Claude Code operates from this directory as working root
- Changes committed to git, synced to GitHub
- Obsidian reads the same directory for graph visualization
- The graph is shared state between human editing and AI processing

## Trademarked Terms

Gap Moment Training™, NeuroMinute™, Pausality™, Anterocept™, Neurogating™, Polyanchora™, Neuro-Ouroboros™, ExterOryx™, SomnoAffinity™, NeuroHarmonics™, TransMetachora™

## License

Proprietary. Copyright 2026 Somnistics Research Labs. All rights reserved.
