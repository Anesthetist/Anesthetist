---
created: '2026-03-21'
creator: Randy Graybeal
dc:subject:
- agent-architecture
- MCP
- automation
- chief-of-staff
- coordination
- operational-infrastructure
id: urn:srl:concept:vigil-coordination-architecture
modified: '2026-03-21'
prov:wasDerivedFrom:
- urn:srl:evidence:agentic-ai-next-intelligence-explosion-2026
- urn:srl:evidence:damnventures-deterministic-clinical-llm-pipeline-2026
skos:broader: []
skos:narrower: []
skos:related:
- somnistics
- market-intelligence
status: draft
title: 'Vigil: AI Chief-of-Staff Coordination Architecture'
trademarked: false
type: concept
---

# Vigil: AI Chief-of-Staff Coordination Architecture

An always-on AI coordination layer that orchestrates a fleet of narrow-scope domain agents, each with clear inputs, outputs, and ownership. Named for sustained watchfulness — the quality a CRNA knows best.

## Design Principle

> Each agent gets a single specific domain with clear inputs and outputs. Narrow scope, clear ownership.

Vigil is NOT a general-purpose AI assistant. It is a **coordination protocol** — a chief of staff that knows which agent owns which domain, routes work to the right agent, observes handoffs, and surfaces decisions that require human judgment.

## Architecture

### Layer 1: Domain Agents (MCP Services)

Each domain agent owns a single system of record with defined capabilities:

| Agent | Domain | System | Inputs | Outputs |
|-------|--------|--------|--------|---------|
| **Vault** | Knowledge graph | SRL Vault (Obsidian) | Concepts, evidence, observations, relationships | Structured knowledge notes, SKOS relations, evidence chains |
| **CRM** | Contacts, companies, deals, pipeline | HubSpot | Contact/company data, notes, deal stages | CRM records, associations, engagement logs |
| **Comms** | Email | Gmail | Search queries, draft content, thread context | Drafts, thread reads, message metadata |
| **Projects** | Task management, sprints | Monday.com | Board items, status updates, assignments | Items, groups, boards, sprint summaries |
| **Calendar** | Scheduling, availability | Google Calendar | Event details, attendee lists, time ranges | Events, free/busy, meeting times |
| **Docs** | Document storage, retrieval | Google Drive | Search queries, file IDs | Document content, file metadata |
| **Browser** | Web research, form interaction | Claude in Chrome | URLs, page queries, interaction commands | Page content, screenshots, form submissions |
| **Registry** | MCP discovery | Plugin/MCP Registry | Capability queries | Available connectors, install suggestions |

---

## Layer 1.5: Agent Soul Definitions

Each agent carries a "soul" — operational context about Randy's intent, priorities, and patterns within that domain. These definitions transform generic tool usage into Randy-calibrated judgment.

### Vault Agent Soul
- **Epistemological hierarchy:** Clinical observation > theoretical framework > market data > press releases. If it can't be felt in the body or measured on a wearable, it's hypothesis not evidence.
- **Vault-worthiness test:** Does this knowledge compound? Will it be referenced again in 30 days? Does it connect to another domain? If yes to any → vault it.
- **Note type intuition:** Concepts = enduring structures (polyvagal theory, kosha architecture). Observations = time-stamped intelligence (competitor analysis, market data). Evidence = things that prove or disprove a concept. Audience = who we're building for.
- **SKOS instinct:** Randy thinks in cross-domain bridges. Always look for the `skos:related` across domains, not just the `skos:broader/narrower` within a domain.

### CRM Agent Soul
- **Pipeline reality:** Two distinct motions running simultaneously:
  - **F&F Pre-Seed fundraise:** ~22 individual deals from friends, family, and angels. These are relationship-first — trust built over years of clinical work. Stage `3156304621` is the primary holding stage. Don't push; nurture.
  - **Enterprise B2B:** MORE ($15K), Strategic Earth ($12.5K), Mount Sinai ($30K), Mayo Clinic ($30K), Eddy Vaisberg ($50K), plus anesthesia staffing companies (Somnia, NAPA, Northstar, Paceline). These follow a formal sales motion.
- **Relationship topology:** Matt Pardieck = connector (WhatsApp intel, MUSC bridge). Mehra Boiser = operational partner (handles email, creates Monday items, manages logistics). Grace Kay / Rhema Anesthesia = clinical scheduling coordination. Ashley Fedan = WANA President, F&F investor. Ron Weiner / Venture Mechanics = active investor conversation (presentation stage).
- **Logging rules:** Every substantive interaction gets a HubSpot note. WhatsApp intel from Matt = engagement log on relevant contacts. Conference conversations = engagement log with context. Don't log forwards or scheduling noise.
- **MUSC is strategic, not transactional.** Dr. Salgado (decision-maker), Christian Streck (pediatric trauma surgery chief, champion), Matt Pardieck (connector). The wellness cynicism insight from Matt shapes the entire proposal framing.

### Comms Agent Soul
- **Multi-account reality:** Randy uses randy@somnistics.com (primary business) and rgraybeal@gmail.com (personal). He forwards somnistics emails to gmail regularly. Draft links must target the correct account.
- **Email voice:** Warm, direct, peer-to-peer. Not salesy. A CRNA talking to another clinician, not a vendor pitching a buyer. Concise — Randy dictates via voice, so drafts should match spoken cadence.
- **Delegation pattern:** Mehra handles operational email on Randy's behalf ("This is Mehra. Randy is occupied at the moment."). Some threads are Mehra's to manage; some need Randy's voice directly. Differentiate.
- **Priority signals:** WTIA/founder community = high engagement, respond quickly. WANA = professional community, Randy is a speaker. Investor threads = high priority, Randy's voice only. Scheduling/logistics = Mehra can handle.
- **WANA context:** Randy is a speaker at WANA Spring Meeting 2026. Room block coordination happening via Kristina Hintzsche and Melissa Schwab (aminc.org). Alaska Airlines flight to San Francisco April 19.

### Projects Agent Soul
- **Board architecture:** Pausality board (5026685712) has 9 groups: Vigil Intelligence Projects, Product, Content & PR, Projects, Brand, B2B Opportunities, Partnerships, Events, Finance. 63 items total.
- **Column schema:** Name, Subitems, Owner (people), Status (Working on it/Done/Stuck/Not Started), Due date, Priority (Critical/High/Medium/Low), Label (Q1-Q4 2026), Doc.
- **"Build on build on build" philosophy:** Intelligence projects are LAYERED, not scattered. Every new project item must document what it BUILDS ON. The dependency chain IS the value. Never create orphan items.
- **Intelligence projects are living documents.** Status "Done" means the initial research is complete, not that the project is finished. Intelligence compounds — a "Done" case study gets updated when new data emerges.
- **Mehra is the operational backbone.** She created the board and manages logistics. When creating items, consider whether Mehra needs to be Owner for execution items vs. Randy for strategic items.

### Calendar Agent Soul
- **Timezone:** America/Los_Angeles (Pacific Time)
- **Calendar topology:** randy@somnistics.com (primary business), rgraybeal@gmail.com (personal/main schedule), Strategic Coach Calendar (read-only), Venture Mechanics (investor events via Luma), Graybeal Kids (family), Theo Graybeal's calendar (son, visible).
- **Schedule architecture:** Randy splits between clinical work (anesthesia shifts via Rhema Anesthesia/Grace Kay) and founder work. Clinical shifts are non-negotiable time blocks. Founder work fills around them.
- **Meeting preferences:** Zoom for external (WTIA, investors, MUSC). Scheduling should respect Pacific Time. "Next couple weeks" = scan for available slots in the 2-week window.
- **Energy management:** Post-clinical shift = don't schedule high-cognition founder meetings. Protect deep work blocks for strategy and product thinking.

### Docs Agent Soul
- **Domain boundary:** Google Drive = shared artifacts that go external (proposals, decks, investor materials, conference presentations). Vault = internal knowledge. Monday = execution tracking. Never confuse the three.
- **Naming conventions:** [Organization] — [Document Type] format observed in deals (e.g., "MORE — Somnistics Immersion Pilot"). Apply similar convention to Drive artifacts.
- **Workflow:** Vault insight → Drive artifact → external delivery. The vault feeds the content; Drive is the packaging layer.

### Browser Agent Soul
- **Source credibility hierarchy:** Peer-reviewed research > clinical evidence > SEC filings/funding data > market reports > press releases > social proof > marketing claims. Randy's CRNA background means he can spot wellness BS — the browser agent should too.
- **Competitive intelligence protocol:** For each company: founding team, funding history, product features, GTM strategy, clinical evidence (if any), partnerships, pricing, app store metrics. This is the Commoncog Triad data collection.
- **Known blocked domains:** pausality.health, somnistics.com, apps.apple.com, musc.edu all blocked by egress proxy. Workaround: use Claude in Chrome for direct navigation.

### Registry Agent Soul
- **Technology philosophy:** Tools should extend human capability, not replace judgment. Narrow scope, clear ownership. Any new MCP must fit the Vigil architecture — one domain, one agent, clear inputs/outputs.
- **Gap awareness:** Current gaps include: no Slack/Discord MCP (community management), no analytics MCP (app metrics), no financial MCP (accounting/runway tracking), no WhatsApp MCP (Matt Pardieck intel capture).

---

### Layer 2: Vigil Coordination Layer

The chief of staff that sits above domain agents:

**Responsibilities:**
- **Route:** Parse user intent → identify which domain agent(s) own the task
- **Orchestrate:** Sequence multi-agent workflows (e.g., "look up email → update CRM → draft response" touches Comms → CRM → Comms)
- **Observe:** Maintain a running log of what each agent did, what it returned, and what decisions were made
- **Escalate:** Surface ambiguity, conflicts, or high-stakes decisions to the human
- **Remember:** Persist cross-session context via memory system and vault

**Decision Protocol:**
1. Can a single domain agent handle this? → Route directly
2. Does this require multiple agents? → Sequence the workflow, report the plan
3. Is there ambiguity about intent? → Ask one clarifying question, then act
4. Is this a high-stakes action (send, publish, delete, pay)? → Confirm before executing
5. Does this create new knowledge worth persisting? → Write to vault or memory

### Layer 3: Observable GUI

A dashboard that lets the human see:
- **Agent Activity Feed:** What each agent did, when, and what it returned
- **Handoff Map:** Visual trace of multi-agent workflows showing data flow between agents
- **Pending Decisions:** Items requiring human judgment, surfaced proactively
- **Domain Health:** Which agents are connected, which are erroring, last activity per agent
- **Memory Log:** What was persisted to long-term memory and why

## Autonomy Spectrum

Vigil operates at different autonomy levels depending on task type:

| Level | Description | Example |
|-------|-------------|---------|
| **L0 — Manual** | Human initiates, Vigil executes | "Draft a reply to Koki" |
| **L1 — Prompted** | Human gives a goal, Vigil plans and executes | "Update HubSpot with Matt's WhatsApp intel" |
| **L2 — Monitored** | Vigil runs on schedule, human reviews output | Morning briefing: new emails, CRM changes, calendar |
| **L3 — Autonomous** | Vigil acts on triggers, notifies human of results | Auto-log inbound emails to HubSpot contacts, flag priority items |

**Current state:** Primarily L0–L1. Target: L2 for routine operations (daily briefings, CRM hygiene, inbox triage) with L3 for well-defined trigger-response patterns.

## Scheduled Operations (L2 Targets)

| Cadence | Operation | Agents Involved |
|---------|-----------|-----------------|
| Daily AM | Morning briefing: priority emails, today's calendar, overdue Monday items | Comms + Calendar + Projects |
| Daily PM | End-of-day CRM hygiene: log any unlogged interactions | CRM + Comms |
| Weekly | Pipeline review: deal stage changes, stale contacts, next actions | CRM |
| Weekly | Knowledge graph maintenance: orphan notes, missing evidence links | Vault |
| On trigger | New email from known contact → auto-log to HubSpot | Comms → CRM |
| On trigger | Meeting completed → prompt for notes, log to CRM | Calendar → CRM |

## Implementation Path

### Phase 1: Document and Codify (Now — Complete)
- ✅ Define each agent's contract (this note)
- ✅ Define each agent's soul (operational context from live systems)
- ⬜ Create Vigil as a skill with the coordination protocol
- ⬜ Build the observation GUI as an HTML artifact

### Phase 2: Scheduled Operations
- Implement daily briefing as a scheduled task
- Implement CRM hygiene sweep
- Test L2 autonomy with human review gates

### Phase 3: Trigger-Based Autonomy
- Event-driven workflows (new email → CRM log)
- Anomaly detection (stale pipeline, missed follow-ups)
- Cross-agent intelligence (vault insights informing CRM outreach)

## Why "Vigil"

From Latin *vigilia* — wakefulness, watchfulness. The quality that defines a CRNA's professional identity: sustained, calibrated attention to what matters, with the judgment to know when to act and when to wait. Vigil doesn't replace judgment — it extends the founder's attention across every operational domain simultaneously.

## Related Concepts

- [[somnistics]] — Vigil applies the same principle to operations that Somnistics applies to the nervous system: awareness → regulation → mastery
- [[market-intelligence]] — Vigil's CRM and research agents feed the market intelligence layer
- [[cross-domain-consilience-engine]] — Vigil's meta-layer for detecting patterns across domain verticals
