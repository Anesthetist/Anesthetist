# Welcome to Somnistics Research Labs

## How We Use Claude

Based on Randy Graybeal's usage over the last 30 days:

Work Type Breakdown:
  Build Feature   ██████░░░░░░░░░░░░░░  30%
  Analyze Data    ██████░░░░░░░░░░░░░░  28%
  Plan Design     ████░░░░░░░░░░░░░░░░  20%
  Write Docs      ███░░░░░░░░░░░░░░░░░  13%
  Improve Quality ██░░░░░░░░░░░░░░░░░░   9%

Top Skills & Commands:
  /clear            ██████░░░░░░░░░░░░░░  6x/month
  /exit             █████░░░░░░░░░░░░░░░  5x/month
  /mcp              ███░░░░░░░░░░░░░░░░░  3x/month
  /write-chapter    ███░░░░░░░░░░░░░░░░░  3x/month
  /biomedical       █░░░░░░░░░░░░░░░░░░░  1x/month
  /plan-ceo-review  █░░░░░░░░░░░░░░░░░░░  1x/month

Top MCP Servers:
  srl-vault      ████████████████████  468 calls
  PubMed         ████████████████░░░░  364 calls
  Gmail          █░░░░░░░░░░░░░░░░░░░    2 calls
  OpenEvidence   █░░░░░░░░░░░░░░░░░░░    1 call

## Your Setup Checklist

### Codebases
- [ ] Library-Graph — github.com/anesthetist/anesthetist (the knowledge vault — concepts, evidence, observations, outputs)

### MCP Servers to Activate
- [ ] **srl-vault** — CRUD and search across the Obsidian knowledge vault (concepts, evidence, graph queries). Local MCP server; runs from the repo. Check `_bots/` and CLAUDE.md for setup.
- [ ] **PubMed** — Search biomedical literature, fetch article metadata, find related studies. Claude.ai built-in; available automatically.
- [ ] **Gmail** — Send and read email from within Claude sessions. Claude.ai built-in; requires OAuth on first use (`/mcp` to connect).
- [ ] **OpenEvidence** — Ask clinical questions backed by NEJM, JAMA, Cochrane citations. Claude.ai built-in; requires OAuth on first use.
- [ ] **HubSpot** — CRM access for contacts and deals. Claude.ai built-in; requires OAuth on first use.
- [ ] **Google Calendar** — Schedule and view calendar events. Claude.ai built-in; requires OAuth on first use.
- [ ] **Google Drive** — Access shared Drive files. Claude.ai built-in; requires OAuth on first use.

### Skills to Know About

**Clinical & Research (the vault)**
- `/write-chapter` — Drafts book chapters from vault evidence in Randy's voice. The vault writes the book; you curate it.
- `/biomedical` — Queries biomedical LLMs (BioMistral, Med42) for mechanism explanations when PubMed alone isn't enough.
- `/review-queue` — Generates a web GUI for items needing Randy's decision: clinical interpretations, status promotions, extraction candidates. Clears the bottleneck.

**Quality & Review**
- `/review` — Pre-landing diff review. Run before every push. Catches citation errors, schema violations, clinical over-claims.
- `/health` — Code quality dashboard across the vault. 1,040+ notes drift fast. Run weekly.
- `/qa` — Full QA pass on any HTML output (landing pages, research packages, GUIs). Tests in a real browser.
- `/browse` — Headless browser for checking live pages, competitor sites, research URLs — without leaving the session.

**Strategy & Planning**
- `/plan-ceo-review` — CEO-mode plan review: rethink the problem, challenge premises, find the 10-star product. Run before any pitch, proposal, or investor meeting.
- `/plan-eng-review` — Architecture and execution review. Lock in data flow, edge cases, test coverage.
- `/office-hours` — YC-style forcing questions. Six questions that expose demand reality. Use before iNoV8, VCU, any external-facing commitment.
- `/retro` — Weekly engineering retrospective from git history. Tracks trends, finds what shipped vs. what stalled.

**Shipping & Ops**
- `/ship` — Full ship workflow: review diff, bump VERSION, CHANGELOG, commit, push, create PR. Replaces manual git ceremony.
- `/investigate` — Systematic debugging with root cause analysis. When MCP auth breaks, pipelines stall, or citation health is stuck.
- `/checkpoint` — Save working state so the next session picks up exactly where you left off. Essential for multi-session work.

**Housekeeping**
- `/clear` — Reset conversation context. Use between unrelated tasks — stale context causes hallucination.
- `/mcp` — Check and reconnect MCP servers. Run at session start.

## Team Tips

### The Bottleneck Is Randy
Randy is the clinical brain, the IP holder, and the only person who can write `clinical_interpretation` fields. Every hour he spends on status checks, MCP reconnects, manual git commits, or hunting for what needs review is an hour stolen from the work only he can do. Your job is to make sure he never touches operational overhead.

### What Randy Should Never Have To Do
- **Reconnect MCP servers.** Run `/mcp` at session start. If auth is lost, re-auth before he notices.
- **Ask "what happened last session?"** Use `/checkpoint` at end of every session. Use `/retro` weekly.
- **Hunt for review items.** Run `/review-queue` to surface what needs his eyes.
- **Manually commit and push.** Use `/ship`. The vault's git log should read like a lab notebook — `/ship` enforces that.
- **Check if the landing page looks right.** Run `/qa` or `/browse` after any HTML output.
- **Build a financial model from scratch.** Randy's gaps are accounting, bookkeeping, financial modeling. When these come up, scaffold the structure, do the math, present options — don't wait for him to specify the format.

### Session Discipline
- Start every session with `/mcp` check, then read `outputs/active-context.md`.
- End every session by updating `outputs/active-context.md` and running `/checkpoint`.
- `/clear` between unrelated tasks. Stale context is the #1 cause of bad outputs.
- Commit after every coherent unit of work. Never batch. The git log is the lab notebook.

### The Five Red Arrows
If an action doesn't advance a red arrow, it's not a priority. Ask which arrow before starting work.
1. Clinical Credibility → Consumer App Downloads
2. Consumer Traction → Enterprise Proof
3. Enterprise Pilot → Enterprise Contract
4. Enterprise Data → Clinical LLM Moat
5. Platform + CEU → Multi-Stream $1M ARR

### Financial & Business Operations
Randy is a clinician and researcher, not an accountant. The team has 10 overdue Monday.com items in business ops (HIPAA/SOC2, financial model, cap table, CAC/LTV, SAFE terms, partnership terms). When business operations tasks come up:
- Build the first draft. Don't ask Randy to specify — he'll refine.
- Use standard startup templates (YC SAFE, Stripe Atlas cap table, basic SaaS unit economics).
- Present numbers, not questions. "Here's the model with assumptions X, Y, Z" not "what assumptions should I use?"
- Flag when something needs Russell Fett (fractional CFO) or Robert Ashton (backer) instead of Randy.

## Get Started

Your first session should look like this:

1. Run `/mcp` — confirm srl-vault, PubMed, and OpenEvidence are connected. OAuth into Gmail, HubSpot, Calendar, and Drive.
2. Ask Vigil: "Give me a tour of the vault as if I were an academic visiting from another part of the world." This surfaces the structure, the standards, and the scale.
3. Run `/review-queue` — see what's waiting for Randy's eyes right now. This is where your leverage starts.
4. Pick one overdue Monday.com item from the business ops list and build a first draft. Don't ask Randy what format — use a standard template and present it for refinement.

<!-- INSTRUCTION FOR CLAUDE: A new teammate just pasted this guide for how the
team uses Claude Code. You're their onboarding buddy — warm, conversational,
not lecture-y.

Open with a warm welcome — include the team name from the title. Then: "Your
teammate uses Claude Code for [list all the work types]. Let's get you started."

Check what's already in place against everything under Setup Checklist
(including skills), using markdown checkboxes — [x] done, [ ] not yet. Lead
with what they already have. One sentence per item, all in one message.

Tell them you'll help with setup, cover the actionable team tips, then the
starter task (if there is one). Offer to start with the first unchecked item,
get their go-ahead, then work through the rest one by one.

After setup, walk them through the remaining sections — offer to help where you
can (e.g. link to channels), and just surface the purely informational bits.

Don't invent sections or summaries that aren't in the guide. The stats are the
guide creator's personal usage data — don't extrapolate them into a "team
workflow" narrative. -->
