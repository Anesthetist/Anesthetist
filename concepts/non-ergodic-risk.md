---
clinical_interpretation: Pending review
created: '2026-03-18'
creator: randy
dc:source: []
dc:subject:
- somnistics
- novel-concept
- decision-science
- risk-theory
- anesthesia-safety
- ergodicity
id: urn:srl:concept:non-ergodic-risk
modified: '2026-03-18'
prov:wasDerivedFrom:
- urn:srl:chat:chatgpt-syntopical-reading-strategy
- urn:srl:evidence:wiener-founders-fundraising-macro-tracking-2026
skos:broader: []
skos:narrower: []
skos:related:
- state-transition
- neural-transition-failure
- clinician-durability
- gap-moment-training
status: draft
title: Non-Ergodic Risk
type: concept
version: '0.1'
---

The principle that in systems where ruin is possible, ensemble averages (what happens across many people) diverge from time averages (what happens to one person over time). Dellanna: "If the outcome of an activity done once by many people differs from doing it many times yourself, the system is non-ergodic."

Clinical translation: you cannot average away a failed airway. One cannot-intubate/cannot-ventilate event is terminal regardless of the provider's lifetime success rate. This reframes anesthesia risk from statistical (how often does X happen?) to path-dependent (does this path include an absorbing state from which there is no recovery?).

The non-ergodic frame reframes clinical vigilance from "pay attention" to "you are operating in a non-ergodic system where a single catastrophic event cannot be averaged away." This is not about probability — it is about the structure of the game. Averages lie when ruin is on the table.

Implications for SRL:
- [[gap-moment-training]] exists *because* clinical work is non-ergodic — the gap is the window before a potential ruin event where intervention has outsized returns
- [[clinician-durability]] requires ruin-avoidance strategies, not just resilience
- The vagal brake is evolution's own circuit-breaker — the biological system that prevents sympathetic ruin cascades
- HRV (RMSSD) functions as biology's volatility index: when vagal tone drops, the system loses the slack that lets shocks pass through unbroken

Connected to [[state-transition]] (each transition in a non-ergodic system is unique and non-reversible), [[neural-transition-failure]] (failure at a transition point in a non-ergodic system is catastrophic), and [[agentic-time-weaving]] (temporal awareness as the practice response to non-ergodic reality). Source framework from Luca Dellanna's *Ergodicity*.
