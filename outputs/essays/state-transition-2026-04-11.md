---
title: "Notes from the Lab: The Physiology of Switching — Why State Transitions Are Where Performance Lives and Dies"
series: "Notes from the Lab"
type: essay
status: draft
created: 2026-04-11
word_count: 1650
core_claim: "Clinical errors concentrate at state transitions — the moments between cases, between phases of care, between cognitive modes — and the underlying mechanism is autonomic, not attentional. Training the transition itself, rather than training for the event, changes the error surface."
potential_use:
  - book-chapter
  - substack
  - linkedin
  - ce-module
related_concepts:
  - state-transition
  - neural-transition-failure
  - gap-moment-training
  - neurogating
  - autonomic-regulation
  - clinician-durability
evidence_used:
  - bordini-2025-cognitive-errors-difficult-airway
  - voity-2025-or-distractions-cognitive-load
  - milleville-2025-crna-decision-making
  - awtry-2025-surgeon-autonomic-complications
  - popov-2025-team-communication-simulation
  - brosschot-2006-perseverative-cognition
gertrude_status: pending
---

# Notes from the Lab: The Physiology of Switching

*Clinical errors concentrate at state transitions. The mechanism is autonomic, not attentional. The transition itself is the trainable surface.*

## The Pattern Nobody Tracks

Twenty-eight years into anesthesia practice, I can tell you the exact shape of a bad shift. It is not the emergency case that breaks you. It is the case after the emergency case.

A difficult intubation at 0730. Adrenaline, focus, resolution. Patient secured. Case proceeds. At 0900 you are in a different room with a different patient, a routine knee scope, and you notice your hands are doing the right things but your attention is narrow in a way that does not match the clinical demand. You are still partially in the last room. Your heart rate settled, but not all the way. Your respiratory pattern shortened and stayed short. Some part of your nervous system is still managing a crisis that ended ninety minutes ago.

That carry-over has a name in the literature. [[brosschot-2006-perseverative-cognition|Brosschot, Gerin, and Thayer (2006)]] called the cognitive version perseverative cognition: the prolonged representation of a stressor that extends sympathetic activation and HPA axis engagement hours beyond the event itself. Worry is the future-oriented form. Rumination is the past-oriented form. Both sustain cortisol and norepinephrine at levels appropriate for the crisis and inappropriate for the knee scope.

But the deeper problem is not cognitive. It is autonomic. The nervous system failed to complete a transition. It got stuck between states, carrying residual sympathetic activation into a context that requires a different physiological posture. I call this [[neural-transition-failure]], and I believe it is the root mechanism behind most of the errors we attribute to fatigue, distraction, or burnout.

## The Evidence for Transition Failure

The data is converging from multiple directions.

[[bordini-2025-cognitive-errors-difficult-airway|Bordini and colleagues]] published in the British Journal of Anaesthesia in 2025, analyzing 2,801 difficult airway cases. Cognitive errors occurred in 17.4% of cases. The most common type was fixation error at 11.5%, where the clinician locked onto a failing plan and could not shift to an alternative. Each cognitive error increased the adjusted odds of complications by 1.86. Multiple errors raised it to 2.48. Fixation is a transition failure: the inability to shift cognitive state from plan A to plan B when plan A is not working.

[[popov-2025-team-communication-simulation|Popov and Rochlen (2025)]] used network analysis to study anesthesiology team performance in simulation. High-performing teams transitioned fluidly from assessment to planning to implementation. Low-performing teams cycled through assessment repeatedly without advancing to action. The effect size was d=1.72, which is enormous. The distinguishing feature between high and low performance was not the quality of the assessment. It was the ability to transition out of it. They called the failure mode "assessment cycling." I would call it getting stuck in a cognitive state that was appropriate thirty seconds ago and is now the wrong gear for what the situation requires.

[[milleville-2025-crna-decision-making|Milleville and colleagues]] published a qualitative study of CRNA decision-making in the AANA Journal in 2025, and the finding that matters here is straightforward: workflow transitions were identified as the points where decisions are most vulnerable. Not the middle of a case. Not the maintenance phase. The transitions. CRNAs themselves reported that stress, tiredness, and emotional load impair their cognitive performance, and they experience that impairment most acutely at the seams between phases of care.

Then there is the [[awtry-2025-surgeon-autonomic-complications|Awtry study]], published in JAMA Surgery in 2025. Prospective, multicenter, 793 procedures, 38 surgeons, four hospitals. Continuous HRV monitoring during surgery. The finding: surgeon sympathovagal balance during the first five minutes of a procedure predicted major surgical complications. Higher sympathovagal activation at incision, meaning the surgeon entered the case in an appropriately aroused and poised state, was associated with fewer complications (adjusted OR 0.63), shorter ICU stays, and lower mortality. The autonomic state at the transition into the case determined the outcome of the case.

Read that again. The clinician's autonomic state during the transition window predicted patient outcomes. Not their skill. Not their experience level. Their physiology at the moment of switching.

## Eighty-One Distractions Per Case

The environment makes transition failure worse. [[voity-2025-or-distractions-cognitive-load|Voity and colleagues (2025)]] observed cesarean deliveries and counted distractions. The mean was 81 per case. Severe distractions occurred in every single observed case. Zero cases were distraction-free. Cases with NICU admissions had higher distraction scores.

Eighty-one distractions per case means roughly one every 30 to 45 seconds. Each distraction is a forced micro-transition: attention gets pulled, state shifts, and the clinician must return to the prior cognitive posture. Most of these returns happen automatically and without awareness. But each incomplete return leaves a small autonomic residue. Over the course of a ten-hour day with five or six cases and hundreds of forced micro-transitions, those residues compound. By 1600, the clinician is operating on a system that has accumulated hours of incomplete transitions, and neither they nor anyone watching can see it.

This is the invisible degradation curve. It does not show up on any performance metric until it shows up as an error.

## Why We Train for the Event and Ignore the Transition

Clinical training is event-focused. We train for the difficult airway. We train for the cardiac arrest. We train for the anaphylaxis protocol. We simulate the crisis and score the response.

We almost never train the [[state-transition|transition]] between events. The three minutes between cases when the clinician walks from one OR to another. The sixty seconds between intubation and line placement. The shift from emergency mode to maintenance mode within the same case. These transitions are treated as dead time, administrative gaps, moments when nothing clinical is happening.

But the physiology does not agree. The nervous system does not have a pause button. When you walk from a room where you just managed a failed intubation to a room where a healthy patient is waiting for an elective procedure, your autonomic system is doing computational work the entire time. It is trying to downregulate sympathetic activation, restore parasympathetic tone, widen attentional aperture, and recalibrate threat assessment. That process takes a minimum of sixty to ninety seconds for amygdala deactivation alone, based on the neurophysiology of cortical override of limbic activation.

If you do not give that process space and structure, it does not complete. The sympathetic residue carries forward. The attentional narrowing persists. The threat calibration stays elevated. And you begin the next case in a physiological posture that does not match the clinical demand.

Thirty to forty natural transitions occur during a typical CRNA shift. Each one is a moment where the autonomic system either resets or fails to reset. Multiply incomplete resets across a shift, across a week, across a career, and you get the cumulative load that clinicians experience as burnout but that is more accurately described as chronic transition failure. This is the degradation curve that [[clinician-durability]] names and that [[gap-moment-training]] attempts to interrupt at the level of a single transition.

## The Transition as a Training Surface

Here is the reframe. If transitions are where errors concentrate, and the mechanism is autonomic rather than purely cognitive, then the transition itself becomes a training surface. Not a gap to fill with email or charting. A physiological event that can be structured, supported, and trained.

The minimum effective dose appears to be sixty seconds. That is the approximate time required for initial amygdala deactivation and dorsolateral prefrontal cortex reactivation. It is also the window within which a single structured breath practice (resonant frequency breathing at roughly 5.5 to 6 breaths per minute) produces a measurable shift in HRV, indicating parasympathetic re-engagement.

The question is not whether clinicians should meditate. That framing misunderstands the problem. The question is whether the autonomic transition between clinical events can be made more complete. Whether the residual sympathetic bleed that compounds across a shift can be interrupted at each transition point, the way a pilot runs a checklist between phases of flight.

This is what we are building at [[somnistics|Somnistics]] Research Labs. Not a relaxation tool. Not a mindfulness app that requires twenty minutes of quiet time that does not exist in a clinical workflow. A system that detects the transition, structures a sixty-second autonomic reset, and confirms that the reset completed before the clinician enters the next clinical context.

The technology layer, which we call [[neurogating|Neurogating]], watches biometric streams for the physiological signatures of transition points: HRV drops, heart rate spikes, respiratory rate changes, context shifts detected through movement patterns. When it detects a transition, it cues the intervention. When the intervention completes, it confirms the autonomic reset through the same biometric channels. Closed loop. No judgment required from the clinician about whether they need it. The physiology decides.

## Where This Goes

The Awtry data tells us that clinician autonomic state predicts patient outcomes. The Bordini data tells us that transition failures produce measurable harm. The Popov data tells us that the ability to transition between cognitive states is the largest differentiator between high and low clinical performance.

Put those together and you get a proposition that is uncomfortable for healthcare institutions built around competency-based training: the transition is the performance. Not the intubation. Not the drug calculation. Not the assessment. The switch between them. The moment when the nervous system either completes its reset or carries its residue forward.

We have trained clinicians for the events of their careers. We have not trained them for the spaces between those events. The physiology suggests that is exactly backward.

---

*You just finished a difficult case. The patient is stable. You are walking to the next room. Your hands are steady. Your thinking is clear, or at least it feels clear.*

*Your heart rate has not returned to baseline. Your breath is two cycles per minute faster than it was this morning. Your attentional field is narrower than you realize.*

*That walk is not dead time. It is the sixty seconds that determines how the next case goes.*
