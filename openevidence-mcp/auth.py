"""
One-time browser login for OpenEvidence.
Launches a browser, user logs in, cookies are saved for the MCP server.

Usage:
    python openevidence-mcp/auth.py
"""

import json
import sys
from pathlib import Path

COOKIE_DIR = Path.home() / ".openevidence-mcp"
COOKIE_PATH = COOKIE_DIR / "cookies.json"
BROWSER_PROFILE = COOKIE_DIR / "browser-profile"


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright not installed. Run:")
        print("  pip install playwright && playwright install chromium")
        sys.exit(1)

    COOKIE_DIR.mkdir(parents=True, exist_ok=True)

    print("Opening browser — log into OpenEvidence...")
    print("After login completes, return here and press Enter.\n")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            str(BROWSER_PROFILE),
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://www.openevidence.com/login")

        input("Press Enter after you've logged in successfully...")

        # Extract cookies
        cookies = context.cookies()
        oe_cookies = [c for c in cookies if "openevidence" in c.get("domain", "")]

        if not oe_cookies:
            print("Warning: No OpenEvidence cookies found. Login may have failed.")
            print("Saving all cookies as fallback...")
            oe_cookies = cookies

        # Save as simple name:value dict for httpx
        cookie_dict = {c["name"]: c["value"] for c in oe_cookies}
        COOKIE_PATH.write_text(json.dumps(cookie_dict, indent=2))
        print(f"\nSaved {len(cookie_dict)} cookies to {COOKIE_PATH}")

        # Also save full Playwright format for debugging
        full_path = COOKIE_DIR / "cookies-full.json"
        full_path.write_text(json.dumps(oe_cookies, indent=2))

        context.close()

    # Quick verification
    print("\nVerifying authentication...")
    import asyncio
    sys.path.insert(0, str(Path(__file__).parent))
    from client import auth_status

    result = asyncio.run(auth_status())
    if result.get("authenticated"):
        print("Authenticated successfully!")
    else:
        print(f"Auth check failed: {result.get('error', 'unknown error')}")
        print("Cookies were saved — the API endpoint may differ. Try using the tools.")


if __name__ == "__main__":
    main()
