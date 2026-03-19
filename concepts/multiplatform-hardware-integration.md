---
created: '2026-03-19'
creator: urn:srl:agent:claude
dc:subject:
- technology
- BLE
- Apple-Neural-Engine
- wearables
- multiplatform
- HRV-biofeedback
- product-roadmap
- Open-Wearables
- Momentum
- FHIR
- EHR-integration
- Garmin
- WHOOP
- partnership
id: urn:srl:concept:multiplatform-hardware-integration
modified: '2026-03-19'
skos:broader: []
skos:narrower: []
skos:related: []
status: draft
title: Multiplatform Hardware Integration (BLE/ANE)
type: concept
---

# Multiplatform Hardware Integration (BLE/ANE)

## Core Concept

Pausality currently receives real-time HRV biofeedback exclusively through Apple HealthKit, limiting the platform to Apple Watch users. **BLE (Bluetooth Low Energy) integration** would enable Pausality to stream biometric data directly from any BLE-compatible wearable — Garmin, Whoop, Polar, Oura, chest straps — bypassing platform-specific APIs. **ANE (Apple Neural Engine) integration** would enable on-device machine learning for real-time personalization of breathing protocols based on HRV patterns, without cloud dependency.

**Active partnership exploration:** Open Wearables (by Momentum) — a unified open-source API for wearable device data — is now in active discussion with SRL as the potential infrastructure layer for multiplatform support. Meeting held March 2026 with Jan, Bartosz (Open Wearables), Jason Fields, and Randy.

## Open Wearables / Momentum Partnership — March 2026

### What Is Open Wearables
An open-source unified API for wearable device data and AI-powered insights, developed by Momentum. Connects major wearable providers through a single integration layer. Options for self-hosting or Momentum's SLA-supported cloud. The project recently had a viral moment — significant growth in GitHub stars and contributions.

### What Was Discussed
- **Real-time data sync:** Currently on Open Wearables' Q2 roadmap. This is the critical feature for Pausality — live HRV streaming during breathing sessions from non-Apple devices. Bartosz advised against SRL implementing real-time Garmin sync independently due to the complexity and opacity of Garmin's API.
- **Device partnerships:** Open Wearables is establishing official partnerships with Garmin, WHOOP, and other major providers. These partnerships provide faster API access, authorization processes, and developer accounts — benefits that flow to companies using the platform.
- **FHIR mapping:** Open Wearables is working on mapping wearable data to FHIR (Fast Healthcare Interoperability Resources) format for EHR integration. This is significant for SRL's enterprise health system play — FHIR compliance is a procurement requirement for many hospitals.
- **Beyond wearables:** Roadmap includes glucose monitoring devices, blood tests, and potentially brain activity data. The vision expands Pausality's potential sensor inputs well beyond heart rate.
- **Enterprise data lake:** Discussion of enterprise-scale biometric data aggregation for mental wellness assessments across large organizations. This maps directly to SRL's enterprise health system expansion ($310-620M market).

### Jason's App Progress (reported in meeting)
- Integrated HIPAA and PHI compliance skills — remediated 80% of data exposure issues
- New share card feature displaying heart rate data with direct sharing from app
- Next steps: supporting additional devices (Apple Watch enhancements, AirPods), enterprise integration
- Working on robust notification system and SOC2 compliance path

### Key Technical Decision
**Wait for Open Wearables' built-in real-time sync vs. build independently.** Bartosz recommended waiting — implementing Garmin real-time sync independently would require significant re-architecture and navigating opaque APIs. Open Wearables' official partnerships with device manufacturers provide cleaner access. Q2 timeline for real-time support aligns with SRL's development roadmap.

### Next Steps from Meeting
1. **Jan:** Send updated roadmap and feature update with expected deliverable dates to Jason and team
2. **Jan/Bartosz:** Provide detailed timeline for real-time data sync support (especially Garmin), including options for prioritization and collaboration
3. **Jan:** Send documentation and GitHub account info to Michael for review
4. **Jan:** Email Randy San Francisco trip dates for meeting coordination
5. **Jason:** Connect Jan/Bartosz with Kelly Smith (Head First) for potential EHR integration collaboration
6. **SF Hackathon:** Team plans to meet in San Francisco next month — wearable hackathon, further collaboration on enterprise dashboard development and clinical data analysis

### Strategic Implications
- **Build vs. partner:** Open Wearables solves the multiplatform integration problem without SRL building and maintaining device-specific integrations. This preserves engineering resources for core product (biofeedback engine, curriculum, clinical LLM).
- **FHIR/EHR:** Wearable-to-FHIR mapping creates the bridge between Pausality's biometric data and hospital EHR systems. This is a major enterprise selling point — "Pausality data flows into your existing clinical infrastructure."
- **Competitive moat:** If SRL integrates early with Open Wearables, they benefit from every new device partnership Momentum establishes. The multiplatform moat grows automatically as the open-source project grows.
- **Data lake vision:** Enterprise-scale biometric data aggregation enables population-level analysis of stress response training effectiveness. This is the data moat at scale — proprietary dataset across devices, institutions, and clinical populations.

## Why It Matters

### BLE: From Apple-Only to Hardware-Agnostic
- **Current state:** Apple Watch via HealthKit is the sole biometric data source. This constrains the addressable market to Apple Watch owners.
- **BLE opportunity:** The BLE Heart Rate Profile (HRP) is a standardized GATT service. Any wearable that broadcasts heart rate over BLE can be read by an iOS or Android app without proprietary SDK integration.
- **Open Wearables pathway:** Rather than implementing raw BLE directly, Open Wearables provides a unified API layer that handles device-specific quirks, authentication, and data normalization. SRL integrates once; Open Wearables handles the device zoo.
- **Enterprise implication:** Health systems will not mandate Apple Watches for their clinical staff. Multiplatform support lets Pausality work with whatever wearable a hospital already deploys — critical for the $300M+ perioperative expansion and $310-620M enterprise health system markets.
- **Android pathway:** Open Wearables is platform-agnostic. The same integration works on Android, opening non-Apple ecosystems.

### ANE: On-Device Clinical AI
- **Current state:** Breathing protocols are delivered via a fixed 21-session progressive curriculum.
- **ANE opportunity:** The Apple Neural Engine (available on iPhone 8+ and all Apple Watches Series 4+) can run Core ML models locally. This enables real-time personalization — adjusting breathing cadence, session duration, and technique selection based on the user's live HRV response patterns.
- **Privacy advantage:** On-device inference means no biometric data leaves the device. For clinical environments (HIPAA) and enterprise deployments, this is a significant compliance and trust advantage.
- **Clinical LLM roadmap:** ANE is the hardware foundation for the clinical LLM personalization layer. Models trained on aggregate (de-identified) HRV response data could be deployed to individual devices.

## Technical Architecture

### Via Open Wearables (Recommended Path)
1. **Integration:** SRL integrates with Open Wearables unified API (single integration point)
2. **Device support:** Garmin, WHOOP, Polar, Oura, Apple Watch, and expanding — handled by Open Wearables' device partnerships
3. **Real-time streaming:** Q2 2026 target for real-time data sync support (pending Jan/Bartosz timeline confirmation)
4. **FHIR mapping:** Wearable data automatically mapped to FHIR format for EHR integration
5. **Hosting:** Self-hosted option for enterprise deployments with strict data residency requirements, or Momentum cloud with SLA
6. **Future sensors:** Glucose monitors, blood tests, brain activity data as Open Wearables roadmap expands

### Direct BLE (Fallback/Supplement)
1. **Discovery:** App scans for nearby BLE devices advertising Heart Rate Service (UUID 0x180D)
2. **Connection:** User pairs wearable once. App subscribes to Heart Rate Measurement characteristic (UUID 0x2A37)
3. **Streaming:** Wearable pushes heart rate data at 1-4 Hz. App processes RR intervals for real-time HRV metrics (RMSSD, SDNN)
4. **Use case:** Clinical-grade chest straps and devices not yet supported by Open Wearables

### ANE On-Device ML (Phase 3)
1. **Model training:** Aggregate de-identified HRV data trains Core ML model (cloud-side)
2. **Model deployment:** Pushed to devices via app update. Runs entirely on Neural Engine
3. **Real-time inference:** During session, model ingests live HRV and outputs protocol adjustments
4. **Feedback loop:** Session outcomes feed back into model refinement

## Strategic Implications

### Moat Building
- **Data moat (emerging):** Multiplatform integration via Open Wearables dramatically increases volume and diversity of HRV data. More data from more devices = harder to replicate.
- **Switching costs:** Once clinicians train with Pausality across their preferred wearable, switching means losing personalized protocol history and CE accreditation pathway.
- **Counter-positioning:** Calm and Headspace have no biometric integration. Multiplatform BLE/Open Wearables widens the competitive gap.
- **Network effect via Open Wearables:** As the open-source project grows, SRL benefits from every new device partnership automatically.

### Market Expansion
- **$32M wedge (CRNAs):** Many CRNAs already own non-Apple wearables. Multiplatform removes the hardware barrier.
- **$300M expansion (perioperative):** Hospitals standardize on different wearable platforms. Hardware-agnostic = procurement-friendly.
- **$310-620M expansion (enterprise health systems):** FHIR mapping + multiplatform = "Pausality integrates with your existing infrastructure."
- **Enterprise data lake:** Population-level biometric data enables outcomes research, ROI proof, and the clinical evidence base that drives health system adoption.

### Investor Narrative
- **One-liner:** "We start with Apple Watch via HealthKit. Open Wearables gives us every major wearable through a single integration. ANE lets us run clinical AI on-device for real-time personalization."
- **Defensibility:** Open Wearables + ANE creates a flywheel — more hardware support drives more users, more users generate more HRV data, more data improves the on-device AI, better AI increases retention and outcomes, which drives more enterprise contracts.

## Implementation Priority

1. **Phase 1 (now):** Continue Apple Watch/HealthKit. Jason advancing HIPAA compliance, share card, notification system.
2. **Phase 2 (Q2 2026):** Integrate Open Wearables unified API when real-time sync ships. Garmin and WHOOP support first. FHIR mapping for enterprise.
3. **Phase 2.5 (supplemental):** Direct BLE Heart Rate Profile for clinical chest straps and devices not yet in Open Wearables.
4. **Phase 3 (roadmap):** Core ML model for on-device HRV-based protocol personalization via ANE. Requires sufficient training data from Phase 1-2 user base.

## Key Contacts
- **Jan (Open Wearables/Momentum):** Roadmap, partnerships, business development
- **Bartosz (Open Wearables/Momentum):** Technical architecture, real-time sync, FHIR mapping
- **Kelly Smith (Head First):** EHR integration collaboration (Jason to connect)
- **Michael:** Technical review of Open Wearables documentation and GitHub
