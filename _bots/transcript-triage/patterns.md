# Transcript Triage Bot — Pattern Library

Accumulated heuristics for fast, accurate classification. Updated after every retrospective.

## Title Patterns

*Patterns discovered from file titles that predict category and value*

| Title Pattern | Likely Category | Likely Score | Confidence | Added |
|--------------|----------------|-------------|------------|-------|
| *populated after first retrospective* | | | | |

## Size Heuristics

| Char Range | Typical Content | Default Score Adjustment |
|-----------|----------------|------------------------|
| <5K | Single question or definition request | -2 (unless title signals novel concept) |
| 5K-20K | Focused exchange, often single topic | 0 (neutral) |
| 20K-100K | Multi-topic session, moderate depth | +1 |
| 100K-300K | Deep working session, likely concept development | +2 |
| >300K | Marathon session — high depth but also high noise | +1 (diminishing returns) |

## Message Count Heuristics

| Messages | Typical Pattern | Score Adjustment |
|----------|----------------|-----------------|
| 1-3 | One-shot Q&A — usually low extraction value | -1 |
| 4-10 | Focused exchange — moderate value | 0 |
| 10-30 | Working session — likely iterative development | +1 |
| 30-100 | Deep session — strong concept development likely | +2 |
| >100 | Marathon — mixed quality, but high-value sections exist | +1 |

## Auto-Skip Patterns

*Files that can be classified without reading content*

| Pattern | Action | Reason |
|---------|--------|--------|
| *populated after first retrospective* | | |

## Auto-Prioritize Patterns

*Files that should always score 8+*

| Pattern | Reason |
|---------|--------|
| Title contains a trademarked SRL term (Gap Moment, NeuroMinute, Anterocept, etc.) | Likely concept development |
| Title contains "novel concept" or "new concept" | Definitionally high-value |
| *more patterns added after retrospectives* | |

## Anti-Patterns (False Positives)

*Patterns that look high-value but aren't*

| Pattern | Why It's a False Positive |
|---------|--------------------------|
| *populated after first retrospective* | |

---

*Last updated: initial creation — no retrospectives yet*
*Pattern count: 0 discovered, 4 seed heuristics*
