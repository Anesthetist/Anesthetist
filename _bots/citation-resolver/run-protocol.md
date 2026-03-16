<!-- v1.0 — initial creation 2026-03-15 -->
# Citation Resolver Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/citation-resolver/soul.md`
2. Read `_bots/citation-resolver/learning-log.md` — load search strategies that worked before
3. Read the flagged evidence items from `outputs/needs-review.md` (Evidence Needing Verification section) or items passed by the review-accelerator

## Execution Steps

### Step 1: Parse the Citation Clues

For each unverified evidence item, extract available information:
- Author name(s) — even partial
- Year — exact or approximate
- Title — full, partial, or keywords
- Journal or publisher
- Key finding described in the vault note
- Any URL or identifier fragments

### Step 2: Search Strategy (escalating)

Try these approaches in order, stopping when a match is found:

**Level 1: PubMed Search**
```
mcp__claude_ai_PubMed__search_articles
  query: "{author} {year} {key terms from finding}"
```

If results returned:
```
mcp__claude_ai_PubMed__get_article_metadata
  pmid: {matched article ID}
```

**Level 2: PubMed Citation Lookup**
```
mcp__claude_ai_PubMed__lookup_article_by_citation
  citation: "{author}, {year}, {partial title or journal}"
```

**Level 3: Web Search**
```
WebSearch: "{author}" "{year}" "{key phrase from title or finding}"
WebSearch: "{author}" "{key finding}" site:pubmed.ncbi.nlm.nih.gov OR site:doi.org
```

**Level 4: Related Articles**
If a related study IS in the vault with a PubMed ID:
```
mcp__claude_ai_PubMed__find_related_articles
  pmid: {known related article}
```

**Level 5: Broader Search**
```
WebSearch: "{key finding}" "{year}" review OR meta-analysis
```

### Step 3: Verify the Match

When a candidate match is found:
1. Compare the key finding attributed in the vault note to the actual abstract
2. Verify author names match
3. Verify year matches
4. If the finding matches → confirmed
5. If the finding doesn't match → flag discrepancy, continue searching

### Step 4: Update Vault Note

For confirmed matches, update the evidence note via MCP:

```
mcp__srl-vault__update_note
  id: {evidence-slug}
  frontmatter_updates: {
    "dc:identifier": "{DOI or PubMed URL}",
    "dc:publisher": "{journal name}",
    "dc:creator": [{verified author list}],
    "dc:date": {verified year},
    "dc:type": "{article type}"
  }
```

### Step 5: Report Results

For each citation processed:

```markdown
| Citation | Status | Method | DOI/PMID | Notes |
|----------|--------|--------|----------|-------|
| {author-year} | Verified | PubMed search | doi:10.xxxx | Exact match |
| {author-year} | Verified | Web search | PMID:12345 | Title differed slightly |
| {author-year} | Unresolved | All 5 levels tried | — | Possible ChatGPT hallucination |
| {author-year} | Discrepancy | PubMed | doi:10.xxxx | Finding attributed doesn't match actual study |
```

### Step 6: Run Retrospective

1. Calculate resolution rate (verified / total attempted)
2. Which search levels were most effective?
3. Were there patterns in unresolved citations? (e.g., "ChatGPT frequently miscites author X")
4. Update `learning-log.md`
5. Increment version comment

## Error Handling

- PubMed MCP tools unavailable → fall back to WebSearch only
- Multiple potential matches → present all candidates, flag for review-accelerator
- ChatGPT hallucinated the study entirely → mark as "likely hallucination", remove from evidence note, flag for Randy
