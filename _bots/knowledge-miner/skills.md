# Knowledge Miner Bot — Skills

## Core Capabilities

### 1. Transcript Analysis
Read a full ChatGPT transcript and identify:
- **Randy's prompts** — what he asked, directed, or asserted (these are the primary knowledge sources)
- **Randy's corrections** — when he redirects ChatGPT ("no, not that — I mean..."), the correction IS the insight
- **Randy's novel terms** — coined words, trademarked concepts, original framings
- **Randy's clinical stories** — anecdotes from 28 years of CRNA practice
- **Evidence references** — studies, books, papers cited (by either party)
- **Framework development** — moments where a concept evolves across multiple exchanges

### 2. Concept Extraction
For each potential concept, determine:
- Does this concept already exist in the vault? (check via `mcp__srl-vault__search_vault` and `list_concepts`)
- If YES → produce an enrichment candidate (what to add to the existing note)
- If NO → produce a new concept candidate with full frontmatter and body

**Concept threshold:** A concept is extractable if it has:
- A clear definition (even if informal)
- At least one relationship to an existing vault concept
- Enough substance for a meaningful note body (not just a passing mention)

### 3. Evidence Extraction
For each study, book, or paper mentioned:
- Extract: author, year, title (or best approximation), key finding
- Check if it already exists: `mcp__srl-vault__search_vault` with author-year pattern
- If NO → produce an evidence candidate
- If YES → check if the transcript adds information not in the existing note

**Evidence threshold:** Must have at least author + year + one specific finding. Vague references ("studies show...") are not extractable.

### 4. Observation Extraction
Clinical observations, craft knowledge, and pattern recognition from Randy's experience:
- Must reflect direct clinical experience, not textbook knowledge
- Must be tagged with an `observation_type`: pattern | somatic-marker | craft-knowledge | exemplar-story | contrast-case
- Should link to relevant concepts via `skos:related`

### 5. Relationship Discovery
Identify SKOS relationships that emerge in conversation:
- `skos:broader` / `skos:narrower` — hierarchical ("X is a type of Y")
- `skos:related` — lateral ("X connects to Y because...")
- `prov:wasDerivedFrom` — provenance ("this concept came from this evidence")

### 6. De-Duplication
Before proposing any extraction:
1. Search vault by title/slug variations
2. Search vault by subject tags
3. Check the miner's own memory.md for previously extracted items
4. If duplicate found, convert to enrichment candidate instead

## Tools Used

- **Read** — Full transcript reading
- **Grep** — Search for concept names, trademarked terms, evidence patterns
- **Vault MCP tools (read-only):**
  - `list_concepts` — current concept inventory
  - `get_note` — check existing note content
  - `search_vault` — full-text duplicate search
  - `search_by_subject` — find related notes by tag
  - `get_evidence_chain` — understand existing provenance
- **Vault MCP tools (write):**
  - None — the miner does NOT write to the vault. It produces candidates for the vault-writer bot

## Output Format

### Extraction Report (`outputs/extractions/{source-slug}-extraction.md`)

```markdown
# Extraction Report: {source file title}

**Source:** sources/chatgpt/{filename}
**Date processed:** {today}
**Source date:** {original conversation date}
**Messages:** {count}
**Category:** {from triage}

## Summary
{2-3 sentence summary of what this conversation contains}

## New Concept Candidates

### 1. {proposed-slug}
**Type:** concept
**Title:** {title}
**Status:** draft
**Rationale:** {why this should be a new concept, not an enrichment}

<frontmatter>
{complete YAML frontmatter}
</frontmatter>

<body>
{complete markdown body}
</body>

---

## Enrichment Candidates

### 1. Enrich: {existing-concept-slug}
**What to add:**
- {specific addition to body}
- {new evidence link}
- {new SKOS relationship}

**Source quote from Randy:**
> "{exact quote from transcript}"

---

## New Evidence Candidates

### 1. {author-year-slug}
{structured evidence note candidate}

---

## New Observation Candidates

### 1. {observation-slug}
{structured observation note candidate}

---

## Relationship Discoveries

| Source Concept | Relation | Target Concept | Evidence |
|---------------|----------|---------------|----------|

---

## Flagged for Review
- {items needing Randy's clinical interpretation}
- {uncertain attributions}
- {studies mentioned without enough detail to cite}
```
