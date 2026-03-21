#!/usr/bin/env zsh
# SRL Citation Link Injector
# Scans evidence notes and adds clickable reference links where missing.
# Usage: ./tools/add-citation-links.sh [--dry-run]
#
# For each evidence note:
#   - If it has a DOI but no clickable DOI link in the body, appends one
#   - If it has a PMID but no clickable PubMed link in the body, appends one
#   - Format: **Full text:** [DOI](https://doi.org/10.xxxx) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/XXXXX/)

set -euo pipefail

VAULT_DIR="/Users/somnisticshq/Documents/Somnistics/Library-Graph"
EVIDENCE_DIR="$VAULT_DIR/evidence"
DRY_RUN=false

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
  echo "=== DRY RUN — no files will be modified ==="
fi

ADDED=0
SKIPPED=0
TOTAL=0

for f in "$EVIDENCE_DIR"/*.md; do
  slug=$(basename "$f" .md)
  TOTAL=$((TOTAL + 1))

  # --- Extract DOI ---
  doi=""
  id_line=$(grep -i 'dc:identifier' "$f" 2>/dev/null | head -1 || true)
  if [[ -n "$id_line" ]]; then
    doi=$(echo "$id_line" | grep -oE '10\.[0-9]{4,9}/[^ "'"'"'}>]+' 2>/dev/null | head -1 || true)
  fi
  if [[ -z "$doi" ]]; then
    doi=$(grep -oE '10\.[0-9]{4,9}/[^ "'"'"'}>]+' "$f" 2>/dev/null | head -1 || true)
  fi
  # Clean trailing punctuation
  if [[ -n "$doi" ]]; then
    doi="${doi%%.}"
    doi="${doi%%,}"
  fi

  # --- Extract PMID ---
  pmid=""
  pmid_match=$(grep -ioE 'PMID:?\s*[0-9]+' "$f" 2>/dev/null | head -1 || true)
  if [[ -n "$pmid_match" ]]; then
    pmid=$(echo "$pmid_match" | grep -oE '[0-9]+' | head -1)
  fi

  # --- Check if clickable links already exist in the body ---
  has_doi_link=false
  has_pmid_link=false
  if [[ -n "$doi" ]] && grep -q "doi.org/$doi" "$f" 2>/dev/null; then
    has_doi_link=true
  fi
  if [[ -n "$pmid" ]] && grep -q "pubmed.ncbi.nlm.nih.gov/$pmid" "$f" 2>/dev/null; then
    has_pmid_link=true
  fi

  # Build the link line
  link_parts=()
  if [[ -n "$doi" && "$has_doi_link" == false ]]; then
    link_parts+=("[DOI](https://doi.org/$doi)")
  fi
  if [[ -n "$pmid" && "$has_pmid_link" == false ]]; then
    link_parts+=("[PubMed](https://pubmed.ncbi.nlm.nih.gov/$pmid/)")
  fi

  if (( ${#link_parts[@]} == 0 )); then
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  # Join parts with " | "
  link_line="**Full text:** ${(j: | :)link_parts}"

  if $DRY_RUN; then
    echo "  [dry-run] $slug -> $link_line"
  else
    # Check if a "Full text:" line already exists
    if grep -q '^\*\*Full text:\*\*' "$f" 2>/dev/null; then
      # Replace existing line
      sed -i '' "s|^\*\*Full text:\*\*.*|$link_line|" "$f"
    else
      # Append after the frontmatter closing ---
      # Find the second --- (end of YAML frontmatter) and append after the heading
      echo "" >> "$f"
      echo "$link_line" >> "$f"
    fi
    echo "  [added] $slug -> $link_line"
  fi
  ADDED=$((ADDED + 1))
done

echo ""
echo "=== Citation Link Injection Complete ==="
echo "Total: $TOTAL | Links added: $ADDED | Skipped (already present or no ID): $SKIPPED"
