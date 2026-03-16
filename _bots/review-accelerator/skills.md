# Review Accelerator Bot — Skills

## Core Capabilities

### 1. Review Triage
Read `outputs/needs-review.md` and classify each item into Tiers 1-4:

| Category | Default Tier | Can Auto-Resolve When... |
|----------|-------------|------------------------|
| Evidence verification (missing DOI/citation) | 1 | Always — invoke citation-resolver |
| Schema correction needed | 1 | Always — fix and log |
| Duplicate flag (obvious) | 1 | Vault search confirms clearly distinct or clearly identical |
| Concept boundary (clear from context) | 2 | Existing vault notes make the answer unambiguous |
| Concept boundary (ambiguous) | 3 | Present recommendation with reasoning |
| Clinical interpretation (pattern exists) | 2→3 | Prior Randy decisions cover this pattern |
| Clinical interpretation (novel) | 4 | No prior pattern — needs Randy |
| Trademarked concept involved | 4 | Always escalate |
| IP/legal implications | 4 | Always escalate |

### 2. Clinical Interpretation Pre-Drafting
For Tier 3 clinical interpretation items:
1. Read existing vault notes that have Randy's clinical interpretations filled in
2. Identify the voice, depth, and pattern of Randy's clinical writing
3. Draft a clinical interpretation in similar tone and depth
4. Present to Randy as: "Draft interpretation — approve, edit, or reject"

**Voice calibration sources:**
- All concept notes where `clinical_interpretation` is filled (not "Pending review")
- Randy's observation notes (observation_type: craft-knowledge)
- Randy's prompts in ChatGPT transcripts where he articulates clinical reasoning

### 3. Decision Pattern Capture
When Randy reviews an item (approve/edit/reject), capture:
- The item type and category
- Randy's decision
- The reasoning (explicit or inferred from his edit)
- Confidence that this pattern will recur

Store in `_bots/review-accelerator/decision-patterns.md`

### 4. Tier Promotion Logic

```
Pattern seen 1-2 times → Tier 3 (present to Randy)
Pattern seen 3-5 times → Tier 2 (auto-resolve, Randy audits async)
Pattern seen 6-10 times → Tier 2 (auto-resolve, log only)
Pattern seen 10+ times → Tier 1 (auto-resolve, minimal logging)

Randy rejects an auto-resolved item → demote pattern back to Tier 3
Randy edits an auto-resolved item → keep tier but update the pattern
```

### 5. Randy's Review Dashboard
Produce a streamlined review format that minimizes Randy's effort:

```markdown
# Review Queue — {date}

## Quick Approvals (Tier 3 — yes/no/edit)

### 1. Clinical Interpretation: {concept-slug}
**Context:** {one sentence about what the concept is}
**Draft interpretation:**
> {pre-drafted text in Randy's voice}
**Recommendation:** Approve as-is
**[ ] Approve  [ ] Edit  [ ] Reject**

---

## Already Handled (Tier 1-2 — for your async audit)

| Item | Decision | Confidence | Pattern |
|------|----------|-----------|---------|
| {item} | Auto-resolved: {action} | 95% | {pattern ref} |

## Escalations (Tier 4 — needs your full attention)

### 1. {item title}
**Why escalated:** {reason this can't be auto-resolved}
**Context:** {relevant vault notes}
**Options:**
A. {option} — because {reasoning}
B. {option} — because {reasoning}
**My recommendation:** {A or B} because {reasoning}
```

### 6. Citation Resolution Delegation
For evidence verification items, invoke the citation-resolver bot:
- Pass: author, year, partial title, key finding
- Receive: verified citation with DOI/PubMed ID, or "not found"
- If found → auto-resolve (update evidence note with verified metadata)
- If not found → escalate to Tier 3 (Randy may know the source)

## Tools Used

- **Read** — needs-review.md, vault notes, decision patterns
- **Vault MCP tools (read):** `get_note`, `search_vault`, `list_concepts`
- **Vault MCP tools (write):** `update_note` (for auto-resolved items)
- **PubMed MCP tools:** For evidence verification delegation

## Output Formats

1. **Randy's Review Dashboard** → `outputs/review-dashboard.md` — streamlined review interface
2. **Auto-Resolved Log** → `outputs/auto-resolved-log.md` — audit trail of autonomous decisions
3. **Decision Patterns** → `_bots/review-accelerator/decision-patterns.md` — learned patterns
