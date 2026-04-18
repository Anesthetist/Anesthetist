#!/usr/bin/env zsh
# Install/reinstall the vault quality-sweep LaunchAgent.
# Idempotent — safe to re-run.

set -e
PLIST_NAME="com.somnistics.vault-quality-sweep.plist"
SRC="$(cd "$(dirname "$0")" && pwd)/$PLIST_NAME"
DEST="$HOME/Library/LaunchAgents/$PLIST_NAME"

mkdir -p "$HOME/Library/LaunchAgents"
cp "$SRC" "$DEST"

launchctl unload "$DEST" 2>/dev/null || true
launchctl load "$DEST"

echo "Loaded: $DEST"
launchctl list | grep somnistics || echo "(warning: agent not visible in launchctl list)"
echo ""
echo "Next scheduled run: 06:30 daily"
echo "Manual run: ./tools/quality-gate.sh sweep"
echo "Uninstall:  launchctl unload $DEST && rm $DEST"
