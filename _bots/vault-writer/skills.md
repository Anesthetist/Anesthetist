# Vault Writer Bot — Skills

## Core Capabilities

### 1. Schema Validation
Before writing any note, validate against `_schema/note-types.yaml`:

**All notes require:**
- `id` — URN format matching type
- `type` — must be one of: concept, evidence, observation, audience, output
- `title` — non-empty
- `status` — must be `draft` for bot-created notes
- `creator` — "Randy Graybeal" (unless otherwise specified)
- `created` — ISO date
- `modified` — ISO date (same as created for new notes)

**Concept notes additionally require:**
- `version` — "1.0" for new notes
- `dc:subject` — list of tags
- `dc:source` — list of source references
- `skos:broader`, `skos:narrower`, `skos:related` — lists (can be empty)
- `prov:wasDerivedFrom` — list of evidence/observation URNs

**Evidence notes additionally require:**
- `dc:creator` — original author(s)
- `dc:date` — publication year
- `dc:identifier` — DOI, URL, ISBN, or PubMed ID
- `dc:type` — journal-article, book, etc.

**Observation notes additionally require:**
- `observation_type` — pattern, somatic-marker, craft-knowledge, exemplar-story, contrast-case

### 2. Duplicate Detection
Before creating any note, run three searches:

1. `mcp__srl-vault__search_vault` with the proposed title
2. `mcp__srl-vault__search_vault` with the proposed slug (hyphenated and unhyphenated)
3. `mcp__srl-vault__search_vault` with 2-3 distinctive terms from the body

If any search returns a match with >70% overlap in subject matter:
- Do NOT create a new note
- Instead, produce an enrichment update via `mcp__srl-vault__update_note`
- Log the decision in the write log

### 3. MCP Tool Usage

**Creating notes:**
```
mcp__srl-vault__create_note
  note_type: concept | evidence | observation
  slug: kebab-case-name
  frontmatter: {JSON object with all required fields}
  body: "markdown content"
```

**Updating notes:**
```
mcp__srl-vault__update_note
  id: slug or URN
  frontmatter_updates: {JSON object with fields to merge}
  body: "new body content" (optional — only if replacing entirely)
```

**Linking evidence:**
```
mcp__srl-vault__add_evidence_link
  concept_id: concept-slug
  evidence_urn: "urn:srl:evidence:author-year-slug"
```

**Adding relationships:**
```
mcp__srl-vault__add_skos_relation
  slug: source-concept-slug
  relation_type: "skos:broader" | "skos:narrower" | "skos:related"
  target_slug: target-concept-slug
```

### 4. Enrichment Strategy

When enriching an existing note rather than creating:
- Read the existing note first: `mcp__srl-vault__get_note`
- Identify what's genuinely new (not already covered)
- Use `update_note` to merge new frontmatter fields
- For body additions, append to the relevant section rather than replacing
- Add new evidence links via `add_evidence_link`
- Add new relationships via `add_skos_relation`

### 5. Audit Logging

After every write operation, append to `outputs/vault-write-log.md`:
```markdown
| Date | Action | Note | Source | Details |
|------|--------|------|--------|---------|
| 2026-03-15 | CREATE | urn:srl:concept:new-slug | chatgpt-export:xyz | New concept: {title} |
| 2026-03-15 | UPDATE | urn:srl:concept:existing | chatgpt-export:xyz | Added evidence link, enriched body |
| 2026-03-15 | LINK | existing → new-slug | chatgpt-export:xyz | skos:related |
| 2026-03-15 | FLAG | urn:srl:concept:existing | chatgpt-export:xyz | Needs clinical_interpretation |
```

## Tools Used

- **Vault MCP tools (read):** `search_vault`, `get_note`, `list_concepts`, `get_evidence_chain`, `search_by_subject`
- **Vault MCP tools (write):** `create_note`, `update_note`, `add_evidence_link`, `add_skos_relation`, `promote_status`
- **Read** — extraction reports from `outputs/extractions/`

## Output Formats

1. **Vault Write Log** → `outputs/vault-write-log.md` — audit trail of all changes
2. **Needs Review** → `outputs/needs-review.md` — items flagged for Randy's input
