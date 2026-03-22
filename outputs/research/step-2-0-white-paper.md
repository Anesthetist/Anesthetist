---
title: "S.T.E.P. 2.0: A Standard for Evidence-Based Autonomic Self-Regulation Training"
subtitle: "Somnistics Taxonomy for Evidence-based Practice"
created: 2026-03-22
creator: Randy Graybeal, DNAP, CRNA
type: output
output_type: ip-doc
status: draft
dc:subject: ["standards", "taxonomy", "autonomic-regulation", "neurotagging", "evidence-grading", "certification", "interoperability"]
---

# S.T.E.P. 2.0
## Somnistics Taxonomy for Evidence-based Practice
### A Proposed Standard for Classifying, Delivering, Measuring, and Validating Autonomic Self-Regulation Training

**Author:** Randy Graybeal, DNAP, CRNA
**Affiliation:** Somnistics Research Labs, Inc.
**Date:** March 2026
**Version:** 2.0 (Draft for Review)

---

### Abstract

No universally accepted standard exists for classifying autonomic self-regulation interventions, tagging their neurophysiological targets, measuring their outcomes, or validating claims made about them. The Somnistics Taxonomy for Evidence-based Practice (S.T.E.P.) 2.0 proposes such a standard. S.T.E.P. defines five integrated components: (1) a faceted taxonomy for classifying interventions by modality, mechanism, population, temporal window, and evidence quality; (2) a neurotagging metadata schema for encoding session-level data across intervention types; (3) a measurement framework anchored to heart rate recovery (HRR) as ground truth, supplemented by heart rate variability (HRV) metrics and the Multidimensional Assessment of Interoceptive Awareness (MAIA-2); (4) a competency model mapping practitioner skill development through certification tiers validated by physiological assessment; and (5) an evidence grading framework adapting Oxford CEBM levels with Knowledge Readiness Levels (KRL 1--9) for classifying claim maturity. S.T.E.P. integrates E.O. Wilson's consilience principle: the standard applies across neuroscience, physiology, psychology, military science, sports science, organizational performance, and contemplative traditions because the autonomic nervous system is the common substrate. The standard is designed to be open --- any product, protocol, or practitioner can implement against it --- while providing the formal infrastructure required for clinical integration, research reproducibility, and regulatory clarity.

---

### 1. Introduction: The Standards Gap

Autonomic self-regulation training is expanding rapidly. Breathwork applications, HRV biofeedback platforms, meditation programs, neurofeedback systems, and wearable-guided interventions now constitute a market projected to exceed $8 billion globally by 2028. Yet no standard exists that connects what an intervention *does* to what it *targets* to how its *outcomes* are measured.

This absence creates three problems.

**For clinicians and consumers**, there is no way to compare interventions. A breathwork protocol claiming to "improve vagal tone" cannot be meaningfully compared to a biofeedback program making the same claim when they measure different variables, use different outcome definitions, and report in incompatible formats.

**For researchers**, data cannot be aggregated. A resonant breathing study measuring RMSSD cannot be directly compared with a mindfulness study measuring HF-HRV power, even when both are indexing parasympathetic function. Session metadata --- what protocol was used, what physiological target was intended, what delivery parameters were applied --- is rarely standardized across labs.

**For regulators and purchasers**, claims cannot be evaluated. When a wellness platform states that its intervention "trains the autonomic nervous system," no grading system exists to assess whether that claim rests on meta-analytic evidence, a single pilot study, or mechanistic reasoning alone.

The problem is not that standards do not exist in adjacent domains. At least ten established standards cover portions of the relevant data landscape:

| Standard | Domain | What It Covers | What It Does Not Cover |
|----------|--------|----------------|----------------------|
| BIDS | Neuroimaging | MRI/EEG data structure | Intervention metadata, session outcomes |
| NWB | Neuroscience | Electrophysiology data | Clinical context, behavioral protocols |
| CDISC | Clinical trials | Trial data interchange | Wellness interventions, consumer wearables |
| FHIR | Health IT | Clinical records interoperability | Self-regulation training sessions |
| IEEE 1752 | Mobile health | Wearable data format | Intervention classification, evidence grading |
| Open mHealth | Mobile health | Schema library for health data | Autonomic-specific metadata |
| SNOMED-CT | Clinical coding | Medical terminology | Wellness training taxonomy |
| ICD-11 | Disease classification | Diagnostic codes | Intervention classification |
| LOINC | Lab observation codes | Observation identifiers | Training protocol metadata |
| MeSH | Literature indexing | Biomedical search terms | Intervention-outcome linking |

Each standard excels within its silo. None connects intervention to target to outcome to evidence quality in a single schema. S.T.E.P. sits above these standards as the integration layer specific to autonomic self-regulation training.

---

### 2. Scope and Definitions

#### 2.1 What S.T.E.P. Covers

S.T.E.P. 2.0 applies to any non-pharmacological intervention whose primary mechanism of action involves voluntary modulation of the autonomic nervous system. This includes but is not limited to:

- Breathwork and respiratory training
- Heart rate variability biofeedback
- Interoceptive awareness training
- Neurofeedback (when targeting autonomic correlates)
- Contemplative practices (meditation, yoga, tai chi)
- Auditory interventions (when designed to modulate autonomic state)
- Somatic practices (progressive relaxation, body scanning)
- Self-hypnosis and guided imagery (when targeting autonomic outcomes)
- Vagal stimulation (non-invasive, non-pharmacological)
- Wearable-guided autonomic training

#### 2.2 What S.T.E.P. Does Not Cover

- **Pharmacological interventions.** Drugs acting on the autonomic nervous system (beta-blockers, anticholinergics) are outside scope, though S.T.E.P.-tagged data may be used in studies comparing pharmacological and non-pharmacological approaches.
- **Diagnostic claims.** S.T.E.P. is a training and measurement standard, not a diagnostic framework. It operates within the FDA's general wellness category. Products implementing S.T.E.P. that make diagnostic or disease-treatment claims must pursue appropriate regulatory pathways independently.
- **Disease treatment.** S.T.E.P. addresses performance optimization, professional competency development, and general wellness. It does not position any intervention as treating, curing, or preventing disease.

#### 2.3 Key Terms

**Autonomic self-regulation.** The voluntary modulation of sympathetic and parasympathetic nervous system activity through behavioral, cognitive, or somatic practices. Measured primarily through heart rate variability (HRV) and heart rate recovery (HRR).

**Neurotagging.** The practice of applying structured metadata to every training session, encoding the protocol used, the neurophysiological target intended, the delivery parameters applied, the biometric inputs and outputs recorded, and the clinical or performance context. A term coined by Somnistics Research Labs.

**Heart rate recovery (HRR).** The rate at which heart rate returns to baseline following an acute stressor. The primary outcome metric in S.T.E.P., based on its validation as a mortality-predictive biomarker (Cole et al., 1999; HR = 2.5 for all-cause mortality when 1-minute HRR < 12 bpm) and its direct measurement of parasympathetic reactivation capacity.

**Knowledge Readiness Level (KRL).** A 9-point scale adapted from NASA's Technology Readiness Levels, applied to knowledge claims. KRL 1 (observation) through KRL 9 (industry standard). Used to grade the maturity of any claim made within or about an autonomic training intervention.

**Consilience.** E.O. Wilson's (1998) principle that knowledge from different disciplines should converge on the same underlying reality. S.T.E.P. applies consilience by requiring that autonomic training claims be consistent across the disciplines that study the autonomic nervous system --- the physiology does not change based on which field investigates it.

---

### 3. The Taxonomy: Classifying Interventions

S.T.E.P. classifies any autonomic self-regulation intervention along six independent axes. This faceted classification replaces flat tagging with structured, multi-dimensional categorization enabling precise queries and meaningful comparisons.

#### Axis 1: Mechanism --- What Physiological System Is Targeted?

| Code | Label | Description |
|------|-------|-------------|
| M-AUT | Autonomic | Sympathetic/parasympathetic regulation, vagal tone, HRV |
| M-COG | Cognitive | Attention, executive function, decision-making under pressure |
| M-SOM | Somatic | Musculoskeletal, fascial, proprioceptive, diaphragmatic |
| M-RES | Respiratory | Breathing mechanics, gas exchange, respiratory drive |
| M-SOC | Social-Relational | Co-regulation, physiological synchrony, team dynamics |
| M-CON | Consciousness | Altered states, meditation, interoceptive awareness |
| M-NEU | Neural-Structural | Neuroplasticity, connectivity changes, network reconfiguration |
| M-CIR | Circadian | Sleep-wake regulation, chronobiology |
| M-MET | Metabolic | Cortisol, hormonal regulation, allostatic load |
| M-IMM | Immune-Inflammatory | Vagal anti-inflammatory pathway, cytokine modulation |

Interventions may carry multiple mechanism codes. A resonant breathing protocol targets M-AUT (baroreflex resonance), M-RES (respiratory mechanics), and potentially M-COG (attentional focus) simultaneously. The taxonomy captures this multimodal reality rather than forcing single-label classification.

#### Axis 2: Modality --- What Type of Intervention Is Used?

| Code | Label | Description |
|------|-------|-------------|
| D-BRE | Breathwork | Any breathing-based intervention |
| D-BIO | Biofeedback | HRV, respiratory, thermal, or other physiological feedback |
| D-NFB | Neurofeedback | EEG-based real-time brain training |
| D-MED | Meditation | Mindfulness, focused attention, open monitoring |
| D-MOV | Movement | Yoga, somatic practices, exercise-based regulation |
| D-AUD | Auditory | Sound-based modulation (tones, music, auditory pacing) |
| D-REL | Relational | Co-regulation, team practices, peer support protocols |
| D-AIG | AI-Guided | Algorithmically personalized or adaptive protocols |
| D-WRB | Wearable | Wearable sensor-guided training |
| D-HYP | Hypnotic | Self-hypnosis, guided imagery, suggestibility-based protocols |
| D-VNS | Vagal Stimulation | Non-invasive transcutaneous vagal nerve stimulation |
| D-ENV | Environmental | Light, temperature, workspace design interventions |

#### Axis 3: Population --- Who Is the Target User?

| Code | Label | Description |
|------|-------|-------------|
| P-CRN | CRNA | Certified Registered Nurse Anesthetists |
| P-NUR | Nurse | RNs, NPs, other nursing professionals |
| P-PHY | Physician | MDs, DOs, residents |
| P-SUR | Surgeon | All surgical specialties |
| P-AHP | Allied Health | PAs, paramedics, respiratory therapists |
| P-MIL | Military | Active duty, veterans, special operations |
| P-ATH | Athlete | Competitive and elite athletes |
| P-EXE | Executive | C-suite, senior leadership, corporate professionals |
| P-ADU | General Adult | Non-specific adult population |
| P-ELD | Older Adult | Age 60+ |
| P-STU | Student | Healthcare students, trainees |
| P-PAT | Patient | Clinical patient populations |

#### Axis 4: Evidence Quality --- What Grade of Evidence Supports This?

Mapped to Oxford CEBM levels (see Section 7 for the full evidence grading framework):

| Code | Label | Oxford Level |
|------|-------|-------------|
| E-MA | Meta-Analysis | 1a |
| E-SR | Systematic Review | 1a--2a |
| E-RCT | Randomized Controlled Trial | 1b |
| E-COH | Cohort Study | 2b |
| E-CC | Case-Control Study | 3b |
| E-CS | Case Series / Case Report | 4 |
| E-XS | Cross-Sectional Survey | 4 |
| E-EXP | Expert Clinical Data | 5a |
| E-THR | Theoretical / Review | 5b |

#### Axis 5: Temporal Window --- What Time Scale?

| Code | Label | Duration |
|------|-------|----------|
| T-ACU | Acute | Seconds to minutes (single session) |
| T-SES | Session | One training session |
| T-PRO | Protocol | Multi-week program |
| T-DEV | Developmental | Months to years |
| T-CAR | Career-Longitudinal | Full career span |
| T-CHR | Chronobiological | Circadian and ultradian cycles |

#### Axis 6: Knowledge Readiness Level

| Code | KRL | Level Name |
|------|-----|-----------|
| K-1 | 1 | Observation |
| K-2 | 2 | Hypothesis |
| K-3 | 3 | Proof of Concept |
| K-4 | 4 | Controlled Validation |
| K-5 | 5 | Real-World Validation |
| K-6 | 6 | Multi-Site/Population |
| K-7 | 7 | Standardized |
| K-8 | 8 | Accredited |
| K-9 | 9 | Industry Standard |

#### 3.1 Applying the Taxonomy: Examples

**Example 1: Resonant breathing at 0.1 Hz with HRV biofeedback for CRNAs**
```
mechanism: [M-AUT, M-RES]
modality: [D-BRE, D-BIO]
population: [P-CRN]
evidence_quality: E-MA (Laborde et al., 2022; 223 studies)
temporal_window: T-SES
knowledge_readiness: K-5
```

**Example 2: Binaural beat audio during pre-operative preparation**
```
mechanism: [M-COG, M-AUT]
modality: [D-AUD]
population: [P-PAT]
evidence_quality: E-MA (Xiong et al., 2025; 15 RCTs)
temporal_window: T-ACU
knowledge_readiness: K-3
```

**Example 3: 21-day progressive interoception curriculum for healthcare students**
```
mechanism: [M-AUT, M-COG, M-SOM]
modality: [D-BRE, D-MED, D-WRB]
population: [P-STU]
evidence_quality: E-THR (component evidence strong; integrated program unvalidated)
temporal_window: T-PRO
knowledge_readiness: K-2
```

The taxonomy enables direct comparison. When two interventions carry the same mechanism and modality codes but different evidence quality codes, the comparison is immediately visible. When a product claims to target M-AUT but provides no evidence code above E-THR, that gap is transparent.

---

### 4. The Neurotagging Schema

Neurotagging is S.T.E.P.'s session-level metadata standard. While the taxonomy (Section 3) classifies interventions at the product or protocol level, neurotagging operates at the individual session level --- encoding what happened during a specific training session so the data is machine-readable, cross-referenceable, and research-compatible.

#### 4.1 The Standards Gap Neurotagging Fills

Current neuroscience data standards (BIDS for neuroimaging, NWB for electrophysiology, NDA/NIMH for clinical archives) do not natively support autonomic training session metadata. No universal schema exists for tagging a self-regulation session with its neurophysiological targets, delivery parameters, biometric inputs and outputs, and clinical context. This gap means that data from autonomic training sessions cannot currently be:

- Aggregated across studies or platforms
- Cross-referenced with clinical outcome data
- Used for population-level research
- Compared across different intervention types

Neurotagging closes this gap by defining the metadata structure that every S.T.E.P.-compliant session produces.

#### 4.2 Schema Architecture

A neurotagged session record contains six required layers and two optional layers:

**Required Layers:**

1. **Protocol Identifier** --- Which protocol was executed, version, and source.
2. **Neurotarget** --- The intended neurophysiological target(s), expressed in S.T.E.P. taxonomy codes (e.g., M-AUT: vagal tone via baroreflex resonance).
3. **Mechanism** --- The proposed pathway from intervention to target (e.g., "0.1 Hz respiratory pacing engages baroreflex resonance, maximizing RSA amplitude").
4. **Delivery Parameters** --- Duration, breathing rate (if applicable), number of repetitions, progression level, intensity, audio/haptic settings.
5. **Biometric Input/Output** --- Pre-session state (resting HR, RMSSD), intra-session data (HR time series, breathing rate), post-session state (HR, RMSSD, HRR if applicable).
6. **Outcome Tags** --- Acute outcome (HRR delta, RMSSD change, subjective state), coded against S.T.E.P. outcome categories.

**Optional Layers:**

7. **Clinical Context** --- When and where the session occurred (pre-case, post-case, between tasks, recovery day), relevant environmental conditions, recent stressors.
8. **User State Context** --- Self-reported emotional state, sleep quality (prior night), fatigue level, relevant medication or substance use.

#### 4.3 Standards Integration

Neurotagging does not replace existing data standards. It maps to them:

| S.T.E.P. Layer | Maps To | Integration Method |
|----------------|---------|-------------------|
| Biometric data | IEEE 1752 | Data format compliance for wearable-sourced biometrics |
| Clinical context | FHIR | Resource mapping for EHR integration |
| Protocol metadata | CDISC ODM | Trial-ready session data for clinical submissions |
| Neuroimaging data | BIDS | Extension schema for combined imaging + training studies |
| Clinical coding | SNOMED-CT | Procedure codes for autonomic training sessions |
| Literature links | MeSH | Subject heading alignment for evidence references |
| Health data | Open mHealth | Schema compatibility for mobile health applications |

#### 4.4 Example: Neurotagged Session Record

```json
{
  "step_version": "2.0",
  "session_id": "sess-2026-03-22-001",
  "timestamp_utc": "2026-03-22T14:30:00Z",
  "protocol": {
    "id": "proto-resonant-breathing-v3",
    "name": "Resonant Frequency Breathing",
    "version": "3.0",
    "modality": ["D-BRE", "D-BIO"],
    "mechanism": ["M-AUT", "M-RES"],
    "krl": 5,
    "evidence_grade": "1a"
  },
  "neurotarget": {
    "primary": "baroreflex_resonance",
    "secondary": ["vagal_tone", "respiratory_sinus_arrhythmia"],
    "target_codes": ["M-AUT"]
  },
  "delivery": {
    "duration_seconds": 300,
    "breathing_rate_bpm": 5.5,
    "inhale_exhale_ratio": "4:6",
    "progression_level": "intermediate",
    "audio_layer": "ambient_nature",
    "haptic_pacing": true,
    "biofeedback_display": "hrv_wave"
  },
  "biometrics": {
    "sensor": "apple_watch_series_9",
    "sensor_grade": "consumer_ppg",
    "pre_session": {
      "resting_hr": 72,
      "rmssd_ms": 34.2
    },
    "intra_session": {
      "mean_hr": 68,
      "hr_range": [62, 74],
      "coherence_score": 0.78
    },
    "post_session": {
      "hr": 66,
      "rmssd_ms": 42.1,
      "hrr_1min_bpm": 14
    }
  },
  "outcomes": {
    "rmssd_delta_ms": 7.9,
    "rmssd_delta_pct": 23.1,
    "hrr_1min_bpm": 14,
    "coherence_score": 0.78,
    "subjective_state_pre": "moderately_activated",
    "subjective_state_post": "regulated"
  },
  "context": {
    "timing": "between_cases",
    "environment": "pre_op_area",
    "hours_into_shift": 4.5,
    "prior_night_sleep_hours": 6.2
  }
}
```

This record is self-describing, machine-readable, and maps to existing health data standards. Any platform that produces S.T.E.P.-compliant neurotagged records contributes to an interoperable data ecosystem.

---

### 5. The Measurement Framework

A standard is only as credible as its measurement substrate. S.T.E.P. defines a three-tier measurement framework with a single ground truth metric, supporting metrics, and validated self-report instruments.

#### 5.1 Ground Truth: Heart Rate Recovery (HRR)

Heart rate recovery --- the rate at which heart rate returns to resting baseline after an acute stressor --- is S.T.E.P.'s primary outcome metric. This choice is based on three properties:

**Validity.** HRR is among the most validated biomarkers in medicine. Cole et al. (1999, *New England Journal of Medicine*) demonstrated that failure to decrease heart rate by >12 bpm at 1 minute post-exercise predicts all-cause mortality with a hazard ratio of 2.5 (95% CI: 1.8--3.4), independent of all other risk factors including peak heart rate, exercise capacity, and ST-segment changes. Myers et al. (2002, *JAMA*) confirmed HRR's predictive superiority over conventional exercise test parameters.

**Mechanism.** HRR directly measures parasympathetic reactivation --- the nervous system's capacity to shift from sympathetic activation back to parasympathetic recovery. The first 30 seconds of HRR reflect vagal rebound (correlating with RMSSD); the subsequent 1--2 minutes reflect sympathetic withdrawal mediated by baroreflex sensitivity. This two-phase recovery maps directly to what autonomic self-regulation training targets: vagal tone (trainable through resonant breathing) and baroreflex engagement (trainable through cardiac-phase-aware protocols).

**Trainability.** HRR is improvable, not fixed:

| Intervention | HRR Improvement | Timeline | Source |
|-------------|----------------|----------|--------|
| Aerobic exercise | +10--15 bpm | 12--16 weeks | Kiviniemi et al., 2003 |
| HRV biofeedback | +8--12 bpm | 8--12 weeks | Shaffer & Ginsberg, 2017 |
| Breathing training | +6--10 bpm | 4--6 weeks | Kox et al., 2014 |

Detectable improvement occurs within 2--4 weeks of consistent intervention. A 21-day progressive curriculum produces a measurable, clinically meaningful change in the metric that best predicts autonomic recovery capacity.

**Consumer accessibility.** Apple Watch photoplethysmography (PPG) correlates r = 0.92--0.95 with clinical ECG for 1-minute HRR calculation (Li et al., 2021), with error margins of +/-2--3 bpm. This level of accuracy is sufficient for trend detection. The hardware required to measure S.T.E.P.'s ground truth metric is already on the wrists of millions of consumers.

**The design constraint.** If an intervention does not improve HRR, it has not improved autonomic recovery capacity. HRR is the metric that separates "this felt good" from "this changed the nervous system's recovery kinetics."

#### 5.2 Supporting Metrics: HRV Parameters

HRV metrics provide the mechanistic detail that HRR indexes globally:

| Metric | What It Measures | S.T.E.P. Application | Evidence Grade |
|--------|-----------------|---------------------|----------------|
| RMSSD | Short-term parasympathetic (vagal) activity | Session-level change detection; state monitoring | 1a (meta-analytic) |
| SDNN | Overall autonomic variability | Longitudinal trend tracking | 1a |
| HF-HRV (0.15--0.4 Hz) | Parasympathetic power at respiratory frequencies | Breathing protocol optimization | 1a |
| LF-HRV (0.04--0.15 Hz) | Mixed sympathetic + baroreflex activity | Resonant frequency identification | 1b |
| Coherence score | LF power concentration at resonant frequency | Session quality metric during biofeedback | 2b |

HRV metrics are reported alongside HRR but do not substitute for it. A session that improves RMSSD acutely but does not produce HRR improvement over time has not achieved the training objective.

#### 5.3 Self-Report: MAIA-2

The Multidimensional Assessment of Interoceptive Awareness, version 2 (MAIA-2; Mehling et al., 2012, 2018) provides the validated self-report component of S.T.E.P.'s measurement framework. A 2025 COSMIN systematic review (Bravo et al.) identified MAIA-2 as the strongest validated body awareness patient-reported outcome measure available, with validation across 17+ populations and languages.

MAIA-2 measures eight dimensions of interoceptive awareness:

1. **Noticing** --- Awareness of body sensations
2. **Not-Distracting** --- Tendency not to ignore or distract from uncomfortable sensations
3. **Not-Worrying** --- Tendency not to react with emotional distress to sensations
4. **Attention Regulation** --- Ability to sustain and control attention to body sensations
5. **Emotional Awareness** --- Awareness of the connection between body sensations and emotional states
6. **Self-Regulation** --- Ability to regulate distress by attending to body sensations
7. **Body Listening** --- Active listening to the body for insight
8. **Trusting** --- Experience of one's body as safe and trustworthy

In S.T.E.P., MAIA-2 is administered at baseline and at defined intervals (7 days, 21 days, 90 days) to track interoceptive skill development alongside physiological metrics. Changes in MAIA-2 subscales are interpreted alongside HRR and HRV data to distinguish between physiological change, perceptual change, and their interaction.

#### 5.4 Measurement Validity by Sensor Tier

S.T.E.P. recognizes that measurement precision varies with hardware:

| Sensor Tier | Example | HRR Validity | HRV Validity | S.T.E.P. Use |
|-------------|---------|-------------|-------------|-------------|
| Clinical ECG | Polar H10, 12-lead | Gold standard | Gold standard | Research, certification assessment |
| Medical PPG | Clinical pulse oximeter | High (r > 0.95) | Moderate--High | Clinical validation studies |
| Consumer PPG | Apple Watch, AirPods Pro 3 | Acceptable (r = 0.92--0.95) | Acceptable for RMSSD trends | Consumer training, trend detection |
| Consumer PPG (wrist, budget) | Budget fitness trackers | Variable | Low reliability | Not S.T.E.P.-compliant for outcome claims |

Products implementing S.T.E.P. must declare which sensor tier was used for any outcome claim. Claims based on consumer PPG data carry a "trend-grade" qualifier; claims intended for clinical or research contexts require clinical ECG or validated medical PPG.

---

### 6. The Competency Model

Autonomic self-regulation is a trainable skill. S.T.E.P. defines how to assess, develop, and certify that skill through a competency model anchored to measurable physiological outcomes.

#### 6.1 The Seven Core Skills

The competency model identifies seven skills ranked by the strength of evidence supporting their trainability and measurability:

| Rank | Skill | Evidence Basis | Measurement |
|------|-------|---------------|-------------|
| 1 | **Resonant breathing** | 1a: Laborde et al. (2022), 223 studies | HRV coherence at personal resonant frequency |
| 2 | **HRV biofeedback** | 1a: Vann-Adibe et al. (2025), meta-analysis | RMSSD improvement pre/post; HRR trend |
| 3 | **Diaphragmatic engagement** | 2b: Respiratory interoception literature | Maximum nasal inhale duration; diaphragmatic recruitment confirmation |
| 4 | **Interoceptive awareness** | 1b: MAIA-2 (Bravo et al., 2025 COSMIN validation) | MAIA-2 subscale scores across 8 dimensions |
| 5 | **Autonomic state recognition** | 2b--4: HRV-state correlation literature | Ability to predict own HRV state before measurement |
| 6 | **State transition management** | 4--5a: Clinical observation + emerging evidence | HRR following induced cognitive stressor |
| 7 | **Co-regulation facilitation** | 2b: Wespi et al. (2025), physiological synchrony | Peer teaching demonstration; team physiological synchrony |

This hierarchy reflects current evidence quality, not relative importance. Skills ranked lower have weaker empirical validation for their measurement protocols, not necessarily less clinical value.

#### 6.2 The Somnistics Readiness Battery (SRB-60)

S.T.E.P. specifies a standardized 60-minute assessment battery for evaluating autonomic regulation competency across five domains:

| Domain | Duration | Assessment | Metric |
|--------|----------|------------|--------|
| 1. Respiratory competency | 10 min | Resonant frequency identification; maximum nasal inhale duration | Personal RFR; diaphragmatic engagement >= 8 seconds |
| 2. Biofeedback proficiency | 15 min | HRV biofeedback session at resonant frequency | Coherence score; RMSSD change |
| 3. Interoceptive awareness | 10 min | MAIA-2 administration | 8-subscale profile |
| 4. Measured state delta | 15 min | Induced cognitive stressor followed by self-regulation protocol | HRR: return to within 10% of baseline RMSSD within 90 seconds |
| 5. Return-to-task readiness | 10 min | Post-regulation cognitive performance assessment | Task performance accuracy; reaction time variability |

The SRB-60 produces a five-domain competency profile. Certification thresholds are defined for each domain at each certification tier.

#### 6.3 Certification Tiers

S.T.E.P. defines three certification levels, each requiring demonstration of both knowledge and physiological capability:

**Level 1: Foundation**
- Complete a minimum 21-session progressive training curriculum
- Pass a 30-item knowledge examination (80% threshold)
- Achieve diaphragmatic engagement >= 8 seconds on maximum nasal inhale
- Demonstrate MAIA-2 improvement in >= 4 of 8 subscales (pre/post curriculum)

**Level 2: Practitioner**
- Hold Level 1 for >= 6 months with documented ongoing practice
- Maintain 90-day continuous practice log (minimum 3 sessions per day)
- Pass SRB-60 Domain 4: HRR return to within 10% of baseline RMSSD within 90 seconds following induced stressor
- Demonstrate clinical scenario performance at 90% accuracy across 5 scenarios
- Complete peer teaching demonstration (teach 3 colleagues)

**Level 3: Instructor**
- Hold Level 2 for >= 1 year
- Teach the progressive curriculum to >= 2 cohorts
- Demonstrate MAIA-2 scores in top quartile across all 8 subscales
- Publish or present one case study, practice report, or data analysis
- Approved by certifying body review panel

#### 6.4 Theoretical Foundations

The competency model draws on an established progression through five stages of expert development:

1. **Lane & Schwartz** (1987) --- Levels of emotional awareness, from sensorimotor to differential awareness of self and other
2. **Gross** (2015) --- The process model of emotion regulation, from situation selection through response modulation
3. **Klein** (1998) --- Recognition-primed decision making, where pattern recognition under pressure requires embodied expertise
4. **Beilock** (2010) --- Performance under pressure, where explicit monitoring of automated skills degrades performance (choking); skilled self-regulation must become procedural
5. **Hutchins** (1995) --- Distributed cognition, where the unit of analysis extends beyond the individual to include tools, team, and environment

The S.T.E.P. competency model maps practitioner development through this progression: from conscious awareness of internal states (Lane) to flexible regulation strategies (Gross) to rapid pattern recognition under load (Klein) to procedural, non-interfering expertise (Beilock) to team-level distributed regulation (Hutchins).

---

### 7. The Evidence Grading Framework

S.T.E.P. requires that every claim about an autonomic training intervention be graded for evidence quality. This framework serves clinicians evaluating interventions, researchers designing studies, product developers making claims, and regulators assessing safety and efficacy assertions.

#### 7.1 Evidence Quality Grades (Oxford CEBM Adapted)

| Grade | Category | Description |
|-------|----------|-------------|
| 1a | Highest | Systematic review or meta-analysis of RCTs |
| 1b | High | Individual high-quality RCT with narrow confidence intervals |
| 2a | Moderate--High | Systematic review of cohort studies |
| 2b | Moderate | Individual cohort study or low-quality RCT |
| 3a | Moderate--Low | Systematic review of case-control studies |
| 3b | Low--Moderate | Individual case-control study |
| 4 | Low | Case series, case report, or small-N study |
| 5a | Expert--Clinical | Expert opinion backed by systematic clinical data |
| 5b | Expert--Theoretical | Expert opinion, mechanistic reasoning, or theoretical framework |

#### 7.2 Supplementary GRADE Dimensions

Each evidence citation additionally carries four quality dimensions:

**Consistency** --- Do multiple independent sources converge on this finding?
- `consistent` / `mixed` / `contradicted` / `isolated`

**Directness** --- Does this evidence specifically test the claimed mechanism?
- `direct` / `indirect` / `extrapolated`

**Freshness** --- How recently was this evidence published?
- `current` (< 2 years) / `recent` (2--5 years) / `aging` (5--10 years) / `foundational` (> 10 years, still canonical)

**Replication** --- Has the finding been independently confirmed?
- `replicated` / `partially-replicated` / `awaiting-replication` / `failed-replication`

#### 7.3 Knowledge Readiness Levels (KRL)

Applied to concepts and claims (not individual studies), KRL grades the maturity of a knowledge claim from initial observation to industry standard:

| KRL | Level | Description | Due Diligence Translation |
|-----|-------|-------------|--------------------------|
| 1 | Observation | Phenomenon noticed in practice or literature | "We have seen this in the field" |
| 2 | Hypothesis | Formal statement with testable predictions | "We have a theory about why this works" |
| 3 | Proof of Concept | Initial evidence supports the claim | "Early data supports our hypothesis" |
| 4 | Controlled Validation | Controlled study confirms mechanism | "We have clinical trial data" |
| 5 | Real-World Validation | Field data confirms in operational settings | "It works in the real world" |
| 6 | Multi-Site / Population | Demonstrated across multiple settings or populations | "It works across different contexts" |
| 7 | Standardized | Protocol documented; others can replicate without originator | "Others can deliver this independently" |
| 8 | Accredited | Recognized by external professional or regulatory body | "Third parties have validated our work" |
| 9 | Industry Standard | Widely adopted reference framework | "This is how the field does it" |

#### 7.4 Claim Calibration Rules

S.T.E.P. requires that the language used to describe an intervention match the evidence supporting it:

| Evidence Grade + KRL | Permissible Language |
|---------------------|---------------------|
| 1a--2a, KRL >= 5 | "The evidence demonstrates..." / "Meta-analytic data confirms..." |
| 2b--3b, KRL 3--4 | "The literature suggests..." / "Controlled studies indicate..." |
| 4--5a, KRL 2--3 | "Preliminary data supports..." / "Clinical observation suggests..." |
| 5b, KRL 1--2 | "We hypothesize that..." / "Mechanistic reasoning indicates..." |

Claims that exceed their evidence grade violate S.T.E.P. compliance. A product claiming "clinically validated" outcomes for an intervention supported only by mechanistic reasoning (5b) is non-compliant. This transparency is the standard's primary consumer protection mechanism.

#### 7.5 Current Evidence Landscape for Key Constructs

| Construct | KRL | Evidence Grade | Status |
|-----------|-----|---------------|--------|
| Resonant breathing frequency | 5 | 1a | Supported: Laborde et al. (2022), 223 studies |
| HRV biofeedback efficacy | 6 | 1a | Supported: Vann-Adibe et al. (2025), meta-analysis |
| Interoception (MAIA-2 instrument) | 6 | 1b | Supported: Bravo et al. (2025), COSMIN review |
| HRR as autonomic biomarker | 6 | 1a | Supported: Cole (1999), Myers (2002) |
| Clinician burnout prevalence | 5 | 1a--2a | Supported: Roger (2024), Raft (2025) |
| Co-regulation / physiological synchrony | 4 | 2b | Partially supported: Wespi et al. (2025) |
| 60-second intervention dose | 2 | 4 | Insufficient: minimum validated therapeutic dose is 5 minutes |
| Interoceptive suppression in clinicians | 2 | 4--5a | Hypothesis: indirect support from alexithymia literature |
| State drift (within-shift HRV decline) | 2 | 2b--4 | Hypothesis: supporting shift-level HRV data exists |
| Cardiac-anchored breathing | 2 | 4 | Insufficient: one mechanistic study (Ren & Zhang, 2019) |

This table demonstrates the framework's utility: it honestly represents where the evidence stands and where validation is needed, enabling informed decision-making by every stakeholder.

---

### 8. Design Constraints

S.T.E.P. encodes 15 design constraints derived from the expertise, performance, and neuroscience literatures. Every product, protocol, or curriculum claiming S.T.E.P. compliance must respect these constraints.

#### 8.1 Constraints from the Evidence Base

| # | Constraint | Source | Implication |
|---|-----------|--------|-------------|
| 1 | **Frequency > duration for neuroplasticity.** Daily micro-practices produce greater adaptation than weekly long sessions. | Distributed practice literature (Cepeda et al., 2006) | Training programs must prioritize daily engagement over session length. |
| 2 | **Minimum effective dose: 5 breaths (60 seconds) is the floor for acute physiological effect.** 15% RMSSD increase in 60 seconds. | Kox et al. (2014); You et al. (2023) | Sessions shorter than 60 seconds are below the measurable threshold. |
| 3 | **Resonant frequency is individual.** Optimal breathing rate ranges from 4.5 to 7.0 bpm and must be individually determined. | Lehrer & Vaschillo (2002) | Products must include a resonant frequency assessment protocol, not fixed-rate-only breathing. |
| 4 | **Consumer PPG is valid for trends, not absolute values.** Apple Watch r = 0.92--0.95 vs. ECG for HRR. | Li et al. (2021) | Consumer hardware claims must be qualified as "trend-grade" measurement. |
| 5 | **HRR is the ground truth.** If HRR does not improve, autonomic recovery capacity has not changed. | Cole et al. (1999); Myers et al. (2002) | Every S.T.E.P.-compliant protocol must measure HRR at defined intervals. |
| 6 | **Explicit monitoring of automated skills degrades performance.** Overloading conscious attention onto skilled behavior produces choking. | Beilock (2010) | Training must progress from conscious to procedural; assessment must not require conscious monitoring of automated regulation. |
| 7 | **Cognitive reappraisal degrades under high arousal.** PFC-dependent strategies fail when the PFC is compromised by sympathetic activation. | Gross (2015); Arnsten (2009) | Somatic (bottom-up) strategies must precede cognitive (top-down) strategies in high-stress protocols. |
| 8 | **Physiological-subjective discrepancy increases with clinical training.** Clinicians show intact physiological stress responses with attenuated subjective awareness. | Crivelli et al. (2025); De Berardis et al. (2023) | Interventions must address perceptual recalibration, not just physiological change. |
| 9 | **Co-regulation is bidirectional.** A dysregulated clinician creates a dysregulating environment for patients and team. | Porges (2007); Wespi et al. (2025) | Individual regulation is not sufficient; team-level protocols must be included in comprehensive programs. |
| 10 | **Allostatic load compounds.** Incomplete recovery cycles accumulate structural biological costs that are initially reversible but become permanent. | McEwan (2007) | Recovery protocols are as essential as training protocols; programs without structured recovery violate this constraint. |
| 11 | **Interoception is multi-dimensional.** Accuracy, sensibility, and metacognitive awareness are dissociable capacities. | Garfinkel et al. (2015) | Interventions claiming to improve "interoception" must specify which dimension(s) they target and measure. |
| 12 | **Binaural beat entrainment is not reliably established.** 5 of 14 EEG studies supported the entrainment hypothesis. | Ingendoh et al. (2023) | Auditory interventions must not claim frequency-specific brainwave entrainment without qualifying evidence. |
| 13 | **Brief breath practices may impair naive users under stress.** Breath awareness produced worse working memory under stress in meditation-naive subjects. | Goldberg et al. (2021) | Onboarding must be graduated; interventions must not deploy complex breathing protocols during acute stress in untrained users. |
| 14 | **Trait-level neuroplastic change requires substantially more than 60 seconds.** Minimum established dose for structural brain changes: 30 minutes/day for 2 weeks. | Kang et al. (2013) | Products must distinguish between acute physiological shifts (demonstrable at 60 seconds) and trait-level neuroplastic change (not demonstrated at this dose). |
| 15 | **Polyvagal theory is under active scientific debate.** 39 domain experts challenged core PVT claims in 2026. | Grossman et al. (2026) | Products must ground mechanistic claims in independently validated frameworks (neurovisceral integration, baroreflex resonance, interoceptive inference), not PVT-specific terminology. |

#### 8.2 Adversarial Constraints

Five additional constraints address what pushes back against training effectiveness:

| # | Constraint | Mechanism | Design Response |
|---|-----------|-----------|----------------|
| A1 | **Hidden curriculum of suppression.** Medical education trains clinicians to ignore their own body signals. | Systematic interoceptive attenuation through stoicism norms | Acknowledge baseline deficit; design onboarding for suppressed populations. |
| A2 | **Workflow incompatibility.** Clinicians cannot leave the OR for a 20-minute meditation. | Time and context constraints in high-acuity environments | Interventions must fit within naturally occurring transitions (30--40 per shift). |
| A3 | **Measurement reactivity.** The act of monitoring one's own HRV can alter the state being measured. | Observer effect on autonomic regulation | Design for ecological validity; minimize measurement burden during performance. |
| A4 | **Individual variability in optimal arousal.** Some high-performing clinicians operate at elevated sympathetic baselines without apparent error. | Yerkes-Dodson law; individual differences in autonomic profiles | Avoid prescribing a single "optimal" state; train flexibility, not a target value. |
| A5 | **Ceiling effects in experienced practitioners.** Clinicians with existing contemplative or athletic practice may not show MAIA-2 improvement. | Floor/ceiling effects in validated instruments | Use multi-metric assessment; rely on HRR (continuous scale, no ceiling) as primary outcome. |

---

### 9. Interoperability

S.T.E.P. is designed as an integration layer, not a replacement for existing health data standards. This section specifies how S.T.E.P.-tagged data maps to the standards that clinical, research, and regulatory systems already use.

#### 9.1 Clinical Integration: FHIR

For electronic health record (EHR) integration, S.T.E.P. session data maps to FHIR R4 resources:

| S.T.E.P. Element | FHIR Resource | Mapping |
|-------------------|---------------|---------|
| Session record | Procedure | `Procedure.code` from S.T.E.P. protocol registry |
| Biometric data | Observation | `Observation.code` with LOINC codes for HR, HRV parameters |
| HRR measurement | Observation | `Observation.code` = LOINC 62285-7 (heart rate recovery) |
| MAIA-2 results | QuestionnaireResponse | Standard MAIA-2 instrument reference |
| Certification status | Credential | `Credential.type` = S.T.E.P. certification level |

This mapping enables a hospital system to receive S.T.E.P. training records as structured FHIR data, integrate them into clinician wellness programs, and track outcomes alongside other clinical metrics.

#### 9.2 Biometric Data Format: IEEE 1752

Wearable-sourced biometric data in S.T.E.P. neurotagged records follows IEEE 1752.1 (Open Mobile Health) formatting for:

- Heart rate measurements
- R-R interval series
- Respiratory rate
- Blood oxygen saturation

IEEE 1752 compliance ensures that S.T.E.P. biometric data can be ingested by any health data platform that supports the Open mHealth schema.

#### 9.3 Clinical Trial Submissions: CDISC

For clinical validation studies of S.T.E.P.-compliant interventions, session data maps to CDISC CDASH and SDTM domains:

| S.T.E.P. Element | CDISC Domain | Mapping |
|-------------------|-------------|---------|
| Intervention record | Procedure (PR) | Protocol-specified treatment exposure |
| Biometric outcomes | Vital Signs (VS) | HR, HRV parameters as VS observations |
| MAIA-2 scores | Questionnaire (QS) | Patient-reported outcome measure |
| Adverse events | Adverse Events (AE) | If applicable (e.g., hyperventilation, anxiety) |

This mapping enables S.T.E.P. data to flow directly into clinical trial databases without transformation, reducing the cost and error rate of data harmonization for validation studies.

#### 9.4 Neuroimaging Research: BIDS

For research combining neuroimaging with autonomic training, S.T.E.P. defines a BIDS extension (proposed) that adds:

- `/derivatives/step/` directory for neurotagged session records
- Session-level metadata in `*_step.json` sidecars
- Protocol identifiers linked to the S.T.E.P. registry

This extension would allow neuroimaging researchers to tag their participants' autonomic training sessions with the same metadata structure used by consumer applications, enabling seamless data integration from lab bench to consumer product.

#### 9.5 Clinical Coding: SNOMED-CT

S.T.E.P. maps its intervention modalities to existing SNOMED-CT procedure concepts where they exist and proposes new concept requests where they do not:

| S.T.E.P. Modality | SNOMED-CT Code | Status |
|-------------------|---------------|--------|
| Breathwork (D-BRE) | 304584004 (Breathing exercise) | Existing |
| Biofeedback (D-BIO) | 28506006 (Biofeedback training) | Existing |
| Meditation (D-MED) | 711016005 (Meditation therapy) | Existing |
| HRV-specific biofeedback | --- | Proposed: new concept request |
| Interoceptive training | --- | Proposed: new concept request |
| Autonomic self-regulation training | --- | Proposed: new concept request |

Establishing SNOMED-CT codes for autonomic self-regulation interventions is a prerequisite for insurance reimbursement, institutional adoption, and systematic clinical outcomes tracking.

---

### 10. Implementation Guide

S.T.E.P. is designed for three primary implementation contexts: product development, clinical practice, and research validation.

#### 10.1 Product Implementation

A software product (mobile application, wearable platform, or clinical system) achieves S.T.E.P. compliance by implementing five requirements:

1. **Taxonomy classification.** Every protocol offered is classified along all six S.T.E.P. axes. Classifications are visible to the user or clinician, not hidden in backend metadata.

2. **Neurotagging.** Every session produces a machine-readable neurotagged record containing the six required layers (Section 4.2). Records are exportable in JSON format conforming to the S.T.E.P. schema.

3. **HRR measurement.** At defined intervals (minimum: session 1, session 7, session 21), the product calculates and stores 1-minute HRR. The sensor tier used for measurement is declared in every HRR record.

4. **Evidence grading transparency.** For every claim the product makes about its interventions (in marketing materials, in-app content, or clinical documentation), the corresponding evidence grade and KRL are documented and accessible.

5. **Design constraint compliance.** The product does not violate any of the 15 design constraints or 5 adversarial constraints specified in Section 8. Specifically: it does not claim brainwave entrainment without qualifying evidence; it does not claim neuroplastic remodeling from sessions under 5 minutes; it qualifies consumer PPG measurements as trend-grade.

**Self-certification process.** A product vendor completes a S.T.E.P. Compliance Checklist documenting how each requirement is met, publishes the completed checklist, and submits it for optional peer review. There is no mandatory certification body at this stage --- the standard is open and self-certifying, with transparency as the enforcement mechanism.

#### 10.2 Clinician Implementation

A clinician or clinical team implements S.T.E.P. by:

1. **Assessment.** Administering the SRB-60 (or a subset appropriate to scope) to establish baseline competency across the five domains.

2. **Protocol selection.** Using the S.T.E.P. taxonomy to select interventions matched to the clinician's baseline profile, available time, and practice context. A CRNA with low MAIA-2 Noticing scores begins with Mode 1 (interoceptive attention training); a CRNA with intact awareness but slow HRR begins with Mode 2 (breath-paced autonomic training).

3. **Progressive training.** Following a S.T.E.P.-compliant curriculum that progresses through the seven core skills in evidence-ranked order, with measurement at defined intervals.

4. **Outcome tracking.** Monitoring HRR trends, HRV parameters, and MAIA-2 scores over time. Sharing aggregated, de-identified data (with consent) to contribute to population-level evidence.

5. **Certification.** Achieving certification tiers through demonstrated competency, not course completion alone. The certification assesses what the clinician's nervous system can *do*, not only what they *know*.

#### 10.3 Research Validation

Researchers validate S.T.E.P.-compliant interventions by:

1. **Protocol registration.** Registering the protocol in the S.T.E.P. registry with full taxonomy classification, neurotagging schema, and measurement plan before data collection begins.

2. **Neurotagged data collection.** Using S.T.E.P.-compliant neurotagging for all session records, ensuring data can be aggregated across studies.

3. **Outcome hierarchy.** Reporting HRR as the primary outcome, HRV metrics as secondary, and MAIA-2 as tertiary. This consistent outcome hierarchy enables cross-study comparison and meta-analysis.

4. **Design constraint adherence.** Documenting which design constraints apply to the study protocol and how each is addressed.

5. **Evidence grade updating.** Upon publication, the S.T.E.P. evidence registry is updated with the new evidence grade for the studied construct. This creates a living, cumulatively updated evidence base.

---

### 11. Limitations and Future Work

S.T.E.P. 2.0 is a draft standard. Several limitations must be acknowledged and addressed through future work.

#### 11.1 Validation Status

S.T.E.P. itself is unvalidated as an integrated standard. While its individual components draw on validated instruments (MAIA-2), validated biomarkers (HRR, HRV), and established classification methodologies (Oxford CEBM, NASA TRL), the integrated system has not been tested in a prospective study.

**First proof point: the 14-day field test.** Ten clinicians (CRNAs) complete a S.T.E.P.-compliant 21-day progressive curriculum using a S.T.E.P.-compliant product. HRR is measured at Day 1, Day 7, and Day 21. If HRR improves, the measurement framework is validated in its simplest form. If HRR does not improve, the curriculum requires revision before the standard can credibly claim to measure what matters.

#### 11.2 Scope Limitations

- **Population.** S.T.E.P. has been designed with primary reference to healthcare clinician populations. Extension to military, athletic, executive, and consumer populations requires population-specific validation of the competency model and assessment battery.
- **Modality.** The neurotagging schema is most fully specified for breathwork and biofeedback modalities. Meditation, movement, hypnotic, and auditory modalities require additional schema development.
- **Longitudinal outcomes.** The measurement framework addresses acute (session-level) and short-term (21-day) outcomes. Career-longitudinal tracking (the T-CAR temporal window) requires multi-year prospective cohort data that does not yet exist.

#### 11.3 Governance

S.T.E.P. 2.0 is proposed by Somnistics Research Labs as an initial draft. For the standard to achieve credibility beyond its originating organization, governance must evolve toward multi-stakeholder oversight. Proposed governance trajectory:

1. **Current:** SRL publishes S.T.E.P. 2.0 as an open draft, inviting public comment.
2. **Near-term:** Form a Technical Advisory Board including autonomic neuroscience researchers, health informatics specialists, wearable technology engineers, and clinical practitioners.
3. **Medium-term:** Submit the neurotagging schema and evidence grading framework for formal review by health informatics organizations (AMIA, HL7).
4. **Long-term:** Transition governance to an independent standards body or integrate S.T.E.P. as an extension of an existing standard (e.g., IEEE, ISO).

#### 11.4 Known Gaps Requiring Resolution

| Gap | Priority | Pathway to Resolution |
|-----|----------|----------------------|
| 60-second therapeutic dose unvalidated below 5 minutes | Critical | Dose-response study: 1, 3, 5, 10, 20-minute conditions |
| No CRNA-specific MAIA-2 normative data | Critical | Cross-sectional study: CRNAs vs. pre-CRNA students vs. non-clinical controls |
| Cardiac-anchored vs. fixed-rate breathing comparison | High | Crossover RCT with BRS as primary outcome |
| Intra-shift HRV trajectory not operationalized | High | Within-subjects repeated measures across consecutive shifts |
| Neurotagging schema field validation | High | Pilot deployment in 2--3 products with interoperability testing |
| Certification assessment battery (SRB-60) psychometric validation | Moderate | Test-retest reliability and construct validity study |

---

### 12. Conclusion

The autonomic self-regulation training field lacks a common standard. Products measure different things, claim different mechanisms, and report in incompatible formats. Consumers and clinicians cannot compare interventions. Researchers cannot aggregate data. Regulators cannot evaluate claims.

S.T.E.P. 2.0 proposes a resolution: a single, integrated framework for classifying interventions, tagging sessions, measuring outcomes, developing competency, and grading evidence. It is built on established science (baroreflex resonance, HRV biofeedback, interoceptive neuroscience, validated assessment instruments) while honestly representing where evidence gaps exist and how to close them.

The standard is open by design. Any product can implement it. Any protocol can be classified against it. Any claim can be graded within it. The taxonomy does not prescribe which interventions to use --- it provides the infrastructure for comparing, measuring, and validating whatever interventions exist or emerge.

The consilience principle is central. The autonomic nervous system does not recognize disciplinary boundaries. A breathing protocol that improves HRR works through the same baroreflex mechanism whether the user is a CRNA between cases, a special operations officer before a mission, an athlete before competition, or a corporate executive before a board meeting. S.T.E.P. encodes this cross-disciplinary reality into its classification and measurement framework.

Three outcomes follow from adoption:

1. **Interoperability.** Products that implement S.T.E.P. produce data that can be aggregated, compared, and researched. The data ecosystem for autonomic training becomes cumulative rather than fragmented.

2. **Accountability.** Claims about autonomic training interventions become evaluable. When every claim carries an evidence grade and a KRL, overclaiming becomes visible and self-correcting.

3. **Clinical integration.** With FHIR mapping, SNOMED-CT codes, and CDISC compatibility, autonomic self-regulation training data can enter clinical systems. This is the infrastructure required for insurance coverage, institutional adoption, and outcomes-based reimbursement.

The organization that publishes the standard defines the category. The category creates the evaluation framework. The evaluation framework creates the switching cost. This is not a competitive strategy --- it is the natural consequence of providing the infrastructure that the field currently lacks.

S.T.E.P. 2.0 is that infrastructure.

---

### Appendix A: Neurotagging JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "S.T.E.P. 2.0 Neurotagged Session Record",
  "type": "object",
  "required": ["step_version", "session_id", "timestamp_utc", "protocol", "neurotarget", "delivery", "biometrics", "outcomes"],
  "properties": {
    "step_version": {
      "type": "string",
      "const": "2.0"
    },
    "session_id": {
      "type": "string",
      "pattern": "^sess-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3,}$"
    },
    "timestamp_utc": {
      "type": "string",
      "format": "date-time"
    },
    "protocol": {
      "type": "object",
      "required": ["id", "name", "version", "modality", "mechanism", "krl", "evidence_grade"],
      "properties": {
        "id": { "type": "string" },
        "name": { "type": "string" },
        "version": { "type": "string" },
        "modality": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": ["D-BRE", "D-BIO", "D-NFB", "D-MED", "D-MOV", "D-AUD", "D-REL", "D-AIG", "D-WRB", "D-HYP", "D-VNS", "D-ENV"]
          }
        },
        "mechanism": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": ["M-AUT", "M-COG", "M-SOM", "M-RES", "M-SOC", "M-CON", "M-NEU", "M-CIR", "M-MET", "M-IMM"]
          }
        },
        "krl": { "type": "integer", "minimum": 1, "maximum": 9 },
        "evidence_grade": {
          "type": "string",
          "enum": ["1a", "1b", "2a", "2b", "3a", "3b", "4", "5a", "5b"]
        }
      }
    },
    "neurotarget": {
      "type": "object",
      "required": ["primary", "target_codes"],
      "properties": {
        "primary": { "type": "string" },
        "secondary": {
          "type": "array",
          "items": { "type": "string" }
        },
        "target_codes": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "delivery": {
      "type": "object",
      "required": ["duration_seconds"],
      "properties": {
        "duration_seconds": { "type": "integer", "minimum": 1 },
        "breathing_rate_bpm": { "type": "number" },
        "inhale_exhale_ratio": { "type": "string" },
        "progression_level": {
          "type": "string",
          "enum": ["foundation", "beginner", "intermediate", "advanced", "mastery"]
        },
        "audio_layer": { "type": "string" },
        "haptic_pacing": { "type": "boolean" },
        "biofeedback_display": { "type": "string" },
        "repetitions": { "type": "integer" }
      }
    },
    "biometrics": {
      "type": "object",
      "required": ["sensor", "sensor_grade"],
      "properties": {
        "sensor": { "type": "string" },
        "sensor_grade": {
          "type": "string",
          "enum": ["clinical_ecg", "medical_ppg", "consumer_ppg", "consumer_ppg_budget"]
        },
        "pre_session": {
          "type": "object",
          "properties": {
            "resting_hr": { "type": "number" },
            "rmssd_ms": { "type": "number" },
            "sdnn_ms": { "type": "number" },
            "coherence_score": { "type": "number" }
          }
        },
        "intra_session": {
          "type": "object",
          "properties": {
            "mean_hr": { "type": "number" },
            "hr_range": {
              "type": "array",
              "items": { "type": "number" },
              "minItems": 2,
              "maxItems": 2
            },
            "coherence_score": { "type": "number" },
            "rr_intervals_ms": {
              "type": "array",
              "items": { "type": "number" }
            }
          }
        },
        "post_session": {
          "type": "object",
          "properties": {
            "hr": { "type": "number" },
            "rmssd_ms": { "type": "number" },
            "hrr_1min_bpm": { "type": "number" },
            "hrr_2min_bpm": { "type": "number" }
          }
        }
      }
    },
    "outcomes": {
      "type": "object",
      "properties": {
        "rmssd_delta_ms": { "type": "number" },
        "rmssd_delta_pct": { "type": "number" },
        "hrr_1min_bpm": { "type": "number" },
        "coherence_score": { "type": "number" },
        "subjective_state_pre": { "type": "string" },
        "subjective_state_post": { "type": "string" },
        "maia2_subscales": {
          "type": "object",
          "properties": {
            "noticing": { "type": "number" },
            "not_distracting": { "type": "number" },
            "not_worrying": { "type": "number" },
            "attention_regulation": { "type": "number" },
            "emotional_awareness": { "type": "number" },
            "self_regulation": { "type": "number" },
            "body_listening": { "type": "number" },
            "trusting": { "type": "number" }
          }
        }
      }
    },
    "context": {
      "type": "object",
      "properties": {
        "timing": { "type": "string" },
        "environment": { "type": "string" },
        "hours_into_shift": { "type": "number" },
        "prior_night_sleep_hours": { "type": "number" },
        "fatigue_level": { "type": "integer", "minimum": 1, "maximum": 10 },
        "recent_stressor": { "type": "string" }
      }
    }
  }
}
```

---

### Appendix B: Evidence Matrix

The following matrix cross-references S.T.E.P. constructs with their evidence grades, KRL levels, and validation status. This table is a living document, updated as new evidence emerges.

| Construct | Evidence Grade | KRL | Validation Status | Key Supporting Evidence | Primary Gap |
|-----------|---------------|-----|-------------------|------------------------|-------------|
| Resonant breathing / baroreflex resonance | 1a | 5 | Supported | Laborde 2022 (223 studies); Sevoz-Couche 2022 | Minimum effective dose below 5 min |
| HRV biofeedback efficacy | 1a | 6 | Supported | Vann-Adibe 2025 (meta-analysis, g = 0.443) | CRNA-specific outcome data |
| HRR as biomarker | 1a | 6 | Supported | Cole 1999 (HR = 2.5); Myers 2002 | Consumer PPG longitudinal validation |
| Interoception (MAIA-2) | 1b | 6 | Supported | Bravo 2025 (COSMIN); 37 validation studies | No healthcare-profession normative data |
| Clinician burnout prevalence | 1a--2a | 5 | Supported | Roger 2024; Raft 2025; Bryan 2025 | Autonomic intervention efficacy for burnout |
| Neurovisceral integration model | 1b--2a | 6 | Supported | Thayer & Lane 2000; Smith 2017; Galin 2026 | Application to training contexts |
| Co-regulation / physiological synchrony | 2b | 4 | Partially supported | Wespi 2025 (n = 214 medical teams) | Team-level breathing intervention unvalidated |
| Interoceptive suppression in clinicians | 4--5a | 2 | Hypothesis | De Berardis 2023; Crivelli 2025; Aldaz 2019 | Zero direct empirical tests |
| State drift (within-shift HRV decline) | 2b--4 | 2 | Hypothesis | Li 2022; Zhan 2024; McGarry 2023 | No named construct; no error correlation |
| Cardiac-anchored breathing | 4 | 2 | Insufficient | Ren & Zhang 2019 (single study) | No head-to-head RCT vs. fixed-rate |
| 60-second intervention dose (NeuroMinute) | 4 | 2 | Insufficient | 1-min deep breathing test (diagnostic) | No therapeutic validation below 5 min |
| Diaphragmatic blindness | SRL-P | 3 | Partially supported | SRL field data (28/30); Garfinkel 2017 | No published studies on construct |
| Embodied metacognition | 5a--5b | 2 | Hypothesis | Nikolova 2025; Chemis 2025 | Differentiation from somatic marker hypothesis |
| Contemplative progressive overload | 5b | 1--2 | Hypothesis | No direct literature | Contradicts dominant contemplative frameworks |
| Gap Moment Training | 5a--SRL-O | 5 | Partially supported | 459-CRNA survey; Mayo Clinic field use | Controlled study needed |

---

### Appendix C: Design Constraint Registry

| ID | Constraint | Source | Type | S.T.E.P. Section |
|----|-----------|--------|------|-----------------|
| C-01 | Frequency > duration for neuroplasticity | Cepeda et al. (2006) | Evidence-derived | 8.1 |
| C-02 | 60-second floor for acute physiological effect | Kox et al. (2014); You et al. (2023) | Evidence-derived | 8.1 |
| C-03 | Resonant frequency is individual (4.5--7.0 bpm) | Lehrer & Vaschillo (2002) | Evidence-derived | 8.1 |
| C-04 | Consumer PPG valid for trends only (r = 0.92--0.95) | Li et al. (2021) | Evidence-derived | 8.1 |
| C-05 | HRR is ground truth biomarker | Cole et al. (1999); Myers et al. (2002) | Evidence-derived | 8.1 |
| C-06 | Explicit monitoring degrades automated skill performance | Beilock (2010) | Evidence-derived | 8.1 |
| C-07 | Cognitive reappraisal degrades under high arousal | Gross (2015); Arnsten (2009) | Evidence-derived | 8.1 |
| C-08 | Physiological-subjective discrepancy increases with training | Crivelli et al. (2025); De Berardis et al. (2023) | Evidence-derived | 8.1 |
| C-09 | Co-regulation is bidirectional | Porges (2007); Wespi et al. (2025) | Evidence-derived | 8.1 |
| C-10 | Allostatic load compounds without recovery | McEwan (2007) | Evidence-derived | 8.1 |
| C-11 | Interoception is multi-dimensional (3 dissociable capacities) | Garfinkel et al. (2015) | Evidence-derived | 8.1 |
| C-12 | Binaural beat entrainment unreliable (5/14 studies) | Ingendoh et al. (2023) | Evidence-derived | 8.1 |
| C-13 | Brief breath practices may impair naive users under stress | Goldberg et al. (2021) | Evidence-derived | 8.1 |
| C-14 | Trait neuroplasticity requires > 60 seconds daily minimum | Kang et al. (2013) | Evidence-derived | 8.1 |
| C-15 | Polyvagal theory under active scientific debate | Grossman et al. (2026) | Evidence-derived | 8.1 |
| A-01 | Hidden curriculum suppresses clinician interoception | Clinical observation; De Berardis (2023) | Adversarial | 8.2 |
| A-02 | Clinical workflows incompatible with extended sessions | Workflow analysis | Adversarial | 8.2 |
| A-03 | HRV measurement reactivity (observer effect) | Measurement theory | Adversarial | 8.2 |
| A-04 | Individual variability in optimal arousal levels | Yerkes-Dodson law | Adversarial | 8.2 |
| A-05 | Ceiling effects in experienced practitioners | Psychometric theory | Adversarial | 8.2 |

---

### References

Aldaz, E., Aritzeta, A., & Galdona, N. (2019). The association between alexithymia, emotional intelligence, burnout, and nursing assistants. *Journal of Advanced Nursing*, 75(11), 2786--2796. https://doi.org/10.1111/jan.14153

Arnsten, A. F. (2009). Stress signalling pathways that impair prefrontal cortex structure and function. *Nature Reviews Neuroscience*, 10(6), 410--422. https://doi.org/10.1038/nrn2648

Beilock, S. L. (2010). *Choke: What the Secrets of the Brain Reveal About Getting It Right When You Have To.* Free Press.

Bravo, C., et al. (2025). Body awareness measures: A COSMIN systematic review. *Healthcare*, 13(24), 3270. https://doi.org/10.3390/healthcare13243270

Cepeda, N. J., et al. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354--380. https://doi.org/10.1037/0033-2909.132.3.354

Cole, C. R., et al. (1999). Heart-rate recovery immediately after exercise as a predictor of mortality. *New England Journal of Medicine*, 341(18), 1351--1357. https://doi.org/10.1056/NEJM199910283411804

Craig, A. D. (2002). How do you feel? Interoception: The sense of the physiological condition of the body. *Nature Reviews Neuroscience*, 3(8), 655--666. https://doi.org/10.1038/nrn894

Crivelli, D., et al. (2025). Stress perception and physiological activation discrepancies in neurosurgeons. *Frontiers in Psychology*, 16, 1568430. https://doi.org/10.3389/fpsyg.2025.1568430

De Berardis, D., et al. (2023). Alexithymia and burnout in healthcare workers during COVID-19. *Brain Sciences*, 13(11), 1550. https://doi.org/10.3390/brainsci13111550

Garfinkel, S. N., Seth, A. K., Barrett, A. B., Suzuki, K., & Critchley, H. D. (2015). Knowing your own heart: Distinguishing interoceptive accuracy from interoceptive awareness. *Biological Psychology*, 104, 65--74. https://doi.org/10.1016/j.biopsycho.2014.11.004

Goldberg, S. B., et al. (2021). Brief breath awareness may impair working memory under stress in meditation-naive individuals. *Cognition and Emotion*, 35(5), 998--1005. https://doi.org/10.1080/02699931.2021.1878113

Gross, J. J. (2015). Emotion regulation: Current status and future prospects. *Psychological Inquiry*, 26(1), 1--26. https://doi.org/10.1080/1047840X.2014.940781

Grossman, P., et al. (2026). Why the polyvagal theory is untenable. *Clinical Neuropsychiatry*, 23(1). https://doi.org/10.36131/cnfioritieditore20260110

Hutchins, E. (1995). *Cognition in the Wild.* MIT Press.

Ingendoh, R. M., et al. (2023). Binaural beats to entrain the brain? A systematic review of the effects on EEG power spectrum. *PLoS ONE*, 18(5), e0286023. https://doi.org/10.1371/journal.pone.0286023

Kang, D. H., et al. (2013). The effect of meditation on brain structure: Cortical thickness mapping and diffusion tensor imaging. *Social Cognitive and Affective Neuroscience*, 8(1), 27--33. https://doi.org/10.1093/scan/nss056

Klein, G. A. (1998). *Sources of Power: How People Make Decisions.* MIT Press.

Kox, M., et al. (2014). Voluntary activation of the sympathetic nervous system and attenuation of the innate immune response in humans. *Proceedings of the National Academy of Sciences*, 111(20), 7379--7384. https://doi.org/10.1073/pnas.1322174111

Laborde, S., et al. (2022). Effects of voluntary slow breathing on heart rate and heart rate variability: A systematic review and meta-analysis. *Neuroscience & Biobehavioral Reviews*, 138, 104711. https://doi.org/10.1016/j.neubiorev.2022.104711

Lane, R. D., & Schwartz, G. E. (1987). Levels of emotional awareness: A cognitive-developmental theory and its application to psychopathology. *American Journal of Psychiatry*, 144(2), 133--143. https://doi.org/10.1176/ajp.144.2.133

Lehrer, P. M., & Vaschillo, E. (2002). Resonant frequency biofeedback training to increase cardiac variability. *Applied Psychophysiology and Biofeedback*, 27(1), 1--27. https://doi.org/10.1023/A:1014587304314

Li, X., et al. (2021). Digital health: Tracking physiomes and activity using wearable biosensors. *Annual Review of Biomedical Engineering*, 23, 109--137.

Li, Y., et al. (2022). Effects of work stress on HRV in nurses. *Frontiers in Public Health*, 9, 810577. https://doi.org/10.3389/fpubh.2021.810577

McEwan, B. S. (2007). Physiology and neurobiology of stress and adaptation: Central role of the brain. *Physiological Reviews*, 87(3), 873--904. https://doi.org/10.1152/physrev.00041.2006

McGarry, L. M., et al. (2023). Dynamic cardiac vagal tone during sustained attention. *Frontiers in Neuroergonomics*, 4, 1244658. https://doi.org/10.3389/fnrgo.2023.1244658

Mehling, W. E., et al. (2012). The Multidimensional Assessment of Interoceptive Awareness (MAIA). *PLoS ONE*, 7(11), e48230. https://doi.org/10.1371/journal.pone.0048230

Myers, J., et al. (2002). Exercise capacity and mortality among men referred for exercise testing. *New England Journal of Medicine*, 346(11), 793--801. https://doi.org/10.1056/NEJMoa011858

Nikolova, N., et al. (2025). Microstructural correlates of interoceptive sensitivity and metacognition. *Journal of Neuroscience*, 45. https://doi.org/10.1523/JNEUROSCI.0787-24.2025

Porges, S. W. (2007). The polyvagal perspective. *Biological Psychology*, 74(2), 116--143. https://doi.org/10.1016/j.biopsycho.2006.06.009

Ren, L., & Zhang, Z. (2019). A heartbeat-detection-based breath controller. *BioMedical Engineering OnLine*, 18, 68. https://doi.org/10.1186/s12938-019-0683-9

Sevoz-Couche, C., & Laborde, S. (2022). Heart rate variability and slow-paced breathing. *Neuroscience & Biobehavioral Reviews*, 135, 104576. https://doi.org/10.1016/j.neubiorev.2022.104576

Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and norms. *Frontiers in Public Health*, 5, 258. https://doi.org/10.3389/fpubh.2017.00258

Thayer, J. F., & Lane, R. D. (2000). A model of neurovisceral integration in emotion regulation and dysregulation. *Journal of Affective Disorders*, 61(3), 201--216. https://doi.org/10.1016/S0165-0327(00)00338-4

Vann-Adibe, A., et al. (2025). Remote HRV biofeedback: Meta-analysis. *Applied Psychophysiology and Biofeedback*. https://doi.org/10.1007/s10484-025-09750-w

Wespi, R., et al. (2025). Physiological synchrony in medical teams. *Frontiers in Psychology*, 16.

Wilson, E. O. (1998). *Consilience: The Unity of Knowledge.* Knopf.

You, M., et al. (2023). Effects of slow-paced breathing on cardiac vagal activity. *Applied Psychophysiology and Biofeedback*, 48, 407--418. https://doi.org/10.1007/s10484-023-09605-2

Zhan, Y., et al. (2024). Night shift effects on HRV in female nurses. *BMC Nursing*, 23, 563. https://doi.org/10.1186/s12912-024-02563-y

---

*S.T.E.P. 2.0 is an open standard proposed by Somnistics Research Labs, Inc. Comments, critiques, and contributions are invited. The standard belongs to the field it serves.*

*Prepared: March 22, 2026*
*Version: 2.0 (Draft for Review)*
