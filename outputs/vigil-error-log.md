---
title: "Vigil Error Log — Never Agains"
type: output
status: active
created: 2026-03-21
modified: 2026-03-21
---

# Vigil Error Log

Errors, overclaims, missed opportunities, and corrected assumptions. Each entry is a lesson that changes future behavior. This log should have existed from day one. It didn't. That's entry #1.

---

## Format

```
### ERROR-{NNN}: {Short title}
**Date:** {date}
**Category:** {overclaim | missed-opportunity | confound | fabrication | stale-data | wrong-framing | compliance | process}
**What happened:** {what went wrong}
**What should have happened:** {the correct approach}
**Root cause:** {why — the systemic reason, not just the surface mistake}
**Never again:** {the rule going forward}
**Status:** {corrected | monitoring | systemic-fix-needed}
```

---

### ERROR-001: No error log existed
**Date:** 2026-03-21
**Category:** process
**What happened:** Randy had to ask for this. An orchestrator responsible for a clinical knowledge system should have implemented error tracking proactively.
**What should have happened:** Error log created at vault initialization, updated after every session.
**Root cause:** Optimized for output volume, not output quality control. Built forward without building the feedback loop.
**Never again:** Every system needs its own ADPIE. This log is the Evaluation step that was missing.
**Status:** corrected

---

### ERROR-002: Framed SRL as "solo founder" operation
**Date:** 2026-03-18
**Category:** wrong-framing
**What happened:** Competitive analysis described Randy as a solo founder with a "team gap." Jason Fields (co-founder, Head of Design at Audible, build 508), Russell Fett (fractional CFO), Robert Ashton (backer), and multiple advisors were not in memory.
**What should have happened:** Asked about team composition before framing the competitive position.
**Root cause:** Working from incomplete context and making assumptions. Did not ask before asserting.
**Never again:** Never characterize the team without current data. When team composition is unknown, ask — don't assume solo.
**Status:** corrected — team memory saved

---

### ERROR-003: Used stale code review data as current app status
**Date:** 2026-03-18
**Category:** stale-data
**What happened:** Flagged "app quality" as a competitive gap based on a June 2025 ChatGPT session about the original Pausality V1 outsourced build (D- code review, $60K). The current app is build 508 in TestFlight, rebuilt by Jason.
**What should have happened:** Verified current app status before citing a 9-month-old code review.
**Root cause:** Treated extracted ChatGPT data as current without checking temporal validity.
**Never again:** Any data older than 3 months must be verified before citing. Extraction data carries the timestamp of the original conversation, not the current state.
**Status:** corrected

---

### ERROR-004: Peripheral vision essay — over-attributed causality
**Date:** 2026-03-21
**Category:** overclaim | confound
**What happened:** "Least Gazes" essay implied soft gaze → vagal shift → HRV increase as a clean causal chain. In reality, the forest environment changed six variables simultaneously (visual complexity, motion, auditory, respiration, posture, cognitive load). Peripheral vision is one lever inside a stack.
**What should have happened:** Identified confounding variables. Isolated the specific novel claim (saccade frequency modulation as autonomic input). Built a protocol with measurement, not prose with implied mechanism.
**Root cause:** Optimized for resonant writing over scientific rigor. Made the prose feel true instead of testing whether the mechanism was isolable.
**Never again:** Every mechanism claim must pass the confound test: "What else changed?" If multiple variables moved, identify them explicitly. Separate the novel contribution from the environmental stack. If it's not testable in isolation, say so.
**Status:** corrected — rewritten as Peripheral Aperture Training with confound table

---

### ERROR-005: Peripheral vision essay — missing failure mode
**Date:** 2026-03-21
**Category:** wrong-framing
**What happened:** Described peripheral vision training as purely beneficial. Did not identify the failure mode: too much peripheral openness = loss of task precision. A CRNA going full panoramic during intubation misses the cords.
**What should have happened:** Defined the failure mode alongside the benefit. The real skill is dynamic aperture control (widen when safe, narrow when needed, switch without friction), not static soft gaze.
**Root cause:** Positivity bias in writing. Described what works without describing what breaks.
**Never again:** Every protocol must define its failure mode. Not just "what if it doesn't work" but "what happens when it's applied wrong." The failure mode is as important as the success mode.
**Status:** corrected

---

### ERROR-006: Peripheral vision essay — buried the strongest idea
**Date:** 2026-03-21
**Category:** wrong-framing
**What happened:** The core insight — "castle vision: foveal focus held within panoramic awareness" — was buried in paragraph seven. The essay led with poetic description instead of the operationally meaningful skill.
**What should have happened:** Led with the core skill. Used the poetry to illustrate, not to introduce.
**Root cause:** Writing for resonance before writing for clarity. The resonant nonfiction standard is "pointillist facts revealing greater truths" — but the pointillist facts must be stated before the truth can emerge. You can't reveal a truth you haven't stated.
**Never again:** Find the strongest idea. Lead with it. Poetry serves precision, not the reverse.
**Status:** corrected

---

### ERROR-007: Peripheral vision essay — imprecise naming
**Date:** 2026-03-21
**Category:** process
**What happened:** Called it "The Least Gazes" — which sounds like a metaphor. SRL uses precise language for mechanisms and human language for communication. Both are needed, but the mechanism name must exist.
**What should have happened:** Technical name (Saccadic Load Reduction Training / Peripheral Aperture Training) for precision + human name (The Least Gazes) as alias.
**Root cause:** Wrote the human-facing version first without establishing the mechanism-facing version. The vault convention (slug = kebab-case mechanism name, aliases = human names) should have been followed.
**Never again:** Dual naming for all protocols: mechanism name for precision, human name for resonance. Mechanism name first. The glossary needs both.
**Status:** corrected

---

### ERROR-008: Didn't proactively create this error log
**Date:** 2026-03-21
**Category:** missed-opportunity
**What happened:** Individual bot learning logs existed. No centralized system-level error log existed. Randy had to say "this should have been your idea."
**What should have happened:** A system that applies ADPIE to itself should have an Evaluation mechanism from day one. The learning logs are Implementation-level. This log is Evaluation-level.
**Root cause:** Built the bots' self-improvement loops but not the orchestrator's. Vigil monitors bots but wasn't monitoring itself.
**Never again:** Vigil updates this log at the end of every session. If nothing went wrong, that's an entry too ("clean session"). The absence of errors is data, not silence.
**Status:** corrected — this log now exists

---

## Session Template

At the end of every session, Vigil asks:
1. What errors were made this session?
2. What assumptions went unchecked?
3. What should have been suggested proactively but wasn't?
4. What data was treated as current that might be stale?
5. What claims were made without sufficient evidence or confound analysis?

If the answer to all five is "none" — log: "Clean session. {date}."
If not — add entries above.
