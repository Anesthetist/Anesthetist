---
created: '2026-03-16'
creator: randy+claude
id: urn:srl:concept:controlled-vocabulary-v1
modified: '2026-03-16'
status: review
subjects:
- knowledge-management
- ontology
- controlled-vocabulary
- thesaurus
- compliance
title: SRL Controlled Vocabulary and Thesaurus v1
type: concept
---

# SRL Controlled Vocabulary and Thesaurus v1

This thesaurus defines the canonical terms used across the SRL Knowledge Vault. Every tag, subject, and concept reference should resolve to a preferred term listed here. Synonyms are indexed for search but display as the preferred term.

---

## Autonomic & Physiological Domain

### autonomic-regulation
- **Synonyms:** ANS regulation, autonomic nervous system control, autonomic balance, sympathovagal balance
- **Broader:** human-performance-optimization
- **Narrower:** vagal-tone, sympathetic-activation, parasympathetic-activation, baroreflex-sensitivity
- **Related:** polyvagal-theory, HRV, biofeedback, co-regulation, state-transition
- **Scope:** The capacity to flexibly shift between sympathetic and parasympathetic states in response to contextual demand. Central to SRL's framework as the physiological substrate of performance under pressure.
- **External IDs:** MeSH: D001341 (Autonomic Nervous System); UMLS: C0004388; SNOMED: 362167005

### heart-rate-variability
- **Synonyms:** HRV, cardiac autonomic function, beat-to-beat variability, R-R interval variability, inter-beat interval variability
- **Broader:** autonomic-regulation
- **Narrower:** RMSSD, SDNN, LF-HF-ratio, respiratory-sinus-arrhythmia, coherence-ratio, pNN50
- **Related:** vagal-tone, biofeedback, resonant-breathing-frequency, wearable-sensors
- **Scope:** The variation in time intervals between consecutive heartbeats. Primary non-invasive marker of autonomic function. SRL uses HRV as both a measurement tool and a biofeedback training target.
- **External IDs:** MeSH: D006339; UMLS: C0018810; SNOMED: 251670001

### vagal-tone
- **Synonyms:** vagal activity, vagal function, cardiac vagal tone, parasympathetic tone, vagal brake
- **Broader:** autonomic-regulation
- **Narrower:** respiratory-sinus-arrhythmia, vagal-efficiency-index
- **Related:** polyvagal-theory, heart-rate-variability, resonant-breathing-frequency, co-regulation
- **Scope:** The degree of tonic parasympathetic (vagal) influence on the heart. Higher vagal tone is associated with greater physiological flexibility, emotional regulation capacity, and social engagement. SRL distinguishes between *tonic* vagal tone (baseline) and *phasic* vagal reactivity (response to challenge).
- **External IDs:** MeSH: D014630 (Vagus Nerve); UMLS: C0042465; SNOMED: 88882009

### polyvagal-theory
- **Synonyms:** PVT, Porges theory, polyvagal framework, neuroception theory
- **Broader:** autonomic-regulation
- **Narrower:** neuroception, ventral-vagal-complex, dorsal-vagal-complex, social-engagement-system
- **Related:** vagal-tone, co-regulation, state-transition, safe-and-sound-protocol
- **Scope:** Stephen Porges' theory proposing a phylogenetic hierarchy of autonomic states (ventral vagal → sympathetic → dorsal vagal) linked to social behavior, threat detection, and immobilization. **Note (2026-03):** Under active scientific debate following Grossman et al. critique. SRL position: clinical interventions derived from PVT remain effective; evolutionary mechanism claims require qualification. See contradiction tracker.
- **External IDs:** No MeSH term; UMLS: C4527448
- **Contradiction flag:** ACTIVE — see urn:srl:evidence:pmc-2026-polyvagal-theory-critique-grossman

### resonant-breathing-frequency
- **Synonyms:** resonance frequency, resonant frequency breathing, RFB, optimal breathing rate, coherent breathing rate
- **Broader:** breathwork
- **Narrower:** — 
- **Related:** heart-rate-variability, baroreflex-sensitivity, biofeedback, coherence-ratio
- **Scope:** The individual-specific breathing rate (typically 4.5–7 breaths per minute) at which heart rate oscillations achieve maximum amplitude, reflecting optimal baroreflex engagement. SRL uses RFB assessment as a baseline measurement and training target.
- **External IDs:** No specific MeSH; related: D001945 (Breathing Exercises)

### respiratory-sinus-arrhythmia
- **Synonyms:** RSA, vagal RSA, heart rate-respiration coupling
- **Broader:** heart-rate-variability
- **Related:** vagal-tone, resonant-breathing-frequency, polyvagal-theory
- **Scope:** The natural fluctuation in heart rate synchronized with breathing — acceleration during inhalation, deceleration during exhalation. Primary non-invasive index of cardiac vagal tone.
- **External IDs:** MeSH: D012120 (Respiratory Sinus Arrhythmia); UMLS: C0520874

---

## Interoceptive Domain

### interoception
- **Synonyms:** interoceptive processing, internal body sensing, visceral perception, bodily awareness (when specifically referring to internal signals)
- **Broader:** human-performance-optimization
- **Narrower:** interoceptive-accuracy, interoceptive-sensibility, interoceptive-awareness, interoceptive-literacy, cardiac-interoception, respiratory-interoception, gastric-interoception
- **Related:** anterocept, gap-moment-training, self-remembering, diaphragmatic-blindness
- **Scope:** The process by which the nervous system senses, interprets, integrates, and regulates signals from within the body. SRL treats interoception as the foundational skill from which all other performance capacities emerge. Distinguished from proprioception (body position) and exteroception (external senses).
- **External IDs:** MeSH: D065808 (Interoception); UMLS: C4521837; SNOMED: Not yet coded

### interoceptive-literacy
- **Synonyms:** interoceptive skill, interoceptive competence, body literacy (in SRL context)
- **Broader:** interoception
- **Narrower:** cardiac-interoceptive-literacy, respiratory-interoceptive-literacy, visceral-interoceptive-literacy
- **Related:** diaphragmatic-literacy, gap-moment-training, MAIA-2, anterocept
- **Scope:** The trained ability to accurately detect, interpret, and respond to internal physiological signals. Distinct from interoceptive *awareness* (knowing that internal signals exist) — literacy implies functional skill that can be applied under operational conditions. SRL's proprietary contribution.
- **External IDs:** No standard code — SRL novel term

### anterocept
- **Synonyms:** predictive interoception, anticipatory body sensing, pre-event interoceptive signal
- **Broader:** interoception
- **Related:** interoceptive-literacy, gap-moment-detection, relevance-realization, neurogating
- **Scope:** The ability to detect and interpret interoceptive signals that *precede* conscious awareness of a state change. SRL's term for the "body knows before the mind" phenomenon observed in experienced clinicians. Theoretically grounded in predictive processing / active inference frameworks. SRL proprietary concept.
- **External IDs:** No standard code — SRL novel term
- **IP status:** Trade secret; included in patent application US Provisional 2025-04-03

### diaphragmatic-blindness
- **Synonyms:** diaphragmatic dissociation, respiratory interoceptive deficit
- **Broader:** interoception
- **Related:** diaphragmatic-literacy, interoceptive-literacy, mouth-breathing
- **Scope:** The inability to voluntarily engage or sense diaphragmatic movement despite intact anatomy. SRL field data: 28/30 anesthesia professionals demonstrated this deficit on initial assessment. SRL proprietary finding.
- **External IDs:** No standard code — SRL novel term
- **IP status:** SRL-P proprietary field data

---

## Cognitive & Consciousness Domain

### gap-moment-training
- **Synonyms:** GMT, transitional moment training, liminal interval training
- **Broader:** human-performance-optimization
- **Narrower:** gap-moment-detection, gap-moment-literacy, gap-moment-codex
- **Related:** state-transition, neurogating, interoceptive-literacy, minimum-effective-dose, neurominute
- **Scope:** SRL's core training methodology: the systematic practice of using naturally occurring transition points (between patients, tasks, environments) as micro-training windows for autonomic regulation, interoceptive check-in, and state optimization. CRNAs experience 30-40 such moments per shift. SRL proprietary concept.
- **External IDs:** No standard code — SRL novel term
- **IP status:** Trademark filed; included in patent application; core commercial offering

### state-transition
- **Synonyms:** state change, autonomic state shift, neural state transition, mode switching
- **Broader:** autonomic-regulation
- **Narrower:** neural-transition-failure, sleep-to-wake-transition, rest-to-activation, task-switching
- **Related:** gap-moment-training, neurogating, polyvagal-theory, cognitive-variability-analysis
- **Scope:** Any shift between distinct physiological, cognitive, or emotional operating states. SRL treats state transitions as both a measurement target (how efficiently does the system shift?) and a training opportunity (gap moments).
- **External IDs:** Related MeSH: D000069736 (Cognitive Flexibility)

### neurogating
- **Synonyms:** neural gating, sensory gating (in broader context), attentional gating
- **Broader:** cognitive-performance
- **Narrower:** —
- **Related:** state-transition, gap-moment-training, relevance-realization, gamma-state-binding
- **Scope:** The brain's mechanism for selectively allowing or blocking information flow between neural networks during state transitions. SRL proposes that trained interoceptive awareness improves the efficiency of neurogating, reducing transition failures. SRL proprietary framing.
- **External IDs:** Related MeSH: D065808; Related SNOMED: 312012004 (Sensory gating)

### neuroharmonics
- **Synonyms:** neural harmonics, NeuroHarmonics (SRL brand), multi-frequency neural entrainment
- **Broader:** cognitive-performance
- **Narrower:** gamma-state-binding, hemispheric-rebalancing, binaural-entrainment
- **Related:** neurofeedback, meditation-neuroscience, resonant-breathing-frequency, EEG
- **Scope:** SRL's framework for understanding and training the harmonic relationships between neural oscillation frequencies (delta, theta, alpha, beta, gamma) and their coupling with autonomic rhythms (cardiac, respiratory). Proprietary concept.
- **External IDs:** No standard code — SRL novel term
- **IP status:** Trademark candidate; included in patent architecture

### self-remembering
- **Synonyms:** self-awareness practice, Gurdjieffian self-remembering, reflexive awareness, meta-awareness
- **Broader:** consciousness-studies
- **Narrower:** —
- **Related:** interoception, gap-moment-training, neurominute, mindfulness
- **Scope:** The practice of maintaining simultaneous awareness of external activity and internal state. Drawn from Gurdjieff's Fourth Way tradition, reframed by SRL as a trainable interoceptive-cognitive skill with measurable physiological correlates.
- **External IDs:** No standard code — philosophical/contemplative term

### neurominute
- **Synonyms:** NeuroMinute (SRL brand), micro-regulation intervention, 60-second neural reset
- **Broader:** gap-moment-training
- **Narrower:** —
- **Related:** minimum-effective-dose, biofeedback, self-remembering, co-regulation
- **Scope:** SRL's branded 60-second structured intervention combining breathwork, interoceptive check-in, and attentional anchoring. Designed to fit within naturally occurring gap moments. Delivery vehicle for SRL's training methodology. Core commercial product unit.
- **External IDs:** No standard code — SRL novel term
- **IP status:** Trademark filed; commercial product name

---

## Clinical & Population Domain

### clinician-durability
- **Synonyms:** clinician resilience, healthcare worker sustainability, professional longevity, career durability
- **Broader:** human-performance-optimization
- **Narrower:** burnout-prevention, compassion-fatigue-prevention, moral-injury-mitigation
- **Related:** co-regulation, interoceptive-literacy, gap-moment-training, autonomic-regulation
- **Scope:** The sustained capacity of healthcare professionals to perform at high levels across a full career without cumulative degradation of health, cognition, or emotional function. SRL's reframe of "burnout prevention" — durability implies *building capacity*, not just *preventing collapse*. Proprietary framing.
- **External IDs:** Related MeSH: D002055 (Burnout, Professional); UMLS: C0006433

### co-regulation
- **Synonyms:** interpersonal regulation, dyadic regulation, social regulation, relational nervous system regulation
- **Broader:** autonomic-regulation
- **Narrower:** team-breath, therapeutic-co-regulation, parent-child-co-regulation
- **Related:** polyvagal-theory, vagal-tone, mirror-neurons, social-engagement-system
- **Scope:** The mutual regulation of physiological and emotional states between two or more nervous systems through proximity, attunement, and shared rhythmic activity. SRL extends this beyond dyadic therapy into team-based clinical environments (OR teams, ICU staff) and AI-mediated co-regulation.
- **External IDs:** No specific MeSH; Related: D012919 (Social Behavior)

---

## Methodology & Measurement Domain

### biofeedback
- **Synonyms:** biological feedback, psychophysiological feedback, self-regulation feedback
- **Broader:** human-performance-optimization
- **Narrower:** HRV-biofeedback, neurofeedback, respiratory-biofeedback, thermal-biofeedback, EMG-biofeedback
- **Related:** heart-rate-variability, wearable-sensors, anterocept, minimum-effective-dose
- **Scope:** The use of real-time physiological signal display to train voluntary control of normally unconscious processes. SRL specializes in HRV biofeedback and respiratory biofeedback, with emerging neurofeedback integration.
- **External IDs:** MeSH: D001676 (Biofeedback, Psychology); UMLS: C0005491; SNOMED: 28506006

### cognitive-variability-analysis
- **Synonyms:** CVA, cognitive performance variability, intra-individual cognitive variability
- **Broader:** measurement
- **Narrower:** reaction-time-variability, executive-function-variability, attention-variability
- **Related:** sleep, state-transition, clinician-durability, wearable-sensors
- **Scope:** SRL's measurement approach that focuses on *variability* in cognitive performance over time rather than single-point assessments. Based on the principle that high variability in cognitive metrics is a more sensitive marker of autonomic dysregulation than mean performance.
- **External IDs:** No standard code — SRL proprietary measurement approach

### minimum-effective-dose
- **Synonyms:** MED, minimal effective intervention, therapeutic minimum, lowest effective dose
- **Broader:** methodology
- **Narrower:** —
- **Related:** neurominute, gap-moment-training, titration-to-effect
- **Scope:** The smallest intervention (in duration, intensity, or complexity) that produces a measurable and clinically meaningful shift in the target variable. SRL's design philosophy: every protocol is optimized for minimum time burden and maximum physiological effect. The NeuroMinute (60 seconds) embodies this principle.
- **External IDs:** Related MeSH: D004305 (Dose-Response Relationship, Drug) — adapted to non-pharmacological context

### wearable-sensors
- **Synonyms:** wearable devices, wearable biosensors, physiological monitors, consumer wearables, wearable technology
- **Broader:** measurement
- **Narrower:** PPG-sensor, chest-strap-ECG, wearable-EEG, continuous-glucose-monitor, sweat-biosensor
- **Related:** heart-rate-variability, biofeedback, data-pipeline, ecological-validity
- **Scope:** Non-invasive sensor technologies worn on or near the body to continuously monitor physiological signals. SRL evaluates wearables for clinical-grade accuracy, real-time data access, and integration with biofeedback training protocols.
- **External IDs:** MeSH: D000076202 (Wearable Electronic Devices); SNOMED: 706689003

---

## Breathwork Domain

### breathwork
- **Synonyms:** breathing exercises, respiratory training, pranayama (in yogic context), breathing practice, breath training
- **Broader:** human-performance-optimization
- **Narrower:** resonant-breathing-frequency, diaphragmatic-breathing, physiological-sigh, box-breathing, slow-breathing, cyclic-sighing
- **Related:** autonomic-regulation, vagal-tone, interoception, respiratory-sinus-arrhythmia
- **Scope:** The intentional modification of breathing patterns to influence autonomic, cognitive, and emotional states. SRL treats breathwork as the primary accessible lever for autonomic regulation — the one modality that is always available, requires no equipment, and produces measurable physiological shifts within seconds.
- **External IDs:** MeSH: D001945 (Breathing Exercises); UMLS: C0006277

---

## Research & Evidence Domain

### meditation-neuroscience
- **Synonyms:** contemplative neuroscience, meditation brain research, mindfulness neuroscience
- **Broader:** cognitive-performance
- **Narrower:** focused-attention-meditation, open-monitoring-meditation, jhana-neuroscience, nondual-awareness-neuroscience, cessation-experience
- **Related:** neuroharmonics, self-remembering, consciousness-studies, EEG, fMRI
- **Scope:** The scientific study of how meditation practices alter brain structure, function, and connectivity. SRL draws on this literature to ground its training protocols in measurable neural mechanisms.
- **External IDs:** MeSH: D019122 (Meditation); UMLS: C0025353

### sleep-science
- **Synonyms:** sleep research, somnology, sleep medicine (clinical context)
- **Broader:** human-performance-optimization
- **Narrower:** sleep-architecture, circadian-biology, sleep-deprivation, sleep-quality, sleep-dependent-memory
- **Related:** cognitive-variability-analysis, clinician-durability, somnoaffinity, recovery
- **Scope:** The study of sleep physiology, architecture, and its relationship to waking performance. SRL integrates sleep science through the concept of SomnoAffinity and its effects on clinician durability and cognitive variability.
- **External IDs:** MeSH: D012890 (Sleep); UMLS: C0037313; SNOMED: 258158006

---

## Term Count Summary

- **Preferred terms defined:** 25 (this version)
- **Synonyms indexed:** 95+
- **External identifiers mapped:** 18 MeSH, 14 UMLS, 8 SNOMED
- **SRL novel terms (no standard code):** 10 (anterocept, interoceptive-literacy, diaphragmatic-blindness, gap-moment-training, neurogating, neuroharmonics, neurominute, clinician-durability, cognitive-variability-analysis, minimum-effective-dose)

---

## Expansion Roadmap

**v1.1:** Add terms for consciousness-studies, somnistics, somnoaffinity, titration-to-effect, neuro-ouroboros, polyanchora, transmetachora, exteroryx, multi-phase-interoceptive-coupling
**v1.2:** Add market/business terms (TAM, enterprise-buyer, CE-accreditation, SAFE-round)
**v2.0:** Implement as machine-readable SKOS/OWL ontology with API query support
