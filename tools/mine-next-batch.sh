#!/bin/bash
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
BATCH_SIZE="${1:-5}"
EFFORT="${EFFORT:-high}"
MODEL="${MODEL:-opus}"
TIMESTAMP=$(date +%Y-%m-%d_%H%M)

cd "$VAULT_DIR"

# Pull latest changes
git pull --rebase origin main 2>/dev/null || true

# Parse the priority queue for unmined files
# Extracts filenames from the markdown table, skipping already-mined entries
get_next_files() {
  local count=$1
  # Look for lines matching "| N | filename.md |" pattern in the queue
  # Skip lines containing "MINED" or "SKIP"
  grep -E '^\| [0-9]+ \|' "$QUEUE_FILE" 2>/dev/null \
    | grep -iv 'mined\|skip\|already' \
    | head -n "$count" \
    | sed 's/.*| *//' \
    | awk -F'|' '{print $1}' \
    | sed 's/ *$//' \
    | sed 's/^ *//'
}

# Get list of files already mined (from extraction reports)
get_mined_files() {
  grep -h "^\\*\\*Source:\\*\\*" "$VAULT_DIR/outputs/extractions/"*.md 2>/dev/null \
    | sed 's/.*chatgpt\///' \
    | sed 's/ *$//' \
    | sort -u
}

# Build the mining prompt for a batch of files
build_mining_prompt() {
  local files=("$@")
  local file_list=""
  local total_chars=0

  for f in "${files[@]}"; do
    local path="$VAULT_DIR/sources/chatgpt/$f"
    if [ -f "$path" ]; then
      local chars=$(wc -c < "$path")
      total_chars=$((total_chars + chars))
      file_list="$file_list\n- sources/chatgpt/$f ($chars chars)"
    fi
  done

  cat <<PROMPT
You are the SRL Knowledge Miner + Vault Writer pipeline. Process these ChatGPT transcripts in a single pass: extract Randy's voice, identify concepts/evidence/observations, check vault for duplicates, create notes via MCP tools, wire relationships, and commit.

## Files to process:
$(echo -e "$file_list")

## Protocol:
1. Read each file. Extract Randy's assertions, corrections, coined terms, clinical anecdotes.
2. For each extraction candidate, search the vault (mcp__srl-vault__search_vault) to check for duplicates.
3. Create high-confidence, Randy-originated concepts via mcp__srl-vault__create_note.
4. Create evidence notes for clearly cited books/papers.
5. Create observations for clinical craft knowledge.
6. Wire SKOS relationships and evidence links.
7. Write an extraction report to outputs/extractions/{slug}-extraction.md
8. Append all actions to outputs/vault-write-log.md

## Rules:
- status: draft, creator: randy
- clinical_interpretation: "Pending review"
- Prioritize Randy's words over ChatGPT's elaborations
- Only vault SRL-original or core scientific concepts
- Never write vault files directly — use MCP tools only
- At the end, output a summary of what was created

## Timestamp: $TIMESTAMP
PROMPT
}

echo "=== SRL Mining Pipeline — $TIMESTAMP ==="
echo "Batch size: $BATCH_SIZE | Effort: $EFFORT | Model: $MODEL"

# Get next files from queue
mapfile -t NEXT_FILES < <(get_next_files "$BATCH_SIZE")

if [ ${#NEXT_FILES[@]} -eq 0 ]; then
  echo "No unmined files in priority queue. Pipeline complete."
  exit 0
fi

echo "Files to mine:"
for f in "${NEXT_FILES[@]}"; do
  echo "  - $f"
done

# Build and execute the mining prompt
PROMPT=$(build_mining_prompt "${NEXT_FILES[@]}")

echo ""
echo "Running Claude mining pipeline..."
echo "$PROMPT" | claude \
  -p \
  --model "$MODEL" \
  --effort "$EFFORT" \
  --permission-mode auto \
  --append-system-prompt "You are Vigil, the SRL vault orchestrator. Read CLAUDE.md for full context." \
  2>&1 | tee "$VAULT_DIR/outputs/pipeline-logs/mine-$TIMESTAMP.log"

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
