# PubMed Systematic Literature Mining Plan

**Status:** Ready for execution in fresh session
**Created:** 2026-03-14
**Purpose:** Deepen the evidence layer (Layer 0) with peer-reviewed citations across all SRL concept domains

---

## PMIDs Already Captured (Need Metadata + Evidence Notes)

From successful PubMed searches before session dropped:

```
41391628, 40176306, 40386190, 41425202, 39943329, 37678565,
34586995, 39945155, 40201059, 35916600, 36075318, 30880101,
30735529, 24956066, 38981179
```

**Step 1:** `get_article_metadata` for all 15 PMIDs
**Step 2:** Create evidence/ notes for each relevant hit
**Step 3:** Link to existing concept notes via prov:wasDerivedFrom

---

## Search Plan: 7 Domains, ~35 Queries

### Domain 1: Breathing Physiology & Autonomic Regulation
Links to: resonant-breathing-frequency, vagal-tone, neurominute, minimum-effective-dose

```
resonance frequency breathing HRV biofeedback              (12 hits captured)
respiratory sinus arrhythmia vagal tone training
diaphragmatic breathing autonomic nervous system
extended exhale parasympathetic activation
CO2 tolerance breathing training performance
cyclic sighing mood physiological arousal
box breathing stress military clinical
```

### Domain 2: Interoception Science
Links to: interoception, anterocept, interoceptive-literacy, diaphragmatic-blindness, MAIA-2

```
interoception training insular cortex clinical              (6 hits captured)
MAIA-2 interoceptive awareness validation
heartbeat detection interoceptive accuracy
interoception emotional regulation clinical
insular cortex anterior posterior functional
interoceptive accuracy prediction emotional
body awareness training healthcare
```

### Domain 3: Clinician Wellness & Burnout
Links to: clinician-durability, neural-transition-failure, bandwidth-saturation, gap-moment-training

```
nurse anesthetist burnout resilience intervention           (2 hits captured)
healthcare worker burnout breathing intervention            (1 hit captured)
clinician wellness micro-intervention
perioperative stress CRNA anesthesia provider
second victim phenomenon healthcare support
anesthesia provider fatigue cognitive performance
nurse burnout prevention brief intervention
```

### Domain 4: Polyvagal & Vagal Stimulation
Links to: polyvagal-theory, vagal-tone, co-regulation, neurogating

```
polyvagal theory breathing intervention                     (1 hit captured)
non-invasive vagus nerve stimulation breathing
vagal tone HRV biofeedback clinical trial
respiratory vagal nerve stimulation review
vagal tone social engagement co-regulation
neuroception safety autonomic
```

### Domain 5: Biofeedback & Wearables
Links to: neurogating, readyscore, sensor-fusion, HRV-deprecation

```
Apple Watch HRV accuracy clinical validation
wearable biofeedback stress intervention
real-time HRV biofeedback mobile app
consumer wearable autonomic monitoring
photoplethysmography HRV accuracy comparison ECG
pupillometry cognitive load wearable
```

### Domain 6: Neuroplasticity & Training
Links to: neuro-ouroboros, anterocept, kosha-architecture, awareness-before-technique

```
breathing training neuroplasticity cortical thickness
mindfulness insular cortex gray matter
brief intervention neuroplasticity dose-response
micro-practice spaced repetition neuroplasticity
frequency duration mindfulness dose response
```

### Domain 7: Advanced Meditation & Consciousness
Links to: consciousness-engineering, self-remembering, harvard-neuroskill-integration

```
meditation jhana neural correlates fMRI
cessation consciousness EEG meditation
heartbeat evoked potential meditation depth
non-dual awareness neuroscience
advanced meditation autonomic nervous system
meditation training variables intensity
```

---

## Citations Referenced in Vault But Missing Evidence Notes

These are mentioned in observation notes but don't have their own evidence/ files yet. Look up via `lookup_article_by_citation`:

| Author | Year | Topic | Priority |
|--------|------|-------|----------|
| Dillard et al. | 2023 | Slow breathing + VR active shooter | High |
| Yuan & Silberstein | 2016 | Vagus nerve stimulation (2-part) | High |
| Ferentzi et al. | 2022 | Heartbeat counting (Trends Cog Sci) | High |
| Keizer et al. | 2010 | Gamma neurofeedback + cognitive binding | High |
| Mehling et al. | 2012 | MAIA original validation | High |
| Mehling et al. | 2018 | MAIA-2 validation | High |
| Laborde et al. | 2022 | HRV and stress physiology | Medium |
| Gerritsen & Band | 2018 | Respiratory vagal stimulation | Medium |
| Holzel et al. | 2011 | Mindfulness + gray matter changes | Medium |
| Prinsloo et al. | 2011 | Immediate HRV biofeedback effects | Medium |
| Gevirtz | 2013 | HRV biofeedback meta-evidence | Medium |
| Goessl et al. | 2017 | HRV training autonomic flexibility | Medium |
| Shalev et al. | 2017 | Early intervention prevents PTSD | Medium |
| Walker | 2009 | Sleep + emotional regulation | Medium |
| Tang et al. | 2019 | Neuroplasticity from interoceptive training | Medium |
| Schechter et al. | 2010 | Breathing instruction for clinicians | Low |
| Paul, Elam & Verhulst | 2007 | Breathing reduces test anxiety | Low |
| Lehrer et al. | 2020 | HRV biofeedback meta-analysis | High |
| McEwen & Gianaros | 2011 | Chronic stress + neuroplasticity | Medium |
| Brosschot et al. | 2006 | Perseverative cognition hypothesis | Low |

---

## Execution Protocol

For each search:
1. Run `search_articles` with query + date filter
2. Run `get_article_metadata` on returned PMIDs
3. Filter for SRL-relevant papers (breathing, interoception, HRV, burnout, vagal, wearable, neuroplasticity)
4. Create evidence/ note for each relevant paper with Dublin Core metadata
5. Link to concept notes via prov:wasDerivedFrom
6. Run `find_related_articles` on highest-value PMIDs to discover adjacent literature
7. For key papers, attempt `get_full_text_article` via PMC for clinical interpretation

Target: **50+ new evidence notes** to bring the evidence layer to parity with the concept and observation layers.

---

## Current Evidence Layer Status

- 27 evidence notes exist (11 review, 16 draft)
- ~20 citations referenced in observations but lacking evidence notes
- Harvard/Sacchet Lab 15 notes need DOIs added
- Target after mining: 75-100 evidence notes with full Dublin Core metadata
