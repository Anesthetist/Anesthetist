"""
MCP server for querying OpenEvidence clinical AI platform.
Provides 4 tools: ask, article_get, history, auth_status.
"""

import json
import asyncio
import sys
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Ensure client module is importable
sys.path.insert(0, str(Path(__file__).parent))
import client

app = Server("openevidence")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="oe_auth_status",
            description="Check OpenEvidence authentication status. Returns user info if connected, or instructions to re-login if session expired.",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="oe_ask",
            description=(
                "Submit a clinical question to OpenEvidence and get an evidence-backed answer "
                "with citations from NEJM, JAMA, Cochrane, NCCN, and other authoritative sources. "
                "Supports follow-up questions via original_article_id."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "Clinical question (3-6000 characters)",
                    },
                    "original_article_id": {
                        "type": "string",
                        "description": "Article ID for follow-up questions (optional)",
                    },
                    "wait_for_completion": {
                        "type": "boolean",
                        "description": "Wait for the full answer (default: true)",
                        "default": True,
                    },
                    "timeout_sec": {
                        "type": "integer",
                        "description": "Max seconds to wait for answer (default: 120)",
                        "default": 120,
                    },
                },
                "required": ["question"],
            },
        ),
        Tool(
            name="oe_article_get",
            description="Fetch a complete OpenEvidence article/answer by its ID. Returns the full answer text and metadata.",
            inputSchema={
                "type": "object",
                "properties": {
                    "article_id": {
                        "type": "string",
                        "description": "Article UUID",
                    },
                },
                "required": ["article_id"],
            },
        ),
        Tool(
            name="oe_history",
            description="List past OpenEvidence queries and articles. Supports pagination and search.",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "Max results (1-100, default: 20)",
                        "default": 20,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Pagination offset (default: 0)",
                        "default": 0,
                    },
                    "search": {
                        "type": "string",
                        "description": "Search query to filter results",
                    },
                },
                "required": [],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        if name == "oe_auth_status":
            result = await client.auth_status()

        elif name == "oe_ask":
            result = await client.ask(
                arguments["question"],
                original_article_id=arguments.get("original_article_id"),
                wait=arguments.get("wait_for_completion", True),
                timeout_sec=arguments.get("timeout_sec", 120),
            )

        elif name == "oe_article_get":
            result = await client.article_get(arguments["article_id"])

        elif name == "oe_history":
            result = await client.history(
                limit=arguments.get("limit", 20),
                offset=arguments.get("offset", 0),
                search=arguments.get("search", ""),
            )

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

        # Strip raw article data to keep responses manageable
        if isinstance(result, dict) and "raw" in result:
            raw = result.pop("raw")
            # Keep question for context
            question = raw.get("inputs", {}).get("question")
            if question:
                result["question"] = question

        return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]

    except FileNotFoundError as e:
        return [TextContent(type="text", text=str(e))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {type(e).__name__}: {e}")]


async def main():
    cookie_exists = client.COOKIE_PATH.exists()
    status = "cookies found" if cookie_exists else "NO COOKIES — run auth.py first"
    print(f"OpenEvidence MCP loaded: {status}", file=sys.stderr)

    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
