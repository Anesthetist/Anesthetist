# Transcript Triage Bot — Skills

## Core Capabilities

### 1. File Metadata Extraction
For each `sources/chatgpt/*.md` file, extract from frontmatter:
- `title` — conversation title
- `created` — date of conversation
- `message_count` — number of exchanges
- `char_count` — total characters
- `participants` — who was involved

### 2. Content Sampling
Read the first 2-3 exchanges (Randy's opening prompt + ChatGPT's first response) to determine:
- What Randy was trying to accomplish
- What domain the conversation falls in
- Whether Randy was creating (novel thinking) or consuming (asking for summaries)

### 3. Classification
Assign each file to exactly one primary category and up to two secondary categories from the taxonomy.

### 4. Priority Scoring (1-10)

Score based on these weighted factors:

| Factor | Weight | High Score Indicators |
|--------|--------|----------------------|
| **Novelty** | 3x | Randy articulating original concepts, coining terms, developing frameworks |
| **Vault Gap** | 3x | Content maps to existing concept notes that are thin (draft status, missing clinical_interpretation) |
| **Depth** | 2x | Extended back-and-forth refining an idea (not one-shot Q&A) |
| **Recency** | 1x | More recent = higher priority (later thinking supersedes earlier) |
| **Size** | 1x | Larger files = more potential content (but diminishing returns above 200K chars) |

**Score interpretation:**
- 9-10: Must extract — contains novel IP, clinical insights, or fills critical vault gaps
- 7-8: High value — enriches existing concepts or contains strong evidence/observations
- 5-6: Moderate — useful context but may duplicate existing vault content
- 3-4: Low — mostly ChatGPT output, generic coaching, or operational chatter
- 1-2: Skip — file management, debugging, or irrelevant personal content

### 5. Target Mapping
For files scoring 7+, identify which vault nodes would benefit:
- Existing concept slugs that would be enriched
- Potential new concept notes to create
- Evidence or observation notes to derive

### 6. Duplicate Detection
Flag files that appear to cover the same ground:
- Same topic discussed across multiple sessions
- Identify which session is the "definitive" version (usually the longest or most recent)

## Tools Used

- **Read** — File headers and first exchanges only (never full transcripts)
- **Glob** — Find all source files
- **Grep** — Search for concept names, trademarked terms, key phrases
- **Vault MCP tools (read-only)** — `list_concepts`, `search_vault` to check what already exists

## Output Formats

1. **Extraction Queue** → `outputs/extraction-queue.md` — Top files ranked by priority with category and target nodes
2. **Extraction Manifest** → `outputs/extraction-manifest.md` — Complete inventory of all 861 files with metadata
