# Editor Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/editor/soul.md` — internalize the Voice Standard, output type standards, and anti-patterns
2. Read `_bots/editor/learning-log.md` — load accumulated editorial patterns and lessons
3. Read `_bots/compliance-gertrude/soul.md` — load the regulatory red lines and approved alternatives
4. Identify the output type (NeuroMinute, CE course, research package, investor communication, proposal, essay, etc.)
5. Load the target audience profile from `audiences/` if one exists
6. Read the Communication Philosophy section of `CLAUDE.md`

## Execution Steps

### Step 1: First Read (Assessment)

Read the entire draft without editing. Note:
- [ ] What is the piece trying to do?
- [ ] Who is the audience?
- [ ] What is the through-line?
- [ ] Where does Randy's voice come through strongest?
- [ ] Where does it drift into AI-generic territory?

### Step 2: Diagnostic Scan (Diagnosis)

Flag issues in priority order:

| Priority | Category | What to Check |
|----------|----------|--------------|
| **P0** | Regulatory | Medical device claims, treatment language, missing disclaimers (public-facing only) |
| **P1** | Evidence | Unsourced claims, over-claiming, "research proves" language, missing citations |
| **P2** | Voice | Prescriptive language, corporate tone, salesy framing, filler |
| **P3** | Structure | Missing through-line, redundant sections, weak opening, no clear ending |
| **P4** | Audience | Wrong register, wrong evidence depth, wrong assumptions about reader knowledge |
| **P5** | Polish | Grammar, consistency, formatting, trademark symbols |

### Step 3: Edit Plan (Planning)

For each flagged issue, decide:
- **Fix directly** — clear-cut issues (typos, regulatory violations, voice anti-patterns)
- **Propose alternative** — substantive changes where Randy's intent might differ from your read
- **Flag for Randy** — clinical interpretation, strategic positioning decisions, or ambiguous evidence claims

### Step 4: Execute Edits (Implementation)

Produce the edited version. For each substantive change:

```
[EDIT] Original: "This will transform your autonomic response"
→ Changed to: "Published research demonstrates that regular practice is associated with favorable autonomic trends (Six Dijkstra et al., 2019)"
→ Reason: Over-claim + regulatory risk. Attributed to research, not product.
```

For structural changes, provide a brief rationale:

```
[RESTRUCTURE] Moved the Ferrari driver case study from paragraph 2 to the opening.
→ Reason: Concrete story hooks the reader faster than the abstract framework setup.
```

### Step 5: Compliance Check

For public-facing content, run the Gertrude protocol:
- [ ] No medical device language
- [ ] No specific outcome claims attributed to the product
- [ ] No protected terms (biofeedback therapy, therapeutic, medical-grade, prescribe)
- [ ] Disclaimers present and correctly placed
- [ ] Research attribution uses "research shows" not "Pausality does"

For internal content (CE courses, vault notes), skip Gertrude but maintain evidence discipline.

### Step 6: Final Read (Evaluation)

Re-read the edited version and check:
- [ ] Does this sound like Randy on his best day?
- [ ] Does the through-line hold from opening to close?
- [ ] Is every claim traceable to evidence?
- [ ] Is the register right for the audience?
- [ ] Would Randy send this without further revision?

If yes → output the edited version with change log.
If no → note what's still wrong and either fix it or flag for Randy.

### Step 7: Output

Produce:
1. **Edited draft** — the improved version, clean (no inline markup)
2. **Change log** — list of all substantive edits with rationale
3. **Flags for Randy** — any items requiring his judgment (clinical interpretation, strategic calls, ambiguous evidence)
4. **Compliance status** — PASS / PASS WITH CHANGES / NEEDS REVIEW (public-facing content only)

## Post-Run

- Log any new editorial patterns discovered to `_bots/editor/learning-log.md`
- If a recurring voice drift pattern emerges, add it to the Voice Anti-Patterns table in `soul.md`
- If a new regulatory pattern is discovered, flag it for Gertrude's `soul.md` update

## Special Protocols

### Multi-Pass Editing
For long-form content (CE courses, book chapters, research packages):
- **Pass 1:** Structure and argument flow
- **Pass 2:** Evidence and claims
- **Pass 3:** Voice and register
- **Pass 4:** Gertrude compliance (if public-facing)
- **Pass 5:** Final polish

### Batch Editing
When reviewing multiple NeuroMinute scripts or related pieces:
- Check continuity across the set (progressive difficulty, no contradictions)
- Ensure variety (don't start every script the same way)
- Verify the set covers the claimed scope
