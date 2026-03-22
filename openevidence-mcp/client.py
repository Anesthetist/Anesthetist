"""
Lightweight HTTP client for the OpenEvidence internal API.
Uses httpx with persisted browser cookies — no Playwright at runtime.
"""

import json
import asyncio
from pathlib import Path

import httpx

BASE_URL = "https://www.openevidence.com"
COOKIE_PATH = Path.home() / ".openevidence-mcp" / "cookies.json"

# Statuses that mean the article is still being generated
PENDING_STATUSES = {"queued", "pending", "processing", "running", "in_progress"}


def load_cookies() -> dict[str, str]:
    """Load cookies from the persisted cookie file."""
    if not COOKIE_PATH.exists():
        raise FileNotFoundError(
            f"No cookies found at {COOKIE_PATH}. "
            "Run 'python openevidence-mcp/auth.py' to log in."
        )
    data = json.loads(COOKIE_PATH.read_text())
    # Support both formats: list-of-dicts (Playwright) or simple dict
    if isinstance(data, list):
        return {c["name"]: c["value"] for c in data}
    return data


def _build_client() -> httpx.AsyncClient:
    """Create an httpx client with stored cookies."""
    cookies = load_cookies()
    return httpx.AsyncClient(
        base_url=BASE_URL,
        cookies=cookies,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "SRL-Vigil/1.0",
        },
        timeout=30.0,
        follow_redirects=True,
    )


async def auth_status() -> dict:
    """Check authentication status. Returns user info or error."""
    async with _build_client() as client:
        resp = await client.get("/api/auth/me")
        if resp.status_code == 401:
            return {"authenticated": False, "error": "Session expired. Run 'python openevidence-mcp/auth.py' to re-login."}
        resp.raise_for_status()
        user = resp.json()
        return {"authenticated": True, "user": user}


async def ask(
    question: str,
    *,
    original_article_id: str | None = None,
    wait: bool = True,
    timeout_sec: int = 120,
    poll_interval_sec: float = 1.5,
) -> dict:
    """Submit a clinical question and optionally wait for the answer."""
    payload = {
        "article_type": "Ask OpenEvidence Light with citations",
        "inputs": {
            "variant_configuration_file": "prod",
            "attachments": [],
            "question": question,
            "use_gatekeeper": True,
        },
        "personalization_enabled": False,
        "disable_caching": False,
    }
    if original_article_id:
        payload["original_article_id"] = original_article_id

    async with _build_client() as client:
        resp = await client.post("/api/article", json=payload)
        if resp.status_code == 401:
            return {"error": "Session expired. Run 'python openevidence-mcp/auth.py' to re-login."}
        resp.raise_for_status()
        article = resp.json()

        if not wait:
            return article

        # Poll until complete
        article_id = article.get("id") or article.get("_id")
        elapsed = 0.0
        while elapsed < timeout_sec:
            await asyncio.sleep(poll_interval_sec)
            elapsed += poll_interval_sec

            poll_resp = await client.get(f"/api/article/{article_id}")
            poll_resp.raise_for_status()
            article = poll_resp.json()

            status = (article.get("status") or "").lower()
            if status not in PENDING_STATUSES:
                break

        return {
            "article_id": article_id,
            "status": article.get("status"),
            "answer": _extract_answer(article),
            "raw": article,
        }


async def article_get(article_id: str) -> dict:
    """Fetch a complete article by ID."""
    async with _build_client() as client:
        resp = await client.get(f"/api/article/{article_id}")
        if resp.status_code == 401:
            return {"error": "Session expired. Run 'python openevidence-mcp/auth.py' to re-login."}
        resp.raise_for_status()
        article = resp.json()
        return {
            "article_id": article_id,
            "status": article.get("status"),
            "answer": _extract_answer(article),
            "raw": article,
        }


async def history(limit: int = 20, offset: int = 0, search: str = "") -> dict:
    """List past queries/articles."""
    params = {"limit": limit, "offset": offset}
    if search:
        params["search"] = search

    async with _build_client() as client:
        resp = await client.get("/api/article/list", params=params)
        if resp.status_code == 401:
            return {"error": "Session expired. Run 'python openevidence-mcp/auth.py' to re-login."}
        resp.raise_for_status()
        return resp.json()


def _extract_answer(article: dict) -> str | None:
    """Extract the answer text from an article's nested structure."""
    try:
        inputs = article.get("inputs", {})
        hist = inputs.get("history", [])
        if hist:
            return hist[-1].get("outputText")
    except (KeyError, IndexError, TypeError):
        pass
    return None
