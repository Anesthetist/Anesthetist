# Somnistics Research Labs — Library Graph

A standards-based Obsidian vault serving as the living knowledge graph for SRL. Connects GitHub, Obsidian, and AI agents.

## Vault Structure (Four Layers + Sources)

```
_schema/          # note-types.yaml, relations.yaml, audiences.yaml
_index/           # auto-generated indexes (by-subject, by-evidence, by-audience)
concepts/         # Layer 1: SKOS Concept notes — one atomic idea per file
evidence/         # Layer 0: Dublin Core source notes — studies, books, papers
observations/     # Layer 0.5: Embodied/clinical knowledge
audiences/        # Layer 2: Audience profiles with evidence depth + language register
outputs/          # Layer 3: Generated artifacts (neurominutes, CEU courses, decks)
Templates/        # Note templates for each type
Maps/             # Maps of Content (MOCs)
```

## Standards

- **Dublin Core** — metadata on every note (title, creator, date, subject, source)
- **SKOS** — concept relationships (broader/narrower/related)
- **PROV-O** — provenance chains (every claim traces to evidence)

## Conventions

- All notes have YAML frontmatter matching `_schema/note-types.yaml`
- IDs use URN format: `urn:srl:{type}:{slug}`
- Filenames: lowercase-kebab-case
- Use `[[wikilinks]]` for internal links
- Status quality gate: `draft` → `review` → `canonical`
- Trademarked terms: Gap Moment Training™, NeuroMinute™, Pausality™, Anterocept™, Neurogating™, Polyanchora™

## AI Agent Workflow

- Claude Code operates from this directory as working root
- Changes committed to git, synced to GitHub
- Obsidian reads the same directory for graph visualization
- The graph is shared state between human editing (Obsidian) and AI processing (Claude)
- If an action doesn't advance a red arrow, it's not a priority

## Five Red Arrows (Priority Filter)

1. Clinical Credibility → Consumer App Downloads (complete)
2. Consumer Traction → Enterprise Proof (in progress)
3. Enterprise Pilot → Enterprise Contract (next)
4. Enterprise Data → Clinical LLM Moat (planned)
5. Platform + CEU → Multi-Stream $1M ARR (target)

## Brand

- Colors: Deep Navy #22253A, Soft Sage #5FC89B, Off-white #F5F5F0
- Font: Poppins (400 headers, 300 body, tracking -0.025em)
- Key terms: somnistics, minimum effective dose, titration to effect, BOLT scores, MAIA-2, RMSSD, HRV coherence, resonant breathing frequency, vagal tone
