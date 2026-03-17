---
title: "Pausality Presentation Skill Specification"
type: output
status: draft
dc.creator: Claude
dc.date: 2026-03-14
dc.subject:
  - somnistics
  - brand-design-system
  - presentation-tooling
  - pausality
source: "LLM output imported from Downloads"
---

# /pausality-presentations Skill — Transfer Description

Purpose: Generates on-brand Pausality / Somnistics Research Labs presentation content.
Encodes the official design system so output is pixel-accurate to Tony's Google Slides templates.

## Design System

Colors:
- Deep Navy: #22253A
- Soft Sage: #5FC89B  
- Off-white: #F5F5F0

Font: Poppins only
- Regular (400) headers
- Light (300) body
- tracking: -0.025em
- line-height: 1.25

Gradient (logo only): 45deg, #3A61AD → #1479B6 → #5FC89B → #96F0BE

EKG/heartbeat watermark on every slide (~5% white opacity dark, ~8% navy opacity light)

No em-dashes, no accent lines under titles, icons standalone sage-colored (not in circles)

## Universal Slide Rules

- Slide 1 = brand title only (logo lockup, nothing else)
- Slide 2 = deck title left + Apple Watch right (never rotated)
- All text left-aligned — no centered text
- Bullet content always inside a card/box — no naked bullets
- Team photos = rounded squares (not circles), ~8-12px radius
- End slide = contact left column, logo or Watch right — not centered
- Apple Watch asset placed as-is, never transformed

## Bundled Assets

- 8 logo SVG variants (gradient/white/black, horizontal/vertical/wordmark-only)
- appleWatch.png — section divider product shot
- Founder headshots: Randy (randy-bio-2.jpg), Jason (jason-bio-2.jpg)
- Full Poppins and Figtree font families

## Output Modes

- .pptx file (via pptx skill + python-pptx)
- HTML mockup at 1920x1080px (screenshot → paste into Google Slides)
- Layout guide (text specs for Tony to build directly in Google Slides)

## Source Documents

- Pausality_Branding.pdf
- Enterprise_Deck__SRL__Pausality.pdf
- Investor_Deck__SRL__Pausality_FINAL.pdf

Skill sub-files: design-system.md, slide-templates.md, content-library.md
