# Somnistics Research Labs — Library Graph

An Obsidian vault serving as a living library connecting research, AI conversations, and organizational knowledge.

## Vault Structure

- **Inbox/** — Drop zone for unsorted imports and new captures
- **Sources/** — Raw or lightly edited material organized by origin
  - `Google-Drive/` — Files synced/imported from Google Drive
  - `Google-Docs/` — Exported Google Docs
  - `ChatGPT/` — Exported ChatGPT conversations
  - `Claude/` — Claude conversation exports and artifacts
  - `Claude-Coworker/` — Claude Code session outputs and artifacts
- **Nodes/** — Atomic notes: one concept per file, richly linked
- **Maps/** — Maps of Content (MOCs) that organize nodes by theme or project
- **Templates/** — Note templates for consistent structure
- **Assets/** — Images, PDFs, and other attachments

## Conventions

- Use `[[wikilinks]]` for internal links between notes
- Tag notes with YAML frontmatter: `source`, `type`, `created`, `tags`
- Node filenames: lowercase-kebab-case (e.g., `interoceptive-coupling.md`)
- Source filenames: preserve original name where possible
- Prefer linking over duplicating content

## AI Agent Workflow

- Claude Code operates from this directory as the working root
- Changes are committed to git and synced to GitHub
- Obsidian reads the same directory for graph visualization and editing
- The graph is the shared state between human editing (Obsidian) and AI processing (Claude)
