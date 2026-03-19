---
clinical_context: Personal biofeedback practice and research platform
created: '2026-03-18'
creator: Randy Graybeal
dc:subject:
- eeg
- personal-practice
- biofeedback
- data-pipeline
- muse
- mind-monitor
id: urn:srl:observation:eeg-data-pipeline
modified: '2026-03-18'
observation_type: craft-knowledge
prov:wasDerivedFrom:
- urn:srl:chat:chatgpt-eeg-data-streaming-setup
- urn:srl:chat:chatgpt-mac-eeg-visualization-tools
- urn:srl:chat:chatgpt-brainwave-visualization-apps
skos:related:
- neuroharmonics
- alpha-theta-crossover
- neuro-respiratory-cardiac-coherence
status: draft
title: 'Randy''s EEG Data Pipeline: Muse 2 + Mind Monitor + OSC Streaming'
type: observation
years_of_evidence: 3
---

# Randy's EEG Data Pipeline: Muse 2 + Mind Monitor + OSC Streaming

Randy's personal EEG toolchain — the empirical platform behind [[neuroharmonics]] development and the measurement infrastructure that validates brainwave claims.

## The Toolchain

- **Muse 2** — consumer-grade 4-channel EEG headset (TP9, AF7, AF8, TP10)
- **Mind Monitor** — iOS/iPad app for real-time EEG visualization and OSC data streaming
- **OSC streaming** — UDP port 5000, Node.js server receiving real-time brainwave data
- **Extra lead setup** — Randy has explored configurations beyond stock Muse placement, indicating hardware experimentation

## Visualization Tools Evaluated

Myndlift, Muse Direct, BrainWave, EEGLAB, OpenBCI GUI, NeuroPype, Brainstorm, Visbrain

## Randy's Intent

Use live EEG output as a visual background for online meetings — making internal states visible in professional contexts. This is an early expression of his commitment to making the invisible (autonomic state) visible.

## Attribution

Randy's words: "I am a researcher with 20 years of clinical anesthesia experience"; "I pair a Muse2 headset with the Mindmonitor app on the iPad to get a rudimentary real-time eeg visualization"; "Compatible with mind monitor extra lead setup."

## Related Concepts

- [[neuroharmonics]] — the frequency architecture this pipeline informs
- [[alpha-theta-crossover]] — a biomarker measurable through this pipeline
- [[neuro-respiratory-cardiac-coherence]] — the combined protocol this pipeline validates
