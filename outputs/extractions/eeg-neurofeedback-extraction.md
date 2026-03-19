# EEG & Neurofeedback Extraction Report

**Miner:** SRL Knowledge Miner
**Date:** 2026-03-18
**Files processed:** 7
**Signal-to-noise ratio:** ~12% Randy / 88% ChatGPT (heavily technical-support and ChatGPT-elaboration weighted)

## Source Files

| # | File | Date | Messages | Signal Level |
|---|------|------|----------|-------------|
| 1 | `eeg-data-streaming-setup.md` | 2023-05-26 | 28 | Medium — Randy's intent is high-signal; technical debugging is noise |
| 2 | `crna-neurofeedback-dmn-control.md` | 2025-04-26 | 6 | Medium — Randy's DMN framing is strong; ChatGPT pitch output is noise |
| 3 | `theta-and-delta-eeg-patterns.md` | 2023-04-05 | 4 | High — Randy asks a novel question about dopaminergic exhaustion risk |
| 4 | `vns-effects-on-alpha-oscillations.md` | 2023-05-19 | 8 | High — Randy's neurophysiology critique of auricular VNS is expert-level |
| 5 | `vitarka-vicara-synthesis.md` | 2025-06-21 | 10 | Very High — Randy's Iyengar/McGilchrist synthesis + "I spend all my time touching the core of being" |
| 6 | `brainwave-visualization-apps.md` | 2024-06-03 | 4 | Medium — social coherence EEG concept is high-signal |
| 7 | `mac-eeg-visualization-tools.md` | 2024-11-15 | 2 | Low — pure tool research, no conceptual content |

## Conversation Arc Summary

These 7 files trace Randy's EEG/neurofeedback journey from 2023-2025:

1. **2023-04**: First explores theta/delta dominance risks — asking about dopaminergic exhaustion for someone pursuing full-time nondual awareness via breathwork. This is remarkably early signal of his nondual clinical awareness concept.
2. **2023-05**: Sets up Muse 2 + Mind Monitor OSC streaming pipeline to his MacBook. Simultaneously explores VNS effects on alpha oscillations with expert neurophysiology reasoning about auricular VNS and nucleus basalis.
3. **2024-06**: Researches Muse-compatible visualization apps (Myndlift, Mind Monitor, Opti Brain). Asks ChatGPT to build a Python program for **5-person group EEG social coherence detection** — a direct precursor to the coherence-field concept.
4. **2024-11**: Continues Mac EEG tool research. Mentions "extra lead setup" with Mind Monitor — indicating hardware experimentation beyond stock Muse.
5. **2025-04**: Applies neurofeedback to CRNA DMN control — framing the shift from "suppress DMN" to "control when DMN is active." Names Pausality for the first time.
6. **2025-06**: Deepest session — synthesizes Iyengar's vitarka/vicara with McGilchrist's hemispheric model and asks for biometric protocols with EEG markers (alpha-theta crossover, gamma binding). Declares "I spend all my time touching the core of being."

---

## New Concept Candidates

### 1. `eeg-data-pipeline` (Observation, not Concept)

**Recommendation:** Extract as **observation** (type: `craft-knowledge`), not concept. This is Randy's personal EEG toolchain, not an atomic idea.

```yaml
id: urn:srl:observation:eeg-data-pipeline
type: observation
title: "Randy's EEG Data Pipeline: Muse 2 + Mind Monitor + OSC Streaming"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
dc:subject: ["eeg", "personal-practice", "biofeedback", "data-pipeline", "muse", "mind-monitor"]
observation_type: craft-knowledge
clinical_context: "Personal biofeedback practice and research platform"
years_of_evidence: 3
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-eeg-data-streaming-setup
  - urn:srl:chat:chatgpt-mac-eeg-visualization-tools
  - urn:srl:chat:chatgpt-brainwave-visualization-apps
skos:related: ["neuroharmonics", "closed-loop-biofeedback", "multimodal-sensor-fusion"]
```

**Body (Randy's voice only):**

Randy uses a Muse 2 headset paired with the Mind Monitor app on iPad for real-time EEG visualization. The pipeline streams data via OSC (Open Sound Control) protocol to a MacBook for processing. He has explored "extra lead setup" configurations beyond stock Muse placement, indicating hardware experimentation.

The toolchain:
- **Muse 2** — consumer-grade 4-channel EEG headset (TP9, AF7, AF8, TP10)
- **Mind Monitor** — iOS/iPad app for real-time EEG visualization and OSC data streaming
- **OSC streaming** — UDP port 5000, Node.js server receiving real-time brainwave data
- **Visualization research**: Evaluated Myndlift, Muse Direct, BrainWave, EEGLAB, OpenBCI GUI, NeuroPype, Brainstorm, Visbrain

Randy's intent: use live EEG output as a visual background for online meetings — making internal states visible in professional contexts. This is an early expression of his commitment to making the invisible (autonomic state) visible.

**Attribution:** Randy's words: "I am a researcher with 20 years of clinical anesthesia experience"; "I pair a Muse2 headset with the Mindmonitor app on the iPad to get a rudimentary real-time eeg visualization"; "Compatible with mind monitor extra lead setup."

---

### 2. `dmn-voluntary-control` (New Concept)

**Confidence:** Medium — Randy framed the concept but ChatGPT did most of the elaboration. The key insight is Randy's.

```yaml
id: urn:srl:concept:dmn-voluntary-control
type: concept
title: "DMN Voluntary Control"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
version: 0.1
dc:subject: ["neuroscience", "default-mode-network", "neurofeedback", "attention", "clinical-performance"]
dc:source: ["chatgpt-export:680cd196-6bf8-8010-833c-44e0a25126ed"]
skos:broader: ["nondual-clinical-awareness"]
skos:narrower: []
skos:related: ["attention-as-gain-control", "neurogating", "gamma-state-binding", "embodied-metacognition"]
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-crna-neurofeedback-dmn-control
```

**Body (Randy's voice):**

The ability to voluntarily modulate Default Mode Network activity — not suppressing it entirely, but controlling **when** it is active. Randy frames the DMN as neither purely good nor purely bad:

> "The DMN isn't always bad. It's also involved in creative thinking and problem-solving. So, perhaps the aim isn't to completely suppress it but to learn to control when it's active."

For CRNAs, an overactive DMN during a case means mind-wandering and attention lapses in a surgical environment where those lapses can be fatal. But between cases, DMN activity supports pattern integration, creative problem-solving, and recovery.

The neurofeedback pathway: real-time EEG monitoring allows CRNAs to see when their DMN is active and practice techniques to quiet it when clinically necessary. This builds on years of mindfulness meditation (Randy notes the CRNA archetype "has been using the Waking Up app for years") as a foundation.

**Clinical interpretation:** Pending review.

**Relationship to existing concepts:**
- `nondual-clinical-awareness` (broader) — NCA is the target state; DMN voluntary control is the trainable mechanism
- `attention-as-gain-control` — DMN modulation is a specific expression of attention gain control
- `neurogating` — the gating mechanism that selectively allows or suppresses DMN during clinical work

---

### 3. `vitarka-vicara-integration` (New Concept)

**Confidence:** High — this is a rich Randy-directed synthesis. Randy prompted the entire framework and explicitly endorsed it ("This!").

```yaml
id: urn:srl:concept:vitarka-vicara-integration
type: concept
title: "Vitarka-Vicara Integration (Castle-Field Vision)"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
version: 0.1
aliases: ["Castle-Field Vision", "front-back brain integration"]
dc:subject: ["somnistics", "novel-concept", "yoga-philosophy", "hemispheric-integration", "iyengar", "mcgilchrist", "eeg-correlates"]
dc:source: ["chatgpt-export:68572aff-d1d8-8010-945b-e161d5e83ac8"]
skos:broader: ["hemispheric-rebalancing"]
skos:narrower: []
skos:related: ["neuroharmonics", "polyanchora", "neurogating", "gamma-state-binding", "nondual-clinical-awareness", "attention-as-gain-control"]
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-vitarka-vicara-synthesis
```

**Body (Randy's voice):**

Randy's original synthesis prompt: "Describe in McGilchrist terms Iyengar's idea synthesizing the front and back of brain vitarka and vicara. He uses the analogy of visiting a medieval castle — your eyes may appear to focus on what's in front of them, while your awareness takes in the whole immense volume of the surrounding space. He describes this as holistic meditative vision."

**Vitarka** = deliberate placing of attention (left-hemisphere, dorsal attention network, foveal focus). **Vicara** = effortless spreading of awareness (right-hemisphere, default-mode/salience networks, panoramic field). The integration is not toggling between them but holding both simultaneously — the stone's texture vivid **within** the echoing vastness.

**EEG correlates identified:**
- Occipital alpha widening during peripheral-vision expansion
- Alpha-theta crossover as signature of holistic meditative vision
- Cross-frequency coupling: gamma nested in alpha/theta
- HRV coherence rise as embodied confirmation of the integrated state

**Somnistics cue architecture (endorsed by Randy):**
1. Anterocept anchor — foveal focal point
2. Polyanchora peripheral gate — right-hemisphere bias, peripheral vision shimmer
3. NeuroGating depth pulse — front-back brain integration via brainstem-occiput connection
4. Vagal sweep — 6-count exhale, full spatial awareness
5. Sonic phase interference — binaural center/surround separation

**Physiological markers:** Ocular muscle softening, ~20% peripheral field gain, rMSSD uptick within 3-4 breaths, alpha-theta crossover.

**Randy's level-4 practitioner status:** "I spend all my time touching the core of being." Places him at Iyengar's highest engagement level — right-hemispheric presence as ontological backdrop, not occasional visitor.

**Clinical interpretation:** Pending review.

---

### 4. `alpha-theta-crossover` (New Concept)

**Confidence:** Medium — referenced as a measurable EEG marker across multiple files. Important as a biomarker concept linking several existing concepts.

```yaml
id: urn:srl:concept:alpha-theta-crossover
type: concept
title: "Alpha-Theta Crossover"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
version: 0.1
dc:subject: ["eeg", "biomarker", "neurofeedback", "meditation", "state-transition"]
dc:source: ["chatgpt-export:68572aff-d1d8-8010-945b-e161d5e83ac8"]
skos:broader: ["neuroharmonics"]
skos:narrower: []
skos:related: ["gamma-state-binding", "state-transition", "vitarka-vicara-integration"]
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-vitarka-vicara-synthesis
```

**Body:**

The moment when theta power (4-8 Hz) exceeds alpha power (8-12 Hz) during a meditation or breath practice — a measurable EEG signature of the transition from relaxed-alert awareness into deep meditative or hypnagogic states.

In the Castle-Field Vision protocol, alpha-theta crossover is the "Seal" confirmation marker: when combined with pupil constriction >= 0.3mm, it indicates the practitioner has achieved the integrated vitarka-vicara state.

**SRL relevance:**
- A concrete, measurable EEG biomarker that can validate whether somnistics practices actually produce the intended state shifts
- Trackable via Muse S headband at 256 Hz sampling in research contexts
- Distinct from gamma-state-binding (which indicates peak integration) — alpha-theta crossover marks the **entry** into deep states

**Clinical interpretation:** Pending review.

---

### 5. `social-coherence-eeg` (New Concept)

**Confidence:** High — this is directly from Randy's request to build a multi-person EEG system.

```yaml
id: urn:srl:concept:social-coherence-eeg
type: concept
title: "Social Coherence EEG"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
version: 0.1
dc:subject: ["eeg", "social-coherence", "co-regulation", "group-neurofeedback", "somnistics"]
dc:source: ["chatgpt-export:03bccd97-3bfb-4e2d-bdfd-4f4e03e3b04c"]
skos:broader: ["co-regulation"]
skos:narrower: []
skos:related: ["coherence-field", "neuroharmonics", "multimodal-sensor-fusion"]
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-brainwave-visualization-apps
```

**Body (Randy's voice):**

> "Let's build a program, in Python, to collect real-time streaming data from 5 participants from each user's Muse 2 + Myndlift output and display the averages, highlighting when social coherence occurs in the group."

Randy envisions multi-person simultaneous EEG monitoring where the system detects and highlights moments of **social coherence** — when participants' brainwave patterns synchronize. This is the neurophysiological substrate of co-regulation made visible.

**Technical architecture (Randy's spec):**
- 5 simultaneous Muse 2 headsets streaming via Lab Streaming Layer (LSL)
- Real-time averaging of brainwave frequencies across participants
- Coherence detection algorithm highlighting group synchronization events
- Python-based (muse-lsl + numpy + matplotlib + scipy)

**SRL application:** Group NeuroMinute sessions where coherence between participants is measured in real-time — turning co-regulation from a felt experience into a quantified, visible phenomenon.

**Clinical interpretation:** Pending review.

---

## Concept Enrichments

### E1. Enrich `neuroharmonics` — Add EEG Data Pipeline Context

**What to add:** Randy's personal Muse 2 + Mind Monitor practice is the **empirical source** for NeuroHarmonics development. The existing note describes the three-layer architecture but doesn't mention that Randy is personally running real-time EEG data during his practice sessions. Add to `prov:wasDerivedFrom`:
- `urn:srl:chat:chatgpt-eeg-data-streaming-setup`

**Body addition:** "Randy personally uses a Muse 2 + Mind Monitor pipeline to observe his own brainwave patterns during coherence breathing + binaural beat sessions. This first-person EEG data informs the NeuroHarmonics frequency architecture."

---

### E2. Enrich `gamma-state-binding` — Add Alpha-Theta Context

**What to add:** The vitarka-vicara synthesis file provides concrete EEG markers that contextualize gamma binding within a progression: alpha-theta crossover marks **entry** to deep states, gamma binding marks **peak** integration. Add `skos:related`:
- `vitarka-vicara-integration`
- `alpha-theta-crossover`

---

### E3. Enrich `hemispheric-rebalancing` — Add Iyengar/Vitarka-Vicara Framework

**What to add:** The existing note cites McGilchrist but not Iyengar's vitarka-vicara model, which provides the yogic language for the same hemispheric integration. Randy explicitly bridged these in the vitarka-vicara session. Add:
- `skos:narrower: ["vitarka-vicara-integration"]` — vitarka-vicara is a specific expression of hemispheric rebalancing
- New evidence source: Iyengar's castle metaphor
- Body addition: "Iyengar's vitarka (deliberate attention placement) maps to left-hemisphere dorsal attention network function; vicara (effortless awareness spreading) maps to right-hemisphere default-mode/salience network function. The medieval castle analogy — eyes focused on stone texture while awareness fills the entire vaulted space — is a practitioner's description of hemispheric integration."

---

### E4. Enrich `closed-loop-biofeedback` — Add EEG as Optional Sensor

**What to add:** The existing note mentions "optionally electrodermal/neural signals" but doesn't specify EEG. Randy's Muse 2 pipeline is the concrete EEG implementation. Add to body: "Optional EEG via Muse S at 256 Hz for research-grade correlation; alpha-theta crossover and gamma coherence as validation markers."

---

### E5. Enrich `nondual-clinical-awareness` — Add DMN Voluntary Control as Mechanism

**What to add:** The existing note describes NCA as "vigilance without vigilance anxiety" but doesn't name DMN voluntary control as the trainable mechanism. Add:
- `skos:narrower: ["dmn-voluntary-control"]`
- Body addition: "The trainable mechanism underlying NCA is DMN voluntary control — the ability to selectively quiet default mode network activity during cases while allowing it during inter-case recovery."

---

### E6. Enrich `co-regulation` — Add Social Coherence EEG

**What to add:** `skos:narrower: ["social-coherence-eeg"]` — group EEG coherence detection is the neurophysiological measurement layer for co-regulation.

---

## New Observations

### O1. VNS Alpha Attenuation Concern

```yaml
id: urn:srl:observation:vns-alpha-attenuation-concern
type: observation
title: "VNS May Attenuate Resting Alpha — Counterproductive for Wellness"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
dc:subject: ["vns", "alpha-oscillations", "wellness", "neurophysiology", "nucleus-basalis"]
observation_type: pattern
clinical_context: "Evaluating auricular VNS for wellness applications"
years_of_evidence: 3
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-vns-effects-on-alpha-oscillations
skos:related: ["vagal-tone", "neuroharmonics", "autonomic-regulation"]
```

**Body (Randy's voice, high signal):**

> "Alpha oscillations are present as a default state and are interrupted with arousal. I think attenuation of that resting state by VNS would go in the opposite direction of a wellness environment."

> "There's a plethora of stuff the vagus nerve does, however I don't know if auricular stimulation generates potentials in the nucleus basalis like stimulation of the ascending cervical branch does. A whole lot of that neuromodulation comes from the induction of plasticity with stimulation of the NB and I don't know if auricular stimulation has any fibers terminating there."

**Randy's expert reasoning:** Auricular VNS may not reach the nucleus basalis (NB), which means it may lack the plasticity-inducing effects of cervical VNS. Furthermore, if VNS attenuates alpha oscillations (the brain's resting-state rhythm), it runs **counter** to wellness goals. This is a sophisticated neuroanatomical critique that should inform SRL's position on VNS-based wellness products.

**Clinical interpretation:** Pending review.

---

### O2. Dopaminergic Exhaustion Risk from Sustained Theta-Delta Practice

```yaml
id: urn:srl:observation:dopaminergic-exhaustion-risk
type: observation
title: "Risk of Dopaminergic Exhaustion from Sustained Theta-Delta EEG Pursuit"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
dc:subject: ["eeg", "theta-waves", "delta-waves", "dopamine", "nondual-awareness", "breathwork", "safety"]
observation_type: pattern
clinical_context: "Evaluating risks of full-time nondual breathwork practice"
years_of_evidence: 3
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-theta-and-delta-eeg-patterns
skos:related: ["nondual-clinical-awareness", "contemplative-progressive-overload", "neuroharmonics"]
```

**Body (Randy's voice):**

> "Define the risk of dopaminergic exhaustion if one pursues a theta and delta wave dominant EEG pattern throughout the day. Consider a person seeking a full time non-dual perspective who spends a majority of the day breathing in active breath work."

This is Randy asking a safety question about his own practice trajectory — and by extension, about the safety envelope for advanced somnistics practitioners. The question itself reveals his awareness that prolonged theta/delta dominance could deplete dopaminergic reserves, affecting motivation, motor control, and reward processing.

**SRL safety implication:** Advanced practitioners who sustain deep meditative states (theta-delta dominant) for extended periods may need dopaminergic recovery protocols. This informs the "guardrails for level-4 practitioners" framework in the vitarka-vicara session.

**Clinical interpretation:** Pending review.

---

### O3. Randy's Level-4 Practitioner Self-Assessment

```yaml
id: urn:srl:observation:randy-level-4-practitioner
type: observation
title: "Randy's Self-Assessment: Level 4 Iyengar Practitioner — 'Touching the Core of Being'"
status: draft
creator: Randy Graybeal
created: 2026-03-18
modified: 2026-03-18
dc:subject: ["personal-practice", "iyengar", "contemplative-depth", "nondual-awareness", "founder-practice"]
observation_type: somatic-marker
clinical_context: "Founder's personal contemplative practice depth"
years_of_evidence: 3
prov:wasDerivedFrom:
  - urn:srl:chat:chatgpt-vitarka-vicara-synthesis
skos:related: ["nondual-clinical-awareness", "contemplative-progressive-overload", "vitarka-vicara-integration"]
```

**Body (Randy's voice):**

> "I spend all my time touching the core of being."

Iyengar's four levels: (1) mild/sporadic, (2) consistent effort, (3) determined/discerning, (4) relentless/inexorable immersion. Randy self-identifies at level 4 — right-hemispheric panoramic presence as the ontological backdrop, not an occasional visitor. This is SRL-P (proprietary) data about the founder's practice depth that underlies the entire somnistics framework.

**Clinical interpretation:** Pending review.

---

## Relationship Discoveries

| From | Relation | To | Source | Confidence |
|------|----------|----|--------|------------|
| `vitarka-vicara-integration` | skos:broader | `hemispheric-rebalancing` | vitarka-vicara-synthesis.md | High |
| `dmn-voluntary-control` | skos:broader | `nondual-clinical-awareness` | crna-neurofeedback-dmn-control.md | High |
| `alpha-theta-crossover` | skos:broader | `neuroharmonics` | vitarka-vicara-synthesis.md | Medium |
| `social-coherence-eeg` | skos:broader | `co-regulation` | brainwave-visualization-apps.md | High |
| `dmn-voluntary-control` | skos:related | `attention-as-gain-control` | crna-neurofeedback-dmn-control.md | High |
| `dmn-voluntary-control` | skos:related | `neurogating` | crna-neurofeedback-dmn-control.md | High |
| `vitarka-vicara-integration` | skos:related | `polyanchora` | vitarka-vicara-synthesis.md | High — Polyanchora is the multi-anchor technique that enables it |
| `vitarka-vicara-integration` | skos:related | `neurogating` | vitarka-vicara-synthesis.md | High — NeuroGating is the front-back integration mechanism |
| `vitarka-vicara-integration` | skos:related | `gamma-state-binding` | vitarka-vicara-synthesis.md | Medium — gamma nested in alpha/theta during integrated state |
| `social-coherence-eeg` | skos:related | `coherence-field` | brainwave-visualization-apps.md | High — social EEG coherence is the measurement layer for coherence fields |
| `alpha-theta-crossover` | skos:related | `state-transition` | vitarka-vicara-synthesis.md | High — marks the transition point |

---

## Evidence Notes Flagged for Verification

| Candidate | Type | Source | Confidence | Issue |
|-----------|------|--------|------------|-------|
| PubMed 33214317 | journal-article | vns-effects-on-alpha-oscillations.md | Medium | Randy shared this PMID; need to verify title, authors, and relevance to VNS + alpha |
| Davidson et al. — Tibetan monks gamma coherence | journal-article | Referenced in gamma-state-binding (existing) | High | Classic study; may already be in evidence layer |
| Iyengar — "Divine Yoga: Do the Asana with Your Soul" | book | vitarka-vicara-synthesis.md | High | Source of the castle metaphor and vitarka/vicara framework |
| McGilchrist — "The Master and His Emissary" | book | vitarka-vicara-synthesis.md | Already in vault | Referenced in hemispheric-rebalancing — confirm link |

---

## Items Flagged for Randy's Review

1. **`dmn-voluntary-control` vs. enrichment of `nondual-clinical-awareness`:** Should this be a standalone concept or folded into NCA as a mechanism section? Randy's framing suggests it's distinct enough to stand alone, but it could go either way.

2. **`vitarka-vicara-integration` naming:** Randy may prefer a different slug. "Castle-Field Vision" is the protocol name; the concept itself is about integrating focused attention with panoramic awareness.

3. **`alpha-theta-crossover` scope:** Is this SRL-original or standard neurofeedback terminology? It's a well-known EEG phenomenon, but Randy's application of it as a validation marker for somnistics states may warrant concept status. Alternatively, it could be an enrichment to `neuroharmonics`.

4. **`social-coherence-eeg` ambition level:** Randy asked for a 5-person simultaneous EEG system. Is this a near-term product feature, a research tool, or a long-term vision? The answer affects where it sits in the vault.

5. **VNS alpha attenuation observation:** Does Randy want to develop a formal SRL position on auricular VNS, or is this a filed-away concern? His neurophysiology reasoning is strong enough to inform competitive positioning against VNS-based wellness devices.

6. **PubMed 33214317:** Need citation-resolver to verify this article and create an evidence note if it adds to the VNS/alpha story.

7. **Truncated messages:** Files 5 and 6 have `[message truncated]` markers. The vitarka-vicara file has at least 3 truncation points. Full content may contain additional extraction material. Recommend verifying import completeness.

---

## Extraction Yield Summary

| Category | Count | Items |
|----------|-------|-------|
| New concepts | 4 | `dmn-voluntary-control`, `vitarka-vicara-integration`, `alpha-theta-crossover`, `social-coherence-eeg` |
| New observations | 3 | `eeg-data-pipeline`, `vns-alpha-attenuation-concern`, `dopaminergic-exhaustion-risk`, `randy-level-4-practitioner` |
| Concept enrichments | 6 | `neuroharmonics`, `gamma-state-binding`, `hemispheric-rebalancing`, `closed-loop-biofeedback`, `nondual-clinical-awareness`, `co-regulation` |
| Evidence flagged | 4 | PubMed 33214317, Davidson gamma monks, Iyengar Divine Yoga, McGilchrist (confirm link) |
| Relationships | 11 | See table above |
| Flagged for review | 7 | See list above |

---

## Processing Notes

- **Highest-signal file:** `vitarka-vicara-synthesis.md` — Randy's Iyengar/McGilchrist bridge with EEG correlates is a major conceptual contribution. His endorsement ("This!") and self-disclosure ("I spend all my time touching the core of being") make this the richest extraction source in the batch.
- **Lowest-signal file:** `mac-eeg-visualization-tools.md` — pure tool research with no conceptual content. Only value is confirming Randy's "extra lead setup" experimentation.
- **Cross-file pattern:** These 7 files together document Randy's evolution from "how do I set up EEG streaming" (2023) to "build me a multi-person social coherence detection system" (2024) to "here's my biometric protocol with EEG markers for integrated hemispheric awareness" (2025). The trajectory shows increasing sophistication and integration with the somnistics framework.
- **Truncation impact:** At least 4 truncation points across files 2, 5, and 6 may contain additional extractable content. Flagged for import verification.
