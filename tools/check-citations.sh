#!/usr/bin/env zsh
# SRL Citation Health Monitor
# Checks every evidence note's DOI/PMID/ISBN link and reports status.
# Usage: ./tools/check-citations.sh
# Designed for monthly cron/launchd execution.
#
# Outputs: outputs/citation-health-report.md

set -euo pipefail

VAULT_DIR="/Users/somnisticshq/Documents/Somnistics/Library-Graph"
EVIDENCE_DIR="$VAULT_DIR/evidence"
REPORT="$VAULT_DIR/outputs/citation-health-report.md"
TIMESTAMP=$(date +%Y-%m-%d)

# Rate-limit delay between HTTP checks (seconds) to avoid throttling
DELAY=1

# Ensure output dir exists
mkdir -p "$VAULT_DIR/outputs"

# Count evidence notes
NOTE_COUNT=$(ls "$EVIDENCE_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')

# Counters
TOTAL=0
VALID=0
MISSING_ID=0
BROKEN=0
ISBN_ONLY=0

# Temp file for the table rows (we insert summary above later)
TMPROWS=$(mktemp)

for f in "$EVIDENCE_DIR"/*.md; do
  slug=$(basename "$f" .md)
  TOTAL=$((TOTAL + 1))

  # --- Extract DOI ---
  # Look in dc:identifier line first, then anywhere in the file
  doi=""
  id_line=$(grep -i 'dc:identifier' "$f" 2>/dev/null | head -1 || true)
  if [[ -n "$id_line" ]]; then
    # Try to pull a DOI pattern from the identifier line
    doi=$(echo "$id_line" | grep -oE '10\.[0-9]{4,9}/[^ "'"'"'}>]+' 2>/dev/null | head -1 || true)
  fi
  # Fallback: scan whole file for DOI
  if [[ -z "$doi" ]]; then
    doi=$(grep -oE '10\.[0-9]{4,9}/[^ "'"'"'}>]+' "$f" 2>/dev/null | head -1 || true)
  fi

  # --- Extract PMID ---
  pmid=""
  pmid_match=$(grep -ioE 'PMID:?\s*[0-9]+' "$f" 2>/dev/null | head -1 || true)
  if [[ -n "$pmid_match" ]]; then
    pmid=$(echo "$pmid_match" | grep -oE '[0-9]+' | head -1)
  fi

  # --- Extract ISBN ---
  isbn=""
  isbn_match=$(grep -ioE 'ISBN:?\s*[0-9X-]+' "$f" 2>/dev/null | head -1 || true)
  if [[ -n "$isbn_match" ]]; then
    isbn=$(echo "$isbn_match" | grep -oE '[0-9X-]+' | head -1)
  fi

  # --- Check link validity ---
  if [[ -n "$doi" ]]; then
    # Strip trailing punctuation that may have been captured
    doi="${doi%%.}"
    doi="${doi%%,}"
    http_code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 15 "https://doi.org/$doi" 2>/dev/null || echo "000")
    if [[ "$http_code" == "200" || "$http_code" == "301" || "$http_code" == "302" || "$http_code" == "303" ]]; then
      echo "| $slug | \`$doi\` | Valid | [DOI](https://doi.org/$doi) |" >> "$TMPROWS"
      VALID=$((VALID + 1))
    else
      echo "| $slug | \`$doi\` | **Broken** ($http_code) | [try](https://doi.org/$doi) |" >> "$TMPROWS"
      BROKEN=$((BROKEN + 1))
    fi
    sleep "$DELAY"
  elif [[ -n "$pmid" ]]; then
    http_code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 15 "https://pubmed.ncbi.nlm.nih.gov/$pmid/" 2>/dev/null || echo "000")
    if [[ "$http_code" == "200" ]]; then
      echo "| $slug | PMID:$pmid | Valid | [PubMed](https://pubmed.ncbi.nlm.nih.gov/$pmid/) |" >> "$TMPROWS"
      VALID=$((VALID + 1))
    else
      echo "| $slug | PMID:$pmid | **Broken** ($http_code) | [try](https://pubmed.ncbi.nlm.nih.gov/$pmid/) |" >> "$TMPROWS"
      BROKEN=$((BROKEN + 1))
    fi
    sleep "$DELAY"
  elif [[ -n "$isbn" ]]; then
    # ISBNs are books -- we mark them as ISBN-only (no live link to check)
    echo "| $slug | ISBN:$isbn | ISBN-only | [WorldCat](https://search.worldcat.org/search?q=isbn:${isbn//[-]/}) |" >> "$TMPROWS"
    ISBN_ONLY=$((ISBN_ONLY + 1))
  else
    echo "| $slug | -- | **No identifier** | -- |" >> "$TMPROWS"
    MISSING_ID=$((MISSING_ID + 1))
  fi

  # Progress indicator
  if (( TOTAL % 10 == 0 )); then
    echo "  checked $TOTAL / $NOTE_COUNT ..."
  fi
done

# Calculate health percentage (exclude ISBN-only from denominator since we can't check them)
CHECKABLE=$((TOTAL - ISBN_ONLY))
if (( CHECKABLE > 0 )); then
  HEALTH=$((VALID * 100 / CHECKABLE))
else
  HEALTH=0
fi

# Build the report
cat > "$REPORT" <<HEADER
# Citation Health Report

**Generated:** $TIMESTAMP
**Evidence notes scanned:** $TOTAL

## Summary

| Metric | Count |
|--------|-------|
| Total evidence notes | $TOTAL |
| Valid links (DOI/PMID) | $VALID |
| ISBN-only (books, no link check) | $ISBN_ONLY |
| Missing identifier | $MISSING_ID |
| Broken links | $BROKEN |
| Link health | ${HEALTH}% |

## Details

| Note | Identifier | Status | Link |
|------|-----------|--------|------|
HEADER

cat "$TMPROWS" >> "$REPORT"
rm -f "$TMPROWS"

echo ""
echo "=== Citation Health Check Complete ==="
echo "Total: $TOTAL | Valid: $VALID | ISBN-only: $ISBN_ONLY | Missing: $MISSING_ID | Broken: $BROKEN | Health: ${HEALTH}%"
echo "Report: $REPORT"
