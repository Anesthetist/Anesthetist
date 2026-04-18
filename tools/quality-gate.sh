#!/usr/bin/env zsh
# SRL Quality Gate — local deterministic checks before outputs/ ship
#
# Subcommands:
#   check <file>    — check a single file; exit non-zero on fail
#   staged          — check all staged outputs/*.md (pre-commit hook)
#   sweep           — scan all outputs/, write outputs/quality-sweep-report.md
#   citations <f>   — just citation checks on one file
#
# Rules enforced (deterministic, no LLM):
#   1. Em-dash density: ≤3 per 100 lines (excluding citations/frontmatter blocks)
#   2. Intensifiers: zero tolerance for precisely/literally/fundamentally/critically/essentially/genuinely/simply/truly/merely
#   3. AI throat-clear transitions: flag "This is where X enters", "It's worth noting",
#      "Importantly,", "That is true. But", "In conclusion", "To summarize"
#   4. "Not just X, it's Y" / "It's not X, it's Y" rhetorical pattern: flag
#   5. Citation hygiene:
#      - DOI pattern 10.xxxx/yyyy must match regex (well-formed)
#      - [[vault-slug]] wikilinks to evidence must resolve to an existing file
#      - "Author Year" mentions flagged for manual verification
#
# Exit codes: 0 pass, 1 fail (blocks commit), 2 warnings-only (sweep mode only)

set -uo pipefail

VAULT_DIR="${VAULT_DIR:-/Users/somnisticshq/Documents/Somnistics/Library-Graph}"
MODE="${1:-}"
FILE="${2:-}"

# Thresholds — tunable via env
MAX_EMDASH_PER_100=${MAX_EMDASH_PER_100:-3}
INTENSIFIER_WORDS="precisely|literally|fundamentally|critically|essentially|genuinely|simply|truly|merely"
THROAT_CLEAR='This is where[^.]*enters|It'"'"'s worth noting|^Importantly,|That is true\. But|In conclusion|To summarize|It should be noted|Needless to say'
NOT_JUST_PATTERN='[Nn]ot just [a-zA-Z]+[,:]|isn'"'"'t just|[Ii]t'"'"'s not [a-zA-Z]+[,:.] [Ii]t'"'"'s'

# ANSI colors for terminal
if [[ -t 1 ]]; then
  RED=$'\033[0;31m'; YEL=$'\033[0;33m'; GRN=$'\033[0;32m'; CYA=$'\033[0;36m'; RST=$'\033[0m'
else
  RED=""; YEL=""; GRN=""; CYA=""; RST=""
fi

# ---------- Helpers ----------

strip_frontmatter() {
  # Emit file content minus frontmatter block and minus citation lists
  awk 'BEGIN{infm=0; incit=0}
    NR==1 && /^---$/ {infm=1; next}
    infm && /^---$/ {infm=0; next}
    infm {next}
    /^## Citation$/ {incit=1; print; next}
    /^## [^C]/ {incit=0}
    {print}' "$1"
}

check_file() {
  local f="$1"
  local fails=0
  local warns=0
  local body emdash lines per100 intens throat notjust

  if [[ ! -f "$f" ]]; then
    echo "${RED}FAIL${RST} file not found: $f"
    return 1
  fi

  body=$(strip_frontmatter "$f")
  lines=$(echo "$body" | wc -l | tr -d ' ')
  [[ $lines -eq 0 ]] && lines=1

  # --- Em-dash density ---
  emdash=$(echo "$body" | grep -o "—" | wc -l | tr -d ' ')
  per100=$(( emdash * 100 / lines ))
  if (( per100 > MAX_EMDASH_PER_100 )); then
    echo "${RED}FAIL${RST} em-dashes: $emdash in $lines lines ($per100/100, max $MAX_EMDASH_PER_100)"
    echo "       Fix: replace — with period, comma, or restructure."
    fails=$((fails + 1))
  fi

  # --- Intensifiers ---
  intens=$(echo "$body" | grep -cEi "\b($INTENSIFIER_WORDS)\b" || true)
  if (( intens > 0 )); then
    echo "${RED}FAIL${RST} intensifiers: $intens hits of [$INTENSIFIER_WORDS]"
    echo "$body" | grep -nEi "\b($INTENSIFIER_WORDS)\b" | head -5 | sed 's/^/       /'
    fails=$((fails + 1))
  fi

  # --- Throat-clear transitions ---
  throat=$(echo "$body" | grep -cE "$THROAT_CLEAR" || true)
  if (( throat > 0 )); then
    echo "${RED}FAIL${RST} AI throat-clear transitions: $throat hits"
    echo "$body" | grep -nE "$THROAT_CLEAR" | head -5 | sed 's/^/       /'
    fails=$((fails + 1))
  fi

  # --- "Not just X" / "It's not X, it's Y" pattern ---
  notjust=$(echo "$body" | grep -cE "$NOT_JUST_PATTERN" || true)
  if (( notjust > 0 )); then
    echo "${RED}FAIL${RST} rhetorical 'not just X' pattern: $notjust hits"
    echo "$body" | grep -nE "$NOT_JUST_PATTERN" | head -3 | sed 's/^/       /'
    fails=$((fails + 1))
  fi

  # --- Citation hygiene ---
  # DOI format
  local bad_dois
  bad_dois=$(grep -oE 'doi:[^ )"'"'"',<>]+' "$f" 2>/dev/null \
    | grep -vE 'doi:10\.[0-9]{4,9}/[^ "'"'"'<>]+' || true)
  if [[ -n "$bad_dois" ]]; then
    echo "${RED}FAIL${RST} malformed DOI strings:"
    echo "$bad_dois" | sed 's/^/       /'
    fails=$((fails + 1))
  fi

  # Vault wikilink existence (evidence only)
  local missing_slugs
  while IFS= read -r slug; do
    [[ -z "$slug" ]] && continue
    if [[ ! -f "$VAULT_DIR/evidence/${slug}.md" && ! -f "$VAULT_DIR/concepts/${slug}.md" && \
          ! -f "$VAULT_DIR/observations/${slug}.md" && ! -f "$VAULT_DIR/audiences/${slug}.md" ]]; then
      missing_slugs="${missing_slugs}${slug}\n"
    fi
  done < <(grep -oE '\[\[[a-z0-9][a-z0-9-]+\]\]' "$f" 2>/dev/null | tr -d '[]' | sort -u)
  if [[ -n "$missing_slugs" ]]; then
    echo "${RED}FAIL${RST} unresolved [[wikilinks]]:"
    printf "$missing_slugs" | sed 's/^/       /'
    fails=$((fails + 1))
  fi

  # Author-Year "Smith 2025" / "Smith et al., 2025" — flag for manual verification
  # Not a fail; just a count for awareness
  local ayear
  ayear=$(grep -oE '\b[A-Z][a-z]+(( et al\.?)|( and [A-Z][a-z]+)|)?,? \(?(19|20)[0-9]{2}\)?' "$f" 2>/dev/null | wc -l | tr -d ' ')
  if (( ayear > 0 )); then
    warns=$((warns + 1))
  fi

  if (( fails == 0 )); then
    if (( ayear > 0 )); then
      echo "${GRN}PASS${RST} $f (${ayear} author-year citations — manual verification needed before publish)"
    else
      echo "${GRN}PASS${RST} $f"
    fi
    return 0
  fi
  return 1
}

# ---------- Subcommand dispatch ----------

case "$MODE" in
  check)
    if [[ -z "$FILE" ]]; then
      echo "usage: $0 check <file.md>" >&2; exit 2
    fi
    check_file "$FILE"
    exit $?
    ;;

  citations)
    if [[ -z "$FILE" ]]; then
      echo "usage: $0 citations <file.md>" >&2; exit 2
    fi
    echo "${CYA}== Citations in $FILE ==${RST}"
    echo "--- DOIs ---"
    grep -oE '10\.[0-9]{4,9}/[^ )"'"'"'<>]+' "$FILE" 2>/dev/null | sort -u
    echo "--- Wikilinks ---"
    grep -oE '\[\[[a-z0-9][a-z0-9-]+\]\]' "$FILE" 2>/dev/null | sort -u
    echo "--- Author-Year mentions ---"
    grep -oE '\b[A-Z][a-z]+(( et al\.?)|( and [A-Z][a-z]+)|)?,? \(?(19|20)[0-9]{2}\)?' "$FILE" 2>/dev/null | sort -u | head -30
    ;;

  staged)
    # Pre-commit hook mode: check staged outputs/*.md
    staged=$(git -C "$VAULT_DIR" diff --cached --name-only --diff-filter=AM | grep -E '^outputs/.*\.md$' || true)
    if [[ -z "$staged" ]]; then
      exit 0
    fi
    echo "${CYA}== SRL Quality Gate (pre-commit) ==${RST}"
    overall=0
    while IFS= read -r f; do
      [[ -z "$f" ]] && continue
      check_file "$VAULT_DIR/$f" || overall=1
    done <<< "$staged"
    if (( overall == 1 )); then
      echo ""
      echo "${RED}Commit blocked.${RST} Fix the flagged issues above."
      echo "Emergency override: git commit --no-verify (use sparingly; sweep report will surface it)"
    fi
    exit $overall
    ;;

  sweep)
    REPORT="$VAULT_DIR/outputs/quality-sweep-report.md"
    TS=$(date '+%Y-%m-%d %H:%M')
    {
      echo "# Quality Sweep Report"
      echo ""
      echo "**Generated:** $TS"
      echo ""
      echo "Scan of all \`outputs/*.md\` against deterministic quality rules (em-dash density, intensifiers, throat-clear transitions, rhetorical patterns, citation hygiene). This report is advisory; commits are blocked by the pre-commit hook going forward."
      echo ""
      echo "## Summary"
      echo ""
    } > "$REPORT"
    total=0; passed=0; failed=0
    declare -a fail_files
    # Iterate — don't recurse into archive directories if any
    while IFS= read -r f; do
      total=$((total + 1))
      result=$(check_file "$f" 2>&1)
      if echo "$result" | grep -q "^${GRN}PASS"; then
        passed=$((passed + 1))
      else
        failed=$((failed + 1))
        fail_files+=("$f")
        {
          echo "### ${f#$VAULT_DIR/}"
          echo ""
          echo '```'
          echo "$result" | sed -E $'s/\033\\[[0-9;]*m//g'
          echo '```'
          echo ""
        } >> "$REPORT"
      fi
    done < <(find "$VAULT_DIR/outputs" -maxdepth 3 -name "*.md" -type f \
              -not -path "*/quality-sweep-report.md" \
              -not -path "*/citation-health-report.md" \
              -not -path "*/vault-write-log*" \
              -not -path "*/active-context.md" \
              -not -path "*/needs-review.md" \
              -not -path "*/review-dashboard.md" | sort)
    # Insert summary table near top
    SUM_FILE=$(mktemp)
    {
      head -n 8 "$REPORT"
      echo "| Metric | Count |"
      echo "|---|---|"
      echo "| Files scanned | $total |"
      echo "| Passed | $passed |"
      echo "| Flagged | $failed |"
      echo ""
      echo "## Files flagged (in scan order)"
      echo ""
      for ff in "${fail_files[@]}"; do
        echo "- ${ff#$VAULT_DIR/}"
      done
      echo ""
      echo "---"
      echo ""
      echo "## Per-file diagnostics"
      echo ""
      tail -n +9 "$REPORT"
    } > "$SUM_FILE"
    mv "$SUM_FILE" "$REPORT"
    echo ""
    echo "${CYA}== Sweep complete ==${RST}"
    echo "Scanned: $total | Passed: $passed | Flagged: $failed"
    echo "Report: $REPORT"
    # Sweep is advisory; exit 2 if anything flagged (signal, non-blocking)
    if (( failed > 0 )); then exit 2; fi
    exit 0
    ;;

  *)
    cat <<USAGE
SRL Quality Gate

Usage:
  $0 check <file.md>       Deterministic quality check of a single file
  $0 citations <file.md>   Extract citations (DOIs, wikilinks, author-year) from a file
  $0 staged                Pre-commit hook mode: check staged outputs/*.md
  $0 sweep                 Scan all outputs/, write outputs/quality-sweep-report.md

Rules:
  - Em-dash density ≤${MAX_EMDASH_PER_100} per 100 lines
  - Zero intensifiers ($INTENSIFIER_WORDS)
  - Zero AI throat-clear transitions
  - Zero "not just X" rhetorical pattern
  - Well-formed DOIs only
  - All [[wikilinks]] must resolve

Exit codes:
  0  pass
  1  fail (blocks pre-commit)
  2  warnings (sweep only)
USAGE
    exit 2
    ;;
esac
