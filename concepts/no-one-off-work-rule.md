---
audience:
- internal
created: '2026-04-12'
creator: randy-graybeal
id: urn:srl:concept:no-one-off-work-rule
modified: '2026-04-12'
skos:related:
- saturday-flight-check-ritual
status: canonical
subject:
- operational-infrastructure
- system-design
- codification
tags:
- vigil
- dispatch
- skills
- automation
title: No One-Off Work Rule
type: concept
---

# No One-Off Work Rule

If a task will need to happen again, it must be codified. The test: if Randy has to ask for something twice, the system failed.

## Protocol

1. **Scope a sample of 3-10 items.** Do the work manually the first time.
2. **Show Randy the output.** Wait for approval.
3. **Codify.** If it's a pattern → skill file. If it should run automatically → scheduled task (cron).
4. **Report codification.** Confirm the skill or cron is live.

## Definitions

- **Recurring (low bar):** anything that happens more than once. Weekly reviews, one-pagers for different audiences, research question packages for different advisors, promotion sprints, content drafts.
- **One-off (high bar):** truly singular events with no repeatable structure. These are rare.
- **3-10 manual items:** the proof-of-concept pass. Enough to validate the pattern, not so many that we've wasted effort before codifying.

## Failure Mode

When the system is about to deliver something Randy has asked for before: stop and name it. "You asked for this last [time]. I should have codified it. Let me do this one and also codify it so you never have to ask again."

## Application
This rule governs all Dispatch, Vigil, and agent behavior. It is a standing operational constraint that applies retroactively to identified patterns.
