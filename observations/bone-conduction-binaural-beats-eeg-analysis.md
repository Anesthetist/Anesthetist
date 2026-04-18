---
clinical_context: Randy's personal EEG measurement practice with Muse + Mind Monitor
  + bone conduction headphones
created: '2026-03-22'
creator: randy
dc:subject:
- binaural-beats
- bone-conduction
- eeg
- muse
- mind-monitor
- entrainment
- experimental-design
id: urn:srl:observation:bone-conduction-binaural-beats-eeg-analysis
modified: '2026-03-22'
observation_type: craft-knowledge
skos:related:
- neuroharmonics
- alpha-theta-crossover
- eeg-data-pipeline
- neuro-respiratory-cardiac-coherence
- embodied-metacognition
status: draft
title: 'Bone Conduction + Binaural Beats + EEG: What Works and What Doesn''t'
type: observation
---

# Bone Conduction + Binaural Beats + EEG Analysis

**BioMistral synthesis (Qwen3-32B, 2026-03-22):** *All citations require independent PubMed verification.*

## Critical Finding: Binaural Beats May Not Work Via Bone Conduction

Traditional binaural beats require **interaural phase differences** — each ear gets a slightly different frequency, and the beat percept is generated in the superior olivary complex from the difference. Bone conduction vibrates the skull, reaching BOTH cochleae simultaneously. This **destroys the interaural phase difference** needed for the binaural beat percept.

**Huang & Charyton 2017:** Binaural beats via bone conduction do not produce the same perceptual beat as air conduction. The IPD is eliminated.

**Implication for SRL:** If Randy's practice uses Shokz bone conduction headphones for binaural beats, he may NOT be getting binaural beats at all. He may be getting **monaural beats** (amplitude modulation perceived by both ears simultaneously) or **just rhythmic vibration**.

### What He Might Actually Be Getting Instead
1. **Monaural beat** — amplitude-modulated tone perceived identically by both ears. Some evidence suggests monaural beats produce STRONGER EEG effects than binaural (Dos Anjos 2024).
2. **Cranial vibration** — bone conduction activates somatosensory pathways (trigeminal nerve, vestibular system). Krause et al. 2020: 10-20 Hz cranial vibration activates vestibular system.
3. **Attentional anchoring** — the rhythmic sound still provides a focus point regardless of beat mechanism.

### This Could Actually Be BETTER

If monaural beats + cranial vibration + attentional anchoring are what's actually happening, and Randy still gets the subjective effects he reports, then:
- The mechanism is different from what's claimed
- But the mechanism may be MORE robust (monaural beats have stronger evidence than binaural)
- The vestibular activation from bone conduction is an additional modality not available from earbuds

## Can Muse/Mind Monitor Detect the Effect?

### What to Look For in Mind Monitor Data
During binaural beats at 10 Hz alpha shifting to 6 Hz theta:

**Evidence of entrainment:**
- Stepwise increase in absolute alpha power (8-12 Hz) during first 5 minutes
- Shift to increased theta power (4-8 Hz) during second 5 minutes
- Theta/alpha ratio shifting toward theta dominance
- Increased coherence between frontal (FP1/FP2) and temporal (T7/T8) channels
- Gradual, sustained shifts (not spiky artifacts)

**Artifacts to rule out:**
- Electrical noise from headphones (broadband, spiky)
- Muscle artifacts from jaw/face (EMG contamination in temporal channels)
- Blinking artifacts in frontal channels

**Muse limitations:**
- 4-channel dry electrodes have lower signal-to-noise than clinical EEG
- Frontal/temporal placement misses parietal/occipital alpha (where alpha is strongest)
- Lopez et al. 2019: Muse CAN detect alpha entrainment but with lower sensitivity than wet electrodes

### Differentiating Real Entrainment from Artifact
- Real entrainment: gradual, sustained power changes in target band
- Artifact: transient, broadband noise correlated with headphone operation
- Key test: does the EEG change TRACK the frequency shift (10→6 Hz)? If power shifts from alpha to theta band when the beat frequency shifts, that's evidence. If it doesn't track, it's noise or placebo.

## Mind Lift Neurofeedback + Binaural Beats

**Use congruent frequencies.** If neurofeedback targets alpha (10 Hz), use 10 Hz binaural beats. If targeting theta, shift to 6 Hz. Conflicting frequencies (e.g., 10 Hz beats while training 6 Hz theta) confuse the feedback loop.

Zhang et al. 2021: congruent frequencies improved neurofeedback outcomes. Conflicting frequencies reduced performance.

## Randy's Self-Experiment Protocol

### Design: N=1 Within-Subjects Crossover

**Condition A:** Coherence breathing (5.5 bpm) + binaural beats (bone conduction, 10 Hz → 6 Hz) + Muse/Mind Monitor
**Condition B:** Coherence breathing (5.5 bpm) + silence + Muse/Mind Monitor

Same time of day. Same duration (10 min). Same breathing protocol. 3 sessions each condition, alternating days. 6 total sessions.

### What to Measure
1. **EEG:** Alpha power (8-12 Hz) and theta power (4-8 Hz) via Mind Monitor — compare A vs B
2. **HRV:** RMSSD via Polar H10 + EHRV — compare A vs B
3. **Subjective:** Rate 1-10 on depth, ease, heartbeat awareness, thought quieting after each session
4. **The tracking test:** Does EEG power shift from alpha to theta band when the beat frequency shifts at minute 5? If yes in A but not B, that's the signal.

### What Would Constitute Evidence
- **Alpha power in A > B during first 5 min** (even by 10-15%) = auditory effect on EEG
- **Theta power in A > B during minutes 5-10** = frequency tracking
- **RMSSD in A > B** = audio enhances autonomic regulation beyond breathing alone
- **No difference** = the audio layer adds attentional value but not measurable neural change. Still useful, just not through the mechanism claimed.

### The Bone Conduction Question
Run an additional Condition C: same binaural beat protocol through AirPods (air conduction). Compare A (bone) vs C (air) to test whether bone conduction preserves the binaural mechanism.

## Design Constraint

**"Before claiming any EEG entrainment effect from NeuroHarmonics, run Randy's self-experiment. N=1 data is worth more than 100 literature citations for a product decision."**

## Clinical Interpretation

Pending review
