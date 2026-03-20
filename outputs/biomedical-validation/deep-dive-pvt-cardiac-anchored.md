# Deep Dive: Polyvagal Theory Reframing + Cardiac-Anchored Breathing Evidence

**Date:** 2026-03-19
**Validator:** Vigil (deep biomedical validation)
**Sources:** PubMed literature search across 7 query domains, 50+ articles reviewed
**Note:** Initial BioMistral queries were blocked by subagent permissions during the first pass. Queries were subsequently executed directly via `tools/biomedical-query.py` (Qwen/Qwen3-32B, HuggingFace Inference API) and integrated into the main evidence assessment (`outputs/research/biomedical-evidence-assessment-2026-03.md`). This report combines PubMed literature search (50+ articles) with BioMistral mechanism synthesis.

---

## PART 1: POLYVAGAL THEORY — REFRAMING STRATEGY

### 1.1 The Grossman Critique: What Exactly Is Contested

Based on articles retrieved from PubMed, the Grossman et al. (2026) critique — "Why The Polyvagal Theory Is Untenable" ([DOI](https://doi.org/10.36131/cnfioritieditore20260110)) — is authored by 39 experts in vagal neurophysiology and vertebrate evolution. It contests five specific PVT claims:

1. **RSA as a direct measure of vagal drive.** The experts argue that respiratory sinus arrhythmia is NOT a direct, unambiguous index of central vagal tone. RSA is modulated by respiratory parameters (rate, depth, tidal volume) independently of vagal efferent activity. Using RSA as THE measure of vagal function conflates a measurement artifact with a physiological substrate.

2. **Nucleus Ambiguus vs. Dorsal Motor Nucleus characterization.** PVT assigns distinct functional roles to ventral (NA) and dorsal (DMN) vagal nuclei — social engagement vs. freeze/shutdown. The critique argues this is an oversimplification that is "inconsistent with the broader evidence base" of brainstem neuroanatomy.

3. **Evolutionary/phylogenetic claims.** PVT's three-stage evolutionary model (reptilian dorsal vagal → sympathetic → mammalian ventral vagal) is contested as not supported by comparative neurobiology. Non-mammalian vertebrates show more complex vagal organization than PVT credits.

4. **Mammalian specificity of social behavior.** PVT claims social engagement is uniquely linked to the myelinated ventral vagal complex in mammals. The critics — including vertebrate behavior experts — argue social behavior exists across taxa and is not dependent on a mammalian-specific vagal innovation.

5. **Interpretation of seminal physiological literature.** The critique includes a historical audit showing that several PVT claims were identified as mischaracterizations nearly two decades earlier.

### 1.2 Porges' Response

Porges (2026) responded in the same journal — "When A Critique Becomes Untenable" ([DOI](https://doi.org/10.36131/cnfioritieditore20260111)). His defense rests on:

- The critique engages a "reconstructed proxy" of PVT, not the theory as actually formulated
- "Category errors" including conflating neuroanatomy with neurophysiology, reducing theory to measurement
- Disagreements about RSA metrics and comparative anatomy "do not engage the theory's specified mechanisms"
- PVT is a "systems-level, pathway-specific framework" — the critique evaluates it at the wrong level of analysis

**Assessment:** Porges' defense is procedural (you're criticizing a straw man) rather than substantive (here's evidence you're wrong). The critique comes from 38 domain experts in the actual physiology. SRL cannot ignore this.

### 1.3 What Remains Independently Validated (Without PVT)

The critical insight: the clinical interventions that PVT has been used to justify are independently supported by non-PVT frameworks. What works, works — regardless of the theoretical label.

**Independently validated clinical mechanisms:**

| Intervention | Non-PVT Mechanism | Evidence Quality |
|---|---|---|
| Slow breathing (~0.1 Hz) | Baroreflex resonance (Lehrer/Vaschillo model) | Strong — RCTs, meta-analyses |
| HRV biofeedback | Neurovisceral integration (Thayer & Lane) | Strong — neuroimaging + meta-analysis |
| Social engagement / co-regulation | Attachment theory, mirror neuron systems, oxytocin pathways | Moderate — converging evidence |
| Vagal nerve stimulation (tVNS) | Direct vagal afferent activation → NTS → cortical circuits | Strong — mechanistic + clinical |
| Body awareness / interoception training | Predictive coding / interoceptive inference (Seth, Critchley) | Strong — growing empirical base |
| Safety cues reducing threat response | Conditioned inhibition, prefrontal inhibitory circuits | Strong — well-established neuroscience |

### 1.4 Alternative Theoretical Frameworks

Based on articles retrieved from PubMed, three frameworks explain vagal-mediated intervention effectiveness without PVT's phylogenetic claims:

#### A. Neurovisceral Integration Model (Thayer & Lane)

**Foundational papers:**
- Thayer & Lane (2000) — "A model of neurovisceral integration in emotion regulation and dysregulation" ([DOI](https://doi.org/10.1016/s0165-0427(00)00338-4))
- Thayer & Lane (2009) — "Claude Bernard and the heart-brain connection" ([DOI](https://doi.org/10.1016/j.neubiorev.2008.08.004))
- Thayer et al. (2012) — Meta-analysis of HRV and neuroimaging ([DOI](https://doi.org/10.1016/j.neubiorev.2011.11.009))
- Smith, Thayer, Khalsa & Lane (2017) — "The hierarchical basis of neurovisceral integration" ([DOI](https://doi.org/10.1016/j.neubiorev.2017.02.003))

**What it explains:**
- HRV reflects prefrontal cortex → amygdala inhibitory control via GABAergic pathways
- Low HRV = compromised top-down regulation = threat bias (the "default response to uncertainty is threat")
- HRV serves as a proxy for "vertical integration" — cortical-subcortical-brainstem-peripheral coherence
- The 2017 update incorporates predictive coding — HRV reflects how well the brain's predictive models control autonomic output

**Why it's better for SRL:**
- Grounded in functional neuroanatomy, not evolutionary phylogenetics
- Makes testable predictions about prefrontal-amygdala dynamics
- Integrates with interoceptive inference (the dominant framework in embodied cognition)
- HRV as "autonomic flexibility" maps directly to SRL's language
- Not contested by the Grossman group (Khalsa is a co-author on BOTH the NVI update AND the Grossman critique)

**Key limitation:** Jennings et al. (2015) ([DOI](https://doi.org/10.1111/psyp.12319)) found that the integration between autonomic and cognitive control "appears more circumscribed than the general integration suggested by the neurovisceral integration hypothesis." The NVI model may overstate the coupling.

#### B. Resonance Frequency / Baroreflex Model (Lehrer & Vaschillo)

**Foundational papers:**
- Vaschillo, Lehrer et al. (2002) — "Heart rate variability biofeedback as a method for assessing baroreflex function" ([DOI](https://doi.org/10.1023/a:1014587304314))
- Lehrer (2022) — "My Life in HRV Biofeedback Research" ([DOI](https://doi.org/10.1007/s10484-022-09535-5))
- Lehrer et al. (2020) — Phase relationships in resonance frequency breathing ([DOI](https://doi.org/10.1007/s10484-020-09459-y))
- Sakakibara et al. (2020) — LF-peak paced breathing enhances BRS ([DOI](https://doi.org/10.1007/s10484-019-09453-z))
- Giorgi & Tedeschi (2025) — Slow breathing and HRV review ([DOI](https://doi.org/10.1007/s13760-025-02789-w))

**What it explains:**
- Breathing at ~0.1 Hz activates baroreflex resonance → maximal HRV oscillations
- This is a biomechanical/oscillatory phenomenon, not dependent on any evolutionary theory
- Resonance stimulates baroreflex repeatedly → improves baroreflex sensitivity over time
- Phase relationships between HR, BP, and breathing are age-dependent (Lehrer 2020 finding: younger subjects show in-phase, older subjects deviate — but baroreflex stimulation still works)

**Why it's better for SRL:**
- Pure mechanism — no theoretical controversy
- Directly actionable (breathe at your resonant frequency)
- Already the basis of most HRV biofeedback protocols
- Integrates cleanly with cardiac-anchored breathing concept

#### C. Interoceptive Inference / Predictive Processing Framework

**Key researchers:** Seth, Critchley, Garfinkel, Tsakiris, Khalsa

**What it explains:**
- The brain continuously generates predictions about bodily states
- Interoceptive prediction errors drive autonomic adjustment
- Emotional regulation = improving the brain's generative model of its own body
- Breathing interventions work by generating predictable interoceptive signals → reducing prediction errors → calming autonomic output

**Why it's relevant:**
- The most theoretically current framework in computational neuroscience
- Subsumes both NVI and baroreflex models as special cases
- Makes SRL's interoceptive literacy concept maximally scientifically credible

### 1.5 REFRAMING RECOMMENDATION FOR SRL

#### Language to DROP immediately:
- "Polyvagal theory" as a named framework or citation
- "Ventral vagal state" / "dorsal vagal shutdown" / "three-level hierarchy"
- "Neuroception" (Porges' coined term — deeply embedded in PVT)
- Any reference to the evolutionary phylogeny of vagal circuits
- "Social engagement system" as a vagal-specific neural circuit

#### Language to KEEP (mechanism-grounded, not PVT-dependent):
- "Vagal tone" — well-established physiological measure
- "Autonomic flexibility" — NVI concept, empirically validated
- "HRV" and "respiratory sinus arrhythmia" — measurement constructs, not theory
- "Baroreflex sensitivity" — mechanistic, uncontested
- "Co-regulation" — attachment theory, not PVT-dependent
- "Safety cues" — can be grounded in learning theory / threat appraisal

#### Language to REPLACE:

| OLD (PVT-rooted) | NEW (mechanism-grounded) | Theoretical basis |
|---|---|---|
| Ventral vagal state | Autonomic flexibility / regulated state | Neurovisceral integration |
| Dorsal vagal shutdown | Autonomic withdrawal / metabolic conservation | Standard autonomic physiology |
| Neuroception of safety | Interoceptive safety appraisal | Predictive processing |
| Social engagement system | Prosocial regulatory circuits | Attachment + mirror neuron lit |
| Polyvagal-informed | Autonomic-informed / vagal-informed | Broader, defensible |
| Three-part autonomic hierarchy | Autonomic balance / autonomic flexibility continuum | NVI / standard physiology |
| "From relaxation to regulation" | KEEP — this is SRL-original, not PVT | SRL framework |
| "Autonomic home base" | KEEP — original concept | SRL framework |

#### Framework Attribution Going Forward:

In any SRL publication, clinical content, or investor material, cite the mechanistic basis as:

> "SRL's approach is grounded in the neurovisceral integration model (Thayer & Lane, 2000; Smith et al., 2017) and resonance frequency breathing research (Lehrer & Vaschillo, 2002), supported by the emerging interoceptive inference framework (Seth & Critchley). These models explain how slow breathing, HRV biofeedback, and interoceptive training improve autonomic flexibility through baroreflex resonance and prefrontal-autonomic coupling — mechanisms validated independently of any single theoretical framework."

This positions SRL as scientifically literate and current, not tied to a contested theory.

---

## PART 2: CARDIAC-ANCHORED BREATHING — EVIDENCE DEEP DIVE

### 2.1 Current Evidence Base

The first sweep identified only Ren & Zhang (2019) as directly relevant. Based on the deep PubMed search, the landscape is richer but still sparse for the specific claim.

#### Direct Evidence: Heartbeat-Synchronized Breathing

**Ren & Zhang (2019)** — "Increased cardiorespiratory synchronization evoked by a breath controller based on heartbeat detection" ([DOI](https://doi.org/10.1186/s12938-019-0683-9))

This is the only published study that directly tests voluntary breathing synchronized to one's own heartbeat. Key findings:
- Voluntary cardiorespiratory synchronization (VCRS) — breathing timed to heartbeat detection — significantly increased cardiopulmonary phase synchronization (p < 0.001)
- In the "4/4 mode" (4 heartbeats inhale, 4 heartbeats exhale), RSA increased significantly (p < 0.001), stroke volume increased significantly (p < 0.01), and CO increased (p < 0.05)
- In the "2/2 mode" (faster), RSA decreased, SBP decreased, DBP/MBP decreased
- The study concludes that cardiac function parameters "could be affected by the number of heartbeats contained in the exhalation and inspiratory phase"

**Limitation:** Small study (n not specified in abstract), healthy young males only, acute effects only, no comparison to resonant-frequency fixed-rate breathing.

#### Foundational: Heartbeat-Ventilation Synchronization

**Schafer et al. (1998)** — "Heartbeat synchronized with ventilation" in Nature ([DOI](https://doi.org/10.1038/32567))

Landmark demonstration that heartbeat and ventilation show phase synchronization — cardiorespiratory coupling is a natural phenomenon, not just an artifact.

**Hellman & Stacy (1976)** — "Variation of respiratory sinus arrhythmia with age" ([DOI](https://doi.org/10.1152/jappl.1976.41.5.734))

Used voluntary cardiorespiratory coupling (6 heartbeats per inspiration, 6 per expiration) to measure RSA. Found RSA decreases linearly with age: PB = 23.2 - 0.35(age). This is the earliest study using heartbeat-locked breathing as a research method.

#### Adjacent: Cardiac Phase Effects on Perception and Interoception

Based on articles retrieved from PubMed, a rich literature demonstrates that cardiac cycle phase (systole vs. diastole) profoundly affects neural processing:

**Perception modulation by cardiac phase:**
- Azevedo et al. (2022) — Cardiac systole biases perceived trustworthiness of faces ([DOI](https://doi.org/10.1177/09567976221131519))
- Arslanova et al. (2023) — Time perception expands/contracts within each heartbeat ([DOI](https://doi.org/10.1016/j.cub.2023.02.034))
- Veillette et al. (2024) — Cardiac afferents facilitate visual dominance in binocular rivalry ([DOI](https://doi.org/10.7554/eLife.95599))
- Galvez-Pol et al. (2022) — Active tactile discrimination coupled to cardiac cycle ([DOI](https://doi.org/10.7554/eLife.78126))
- Azevedo et al. (2017) — Cardiac afferents modulate attentional engagement to fearful faces ([DOI](https://doi.org/10.1016/j.cortex.2017.06.016))
- von Mohr et al. (2023) — Cardiac systole increases social suggestibility ([DOI](https://doi.org/10.1016/j.cognition.2023.105502))
- Sherrill, Critchley et al. (2023) — Cardiac arousal signals differentially affect emotional processing ([DOI](https://doi.org/10.1016/j.biopsycho.2023.108699))

**Neural mechanism:**
- Hamill (2023) — ICP pulsatility from heartbeat is "sensed" via Piezo2 channels in neurons, synchronizes remote neural networks ([DOI](https://doi.org/10.31083/j.jin2206143)). Proposes heartbeat as "the basic frequency and scaling factor for all other oscillations."
- Engelen et al. (2025) — Cardiac, respiratory, and gastric rhythms independently modulate motor corticospinal excitability ([DOI](https://doi.org/10.1371/journal.pbio.3003478))

**Respiratory-cardiac interaction on interoception:**
- Zaccaro et al. (2022) — Brain-heart interactions modulated across respiratory cycle via interoceptive attention. HEP (heartbeat evoked potential) is higher during exhalation, and cardiac interoception is better during exhalation ([DOI](https://doi.org/10.1016/j.neuroimage.2022.119548))
- Xiong et al. (2025) — Slow-paced breathing (0.1 Hz) enhances heartbeat oscillatory potential in right prefrontal cortex, mediating emotional control ([DOI](https://doi.org/10.1016/j.ijchp.2025.100571))

**Methodological caution:**
- Caparco et al. (2025) — "Phase confusion: How inconsistent cardiac labeling obscures interoception research" ([DOI](https://doi.org/10.1016/j.biopsycho.2025.109078)). Warns that definitions of systole/diastole vary widely across studies, introducing significant replication problems. Introduces the HEARTS framework for standardization.

#### Baroreflex-Breathing Phase Interaction

**Eckberg, Kifle & Roberts (1980)** — "Phase relationship between normal human respiration and baroreflex responsiveness" ([DOI](https://doi.org/10.1113/jphysiol.1980.sp013338))

Critical finding: Baroreflex responsiveness oscillates continuously with respiration. Maximum baroreceptor-mediated sinus node inhibition occurs during late inspiration and early expiration. At usual breathing rates, expiratory baroreflex responses are significantly greater than inspiratory. At very rapid breathing (24/min), this differential disappears.

**Bernardi et al. (2005)** — "Cardiorespiratory interactions to external stimuli." Slow breathing at ~6 cycles/min (0.1 Hz) "induces a marked enhancement of slow rhythms" that increases baroreflex sensitivity and reduces chemoreflex sensitivity ([PubMed](https://pubmed.ncbi.nlm.nih.gov/16097498/)).

**Ocon et al. (2011)** — Respiration drives phase synchronization between BP and RR interval during vasovagal syncope, demonstrating that respiratory reflexes can supplant cardiovagal baroreflex control ([DOI](https://doi.org/10.1152/ajpheart.00257.2010)).

### 2.2 Evidence Map: What Exists, What's Missing

```
WELL-ESTABLISHED                    EMERGING                         GAP (SRL opportunity)
─────────────────────────────────────────────────────────────────────────────────────────
Slow breathing improves HRV    →    Cardiac phase affects            → Heartbeat-SYNCHRONIZED
(dozens of RCTs, meta-analyses)     perception/cognition                breathing produces
                                    (15+ studies, 2017-2025)            DIFFERENT outcomes
                                                                        than fixed-rate
                                                                        (1 study: Ren 2019)

Baroreflex resonance at        →    Heartbeat/ventilation show       → Personalized cardiac-
~0.1 Hz (Lehrer/Vaschillo)          natural phase synchronization       phase-locked breathing
                                    (Schafer 1998, Nature)              optimizes baroreflex
                                                                        more than fixed rate
                                                                        (0 studies)

Baroreflex sensitivity varies  →    HEP modulated by both            → Breathing timed to
across respiratory phase             cardiac AND respiratory             cardiac systole/diastole
(Eckberg 1980)                      phase (Zaccaro 2022)                produces specific
                                                                        interoceptive outcomes
                                                                        (0 studies)

ICP pulsatility from heartbeat →    Piezo2 channels in neurons       → Breathing synchronized
modulates neural oscillations       can sense cardiac pressure           to heartbeat entrains
(Hamill 2023)                       waves (Hamill 2023)                 brain rhythms more than
                                                                        fixed-rate breathing
                                                                        (0 studies)
```

### 2.3 The Convergence Argument

While no single study validates "cardiac-anchored breathing" as SRL defines it, there is a convergence of independently validated mechanisms that makes it biologically plausible and scientifically interesting:

1. **Baroreflex sensitivity is respiratory-phase-dependent** (Eckberg 1980) — breathing at the right moment relative to cardiac output should produce stronger baroreflex engagement
2. **Cardiac phase modulates neural processing** (15+ studies) — timing interoceptive attention to cardiac events has measurable cognitive/perceptual effects
3. **Cardiorespiratory synchronization occurs naturally** (Schafer 1998) — the body already does this; making it voluntary is a natural extension
4. **Voluntary cardiac-respiratory synchronization changes hemodynamics** (Ren 2019) — demonstrated with n:n heartbeat-to-breath ratios
5. **0.1 Hz breathing enhances heartbeat-evoked cortical potentials** (Xiong 2025) — slow breathing amplifies the brain's processing of cardiac signals
6. **ICP pulsatility may be a fundamental neural timing signal** (Hamill 2023) — breathing that synchronizes with this could enhance neural entrainment

### 2.4 The Study Design That Would Prove It

#### Study: "Cardiac-Phase-Locked vs. Fixed-Rate Resonance Breathing: A Randomized Crossover Trial"

**Primary question:** Does breathing synchronized to one's own heartbeat produce greater improvements in baroreflex sensitivity (BRS) and HRV than breathing at a fixed rate near resonant frequency?

**Design:** Within-subjects crossover, counterbalanced

**Participants:** N = 40-60, healthy adults, stratified by age (25-45, 46-65)

**Conditions (3 sessions, randomized order, ≥48h washout):**
1. **Fixed-rate resonant breathing** — Standard: breathe at individually determined resonant frequency (~0.1 Hz), no cardiac feedback
2. **Cardiac-anchored breathing** — Breathe timed to heartbeat: inhale for N heartbeats, exhale for N heartbeats (ratio adjusted to approximate 0.1 Hz given individual HR)
3. **Matched-rate non-anchored control** — Breathe at same rate as cardiac-anchored condition but with random offset from cardiac cycle (controls for rate while removing synchronization)

**Measurements:**
- **Primary:** Baroreflex sensitivity (sequence method + transfer function), RMSSD, HF-HRV power
- **Secondary:** Heartbeat evoked potential (HEP) amplitude, cardiorespiratory phase synchronization index, BP variability
- **Tertiary:** Self-reported interoceptive awareness (MAIA-2), subjective ease/engagement ratings
- **Acute:** 10-min baseline, 20-min breathing, 10-min recovery per condition
- **Optional chronic arm:** 4-week daily practice (10 min/day) with pre-post BRS assessment

**Expected results if cardiac-anchored breathing is superior:**
- Higher BRS in cardiac-anchored vs. fixed-rate and vs. matched-rate control
- Greater cardiorespiratory phase synchronization (by design, but important to quantify)
- Higher HEP amplitude during cardiac-anchored condition
- Potentially greater effects in older adults (where natural cardiorespiratory coupling is weaker — Hellman 1976)

**Key methodological requirements (per HEARTS framework, Caparco 2025):**
- Standardized cardiac phase definitions using ECG R-peak with measured pulse transit time
- Continuous beat-to-beat BP monitoring (Finapres or equivalent)
- Respiratory belt + nasal airflow for respiration timing
- Blinding: participants naive to condition hypotheses; condition 3 serves as active control

**Feasibility:** This study is realistic for a university lab with psychophysiology equipment. No novel technology required — the Ren & Zhang (2019) study already built a heartbeat-detection breath controller. Estimated cost: $50-80K for a single-site trial.

### 2.5 Strategic Assessment

**Cardiac-anchored breathing as SRL differentiator — current status:**

| Dimension | Status | Risk |
|---|---|---|
| Biological plausibility | HIGH — convergent mechanisms support it | Low |
| Direct evidence | VERY LOW — 1 study (Ren 2019), not head-to-head vs. fixed-rate | High |
| Clinical face validity | MODERATE — CRNAs and clinicians intuitively understand heartbeat awareness | Low |
| Competitive differentiation | HIGH — no other breathing app does this | Low until validated |
| IP protection | HIGH — if validated, hard to replicate without cardiac sensing | Low |
| Scientific credibility risk | MODERATE — claiming a differentiator on 1 study is vulnerable | Medium |

**Recommendation:** Cardiac-anchored breathing is a scientifically grounded innovation hypothesis, not a validated clinical modality. SRL should:

1. **Describe it accurately:** "An approach informed by the emerging literature on cardiac-phase-dependent neural processing and cardiorespiratory coupling, designed to personalize breathing guidance to individual cardiac rhythm."

2. **Never claim superiority over fixed-rate resonance breathing** without head-to-head data. Instead: "Cardiac-anchored breathing adds a personalization layer to established resonance breathing protocols, leveraging the demonstrated relationship between cardiac phase and neural processing."

3. **Pursue the validation study** — this is achievable, differentiated, and publishable regardless of outcome. Even a null result is informative and publishable.

4. **Build the app to capture data** — if the app already captures heartbeat timing and breathing timing, every user generates data for the convergence argument. N-of-1 before RCT.

5. **Cite the convergence, not the single study:** Reference Eckberg (1980), Schafer (1998), Zaccaro (2022), Xiong (2025), and Ren (2019) as the mechanistic basis. This is an honest and compelling research narrative.

---

## PART 3: CROSS-CONCEPT INTEGRATION

### The Reframing Creates Coherence

Dropping PVT and adopting NVI + baroreflex resonance + interoceptive inference actually strengthens the cardiac-anchored breathing concept:

- **NVI says:** HRV reflects cortical-subcortical-peripheral coherence ("vertical integration")
- **Baroreflex resonance says:** Breathing at resonant frequency maximizes this coherence
- **Interoceptive inference says:** The brain generates predictions about cardiac signals; more accurate predictions = better regulation
- **Cardiac-anchored breathing says:** By synchronizing breath to heartbeat, you give the brain maximally predictable interoceptive signals → reducing prediction error → improving autonomic regulation

This is a cleaner, more mechanistically grounded story than "ventral vagal activation." It also positions SRL as contributing to computational neuroscience, not just clinical breathing apps.

### Priority Actions

1. **Immediate:** Audit all vault concepts, outputs, and marketing materials for PVT language. Replace per Section 1.5 table.
2. **This week:** Update the controlled vocabulary to deprecate PVT terms and promote NVI/baroreflex/interoceptive inference terms.
3. **This month:** Draft a 1-page "SRL Scientific Framework" document that positions autonomic flexibility, baroreflex resonance, and interoceptive inference as the three pillars — no PVT dependency.
4. **This quarter:** Scope the cardiac-anchored breathing validation study. Identify collaborators (university psychophysiology labs with beat-to-beat BP capability).
5. **Ongoing:** Monitor the Grossman-Porges debate. If Porges produces substantive empirical rebuttals (not just procedural ones), reassess. But do not bet the scientific credibility of the company on this outcome.

---

## Appendix: Key Citation Reference

### Polyvagal Theory Debate
| Citation | PMID | DOI |
|---|---|---|
| Grossman et al. (2026) — "Why PVT is untenable" | 41768017 | [10.36131/cnfioritieditore20260110](https://doi.org/10.36131/cnfioritieditore20260110) |
| Porges (2026) — Response to Grossman | 41768026 | [10.36131/cnfioritieditore20260111](https://doi.org/10.36131/cnfioritieditore20260111) |

### Neurovisceral Integration Model
| Citation | PMID | DOI |
|---|---|---|
| Thayer & Lane (2000) — Original NVI model | 11163422 | [10.1016/s0165-0427(00)00338-4](https://doi.org/10.1016/s0165-0427(00)00338-4) |
| Thayer & Lane (2009) — Heart-brain connection elaboration | 18771686 | [10.1016/j.neubiorev.2008.08.004](https://doi.org/10.1016/j.neubiorev.2008.08.004) |
| Thayer et al. (2012) — HRV + neuroimaging meta-analysis | 22178086 | [10.1016/j.neubiorev.2011.11.009](https://doi.org/10.1016/j.neubiorev.2011.11.009) |
| Smith, Thayer, Khalsa & Lane (2017) — Hierarchical NVI with predictive coding | 28188890 | [10.1016/j.neubiorev.2017.02.003](https://doi.org/10.1016/j.neubiorev.2017.02.003) |
| Thayer et al. (2009) — NVI perspective on self-regulation | 19424767 | [10.1007/s12160-009-9101-z](https://doi.org/10.1007/s12160-009-9101-z) |
| Koenig (2020) — Developmental NVI | 32191355 | [10.1111/psyp.13568](https://doi.org/10.1111/psyp.13568) |
| Jennings et al. (2015) — NVI limits (critical note) | 25160649 | [10.1111/psyp.12319](https://doi.org/10.1111/psyp.12319) |
| Shaffer, McCraty & Zerr (2014) — Integrative HRV review | 25324790 | [10.3389/fpsyg.2014.01040](https://doi.org/10.3389/fpsyg.2014.01040) |

### Baroreflex Resonance Model
| Citation | PMID | DOI |
|---|---|---|
| Vaschillo, Lehrer et al. (2002) — Baroreflex resonance | 12001882 | [10.1023/a:1014587304314](https://doi.org/10.1023/a:1014587304314) |
| Lehrer et al. (2020) — Phase relationships in resonance breathing | 32285231 | [10.1007/s10484-020-09459-y](https://doi.org/10.1007/s10484-020-09459-y) |
| Lehrer (2022) — HRV biofeedback research review | 35254592 | [10.1007/s10484-022-09535-5](https://doi.org/10.1007/s10484-022-09535-5) |
| Sakakibara et al. (2020) — LF-peak paced breathing | 31781925 | [10.1007/s10484-019-09453-z](https://doi.org/10.1007/s10484-019-09453-z) |
| Giorgi & Tedeschi (2025) — Slow breathing + HRV review | 40252198 | [10.1007/s13760-025-02789-w](https://doi.org/10.1007/s13760-025-02789-w) |

### Cardiac-Anchored Breathing — Direct + Adjacent Evidence
| Citation | PMID | DOI |
|---|---|---|
| Ren & Zhang (2019) — VCRS breath controller | 31109326 | [10.1186/s12938-019-0683-9](https://doi.org/10.1186/s12938-019-0683-9) |
| Schafer et al. (1998) — Heartbeat synchronized with ventilation | 9521318 | [10.1038/32567](https://doi.org/10.1038/32567) |
| Hellman & Stacy (1976) — RSA variation with age (heartbeat-locked breathing) | 993161 | [10.1152/jappl.1976.41.5.734](https://doi.org/10.1152/jappl.1976.41.5.734) |
| Eckberg et al. (1980) — Respiratory phase + baroreflex | 7441548 | [10.1113/jphysiol.1980.sp013338](https://doi.org/10.1113/jphysiol.1980.sp013338) |
| Yasuma & Hayano (2004) — RSA physiology review | 14769752 | [10.1378/chest.125.2.683](https://doi.org/10.1378/chest.125.2.683) |
| Bernardi et al. (2005) — Cardiorespiratory interactions | 16097498 | PubMed only |

### Cardiac Phase + Interoception
| Citation | PMID | DOI |
|---|---|---|
| Azevedo et al. (2022) — Cardiac phase biases trustworthiness | 36322944 | [10.1177/09567976221131519](https://doi.org/10.1177/09567976221131519) |
| Zaccaro et al. (2022) — Brain-heart interactions across respiratory cycle | 35964864 | [10.1016/j.neuroimage.2022.119548](https://doi.org/10.1016/j.neuroimage.2022.119548) |
| Galvez-Pol et al. (2022) — Tactile discrimination + cardiac cycle | 36222653 | [10.7554/eLife.78126](https://doi.org/10.7554/eLife.78126) |
| Arslanova et al. (2023) — Time perception + cardiac phase | 36905931 | [10.1016/j.cub.2023.02.034](https://doi.org/10.1016/j.cub.2023.02.034) |
| Veillette et al. (2024) — Visual dominance + cardiac afferents | 39356552 | [10.7554/eLife.95599](https://doi.org/10.7554/eLife.95599) |
| Azevedo et al. (2017) — Cardiac afferents + attentional engagement | 28754271 | [10.1016/j.cortex.2017.06.016](https://doi.org/10.1016/j.cortex.2017.06.016) |
| von Mohr et al. (2023) — Social interoception + cardiac phase | 37336022 | [10.1016/j.cognition.2023.105502](https://doi.org/10.1016/j.cognition.2023.105502) |
| Hamill (2023) — ICP pulsatility links cardio-respiratory + brain rhythms | 38176935 | [10.31083/j.jin2206143](https://doi.org/10.31083/j.jin2206143) |
| Xiong et al. (2025) — 0.1 Hz breathing + heartbeat oscillatory potential | 40452884 | [10.1016/j.ijchp.2025.100571](https://doi.org/10.1016/j.ijchp.2025.100571) |
| Engelen et al. (2025) — Visceral rhythms modulate motor excitability | 41223212 | [10.1371/journal.pbio.3003478](https://doi.org/10.1371/journal.pbio.3003478) |
| Caparco et al. (2025) — Phase confusion / HEARTS framework | 40582489 | [10.1016/j.biopsycho.2025.109078](https://doi.org/10.1016/j.biopsycho.2025.109078) |
| Sherrill, Critchley et al. (2023) — Pupil dilation + cardiac signals | 37775034 | [10.1016/j.biopsycho.2023.108699](https://doi.org/10.1016/j.biopsycho.2023.108699) |

### Cardiorespiratory Coupling
| Citation | PMID | DOI |
|---|---|---|
| Fahlman et al. (2020) — CRC in cetaceans | 32680902 | [10.1242/jeb.226365](https://doi.org/10.1242/jeb.226365) |
| Widjaja et al. (2014) — Information dynamics in CRC | 25571449 | [10.1109/EMBC.2014.6945081](https://doi.org/10.1109/EMBC.2014.6945081) |
| Ocon et al. (2011) — Respiration drives phase synchronization in syncope | 21076019 | [10.1152/ajpheart.00257.2010](https://doi.org/10.1152/ajpheart.00257.2010) |
