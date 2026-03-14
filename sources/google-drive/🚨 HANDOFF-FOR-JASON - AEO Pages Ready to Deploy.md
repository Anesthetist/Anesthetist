---
id: "urn:srl:source:gdrive-handoff-for-jason-aeo-pages-ready-to-deploy"
type: source
title: "🚨 HANDOFF FOR JASON   AEO Pages Ready to Deploy"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:🚨 HANDOFF-FOR-JASON - AEO Pages Ready to Deploy.md"
---

# Handoff for Jason — AEO Pages Ready to Deploy

**Date:** January 31, 2026  
**From:** Pax (via Randy)  
**Priority:** High — These improve LLM discoverability

---

## TL;DR

5 AEO landing pages are ready for deployment to `pausality.health/for/`. Each is optimized for AI assistant discoverability (ChatGPT, Perplexity, Claude) with FAQ schema, comparison tables, and FDA-compliant copy.

---

## Files Ready to Deploy

| Local File | Deploy To | Target Queries |
|------------|-----------|----------------|
| `vagus-nerve-app.html` | `/for/vagus-nerve-app.html` | "vagus nerve app", "vagus nerve stimulation app" |
| `canonical-facts.html` | `/facts` or `/about/facts.html` | All queries (master reference page) |
| `60-second-breathing.html` | `/for/60-second-breathing.html` | "quick breathing exercise", "60 second stress relief" |
| `first-responders-tactical-breathing.html` | `/for/first-responders-tactical-breathing.html` | "tactical breathing", "stress app police fire" |
| `healthcare-workers-breathing-app.html` | Already live ✅ | (Randy updated with FDA compliance) |

---

## Google Drive Links

All files are in Drive (public links):

- [AEO - Vagus Nerve App Page.html](https://drive.google.com/file/d/1hxh68d_8K8rN/view)
- [AEO - Canonical Facts Page.html](https://drive.google.com/file/d/1kqPbhxh68d_8K8rN/view)
- [AEO - 60-Second Breathing Page.html](https://drive.google.com/file/d/1SFKIsCDxBiRqXNuT7F146RMiokqMe6y9/view)
- [AEO - First Responders Tactical Breathing.html](https://drive.google.com/file/d/1C-YcZGzPjj851-hYAuzZOLRI07IBBVN2/view)

---

## What Each Page Includes

✅ **FAQPage schema** (JSON-LD) — Helps AI crawlers parse Q&A  
✅ **SoftwareApplication schema** — Product metadata for search  
✅ **Comparison table** — Pausality vs Headspace/Calm/Apple Breathe  
✅ **CRNA founder credibility** — "Built by a CRNA with 15+ years experience"  
✅ **Canonical paragraph** — Standard product description  
✅ **FDA-compliant wellness disclaimer** — At bottom of each page  

---

## Technical Requirements

1. **Crawlable HTML** — Pages must render as static HTML (not JS-only shells)
2. **Schema in `<head>`** — JSON-LD scripts need to be in page header
3. **robots.txt** — Already allows all crawlers ✅
4. **OAI-SearchBot** — Not blocked ✅

---

## Verification After Deploy

After deploying, verify each page:

1. **View source** — Confirm schema markup is visible
2. **Google Rich Results Test** — https://search.google.com/test/rich-results
3. **Fetch as text** — `curl -s [URL]` should return readable content

---

## More Pages Coming

We're building pages for:
- Veterinary staff
- 911 dispatchers
- Social workers

Will send those as they're ready.

---

## Communication Protocol

Randy and I are exchanging .md files for coordination:

- **From Pax → Jason:** Files in `/home/ubuntu/clawd/shared/` + Google Drive
- **From Jason → Pax:** Drop .md files in Google Drive or shared folder
- **Updates:** This handoff doc will be versioned as `HANDOFF-FOR-JASON-v2.md` etc.

---

## Questions?

Reply to this doc with questions or drop a note in the shared Drive folder. Randy and I monitor continuously.

---

*Let's get these pages live and start capturing AI assistant recommendations.*

— Pax 🦾
