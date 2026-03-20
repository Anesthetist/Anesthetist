---
id: urn:srl:output:linkedin-nurse-execs-agentic-ai
type: output
title: "LinkedIn Post: The Missing Agent at HIMSS"
status: draft
creator: Randy Graybeal
created: 2026-03-19
modified: 2026-03-19
output_type: creative
target_audience: urn:srl:audience:investor
prov:wasDerivedFrom:
  - urn:srl:concept:closed-loop-biofeedback
  - urn:srl:concept:in-shift-mental-hygiene
  - urn:srl:concept:clinician-durability
  - urn:srl:concept:gap-moment-training
---

# LinkedIn Post: The Missing Agent at HIMSS

**Audience:** Nurse executives, CNOs, nursing informatics leaders returning from HIMSS 2026
**Tone:** Clinical peer, not vendor. Descriptive, not prescriptive. Framework, not pitch.
**Length:** ~600 words (LinkedIn optimal)

---

## POST

**The agent nobody built at HIMSS.**

You just spent four days in Las Vegas hearing about agentic AI. The pitch was consistent: autonomous agents handling revenue cycle, scheduling, documentation, claims — the administrative load that crowds out care.

Good. That work matters.

But here's what I noticed was missing from every exhibit hall demo and every main stage keynote:

Not a single agent was watching the clinician.

We built agents to chart. Agents to code. Agents to schedule and triage and summarize. We built agents that listen to the patient's voice, the patient's labs, the patient's imaging.

Nobody built an agent that asks: what is happening in the nurse's nervous system right now?

**The data says this matters.**

62% of CRNAs report burnout. $56,000 per nurse in turnover costs. $9 billion a year — not in care delivery, but in losing the people who deliver it. And the primary barrier clinicians cite isn't workload. It's that they have no tools for real-time recovery during the shift.

We've been solving the wrong problem. We've been giving clinicians wellness apps to use before and after work. Meditation programs for the quiet room. EAP referrals after the critical incident.

The shift itself — the 12 hours where autonomic dysregulation actually happens — remains unaddressed.

**What an agent for the clinician could look like.**

Imagine an architecture where:

The wearable your nurse already owns detects a heart rate pattern consistent with acute stress — not at the end of the shift, but between cases, during a turnover, in the 30-second gap before the next intubation.

An inference layer classifies the autonomic state: hyperarousal, cognitive tunnel, recovery window.

A 60-second protocol — breath-paced, biofeedback-guided, adapted to that clinician's physiology in real time — is delivered through the same device. No app to open. No session to schedule. No quiet room to find.

The clinician's heart rate drops. Measurably. In under a minute. They return to the next case regulated, not depleted.

That's a closed-loop system. Sense → classify → intervene → measure → adapt. The same architecture we're building for revenue cycle and clinical decision support — applied to the human being inside the workflow.

**The technical pieces exist.**

- Wearable biometrics: Apple Watch, Garmin, WHOOP — streaming HRV, heart rate, respiratory rate
- Open APIs: platforms like Open Wearables (Momentum) now unify 300+ devices through a single integration, with FHIR mapping for EHR interoperability
- On-device ML: Apple Neural Engine runs inference locally — no PHI leaves the device
- Evidence base: Six Dijkstra, Soer, McCraty et al. (2019) validated a 1-minute paced breathing HRV protocol on 877 workers — proving 60 seconds is a sufficient physiological window. You, Laborde et al. (2021) showed that 5 minutes of slow-paced breathing at resonant frequency produces the same cardiac vagal activation as 20 minutes — the dose-response curve is flat. Lehrer, Vaschillo & Vaschillo's foundational work on resonant frequency breathing established the mechanism. Garfinkel et al. (2015) gave us the interoceptive accuracy framework that makes measurement possible.

The science is not new. Porges' Polyvagal Theory, Thayer & Lane's neurovisceral integration model, Damasio's somatic marker hypothesis — these researchers built the foundation decades ago. What's new is that wearable sensors and on-device ML can now operationalize their work inside a clinical workflow — where the intervention has to be 60 seconds, silent, and invisible to the patient.

**The question for nurse executives.**

You're evaluating AI investments for the next budget cycle. You're looking at ambient documentation, clinical decision support, predictive analytics. All important.

But consider this: what is the ROI on a system that reduces turnover by helping clinicians regulate their nervous systems during the shift — not after it?

The documentation agent saves time. The scheduling agent saves money. The clinician regulation agent saves people.

I'd argue that's the agent worth building next.

---

*Randy Graybeal, CRNA — Co-founder, Somnistics Research Labs. 28 years in the OR. Building the intervention layer that wearables are missing. Standing on the shoulders of Porges, Lehrer, Thayer, Damasio, Garfinkel, Mehling, and every researcher who proved the body keeps the score — and that the body can learn to change it.*

---

## HASHTAGS

#NursingLeadership #HIMSS26 #AgenticAI #ClinicalAI #NurseWellbeing #HealthcareAI #ClinicianBurnout #HRV #Biofeedback #NursingInformatics #DigitalHealth #WorkforceRetention

## NOTES FOR RANDY

- This follows the Communication Philosophy: descriptive landscape first, SRL positioning last
- No prescriptive language — "consider this" not "you should"
- The technical section establishes credibility without selling
- The closing positions SRL without naming the product — the curious will click through
- Six named researchers/research teams attributed in the evidence section
- Closing byline names the foundational scientists explicitly — credibility through attribution
- "The agent nobody built" hook lands because it's true — Becker's and SiliconAngle both confirm agentic AI at HIMSS was administrative, not clinical wellness
- The attribution signals: we didn't invent the science, we're operationalizing decades of validated research
