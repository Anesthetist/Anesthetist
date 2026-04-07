---
created: '2026-03-30'
creator: Claude (Vigil)
id: urn:srl:observation:gstack-skill-design-patterns-for-vigil
modified: '2026-03-30'
prov:wasDerivedFrom:
- urn:srl:evidence:garrytan-gstack-claude-code-skill-pack-2026
status: draft
subject:
- agent-architecture
- skill-design
- vigil
- process-design
title: Skill Design Patterns from gstack Applicable to Vigil Agent Architecture
type: observation
---

# Skill Design Patterns from gstack for Vigil

## Pattern 1: Forcing Questions Before Action
gstack's /office-hours uses six "forcing questions" (demand reality, status quo, desperate specificity, narrowest wedge, observation, future-fit) before any implementation. These are deliberately uncomfortable.

**Vigil application:** Create an /office-hours skill for SRL that forces Randy to articulate: Who specifically needs this? What do they do now? What's the narrowest intervention? What would you observe if it worked? This prevents scope creep and grounds strategy in clinical reality.

## Pattern 2: Scope Modes
/plan-ceo-review offers four explicit scope modes: Expansion, Selective Expansion, Hold Scope, Reduction. The user selects the mode, and the agent operates within it.

**Vigil application:** Vigil strategic reviews should explicitly ask Randy which mode before proceeding. Prevents the pattern where Vigil suggests expansive work when Randy needs to focus, or vice versa.

## Pattern 3: Deliberate Sprint Sequence
Skills run in fixed order: Think → Plan → Build → Review → Test → Ship → Reflect. Each skill reads the output of the previous one.

**Vigil application:** Define explicit handoff artifacts between agents. Researcher produces evidence summaries → Builder reads them for content creation → Operator reads Builder output for distribution. Currently, Vigil coordinates but handoff formats aren't standardized.

## Pattern 4: Iron Law of Investigation
/investigate enforces: no fixes without investigation, max 3 failed hypotheses before stopping, auto-freeze to scope.

**Vigil application:** Researcher should follow this pattern when evaluating conflicting evidence or debugging vault inconsistencies. Prevents the "fix everything at once" anti-pattern.

## Pattern 5: Trend-Tracking Retros
/retro saves JSON snapshots to enable week-over-week trend tracking (shipping streaks, test health, per-person breakdowns).

**Vigil application:** Heartbeat reports should accumulate structured data, not just prose. Track: vault note count trends, pipeline deal movement, evidence strength scores, agent task completion rates. Store as structured JSON alongside the prose report.

## Pattern 6: Proactive Skill Suggestion
gstack detects work stage and suggests the appropriate skill. Respects user override ("stop suggesting").

**Vigil application:** Vigil should proactively suggest which agent to invoke based on context. If Randy is discussing strategy, suggest Researcher or Finance. If discussing content, suggest Builder. Currently reactive only.

## Pattern 7: Smart Review Routing
CEO doesn't review infra changes; design review skips backend. Reviews are matched to relevance.

**Vigil application:** Not every heartbeat needs to surface every agent's full report. Vigil should route based on what's actually changed or at risk. If vault hasn't changed, Librarian heartbeat should be minimal.

## Priority Adaptations for SRL

1. **HIGH: /office-hours skill** — Adapt forcing questions for SRL product/strategy context
2. **HIGH: Structured heartbeat data** — JSON snapshots alongside prose for trend tracking
3. **MEDIUM: Scope modes** — Add to Vigil strategic planning prompts
4. **MEDIUM: Sprint sequence formalization** — Standardize inter-agent handoff artifacts
5. **LOW: Proactive skill suggestion** — Requires more mature skill library first
