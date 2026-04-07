---
created: '2026-04-05'
creator: Vigil (automated lint cycle)
dc:subject:
- vault-health
- knowledge-management
- quality-assurance
- polyvagal-audit
id: urn:srl:observation:vault-lint-report-2026-04-05
modified: '2026-04-05'
status: review
title: SRL Vault Lint Report — 2026-04-05
type: observation
---

# SRL Vault Lint Report — 2026-04-05

**Librarian:** Vigil (automated weekly cycle)
**Scope:** Full vault audit — all note types, all statuses

---

## 1. Vault Stats

| Type | Total | Canonical | Review | Draft | Other |
|------|-------|-----------|--------|-------|-------|
| Concepts | 150 | 32 | 12 | ~105 | 1 active |
| Evidence | 485 | 1 | 105 | 214 | 165 (seedling/captured/seed) |
| Observations | 327 | 0 | 30 | 250 | 47 (seed/active/captured/current) |
| Audiences | 12 | 0 | 1 | 11 | 0 |
| Outputs | ~15 | 0 | 5 | ~10 | 0 |
| Unknown type | 12 | 0 | 0 | 12 | 0 |

**Total notes: ~1,000+.** 12 notes have type "unknown" and need classification.

## 2. Pipeline Health

Review queue has 12 concepts — manageable, not blocked. Most are infrastructure/meta-framework notes. Recommend batch-promoting controlled-vocabulary-v1, faceted-classification-taxonomy, evidence-grading-framework, vault-architecture-v2 to canonical since they are operational.

Nonstandard statuses detected: vigil-soul-randy-cognitive-model ("active"), plus evidence notes in "captured", "seedling", "seed", "reviewed", "current" statuses outside the standard pipeline.

## 3. Orphans

All 32 canonical concepts have SKOS relationships — no canonical orphans. Four concepts lack broader parents and should be linked: autonomic-regulation, hemispheric-rebalancing, polyvagal-theory, titration-to-effect.

## 4. Under-Evidenced Canonical Concepts

Most canonical concepts are well-supported (20-80+ evidence links). Two flagged:
- **Kosha Architecture** (8 links) — thin, needs contemplative science evidence
- **Titration to Effect** (5 links) — thin, needs pharmacology/dose-response evidence

## 5. Stale Content

Six preprints (medRxiv/bioRxiv from 2025) should be checked for journal publication. Weekly digests accumulating — consider archival policy.

## 6. Duplicate Candidates

**4 confirmed evidence duplicates** requiring immediate merge: grossman-2026 pair, nondual-awareness pair, jhana fMRI pair, ELIA scale pair.

**Concept overlaps:** career-longitudinal-gmt ↔ gmt-career-arc (merge); 4 consilience concepts (consolidate to 2); somnistics ↔ somnistics-category-definition (clarify relationship).

## 7. PVT Audit (URGENT)

The polyvagal-theory canonical note has evidence links to both the Grossman critique and Porges response, BUT the body text does not mention the scientific debate. It presents PVT as established fact. **Action: Add "Scientific Debate (2026)" section.** Five additional notes flagged for PVT caveat updates.

## 8. Tag Hygiene

"polyvagal" tag severely under-applied (2 notes tagged vs 90+ referencing PVT). "autonomic-regulation" (44 notes) and "interoception" (63 notes) have good coverage. 12 notes need type assignment.

## 9. Top 10 Recommended Actions

1. [URGENT] Update polyvagal-theory body with debate section
2. [URGENT] Merge 4 confirmed evidence duplicates
3. [HIGH] Batch-promote 4 infrastructure concepts to canonical
4. [HIGH] Add PVT debate caveat to review-status notes
5. [HIGH] Merge career-longitudinal-gmt into gmt-career-arc
6. [MEDIUM] Strengthen evidence for Kosha Architecture and Titration to Effect
7. [MEDIUM] Add broader links to 4 rootless canonical concepts
8. [MEDIUM] Assign types to 12 "unknown" notes
9. [LOW] Check 6 preprints for journal publication
10. [LOW] Systematic "polyvagal" tag application
