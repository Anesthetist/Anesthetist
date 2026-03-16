<!-- v1.0 — initial creation 2026-03-15 -->
# Knowledge Miner Bot — Run Protocol

## Pre-Run Checklist

1. Read `_bots/knowledge-miner/soul.md` — internalize the persona
2. Read `_bots/knowledge-miner/skills.md` — know the extraction rules
3. Read `_bots/knowledge-miner/patterns.md` — load accumulated extraction heuristics from prior runs
4. Read `_bots/knowledge-miner/learning-log.md` — know what was learned last time, including vault-writer feedback
5. Read `_bots/knowledge-miner/memory.md` — know what's already been extracted
6. Run `mcp__srl-vault__list_concepts` — load current concept inventory
7. Read `_schema/note-types.yaml` — know required fields for each note type
8. Read the target file's triage entry in `outputs/extraction-queue.md` if available — know what category and target nodes were identified

## Execution Steps

### Step 1: Read the Transcript

Read the full `sources/chatgpt/{filename}` file. On first pass, identify:
- Total message count and conversation arc
- Randy's key prompts (what was he trying to accomplish?)
- Where the conversation gets deep (multi-turn refinement of an idea)
- Where Randy corrects or redirects ChatGPT (corrections = insights)

### Step 2: Extract Randy's Voice

Go through the transcript again, this time extracting only:
- **Randy's assertions** — statements of fact, opinion, or framework
- **Randy's questions that reveal thinking** — "What if we..." "How does X connect to Y..."
- **Randy's corrections** — "No, I mean..." "That's not quite right, the actual mechanism is..."
- **Randy's coined terms** — novel words or phrases he's developing
- **Randy's clinical anecdotes** — stories from practice

Ignore:
- ChatGPT's generic elaborations (unless Randy explicitly endorsed them)
- Coaching advice Randy didn't engage with
- Tool/API calls and system messages
- Repetitive prompts (file uploads, formatting requests)

### Step 3: Check Vault for Existing Coverage

For each potential extraction:
1. `mcp__srl-vault__search_vault` with the concept name
2. `mcp__srl-vault__search_vault` with key terms from the content
3. If a match exists, `mcp__srl-vault__get_note` to read the existing note
4. Determine: is this a NEW concept or an ENRICHMENT of an existing one?

### Step 4: Structure Candidates

For each extraction candidate, produce the full structured output per skills.md format:
- Complete frontmatter matching `_schema/note-types.yaml`
- URN ID in proper format
- Body content derived from Randy's words (not ChatGPT's expansions)
- `prov:wasDerivedFrom` linking back to the source chat-import URN
- `dc:source` referencing the ChatGPT export ID
- SKOS relationships to existing vault concepts

### Step 5: Quality Check

Before including in the extraction report, each candidate must pass:
- [ ] Has a clear, non-duplicate slug
- [ ] Frontmatter includes all required fields for its type
- [ ] Body adds genuine knowledge (not just a definition that exists elsewhere)
- [ ] At least one provenance link
- [ ] At least one subject tag
- [ ] `clinical_interpretation` is "Pending review" (never filled by bot)
- [ ] No personal/private information
- [ ] Attributions are accurate (Randy's words vs. ChatGPT's)

### Step 6: Produce Extraction Report

Write the extraction report to `outputs/extractions/{source-slug}-extraction.md` following the template in skills.md.

### Step 7: Update Memory

Append to `_bots/knowledge-miner/memory.md`:
- File processed
- Date
- Concepts extracted (new + enrichments)
- Evidence notes identified
- Observations captured
- Items flagged for review

## Processing Guidelines

### Handling Long Transcripts (>100K chars)

For very long conversations:
1. First pass: scan for section breaks, topic shifts, and key moments
2. Focus extraction on the densest sections (where Randy and ChatGPT go back-and-forth refining)
3. Skip sections that are purely operational (file uploads, formatting, debugging)

### Handling Multi-Topic Conversations

Some sessions cover multiple unrelated topics:
1. Treat each topic segment as a separate extraction unit
2. Produce separate candidates for each topic
3. Note the topic boundaries in the extraction report

### Handling Concept Evolution

When a concept evolves across multiple sessions:
1. Check memory.md for earlier extractions of the same concept
2. Identify what's NEW in this session vs. what was already captured
3. Produce an enrichment candidate that adds only the new material
4. Note the evolution in the report: "This session refines {concept} from {earlier session}"

## Error Handling

- If the transcript is truncated (`*[message truncated — full text in source]*`), work with what's available and flag truncation points
- If evidence is mentioned without sufficient citation detail, add to "Flagged for Review" rather than fabricating metadata
- If you're unsure whether something is Randy's original thinking or common knowledge, flag it

## Step 8: Run Retrospective

After completing the extraction, execute the retrospective protocol per `_bots/knowledge-miner/retrospective.md`:
1. Calculate extraction yield metrics
2. Analyze signal-to-noise ratio
3. Check attribution accuracy
4. Append retrospective entry to `learning-log.md`
5. Update `patterns.md` with any new extraction heuristics
6. Feed triage calibration data back (was the triage score accurate?)
7. Increment version comment at top of this file
