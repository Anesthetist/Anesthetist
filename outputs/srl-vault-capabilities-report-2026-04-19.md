---
id: urn:srl:output:srl-vault-capabilities-report-2026-04-19
type: output
title: "SRL Vault Capabilities Report"
status: draft
creator: Vigil
created: 2026-04-19
modified: 2026-04-19
output_type: ip-doc
target_audience: urn:srl:audience:corporate-executive
prov:wasDerivedFrom:
  - urn:srl:concept:somnistics
dc:format: md
purpose: Strategic inventory of what the Library-Graph can do today, what is one build-session away, and what becomes possible as the graph scales. For Randy's internal reference and forwardable to advisors.
---

# SRL Vault Capabilities Report

A strategic inventory of what the Library-Graph currently enables, what is within reach this quarter, and what becomes possible as the graph compounds.

**Baseline as of 2026-04-19:** 547 evidence notes, 188 concepts, 380 practice observations, 322 generated outputs, 12 audience profiles, 11 specialized AI agents, 219 commits on the main branch.

## What's Live Today

### 1. On-demand content regeneration

Any SRL communication (investor deck, LinkedIn post, CEU module, pitch email, research brief, pilot protocol) can be generated or regenerated from the graph with accurate evidence chains and audience-matched framing. Publish cost for a new format of existing thinking is minutes, not days.

Active in the last 30 days: CRNA Ecology brief and deck, NeuroMinute composable architecture doc, Pausality B2B sales framework, three published essays on clinician durability and resonant breathing frequency, multiple HN intel scans, the Jason Fields explainer.

### 2. Evidence-chained clinical claims

Every claim SRL puts in public materials traces back to specific evidence notes via PROV-O provenance links. Pausality app content, CEU curriculum, investor collateral, and the IRB pilot protocol all pull from the same chain. If an advisory board, regulator, legal reviewer, or journalist asks for the citation behind any claim, the chain is one query away.

This is the architecture that lets SRL make clinical positioning statements without flinching.

### 3. Duplicate detection and audit trail

Every vault write goes through schema validation. The write log records who changed what and why. The pre-commit hook blocks outputs with quality violations (em-dash density, unverified DOIs, regulatory red-line language, broken wikilinks). Six weeks of operation have surfaced (and resolved) multiple duplicate-record failure modes that would have corrupted the graph silently.

### 4. Gap analysis and literature mapping

The 30-discipline psychophysiology map names the territories SRL's work spans and lets us answer "what do we know and what are we missing" per discipline. The TF-IDF corpus analysis identifies concepts that are under-evidenced or evidence notes that are under-concepted. The competitive-landscape bot watches the external field weekly and maps what competitors claim vs. what evidence supports.

### 5. Audience-matched rendering

The audiences layer (CRNAs, researchers, investors, corporate executives, family consumers, pediatric surgeons, ED nurses, others) carries evidence depth and language register per audience. The same claim renders differently for a CRNA (full mechanism, primary evidence) and for a consumer parent (framed outcome, accessible language). No rewriting from scratch.

### 6. Concept-to-product tracing

Trademarked terms (Gap Moment Training, NeuroMinute, Pausality, Anterocept, Neurogating, Polyanchora) have vault histories showing where they originated, how they relate to each other via SKOS hierarchy, and which evidence grounds them. IP-defense posture is documented, not reconstructed.

### 7. Orchestrated multi-agent operations

Vigil (orchestrator) routes work to the right agent. The bot roster:

- **transcript-triage:** sorts raw ChatGPT and cowork exports
- **knowledge-miner:** extracts concepts, evidence, observations from sources
- **vault-writer:** validates and writes through MCP tools
- **citation-resolver:** verifies DOIs, authors, publication dates
- **review-accelerator:** streamlines Randy's review queue
- **competitive-landscape:** weekly external scans
- **marketing-intelligence:** maps the persuasion landscape
- **compliance-gertrude:** FDA/SaMD red-line gate
- **editor:** edits drafts before ship
- **cognitive-ethnographer:** extracts embodied knowledge from clinical observation
- **extraction-coordinator:** tracks pipeline progress

Each bot has a soul (identity), skills (tools), run-protocol (steps), and a learning log that accumulates across runs.

### 8. Daily intelligence surface

Hacker News scans, weekly HPO digests, competitive intel, Leading Edge community signals, and investor-channel feedback all flow into observations and get cross-wired to concepts. The vault is an intelligence console, not only a knowledge archive.

## What's One Build-Session Away

### 9. Certification curriculum auto-sequencing

The somatic certification's five competency domains map cleanly onto existing concept clusters. A curriculum generator could pull from the graph and produce the CEU module sequence with evidence-backed lesson plans. Scoped, not yet built.

### 10. Per-investor evidence package generation

Each SRL investor has documented concerns, questions, and prior conversations. A package generator could output a custom-sequenced brief for any given investor pulling the most-relevant evidence and concepts for their priors. Don Diamond, Whitney Casey, Elevate Capital, Tom Morgan's network: each gets a different rendering of the same underlying graph.

### 11. Pausality content CMS

The Pausality app already carries research-backed messaging. A lightweight content API against the graph would let the product ship new content without engineering release cycles. Every content card in the app becomes a view into the vault.

### 12. Clinical claim watchdog

When the Pausality app, marketing site, or CEU materials are updated, a watchdog could run compliance-gertrude against the new content and block publish if a claim lacks a valid evidence link or crosses an FDA red-line pattern.

### 13. Grant and IRB auto-assembly

The IRB pilot protocol is already in the vault. Grant applications and IRB amendments typically ask the same questions (aims, background, significance, preliminary data, methods). Each section can be assembled from graph content with minimal human editing.

## What's Architecturally Possible

### 14. Somnistics clinical LLM

The vault's typed structure plus 15 years of Randy's clinical observation is a training corpus no competitor can reproduce. Fine-tuning a model on this substrate (not raw text, but evidence-linked, concept-cross-wired, audience-registered data) is a defensible AI moat. The data shape is the product.

### 15. Evidence-chain inference at scale

Given a new paper, the graph can answer: which concepts does this support, contradict, extend, or replace? Which SRL claims get stronger? Which get weaker? Which outputs need regeneration? Current practice does this manually; the graph structure makes it automatable.

### 16. Longitudinal concept evolution

The git history lets SRL show when concepts were coined, how they evolved, and which evidence drove revisions. For IP defense, academic credibility, and the eventual Somnistics book, the graph is a reproducible record of the intellectual lineage.

### 17. Federated publishing

The same graph can publish to multiple surfaces: SRL website, investor data room, academic preprint, CEU platform, Pausality app, clinical advisory materials. Each surface renders the graph for its audience. One source, many faces.

## What This Enables That Competitors Cannot Match

1. **Speed.** Any new output format is minutes, not weeks. New investor ask, new clinical advisor question, new conference submission: generate from graph, edit, ship.

2. **Citation integrity.** Every claim is traceable. Competitors make clinical claims without citations; SRL never has to.

3. **Audience fidelity.** The same content respects 12 distinct audience registers without rewriting.

4. **Institutional memory.** Nothing drifts. The graph remembers when every concept was introduced, why, and what evidence drove the decision. Founder risk in knowledge-holding is reduced.

5. **AI data substrate.** The graph is training substrate for a domain-specific clinical LLM. The structure, not the scrape-able text, is the moat.

6. **IP defensibility.** Trademarked terms, novel concepts, and clinical observations are timestamped, cross-wired, and audit-logged. Prior-art disputes are answerable with a git log query.

## Current Friction and Gaps

- **Bot-output schema drift:** researcher-heartbeat and weekly-hpo-scan bots have historically produced non-compliant frontmatter (legacy `subjects:` field, inconsistent ID schemes). Being cleaned up under the new schema v2 gates.
- **Provisional subject vocabulary:** 134 subject tags in the 3-to-4-use frequency band still need canonical labels and hierarchy. Subjects.yaml v0.2 is backlogged.
- **Clinical interpretation backlog:** many evidence notes carry "Pending review" in the clinical interpretation field. Randy's field alone; no bot fills it.
- **FRBR conflation:** instruments (NANTS, MAIA-2, BOLT) are distinct from the evidence notes that validate them. Instrument note type now exists in the schema; retrofit pending.
- **Author authority control:** deferred. No ORCID or VIAF identifiers on authors. Revisit at 1,000 evidence notes.

## Strategic Implication

The Library-Graph is not content infrastructure. It is the unfair advantage. Every week it compounds. Every new evidence note strengthens the chains around every existing concept. Every new concept sharpens the audience-matched outputs. Every new output exposes gaps that direct the next literature scan.

The compounding is load-bearing for the five red arrows. Clinical credibility is the graph. Consumer traction rests on evidence-backed content shipped fast. Enterprise proof cites the graph. Clinical LLM moat is the graph.

The right action most weeks is: feed the graph and let it work.
