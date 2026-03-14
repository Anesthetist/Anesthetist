---
id: "urn:srl:source:gdrive-deep-research-report"
type: source
title: "deep research report"
status: draft
creator: "Randy Graybeal"
created: 2026-02-15
imported: 2026-03-14
dc:source: "google-drive:deep-research-report.md"
---

# Best Substack + YouTube for OpenClaw Mac mini

## Executive summary
Baseline: `openclaw onboard --install-daemon`; bind loopback+token; remote via Tailscale Serve/SSH; never expose :18789. citeturn2search1 Scores=ASCP 0–5.

## Ranked Substack posts
1) entity["people","Robert H. Eubanks","substack author"] Feb26 L 5554 best+secure https://substack.com/home/post/p-187294099  
2) entity["people","Sid Saladi","substack author"] Feb26 M 4443 safety; stats vary https://sidsaladi.substack.com/p/openclawmoltbotclawdbot-101-the-complete  
3) entity["people","Aman Khan","substack author"] Feb26 M 4353 burners/WA; weak harden https://amankhan1.substack.com/p/how-to-get-clawdbotmoltbotopenclaw  
4) entity["people","Burgessing","substack author"] Feb26 S 4443 blast radius; not how‑to https://burgessing.substack.com/p/for-writers-a-cautionary-note-on  
5) entity["people","Paolo Perazzo","substack author"] Feb26 M 5434 arch/deploy https://ppaolo.substack.com/p/openclaw-system-architecture-overview  

## Ranked YouTube videos
1) entity["people","Ray Fernando","youtube creator"] Feb26 ~4h 4334 from‑zero https://youtu.be/7UmXs3z3Hks  
2) entity["organization","GamesPatch","youtube channel"] Feb26 26m 3244 walkthrough; sec ? https://youtu.be/hM8Fxfe8Nv4  
3) entity["people","Matthew Berman","youtube creator"] Feb26 ? 4345 “SAFE”; no port‑fw https://youtu.be/AWu68zRcHHk  
4) (same) Feb26 ? 4245 workflows https://youtu.be/Q7r--i9lLck  
5) pjiuQnEVges Feb26 ? 3233 VPS; no 18789 https://youtu.be/pjiuQnEVges  

## Checklist + best start
Default hw (→ M4 24/512). Do: install → daemon → verify bind=loopback+token. Remote: Tailscale Serve/SSH. Safety: pairing/allowlists, sandbox, exec approvals, disable mDNS. Backup: TM + `~/.openclaw` + workspace. Start: Eubanks + Ray. If stuck: hire freelancer.