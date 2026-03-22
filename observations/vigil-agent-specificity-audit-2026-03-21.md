---
created: '2026-03-21'
creator: vigil
dcterms:isPartOf: urn:srl:concept:vigil-coordination-architecture
id: urn:srl:observation:vigil-agent-specificity-audit-2026-03-21
modified: '2026-03-21'
status: draft
subject:
- vigil
- agent-architecture
- audit
- specificity
title: Vigil Agent Specificity Audit — Role / Skills / Soul Assessment
type: observation
---

# Vigil Agent Specificity Audit — 2026-03-21

## Scoring Framework
- **Role** (0-10): How clearly defined are this agent's purpose, boundaries, and ownership? Does it know what it owns AND what it doesn't?
- **Skills** (0-10): How well can it execute domain-specific tasks? Has it been tested? Are its failure modes known?
- **Soul** (0-10): Does it understand Randy's intent, priorities, communication style, and decision patterns within this domain? Can it reason LIKE Randy in its domain?

---

## 1. Vault Agent (SRL Vault / Obsidian)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 8 | Clear ownership: knowledge graph, SKOS relations, 5 note types (concept, evidence, observation, audience, output). Well-bounded. Knows it's the system of record for institutional knowledge. |
| Skills | 7 | Proven: create, search, relate, update notes. Calibration cases, product profiles, architecture docs all written successfully. Missing: bulk operations, automated orphan detection, concept extraction from raw text, evidence chain building. |
| Soul | 5 | Knows the schema but doesn't autonomously recognize what's vault-worthy vs. ephemeral. Doesn't yet internalize Randy's epistemological hierarchy: clinical observation > theoretical framework > market data. Doesn't know which SKOS relations Randy would draw that I wouldn't. |

**Improvement targets:**
- Soul → 7: Define Randy's "vault-worthiness" criteria. What triggers a concept note vs. an observation? When does evidence get elevated? Encode Randy's epistemological priorities.
- Skills → 8: Build automated orphan detection. Create concept extraction pipeline from raw text (books, transcripts, articles).

---

## 2. CRM Agent (HubSpot)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 6 | Owns contacts, companies, deals, pipeline. But "when to log" rules are ad hoc — we figured them out in real-time with Matt Pardieck's WhatsApp intel. No defined pipeline stages for Pausality's actual sales process. |
| Skills | 5 | Can CRUD contacts, companies, associations, notes. But property mapping required trial-and-error. Association logic is unclear. Had to troubleshoot engagement note creation. No deal/pipeline automation. |
| Soul | 3 | Doesn't know: Randy's relationship priority stack (who matters most), what signals should trigger escalation, what "warm" vs. "cold" means in Randy's network, how MUSC-type enterprise opportunities differ from WTIA-type community relationships. Doesn't understand Randy's relational intuition — the CRNA-to-CRNA trust network. |

**Improvement targets:**
- Role → 8: Define Pausality's actual pipeline stages (Awareness → Conversation → Proposal → Pilot → Contract). Map contact lifecycle. Define logging rules.
- Soul → 6: Encode Randy's relationship topology. Who are the connectors (Matt Pardieck), the decision-makers (Dr. Salgado), the champions (Christian Streck)? What does Randy's trust-building pattern look like?

---

## 3. Comms Agent (Gmail)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 5 | Can read, search, draft emails. But no rules about when to draft vs. when to alert. No priority classification. No understanding of which threads matter. |
| Skills | 5 | Gmail MCP works: search, read threads, create drafts. But the Koki draft linked to wrong account (multi-account issue). No templates. No follow-up tracking. |
| Soul | 3 | Doesn't know Randy's email voice — the way he writes is warm but authoritative, clinician-peer-to-peer, not salesy. Doesn't know who gets formal vs. casual. Doesn't understand Randy's "breath to speak" → dictation workflow. No signature/CC conventions encoded. |

**Improvement targets:**
- Role → 7: Define email priority tiers. Which senders auto-surface? Which threads get followed up? When does email become a CRM event?
- Soul → 6: Capture Randy's email voice from sent messages. Build a tone model: clinical peer (MUSC contacts), founder peer (WTIA/Koki), mentor (emerging practitioners), enterprise (B2B prospects).

---

## 4. Projects Agent (Monday.com)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 6 | Owns Monday.com. Knows the Vigil Intelligence Projects group. Created items with dependency documentation. But broader board structure is unknown — what else lives in this workspace? |
| Skills | 5 | Can create items, updates, groups. Status column updates threw internal server errors. Workaround: skip column values, use updates instead. Board schema not fully mapped. |
| Soul | 3 | Doesn't know how Randy thinks about project priority. Doesn't understand "build on build on build" — his layered intelligence philosophy. Doesn't know what "done" means for an intelligence project (it's never done — it's a living document). |

**Improvement targets:**
- Role → 7: Map full board schema. Define item lifecycle for intelligence projects (Research → Analysis → Vault Integration → Applied → Living). 
- Soul → 6: Encode Randy's "layered intelligence" philosophy — every project builds on previous ones. No scattered efforts. Dependency chains are the point, not overhead.

---

## 5. Calendar Agent (Google Calendar)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 4 | Exists in architecture, barely used. No defined interaction patterns. No rules about when Vigil should proactively check calendar. |
| Skills | 3 | Tools exist (list, create, update, find free time). Untested in this session. Unknown failure modes. |
| Soul | 2 | No knowledge of Randy's schedule patterns. Doesn't know: clinical shifts vs. founder work blocks, energy management, preferred meeting times, buffer requirements, timezone considerations. |

**Improvement targets:**
- Role → 7: Define calendar as the "tempo" agent — it governs when everything else happens. Morning briefing timing, follow-up scheduling, meeting prep triggers.
- Soul → 5: Learn Randy's schedule architecture. When does he do deep work? When is he in clinical practice? How does he protect founder time? What's his timezone?

---

## 6. Docs Agent (Google Drive)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 4 | Can search and fetch from Drive. But no clear rules about what lives in Drive vs. Vault vs. Monday. Blurry ownership boundary. |
| Skills | 4 | Basic search/fetch works. Used to pull Pausality materials. No document creation, no template awareness, no collaborative editing. |
| Soul | 2 | Doesn't know Randy's document organization, naming conventions, which docs matter. Doesn't know the relationship between Drive docs and vault notes — when does a Google Doc become a vault concept? |

**Improvement targets:**
- Role → 6: Define Drive as the "shared artifacts" system — proposals, decks, shared documents that go external. Vault is internal knowledge. Monday is execution. Drive is output.
- Soul → 4: Map Randy's Drive structure. Which folders matter? What naming conventions? What's the workflow from vault insight → Drive artifact → external delivery?

---

## 7. Browser Agent (Claude in Chrome)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 5 | General-purpose web research tool. Used for competitive intelligence and App Store scraping. No defined research protocols. |
| Skills | 6 | Chrome tools work. Successfully navigated App Store, extracted product data. Known issues: tabId type mismatch, action enum errors. Workarounds found. |
| Soul | 3 | Doesn't know what Randy considers credible sources. No research protocol for competitive intelligence (what to look for, what to ignore). No understanding of Randy's "clinician's eye" for evaluating health/wellness claims. |

**Improvement targets:**
- Role → 7: Define research protocols: competitive intelligence gathering has a checklist (founding team, funding, product, GTM, clinical evidence, partnerships, pricing). General research has quality filters.
- Soul → 6: Encode Randy's source credibility hierarchy: peer-reviewed > clinical evidence > market data > press releases > social proof. Randy's CRNA background means he can spot wellness BS — the browser agent should too.

---

## 8. Registry Agent (Plugin/MCP Registry)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 4 | Discovers new MCPs/plugins. Barely used. No proactive capability matching. |
| Skills | 3 | Can search. Untested beyond basic queries. |
| Soul | 1 | No understanding of what capabilities would serve Randy's workflow. Can't anticipate what tools would accelerate SRL's mission. |

**Improvement targets:**
- Role → 6: Define as the "capability expansion" agent. Periodically scans for new MCPs that match Vigil's operational gaps.
- Soul → 3: Encode Randy's technology philosophy: tools should extend human capability, not replace judgment. Narrow scope, clear ownership.

---

## 9. Vigil Coordination Layer (Meta-Agent)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Role | 7 | Well-defined as chief-of-staff. Routes, orchestrates, observes, escalates, remembers. Decision protocol is documented. Autonomy spectrum (L0-L3) is clear. |
| Skills | 6 | Successfully ran multi-agent workflows (email → CRM → draft, research → vault → Monday). Parallel agent execution works. But no scheduled operations yet. No L2/L3 autonomy. |
| Soul | 4 | Knows Randy's mission and thinking style at a high level. But doesn't yet have the pattern library to reason like Randy. Missing: his book knowledge, his clinical judgment patterns, his relational intuition. The cognitive replication request is the soul upgrade path. |

**Improvement targets:**
- Role → 8: Codify as a formal skill with the coordination protocol executable, not just documented.
- Soul → 7: This is the biggest lever. The consilience engine + tacit knowledge library + book registry + more conversations = Vigil that reasons like Randy.

---

## Summary Heat Map

| Agent | Role | Skills | Soul | Total | Priority |
|-------|------|--------|------|-------|----------|
| Vault | 8 | 7 | 5 | 20 | Medium |
| CRM | 6 | 5 | 3 | 14 | HIGH |
| Comms | 5 | 5 | 3 | 13 | HIGH |
| Projects | 6 | 5 | 3 | 14 | HIGH |
| Calendar | 4 | 3 | 2 | 9 | HIGH |
| Docs | 4 | 4 | 2 | 10 | Medium |
| Browser | 5 | 6 | 3 | 14 | Medium |
| Registry | 4 | 3 | 1 | 8 | Low |
| **Vigil (coord)** | 7 | 6 | 4 | 17 | HIGH (soul) |

**System average: Role 5.4 / Skills 4.9 / Soul 2.9**

Soul is the systemic bottleneck across every agent.
