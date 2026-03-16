# Knowledge Miner Bot — Pattern Library

Accumulated extraction heuristics. Each pattern is discovered through retrospectives and validated across multiple files.

## Randy's Voice Patterns

*How to recognize Randy's original thinking vs. ChatGPT's elaboration*

| Signal | Meaning | Extraction Action | Confidence | Added |
|--------|---------|-------------------|------------|-------|
| Randy uses a capitalized novel term | Likely a coined/trademarked SRL concept | Extract as concept candidate | High | seed |
| Randy says "No, I mean..." or "That's not quite right" | Correction = insight; the redirect IS the knowledge | Extract the correction, not what came before | High | seed |
| Randy says "In my experience..." or "What I've seen in 28 years..." | Clinical observation from practice | Extract as observation (craft-knowledge or pattern) | High | seed |
| Randy provides a numbered list unprompted | Framework development — organizing his thinking | Extract as concept structure | Medium | seed |
| Randy asks "How does X connect to Y?" | Relationship discovery in progress | Extract as SKOS relationship candidate | Medium | seed |
| Randy says "Let me think about this differently" | Reframing — new lens on existing concept | Check for enrichment to existing concept | Medium | seed |

## ChatGPT Noise Patterns

*Content that looks extractable but usually isn't*

| Pattern | Why It's Noise | Action |
|---------|---------------|--------|
| ChatGPT's emoji-heavy headers (🧠, 🔬, ⚙️) | Formatting, not content | Skip formatting, read content only |
| "Here's how I'd frame this..." followed by 10 bullet points | ChatGPT expanding Randy's 2-sentence insight | Extract Randy's original, not the expansion |
| Tables mapping Randy's concepts to generic frameworks | Often superficial mapping, not deep synthesis | Verify Randy engaged with the mapping before extracting |
| "Based on your previous conversations..." | ChatGPT's memory recall — may be inaccurate | Cross-reference against vault, don't trust blindly |

## File Type Patterns

*Extraction approaches by file category (learned from triage feedback)*

| Category | Typical Extraction Approach | Yield Expectation |
|----------|---------------------------|-------------------|
| clinical | Focus on mechanism descriptions, protocol specs, patient observations | High (3-5 candidates/file) |
| strategy | Focus on market-specific claims with numbers, positioning language | Medium (1-3 candidates/file) |
| framework | Focus on novel synthesis across traditions, concept relationships | High (2-4 candidates/file) |
| product | Focus on design decisions with clinical rationale | Medium (1-2 candidates/file) |
| personal | Usually low yield unless personal insight drives product design | Low (0-1 candidates/file) |
| operations | Rarely extractable unless reveals strategic thinking | Low (0 candidates/file) |

## Concept Boundary Heuristics

*How to decide if something is a new concept vs. enrichment*

| Signal | Decision |
|--------|----------|
| Randy gives it a unique name | New concept |
| Randy describes a mechanism not in any existing note | New concept |
| Randy adds a new clinical observation to a known concept | Enrichment |
| Randy connects two existing concepts in a new way | Relationship discovery (not new concept) |
| Randy refines a definition he's used before | Enrichment (update existing) |
| ChatGPT suggests a name Randy doesn't adopt | NOT a concept — skip |

---

*Last updated: initial creation — no retrospectives yet*
*Pattern count: 6 voice patterns, 4 noise patterns, 6 file type patterns, 6 boundary heuristics (all seed)*
