---
clinical_context: Comprehensive tagging framework for the 21-day VagalBeats nervous
  system curriculum — designed for dev team implementation
created: '2026-03-15'
creator: randy
dc:subject:
- VagalBeats
- metadata-architecture
- nervous-system-mapping
- intervention-taxonomy
- cueing-system
- diagnostics
id: urn:srl:observation:vagalbeats-metadata-architecture
modified: '2026-03-15'
observation_type: technical-spec
prov:wasDerivedFrom:
- urn:srl:observation:vagalbeats-8-layer-slider
skos:related:
- neurogating
- neuro-ouroboros
- polyanchora
- anterocept
- autonomic-regulation
- neuroharmonics
status: draft
title: 'VagalBeats Metadata Tagging Architecture: Nervous System Mapping, Interventions,
  Cueing, and Diagnostics'
type: observation
---

# VagalBeats Metadata Tagging Architecture

## Overview

A quantifiable, modular tagging framework for delivering and adapting the 21-day VagalBeats nervous system curriculum. This spec was developed for the dev team meeting and covers four integrated layers: nervous system mapping, interventions, cueing, and real-time diagnostics.

## Layer 1: Nervous System Mapping

Maps the specific neural pathways and structures targeted by each intervention:

| System/Structure | Function | Targeted by Interventions |
|---|---|---|
| Vagus Nerve (CN X) | Parasympathetic regulation, HRV | Breathwork, interoception, haptic feedback |
| Insular Cortex | Interoceptive awareness, emotional tone | Body scanning, sensory cues, self-generated focus |
| Limbic System | Emotional regulation, stress resilience | Affirmations, guided hypnosis, binaural beats |
| Diaphragm | Breathing regulation, vagal activation | Breath patterns, focus on diaphragm movement |
| Cerebral Hemispheres | Right-shift dominance for flow states | Bilateral stimulation, attention shifting |

## Layer 2: Intervention Taxonomy

Each intervention is tagged with:
- **Target system** (from Layer 1)
- **Modality** (breath, sound, haptic, visual, narrative)
- **Intensity level** (1–8, corresponding to the 8-layer slider)
- **Expected physiological shift** (HRV↑, RR↓, RSA amplitude↑, etc.)
- **Contraindications** (panic disorder, respiratory conditions, etc.)

## Layer 3: Cueing System

Multi-modal cueing architecture for real-time guidance:
- **Haptic cues** — Apple Watch taps synchronized to breath phase
- **Audio cues** — Binaural beat frequencies, voice guidance, ambient soundscapes
- **Visual cues** — Breath orb animation, color-coded state indicators
- **Narrative cues** — Interoceptive labeling prompts, self-remembering directives

Cross-modal tagging ensures every exercise carries a tri-tag: biometric target + symbolic cue + behavioral micro-act.

## Layer 4: Diagnostics Integration

Real-time adaptive layer:
- **Input signals**: HRV (RMSSD, HF power), respiratory rate, SpO₂, motion/stillness
- **State classification**: Maps to 5-state model (freeze → sympathetic dominant → mixed → parasympathetic dominant → flow)
- **Adaptation rules**: If HRV drops below threshold mid-session, system softens intensity; if coherence is high, system offers layer-up prompt
- **Session-over-session tracking**: Trends in baseline HRV, completion rates, self-reported state shifts

## Relationship to 8-Layer Slider

This metadata architecture is the *backend spec* that powers the [[vagalbeats-8-layer-slider]] frontend. The user sees a slider; the system references this tagging framework to determine what content, cueing, and diagnostics to deploy at each layer.

## Source

Google Drive: "Vagalbeats Metadata Architecture" (ChatGPT Migration files, created 2026-03-09)
