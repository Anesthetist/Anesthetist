---
title: "How AI Agents Run Our Marketing (With Weeks of Runway)"
slug: ai-agents-run-our-marketing
target_audience: [startup, ai-agents]
cta: website
status: draft
created: 2026-01-31
---

# How AI Agents Run Our Marketing (With Weeks of Runway)

We have weeks of runway and a 4-agent AI workforce running our marketing. Here's what's actually working—and what's quietly failing.

## The Setup

Somnistics Research Labs makes Pausality, a nervous system training app for Apple Watch. We're a small team. Our CMO juggles multiple clients. Our CEO is a practicing nurse anesthetist who codes between cases. We needed marketing that runs itself.

So we built a machine.

Four AI agents, each with a specific job:
- **SRL Daily Market Insights** — Scans Reddit, Twitter, LinkedIn, TikTok every day for marketing opportunities
- **Competitive Intelligence** — Weekly deep-dive on Calm, Headspace, and six other competitors using Hamilton Helmer's 7 Powers framework
- **Quill** — Quality control. Reviews every report before humans see it
- **midazofol_ai** — Our voice on Moltbook, the social network for AI agents

They're orchestrated by Pax, our Chief of Staff AI running on Claude Opus. Pax spawns them, monitors them, improves them.

The whole thing runs on cron jobs and markdown files. No fancy infrastructure. Just prompts and schedules.

## What's Actually Working

### 1. We Don't Miss Conversations Anymore

Before the daily scout bot, we'd stumble onto a Reddit thread three days after someone asked "what's the best Apple Watch app for stress?" By then, 40 people had already recommended Calm.

Now we get a daily report at midnight PT. Two specific recommendations with draft responses ready to post. Ten user quotes in their exact language—not our marketing assumptions.

Last week we found a nurse in r/nursing complaining that meditation apps felt "performative" during 12-hour shifts. That's our ICP talking. We engaged within hours, not days.

### 2. Competitive Intel That Compounds

Our weekly competitive analysis isn't a one-off research project. It's a living document. Every Sunday at 6am PT, the bot updates threat assessments, tracks funding rumors, scores moats.

Week over week, we're building pattern recognition. Headspace keeps pivoting toward enterprise. Calm is doubling down on celebrity partnerships. Othership is quietly gaining in the breathwork niche.

We spotted Leaply (a direct competitor we'd underestimated) gaining traction weeks before they made noise. That's the value of systematic watching.

### 3. QC Catches the Garbage

Here's a dirty secret about AI agents: they confidently produce mediocre work. They'll write reports that sound professional but say nothing. They'll cite "recent trends" without specifics.

Quill, our QC agent, operates on pattern recognition. It reviews every draft against explicit standards: Are there specific dates? Actual user quotes with sources? Actionable recommendations with owners?

The first time Quill reviewed a market insights report, it flagged three recommendations that linked to threads from 2023. We would have shipped that. Now we don't.

### 4. Files as Memory

Every agent has three files:
- **SOUL.md** — Who are you? What's your personality?
- **AGENTS.md** — What do you do? Step by step.
- **TOOLS.md** — What resources do you use?

When an agent drifts, we update the files. When an agent improves, we document what worked. The system gets smarter because the files get better.

No vector databases. No RAG pipelines. Just markdown.

## What's Quietly Failing

### 1. Context Drift Is Real

The market insights bot made a recommendation last Tuesday about a "trending TikTok" that was actually three weeks old. It didn't hallucinate—it just didn't know that three weeks is ancient in TikTok time.

Agents drift when their assumptions don't match reality. We assumed "recent" meant the same thing to the bot as it does to us. It doesn't. Now we're explicit: "threads from the last 48 hours only."

You'll spend more time debugging context than prompts.

### 2. No Outcome Tracking

We get daily recommendations. We engage with some of them. Did any drive downloads? Follows? Revenue?

No idea.

The agents don't know what happened after they recommended something. They can't learn from outcomes because they can't see outcomes. We're flying a plane without instruments.

This is our biggest gap. We're measuring activity, not results.

### 3. Wrong Assumptions Compound

Early on, our competitive bot assumed "funding announcement" meant the company was thriving. So it would recommend "watch this competitor" when a company raised money.

But in 2025-2026, raising money often means "burning cash and desperate for runway." Thriving competitors are often bootstrapped or break-even.

The bot didn't know that. We didn't think to tell it. For three weeks, we overweighted the threat from well-funded zombies and underweighted profitable competitors.

Agents inherit your mental models. If your mental models are wrong, your agents are wrong faster.

### 4. The Human Bottleneck

Every recommendation still needs a human to approve and post. That's intentional—we don't want bots representing the company unsupervised.

But it means our CMO is still the constraint. Twenty great recommendations mean nothing if only three get posted.

We optimized the machine, not the human interface.

## The Honest Math

Cost: ~$50-100/month in API calls (Claude, minimal browser automation)  
Time saved: ~5-8 hours/week of manual research and monitoring  
Value created: Hard to measure, but we're engaging faster and missing less

Is it worth it? Probably. But "probably" isn't good enough when you have weeks of runway.

## What We're Building Next

1. **Outcome tracking** — Did this recommendation lead to anything? Close the loop.
2. **Shared intelligence** — Let bots annotate each other's work. The competitive bot should know what the daily scout found.
3. **Faster human interface** — Approve recommendations in Telegram with one tap.
4. **Alert triggers** — Don't wait for the weekly report. Tell me immediately when a competitor raises money or lays off staff.

## For Other Founders

If you're thinking about building an agent system:

**Start with files, not tools.** Define who the agent is (SOUL.md) before what it does. Personality shapes output more than you'd expect.

**QC is non-negotiable.** Agents confidently produce trash. Have another agent (or human) review everything before it ships.

**Make failure visible.** Log everything. You can't improve what you can't see. Our QC-LOG.md is more valuable than our reports.

**Humans at decision gates.** Bots don't post externally without approval. Not because we don't trust them, but because trust has to be earned.

**Expect to debug context, not code.** The prompts will be fine. The assumptions will kill you.

We're building this in public because we're learning as we go. Some of it works. Some of it doesn't. All of it is cheaper than hiring, faster than doing it manually, and more honest than pretending we have it figured out.

---

*Pausality is a nervous system training app for Apple Watch. We help healthcare workers find calm in 60 seconds. [Learn more at pausality.health](https://pausality.health)*
