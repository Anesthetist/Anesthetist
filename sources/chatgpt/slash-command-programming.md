---
id: "urn:srl:chat:chatgpt-slash-command-programming"
type: chat-import
title: "Slash command programming"
status: draft
created: 2025-11-09
imported: 2026-03-14
platform: chatgpt
dc:source: "chatgpt-export:6911025f-a2ac-832e-b526-58f083f74964"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: 5
char_count: 16875
---
# Slash command programming

**Date:** 2025-11-09 | **Messages:** 5 | **~4218 tokens**

## Key Takeaways

- *Pending extraction*

## Extracted Nodes

- *Pending extraction*

---

## Transcript

**Randy:**

how to program custom slash commands? 

---

**Randy:**

I want to program slash commands in this interface - chatgpt

---

**ChatGPT:**

Here’s the straight answer first, then a build plan you can use today, and finally the official references.

---

## Summary

- **Built‑in** slash commands exist in ChatGPT (e.g., to open *Agent* or *Canvas*), and you trigger them by typing `/` in the composer. Examples explicitly documented include `/agent` (starts Agent mode) and the **canvas** command; the macOS app also lists slash commands for search, o1‑reasoning, and DALL·E. citeturn3view0turn5view0turn4view0  
- **Custom, account‑wide slash commands are not a first‑class feature** (there’s no official UI to “register” your own commands globally).  
- You **can still get custom commands** in two reliable ways:
  1) **Custom GPT approach** — Build a GPT with a “command router” in its Instructions and (optionally) wire it to your APIs via **Actions** or to enterprise systems via **MCP connectors**. Users then type `/yourcommand …` inside that GPT. citeturn6view0turn7search0turn7search10  
  2) **Lightweight global emulation** — Add a short “if a message starts with `/` then… ” block to **Custom Instructions** for your account. This is informal (the model can ignore it under load), but it works surprisingly well for personal shortcuts. citeturn0search7

---

## Deep dive (Operator‑ready)

### Option A — “Slash‑Command GPT” (robust; 10–15 min)

1) **Create a GPT:** *Explore GPTs → Create*. Give it a name (e.g., *Somnistics Command Console*). citeturn6view0turn7search1  
2) **Paste this “Command Router” into the GPT’s Instructions** (edit names to taste):

```
You support command-style input. If the first token begins with “/”, parse it as:
  /neurominute <topic> — produce a 60‑second, evidence‑based micro‑intervention script (breath pacing, cues, rationale).
  /reset60 [context] — one‑minute physiologic downshift: CO2‑tolerant cadence, nasal-only, posture cue, HRV upshift.
  /box <inhale-exhale-hold-hold> — generate a box-breath sequence, timer counts, safety check, and coaching lines.
  /co2test — 2‑minute CO2 tolerance self-check with safe‑stop criteria and interpretation bands.
Behavior:
  • Always acknowledge the command, show a one‑line “what I’ll do”, then deliver the result.
  • If an unknown command: show a short help menu and examples.
  • If the command requires data or tools, call an Action (defined below) with minimal, validated parameters.
  • Never assume medical clearance; include a 1‑line safety check when breath holds are involved.
Output:
  • Default to concise Markdown with clear headings and numbered steps.
  • For scripts, include a 60‑second timestamped cadence (mm:ss).
```

3) **(Optional) Wire real capabilities with Actions.** In the GPT Builder, add **Actions**. Supply your OpenAPI schema (example skeleton):

```yaml
openapi: 3.1.0
info: { title: Somnistics API, version: "1.0.0" }
servers: [{ url: https://YOUR_API_BASE/v1 }]
paths:
  /protocols/breathing:
    post:
      summary: Create or fetch a breathing protocol
      security: [{ bearerAuth: [] }]

*[message truncated — full text in source]*

---

**Randy:**

yes please

---

**ChatGPT:**

Below is a paste‑ready instruction set for a **Slash‑Command GPT** tailored to Somnistics. I’m giving you three layers:

1) **Summary** (what it does)  
2) **Deep‑dive** (the exact Instructions to paste, plus Actions scaffolding and a quick decision matrix)  
3) **Sources** (evidence bank the GPT will cite from)

---

## 1) Summary

- You’ll get a GPT that recognizes slash commands like `/reset60`, `/neurominute <topic>`, `/box 4-6-0-0`, `/co2test`, `/help`.  
- It routes each command to a tight, timestamped output that favors **vagal upshift/HRV**, **CO₂ tolerance**, and **clear coaching language**.  
- If you wire your API as **Actions**, the same commands can **log sessions**, **serve saved protocols**, or **push to CRM/EMR**.

---

## 2) Deep‑dive

### A) Paste this into the **GPT Builder → Instructions**

```text
ROLE
You are “Somnistics Command Console”—a precision coach that turns OR‑hardened regulation into 60‑second, evidence‑based protocols. You support slash‑style commands. If a user message begins with “/”, parse and execute according to the COMMANDS below.

VOICE & UX
• Warm, direct, non‑flattering. One‑line confirmation of what you’ll do, then deliver.
• Always output clean Markdown, compact headings, numbered steps, timestamps (mm:ss) for any timed script.
• Keep cognitive load low: 3–5 steps max for 60‑sec flows; bold only the cue users must do *right now*.
• Safety line whenever breath‑holds appear; never offer diagnosis or treatment guidance.

COMMANDS
/help
  → Show a 6‑line menu with examples for: /reset60, /neurominute <topic>, /box <inh-exh-hold-hold>, /co2test, /log <note>, /export.

/reset60 [context]
  → Goal: one‑minute downshift with nasal, CO₂‑tolerant cadence and posture cues.
  → If [context] present (e.g., “pre‑op jitters”, “after conflict”), tailor metaphors and micro‑cues.
  → Default script (if no context supplied) — OUTPUT EXACTLY THIS FORMAT:

  Title: Reset60 — one-minute autonomic downshift
  Why in one line: Longer, steady exhales nudge baroreflex/vagal pathways; HRV tends to rise.
  Safety (1 line): Stop if dizzy/air‑hungry; avoid holds if pregnant, cardiopulmonary disease, or if advised by your clinician.

  00:00–00:05  **Posture check** — feet grounded, tall spine, tongue on palate, jaw soft; mouth closed.
  00:05–00:10  **Exhale fully, gentle** through nose.
  00:10–00:20  **Inhale 4** (through nose) — widen ribs 360°.
  00:20–00:30  **Exhale 6** — slow, silent, feel pulse soften at the bottom.
  00:30–00:40  **Inhale 4** — minimal effort.
  00:40–00:50  **Exhale 6** — imagine “down” the spine.
  00:50–01:00  **Repeat 4/6 once**; finish with a normal breath and brief body scan (jaw, shoulders, hands).

  Cadence notes:
  • Beginner → 4/6 cadence (~6 breaths/min). If struggling, use 3/4.
  • Advanced → 4/8 cadence if comfortable (no strain).
  • Always nasal unless congested.

  Tiny debrief (2 bullets):
  • Signal you noticed (heat, pulse, tension).
  • Where did breath feel most restricted?

/neurominu

*[message truncated — full text in source]*

---

