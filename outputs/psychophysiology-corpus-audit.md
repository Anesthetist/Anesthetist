# Psychophysiology Corpus Audit

**Date:** 2026-04-17
**Phase:** 1 of 5 (per `outputs/psychophysiology-master-plan.md`)
**Method:** Automated scan across concepts/, evidence/, observations/ using extended regex per discipline. Canonical author coverage cross-referenced against evidence/ notes.

---

## Vault State Snapshot

| Layer | Count | Status Distribution |
|-------|-------|-------------------|
| Concepts | 186 | 48 canonical, 136 draft, 1 deprecated, 1 active |
| Evidence | 551 | 8 canonical, 118 review, 257 draft, 113 seedling, 31 captured, 18 seed |
| Observations | 370 | (not status-gated) |
| **Total vault-proper** | **1,107** | |

---

## Gap-Scored Discipline Matrix

Gap score = current coverage relative to target depth for that tier.
- Tier 1 target: 10 (full dissertation-chapter depth)
- Tier 2 target: 7 (half-chapter depth)
- Tier 3 target: 4 (survey/orientation depth)

### Tier 1 — Central (target: 10)

| # | Discipline | Files (C/E/O) | Total | Gap Score | Key Finding |
|---|-----------|--------------|-------|-----------|-------------|
| 1 | Autonomic neuroscience | 121/234/185 | 540 | **7/10** | Broadest coverage. Porges(14), Thayer(7). Needs canonical evidence promotion + systematic Porges corpus. |
| 2 | Cardiovascular psychophys | 93/169/150 | 412 | **6/10** | Strong operational coverage. Lehrer(4), Gevirtz(2), Laborde(3). Missing: systematic RSA/baroreflex/CVA literature. |
| 3 | Respiratory psychophys | 100/184/193 | 477 | **6/10** | Excellent SRL-original concepts (diaphragmatic blindness, BOLT). Missing: Buteyko corpus, McKeown, respiratory physiology textbooks. |
| 4 | Interoceptive neuroscience | 103/183/154 | 440 | **7/10** | Deepest single discipline. Craig(4), Critchley(4), Khalsa(2). Missing: Mehling (MAIA developer), Garfinkel (accuracy tasks), Murphy systematic review. |
| 5 | Clinical psychophys | 57/94/86 | 237 | **5/10** | Good product concepts. Missing: AAPB theoretical framework, Schwartz & Andrasik foundations, Yucha & Montgomery evidence base. |
| 6 | **Affective neuroscience** | **2/10/2** | **14** | **1/10** | **CRITICAL GAP.** Tier 1 discipline with near-zero vault presence. Barrett(2 notes), Panksepp(1), LeDoux MISSING. No constructed emotion theory, no emotion regulation deep dive, no affective science foundations. |
| 7 | Trauma neuroscience | 35/37/46 | 118 | **3/10** | SRL framing exists (trauma-informed-design canonical). VanDerKolk(1 note). Levine, Schore, Ogden all MISSING. No Somatic Experiencing coverage. |
| 8 | **Stress neuroendocrinology** | **13/23/21** | **57** | **2/10** | **CRITICAL GAP.** Selye(1), McEwen(3). No allostatic load deep dive, no Sterling & Eyer, no Sapolsky (Why Zebras). HPA axis barely touched. |
| 9 | Contemplative neuroscience | 68/89/86 | 243 | **4/10** | High file count but missing foundations. Davidson MISSING, Kabat-Zinn MISSING. SRL applications present but research canon absent. |

### Tier 2 — Supporting (target: 7)

| # | Discipline | Files (C/E/O) | Total | Gap Score | Key Finding |
|---|-----------|--------------|-------|-----------|-------------|
| 10 | Cognitive neuroscience | 21/35/14 | 70 | **2/7** | Scattered references, no systematic coverage. |
| 11 | **Embodied cognition** | **10/5/4** | **19** | **1/7** | Varela(1). Thompson MISSING. 4E cognition framework absent. |
| 12 | Predictive processing | 2/14/5 | 21 | **2/7** | Small but quality: Friston(4), Seth(3). Needs: Clark, active inference tutorial papers. |
| 13 | Sleep/chronobiology | 24/36/45 | 105 | **3/7** | Scattered. No Walker (Why We Sleep), no systematic sleep physiology. |
| 14 | **Exercise physiology** | **3/5/3** | **11** | **0/7** | **ABSENT.** No exercise psychophysiology coverage at all. |
| 15 | Pain psychophysiology | 2/18/12 | 32 | **1/7** | Moseley MISSING. No central sensitization framework. |
| 16 | **Health psychology** | **0/3/3** | **6** | **0/7** | **ABSENT.** |
| 17 | **Placebo/mind-body** | **3/2/1** | **6** | **0/7** | **ABSENT.** Kaptchuk MISSING, Benson MISSING. |
| 18 | Wearables/digital | 36/58/86 | 180 | **5/7** | Surprisingly thick (product-driven). Good for a Tier 2. |
| 19 | Time psychophysics | 18/36/23 | 77 | **5/7** | Deep single-author corpus: Wittmann(24). Strong for Tier 2. |

### Tier 3 — Survey (target: 4)

| # | Discipline | Files (C/E/O) | Total | Gap Score | Key Finding |
|---|-----------|--------------|-------|-----------|-------------|
| 20 | PNI/immunology | 3/4/1 | 8 | **0/4** | Absent. |
| 21 | Developmental psychobiol | 4/12/1 | 17 | **0/4** | Schore, Bowlby MISSING. |
| 22 | Social psychophysiology | 24/36/31 | 91 | **3/4** | Co-regulation concept canonical. Decent for Tier 3. |
| 23 | Psychopathology | 4/29/13 | 46 | **1/4** | Evidence exists but unstructured. |
| 24 | Pharmacology | 5/16/11 | 32 | **1/4** | Scattered. |
| 25 | Philosophy of mind | 46/82/40 | 168 | **3/4** | Surprisingly thick. Consciousness terms broadly present. |
| 26 | Psychosomatics history | 0/5/1 | 6 | **0/4** | Absent. |
| 27 | Cybernetics/systems | 11/16/30 | 57 | **2/4** | Wiener(4). Homeostasis terms present. |
| 28 | Somatic psychotherapy | 2/11/7 | 20 | **0/4** | No key authors. |
| 29 | Body cultivation | 10/12/14 | 36 | **1/4** | Yoga/qigong mentioned, not systematized. |
| 30 | Methods | 30/41/32 | 103 | **3/4** | EEG coverage decent. |

---

## Canonical Author Coverage

### Present in evidence/ (with note count)
Wittmann(24), Porges(14), Thayer(7), Craig(4), Critchley(4), Lehrer(4), Friston(4), Wiener(4), McEwen(3), Gross(3), Seth(3), Laborde(3), Damasio(2), Barrett(2), Khalsa(2), Gevirtz(2), Selye(1), Panksepp(1), Van der Kolk(1), Varela(1)

### MISSING from evidence/ (no dedicated notes)
**Tier 1 critical:** LeDoux, Levine, Schore, Davidson, Kabat-Zinn, Ogden
**Tier 2 important:** Thompson, Moseley, Kaptchuk, Benson, Clark (Andy)
**Tier 3 notable:** Bowlby, Bateson, Cannon, Gendlin, Pollan, Sapolsky

---

## Heat Map Summary

```
COVERAGE HEAT (vault files touching discipline)
██████████ D01 Autonomic (540)
█████████  D03 Respiratory (477)
████████   D04 Interoceptive (440)
████████   D02 Cardiovascular (412)
████░░░░░  D09 Contemplative (243)
████░░░░░  D05 Clinical Psychophys (237)
███░░░░░░  D18 Wearables (180)
███░░░░░░  D25 Philosophy Mind (168)
██░░░░░░░  D07 Trauma (118)
██░░░░░░░  D13 Sleep (105)
██░░░░░░░  D30 Methods (103)
█░░░░░░░░  D22 Social (91)
█░░░░░░░░  D19 Time (77)
█░░░░░░░░  D10 Cognitive (70)
█░░░░░░░░  D08 Stress Neuroendo (57)
█░░░░░░░░  D27 Cybernetics (57)
░░░░░░░░░  D23 Psychopathology (46)
░░░░░░░░░  D29 Body Cultivation (36)
░░░░░░░░░  D15 Pain (32)
░░░░░░░░░  D24 Pharmacology (32)
░░░░░░░░░  D12 Pred Processing (21)
░░░░░░░░░  D28 Somatic Psychother (20)
░░░░░░░░░  D11 Embodied Cognition (19)
░░░░░░░░░  D21 Developmental (17)
░░░░░░░░░  D06 Affective (14) ← TIER 1!
░░░░░░░░░  D14 Exercise (11)
░░░░░░░░░  D20 PNI (8)
░░░░░░░░░  D16 Health Psych (6)
░░░░░░░░░  D17 Placebo (6)
░░░░░░░░░  D26 Psychosomatics (6)
```

---

## Critical Gaps (priority order for Phase 3)

### Red-flag gaps: Tier 1 disciplines scoring below 3/10

1. **D06 Affective neuroscience (1/10)** — A Tier 1 discipline with less vault presence than most Tier 3 disciplines. Emotion is the bridge between interoception and behavior. Without this, the vault has sensation without meaning.

2. **D08 Stress neuroendocrinology (2/10)** — The HPA axis, allostatic load, and stress physiology underpin everything SRL does clinically. McEwen's allostasis framework and Sapolsky's chronic stress model are load-bearing for the CRNA use case.

3. **D07 Trauma neuroscience (3/10)** — Trauma-informed design is canonical but the science behind it is almost absent. Van der Kolk gets one note. Levine/Schore/Ogden: zero.

4. **D09 Contemplative neuroscience (4/10)** — Paradox: high file count from SRL applications but missing the research canon. Davidson's meditation neuroscience and Kabat-Zinn's MBSR evidence base are absent.

### Yellow-flag gaps: Tier 2 disciplines scoring 0-1/7

5. **D14 Exercise physiology (0/7)** — Totally absent. Exercise is a primary modality for autonomic regulation and a comparator for SRL interventions.

6. **D16 Health psychology (0/7)** — The behavioral medicine tradition is SRL's intellectual ancestor. Absent.

7. **D17 Placebo/mind-body (0/7)** — Kaptchuk, Benson, expectancy effects. Critical for understanding mechanism vs. context effects in biofeedback.

8. **D11 Embodied cognition (1/7)** — The theoretical foundation for why body-based interventions work. Varela gets one note.

---

## Phase 3 Execution Order (recommended)

Based on gap scores, tier importance, and dependency chains:

### Sprint 1: Fill Tier-1 critical gaps
1. D06 Affective neuroscience (1/10 → target 7+)
2. D08 Stress neuroendocrinology (2/10 → target 7+)
3. D07 Trauma neuroscience (3/10 → target 7+)
4. D09 Contemplative neuroscience (4/10 → target 7+)

### Sprint 2: Deepen Tier-1 strengths
5. D05 Clinical psychophysiology (5/10 → target 8+)
6. D01 Autonomic neuroscience (7/10 → target 9+)
7. D04 Interoceptive neuroscience (7/10 → target 9+)
8. D02 Cardiovascular psychophysiology (6/10 → target 8+)
9. D03 Respiratory psychophysiology (6/10 → target 8+)

### Sprint 3: Fill Tier-2 gaps
10. D14 Exercise physiology (0/7 → target 4+)
11. D17 Placebo/mind-body (0/7 → target 4+)
12. D16 Health psychology (0/7 → target 4+)
13. D11 Embodied cognition (1/7 → target 5+)
14. D12 Predictive processing (2/7 → target 5+)
15. D15 Pain psychophysiology (1/7 → target 4+)
16. D10 Cognitive neuroscience (2/7 → target 4+)
17. D13 Sleep/chronobiology (3/7 → target 5+)

### Sprint 4: Tier-2 maintenance + Tier-3 batch
18. D18 Wearables (5/7 — maintain)
19. D19 Time psychophysics (5/7 — maintain)
20-30. All Tier 3 disciplines in 3-4 batch sessions

---

## Canonical vs. Emerging Weighting Decision (deferred from Phase 0)

**Data-driven recommendation:** The vault is thin on canonical texts across most disciplines. Wittmann(24) is the exception — deep single-author coverage. Most canonical authors have 0-4 notes.

**Recommended weighting for Phase 3:**
- **Sprint 1 (filling gaps): 80/20 canonical/emerging.** Build the foundation first. Barrett, LeDoux, Panksepp, Selye, McEwen, Sapolsky, Van der Kolk, Levine, Schore, Davidson, Kabat-Zinn must all have foundational evidence notes before adding 2025-2026 papers.
- **Sprint 2 (deepening strengths): 50/50.** Foundation already exists; add recent meta-analyses and systematic reviews alongside canonical gaps.
- **Sprint 3-4 (Tier 2/3): 60/40 canonical/emerging.** Survey the field, emphasize landmarks.

---

## Notes on Methodology

- File counts measure *files mentioning* discipline terms, not dedicated files *about* that discipline. A concept about "Gap Moment Training" that mentions "autonomic" once is counted under D01. True discipline depth is therefore overestimated by these counts.
- Canonical author coverage is a stronger signal of real depth than file counts.
- Many vault files cross multiple disciplines — the autonomic-interoceptive-respiratory-cardiovascular cluster is tightly coupled, inflating all four counts from the same underlying content.
- Evidence status distribution (only 8 canonical out of 551) suggests the vault has breadth without quality gates. Evidence promotion should accompany new creation.
