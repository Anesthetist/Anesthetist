---
id: "urn:srl:chat:chatgpt-srl-branding-strategy-guide"
type: chat-import
title: "SRL Branding Strategy Guide"
status: draft
created: 2025-05-01
imported: 2026-03-14
platform: chatgpt
dc:source: "chatgpt-export:6813e6a3-010c-8010-b2bb-08a8403a0ec4"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: 2
char_count: 7549
---
# SRL Branding Strategy Guide

**Date:** 2025-05-01 | **Messages:** 2 | **~1887 tokens**

## Key Takeaways

- *Pending extraction*

## Extracted Nodes

- *Pending extraction*

---

## Transcript

**Randy:**

SRL builds 1 minute biofeedback based tools (app) on the IOS and Apple Watch. The Flow Collective, Shiftadapt.com are some of my influences (and competitors). We are building our brand and considering the branding elements of our competitors.   Let's make this a first replit project: 

---

**ChatGPT:**

Below is a **battle-tested starter kit** you can paste straight into a brand-new **Python-flavoured Replit**.  
It does three things:

1. **Scrapes & snapshots** key branding signals (tag-lines, primary copy blocks, hero images) from your two closest comparators—**SH//FT / Shift Adapt** and **Flow Research Collective**.  
2. **Extracts colour palettes** from those hero images and stores them in JSON so you can eyeball the chromatic territory they already occupy.  
3. **Generates a skeletal SRL style-guide** (Markdown) and a one-page HTML landing prototype so your designers and copywriters have a living canvas to play with.

---

## 1 Quick “Why” & Positioning Take-aways

| Brand | Core Promise | Tone/Voice | Visual Feel | Notable Device |
|-------|--------------|-----------|-------------|----------------|
| **SH//FT (Shift Adapt)** | *“Master your breath. Your performance. Your recovery. YOURSELF.”* | Athletic coach, challenge-oriented | High-contrast black/white plus a single neon accent; bold slash glyph “SH//FT” | **Diagnostic funnel (Exhale Test)** that drags users into the product funnel first thing. citeturn2view0 |
| **Flow Research Collective** | *“We help leaders and their teams reach their potential through harnessing the power of flow state.”* | B2B scientific-authority, data heavy (+500 %, +600 %) | Tech-gradient blues/purples over charcoal; wide sans-serif; lots of stat cards | **Quant graphs** & marquee client logos to social-proof. citeturn4view0 |
| **The Flow Collective** (Maisie Hill) | Menstrual-cycle literacy & community | Empathic, peer support | Warm terracotta & neutrals; lower-contrast serif/sans mix | **Community stories** & coaching podcasts. citeturn6search0 |

**White-space for SRL** → *Clinical-grade precision + 60-second “press-play” practicality.*  
Lean into *“one-minute neuro-spike”* positioning, **hospital-clean cobalt + calming coral** palette, and copy that balances authority (your 40 k clinical hours) with invitation (“Borrow my nervous-system for 60 seconds”).  

---

## 2 Repo Layout

```
srl-brand-intelligence/
├─ .replit              # runs `python main.py`
├─ replit.nix           # handles pip installs (requests, beautifulsoup4, pillow, colorthief)
├─ README.md            # project purpose & quick-start
├─ main.py              # CLI entrypoint
├─ scripts/
│   ├─ fetch_assets.py  # grabs HTML + hero imgs
│   └─ extract_palette.py
├─ data/
│   ├─ competitors.json # structured copy & colour data
│   └─ palettes/
│       ├─ shiftadapt.png
│       └─ flowresearch.png
├─ docs/
│   ├─ competitor_analysis.md
│   └─ srl_style_guide.md
└─ web/
    ├─ index.html       # SRL landing stub
    └─ styles.css
```

### .replit
```toml
run = "python main.py"
```

### replit.nix
```nix
{ pkgs }: {
  deps = [
    pkgs.python311Full
    pkgs.python311Packages.requests
    pkgs.python311Packages.beautifulsoup4
    pkgs.python311Packages.pillow
    pkgs.python311Packages.colorthief
  ];
}
```

### main.py (excerpt)
```

*[message truncated — full text in source]*

---

