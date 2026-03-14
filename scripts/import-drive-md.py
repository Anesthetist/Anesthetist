#!/usr/bin/env python3
"""
Import readable .md and .txt files from Google Drive into the vault.

Copies files from the somnistics Google Drive into sources/google-drive/
with proper chat-import or source frontmatter.

Usage:
    python3 scripts/import-drive-md.py [--dry-run]
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
DEST_DIR = VAULT_ROOT / "sources" / "google-drive"
GDRIVE = Path.home() / "Library/CloudStorage/GoogleDrive-randy@somnistics.com/My Drive"

# Also check memory folder
EXTRA_DIRS = [
    GDRIVE / "memory",
    GDRIVE / "MANUALLY COPIED",
    GDRIVE / "Clawdbot Artifacts",
    GDRIVE / "Clawdbot Files",
    GDRIVE / "Clawdbot Files (1)",
    GDRIVE / "SRL Strategy & Exec Briefs",
]


def slugify(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s[:80].strip('-')


def has_frontmatter(content: str) -> bool:
    return content.strip().startswith('---')


def wrap_with_frontmatter(content: str, filepath: Path) -> str:
    """Add vault frontmatter to a file that doesn't have it."""
    title = filepath.stem.replace('-', ' ').replace('_', ' ')
    stat = filepath.stat()
    modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')

    fm = f"""---
id: "urn:srl:source:gdrive-{slugify(filepath.stem)}"
type: source
title: "{title}"
status: draft
creator: "Randy Graybeal"
created: {modified}
imported: {datetime.now().strftime('%Y-%m-%d')}
dc:source: "google-drive:{filepath.relative_to(GDRIVE)}"
---

"""
    return fm + content


def main():
    dry_run = '--dry-run' in sys.argv
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all .md and .txt files
    sources = []

    # Top-level Drive files
    for f in GDRIVE.glob('*.md'):
        sources.append(f)
    for f in GDRIVE.glob('*.txt'):
        sources.append(f)

    # Extra directories
    for d in EXTRA_DIRS:
        if d.exists():
            for f in d.rglob('*.md'):
                sources.append(f)
            for f in d.rglob('*.txt'):
                sources.append(f)

    print(f"Found {len(sources)} readable files")

    imported = 0
    for src in sorted(sources):
        try:
            content = src.read_text(errors='replace')
        except Exception as e:
            print(f"  [SKIP] {src.name}: {e}")
            continue

        if not content.strip():
            continue

        # Add frontmatter if missing
        if not has_frontmatter(content):
            content = wrap_with_frontmatter(content, src)

        dest_name = src.name
        dest_path = DEST_DIR / dest_name

        counter = 1
        while dest_path.exists():
            counter += 1
            dest_path = DEST_DIR / f"{src.stem}-{counter}{src.suffix}"

        if dry_run:
            print(f"  [DRY RUN] {src.name} -> {dest_path.name}")
        else:
            dest_path.write_text(content)

        imported += 1

    print(f"\nDone: {imported} files imported")
    if not dry_run:
        print(f"Files written to: {DEST_DIR}")


if __name__ == '__main__':
    main()
