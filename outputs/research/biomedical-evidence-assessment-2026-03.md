---
title: "SRL Evidence Assessment: Biomedical Validation of Core Constructs"
created: 2026-03-19
creator: Vigil (SRL Knowledge Graph Orchestrator)
type: output
output_type: proposal
status: draft
---

# SRL Evidence Assessment: Biomedical Validation of Core Constructs
## March 2026

---

### Executive Summary

Somnistics Research Labs (SRL) proposes that autonomic regulation, interoceptive awareness, and structured breathwork can be trained as clinical competencies to reduce burnout, improve performance, and extend career longevity in certified registered nurse anesthetists (CRNAs) and other high-acuity clinicians. This report presents the results of a systematic biomedical validation sweep conducted against the SRL knowledge vault --- 44 concepts across 8 thematic clusters, cross-referenced against 150+ PubMed articles (2014--2026 focus, with foundational literature back to 1976) and supplemented by 8 targeted queries through BioMistral (Qwen/Qwen3-32B via HuggingFace Inference API) for mechanism validation, literature synthesis, and gap identification.

The core physiological science underlying SRL's approach is strong. Slow breathing at resonant frequency (~0.1 Hz) improves heart rate variability (HRV) via baroreflex resonance, with meta-analytic support from 223 studies (Laborde et al., 2022). HRV biofeedback demonstrates medium effect sizes for depression and autonomic outcomes (Vann-Adibe et al., 2025). Interoception is a mature and expanding neuroscience field with validated instruments (MAIA-2), robust neuroimaging evidence, and growing clinical applications including a $4M NIH initiative.

Where SRL's position becomes more nuanced is at the interface of established science and novel application. Several SRL-original constructs --- the Interoceptive Suppression Hypothesis (ISH), State Drift, Cardiac-Anchored Breathing, Contemplative Progressive Overload --- represent scientifically plausible hypotheses built on solid mechanistic foundations but currently lacking direct empirical validation. The polyvagal theory framework, which SRL has used as a theoretical anchor, faces a significant 2026 challenge from 39 domain experts (Grossman et al., 2026) that necessitates reframing toward independently validated mechanisms (neurovisceral integration, baroreflex resonance, interoceptive inference). Additionally, binaural beat entrainment --- the mechanistic claim underlying NeuroHarmonics --- is not reliably supported by the EEG literature, with a systematic review finding only 5 of 14 studies confirming the entrainment hypothesis (Ingendoh et al., 2023).

This report distinguishes between what the literature establishes, what remains actively debated, and what SRL proposes as testable hypotheses. It identifies five literature voids that represent genuine research opportunities and proposes three priority studies with designs, power analyses, and cost estimates. The goal is not to defend SRL's framework but to present it honestly --- to show where the evidence stands, where the gaps are, and how to close them.

---

### Methodology

#### Validation Approach

The biomedical validation sweep was conducted between March 15--19, 2026. The process involved:

1. **Concept inventory.** All 44 active concepts in the SRL knowledge vault were categorized into 8 thematic clusters: Autonomic/HRV/Vagal (10 concepts), Interoception/Body Sensing (9), Breathwork/Respiratory (4), Neurofeedback/EEG/Brainwaves (6), Clinician Performance/Durability (8), Consciousness/Contemplative (7).

2. **PubMed literature search.** For each concept, targeted PubMed queries were constructed using MeSH terms and free-text combinations. Over 150 articles were screened for relevance, with full abstracts reviewed and key papers analyzed for mechanism validation, evidence strength, gaps, and contradictions.

3. **Evidence grading.** Each concept was assessed against the SRL Evidence Grading Framework, which adapts Oxford CEBM levels (1a--5b) and incorporates Knowledge Readiness Levels (KRL 1--9) adapted from NASA's Technology Readiness Levels (see Appendix A for the full matrix).

4. **Cross-referencing.** Vault claims were compared against PubMed evidence. Where the vault cited specific mechanisms, effect sizes, or clinical outcomes, these were verified or flagged as unsupported. Where vault concepts had no published analogs, this was noted as either a gap or a research opportunity.

5. **Deep dives.** Three concept clusters received extended analysis: (a) polyvagal theory reframing and cardiac-anchored breathing, (b) ISH, State Drift, and MAIA-2-CRNA, and (c) binaural beat entrainment, hormesis, and micro-dose intervention dosing.

#### BioMistral Methodology

In addition to PubMed literature search, 8 targeted queries were executed through the BioMistral biomedical language model on 2026-03-19 for mechanism validation, literature synthesis, and gap identification.

- **Tool.** Queries were run through `tools/biomedical-query.py`, which calls the HuggingFace Inference API.
- **Model.** Qwen/Qwen3-32B, routed via the HuggingFace inference router.
- **Purpose.** Three functions: (1) mechanism validation --- testing whether SRL's mechanistic claims are consistent with published literature; (2) literature synthesis --- aggregating findings across domains that span multiple PubMed search strategies; (3) gap identification --- surfacing absence of evidence in specific intersections.
- **Queries executed.** 8 queries covering: polyvagal theory debate specifics, interoceptive suppression and alexithymia in medical training, binaural beat entrainment evidence, minimum effective dose for breathing interventions, state drift during sustained clinical performance, cardiac-anchored versus fixed-rate breathing, nondual awareness and DMN mechanisms, and hormesis applicability to psychological stressors.
- **Limitation.** BioMistral is a research accelerator, not a source of truth. The model synthesizes patterns from its training corpus but may generate plausible-sounding citations that do not exist or misattribute findings. All specific claims surfaced by BioMistral were cross-referenced against PubMed where possible. Citations generated by the model require independent verification before use in any external-facing document. BioMistral contributions are explicitly labeled throughout this report.

#### Limitations

- The validation focused on mechanism plausibility and evidence existence, not on exhaustive systematic review methodology. This is a scoping assessment, not a Cochrane review.
- Publication bias applies to all PubMed-derived conclusions: positive results are overrepresented.
- BioMistral-sourced findings are clearly marked and should be treated as hypothesis-generating synthesis, not as independently verified evidence. All BioMistral citations require PubMed verification before external use.

---

### Part 1: Established Science (KRL 5--7)

These concepts rest on foundations with strong meta-analytic or RCT support. SRL builds on this science but did not originate it.

#### 1.1 Autonomic Regulation and HRV as Biomarker

The capacity to shift flexibly between sympathetic and parasympathetic states --- and the measurement of this capacity via HRV --- is supported by converging evidence at the highest quality levels.

- **Meta-analytic support.** Galin et al. (2026) conducted a meta-analysis of 56 longitudinal studies confirming HRV (RMSSD, SDNN, HF, LF, VLF) as a prospective predictor of depressive symptoms with small but significant negative correlations (DOI: 10.1016/j.jad.2026.121388). Vann-Adibe et al. (2025) found medium effect sizes for remote HRV biofeedback on both depression improvement (g = -0.41) and HRV increase (g = 0.443) across multiple studies (DOI: 10.1007/s10484-025-09750-w).
- **Mechanistic validation.** The neurovisceral integration model (Thayer & Lane, 2000; Smith et al., 2017) explains HRV as reflecting prefrontal cortex-to-amygdala inhibitory control via GABAergic pathways. Low HRV indexes compromised top-down regulation. This model is independently validated through neuroimaging (Thayer et al., 2012; DOI: 10.1016/j.neubiorev.2011.11.009) and is not dependent on polyvagal theory.
- **Emerging direction.** AI-driven adaptive biofeedback is identified as a future direction in multiple reviews (Gitler et al., 2025; DOI: 10.3892/mi.2025.236), validating SRL's adaptive technology thesis.

**Evidence grade: 1a (meta-analytic). KRL: 6.** SRL's application of this science to CRNA populations is at KRL 4--5.

#### 1.2 Resonant Breathing Frequency and Baroreflex Resonance

The mechanism by which slow diaphragmatic breathing at ~0.1 Hz produces baroreflex resonance and maximizes HRV amplitude is among the best-validated constructs in the vault.

- **Definitive meta-analysis.** Laborde et al. (2022) reviewed 223 studies and confirmed that voluntary slow breathing increases vagally-mediated HRV during practice, immediately after a single session, and after multi-session interventions (DOI: 10.1016/j.neubiorev.2022.104711).
- **Mechanistic review.** Sevoz-Couche & Laborde (2022) confirmed that breathing at resonant frequency increases cardiac oscillations via temporal coherence of respiratory, blood pressure, and cardiac phases, improving vagally-mediated HRV and baroreflex sensitivity (DOI: 10.1016/j.neubiorev.2022.104576).
- **Dose-response data.** You et al. (2023) demonstrated that all slow-paced breathing conditions (5--7 cpm) significantly increased cardiac vagal activity versus spontaneous breathing, with measurable effects in 5-minute bouts (DOI: 10.1007/s10484-023-09605-2).
- **Neural evidence.** Xiong et al. (2025) showed 0.1 Hz slow-paced breathing increases heartbeat oscillatory potentials in right prefrontal cortex, mediating enhanced emotional control (DOI: 10.1016/j.ijchp.2025.100571). Plantard et al. (2025) demonstrated modulation of heartbeat-evoked potentials with insular and cingulate cortex sources (DOI: 10.1152/jn.00118.2025).

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 4 — Micro-Dose Breathing):** Kox et al. (2020) reported that 1 minute of slow breathing increased RMSSD by approximately 15%, with effects peaking at 3 minutes. Huberman (2023) found that cyclic sighing with 3--5 slow breaths produced rapid vagal tone increases. This positions 60 seconds at the floor of measurable physiological effect, suggesting the NeuroMinute format may be viable but sits at the minimum threshold. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Evidence grade: 1a. KRL: 5.** The minimum effective dose below 5 minutes is not established (see Part 4).

#### 1.3 Interoception and the Garfinkel Trichotomy

Interoception --- the sense of the body's internal physiological state --- is a mature neuroscience field with validated measurement tools and expanding clinical applications.

- **Neural architecture.** The posterior insula processes raw sensory input; the anterior insula performs complex integration; the ACC handles error monitoring. This architecture is confirmed by Nikolova et al. (2025), who identified distinct microstructural patterns in insular, cingulate, and primary sensory cortices underlying interoceptive sensitivity and precision using quantitative brain imaging in over 200 participants (DOI: 10.1523/JNEUROSCI.0787-24.2025).
- **Three-dimensional model.** Garfinkel et al. (2015) established that interoceptive accuracy (behavioral task performance), sensibility (self-reported awareness), and metacognitive awareness (correspondence between the two) are dissociable dimensions (DOI: 10.1016/j.biopsycho.2014.11.004). This trichotomy has been extended to autism (Garfinkel et al., 2016) and cross-modal domains including respiratory interoception (Garfinkel et al., 2017; DOI: 10.1098/rstb.2016.0014).
- **Instrument validation.** MAIA-2 is the strongest validated body awareness patient-reported outcome measure, per a 2025 COSMIN systematic review (Bravo et al., 2025; DOI: 10.3390/healthcare13243270). It has been validated across 17+ populations and languages.
- **Measurement debate.** The Schandry heartbeat counting task, long considered the standard for interoceptive accuracy, is increasingly contested. Harrison et al. (2021) developed the Filter Detection Task for respiratory interoception as a more rigorous alternative (DOI: 10.1016/j.biopsycho.2021.108185). Caparco et al. (2025) demonstrated that inconsistent cardiac phase labeling across studies introduces significant replication problems (DOI: 10.1016/j.biopsycho.2025.109078).

**Evidence grade: 1b--2a. KRL: 6.** No CRNA-specific interoception data exists (see Part 4).

#### 1.4 Clinician Burnout and the Second-Victim Phenomenon

The prevalence and consequences of clinician burnout are extensively documented.

- **Prevalence data.** ICU staff PTSD prevalence at 16.8%, anxiety at 22.8% in the second year of COVID-19 (Roger et al., 2024; DOI: 10.1186/s12991-023-00488-5). In French anesthesia teams, 83% experienced incivility, with nurse anesthetists showing higher emotional exhaustion than anesthesiologists (Raft et al., 2025; DOI: 10.1016/j.jclinane.2025.111983).
- **Second-victim syndrome.** A 2025 meta-analysis of surgeons found: anxiety 56.3%, guilt 53.8%, sleep disturbance 50.5%, sadness 48.3% (Bryan et al., 2025; DOI: 10.1093/bjs/znaf258). Deng et al. (2025) confirmed that over two-thirds of healthcare professionals encounter such trauma during their careers (DOI: 10.1016/j.ijnurstu.2025.105248).
- **Institutional recognition.** The AANA Wellness Ambassador MC integration into NAEP curriculum validates institutional recognition of the problem (Morgan et al., 2025; DOI: 10.70278/AANAJ/.0000001070).

**Evidence grade: 1a--2a for prevalence; 2b--3b for interventions. KRL: 4--5 for SRL's specific approach.** The gap is not in recognizing the problem but in demonstrating that autonomic regulation training improves clinical outcomes.

#### 1.5 Default Mode Network Modulation

The ability to modulate DMN activity through contemplative practice is well-established in neuroimaging.

- Sezer et al. (2022) synthesized resting-state fMRI studies showing mindfulness relates to functional connectivity changes in DMN, frontoparietal, and salience networks (DOI: 10.1016/j.neubiorev.2022.104583). Bauer et al. (2019) found experienced meditators develop increased DMN-CEN coupling --- active co-regulation rather than simple DMN suppression (DOI: 10.1523/ENEURO.0335-18.2019).
- SRL's framing --- "DMN is a tool, not an enemy; the goal is a switch, not a kill" --- aligns with the Bauer (2019) data showing co-regulation rather than suppression in experienced practitioners.

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 7 — Nondual Awareness + DMN):** Nondual awareness states involve reduced activation in mPFC and PCC (core DMN hubs), enhanced salience network engagement, and increased thalamocortical connectivity. Zeidan (2010) found that brief mindfulness sessions (10 minutes) can improve attention. This suggests that even micro-practices may train DMN switching ability, though deep nondual states likely require extensive practice. The practical implication for SRL is that brief interventions may target network reconfiguration without requiring the thousands of hours associated with advanced contemplative attainments. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Evidence grade: 2a--2b. KRL: 5 (general); KRL 2 for CRNA-specific application.**

---

### Part 2: Active Scientific Debate

These concepts involve mechanisms where the evidence is contested or where SRL's framing requires careful positioning relative to ongoing scientific disagreement.

#### 2.1 Polyvagal Theory: The Grossman-Porges Exchange

This is the most consequential validation finding. The SRL vault has used polyvagal theory (PVT) as a foundational theoretical framework. A 2026 publication challenges this directly.

**The critique.** Grossman et al. (2026), in a paper titled "Why The Polyvagal Theory Is Untenable" with 38 co-authors --- acknowledged experts in vagal neurophysiology and vertebrate evolution --- contested five specific PVT claims: (1) RSA is not a direct measure of central vagal drive; (2) PVT mischaracterizes the neuroanatomy of Nucleus Ambiguus versus Dorsal Motor Nucleus; (3) PVT's evolutionary claims about vagal phylogeny are not supported by comparative neurobiology; (4) mammalian social behavior specificity claims are incorrect; (5) several PVT claims had been identified as mischaracterizations nearly two decades earlier (DOI: 10.36131/cnfioritieditore20260110).

**The response.** Porges (2026) responded that the critique engages a "reconstructed proxy" of PVT through "persistent category errors" and that disagreements reflect "differences in measurement preference, level of analysis, or theoretical framing rather than evidence against the theory's organizing principles" (DOI: 10.36131/cnfioritieditore20260111).

**Assessment for SRL.** The critique comes from 39 domain experts in the actual physiology; the defense is procedural rather than substantive. However, the critical insight is that the *clinical interventions* PVT has been used to justify are independently supported by non-PVT frameworks:

| Intervention | Non-PVT Mechanism | Evidence Quality |
|---|---|---|
| Slow breathing (~0.1 Hz) | Baroreflex resonance (Lehrer/Vaschillo) | Strong --- RCTs, meta-analyses |
| HRV biofeedback | Neurovisceral integration (Thayer & Lane) | Strong --- neuroimaging + meta-analysis |
| Co-regulation | Attachment theory, physiological synchrony | Moderate --- converging evidence |
| Body awareness training | Interoceptive inference (Seth, Critchley) | Strong --- growing empirical base |

Three alternative frameworks explain SRL's intervention mechanisms without PVT's phylogenetic claims:

1. **Neurovisceral Integration Model** (Thayer & Lane, 2000; Smith et al., 2017) --- HRV reflects prefrontal-amygdala inhibitory control. Importantly, Khalsa is a co-author on both the NVI update and the Grossman critique, meaning this framework is accepted by both sides of the PVT debate.
2. **Resonance Frequency / Baroreflex Model** (Lehrer & Vaschillo, 2002) --- a biomechanical/oscillatory phenomenon not dependent on any evolutionary theory.
3. **Interoceptive Inference / Predictive Processing** (Seth, Critchley, Garfinkel) --- the most theoretically current framework in computational neuroscience.

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 1 — PVT Debate):** Grossman's specific contestations include: (1) RSA is not a reliable measure of central vagal drive; (2) the NA/DMN characterization in PVT misrepresents vagal neuroanatomy; (3) vagal evolutionary phylogeny claims are not supported by comparative data --- the myelinated vagus is not uniquely mammalian; (4) mammalian social behavior specificity claims lack comparative evidence. BioMistral identified the Thayer Neurovisceral Integration (NVI) model as the strongest alternative framework, consistent with this report's independent PubMed analysis. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Recommendation.** SRL should transition from PVT-dependent language to mechanism-grounded terminology. The interventions work; the theoretical label is the vulnerability. Specific language replacements: "ventral vagal state" becomes "regulated state / autonomic flexibility"; "neuroception" becomes "interoceptive safety appraisal"; "polyvagal-informed" becomes "autonomic-informed."

#### 2.2 NeuroHarmonics and Binaural Beat Entrainment

SRL's NeuroHarmonics concept implies that binaural beats can reliably entrain brainwaves at target frequencies. The evidence does not support this specific mechanism.

**Systematic review evidence.** Ingendoh et al. (2023) reviewed 14 EEG studies specifically testing brainwave entrainment from binaural beats. Only 5 of 14 supported the entrainment hypothesis; 8 reported contradictory results. The authors concluded: "The results corroborate the impression of an overall inconsistency of empirical outcomes" (DOI: 10.1371/journal.pone.0286023).

**What IS confirmed.** Binaural beats produce interhemispheric alpha-band coherence --- but Solca et al. (2015) explicitly stated this "seems to reflect binaural integration rather than entrainment" (DOI: 10.1016/j.heares.2015.09.011). Yang et al. (2025) found no significant difference between theta, alpha, and beta binaural beats for anxiety reduction, suggesting effects may not be frequency-specific (DOI: 10.1186/s12906-025-04922-x).

**Clinical effects exist but through different mechanisms.** A meta-analysis of 15 RCTs (n=1047) found binaural beats significantly reduced perioperative anxiety (SMD = -1.38, p<0.0001), though heterogeneity was substantial (I-squared = 91.6%) (Xiong et al., 2025; DOI: 10.1016/j.ctim.2025.103299). The effects are likely driven by attentional engagement, expectancy, and relaxation context rather than frequency-specific neural entrainment.

**Alternative.** Dos Anjos et al. (2024) found isochronic tones produced significantly greater EEG power changes than binaural beats (p<0.001) (DOI: 10.1016/j.neuroscience.2024.07.014). If SRL wants a neurophysiologically grounded auditory intervention, isochronic tones may have a stronger evidence base.

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 3 — Binaural Entrainment):** BioMistral confirmed the Ingendoh (2023) finding of 5/14 supporting studies. Additionally, it identified Huang & Charyton (2017) as reporting that isochronic tones produce stronger EEG modulation than binaural beats, consistent with the Dos Anjos (2024) finding already in this report. BioMistral flagged a mechanistic distinction: binaural beat effects may be peripheral (cochlear-level processing) rather than central neural entrainment, which would explain the inconsistent EEG results. If the effect originates in cochlear processing rather than cortical synchronization, frequency-specific brainwave claims are fundamentally unsupportable. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Recommendation.** Retire the term "entrainment" from NeuroHarmonics claims. Use "auditory modulation" or "auditory-autonomic coupling." Frame as: "Audio environments designed to support nervous system regulation through attention, breath pacing, and auditory engagement" --- not "brainwave entrainment technology." The breath-pacing component (Layer 2) has strong evidence; the binaural entrainment component (Layer 1) does not.

#### 2.3 Hemispheric Rebalancing

The McGilchrist framework (left-hemisphere analytical focus versus right-hemisphere broad awareness) is a useful heuristic but neuroscience has largely moved beyond strict lateralization models.

- Yordanova et al. (2020) did find lateralized connectivity patterns during meditation --- left-hemispheric theta networks and right-hemispheric alpha networks (DOI: 10.1038/s41598-020-64324-6). However, both hemispheres contribute to most cognitive functions; the difference is in degree and processing mode, not exclusive localization.
- No published evidence demonstrates that SRL practices specifically "rebalance" hemispheric activity as measured by any standard EEG or fMRI metric.

**Recommendation.** Consider reframing from "hemispheric rebalancing" to "attentional mode shifting" or "network reconfiguration" --- terms consistent with current network neuroscience while preserving the clinical insight.

---

### Part 3: SRL-Original Hypotheses (KRL 2--4)

These are novel constructs with mechanistic plausibility but limited direct evidence. They represent SRL's intellectual contribution to the field and should be framed as hypotheses to be tested, not established findings.

#### 3.1 Interoceptive Suppression Hypothesis (ISH)

**The hypothesis.** Professional clinical training systematically suppresses interoceptive awareness through a "hidden curriculum" of emotional detachment, creating a population with intact physiological signaling but degraded subjective awareness --- a discrepancy that drives burnout, compassion fatigue, and clinical error.

**Supporting evidence (indirect).**
- De Berardis et al. (2023) found 14.8% of 1,445 Italian healthcare workers met criteria for alexithymia (TAS-20 positive), with significantly higher emotional exhaustion and depersonalization (DOI: 10.3390/brainsci13111550).
- Riethof et al. (2020) found alexithymia correlated with burnout (r = 0.41) and emotional exhaustion (r = 0.37) in 114 female healthcare professionals (DOI: 10.1177/0300060519887633).
- Aldaz et al. (2019) found alexithymia was a stronger predictor of burnout than emotional intelligence in 159 nursing assistants (DOI: 10.1111/jan.14153).
- Crivelli et al. (2025) found discrepancies between physiological activation and subjective stress perception in neurosurgeons --- precisely the pattern ISH predicts (DOI: 10.3389/fpsyg.2025.1568430).
- Six PubMed results for "hidden curriculum emotional suppression medical education" confirm this is a recognized but understudied phenomenon.

**Counter-evidence.** Handford et al. (2013) found that clinical practice preserved empathic accuracy against age-related decline, suggesting clinical exposure may enhance rather than suppress certain forms of perceptual sensitivity (DOI: 10.1371/journal.pone.0065159). ISH may need to distinguish between expertise-based clinical pattern recognition and personal body-signal awareness.

**Critical gap.** PubMed returned zero results for "interoceptive accuracy burnout healthcare workers." The intersection of interoceptive measurement and clinician burnout is nearly unresearched --- 4 total results for "interoception burnout stress occupational."

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 2 — Interoceptive Suppression + Alexithymia):** Alexithymia prevalence in medical students and residents ranges from 15--25% compared to approximately 10% in the general population, with surgeons reaching up to 30%. HRV decline during training correlates with interoceptive blunting. Krasner et al. documented empathy erosion during medical training. This is consistent with ISH's core prediction that training systematically degrades body-signal awareness and suggests the suppression may be measurable via both psychometric (TAS-20/MAIA-2) and physiological (HRV trajectory) instruments simultaneously. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Evidence grade: 4--5a (indirect). KRL: 2.** High face validity; zero direct empirical tests. The construct is testable and potentially publishable as a landmark paper.

#### 3.2 State Drift

**The hypothesis.** Autonomic regulation progressively degrades during sustained clinical performance, creating a measurable trajectory of HRV decline that can be detected and intervened upon. The five-step mechanism: arousal spike, incomplete recovery, baseline elevation, perceptual narrowing, error vulnerability.

**Supporting evidence.**
- Li et al. (2022) monitored 17 nurses with ECG during work and found work shifts had significant effects on LF%, LnHF, and RMSSD, with higher LF% correlating with higher subjective stress (DOI: 10.3389/fpubh.2021.810577).
- Zhan et al. (2024) found night shifts significantly altered HRV in 35 female nurses, with greater parasympathetic suppression post-shift (DOI: 10.1186/s12912-024-02563-y).
- McGarry et al. (2023), from the U.S. Naval Research Lab, found cardiac vagal tone changes dynamically over the course of a vigilance task in a non-monotonic, individual-dependent pattern (DOI: 10.3389/fnrgo.2023.1244658). This is, effectively, state drift measured.
- Hamidi Shishavan et al. (2022) showed HRV on workdays decreased compared to non-work days in ICU nurses with continuous 24-hour monitoring (DOI: 10.1016/j.apergo.2022.103937).

**Critical gap.** No published study has named this phenomenon, operationalized the trajectory, or built real-time detection. The term "state drift" does not appear in the biomedical literature in this autonomic context.

**Important caveat.** Some high-performing clinicians operate at elevated sympathetic baselines without apparent errors. The model needs to account for individual variability in optimal arousal windows (Yerkes-Dodson). Additionally, the causal link from baseline elevation to clinical error is inferred, not demonstrated.

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 5 — State Drift):** Kvernmo (2017) found that nurses show increased sympathetic activity and decreased parasympathetic activity by shift end. Smith (2020) reported a 25% RMSSD reduction in paramedics over 12-hour shifts. BioMistral also noted that consumer wearables (e.g., Oura, Apple Watch) can detect HRV trends over shift-length intervals but lack the precision for absolute value thresholds --- meaning State Drift detection would need to be trajectory-based (relative decline) rather than threshold-based (absolute cutoff). This has design implications for SRL's real-time monitoring approach. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Evidence grade: 2b--4 (indirect). KRL: 2.** The underlying physiology is supported; the assembled construct and its measurement framework are SRL-original.

#### 3.3 Cardiac-Anchored Breathing

**The hypothesis.** Synchronizing breathing to one's own heartbeat rather than an external clock produces greater improvements in baroreflex sensitivity and HRV than standard fixed-rate pacing, by leveraging the demonstrated relationship between cardiac phase and neural processing.

**Direct evidence.** One study. Ren & Zhang (2019) demonstrated a heartbeat-detection-based breath controller that successfully increased cardiorespiratory synchronization (p < 0.001). In the "4/4 mode" (slow breathing locked to heartbeats), RSA increased significantly and stroke volume increased. However, in the "2/2 mode" (fast breathing locked to heartbeats), RSA decreased --- effects are ratio-dependent, not uniformly positive (DOI: 10.1186/s12938-019-0683-9).

**Convergence argument.** While no single study validates the concept, converging mechanisms make it biologically plausible:
- Baroreflex sensitivity is respiratory-phase-dependent (Eckberg et al., 1980; DOI: 10.1113/jphysiol.1980.sp013338).
- Cardiac phase modulates neural processing across 15+ studies (2017--2025): trustworthiness perception (Azevedo et al., 2022), time perception (Arslanova et al., 2023), visual dominance (Veillette et al., 2024), social suggestibility (von Mohr et al., 2023).
- Cardiorespiratory synchronization occurs naturally (Schafer et al., 1998, Nature; DOI: 10.1038/32567).
- 0.1 Hz breathing enhances heartbeat-evoked cortical potentials (Xiong et al., 2025).

**Critical gap.** No published RCT compares cardiac-anchored versus fixed-rate breathing for HRV outcomes. Consumer wearable accuracy for beat-to-beat timing is unvalidated for this application.

**BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 6 — Cardiac-Anchored Breathing):** Khalsa (2017) reported that heartbeat-synchronized breathing (HSB) increased HRV by 22% compared to fixed-rate breathing. Zaccardi (2018) found a 15% reduction in sympathetic markers with HSB. BioMistral also identified converging evidence from the Critchley, Garfinkel, and Azevedo groups showing that cardiac phase modulates perception, decision-making, and emotional processing --- supporting the mechanistic rationale that synchronizing breath to cardiac phase could amplify these effects. If the Khalsa and Zaccardi findings verify, the evidence base for cardiac-anchored breathing would advance from KRL 2 to KRL 3--4. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

**Evidence grade: 4 (single mechanistic study). KRL: 2.** High biological plausibility; very low direct evidence.

#### 3.4 Embodied Metacognition

**The hypothesis.** Monitoring cognition through somatic signals constitutes a distinct metacognitive process, distinguishable from standard (abstract) metacognition.

- Nikolova et al. (2025) demonstrated that respiratory metacognition has specific microstructural correlates in midline prefrontal cortex, distinct from interoceptive sensitivity patterns in insula (DOI: 10.1523/JNEUROSCI.0787-24.2025).
- Chemis et al. (2025) found breathing-related interoceptive metacognitive bias correlated with amygdala-insula connectivity (DOI: 10.3758/s13415-025-01328-7).

The construct requires differentiation from the Damasio somatic marker hypothesis, which is the closest established framework. Standard metacognition research does not typically distinguish "embodied" from "abstract" metacognition.

**Evidence grade: 5a--5b (theoretical + emerging neuroimaging). KRL: 2.**

#### 3.5 Contemplative Progressive Overload

**The hypothesis.** Exercise physiology principles (progressive overload, periodization) can be applied to contemplative training, systematically increasing challenge across five levers: frequency, complexity, stressors, compression, and integration.

This is the most conceptually novel construct in the vault. No published literature applies exercise periodization principles to contemplative training. Many contemplative traditions explicitly reject the "effort and intensity" approach (e.g., shikantaza, Dzogchen). Additionally, the assumption that awareness responds to overload like muscle tissue requires validation --- neural adaptation follows different rules than muscle hypertrophy.

**Evidence grade: 5b (theoretical). KRL: 1--2.**

---

### Part 4: Evidence Gaps and Research Opportunities

#### 4.1 Summary of Gaps by Severity

| Priority | Gap Description | Affected Concepts | Closest Existing Evidence | Severity |
|----------|----------------|-------------------|--------------------------|----------|
| 1 | No MAIA-2 data from any CRNA or anesthesia provider population | ISH, MAIA-2-CRNA, interoceptive literacy, diaphragmatic blindness | MAIA-2 validated in 17+ populations; zero healthcare-profession-specific adaptations (PubMed: 0 results) | Critical |
| 2 | No published correlation between interoceptive accuracy and burnout in clinicians | ISH, clinician durability | Alexithymia-burnout correlation r=0.37--0.41 (Riethof 2020, Aldaz 2019); interoception-burnout: 4 PubMed results total | Critical |
| 3 | No RCT comparing cardiac-anchored versus fixed-rate breathing | Cardiac-anchored breathing, NRCC | 1 mechanistic study (Ren & Zhang 2019); convergent cardiac-phase literature | High |
| 4 | No continuous within-shift HRV trajectory data correlated with clinical errors | State drift, clinician durability | Li 2022, Zhan 2024, McGarry 2023 (shift-level HRV changes documented but not linked to error events) | High |
| 5 | No published evidence for 60-second therapeutic dose of breathing interventions | NeuroMinute, Five-Breath Re-Embodiment | 5-minute minimum tested (Balban et al. 2023, You et al. 2023); 1-minute deep breathing test exists as diagnostic, not therapeutic | High |
| 6 | Binaural beat entrainment not reliably established as a mechanism | NeuroHarmonics | 5/14 EEG studies supportive (Ingendoh 2023); clinical anxiety effects documented through other mechanisms | High |
| 7 | PVT theoretical framework under expert challenge | All concepts referencing polyvagal theory | Non-PVT frameworks (NVI, baroreflex, interoceptive inference) explain same interventions | High |
| 8 | No longitudinal tracking of interoceptive awareness across clinical training | ISH, interoceptive literacy | Hidden curriculum literature (6 PubMed results); alexithymia prevalence in HCWs documented cross-sectionally | Moderate |
| 9 | 90-second amygdala deactivation timeline weakly sourced | State transition, NeuroMinute | Widely cited in popular neuroscience; lacks clear primary source with this specific number | Moderate |
| 10 | Micro-dose breathing may impair performance in naive users under stress | NeuroMinute, SIT | Goldberg et al. (2021): brief breath awareness produced worse working memory under stress in meditation-naive sample (DOI: 10.1080/02699931.2021.1878113) | Moderate |

#### 4.2 Five Literature Voids SRL Can Fill

1. **Interoceptive awareness in anesthesia providers.** PubMed returns zero results for "MAIA interoceptive awareness clinician nurse" and zero for "interoceptive awareness assessment anesthesia provider." The first MAIA-2 administration to a CRNA cohort would generate a publishable paper regardless of the finding.

2. **Interoceptive-burnout mechanistic link.** PubMed returns zero results for "interoceptive accuracy burnout healthcare workers." The alexithymia-burnout connection is established (r = 0.37--0.41); the interoception-specific pathway has not been tested. SRL's ISH provides the theoretical framework and testable predictions.

3. **Intra-shift autonomic trajectory monitoring.** While isolated studies have measured pre/post HRV in clinicians, no study has named and operationalized the within-shift degradation trajectory or correlated it with performance markers. "State Drift" could become a named construct in the literature.

4. **Cardiac-phase-locked breathing intervention.** No published study compares cardiac-anchored breathing to fixed-rate resonance breathing in a controlled design. The convergent evidence from cardiac-phase perception research (15+ studies) provides strong mechanistic rationale.

5. **Sub-5-minute breathing dose-response.** The literature jumps from 1-minute deep breathing as a diagnostic marker to 5-minute breathwork as the shortest tested therapeutic dose. What happens between 1 and 5 minutes is unmapped. SRL could contribute the first dose-response curve for this range.

---

### Part 5: Proposed Research Program

Three priority studies, ordered by feasibility and impact.

#### Study 1: MAIA-2-CRNA Validation and ISH Cross-Sectional Test

**Rationale.** This study simultaneously validates a CRNA-specific interoceptive instrument and tests the Interoceptive Suppression Hypothesis. It is the enabling study for the entire research program.

**Design.** Cross-sectional, three-group comparison.

**Population.**
- Group 1: CRNAs (n = 80)
- Group 2: Pre-CRNA nursing students (n = 80) --- same pipeline, earlier training stage
- Group 3: Non-clinical professionals matched for age, education, stress level (n = 80)
- Total N = 240

**Measures.**
1. MAIA-2 (or MAIA-2-CRNA with supplementary items) --- 8 dimensions of interoceptive awareness
2. Heartbeat Detection Task (Schandry, 1981) --- objective interoceptive accuracy
3. TAS-20 (alexithymia) --- convergent validity
4. Resting HRV (RMSSD, SDNN, LF/HF) --- autonomic baseline
5. Physiological stress response (HR, skin conductance) during standardized stress task
6. Subjective stress rating during same task --- the ISH discrepancy measure
7. MBI (burnout) --- dependent variable for clinical significance
8. PSS-10 (perceived stress)
9. Professional training exposure --- years of clinical experience, specialty, shift type

**Primary hypotheses.**
- H1: CRNAs will show lower MAIA-2 scores (especially Noticing, Emotional Awareness, Body Listening) compared to non-clinical controls (expected d = 0.4--0.6, based on alexithymia effect sizes in HCW literature).
- H2: CRNAs will show larger physiological-subjective discrepancy scores during stress tasks (expected d = 0.5--0.7, extrapolated from Crivelli 2025).
- H3: Physiological-subjective discrepancy will correlate with burnout severity (expected r = 0.3--0.4, based on Riethof 2020 and Aldaz 2019).
- H4: Years of clinical training will predict lower interoceptive awareness scores (dose-response relationship supporting causal pathway).

**Power analysis.** For d = 0.5 between groups, alpha = 0.05, power = 0.80: n = 64 per group. With 80 per group: sufficient for medium effects and multivariate models.

**Publication targets.** *Journal of Psychosomatic Research*, *Academic Medicine*, *Psychophysiology*.

**Estimated cost.** $40--60K (survey administration, physiological testing equipment, research coordinator time, statistician).

**Timeline.** 12--18 months from IRB approval to manuscript submission.

#### Study 2: State Drift Continuous Monitoring in CRNAs

**Rationale.** This study names and operationalizes intra-shift autonomic degradation with real-time monitoring. It builds on the Li (2022), Zhan (2024), and McGarry (2023) findings by mapping the full trajectory.

**Design.** Within-subjects repeated measures (each CRNA serves as own control).

**Population.** N = 60 CRNAs wearing continuous HRV monitors across 3 consecutive shifts.

**Measures.**
1. Continuous HRV (ECG chest strap: Polar H10 or equivalent) --- RMSSD, SDNN, LF/HF in 5-minute epochs across entire shift
2. Pre-shift 5-minute seated HRV baseline
3. Hourly subjective ratings --- fatigue, stress, clinical confidence (VAS)
4. Psychomotor Vigilance Task (PVT) at shift-start, mid-shift, shift-end
5. Shift characteristics --- case complexity, critical events, break frequency
6. Post-shift recovery via Oura Ring nocturnal HRV
7. Morning RMSSD on post-shift days versus off days

**Primary hypotheses.**
- H1: RMSSD will decrease across the shift (expected slope: -2 to -5 ms/hour).
- H2: LF/HF ratio will increase across the shift.
- H3: HRV drift magnitude will correlate with end-of-shift cognitive performance decline.
- H4: Nocturnal RMSSD on post-shift nights will be lower than off-day nights.
- H5: Critical events during shift will accelerate HRV drift (event-locked analysis).

**Publication targets.** *AANA Journal*, *Applied Ergonomics*, *Frontiers in Neuroergonomics*.

**Estimated cost.** $60--90K (wearable devices, research coordinator for shift-level data collection, data analysis infrastructure).

**Timeline.** 12--18 months.

#### Study 3: Cardiac-Anchored Versus Fixed-Rate Breathing Crossover Trial

**Rationale.** This is SRL's strongest competitive differentiator. If cardiac-anchored breathing produces greater BRS improvements than fixed-rate pacing, it validates the core product thesis and generates a novel, publishable finding.

**Design.** Within-subjects crossover, counterbalanced, three conditions.

**Population.** N = 40--60, healthy adults, stratified by age (25--45, 46--65).

**Conditions (3 sessions, randomized order, >=48h washout).**
1. Fixed-rate resonant breathing --- breathe at individually determined resonant frequency (~0.1 Hz), no cardiac feedback
2. Cardiac-anchored breathing --- breathe timed to heartbeat: inhale for N heartbeats, exhale for N heartbeats (ratio adjusted to approximate 0.1 Hz given individual HR)
3. Matched-rate non-anchored control --- breathe at same rate as cardiac-anchored condition but with random offset from cardiac cycle (controls for rate while removing synchronization)

**Measurements.**
- Primary: Baroreflex sensitivity (sequence method + transfer function), RMSSD, HF-HRV
- Secondary: Heartbeat evoked potential (HEP) amplitude, cardiorespiratory phase synchronization index, blood pressure variability
- Tertiary: MAIA-2, subjective ease/engagement ratings
- Protocol: 10-min baseline, 20-min breathing, 10-min recovery per condition

**Key methodological requirements (per HEARTS framework, Caparco 2025).**
- Standardized cardiac phase definitions using ECG R-peak with measured pulse transit time
- Continuous beat-to-beat BP monitoring (Finapres or equivalent)
- Respiratory belt + nasal airflow for respiration timing

**Publication targets.** *Applied Psychophysiology and Biofeedback*, *Psychophysiology*, *Frontiers in Neuroscience*.

**Estimated cost.** $50--80K for a single-site trial.

**Timeline.** 12--15 months.

---

### Part 6: Claim Calibration

This section provides specific language guidance for SRL communications with scientific audiences.

#### 6.1 Claims Supported at Each Evidence Level

**Can state with confidence (Evidence grade 1a--2a, KRL 5+):**
- "Slow breathing at approximately 0.1 Hz improves heart rate variability through baroreflex resonance, with meta-analytic support."
- "HRV biofeedback demonstrates medium effect sizes for depression and autonomic outcomes."
- "Interoception is a trainable capacity with validated measurement tools and growing clinical applications."
- "Clinician burnout is a documented crisis with measurable physiological correlates."

**Can state with qualification (Evidence grade 2b--4, KRL 3--4):**
- "The literature suggests that autonomic regulation training may reduce clinician burnout, though controlled trials specific to this intervention-population combination are needed."
- "Physiological synchrony between team members during cooperative clinical tasks has been demonstrated (Wespi et al., 2025), supporting the concept of co-regulation in clinical environments."
- "DMN modulation through contemplative practice is well-documented in meditation research; its application to clinical performance requires further study."

**Can state as hypothesis (Evidence grade 4--5b, KRL 1--2):**
- "We hypothesize that clinical training may systematically suppress interoceptive awareness through a hidden curriculum of emotional detachment. Preliminary data from alexithymia research and neurophenomenological stress studies are consistent with this hypothesis, but direct testing is needed."
- "State drift --- the progressive degradation of autonomic regulation during sustained clinical performance --- is proposed as a measurable phenomenon based on converging evidence from shift-level HRV studies. A formal operationalization and validation study is planned."
- "Cardiac-anchored breathing leverages the emerging literature on cardiac-phase-dependent neural processing. Whether this produces superior outcomes to fixed-rate pacing is an empirical question we are designing a study to answer."

**Should not claim without further evidence:**
- "Binaural beats entrain brainwaves at target frequencies." (Majority of EEG studies fail to confirm entrainment.)
- "Sixty seconds rewires your nervous system." (No therapeutic study has tested this dose; minimum tested therapeutic dose is 5 minutes.)
- "Polyvagal theory explains why SRL's approach works." (The theoretical framework is under active expert challenge; the mechanisms are independently validated without PVT.)
- "Hormesis applies to all forms of stress training." (Hormesis is established for physiological stressors; its extension to psychological/behavioral domains has minimal empirical validation. Moral injury may not be hormetic at any dose.) **BioMistral synthesis (Qwen3-32B, 2026-03-19, Query 8 — Hormesis + SIT):** Patel (2018) found that structured stress exposure increased PFC activation and reduced amygdala reactivity. Lee (2021) reported that nurses who underwent stress inoculation training showed higher HRV during acute stress events. BioMistral's key finding: Stress Inoculation Training (SIT) is a better framework than hormesis for the psychological domain --- SIT has an established clinical evidence base (Meichenbaum), while hormesis as a concept lacks validated dose-response curves for cognitive and emotional stressors. SRL should reference SIT rather than hormesis when discussing psychological stress adaptation. *Note: model-generated synthesis --- citations require independent verification via PubMed.*

#### 6.2 Terms to Use and Avoid

| Avoid | Use Instead | Rationale |
|-------|-------------|-----------|
| Ventral vagal state | Autonomic flexibility / regulated state | PVT-specific; contested |
| Dorsal vagal shutdown | Autonomic withdrawal / metabolic conservation | PVT-specific; oversimplifies neuroanatomy |
| Neuroception | Interoceptive safety appraisal | Porges' coined term; deeply embedded in PVT |
| Brainwave entrainment | Auditory modulation / auditory-autonomic coupling | Entrainment not reliably demonstrated |
| Micro-dose autonomic regulation | Brief structured breathing practice | "Micro-dose" implies pharmacological analogy; 60s dose is unvalidated |
| Research proves | The literature suggests; evidence indicates | No single study "proves" anything |
| Clinically validated (for SRL protocols) | Informed by clinical research; built on validated mechanisms | SRL's specific protocols are not yet clinically validated as integrated systems |

#### 6.3 FDA Wellness Boundary Considerations

SRL operates in the general wellness space. Claims supported only by SRL-P or SRL-O evidence should remain framed as "general wellness" or "training and education." The following claim categories require caution:

- **Disease treatment claims** (e.g., "treats burnout," "prevents PTSD") --- should not be made without Level 1--3 evidence and regulatory review.
- **Diagnostic claims** (e.g., "detects state drift") --- monitoring tools that detect physiological patterns are permissible as general wellness; claims about detecting clinical conditions require regulatory pathway.
- **Performance claims** (e.g., "reduces clinical errors") --- supportable with appropriate evidence but currently lack direct RCT evidence for SRL's specific interventions.

---

### Appendix A: Concept Evidence Matrix

| Concept | KRL | Evidence Grade | Validation Status | Key Evidence | Key Gap |
|---------|-----|---------------|-------------------|-------------|---------|
| Autonomic regulation | 6 | 1a | Supported | Galin 2026 meta-analysis; Thayer NVI model | CRNA-specific outcome data |
| Vagal tone | 6 | 1a--1b | Supported | Laborde 2022; Shaffer & Ginsberg 2017 | RSA measurement caveat per Grossman |
| Resonant breathing frequency | 5 | 1a | Supported | Laborde 2022 (223 studies); Sevoz-Couche 2022 | Minimum effective dose below 5 min |
| Polyvagal theory | 5* | 2b--Active debate | Partially supported | Porges 2025, 2026; Grossman 2026 | Reframe to NVI/baroreflex |
| Interoception | 6 | 1b--2a | Supported | Garfinkel 2015; Nikolova 2025; NIH initiative | No CRNA-specific data |
| Interoceptive accuracy | 6 | 1b | Supported | Garfinkel 2015; Harrison 2021 | Schandry task validity debate |
| MAIA-2 (base instrument) | 6 | 1b | Supported | 37 PubMed validation studies; Bravo 2025 COSMIN | No healthcare-profession adaptation |
| Clinician durability | 5 | 2a--2b | Supported | Roger 2024; Raft 2025; McEwen allostatic load | Autonomic recovery kinetics unmeasured |
| Second-victim phenomenon | 5 | 2a | Supported | Bryan 2025; Deng 2025 | CRNA-specific data sparse |
| Stress inoculation training | 5 | 1b (general) | Supported | Sterling 2019 RCT; Meichenbaum 1985 | No RCTs for HCW target population |
| DMN voluntary control | 5 | 2a--2b | Supported | Sezer 2022; Bauer 2019 | CRNA-specific application |
| Co-regulation | 4 | 2b--4 | Partially supported | Wespi 2025 (n=214 medical teams) | Team breath intervention unvalidated |
| Alpha-theta crossover | 4 | 2b | Partially supported | Established neurofeedback literature | Consumer EEG validation needed |
| State transition | 4 | 4--5a | Partially supported | Neuroimaging; clinical observation | 90-second claim weakly sourced |
| Interoceptive literacy | 3 | 5a--SRL-O | Partially supported | MAIA-2 subscales validated individually | Term not in published literature |
| Gamma-state binding | 3 | 2b (correlational) | Partially supported | Ferrarelli 2013; Lee 2025 | Practice-type dependent; overclaiming risk |
| Hemispheric rebalancing | 3 | 5b | Partially supported | Yordanova 2020 lateralized patterns | Not a neuroscience term; reframe needed |
| Awe as regulation | 3 | 4 | Partially supported | Shiota 2011; Stellar 2015 | Deployability as clinical tool undemonstrated |
| Curiosity as clinical stance | 3 | 4 (reappraisal lit) | Partially supported | Wang 2024; Burr 2021 | No curiosity-specific training studies |
| Hormesis-durability model | 3 | 2b (biological) | Partially supported | Ricon-Becker 2021; Holton 2026 scoping review | Psychological hormesis minimally validated |
| NeuroHarmonics | 2 | C+ (binaural entrainment inconsistent) | Weakly supported | Ingendoh 2023: 5/14 studies supportive | Entrainment mechanism not reliable |
| Interoceptive suppression hypothesis | 2 | 4--5a (indirect) | Hypothesis --- untested | De Berardis 2023; Crivelli 2025 | Zero direct empirical tests |
| State drift | 2 | 4 (indirect) | Hypothesis --- untested | Li 2022; McGarry 2023 | No named construct in literature |
| Cardiac-anchored breathing | 2 | 4 (1 study) | Insufficient evidence | Ren & Zhang 2019 | No head-to-head comparison |
| MAIA-2-CRNA | 2 | N/A (instrument) | Instrument not yet developed | MAIA-2 base validated; COSMIN methodology available | Complete greenfield |
| Embodied metacognition | 2 | 5a--5b | Hypothesis --- untested | Nikolova 2025; Chemis 2025 | Needs differentiation from somatic marker hypothesis |
| Contemplative progressive overload | 1--2 | 5b | Hypothesis --- untested | None directly | Contradicts dominant contemplative frameworks |
| Nondual clinical awareness | 2 | 4--5b | Speculative | Cooper 2022 TRoM; Josipovic 2019 | Requires thousands of practice hours |
| NeuroMinute (60-second dose) | 2 | 4 (diagnostic) | Insufficient evidence | 1-min deep breathing test (diagnostic); Balban 2023 (5 min) | No therapeutic validation below 5 min |
| Five-Breath Re-Embodiment | 2 | 5a--SRL-O | Insufficient evidence | Resonant breathing components validated | Specific 5-breath sequence unvalidated |
| Diaphragmatic blindness | 2 | 5a--SRL-P | Partially supported | Garfinkel 2017 respiratory interoception; SRL field data (28/30) | No published studies on construct |
| Autonomic home base | 2 | 5b | Partially supported | Meditation trait literature | Novel SRL concept |
| Vitarka-vicara integration | 1--2 | 5b--SRL-O | Speculative | Yordanova 2020 lateralized meditation patterns | No empirical validation of synthesis |

*Asterisk on PVT: Strong real-world validation for interventions; theoretical framework under active expert challenge.*

---

### Appendix B: PubMed Reference List

References are organized by domain. PMIDs and DOIs are provided where available.

#### Autonomic Regulation and HRV

1. Galin et al. (2026). HRV as prospective predictor of depressive symptoms; meta-analysis of 56 studies. DOI: 10.1016/j.jad.2026.121388
2. Vann-Adibe et al. (2025). Remote HRV-B meta-analysis; medium effect sizes. DOI: 10.1007/s10484-025-09750-w
3. Gitler et al. (2025). HRV-B and SSP review for cardiovascular and autonomic regulation. DOI: 10.3892/mi.2025.236
4. Thayer & Lane (2000). Neurovisceral integration model. PMID: 11163422. DOI: 10.1016/s0165-0427(00)00338-4
5. Thayer & Lane (2009). Heart-brain connection elaboration. PMID: 18771686. DOI: 10.1016/j.neubiorev.2008.08.004
6. Thayer et al. (2012). HRV + neuroimaging meta-analysis. PMID: 22178086. DOI: 10.1016/j.neubiorev.2011.11.009
7. Smith, Thayer, Khalsa & Lane (2017). Hierarchical NVI with predictive coding. PMID: 28188890. DOI: 10.1016/j.neubiorev.2017.02.003
8. Shaffer, McCraty & Zerr (2014). Integrative HRV review. PMID: 25324790. DOI: 10.3389/fpsyg.2014.01040
9. Jennings et al. (2015). NVI limits. PMID: 25160649. DOI: 10.1111/psyp.12319

#### Polyvagal Theory Debate

10. Grossman et al. (2026). "Why The Polyvagal Theory Is Untenable." PMID: 41768017. DOI: 10.36131/cnfioritieditore20260110
11. Porges (2026). "When A Critique Becomes Untenable." PMID: 41768026. DOI: 10.36131/cnfioritieditore20260111
12. Porges (2025). PVT current status, clinical applications. DOI: 10.36131/cnfioritieditore20250301
13. Porges (2025). PVT journey from observation to clinical insight. DOI: 10.3389/fnbeh.2025.1659083

#### Resonant Breathing and Baroreflex

14. Laborde et al. (2022). Meta-analysis of VSB and HRV, 223 studies. DOI: 10.1016/j.neubiorev.2022.104711
15. Sevoz-Couche & Laborde (2022). Resonant frequency mechanism review. DOI: 10.1016/j.neubiorev.2022.104576
16. Shaffer & Meehan (2020). Resonance frequency assessment guide. DOI: 10.3389/fnins.2020.570400
17. Vaschillo, Lehrer et al. (2002). Baroreflex resonance. PMID: 12001882. DOI: 10.1023/a:1014587304314
18. Lehrer et al. (2020). Phase relationships in resonance breathing. PMID: 32285231. DOI: 10.1007/s10484-020-09459-y
19. Lehrer (2022). HRV biofeedback research review. PMID: 35254592. DOI: 10.1007/s10484-022-09535-5
20. Sakakibara et al. (2020). LF-peak paced breathing enhances BRS. PMID: 31781925. DOI: 10.1007/s10484-019-09453-z
21. Giorgi & Tedeschi (2025). Slow breathing + HRV review. PMID: 40252198. DOI: 10.1007/s13760-025-02789-w
22. You et al. (2023). SPB dose-response across frequencies. DOI: 10.1007/s10484-023-09605-2
23. Xiong et al. (2025). 0.1 Hz SPB + heartbeat oscillatory potential. PMID: 40452884. DOI: 10.1016/j.ijchp.2025.100571
24. Plantard et al. (2025). HEP changes with blood pressure and slow-paced breathing. DOI: 10.1152/jn.00118.2025
25. Balban et al. (2023). Brief structured respiration practices enhance mood. DOI: 10.1016/j.xcrm.2022.100895
26. Pingali & Hunter (2022). Slow breathing and BP regulation. DOI: 10.1016/j.autneu.2022.103050

#### Interoception

27. Garfinkel et al. (2015). Interoceptive trichotomy. PMID: 25451381. DOI: 10.1016/j.biopsycho.2014.11.004
28. Garfinkel et al. (2017). Cardiac vs respiratory interoception. PMID: 28080971. DOI: 10.1098/rstb.2016.0014
29. Harrison et al. (2021). Filter Detection Task for respiratory interoception. PMID: 34487805. DOI: 10.1016/j.biopsycho.2021.108185
30. Nikolova et al. (2025). Brain microstructure of respiratory interoception. PMID: 40750358. DOI: 10.1523/JNEUROSCI.0787-24.2025
31. Chemis et al. (2025). Breathing interoception, amygdala-insula connectivity. PMID: 40835808. DOI: 10.3758/s13415-025-01328-7
32. Bravo et al. (2025). COSMIN review: MAIA-2 best body awareness PROM. PMID: 41464339. DOI: 10.3390/healthcare13243270
33. Mehling et al. (2012). Original MAIA development. DOI: 10.1371/journal.pone.0048230
34. Fiskum et al. (2023). Norwegian MAIA-2 validation. PMID: 37430262. DOI: 10.1186/s12888-023-04946-y
35. Teng et al. (2022). Chinese MAIA-2 validation. PMID: 36440402. DOI: 10.3389/fpsyt.2022.970982
36. Scheffers et al. (2024). Dutch MAIA-2 validation. DOI: 10.1186/s40359-024-01553-8
37. Lavretsky et al. (2026). Interoceptive regulation in brain health. PMID: 41606214. DOI: 10.1038/s41386-026-02332-2
38. Matus et al. (2026). MAIA-2 moderates hypoglycemia awareness. PMID: 41467850. DOI: 10.2337/dc25-2242
39. Salvato et al. (2021). MAIA Trusting predicts clinical decision-making. PMID: 34437629. DOI: 10.1371/journal.pone.0256806
40. Caparco et al. (2025). Phase confusion / HEARTS framework. PMID: 40582489. DOI: 10.1016/j.biopsycho.2025.109078

#### ISH and Clinician Interoception

41. De Berardis et al. (2023). Alexithymia 14.8% in 1445 HCWs. DOI: 10.3390/brainsci13111550
42. Riethof et al. (2020). Alexithymia-burnout r=0.41. PMID: 31906730. DOI: 10.1177/0300060519887633
43. Aldaz et al. (2019). Alexithymia > EI for burnout prediction. DOI: 10.1111/jan.14153
44. Crivelli et al. (2025). Neurophenomenological stress in neurosurgeons. PMID: 40357485. DOI: 10.3389/fpsyg.2025.1568430
45. Mensinger et al. (2024). HRVB restores interoception in HCWs. PMID: 38502516. DOI: 10.1007/s10484-024-09621-w
46. Mensinger (2025). MAIA-2 subscales as HRV biofeedback mediators. PMID: 41319396. DOI: 10.1016/j.eatbeh.2025.102060
47. Dale et al. (2025). Somatic intervention for healthcare worker distress. PMID: 41464305. DOI: 10.3390/healthcare13243236
48. Zhou et al. (2025). MBSR for nurse burnout: interoceptive mechanism. PMID: 40933167. DOI: 10.5498/wjp.v15.i9.107630
49. Handford et al. (2013). Clinical practice and empathy. PMID: 23755185. DOI: 10.1371/journal.pone.0065159
50. Shanafelt & Habermann (2002). Medical resident emotional well-being. DOI: 10.1001/jama.288.15.1846

#### State Drift and Shift-Level HRV

51. Li et al. (2022). Intra-shift HRV changes in nurses. DOI: 10.3389/fpubh.2021.810577
52. Zhan et al. (2024). Night shift autonomic effects. DOI: 10.1186/s12912-024-02563-y
53. Hamidi Shishavan et al. (2022). 24hr wearable monitoring ICU nurses. DOI: 10.1016/j.apergo.2022.103937
54. McGarry et al. (2023). Vagal tone + vigilance decrement. DOI: 10.3389/fnrgo.2023.1244658
55. Tsakmaki et al. (2026). HRV predicts cognitive fatigue via LSTM. DOI: 10.1007/978-3-032-03402-1_43
56. Chen et al. (2025). Circadian disruption + sympathovagal imbalance. DOI: 10.1016/j.ijcard.2025.133463

#### Cardiac-Anchored Breathing and Cardiac Phase Effects

57. Ren & Zhang (2019). Heartbeat-synchronized breathing. PMID: 31109326. DOI: 10.1186/s12938-019-0683-9
58. Schafer et al. (1998). Heartbeat synchronized with ventilation (Nature). PMID: 9521318. DOI: 10.1038/32567
59. Eckberg, Kifle & Roberts (1980). Respiratory phase + baroreflex. PMID: 7441548. DOI: 10.1113/jphysiol.1980.sp013338
60. Hellman & Stacy (1976). RSA variation with age. PMID: 993161. DOI: 10.1152/jappl.1976.41.5.734
61. Azevedo et al. (2022). Cardiac phase biases trustworthiness. PMID: 36322944. DOI: 10.1177/09567976221131519
62. Arslanova et al. (2023). Time perception + cardiac phase. PMID: 36905931. DOI: 10.1016/j.cub.2023.02.034
63. Veillette et al. (2024). Visual dominance + cardiac afferents. PMID: 39356552. DOI: 10.7554/eLife.95599
64. von Mohr et al. (2023). Social interoception + cardiac phase. PMID: 37336022. DOI: 10.1016/j.cognition.2023.105502
65. Zaccaro et al. (2022). Brain-heart interactions across respiratory cycle. PMID: 35964864. DOI: 10.1016/j.neuroimage.2022.119548
66. Zaccaro et al. (2026). Respiratory-phase modulation of HEP. DOI: 10.1016/j.neuroimage.2026.121711
67. Hamill (2023). ICP pulsatility + neural network synchronization. PMID: 38176935. DOI: 10.31083/j.jin2206143
68. Engelen et al. (2025). Visceral rhythms modulate motor excitability. PMID: 41223212. DOI: 10.1371/journal.pbio.3003478

#### Clinician Burnout and Second-Victim

69. Roger et al. (2024). ICU staff PTSD/anxiety prevalence. DOI: 10.1186/s12991-023-00488-5
70. Raft et al. (2025). Incivility in anesthesia teams. DOI: 10.1016/j.jclinane.2025.111983
71. Bryan et al. (2025). Second-victim syndrome in surgeons meta-analysis. DOI: 10.1093/bjs/znaf258
72. Deng et al. (2025). Second-victim qualitative synthesis. DOI: 10.1016/j.ijnurstu.2025.105248
73. Morgan et al. (2025). AANA Wellness Ambassador integration. DOI: 10.70278/AANAJ/.0000001070
74. von Kanel et al. (2023). Reduced epinephrine response in burned-out physicians. DOI: 10.1016/j.biopsycho.2023.108687
75. Woolley et al. (2025). Reduced IL-6 reactivity in burned-out physicians. DOI: 10.1007/s00702-025-02945-9
76. Langelaan et al. (2007). Burnout and allostatic load. DOI: 10.1007/BF03002995

#### Binaural Beats and Auditory Modulation

77. Ingendoh et al. (2023). Binaural beats entrainment systematic review: 5/14 supportive. DOI: 10.1371/journal.pone.0286023
78. Xiong et al. (2025). BB perioperative anxiety meta-analysis (15 RCTs). DOI: 10.1016/j.ctim.2025.103299
79. Solca et al. (2015). BB interhemispheric coherence (not entrainment). PMID: [see DOI]. DOI: 10.1016/j.heares.2015.09.011
80. Dos Anjos et al. (2024). Isochronic tones > binaural beats for EEG modulation. DOI: 10.1016/j.neuroscience.2024.07.014
81. Kim et al. (2024). 18 Hz BB increased beta power; 40 Hz did not produce gamma. DOI: 10.1093/cercor/bhad459
82. McConnell et al. (2014). Theta BB post-exercise parasympathetic activation. DOI: 10.3389/fpsyg.2014.01248
83. Yang et al. (2025). No frequency-specific difference for anxiety reduction. DOI: 10.1186/s12906-025-04922-x
84. Scala et al. (2025). 6 Hz BB entrains cortex but minimal ANS changes. DOI: 10.14814/phy2.70271
85. Shamsi et al. (2024). BB and pain perception systematic review. DOI: 10.1186/s12906-024-04339-y
86. Melnichuk et al. (2025). Parametric BB investigation. DOI: 10.1038/s41598-025-88517-z

#### Hormesis and Stress Inoculation

87. Holton et al. (2026). Antifragility scoping review: 18 human studies. DOI: 10.1177/00332941261416041
88. Ricon-Becker et al. (2021). Post-stress glucose hormetic training in rats. DOI: 10.1080/10253890.2021.1931677
89. Sterling et al. (2019). StressModex: SIT + exercise for whiplash RCT. DOI: 10.1136/bjsports-2018-100139

#### Neurofeedback and EEG

90. Ferrarelli et al. (2013). Gamma during NREM sleep in meditators. DOI: 10.1371/journal.pone.0073417
91. Lee et al. (2025). Chan meditation gamma EEG. DOI: 10.3390/bs15091213
92. DeLosAngeles et al. (2016). Graded meditation: deeper absorption decreased beta/gamma. DOI: 10.1016/j.ijpsycho.2016.09.020
93. Bauer et al. (2019). DMN-CEN reconfiguration in meditators. DOI: 10.1523/ENEURO.0335-18.2019
94. Sezer et al. (2022). DMN functional connectivity and mindfulness. DOI: 10.1016/j.neubiorev.2022.104583
95. Yordanova et al. (2020). Lateralized meditation EEG patterns. DOI: 10.1038/s41598-020-64324-6
96. Cooper et al. (2022). TRoM: nondual awareness neural model. DOI: 10.1093/nc/niac013

#### Wearable Validation

97. Kinnunen et al. (2020). Oura Ring vs. ECG: r=0.996 HR, r=0.980 HRV. DOI: 10.1088/1361-6579/ab840a
98. Cao et al. (2022). Oura Ring RMSSD accuracy. DOI: 10.2196/27487
99. Sarhaddi et al. (2022). Samsung watch: good sleep HRV, poor awake. DOI: 10.1371/journal.pone.0268361
100. Siswishanto et al. (2026). Wearable SDNN and inflammation. DOI: 10.3390/diagnostics16040538

#### Physiological Synchrony and Co-Regulation

101. Wespi et al. (2025). Physiological synchrony in medical teams (n=214). DOI: 10.1186/s41077-025-00335-5
102. Algumaei et al. (2023). Physiological synchrony predicts team performance. DOI: 10.3390/s23042268

#### Micro-Dose and Brief Interventions

103. Shuai et al. (2019). 6-min breath counting promotes stress recovery. DOI: 10.1016/j.addbeh.2019.106141
104. Goldberg et al. (2021). Brief breath awareness impairs working memory under stress. DOI: 10.1080/02699931.2021.1878113

#### Contemplative Neuroscience

105. Tal et al. (2025). Active Inference framework for meditation. PMID: 41475512. DOI: 10.1016/j.neubiorev.2025.106539
106. Stapleton et al. (2020). 3-day meditation workshop: 11% gamma increase. DOI: 10.1016/j.ibror.2020.10.006

---

*This report was generated on 2026-03-19 by Vigil, the SRL Knowledge Graph Orchestrator, and updated on 2026-03-19 with BioMistral synthesis results (Qwen/Qwen3-32B via HuggingFace Inference API, 8 queries). All PubMed citations are attributed per database terms of use. BioMistral-generated citations are explicitly marked and require independent verification before external use. This document is draft status and should be reviewed before distribution to external collaborators. The assessment reflects the state of the literature as of March 2026 and will require updates as new evidence is published.*

*For questions about methodology, evidence grading criteria, or specific concept assessments, contact the SRL research team.*
