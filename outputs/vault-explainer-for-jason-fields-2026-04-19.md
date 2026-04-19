---
id: urn:srl:output:vault-explainer-for-jason-fields-2026-04-19
type: output
title: "SRL Library-Graph Explainer for Jason Fields"
status: draft
creator: Vigil
created: 2026-04-19
modified: 2026-04-19
output_type: ip-doc
target_audience: urn:srl:audience:corporate-executive
prov:wasDerivedFrom:
  - urn:srl:concept:somnistics
dc:format: md
audience: Jason Fields (SRL cofounder, design lead, ex-Audible)
purpose: Context-setting brief so Jason can speak to the vault's strategic role in board rooms, investor conversations, and product reviews.
---

# The SRL Library-Graph, Explained

A brief for Jason Fields. Forwardable as-is or adaptable.

## What it is

A standards-based Obsidian vault, stored in git, shared across humans and AI agents. It models everything SRL knows as structured data. Every study, every concept, every practice observation is a typed note with validated metadata. Relationships between them (evidence grounds concept, concept narrower-than parent concept, audience reads output) are formal links, not prose.

Think of it as our internal ontology rendered as a living document. The same way Audible structures metadata around every title, narrator, series, and license.

It is not a doc repo. Not a wiki. Not a notes folder.

## Four layers

1. **Evidence** (547 notes). Every paper, book, or study SRL relies on, with authors, DOIs, journal info, license. Rock-solid citation is a load-bearing moat for our CRNA positioning.
2. **Concepts** (188 notes). Atomic ideas. Gap Moment Training, NeuroMinute, closed-loop controller, interoceptive literacy. Each concept is linked to the evidence that grounds it.
3. **Observations** (380 notes). Clinical and embodied knowledge from Randy's 15 years of anesthesia practice. The tacit-knowledge layer. This is the part no competitor can reproduce.
4. **Outputs** (321 artifacts). Everything generated from the graph: decks, essays, CEU curriculum drafts, research briefs, pilot protocols. Outputs are derivations, not originals. Re-generated as the graph matures.

Plus an **audiences** layer (CRNAs, researchers, investors, corporate executives, family consumers) defining how we speak to each.

## Why it matters strategically

Three compounding moats:

1. **Distribution.** The graph regenerates any output format on demand (deck, email, LinkedIn post, CEU module) without re-researching. Publish cost approaches zero.
2. **Regulatory and clinical credibility.** Every Pausality claim is traceable back to primary evidence. When legal, FDA, or a clinical advisory board asks for the citation, we have the full chain.
3. **LLM moat.** The graph's structure, not just its content, is the training substrate for a Somnistics clinical LLM. Competitors can scrape research. They cannot scrape 15 years of Randy's clinical observation, structured into a knowledge graph with formal evidence links.

## Standards under the hood

- **Dublin Core** for metadata on every note.
- **SKOS** for concept relationships (broader, narrower, related).
- **PROV-O** for provenance (every claim traces to its source).

If an academic librarian audited this vault tomorrow, the architecture would hold up. That matters for the eventual FDA submissions and the academic partnerships Randy is building.

## Scale right now

- 218 commits on the main branch
- 1,200+ notes across the four layers
- 11 specialized AI agents that mine, verify, enrich, and maintain the graph under strict schema rules
- Daily audit log of every bot-initiated change

## How it flows into the product

- **Pausality** pulls evidence URNs to back each claim in the app's content (research-backed by design).
- **Somatic certification** curriculum is sequenced directly from concepts and their SKOS hierarchy.
- **Investor and CRNA materials** are generated from the vault and re-generated as the graph updates. The deck you help polish is a rendering of the vault, not a hand-authored artifact.

## How you interact with it

Mostly you don't, directly. You see the outputs layer: the decks you help design, the briefs you review, the positioning arguments for investors. When you want to understand why a claim holds, Vigil (the orchestrator AI) walks the graph backward from the claim to the evidence. Ask Randy for a tour any time.

## What's distinct

Companies with knowledge bases usually have wikis that rot. This is a typed, versioned, audited graph with schema enforcement and bot-driven quality gates. The vault cannot drift without leaving a trace. That is the difference between a documentation habit and an institutional memory.

## One-line summary

The Library-Graph is the single source of truth SRL pulls from for product content, certification curriculum, clinical claims, and investor materials. It is versioned, evidence-chained, and maintained by AI agents under strict schema rules.
