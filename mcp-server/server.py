"""
MCP server for the Somnistics Research Labs knowledge vault.
Provides 9 tools for querying concepts, evidence, observations, and audiences.
"""

import json
import os
import asyncio
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from vault import VaultIndex, NoteRecord

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", Path(__file__).parent.parent))

app = Server("srl-vault")
vault = VaultIndex(VAULT_ROOT)


def note_summary(note: NoteRecord) -> dict:
    """Compact summary of a note for list views."""
    return {
        "slug": note.slug,
        "title": note.title,
        "type": note.type,
        "status": note.status,
        "id": note.id,
    }


def note_full(note: NoteRecord) -> str:
    """Full note content as markdown with frontmatter."""
    meta_lines = []
    for k, v in note.metadata.items():
        meta_lines.append(f"{k}: {json.dumps(v) if isinstance(v, (list, dict)) else v}")
    frontmatter = "\n".join(meta_lines)
    return f"---\n{frontmatter}\n---\n\n{note.body}"


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="list_concepts",
            description="List all concept notes in the SRL knowledge vault with their title, status, and ID",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="get_note",
            description="Get a single note's full metadata and body content by slug or URN ID. Works for any note type (concept, evidence, observation, audience).",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Note slug (e.g. 'interoception') or full URN (e.g. 'urn:srl:concept:interoception')",
                    }
                },
                "required": ["id"],
            },
        ),
        Tool(
            name="get_evidence_chain",
            description="Get the evidence chain for a concept — traces prov:wasDerivedFrom links recursively to find all supporting evidence and observations",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {"type": "string", "description": "Concept slug or URN"},
                },
                "required": ["id"],
            },
        ),
        Tool(
            name="get_relationships",
            description="Get SKOS relationships (broader, narrower, related) for a concept with resolved titles",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {"type": "string", "description": "Concept slug or URN"},
                },
                "required": ["id"],
            },
        ),
        Tool(
            name="search_by_subject",
            description="Find all notes tagged with a given dc:subject tag (e.g. 'autonomic-regulation', 'breathwork', 'polyvagal')",
            inputSchema={
                "type": "object",
                "properties": {
                    "subject": {"type": "string", "description": "Subject tag to search for"},
                },
                "required": ["subject"],
            },
        ),
        Tool(
            name="search_by_type",
            description="Find all notes of a given type: concept, evidence, observation, audience, or output",
            inputSchema={
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "Note type",
                        "enum": ["concept", "evidence", "observation", "audience", "output"],
                    },
                },
                "required": ["type"],
            },
        ),
        Tool(
            name="search_by_status",
            description="Find all notes at a given quality gate: draft, review, or canonical",
            inputSchema={
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "description": "Quality gate status",
                        "enum": ["draft", "review", "canonical"],
                    },
                },
                "required": ["status"],
            },
        ),
        Tool(
            name="get_audience_concepts",
            description="Get all concepts linked from an audience profile (e.g. 'crna', 'investor', 'corporate-executive')",
            inputSchema={
                "type": "object",
                "properties": {
                    "audience_id": {"type": "string", "description": "Audience slug"},
                },
                "required": ["audience_id"],
            },
        ),
        Tool(
            name="search_vault",
            description="Full-text search across all note titles, bodies, and subject tags. Returns matching notes.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query string"},
                },
                "required": ["query"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    vault.refresh_if_needed()

    if name == "list_concepts":
        concepts = vault.get_by_type("concept")
        result = [note_summary(n) for n in concepts]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "get_note":
        note = vault.get_note(arguments["id"])
        if not note:
            return [TextContent(type="text", text=f"Note not found: {arguments['id']}")]
        return [TextContent(type="text", text=note_full(note))]

    elif name == "get_evidence_chain":
        chain = vault.get_evidence_chain(arguments["id"])
        if not chain:
            note = vault.get_note(arguments["id"])
            if not note:
                return [TextContent(type="text", text=f"Note not found: {arguments['id']}")]
            return [TextContent(type="text", text="No evidence chain found for this note.")]
        result = [{"slug": n.slug, "title": n.title, "type": n.type, "id": n.id} for n in chain]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "get_relationships":
        rels = vault.get_relationships(arguments["id"])
        if not any(rels.values()):
            note = vault.get_note(arguments["id"])
            if not note:
                return [TextContent(type="text", text=f"Note not found: {arguments['id']}")]
        return [TextContent(type="text", text=json.dumps(rels, indent=2))]

    elif name == "search_by_subject":
        notes = vault.get_by_subject(arguments["subject"])
        result = [note_summary(n) for n in notes]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "search_by_type":
        notes = vault.get_by_type(arguments["type"])
        result = [note_summary(n) for n in notes]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "search_by_status":
        notes = vault.get_by_status(arguments["status"])
        result = [note_summary(n) for n in notes]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "get_audience_concepts":
        concepts = vault.get_audience_concepts(arguments["audience_id"])
        if not concepts:
            note = vault.get_note(arguments["audience_id"])
            if not note:
                return [TextContent(type="text", text=f"Audience not found: {arguments['audience_id']}")]
            return [TextContent(type="text", text="No concept links found in this audience profile.")]
        result = [note_summary(n) for n in concepts]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "search_vault":
        notes = vault.search(arguments["query"])
        result = [note_summary(n) for n in notes]
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    vault.load()
    note_count = len(vault.notes_by_slug)
    type_counts = {t: len(notes) for t, notes in vault.notes_by_type.items()}
    import sys
    print(f"SRL Vault MCP loaded: {note_count} notes {type_counts}", file=sys.stderr)

    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
