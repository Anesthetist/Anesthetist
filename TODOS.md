# TODOS — Somnistics Library Graph

Last updated: 2026-04-11
Source: CEO Review + Eng Review (plan-ceo-review, plan-eng-review)

## P1 — Critical Path (May 30 Sprint)

### ~~Submit AANA Category A application~~ DONE
- **Status:** COMPLETED per Monday.com (Feb 24, 2026). Item "Q1 Jan 26 2026 AANA Cat A CE Application" marked Done.
- **What remains:** Complete course content to fulfill the approved application. Target: CANA conference May 28.

### Reconcile neurominute scripts to CE curriculum session map
- **What:** Lay all 21 neurominute scripts (outputs/neurominutes/day-01 through day-21.md) next to all 21 CE curriculum sessions (outputs/product/ce-course-maia2-mapped-curriculum.md). Confirm or deny alignment. Identify gaps where new scripts are needed.
- **Why:** Day numbers don't match session numbers. Day-08 is Alternate Nostril Breathing but CE Session 8 is "Listening" (body scan). The plan assumed alignment. They're not aligned. Every downstream task (wrappers, citations, quality gates) is blocked until this is resolved.
- **Context:** Discovered during eng review outside voice. This is the true Day 1 blocker.
- **Effort:** S (human: ~2 hours / CC: ~15 min)
- **Depends on:** Nothing. Start Day 1.

### Add contraindication protocol to CE session wrappers
- **What:** For techniques with safety considerations (breath-hold/kumbhaka, energizing breath), add contraindication sections to CE wrappers. Cover: pregnancy, cardiovascular disease, anxiety disorders, panic history.
- **Why:** AANA Category A requires safety protocols. The neurominute app scripts intentionally omit warnings ("we trust our users"), but CE clinical education has different liability requirements.
- **Context:** Contraindications go in CE wrappers only, not app scripts. Right boundary between consumer product and clinical education.
- **Effort:** S (CC: ~5 min per session)
- **Depends on:** Session map reconciliation complete.

_See also: CEO plan at `~/.gstack/projects/Anesthetist-Anesthetist/ceo-plans/2026-04-11-vault-strategic-realignment.md`._

## P2 — Post-May 30

### Build curriculum sequencer bot
- **What:** New bot at `_bots/curriculum-sequencer/` with soul.md, run-protocol.md, patterns.md. Maps vault concepts to AANA competency domains, generates CE session drafts from evidence chains.
- **Why:** Manual session mapping works but doesn't scale. Every future course (SRNA, enterprise, specialty) needs the same concept → competency → session pipeline.
- **Pros:** Reusable infrastructure, consistent quality, faster course generation.
- **Cons:** Requires AANA competency domain mapping as input. Pedagogical sequencing needs Randy validation.
- **Context:** Deferred from May 30 sprint — outside voice identified it as over-engineered for the deadline. Build after sessions 8-14 are complete, before starting 15-21.
- **Effort:** M (human: ~1 week / CC: ~30 min)
- **Depends on:** May 30 CE sessions 8-14 complete.

### Scope and build feedback layer infrastructure
- **What:** Add `feedback` note type to `_schema/note-types.yaml`, create template at `Templates/feedback.md`, modify srl-vault MCP server to accept new type in `create_note`.
- **Why:** Enables structured practitioner data collection from 14-day test (HRV readings, MAIA-2 scores). Turns vault from library into research instrument.
- **Pros:** Closes the data loop — practitioner outcomes become vault evidence.
- **Cons:** Requires MCP server code change (Python, local). Effort unscoped.
- **Context:** Deferred because MCP modification is always non-trivial until scoped. Fields defined in 14-day test protocol (participant_id, date, protocol_used, hrv_baseline, hrv_reading, maia2_score, subjective_report, peer_invitation_sent).
- **Effort:** S-M depending on MCP complexity
- **Blocked by:** 14-day test protocol must define data fields first. MCP server modification must be scoped.

### Build output dependency graph
- **What:** Add `sources:` frontmatter field to output notes. Build staleness detection script that compares source note `modified` dates against output `modified` dates.
- **Why:** Prevents stale outputs from undermining clinical credibility. When evidence is updated, downstream outputs (essays, CE sessions, proposals) should be flagged for refresh.
- **Pros:** Automated staleness detection. Foundation for auto-updating outputs (Phase 2+).
- **Cons:** Requires frontmatter migration on existing output notes. Graph traversal adds complexity.
- **Context:** Phase 2 infrastructure. The `sources:` field makes future auto-update possible but this plan only builds detection, not auto-update.
- **Effort:** M (human: ~1 week / CC: ~30 min)
- **Depends on:** Nothing — can start anytime post-May 30.

### Write CE sessions 15-21
- **What:** Complete the remaining 7 CE sessions using the same manual workflow (or curriculum sequencer bot if built first).
- **Why:** Full 21-session AANA Category A course for CANA.
- **Context:** Sessions 8-14 target May 30. Sessions 15-21 follow in June.
- **Effort:** M (same as 8-14 batch)
- **Depends on:** Sessions 8-14 approved. Optionally: curriculum sequencer bot.

## P3 — Infrastructure

### Fix remote essay engine git push credentials
- **What:** Configure git credentials in CCR (Claude Code Remote) environment so the remote essay engine can push commits.
- **Why:** Enables automated content generation without requiring local CC sessions. Currently enabled but has never successfully pushed.
- **Pros:** 24/7 content generation. Removes dependency on Randy having CC open.
- **Cons:** Security — git creds in remote environment must follow security protocol.
- **Context:** The remote trigger (trig_01V9vgkN7AXGUpmfEVtRsiFH) is ENABLED at claude.ai/code/scheduled but never pushed.
- **Effort:** S (human: ~2 hours / CC: ~15 min)
- **Depends on:** Nothing.

### Process remaining ChatGPT files
- **What:** Continue mining the 800+ remaining ChatGPT source files beyond the CE-relevant subset.
- **Why:** Potential missed insights, completeness of the knowledge graph.
- **Context:** Only 30-50 files triaged for May 30 sprint. 800+ remain in `sources/chatgpt/`.
- **Effort:** L (ongoing, batch processing)
- **Depends on:** Mining pipeline operational.

### Bot patterns.md creation
- **What:** Create `patterns.md` for 6 bots currently missing it. Bots operate in degraded mode without accumulated heuristics.
- **Why:** CLAUDE.md startup protocol requires loading patterns.md at pre-run. Missing files = degraded bot performance.
- **Context:** Address as each bot is activated. Don't build patterns for stalled bots.
- **Effort:** S per bot (CC: ~5 min each)
- **Depends on:** Bot activation.

### Vault-wide citation health remediation
- **What:** Run citation health check across all 523 evidence notes and fix broken/missing DOIs.
- **Why:** Currently at 45% health (100 valid, 70 broken, 52 missing). Clinical credibility requires verified citations.
- **Context:** May 30 sprint scopes to CE-relevant notes only. This covers the rest.
- **Effort:** L (human: ~2 weeks / CC: ~2 hours)
- **Depends on:** `tools/check-citations.sh` validated.

### 14-day test participant-facing artifact
- **What:** Design and build what CRNAs actually receive as participants — email sequence, PDF protocol, app integration, or all three.
- **Why:** The protocol exists in the vault but participants need a usable artifact. Without this, the test cannot run.
- **Context:** Flagged by outside voice — the plan builds the protocol but not the delivery mechanism.
- **Effort:** M
- **Depends on:** 14-day test protocol complete.
