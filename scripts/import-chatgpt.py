#!/usr/bin/env python3
"""
Import ChatGPT conversation exports into the SRL Knowledge Vault.

Reads conversations-*.json from the ChatGPT Migration folder,
filters for SRL-relevant conversations, and produces markdown
chat-import notes with proper frontmatter.

Usage:
    python3 scripts/import-chatgpt.py [--all] [--dry-run]

    --all     Import all conversations (not just SRL-relevant)
    --dry-run Print what would be created without writing files
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = VAULT_ROOT / "sources" / "chatgpt"
GDRIVE_BASE = Path.home() / "Library/CloudStorage/GoogleDrive-randy@somnistics.com/My Drive/Chatgpt Migration files"

SRL_KEYWORDS = [
    'somnist', 'pausality', 'crna', 'anesthes', 'breathing', 'vagal',
    'polyvagal', 'hrv', 'biofeedback', 'interocept', 'neurominute',
    'gap moment', 'kosha', 'mindful', 'nervous system', 'wellness',
    'resilience', 'burnout', 'stress manage', 'clinical', 'titration',
    'eeg', 'muse', 'neuro', 'blip', 'breathwork', 'autonomic',
    'glossary', 'novel concept', 'patent', 'investor', 'enterprise',
    'mayo', 'fascia', 'intubat', 'meditation', 'coherence', 'vagalbeats',
    'anterocept', 'polyanchora', 'neurogating', 'ouroboros',
    'interoceptiv', 'hemispher', 'relevance realiz', 'self-remember',
    'minimum effective', 'category theory', 'seven powers', '7 powers',
    'state transition', 'apple watch', 'polar h10', 'ceu', 'aana',
]


def slugify(title: str) -> str:
    """Convert title to kebab-case slug."""
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s[:80].strip('-')


def extract_messages(conversation: dict) -> list[dict]:
    """Walk the conversation tree and extract messages in order."""
    mapping = conversation.get('mapping', {})

    # Build parent->children map and find root
    children_map = {}
    root_id = None
    for node_id, node in mapping.items():
        parent = node.get('parent')
        if parent is None:
            root_id = node_id
        else:
            children_map.setdefault(parent, []).append(node_id)

    # Walk tree depth-first following the "current path"
    messages = []
    current = conversation.get('current_node')

    # Build path from current_node back to root
    path = []
    visited = set()
    node_id = current
    while node_id and node_id not in visited:
        visited.add(node_id)
        path.append(node_id)
        node = mapping.get(node_id, {})
        node_id = node.get('parent')
    path.reverse()

    for nid in path:
        node = mapping.get(nid, {})
        msg = node.get('message')
        if not msg:
            continue
        content = msg.get('content', {})
        parts = content.get('parts', [])
        role = msg.get('author', {}).get('role', 'unknown')

        text_parts = []
        for part in parts:
            if isinstance(part, str) and part.strip():
                text_parts.append(part)

        if text_parts and role in ('user', 'assistant', 'system'):
            messages.append({
                'role': role,
                'text': '\n'.join(text_parts),
                'timestamp': msg.get('create_time'),
            })

    return messages


def is_relevant(conversation: dict, messages: list[dict]) -> bool:
    """Check if conversation is SRL-relevant by title + content sampling."""
    title = (conversation.get('title') or '').lower()
    if any(kw in title for kw in SRL_KEYWORDS):
        return True

    # Sample first few messages for keywords
    sample_text = ' '.join(m['text'][:500].lower() for m in messages[:6])
    matches = sum(1 for kw in SRL_KEYWORDS if kw in sample_text)
    return matches >= 2


def format_note(conversation: dict, messages: list[dict]) -> str:
    """Format a conversation as a vault chat-import note."""
    title = conversation.get('title') or 'Untitled Conversation'
    conv_id = conversation.get('id', conversation.get('conversation_id', 'unknown'))
    create_time = conversation.get('create_time', 0)
    created = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d') if create_time else '2024-01-01'
    slug = slugify(title)

    # Count tokens roughly
    total_chars = sum(len(m['text']) for m in messages)

    escaped_title = title.replace('"', '\\"')
    today = datetime.now().strftime('%Y-%m-%d')
    msg_count = len(messages)

    frontmatter = f"""---
id: "urn:srl:chat:chatgpt-{slug}"
type: chat-import
title: "{escaped_title}"
status: draft
created: {created}
imported: {today}
platform: chatgpt
dc:source: "chatgpt-export:{conv_id}"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: {msg_count}
char_count: {total_chars}
---"""

    body = f"\n# {title}\n\n"
    body += f"**Date:** {created} | **Messages:** {len(messages)} | **~{total_chars // 4} tokens**\n\n"
    body += "## Key Takeaways\n\n- *Pending extraction*\n\n"
    body += "## Extracted Nodes\n\n- *Pending extraction*\n\n"
    body += "---\n\n## Transcript\n\n"

    for msg in messages:
        role = msg['role']
        if role == 'system':
            continue
        label = '**Randy:**' if role == 'user' else '**ChatGPT:**'
        text = msg['text']
        # Truncate very long messages for readability
        if len(text) > 3000:
            text = text[:3000] + '\n\n*[message truncated — full text in source]*'
        body += f"{label}\n\n{text}\n\n---\n\n"

    return frontmatter + body


def main():
    dry_run = '--dry-run' in sys.argv
    import_all = '--all' in sys.argv

    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    json_files = sorted(GDRIVE_BASE.glob('conversations-*.json'))
    if not json_files:
        print(f"No conversation files found in {GDRIVE_BASE}")
        sys.exit(1)

    total = 0
    imported = 0
    skipped = 0

    for json_file in json_files:
        with open(json_file) as f:
            conversations = json.load(f)

        for conv in conversations:
            total += 1
            title = conv.get('title') or 'Untitled'
            messages = extract_messages(conv)

            if not messages:
                skipped += 1
                continue

            if not import_all and not is_relevant(conv, messages):
                skipped += 1
                continue

            slug = slugify(title)
            if not slug:
                slug = f"untitled-{total}"

            filename = f"{slug}.md"
            filepath = SOURCES_DIR / filename

            # Handle duplicates
            counter = 1
            while filepath.exists():
                counter += 1
                filepath = SOURCES_DIR / f"{slug}-{counter}.md"

            note_content = format_note(conv, messages)

            if dry_run:
                print(f"  [DRY RUN] {filepath.name} ({len(messages)} msgs)")
            else:
                filepath.write_text(note_content)

            imported += 1

    print(f"\nDone: {imported} imported, {skipped} skipped, {total} total")
    if not dry_run:
        print(f"Files written to: {SOURCES_DIR}")


if __name__ == '__main__':
    main()
