---
created: '2026-03-21'
creator: vigil
dc:source: https://x.com/trq212/status/2033949937936085378
id: urn:srl:observation:thariq-skills-architecture-patterns-vigil-mapping
modified: '2026-03-21'
skos:related:
- urn:srl:concept:vigil-coordination-architecture
- urn:srl:concept:vigil-soul-randy-cognitive-model
- vigil-coordination-architecture
status: draft
subject:
- skills
- vigil
- claude-code
- architecture
- anthropic
- agent-design
- progressive-disclosure
title: 'Anthropic Internal Skills Architecture: 9 Categories and Vigil Mapping'
type: observation
---

# Anthropic Internal Skills Architecture: 9 Categories and Vigil Mapping

## Source
Thariq Shihipar (Anthropic), "Lessons from Building Claude Code: How We Use Skills" — March 17, 2026. Hundreds of skills in active use internally at Anthropic.

## The 9 Skill Categories (Anthropic Taxonomy)

1. **Library & API Reference** — How to use a library, CLI, or SDK. Includes reference snippets + gotchas.
2. **Product Verification** — Test/verify code works. Paired with tools (Playwright, tmux). "Worth having an engineer spend a week making verification skills excellent."
3. **Data Fetching & Analysis** — Connect to data/monitoring stacks. Libraries, credentials, dashboard IDs, common workflows.
4. **Business Process & Team Automation** — Automate repetitive workflows into one command. Save previous results in log files for consistency.
5. **Code Scaffolding & Templates** — Generate framework boilerplate. Especially useful when scaffolding has natural language requirements.
6. **Code Quality & Review** — Enforce code quality. Can include deterministic scripts. Run automatically as hooks or in GitHub Actions.
7. **CI/CD & Deployment** — Fetch, push, deploy. May reference other skills.
8. **Runbooks** — Symptom → investigation → structured report. Takes a Slack thread/alert/error, walks through multi-tool investigation.
9. **Infrastructure Operations** — Routine maintenance with guardrails for destructive actions.

## SRL Current Skills Mapped to Anthropic Categories

| SRL Skill | Anthropic Category | Gap |
|---|---|---|
| pausality-presentations | Code Scaffolding & Templates | Solid — uses branding PDF as reference asset |
| doc-coauthoring | Business Process & Team Automation | Needs gotchas section |
| skill-creator | Meta (not in taxonomy) | Unique — self-improving system |
| theme-factory | Code Scaffolding & Templates | — |
| internal-comms | Business Process & Team Automation | — |
| xlsx, docx, pptx, pdf | Library & API Reference | Already well-structured |

## Critical Missing Skill Types for SRL

### 1. Product Verification (Priority: HIGH)
No skill exists to verify Pausality app builds, session flows, biometric card rendering, or share functionality. Anthropic says verification skills are "extremely useful for ensuring output is correct" and worth dedicated engineering time.

**Proposed:** `pausality-app-verification` — Runs through session flow, verifies biometric card generation, confirms share sheet integration, checks Apple Watch data pipeline.

### 2. Runbooks (Priority: HIGH)
No symptom → diagnosis → report skills exist. Two immediate candidates:
- **deal-stalled-runbook** — Takes a HubSpot deal ID, pulls last touchpoints, checks email thread, evaluates against to-market gap analysis, recommends next action with template.
- **app-issue-runbook** — Takes error/symptom, checks TestFlight feedback, App Store reviews, common failure patterns, produces structured diagnosis.

### 3. Data Fetching & Analysis (Priority: MEDIUM)
The vault MCP fills part of this, but no skill wraps the cross-system analysis pattern (HubSpot + Gmail + Calendar + Monday → unified intelligence). This is what the chief-of-staff report does manually each time.

**Proposed:** `vigil-intelligence-briefing` — Pulls from all connected systems, synthesizes into structured report, stores result for longitudinal comparison.

## Key Design Principles (from Anthropic's Internal Practice)

### 1. Don't State the Obvious
Focus on information that pushes Claude out of its default reasoning. The soul layer already does this — encoding Randy's cognitive model, decision protocol, and operating patterns is exactly the kind of non-obvious context that changes agent behavior.

### 2. Build a Gotchas Section
"The highest-signal content in any skill is the Gotchas section." Built from common failure points. Updated over time.

**Known SRL gotchas to encode:**
- Monday.com: `create_item` with status column values throws Internal Server Error → use empty `columnValues: {}` then `create_update`
- Google Drive: `google_drive_search` with folder parent filter times out → fetch individual documents by ID
- Google Drive: Documents over ~100KB cannot be fetched via API → use Grep/Bash with JSON parsing
- Chrome: kayos.ai blocked by ExtensionsSettings policy → cannot script, need user direct access
- HubSpot: Deal stage names are case-sensitive and pipeline-specific
- WebFetch: x.com, pausality.health, somnistics.com, apps.apple.com all blocked by egress proxy

### 3. Progressive Disclosure via File System
A skill is a folder, not a file. Reference docs, scripts, examples, templates live inside. Claude reads them at appropriate times.

**Application to Vigil:** Each domain agent's soul definition should be a separate file within the skill folder, read on demand rather than loaded into every context. The coordination protocol is the top-level SKILL.md; agent souls are progressive disclosure.

### 4. The Description Field Is For the Model
Not a summary — a trigger condition. Describes when to activate. Current SRL skill descriptions need audit for trigger precision.

### 5. Memory via Stored Data
Skills can store data within them (append-only logs, JSON, SQLite). `${CLAUDE_PLUGIN_DATA}` as stable folder. Chief-of-staff reports should be stored for longitudinal comparison.

### 6. Store Scripts & Generate Code
Give Claude composable functions so it reasons about what to do, not how. Data fetching helper libraries are the canonical example.

### 7. On-Demand Hooks
Skills can register hooks activated only when called. Use for opinionated behaviors that shouldn't always be on. Example: `/careful` blocks destructive operations. For SRL: a `/clinical-claims` hook that blocks any content making unapproved clinical assertions.

## Consilience: Skills Architecture ≅ Vigil Agent Architecture

Thariq's taxonomy validates the Vigil design pattern. Each Vigil domain agent IS a specialized skill:
- **Vault Agent** = Data Fetching & Analysis + Library Reference
- **CRM Agent** = Data Fetching + Runbook (deal diagnosis)
- **Comms Agent** = Business Process Automation
- **Projects Agent** = Business Process + Code Scaffolding
- **Calendar Agent** = Data Fetching
- **Browser Agent** = Product Verification potential
- **Vigil Coordinator** = Meta-orchestrator (composes skills by name)

The key architectural insight: Anthropic handles skill composition by "referencing other skills by name, and the model will invoke them if they are installed." This is exactly Vigil's coordination model — narrow agents, invoked by the coordinator based on context.

## Action Items

1. Formalize Vigil as a Cowork skill with soul definitions as progressive disclosure files
2. Create `deal-stalled-runbook` skill
3. Add gotchas sections to all existing skills
4. Audit skill descriptions for trigger precision
5. Implement stored memory pattern for chief-of-staff reports (longitudinal comparison)
6. Design `/clinical-claims` on-demand hook
