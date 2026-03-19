#!/usr/bin/env zsh
# SRL Knowledge Mining Pipeline — Automated Batch Processor
# Reads the priority queue, mines the next N files, vault-writes results, commits.
#
# Usage:
#   ./tools/mine-next-batch.sh              # Mine next 5 files (default)
#   ./tools/mine-next-batch.sh 10           # Mine next 10 files
#   EFFORT=max ./tools/mine-next-batch.sh   # Use max effort level
#
# Designed to run via launchd/cron on Mac Mini, or manually.
# Requires: claude CLI, git, vault MCP server running

set -euo pipefail

VAULT_DIR="/Users/somnisticshq/Documents/Somnistics/Library-Graph"
QUEUE_FILE="$VAULT_DIR/outputs/mining-priority-queue.md"
PROGRESS_FILE="$VAULT_DIR/_bots/extraction-coordinator/progress.md"
LOG_FILE="$VAULT_DIR/outputs/vault-write-log.md"
BATCH_SIZE="${1:-3}"
MAX_CHARS="${MAX_CHARS:-200000}"  # Max total chars per batch (200K default)
EFFORT="${EFFORT:-high}"
MODEL="${MODEL:-opus}"
TIMESTAMP=$(date +%Y-%m-%d_%H%M)

cd "$VAULT_DIR"

# Pull latest changes
git pull --rebase origin main 2>/dev/null || true

# Parse the priority queue for unmined files
# Get list of files already mined (from the "Fully extracted" section of the queue)
get_mined_files() {
  # Extract the comma-separated list from the "Fully extracted" line onwards
  sed -n '/^### Fully extracted/,/^$/p' "$QUEUE_FILE" 2>/dev/null \
    | grep -v '^#' \
    | tr ',' '\n' \
    | sed 's/^ *//' \
    | sed 's/ *$//' \
    | grep '\.md$'
}

# Extracts filenames from the markdown table, skipping already-mined entries
get_next_files() {
  local count=$1
  local mined_file=$(mktemp)
  get_mined_files > "$mined_file"

  # Extract column 2 (filename) from table rows like "| 1 | filename.md | ..."
  grep -E '^\| [0-9]+ \|' "$QUEUE_FILE" 2>/dev/null \
    | awk -F'|' '{gsub(/^ +| +$/, "", $3); print $3}' \
    | while read -r fname; do
        # Skip if already mined
        if ! grep -qF "$fname" "$mined_file" 2>/dev/null; then
          echo "$fname"
        fi
      done \
    | head -n "$count"

  rm -f "$mined_file"
}

# Build the mining prompt for a batch of files
build_mining_prompt() {
  echo "You are the SRL Knowledge Miner + Vault Writer pipeline. Process these ChatGPT transcripts: extract Randy's voice, identify concepts/evidence/observations, check vault for duplicates, create notes via MCP tools, wire relationships."
  echo ""
  echo "## Files to process:"
  for f in "$@"; do
    local fpath="$VAULT_DIR/sources/chatgpt/$f"
    if [ -f "$fpath" ]; then
      echo "- sources/chatgpt/$f ($(wc -c < "$fpath" | tr -d ' ') chars)"
    fi
  done
  echo ""
  echo "## Protocol:"
  echo "1. Read each file. Extract Randy's assertions, corrections, coined terms, clinical anecdotes."
  echo "2. Search vault (mcp__srl-vault__search_vault) to check for duplicates before creating."
  echo "3. Create high-confidence Randy-originated concepts via mcp__srl-vault__create_note."
  echo "4. Create evidence notes for clearly cited books/papers."
  echo "5. Create observations for clinical craft knowledge."
  echo "6. Wire SKOS relationships and evidence links."
  echo "7. Write extraction report to outputs/extractions/{slug}-extraction.md"
  echo "8. Append actions to outputs/vault-write-log.md"
  echo ""
  echo "## Rules:"
  echo "- status: draft, creator: randy, clinical_interpretation: Pending review"
  echo "- Prioritize Randy's words over ChatGPT elaborations"
  echo "- Only vault SRL-original or core scientific concepts"
  echo "- Use MCP tools only — never write vault files directly"
  echo "- Output a summary of what was created"
}

echo "=== SRL Mining Pipeline — $TIMESTAMP ==="
echo "Batch size: $BATCH_SIZE | Effort: $EFFORT | Model: $MODEL"

# Get next files from queue, respecting both count and size limits
ALL_CANDIDATES=("${(@f)$(get_next_files 20)}")  # Get up to 20 candidates

if [ ${#ALL_CANDIDATES[@]} -eq 0 ] || [ -z "${ALL_CANDIDATES[1]}" ]; then
  echo "No unmined files in priority queue. Pipeline complete."
  exit 0
fi

# Filter by size limit and batch count
NEXT_FILES=()
total_batch_chars=0
for f in "${ALL_CANDIDATES[@]}"; do
  [ -z "$f" ] && continue
  fpath="$VAULT_DIR/sources/chatgpt/$f"
  [ ! -f "$fpath" ] && continue
  fchars=$(wc -c < "$fpath" | tr -d ' ')
  if (( total_batch_chars + fchars > MAX_CHARS && ${#NEXT_FILES[@]} > 0 )); then
    break
  fi
  NEXT_FILES+=("$f")
  total_batch_chars=$((total_batch_chars + fchars))
  (( ${#NEXT_FILES[@]} >= BATCH_SIZE )) && break
done

echo "Files to mine (${#NEXT_FILES[@]} files, ~$((total_batch_chars / 1024))K chars):"
for f in "${NEXT_FILES[@]}"; do
  echo "  - $f"
done

# Build the mining prompt and write to file
PROMPT_FILE="$VAULT_DIR/outputs/pipeline-logs/prompt-$TIMESTAMP.md"
build_mining_prompt "${NEXT_FILES[@]}" > "$PROMPT_FILE"

echo ""
echo "Running Claude mining pipeline..."
echo "Prompt saved to: $PROMPT_FILE"

# Pass prompt file path — Claude reads the file itself
claude \
  -p \
  --model "$MODEL" \
  --effort "$EFFORT" \
  "Read the mining prompt at $PROMPT_FILE and execute it. Process the listed ChatGPT transcript files, extract knowledge, create vault notes via MCP tools, wire relationships, and write an extraction report." \
  > "$VAULT_DIR/outputs/pipeline-logs/mine-$TIMESTAMP.log" 2>&1

CLAUDE_EXIT=$?
cat "$VAULT_DIR/outputs/pipeline-logs/mine-$TIMESTAMP.log"

if [ $CLAUDE_EXIT -ne 0 ]; then
  echo "ERROR: Claude exited with code $CLAUDE_EXIT"
  exit $CLAUDE_EXIT
fi

# Commit results
echo ""
echo "Committing results..."
git add concepts/ evidence/ observations/ outputs/ _bots/
git commit -m "$(cat <<EOF
Extract: Automated pipeline batch — $TIMESTAMP

Details:
- Batch size: $BATCH_SIZE files
- Files: $(printf '%s, ' "${NEXT_FILES[@]}" | sed 's/, $//')
- Sources: Automated mining pipeline

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)" || echo "Nothing to commit"

# Push if configured
if [ "${PUSH:-false}" = "true" ]; then
  git push origin main
fi

echo ""
echo "=== Pipeline complete — $TIMESTAMP ==="
