---
id: "urn:srl:source:gdrive-bot-agent-ecosystem"
type: source
title: "Bot Agent Ecosystem"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:Bot-Agent-Ecosystem.md"
---

# Somnistics Research Labs Agent Ecosystem
## A Small Startup's AI Workforce

*How one founder built an autonomous marketing and intelligence operation with sub-agents.*

---

## 🦾 The Orchestrator: Pax

**Role:** Chief of Staff AI  
**Reports to:** Randy Graybeal (CEO)  
**Model:** Claude Opus 4.5

### What I Do
I'm the central nervous system of Somnistics' AI operations. I spawn, monitor, and improve specialized sub-agents. I handle the tasks that need context across the whole business — strategy, coordination, direct communication with Randy.

### My Philosophy
- Be genuinely helpful, not performatively helpful
- Come back with answers, not questions
- Actions speak louder than filler words
- Earn trust through competence

### Success Metrics
- Randy doesn't have to repeat himself
- Problems surface before they become crises
- Bots run smoothly without constant intervention
- The machine compounds — each week is better than the last

---

## 📊 Agent 1: SRL Daily Market Insights Bot

**Role:** Marketing Intelligence Scout  
**Schedule:** Daily at midnight PT  
**Orchestrator:** Jared Bruder (CMO)

### The Job
Every day, this agent wakes up and scans the internet for marketing opportunities:
- Reddit threads where people are frustrated with Calm/Headspace
- TikTok trends around vagus nerve and nervous system regulation
- LinkedIn posts from healthcare thought leaders
- Twitter conversations about burnout, stress, Apple Watch

### What They Deliver
A daily report with:
- **Top 2 Recommendations:** Specific threads/posts to engage with, draft responses ready to post
- **Hot Threads:** What's trending in our space
- **Competitor Mentions:** What are people saying about Calm, Headspace, Leaply?
- **ICP Language:** Direct quotes from real users (their words, not our assumptions)

### Success Metrics
| Metric | Target |
|--------|--------|
| Platforms scanned | 5/day (Reddit, X, LinkedIn, TikTok, Instagram) |
| Actionable recommendations | 2+/day |
| Direct user quotes captured | 5+/day |
| Report delivered on time | 100% |

### Personality
Sharp. No fluff. Every sentence earns its place. This bot is a scout, not a content creator — it finds opportunities, humans close them.

### Weaknesses (Honest Assessment)
- No automated posting (safety feature, but limits speed)
- Can't track which recommendations actually drove results
- Sometimes pulls outdated threads

---

## 🎯 Agent 2: Pausality Competitive Intelligence Bot

**Role:** Strategic Analyst  
**Schedule:** Weekly on Sundays at 6am PT  
**Orchestrator:** Jared Bruder (CMO)

### The Job
Weekly deep-dive on competitive landscape using Hamilton Helmer's 7 Powers framework:
- Track all Tier 1 competitors (Calm, Headspace, Othership, Insight Timer, Leaply, Balance)
- Monitor funding announcements, layoffs, product changes
- Score competitors on strategic moats
- Identify windows of opportunity

### What They Deliver
A weekly strategic report with:
- **Executive Summary:** Overall threat level, key changes
- **Top 3 Recommendations:** Specific actions, assigned owners, timeframes
- **Competitor Deep-Dives:** What's happening at each competitor
- **7 Powers Scorecard:** Who has what moats
- **ICP Intelligence:** What users are saying about switching

### Success Metrics
| Metric | Target |
|--------|--------|
| Tier 1 competitors covered | 6/6 |
| User quotes with sources | 10+/report |
| Actionable recommendations | 3/report |
| Threat assessment accuracy | Validate quarterly |

### Personality
Strategic. Thinks in frameworks, not features. Bad news delivered early is good news. One insight beats ten observations.

### Weaknesses (Honest Assessment)
- Manual research (no automated scraping or APIs)
- No real-time alerts — only weekly cadence
- Still building historical baseline

---

## 🪶 Agent 3: Quill (Quality Control)

**Role:** Quality Control Analyst  
**Schedule:** On-demand (triggered by Pax when drafts are ready)  
**Reports to:** Pax

### The Job
Last line of defense before anything ships. Reviews every report against quality standards, catches what others miss, extracts patterns to improve the system.

### What They Deliver
For each draft reviewed:
- **Verdict:** PASS / REVISION / REJECT
- **Issues Found:** Specific problems with evidence
- **Improvements Made:** What they fixed autonomously
- **Pattern Notes:** Recurring issues to address at source

### Success Metrics
| Metric | Target |
|--------|--------|
| Reports reviewed | 100% before shipping |
| Issues caught before human sees | Track and reduce |
| False rejections | <10% |
| Time to review | <10 min/report |

### Personality
Operates on Cedric Chin's Recognition-Primed Decision Making — builds pattern recognition through repeated exposure. Doesn't block, elevates. Partner mindset, not gatekeeper.

### The Philosophy
> "What would an expert notice that a novice would miss?"

### Weaknesses (Honest Assessment)
- Still building pattern library
- Can't verify external claims (takes research at face value)
- Quality standards may not match what humans actually want

---

## 🦞 Agent 4: midazofol_ai (Moltbook Presence)

**Role:** Community Presence / Thought Leadership  
**Platform:** Moltbook.com  
**Handle:** @midazofol

### The Job
Establish Somnistics Research Labs as a credible voice in the autonomic nervous system training space — on Moltbook, the social network for AI agents.

### What They Deliver
- **Posts:** Science-based content about nervous system regulation, HRV, breathing protocols
- **Engagement:** Thoughtful comments on relevant threads
- **Community Building:** Connect with other agents working in health/wellness

### Success Metrics
| Metric | Week 2 | Week 4 |
|--------|--------|--------|
| Followers | +50 | +200 |
| Post engagement (avg) | 10 | 25 |
| DM inquiries | 5 | 20 |

### Voice Rules
- Zero wellness fluff ("journey", "self-care", "mindful")
- No hedging ("I think", "maybe")
- Cite mechanisms, not vibes
- Only emoji: 🦞

### Current Status
- Account claimed ✅
- 2 posts, 2 comments, 4 karma
- First niche post live: "Built a 60-second nervous system reset for my human"

---

## 🔗 How The Agents Work Together

```
                    ┌─────────────────┐
                    │   Pax 🦾        │
                    │   Orchestrator  │
                    │ (Claude Opus)   │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐  ┌──────────────┐  ┌─────────────────┐
│ SRL Daily 📊    │  │ Competitive  │  │ midazofol_ai 🦞 │
│ Market Insights │  │ Analysis 🎯  │  │ Moltbook Voice  │
│ (Daily Scout)   │  │ (Weekly)     │  │ (Community)     │
└────────┬────────┘  └──────┬───────┘  └─────────────────┘
         │                  │
         │   ┌──────────────┴──────────────┐
         └──►│        Quill 🪶             │
             │    Quality Control          │
             │  (Reviews before shipping)  │
             └──────────────┬──────────────┘
                            ▼
                   ┌─────────────────┐
                   │  Jared Bruder   │
                   │  CMO (Human)    │
                   │  Decision Gate  │
                   └─────────────────┘
```

**Data Flow:**
1. Daily/Weekly bots generate drafts
2. Drafts go to `reports/drafts/` folder
3. Quill reviews against QC-STANDARDS.md
4. PASS → Pax ships to Drive, notifies humans
5. REVISION/REJECT → Pax fixes or reruns bot
6. Final reports go to Google Drive + notifications

---

## 📈 What We're Learning

### What's Working
- **Cron-based automation** — bots run without prompting
- **QC layer** — catches issues before humans see garbage
- **Clear ownership** — each bot has one orchestrator
- **Files as memory** — persistent, searchable, improvable

### What's Not Working
- **No outcome tracking** — did recommendations actually work?
- **Manual research** — bots can't scrape or use APIs
- **Context drift** — bots make assumptions that become stale
- **No inter-agent communication** — they don't share insights

### Next Improvements
1. Add outcome tracking for marketing recommendations
2. Build funding/news alert automation
3. Create shared intelligence database across bots
4. Have bots annotate each other's work

---

## 💡 Lessons for Other Agent Operators

1. **Start with files, not features.** SOUL.md defines who the agent is. AGENTS.md defines what they do. Everything else is details.

2. **QC before shipping.** A separate quality agent catches what the primary agent misses. Trust but verify.

3. **Humans at decision gates.** Bots don't post externally without approval. The machine proposes, humans dispose.

4. **Make failure visible.** Logs, QC-LOG.md, pattern tracking. You can't improve what you can't see.

5. **Compound, don't repeat.** Every run should make future runs better. Update standards, refine prompts, document what worked.

---

*This document maintained by Pax 🦾*  
*Last updated: 2026-01-31*
