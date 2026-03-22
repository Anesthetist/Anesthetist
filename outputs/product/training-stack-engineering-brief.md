---
title: "Pausality Training Stack — Engineering Brief"
created: 2026-03-22
creator: Vigil
type: output
output_type: ip-doc
status: draft
target_audience: engineering team
---

# Pausality Training Stack
## What We're Replacing, What We're Building, and Why

**For:** Engineering team
**From:** Randy Graybeal / Vigil
**Date:** March 22, 2026

---

## The Problem

Randy's daily autonomic training practice requires six separate apps running across three hardware devices. Each app handles one modality. None of them talk to each other. There is no shared data layer, no integrated session, and no progressive curriculum that spans all six modalities.

Pausality should be one app that does what six apps currently do — measured, progressive, and integrated.

---

## The Current Stack (What Randy Actually Uses Today)

### App 1: EHRV+ (Elite HRV)
**What it does:** Real-time HRV biofeedback during resonant frequency breathing
**Hardware:** Polar H10 chest strap (BLE, ECG-grade R-R intervals)
**Key capability we need:** Resonance frequency finder — identifies the user's personal optimal breathing rate (~4.5-7 bpm) by testing different rates and measuring which produces maximum HRV amplitude. Displays real-time HRV trace as a sine wave that the user watches smooth out during practice.
**Data:** RMSSD, SDNN, LF, HF, LF/HF ratio, coherence score, session duration. Exportable.
**What to absorb:** The resonance frequency assessment protocol. The real-time HRV wave visualization. The coherence score as a session quality metric.
**Integration note:** Polar H10 connects via BLE. EHRV uses the Polar SDK. We'd need the same or use Apple Watch R-R intervals (lower precision but acceptable for trends — Li et al. 2021: r=0.92-0.95 vs ECG for HR recovery).

### App 2: Echobay Heal (Binaural Beats)
**Developer:** App Influence, LLC
**What it does:** Generates binaural beat frequencies across all bands (delta through gamma). Runs in background while other apps run in foreground.
**Hardware:** AirPods Pro 3 (air conduction — required for binaural effect. Bone conduction destroys the interaural phase difference.)
**Key capability we need:** Background audio layer that plays under Pausality sessions. Adjustable frequency. Timer. Mixer with ambient sounds.
**Evidence caveat:** Binaural entrainment is weakly supported (5/14 EEG studies per Ingendoh 2023). The value is attentional anchoring and auditory-autonomic coupling, not brainwave entrainment. Do not use the word "entrainment" in any user-facing copy.
**What to absorb:** Background audio generation at selectable frequencies. The "runs under other apps" pattern becomes "audio layer within Pausality sessions." Consider isochronic tones as alternative — stronger EEG evidence (Dos Anjos 2024).
**Integration note:** Audio generation is straightforward. The question is whether to generate tones programmatically or use pre-rendered audio files. Programmatic gives frequency flexibility. Pre-rendered gives better audio design.

### App 3: ThinkUp (Self-Voiced Affirmations)
**Developer:** Precise Wellness LLC
**What it does:** User records affirmations in their own voice. Plays them back with background music. 21-day practice cycle.
**Hardware:** Any microphone + headphones
**Key capability we need:** User records a short audio clip (5-10 seconds) of a personal anchor phrase. This plays at a specific moment during the NeuroMinute session — e.g., at the transition between exhale and the return to task.
**Why own-voice matters:** Hearing your own voice activates self-referential processing (mPFC, PCC) and auditory self-recognition (superior temporal sulcus) differently than hearing another person's voice. It's identity-level anchoring, not just motivational content.
**What to absorb:** Recording UI (simple — record, play back, save). Playback trigger at a defined point in the session timeline. Storage is local only (privacy — AES-256, same as current biometric data).
**Integration note:** This is a small feature with outsized impact. Record once, plays every session. Not a full affirmation library — one anchor phrase per user.

### App 4: Pausality (Current Product)
**Developer:** Somnistics Research Labs
**What it does today:**
- 21 guided breathing sessions (Foundation → Awareness → Mastery)
- Clock-based metronome pacing (fixed rhythm)
- Self-counting by user
- HR measurement via Apple Watch and/or AirPods Pro 3
- SpO2 measurement via Apple Watch
- Post-session recaps (HR journey, recovery speed)
- Emotional state tracking
- Shareable results cards

**What it does NOT do yet:**
- Does not find the user's resonant frequency (planned — absorb from EHRV+)
- Does not use HR/HRV to adapt the session in real-time (planned — closed-loop)
- Does not sync breathing pace to heartbeat (planned — cardiac-anchored breathing)
- Does not generate audio tones (planned — absorb from Echobay)
- Does not record user voice (planned — absorb from ThinkUp)
- Does not offer deep recovery sessions (planned — absorb from Waking Up/NSDR)
- Does not offer self-hypnosis protocols (planned — absorb from Reveri)

### App 5: Reveri (Self-Hypnosis)
**Developer:** Reveri Health (David Spiegel, MD — Stanford)
**What it does:** AI-guided self-hypnosis. 1-minute and 10-minute sessions. Pre/post workout priming. Hypnotizability assessment.
**Hardware:** Headphones (any)
**Key capability we need:** 1-minute hypnotic protocols as an alternate NeuroMinute modality. Pre-case priming ("prepare for the next case") and post-case reset ("release the last case"). These are distinct from breathwork — they use suggestibility and focused attention via different neural pathway (dACC modulation, not vagal/baroreflex).
**Evidence:** Spiegel has 400+ published papers. 45 years of Stanford clinical research. The 1-minute effective dose independently validates our NeuroMinute format from a completely different modality.
**What to absorb:** Short-form hypnotic scripts (licensed or developed with clinical hypnotherapist). Pre-performance and post-performance session types. Suggestibility intake assessment (maps to our interoceptive sensitivity assessment).
**Integration note:** This requires clinical content development — we can't just generate hypnotic scripts. Either license from Spiegel/Reveri, partner, or develop with a qualified clinical hypnotherapist. The scripts need to be trauma-informed.

### App 6: Waking Up — Kelly Boys + Huberman NSDR
**Developer:** Waking Up (Sam Harris) / YouTube (Huberman)
**What it does:** Deep parasympathetic recovery. Kelly Boys' "Relax the Nervous System" guided session. Huberman's 10-minute NSDR protocol.
**Hardware:** Headphones (any)
**Key capability we need:** A "Deep Recovery" mode — 10-20 minute guided sessions that produce maximal parasympathetic activation. Not breathwork training. Not skill building. Pure recovery. The counterpart to progressive overload — without recovery, training produces damage, not adaptation.
**What to absorb:** Guided body scan / progressive relaxation protocols. Could be Days 7, 14, 21 in the curriculum (weekly recovery), or a standalone mode accessible anytime. Audio content needs to be original (can't use Kelly Boys' or Huberman's recordings).
**Integration note:** This is content development, not engineering. The technical implementation is just a longer audio session with HRV measurement to confirm parasympathetic saturation is achieved.

---

## The Integration Architecture

```
┌─────────────────────────────────────────────┐
│              PAUSALITY APP                   │
│                                              │
│  ┌─────────────┐  ┌──────────────────────┐  │
│  │ Session      │  │ Measurement Layer    │  │
│  │ Engine       │  │                      │  │
│  │              │  │ Apple Watch HR/HRV   │  │
│  │ Clock-paced  │  │ AirPods Pro 3 HR     │  │
│  │ (current)    │  │ Polar H10 ECG        │  │
│  │              │  │ (future BLE)         │  │
│  │ Cardiac-     │  │                      │  │
│  │ anchored     │  │ Post-session recap   │  │
│  │ (roadmap)    │  │ HRR calculation      │  │
│  └──────┬───────┘  └──────────────────────┘  │
│         │                                     │
│  ┌──────┴───────────────────────────────┐    │
│  │         Audio Layer                   │    │
│  │                                       │    │
│  │  Voice guidance (current)             │    │
│  │  + Frequency tones (from Echobay)     │    │
│  │  + Self-voiced anchor (from ThinkUp)  │    │
│  │  + Ambient/nature sounds              │    │
│  │  + Hypnotic scripts (from Reveri)     │    │
│  │                                       │    │
│  │  Mixed and delivered via AirPods      │    │
│  └───────────────────────────────────────┘    │
│                                              │
│  ┌───────────────────────────────────────┐   │
│  │         Session Types                  │   │
│  │                                        │   │
│  │  NeuroMinute (60s breathwork)          │   │
│  │  NeuroMinute (60s hypnotic prime)      │   │
│  │  Resonance Finder (5-10 min assess)    │   │
│  │  Deep Recovery (10-20 min NSDR)        │   │
│  │  Pre-Case Prep (60s, before first)     │   │
│  │  Post-Case Reset (60s, after crisis)   │   │
│  │  21-Day Curriculum (progressive)       │   │
│  └───────────────────────────────────────┘   │
│                                              │
│  ┌───────────────────────────────────────┐   │
│  │         Data Layer                     │   │
│  │                                        │   │
│  │  Session metadata (neurotagging)       │   │
│  │  HR/HRV time series                    │   │
│  │  HRR (heart rate recovery) per session │   │
│  │  Resonant frequency profile            │   │
│  │  Coherence score trend                 │   │
│  │  Self-report (emotional state)         │   │
│  │  All AES-256 encrypted, on-device      │   │
│  └───────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## Priority Order for Absorption

Based on engineering complexity and user impact:

| Priority | Feature | Absorbs From | Complexity | User Impact |
|----------|---------|-------------|------------|-------------|
| **P0** | Background audio tones (frequency selectable) | Echobay | Low | Medium — attentional anchoring during sessions |
| **P1** | Self-voiced anchor recording + playback | ThinkUp | Low | High — identity-level engagement, unique differentiator |
| **P1** | HRR calculation from session data | New | Low | High — ground truth outcome metric |
| **P2** | Resonance frequency assessment | EHRV+ | Medium | High — personalized breathing rate |
| **P2** | Deep recovery session type (10-20 min) | Waking Up/NSDR | Medium (content) | Medium — completes the training cycle |
| **P3** | Real-time HRV visualization during session | EHRV+ | Medium | High — the biofeedback loop that drives engagement |
| **P3** | Pre-case / post-case session types | Reveri concept | Low (UI) | High — clinical workflow integration |
| **P4** | Cardiac-anchored breathing (sync to heartbeat) | New / research | High | High — key differentiator, but needs R-R interval processing |
| **P4** | Polar H10 BLE integration | EHRV+ | Medium | Medium — clinical-grade HRV for power users |
| **P5** | Hypnotic script sessions | Reveri concept | High (content + clinical) | Medium — requires licensed content |
| **P5** | Adaptive audio (HRV-responsive) | NeuroHarmonics concept | High | Medium — closed-loop, needs real-time HRV processing |

---

## What NOT to Build

- **Brainwave entrainment claims** — the evidence doesn't support it. Build attentional anchoring, not entrainment.
- **Full affirmation library** — ThinkUp has 300+. We need ONE self-voiced anchor phrase per user. Simple.
- **Clinical EEG integration** — Muse/Mind Monitor is Randy's personal practice, not a product feature.
- **Full hypnotherapy platform** — Reveri has 45 years of Stanford research. We take the 1-minute format concept, not the clinical depth.
- **AI-adaptive sessions (yet)** — Reveri's AI personalization is impressive but premature for our stage. Ship the static content first, adapt later.

---

## The Validation Test

Before building any of this:

**10 CRNAs. 21 days. Current product (clock-based, no audio layer, no affirmation, no recovery mode).**

Measure HRR at Day 1, Day 7, Day 21. If HRR improves with the current product, every feature above makes it better. If HRR doesn't improve with current product, fix the breathing protocol before adding layers.

The foundation has to work before the layers compound.

---

## Hardware Compatibility Matrix

| Device | Current | Roadmap |
|--------|---------|---------|
| iPhone | Required | Required |
| Apple Watch Series 4+ | HR, HRV (post-session), SpO2 | Real-time HRV display, HRR calc |
| AirPods Pro 3 | HR measurement | Binaural audio delivery + HR |
| Polar H10 | Not supported | BLE ECG for clinical-grade R-R intervals |
| Muse EEG | Not supported | Not planned for product (Randy's personal use) |

---

## The One-Sentence Brief

**Pausality absorbs six apps into one integrated platform: resonant breathing (EHRV+), auditory anchoring (Echobay), self-voiced identity (ThinkUp), progressive curriculum (current Pausality), performance priming (Reveri), and deep recovery (Waking Up/NSDR) — measured by heart rate recovery as the ground truth biomarker.**

---

*Prepared by Vigil — March 22, 2026*
*Source: Randy's personal training practice, vault concept architecture, biomedical validation sweep*
