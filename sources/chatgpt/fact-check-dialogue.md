---
id: "urn:srl:chat:chatgpt-fact-check-dialogue"
type: chat-import
title: "Fact check dialogue"
status: draft
created: 2025-09-13
imported: 2026-03-14
platform: chatgpt
dc:source: "chatgpt-export:68c5c1c0-28fc-8325-ba57-e6d40e1581f9"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: 6
char_count: 18636
---
# Fact check dialogue

**Date:** 2025-09-13 | **Messages:** 6 | **~4659 tokens**

## Key Takeaways

- *Pending extraction*

## Extracted Nodes

- *Pending extraction*

---

## Transcript

**Randy:**

Fact check, cross check the above entire dialogue; from the beginning, step
By step. Role: auditor

---

**ChatGPT:**

Here’s a tight, auditor-style fact check of the dialogue you shared (through Sep 13, 2025 PT). I mark items as:
- ✓ internally consistent / self-reported
- ! internal contradiction or math/date error
- ? needs external evidence to verify

I also separate **Descriptive (reported facts/claims)** vs **Prescriptive (plans/intent/design)** where relevant.

# Executive summary
- **Top issues (fix first):**
  1) **Pausality launch date** is contradictory across threads. (!)  
  2) **Early-momentum metrics** (downloads, conversion, revenue) don’t math out. (!)  
  3) **Regulatory-safe language**: several passages flirt with outcome claims; keep these descriptive and sourceable. (?)
- **Overall**: Many statements are reasonable but **lack documentary evidence** (App Store/LinkedIn exports, emails, calendar entries). Create a single “Evidence Packet” (see end) to lock these down.

# Key contradictions & math checks
1) **Launch date**  
   - 2025-09-09 post says “**10 days post-launch**,” implying launch ~**Aug 30–Sep 1, 2025**.  
   - Another thread says “**We released the app on 10/18/25**,” then immediately “**This is incorrect.**”  
   - **Status:** **! Contradiction.** Decide and document the actual first public availability date (App Store Connect “First Available” + TestFlight dates).

2) **Early metrics** (2025-09-09)  
   - **Claims:** “**88 downloads**, **13.9% conversion**, **$140 proceeds at $35 per paying user**,” and “**4.72 sessions per active device**.”  
   - **Math check:** $140 / $35 = **4 paying users**. 4 / 88 = **4.55% conversion**, **not 13.9%**.  
   - **Status:** **! Internal math error.** Recompute or correct inputs (define whether “downloads” = installs; “conversion” = trial→paid or visitor→paid; timeframe).

3) **“10 days post-launch” vs sessions/usage window**  
   - Sessions (“4.72 per active device”) has no timeframe and no definition of “active.”  
   - **Status:** ? Needs definition + analytics export.

4) **CRNA Facebook group = 12,500 (~20% of CRNAs)**  
   - Implies total CRNAs ≈ 62,500. Historically plausible but needs a current source.  
   - **Status:** ? Needs external verification (membership count + current national CRNA total).

5) **Seattle Times meeting “tomorrow at 11”** (dated context around 2025-09-10–12)  
   - **Status:** ? Verify via calendar/email.

6) **Mayo Clinic engagement (Michael Thorne), ARNP innovation challenge, research/Ventures**  
   - Narrative is plausible. **Status:** ? Needs email/notes/calendar corroboration + follow-ups documented.

7) **Titles/roles (e.g., Chair of WANAC Wellness Committee; subscriptions; domains owned)**  
   - **Status:** ? Needs proof (org confirmation, receipts, WHOIS/purchase receipts).

# Step-by-step cross-check (by conversation clusters)
**1) 2025-09-09 “6-month board report / exec analysis”**  
- **Desc:** CEO/board reports requested; stage-setting for strategy. ✓  
- **Presc:** Rewrites, perspective shifts requested. ✓  
- **Notes:** No factual claims to verify

*[message truncated — full text in source]*

---

**Randy:**

Yes. Define what these are. Think Soc2 prep

---

**ChatGPT:**

Got it. I’ll treat this like SOC 2 prep — so **definitions are tight, unambiguous, and auditable**. Each metric needs:  
- **Definition** (how it’s calculated)  
- **Source of record** (system / report)  
- **Frequency** (how often measured)  
- **Control check** (how to verify integrity)  

Here’s a draft “Metrics Definitions v1.0”:

---

# 📊 Pausality Metrics Dictionary (SOC 2 Prep)

## 1. **Download**
- **Definition:** A completed install of the Pausality app from the App Store (initial install event, not including re-installs on same device).  
- **Source of Record:** App Store Connect → Sales and Trends → Units.  
- **Frequency:** Daily roll-up.  
- **Control Check:** Compare App Store Connect units vs. Firebase/Amplitude install events. Flag variance >2%.

---

## 2. **Active Device**
- **Definition:** A unique device that opens the app at least once during the measurement window (day/week/month).  
- **Source of Record:** Firebase Analytics → `user_engagement` event, deduplicated by `device_id`.  
- **Frequency:** Daily, Weekly, Monthly.  
- **Control Check:** Cross-check with App Store active device trend. Variance >5% triggers review.

---

## 3. **Session**
- **Definition:** A continuous period of user interaction with the app beginning with an `app_start` event and ending after 30 minutes of inactivity (industry standard).  
- **Source of Record:** Firebase/Amplitude → `session_start` events.  
- **Frequency:** Daily aggregation.  
- **Control Check:** Spot-check session counts per user against raw logs.

---

## 4. **Sessions per Active Device**
- **Definition:** Average number of sessions per active device in a defined time window.  
- **Formula:** `Total Sessions ÷ Active Devices`.  
- **Source of Record:** Firebase/Amplitude aggregated dashboards.  
- **Frequency:** Weekly.  
- **Control Check:** Confirm denominator matches Active Device definition.  

---

## 5. **Conversion Rate**
- **Definition:** % of unique installs that result in a paid subscription.  
- **Formula:** `(Paying Users ÷ Installs) × 100`.  
- **Clarification:** Install = first-time app download; Paying User = unique Apple ID with active subscription.  
- **Source of Record:** RevenueCat (subscription events) + App Store Connect (units).  
- **Frequency:** Weekly.  
- **Control Check:** Reconcile RevenueCat subscriber count with App Store Connect subscriber report. Variance >1% triggers review.  

---

## 6. **Paying User**
- **Definition:** A unique Apple ID with at least one active paid subscription during the measurement window.  
- **Source of Record:** RevenueCat Subscriber List.  
- **Frequency:** Daily snapshot.  
- **Control Check:** Verify subscriber receipts are valid and not expired.  

---

## 7. **Proceeds**
- **Definition:** Net revenue after Apple’s platform fee (15% or 30%, depending on eligibility).  
- **Formula:** `Gross Sales – Apple Commission – Taxes`.  
- **Source of Record:** App Store Connect → Payments and Financial Reports.  
- **Frequen

*[message truncated — full text in source]*

---

**Randy:**

Role prompt engineer.

Create a soc2 prep role for SRL in anticipation of b:b sales.

Operational excellence

---

**ChatGPT:**

Here’s a **role definition prompt** you can drop into your SRL playbook. It’s written in a way that works both as an internal job description and as a reusable “prompt role” you can activate with me or other AI assistants.  

---

# 🛡️ SOC 2 Prep Role – Somnistics Research Labs (SRL)

**Role Title:** SOC 2 Prep & Compliance Engineer  
**Domain:** Operational Excellence / Risk & Trust Layer  
**Context:** SRL is scaling from consumer pilots into **B2B healthcare + enterprise sales**, where trust, security, and compliance are mandatory. SOC 2 readiness is both a sales enabler and a credibility signal.  

---

## 🎯 Purpose
- Anticipate and design **SOC 2 Type I → Type II readiness**.  
- Build **repeatable, evidence-backed controls** across security, availability, processing integrity, confidentiality, and privacy.  
- Translate complex compliance frameworks into **operational excellence rituals** that reinforce trust without slowing innovation.  

---

## 📌 Responsibilities
1. **Framework Alignment**
   - Map SRL systems (App Store Connect, Firebase, RevenueCat, Supabase, ClickUp, GDrive, Slack) to SOC 2 Trust Service Criteria.  
   - Maintain an evolving **Controls Matrix** (what, why, owner, evidence).  

2. **Metrics & Evidence**
   - Define all SRL **business-critical metrics** (downloads, conversion, paying users, ARPPU, uptime, error rate).  
   - Attach each metric to a **system of record + evidence packet** (screenshot, export, signed PDF).  

3. **Policies & SOPs**
   - Draft lightweight but **audit-grade policies** for:  
     - Access control & onboarding/offboarding  
     - Change management & version control  
     - Incident response & escalation  
     - Data retention & privacy  
   - Store policies in Notion/GDrive with **version history + approvals**.  

4. **Controls Automation**
   - Automate evidence capture (monthly exports, log snapshots).  
   - Maintain **Metrics Log Spreadsheet** (Metric, Value, Source, Evidence Link, Reviewer, Status).  
   - Integrate with ClickUp automations for reminders and task closure.  

5. **B2B Sales Enablement**
   - Maintain a **SOC 2 Readiness Deck** for enterprise buyers (overview of controls, roadmap, evidence packet).  
   - Be the internal **RFP/InfoSec questionnaire first responder**.  

6. **Audit Prep**
   - Run quarterly **mock audits**: sample controls, pull evidence, ensure traceability.  
   - Maintain “**Single Source of Truth Binder**” (read-only GDrive folder with signed PDFs/exports).  

---

## ✅ Acceptance Criteria (Unit Tests)
- **UT-01:** Every external metric has a definition + evidence artifact.  
- **UT-02:** Access logs exist for all core systems; last 90 days are retrievable.  
- **UT-03:** Policies are versioned, signed, and accessible within 2 clicks.  
- **UT-04:** Quarterly mock audit completed; gaps remediated <30 days.  
- **UT-05:** Sales team has a one-pager SOC 2 readiness statement and can answer basic InfoSec questions.  

---

## 🧭 Success Criteria
- SRL ca

*[message truncated — full text in source]*

---

