#!/usr/bin/env zsh
# SRL Evidence Brief Generator
# Generates a Pausality-styled HTML evidence brief from a hypothesis.
#
# Usage:
#   ./tools/evidence-brief.sh "Does cardiac-anchored breathing produce greater HRV improvements than fixed-rate breathing?"
#
# Requirements:
#   - claude CLI (claude -p)
#   - python3 (for BioMistral query)
#   - HUGGINGFACE_TOKEN env var or .env file in vault root
#
# Output: Single-page HTML in outputs/evidence-briefs/

set -euo pipefail

# --- Config ---
VAULT_DIR="/Users/somnisticshq/Documents/Somnistics/Library-Graph"
TOOLS_DIR="$VAULT_DIR/tools"
OUTPUT_DIR="$VAULT_DIR/outputs/evidence-briefs"
TIMESTAMP=$(date +%Y-%m-%d)
TIMESTAMP_FILE=$(date +%Y-%m-%d_%H%M)

# --- Validate input ---
if [[ -z "${1:-}" ]]; then
  echo "Usage: $0 \"Your hypothesis here\""
  echo ""
  echo "Example:"
  echo "  $0 \"Does cardiac-anchored breathing produce greater HRV improvements than fixed-rate breathing?\""
  exit 1
fi

HYPOTHESIS="$1"

# Generate slug from hypothesis (lowercase, alphanumeric + hyphens, max 60 chars)
SLUG=$(echo "$HYPOTHESIS" | tr '[:upper:]' '[:lower:]' | tr -cs '[:alnum:]' '-' | sed 's/^-//;s/-$//' | cut -c1-60)
OUTPUT="$OUTPUT_DIR/${SLUG}.html"

mkdir -p "$OUTPUT_DIR"

echo "============================================"
echo "  SRL Evidence Brief Generator"
echo "============================================"
echo ""
echo "Hypothesis: $HYPOTHESIS"
echo "Output:     $OUTPUT"
echo ""

# --- Step 1: Search vault for related concepts and evidence ---
echo "[1/4] Searching vault for related content..."

# Extract key terms from hypothesis (words > 4 chars, deduplicated)
KEY_TERMS=$(echo "$HYPOTHESIS" | tr '[:upper:]' '[:lower:]' | tr -cs '[:alnum:]\n' ' ' | tr ' ' '\n' | awk 'length > 4' | sort -u | head -20)

VAULT_HITS=""
VAULT_CONCEPTS=""
VAULT_EVIDENCE=""

for term in ${(f)KEY_TERMS}; do
  # Search concepts
  hits=$(grep -ril "$term" "$VAULT_DIR/concepts/" 2>/dev/null | head -5)
  if [[ -n "$hits" ]]; then
    VAULT_CONCEPTS="$VAULT_CONCEPTS\n$hits"
  fi
  # Search evidence
  hits=$(grep -ril "$term" "$VAULT_DIR/evidence/" 2>/dev/null | head -5)
  if [[ -n "$hits" ]]; then
    VAULT_EVIDENCE="$VAULT_EVIDENCE\n$hits"
  fi
done

# Deduplicate
VAULT_CONCEPTS=$(echo "$VAULT_CONCEPTS" | sort -u | head -15)
VAULT_EVIDENCE=$(echo "$VAULT_EVIDENCE" | sort -u | head -15)

CONCEPT_COUNT=$(echo "$VAULT_CONCEPTS" | grep -c '/' 2>/dev/null || echo "0")
EVIDENCE_COUNT=$(echo "$VAULT_EVIDENCE" | grep -c '/' 2>/dev/null || echo "0")

echo "  Found $CONCEPT_COUNT related concepts, $EVIDENCE_COUNT evidence notes."

# Build vault context: extract titles from matched files
VAULT_CONTEXT=""
for f in ${(f)VAULT_CONCEPTS}; do
  [[ -z "$f" ]] && continue
  title=$(grep '^title:' "$f" 2>/dev/null | head -1 | sed 's/^title: *//' | tr -d '"')
  [[ -n "$title" ]] && VAULT_CONTEXT="$VAULT_CONTEXT\n- Concept: $title"
done
for f in ${(f)VAULT_EVIDENCE}; do
  [[ -z "$f" ]] && continue
  title=$(grep '^title:' "$f" 2>/dev/null | head -1 | sed 's/^title: *//' | tr -d '"')
  doi=$(grep '^dc:identifier:' "$f" 2>/dev/null | head -1 | sed 's/^dc:identifier: *//' | tr -d '"')
  [[ -n "$title" ]] && VAULT_CONTEXT="$VAULT_CONTEXT\n- Evidence: $title ($doi)"
done

echo ""

# --- Step 2: Run BioMistral query ---
echo "[2/4] Querying BioMistral for biomedical evaluation..."

BIOMISTRAL_RESULT=""
if [[ -f "$TOOLS_DIR/biomedical-query.py" ]]; then
  BIOMISTRAL_RESULT=$(python3 "$TOOLS_DIR/biomedical-query.py" --max-tokens 1500 \
    "Evaluate this hypothesis for supporting and contradicting evidence. Be specific about study designs, sample sizes, and evidence levels. Hypothesis: $HYPOTHESIS" 2>&1) || true

  if [[ -z "$BIOMISTRAL_RESULT" ]] || echo "$BIOMISTRAL_RESULT" | grep -qi "error\|loading\|timeout"; then
    echo "  BioMistral unavailable or returned error. Proceeding with vault context only."
    BIOMISTRAL_RESULT="BioMistral query unavailable. Synthesis based on vault evidence only."
  else
    echo "  BioMistral response received ($(echo "$BIOMISTRAL_RESULT" | wc -c | tr -d ' ') chars)."
  fi
else
  echo "  biomedical-query.py not found. Skipping BioMistral."
  BIOMISTRAL_RESULT="BioMistral not available."
fi

echo ""

# --- Step 3: Generate HTML via Claude ---
echo "[3/4] Generating evidence brief via Claude..."

# Build the synthesis prompt
PROMPT=$(cat <<ENDPROMPT
Generate a complete, single-page Pausality-styled HTML evidence brief. Output ONLY the HTML — no markdown fences, no explanation, just the <!DOCTYPE html> through </html>.

HYPOTHESIS: $HYPOTHESIS

VAULT CONTEXT (related SRL knowledge graph entries):
$(echo "$VAULT_CONTEXT")

BIOMISTRAL SYNTHESIS:
$BIOMISTRAL_RESULT

DESIGN REQUIREMENTS:
- Dark background #1A1D2E, sage accent #5FC89B, text #F5F5F0, Poppins font from Google Fonts
- Card background #242840
- One-page executive brief for clinical leadership (surgeons, CNOs, clinical directors)
- Every sentence earns its space. No marketing language. "The literature suggests" not "we believe."

STRUCTURE (follow exactly):
1. HEADER: "Evidence Brief: [topic from hypothesis]"
   SUBTITLE: "Somnistics Research Labs | For Clinical Leadership Review"

2. THE HYPOTHESIS: 2-3 sentences, in a sage-bordered card

3. EVIDENCE SUPPORTS: 3 cards in a row (green left border)
   Each card: phase label, 2-3 sentence finding, citation with evidence level badge

4. EVIDENCE CHALLENGES: 2x2 grid of cards (red left border)
   Each card: challenge name, 2-3 sentence explanation of the gap, level badge
   Include: dose/duration gaps, ecological validity, missing RCTs, integration gaps

5. THE HONEST ASSESSMENT: amber-bordered box
   Three paragraphs: what is strong, what is absent, where the research gap lives
   Use Oxford CEBM levels (1a, 1b, 2a, 2b, 3, 4, 5)

6. THREE THINGS WE ARE DOING ABOUT IT: numbered list with blue step indicators
   Plausible next research steps that would close the evidence gaps

7. FOOTER: "Vigil | SRL Knowledge Graph | Generated $TIMESTAMP"
   Second line: "All claims graded per Oxford CEBM. Cross-referenced against PubMed and SRL vault."
   Third line: "This brief describes research landscapes. It does not prescribe clinical behavior."

TONE: Direct. Clinical precision. If a surgeon reads this and thinks "these people know what they don't know," you have succeeded.
ENDPROMPT
)

# Run Claude synthesis
claude -p --output-format text "$PROMPT" > "$OUTPUT" 2>/dev/null

# Validate output
if [[ ! -s "$OUTPUT" ]]; then
  echo "  ERROR: Claude produced empty output."
  echo "  Check that 'claude' CLI is installed and authenticated."
  exit 1
fi

# Check it looks like HTML
if ! head -5 "$OUTPUT" | grep -qi "<!DOCTYPE\|<html"; then
  echo "  WARNING: Output may not be valid HTML. Check $OUTPUT manually."
fi

echo "  Evidence brief written ($(wc -c < "$OUTPUT" | tr -d ' ') bytes)."
echo ""

# --- Step 4: Open in browser ---
echo "[4/4] Opening in browser..."
open "$OUTPUT"

echo ""
echo "============================================"
echo "  Evidence brief generated successfully."
echo "  $OUTPUT"
echo "============================================"
