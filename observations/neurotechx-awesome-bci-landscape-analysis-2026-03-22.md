---
created: '2026-03-22'
creator: Randy Graybeal
dc:source:
- https://github.com/NeuroTechX/awesome-bci
dc:subject:
- BCI
- eeg
- neurotechnology
- hardware
- software
- competitive-landscape
- neurofeedback
- brain-stimulation
id: urn:srl:observation:neurotechx-awesome-bci-landscape-analysis-2026-03-22
modified: '2026-03-22'
status: draft
title: NeuroTechX Awesome BCI — Full Landscape Analysis for SRL
type: observation
---

# NeuroTechX Awesome BCI — Full Landscape Analysis for SRL

## Source

[NeuroTechX/awesome-bci](https://github.com/NeuroTechX/awesome-bci) — community-maintained curated list of BCI resources, hardware, software, databases, and learning materials. Maintained by the NeuroTechX community.

## Why This Matters to SRL

SRL uses consumer EEG (Muse 2/Emotiv) in assessment protocols, plans real-time cognitive load detection ([[neurogating]]), and tracks alpha/theta ratios as part of the SRB-60. This repository maps the entire BCI ecosystem — hardware options, software for signal processing, neurofeedback frameworks, brain stimulation modalities, and research databases. It's the landscape SRL operates within.

---

## Tier 1: Directly Relevant to Current SRL Operations

### Consumer EEG Hardware for Assessment Stations

| Device | Channels | Key Feature | Price Range | SRL Fit |
|--------|----------|-------------|-------------|---------|
| **Muse 2** | 4 (AF7, AF8, TP9, TP10) | Meditation/focus app ecosystem, PPG, accelerometer | ~$250 | Current choice for intake EEG baseline |
| **Emotiv Insight** | 5 | Better spatial coverage, motion sensors | ~$300 | Upgrade option — more channels for frontal asymmetry |
| **Emotiv EPOC X** | 14 | Research-grade density in consumer form | ~$850 | Best consumer option for detailed alpha/theta mapping |
| **Neurosity Crown** | 8 | Edge computing, real-time ML on device | ~$1,000 | Premium option — on-device processing for Neurogating prototype |
| **BrainBit Headband** | 4 | Affordable, SDK available | ~$200 | Budget alternative to Muse |
| **OpenBCI Cyton** | 8-16 | Fully open-source, customizable | ~$500-1,000 | Research/DIY option, maximum flexibility |

**Recommendation:** Muse 2 is adequate for current intake assessments (alpha/theta ratio, frontal asymmetry at 2 sites). If SRL moves toward real-time cognitive load detection (Neurogating MVP), Neurosity Crown or Emotiv EPOC X provide the channel density needed.

### EEG Signal Processing Software

| Tool | Language | Key Capability | SRL Use Case |
|------|----------|----------------|--------------|
| **MNE-Python** | Python | Gold standard EEG analysis, spectral analysis, source localization | Processing assessment EEG data into alpha/theta ratios, frontal asymmetry scores |
| **BrainFlow** | Python/C++ | Unified API across all consumer devices (Muse, OpenBCI, Emotiv, BrainBit) | Hardware-agnostic data collection — switch devices without rewriting code |
| **pyRiemann** | Python | Riemannian geometry for BCI classification | Cognitive state classification for Neurogating |
| **Braindecode** | Python | Deep learning for EEG decoding | Advanced state classification R&D |
| **Timeflux** | Python | Real-time signal processing pipeline | Real-time processing for live sessions |

**Recommendation:** BrainFlow for data collection (hardware-agnostic), MNE-Python for offline analysis (assessment reports), Timeflux for real-time processing if SRL builds live neurofeedback features.

### Neurofeedback Frameworks

| Tool | Description | SRL Relevance |
|------|-------------|---------------|
| **BrainBay** | Open-source bio/neurofeedback, works with OpenBCI/OpenEEG | Could power a basic neurofeedback loop during coached sessions |
| **OpenNFB** | Python-based neurofeedback | Lightweight, scriptable — could integrate with Pausality data pipeline |
| **NeuroPype** | Commercial real-time BCI platform | Full-featured but paid — supports EEG + fNIRS multimodal |
| **EEGsynth** | Python-based, converts EEG to control signals | Creative applications — could map brain state to breathing guidance |

---

## Tier 2: Strategic Opportunities (Near-Term)

### Brain Stimulation Modalities — Future Protocol Layers

| Modality | Device/Company | Mechanism | SRL Integration Potential |
|----------|---------------|-----------|--------------------------|
| **Transcranial Photobiomodulation (tPBM)** | Vielight | Near-infrared light through skull, upregulates mitochondrial function | Could layer into pre-sleep or recovery protocols. Non-invasive, consumer-accessible. Research shows effects on cerebral blood flow and oxygenation. |
| **tDCS (transcranial direct current stimulation)** | Soterix Medical, Neuroelectrics | Weak electrical current modulates cortical excitability | Research tool for understanding state transitions. Not consumer-ready for SRL, but relevant for clinical study design. |
| **tACS (transcranial alternating current stimulation)** | Soterix Medical | Entrains neural oscillations at specific frequencies | Could theoretically entrain alpha rhythms to support resonant breathing. Research-phase. |
| **Elemind** | Consumer neurostim | Closed-loop brain stimulation for sleep | Direct competitor in the sleep/recovery space. Watch closely. |

### Research Databases for Evidence Notes

| Database | Content | SRL Use |
|----------|---------|---------|
| **National Sleep Research Resource** (sleepdata.org) | Massive sleep datasets, supported by Sleep Research Society | Pre-sleep protocol evidence, sleep architecture research |
| **PhysioNet** | Open physiological signal databases including HRV | HRV normative data, validation datasets for RMSSD claims |
| **OpenNeuro** | Open neuroimaging datasets | EEG baseline comparisons, alpha/theta normative ranges |
| **MindBigData** | EEG during cognitive tasks | Cognitive load state classification training data |
| **Temple University EEG Corpora** | Various clinical EEG datasets | Clinical EEG pattern libraries |

### Communication Protocols

| Protocol | Description | SRL Relevance |
|----------|-------------|---------------|
| **Lab Streaming Layer (LSL)** | De facto standard for real-time biosignal streaming | If SRL ever streams EEG + HRV + breathing simultaneously, LSL is the protocol |
| **BrainFlow** | Unified biosignal acquisition | Already listed above — handles protocol layer |

---

## Tier 3: Competitive Landscape Flags

### Direct Overlaps with SRL Vision

| Company/Product | What They Do | SRL Overlap | Threat Level |
|----------------|-------------|-------------|--------------|
| **Kernel Flow** | TD-fNIRS for "wellness tracking, cognitive function assessment, mental health monitoring" | Long-term SRL vision: real-time cognitive state monitoring | Medium — different modality (fNIRS vs EEG + HRV), much higher price point |
| **Neurable MW75 Neuro** | BCI in headphones, "real-time insights into focus and cognitive load" | Neurogating concept — passive cognitive load detection in consumer form | High — consumer packaging of cognitive load detection. Watch their SDK and data quality claims. |
| **Dreem by Beacon Biosignals** | Sleep-focused EEG headband | Pre-sleep recovery protocols, sleep architecture monitoring | Medium — sleep-specific, doesn't address waking regulation |
| **Elemind** | Closed-loop brain stimulation for sleep | Sleep optimization competitive entry | Medium — stimulation approach vs. SRL's breathing/regulation approach |
| **IDUN Guardian** | In-ear EEG for continuous monitoring | Passive brain state monitoring, could enable always-on state detection | Low-medium — early stage, but the form factor (in-ear) is compelling for continuous wear |

### Differentiation

None of these companies combine:
1. Real-time cardiac data (Apple Watch HRV) +
2. Breathing guidance (Pausality) +
3. EEG state assessment +
4. Clinical expertise (CRNA) +
5. Structured micro-interventions (NeuroMinute 60-second format)

SRL's moat is the integration layer — not any single measurement modality, but the closed loop from detection → classification → intervention → measured outcome within 60 seconds. The BCI landscape is fragmented into measurement companies and intervention companies. SRL is both.

---

## Conferences & Events to Track

| Event | Date | Location | Why |
|-------|------|----------|-----|
| **10th Graz BCI Conference** | Sept 14-18, 2026 | Graz, Austria | Premier BCI research conference. Real-time BCI, neurofeedback, cognitive state classification. |
| **SfN 2026** | Nov 14-18, 2026 | Washington, DC | Society for Neuroscience. Largest neuroscience conference. Interoception, autonomic regulation sessions. |
| **BCI Meeting 2027** | June 7-10, 2027 | Croatia | BCI Society's main event. 2 years out but worth planning for a poster/demo. |
| **CNS 2026** | March 7-10, 2026 | Vancouver | Cognitive Neuroscience Society. Already passed but future years relevant. |
| **Brainhack 2026** | Various | Multiple cities | Community-driven, hands-on. Good for recruiting technical collaborators. |

---

## Key Takeaways for SRL

1. **BrainFlow is the bridge.** Single Python library that talks to Muse, Emotiv, OpenBCI, BrainBit. If SRL ever needs to support multiple EEG devices, start here.

2. **MNE-Python for assessment reports.** The EEG data from Massimo's intake (and future clients) should be processed through MNE-Python for standardized spectral analysis. Publishable, reproducible, open-source.

3. **Neurable is the company to watch.** BCI in headphones with cognitive load detection is the closest consumer product to what Neurogating describes. Their approach (passive EEG in everyday form factor) is the direction the market is moving.

4. **PhysioNet + Sleep Research Resource** should be mined for normative HRV and sleep data to validate SRL's claims against published baselines.

5. **The SRL closed loop (detect → classify → intervene → measure) doesn't exist anywhere in this list.** Every tool is either measurement OR intervention. Nobody closes the loop in 60 seconds with a consumer device.

## Clinical Interpretation

Pending review.

## Related Concepts

- [[neurogating]] — Real-time cognitive load detection and adaptive intervention triggering
- [[cognitive-variability-analysis]] — AI-driven cognitive state tracking using multimodal biomarkers
- [[attention-as-gain-control]] — Neurophysiological basis for BCI-detected attentional states
- [[somnistics-readiness-battery]] — SRB-60 Domain 4 (Measured State Delta) requires real-time biometric capture
- [[cardiac-anchored-breathing]] — SRL's differentiator vs. clock-paced BCI interventions
