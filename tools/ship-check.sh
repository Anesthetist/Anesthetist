#!/usr/bin/env zsh
# SRL Ship Check — stronger pre-publish gate.
# Run this before declaring any output/* ready to leave the laptop.
#
# Usage: ./tools/ship-check.sh <file.md>
#
# What it does:
#   1. Runs the deterministic quality gate (em-dash, intensifiers, AI patterns, format)
#   2. Live-resolves every DOI in the file against doi.org
#   3. Flags [[wikilinks]] that point to evidence notes with status=draft/seed/seedling
#      (not ready to cite publicly)
#   4. Lists author-year mentions that require manual PubMed/web verification
#   5. Gertrude red-line word scan (flags for manual review — cannot regex compliance fully)
#
# Exit codes: 0 clean | 1 hard fail | 2 needs manual verification

set -uo pipefail

VAULT_DIR="${VAULT_DIR:-/Users/somnisticshq/Documents/Somnistics/Library-Graph}"
FILE="${1:-}"

if [[ -z "$FILE" || ! -f "$FILE" ]]; then
  echo "usage: $0 <file.md>" >&2
  exit 2
fi

if [[ -t 1 ]]; then
  RED=$'\033[0;31m'; YEL=$'\033[0;33m'; GRN=$'\033[0;32m'; CYA=$'\033[0;36m'; RST=$'\033[0m'
else
  RED=""; YEL=""; GRN=""; CYA=""; RST=""
fi

fail=0
warn=0

echo "${CYA}== Ship Check: $FILE ==${RST}"
echo ""

# ---- Stage 1: Local quality gate ----
echo "${CYA}[1/5] Quality gate${RST}"
if "$VAULT_DIR/tools/quality-gate.sh" check "$FILE"; then
  echo "  ${GRN}ok${RST}"
else
  fail=$((fail + 1))
fi
echo ""

# ---- Stage 2: Live DOI resolution ----
echo "${CYA}[2/5] Live DOI resolution${RST}"
dois=$(grep -oE '10\.[0-9]{4,9}/[^ )"'"'"'<>]+' "$FILE" 2>/dev/null | sort -u || true)
if [[ -z "$dois" ]]; then
  echo "  (no DOIs found)"
else
  while IFS= read -r doi; do
    [[ -z "$doi" ]] && continue
    doi="${doi%%.}"; doi="${doi%%,}"; doi="${doi%%)}"
    code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 12 "https://doi.org/$doi" 2>/dev/null || echo "000")
    if [[ "$code" =~ ^(200|301|302|303)$ ]]; then
      echo "  ${GRN}ok${RST}  doi:$doi  (HTTP $code)"
    else
      echo "  ${RED}BROKEN${RST}  doi:$doi  (HTTP $code)"
      fail=$((fail + 1))
    fi
    sleep 1
  done <<< "$dois"
fi
echo ""

# ---- Stage 3: Wikilink status check ----
echo "${CYA}[3/5] Vault wikilink status${RST}"
slugs=$(grep -oE '\[\[[a-z0-9][a-z0-9-]+\]\]' "$FILE" 2>/dev/null | tr -d '[]' | sort -u || true)
if [[ -z "$slugs" ]]; then
  echo "  (no wikilinks)"
else
  while IFS= read -r slug; do
    [[ -z "$slug" ]] && continue
    note_path=""
    for dir in evidence concepts observations audiences; do
      if [[ -f "$VAULT_DIR/$dir/${slug}.md" ]]; then
        note_path="$VAULT_DIR/$dir/${slug}.md"
        break
      fi
    done
    if [[ -z "$note_path" ]]; then
      echo "  ${RED}MISSING${RST} [[${slug}]] file does not exist"
      fail=$((fail + 1))
    else
      note_status=$(awk '/^status:/ {print $2; exit}' "$note_path" | tr -d '"' | tr -d "'")
      case "$note_status" in
        canonical|review|active|reviewed|captured)
          echo "  ${GRN}ok${RST}  [[${slug}]] status=$note_status"
          ;;
        draft|seed|seedling|"")
          echo "  ${YEL}weak${RST} [[${slug}]] status=${note_status:-unknown} - not promoted, weak citation"
          warn=$((warn + 1))
          ;;
        *)
          echo "  ${YEL}?${RST}    [[${slug}]] status=$note_status (unrecognized)"
          warn=$((warn + 1))
          ;;
      esac
    fi
  done <<< "$slugs"
fi
echo ""

# ---- Stage 4: Author-year citations needing manual verification ----
echo "${CYA}[4/5] Author-year citations (manual verification required)${RST}"
ay=$(grep -oE '\b[A-Z][a-z]+(( et al\.?)|( and [A-Z][a-z]+))? \(?(19|20)[0-9]{2}\)?' "$FILE" 2>/dev/null | sort -u || true)
if [[ -z "$ay" ]]; then
  echo "  (none)"
else
  echo "$ay" | sed 's/^/  /'
  echo ""
  echo "  ${YEL}Each must be verified in PubMed / Google Scholar before publish:${RST}"
  echo "  1. Paper exists at claimed year and by claimed author(s)"
  echo "  2. Paper's finding matches the claim being made in the essay"
  warn=$((warn + 1))
fi
echo ""

# ---- Stage 5: Gertrude red-line word scan ----
echo "${CYA}[5/5] Gertrude red-line scan${RST}"
RED_LINES="treats|cures|prevents|diagnoses|clinically proven|biofeedback therapy|therapeutic breathing|medical-grade|prescribes|mitigates"
hits=$(grep -niE "$RED_LINES" "$FILE" 2>/dev/null || true)
if [[ -z "$hits" ]]; then
  echo "  ${GRN}ok${RST} no red-line terms detected"
else
  echo "  ${RED}FLAG${RST} possible regulatory-sensitive language:"
  echo "$hits" | sed 's/^/    /'
  echo "  Run _bots/compliance-gertrude/run-protocol.md for full review."
  fail=$((fail + 1))
fi
echo ""

# ---- Verdict ----
echo "${CYA}== Verdict ==${RST}"
if (( fail > 0 )); then
  echo "${RED}NOT SHIP-READY${RST} ($fail hard fails, $warn warnings)"
  exit 1
elif (( warn > 0 )); then
  echo "${YEL}NEEDS MANUAL VERIFICATION${RST} ($warn warnings — address before publish)"
  exit 2
else
  echo "${GRN}SHIP-READY${RST}"
  exit 0
fi
