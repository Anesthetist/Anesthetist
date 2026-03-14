---
id: "urn:srl:source:gdrive-pausality-prd"
type: source
title: "PAUSALITY PRD"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:PAUSALITY-PRD.md"
---

# Pausality Product Requirements Document (PRD)
## Single Source of Truth for Marketing & Content

**Version:** 1.1.0
**Last Updated:** January 2026
**Status:** Production
**Document Purpose:** Source of truth for AEO/SEO marketing content

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Product Vision](#product-vision)
3. [Problem Statement](#problem-statement)
4. [Target Users](#target-users)
5. [Core Features](#core-features)
6. [Key Differentiators](#key-differentiators)
7. [Technical Specifications](#technical-specifications)
8. [Pricing & Subscription](#pricing--subscription)
9. [User Benefits](#user-benefits)
10. [Competitive Positioning](#competitive-positioning)
11. [Marketing Messages](#marketing-messages)
12. [FAQ Reference](#faq-reference)

---

## Executive Summary

**Pausality** is a science-backed iOS and watchOS breathing app that provides real-time biometric feedback during guided breathing sessions. Unlike traditional meditation apps that rely on subjective feelings, Pausality shows users measurable physiological changes through heart rate monitoring and blood oxygen measurements.

### The One-Liner
> Pausality is the breathing app that proves it's working—with real-time heart rate biofeedback during 21 science-backed breathing techniques.

### Key Stats
- **21** progressive breathing sessions
- **3** skill categories (Foundation → Awareness → Mastery)
- **60-second** session time (fits any schedule)
- **2** biometric device options (Apple Watch for full biometrics, AirPods Pro 3 for heart rate)
- **Real-time** heart rate and blood oxygen tracking

---

## Product Vision

### Mission Statement
To democratize evidence-based breathwork by making physiological improvements visible and measurable for everyone.

### Vision
Pausality transforms breathing exercises from an abstract practice into a data-driven skill development journey, proving effectiveness through biometric feedback rather than promises.

### Company
**Somnistics Research Labs, Inc.** — Pioneering the intersection of respiratory science and consumer technology.

---

## Problem Statement

### The Problem
Traditional meditation and breathing apps ask users to "feel calmer" without proof. Users invest time in practices but can't measure if they're working. This leads to:

- **Skepticism** about whether breathing exercises actually help
- **Abandonment** when users don't "feel" immediate results
- **Inconsistent practice** without visible progress markers
- **No skill progression** — users repeat the same basic exercises indefinitely

### The Solution
Pausality solves this by:

1. **Showing real-time biometric changes** during every session
2. **Providing measurable metrics** (heart rate drop, blood oxygen, recovery speed)
3. **Structuring progressive skill development** across 21 sessions
4. **Linking every technique to scientific research** for credibility

---

## Target Users

### Primary Personas

#### 1. The Busy Professional (25-45)
- Works high-stress job in tech, finance, healthcare
- Has 1-5 minutes between meetings
- Owns Apple Watch or AirPods Pro 3
- Wants quick stress relief they can measure
- Values efficiency and data-driven approaches

#### 2. The Wellness Optimizer (30-50)
- Already tracks fitness, sleep, nutrition
- Interested in nervous system health
- Uses Apple Health ecosystem
- Wants to add breathwork to their stack
- Appreciates science-backed methods

#### 3. The Stressed Parent (30-45)
- Limited personal time
- High daily stress levels
- Needs quick reset techniques
- Skeptical of meditation apps ("don't have time")
- Motivated by seeing tangible results

#### 4. The Performance Seeker (20-40)
- Athlete, entrepreneur, or executive
- Interested in stress resilience and recovery
- Wants to optimize physiological response
- Seeks competitive edge through breathwork

### User Requirements
- iPhone with iOS 16+
- Apple Watch Series 4+ OR AirPods Pro 3
- Apple Health app access

---

## Core Features

### 1. Session Library (21 Progressive Sessions)

#### Foundation Category (Beginner)
Entry-level techniques for building foundational breathing skills:
- Diaphragmatic breathing fundamentals
- Basic breath awareness
- Introductory coherent breathing patterns
- Establishing breathing rate baselines

#### Awareness Category (Intermediate)
Advanced techniques for physiological understanding:
- Extended exhale patterns
- CO2 tolerance building
- Stress response recognition
- Nervous system regulation

#### Mastery Category (Expert)
Complex patterns for peak performance:
- Advanced coherent breathing
- Acute stress recovery protocols
- Performance breathing under pressure
- Long-form extended sessions

### 2. Real-Time Biometric Monitoring

#### Supported Devices & Capabilities
| Device | Heart Rate | Blood Oxygen | Full Biometrics |
|--------|------------|--------------|-----------------|
| **Apple Watch Series 4+** | ✓ | ✓ | ✓ (Primary experience) |
| **AirPods Pro 3** | ✓ | ✗ | Heart rate only |
| **Audio-only (no device)** | ✗ | ✗ | No biometrics recorded |

The first-party experience requires Apple Watch or AirPods Pro 3 for biometric feedback.

#### Metrics Tracked During Sessions (Apple Watch)
| Metric | Description | Update Frequency |
|--------|-------------|------------------|
| Heart Rate (BPM) | Live current heart rate | Every second |
| Blood Oxygen (SpO2) | Peripheral oxygen saturation | Real-time |
| Session Phase | Current phase with time remaining | Continuous |

#### Post-Session Metrics
| Metric | Description | Significance |
|--------|-------------|--------------|
| Baseline HR | Pre-session heart rate | Starting point |
| Peak HR | Maximum during session | Stress activation |
| Final HR | End of session heart rate | Recovery result |
| HR Recovery | Peak minus Final HR | Nervous system response speed |
| SpO2 Change | Initial vs Final oxygen | Breathing efficiency |

### 3. Session Structure

Every session follows a three-phase architecture:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   WARMUP    │────>│    ACTIVE    │────>│  COOLDOWN   │
│  5-15 sec   │     │    60 sec    │     │  5-15 sec   │
│ Preparation │     │ Guided Work  │     │  Recovery   │
└─────────────┘     └──────────────┘     └─────────────┘
```

- **Warmup Phase**: Audio countdown, haptic feedback, mental preparation
- **Active Phase**: Guided breathing with voice cues and binaural beats
- **Cooldown Phase**: Recovery period with completion feedback

### 4. Progression System

```
Session 1 ──> Complete ──> Unlock Session 2 ──> Complete ──> ...
     │                           │
     └─ Track Completion Count   └─ Visual Progress Indicators
```

- Sequential unlocking encourages consistent practice
- Completion counts visible for each session
- Category-based access (subscription unlocks higher tiers)
- Visual status indicators (Current, Locked, Completed)

### 5. Session Recap & Analytics

Post-session analysis includes:

- **Heart Rate Journey Visualization**: Chart showing session progression
- **Biometric Summary Cards**: Key metrics with comparisons
- **Research Links**: Scientific backing for each technique
- **Effectiveness Rating**: User feedback capture
- **Emotional State Tracking**: Calm, Focused, Energized, Relaxed
- **Session History**: Last 5 sessions with thumbnails
- **Share Feature**: Social sharing with results summary

### 6. Apple Watch Companion App

- Start/stop sessions directly from Watch
- Browse full session library on-wrist
- Real-time heart rate display during sessions
- Haptic countdown feedback
- Live Activity support (iOS 16+)
- Seamless iPhone-Watch synchronization
- Offline capability with cached sessions

### 7. Audio & Haptic Feedback

#### Audio Options
- Voice guidance (on/off, volume adjustable)
- Binaural beats (on/off, volume adjustable)
- Countdown audio cues (gentle vibraphone)
- Completion chimes

#### Haptic Options
- iPhone haptic feedback
- Watch haptic countdown ticks
- Phase transition feedback

### 8. Customization Settings

| Setting | Options | Default |
|---------|---------|---------|
| Session Duration | 60 seconds (fixed) | 60 seconds |
| Warmup Duration | 5-15 seconds | 5 seconds |
| Cooldown Duration | 5-15 seconds | 5 seconds |
| Voice Guidance | On/Off + Volume | On, 70% |
| Binaural Beats | On/Off + Volume | On, 50% |
| Haptic Feedback | On/Off | On |
| Countdown Sounds | On/Off | On |

---

## Key Differentiators

### 1. Real-Time Biofeedback (vs. Guided-Only Apps)
Unlike Headspace, Calm, or Breathe: Pausality shows users their heart rate dropping in real-time. This creates a feedback loop that proves the technique is working.

### 2. Dual-Device Flexibility (vs. Watch-Only Apps)
Pausality works with Apple Watch (full biometrics) OR AirPods Pro 3 (heart rate only)—users don't need to own a Watch to get heart rate feedback.

### 3. Science-First Approach (vs. Spirituality-Focused Apps)
Every session links to peer-reviewed research. No mysticism, no vague promises—just physiology.

### 4. Micro-Session Design (vs. Long Meditation Sessions)
1-minute default sessions fit between meetings, in the car, or during any small break. Pausality is for busy people.

### 5. Progressive Skill System (vs. Random Session Selection)
21 sessions unlock sequentially, building physiological capabilities over time—not random daily content.

### 6. Privacy-First Design (vs. Data-Harvesting Apps)
- No third-party data sharing
- Anonymized crash reporting
- Follows Apple HealthKit policies
- PII protection built-in
- No ads, no data selling

---

## Technical Specifications

### Platform Requirements
| Platform | Minimum Version |
|----------|-----------------|
| iOS | 16.0+ |
| watchOS | 9.0+ |
| Xcode | 15.0+ |
| Swift | 5.x |

### Frameworks & Dependencies
- **SwiftUI**: Native UI framework
- **HealthKit**: Biometric data acquisition
- **WatchConnectivity**: Device communication
- **AVFoundation**: Audio playback
- **ActivityKit**: Live Activities (Dynamic Island)
- **RevenueCat**: Subscription management
- **Sentry**: Error monitoring

### Architecture
- MVVM pattern for iOS views
- @Observable macro (Swift 5.9+)
- Async/await concurrency
- @MainActor thread safety
- Actor-based message queuing

### Performance Characteristics
- Offline session support
- Smart API caching (4hr/24hr refresh cycles)
- Battery-optimized Watch monitoring
- 60-second session runtime
- 1-second biometric sampling rate

---

## Pricing & Subscription

### Free Tier
- Access to Foundation category sessions
- Full biometric monitoring
- Session recap and analytics
- Watch app access

### Pausality Premium
**$49.99/year** (with 3-day free trial)

Includes:
- All 21 sessions across all categories
- Foundation + Awareness + Mastery access
- Unlimited session completions
- All current and future sessions
- Cross-device access (iPhone + Watch)

### Purchase Flow
1. User downloads free app
2. Completes Foundation sessions
3. Encounters subscription gate for Awareness/Mastery
4. 3-day free trial offered
5. Annual subscription after trial

---

## User Benefits

### Immediate Benefits (First Session)
- **See your heart rate drop** during first session
- **Visual proof** that breathing exercises work
- **Learn a new technique** with proper guidance
- **Feel calmer** with measurable validation

### Short-Term Benefits (First Week)
- **Understand your stress baseline** through HR patterns
- **Develop consistent practice** with progression system
- **Build breathing awareness** with technique variety
- **Track improvements** in session recap data

### Long-Term Benefits (30+ Days)
- **Faster heart rate recovery** under stress
- **Expanded CO2 tolerance** through advanced techniques
- **Autonomic nervous system regulation** skills
- **Measurable stress resilience** improvements
- **Lower resting heart rate** over time

---

## Competitive Positioning

### Competitive Landscape

| App | Approach | Biofeedback | Session Length | Price |
|-----|----------|-------------|----------------|-------|
| **Pausality** | Science + Data | Real-time HR + SpO2 | 60 sec | $49.99/yr |
| Headspace | Meditation | None | 5-45 min | $69.99/yr |
| Calm | Relaxation | None | 10-30 min | $69.99/yr |
| Breathe (Apple) | Basic breathing | Limited | 1-5 min | Free |
| Othership | Guided breathwork | None | 5-30 min | $99.99/yr |

### Positioning Statement
> For busy professionals who want stress relief they can measure, Pausality is the breathing app that provides real-time biometric feedback during science-backed sessions. Unlike meditation apps that ask you to "feel calmer," Pausality shows your heart rate dropping in real-time—proving it works.

---

## Marketing Messages

### Primary Headlines
1. "Breathing that proves it's working"
2. "See your stress melt away—literally"
3. "Real-time biofeedback breathing"
4. "The data-driven breathwork app"
5. "21 science-backed breathing sessions"

### Secondary Messages
- "1-minute sessions that fit your schedule"
- "Works with Apple Watch OR AirPods Pro 3"
- "Every technique backed by research"
- "Watch your heart rate drop in real-time"
- "Progressive skill building, not random content"

### Feature Callouts
- "Real-time heart rate monitoring"
- "Blood oxygen tracking (with Apple Watch)"
- "21 progressive breathing techniques"
- "Science-backed methods with research links"
- "Heart rate tracking with AirPods Pro 3"
- "60-second sessions"
- "Offline session support"

### Trust Builders
- "By Somnistics Research Labs"
- "Every session links to peer-reviewed research"
- "Follows Apple HealthKit privacy policies"
- "No ads, no data selling"

---

## FAQ Reference

### General Questions

**What is Pausality?**
Pausality is an iOS/watchOS app offering 21 science-backed guided breathing sessions with real-time biometric feedback. Users see their heart rate and blood oxygen change during sessions—proving the techniques work.

**How is Pausality different from meditation apps?**
Pausality provides real-time biometric feedback showing physiological changes during sessions. Instead of asking you to "feel calmer," it shows your heart rate dropping on screen.

**What device do I need?**
For full biometrics (heart rate + blood oxygen), use Apple Watch Series 4+. For heart rate only, AirPods Pro 3 works. Audio-only mode is available but does not record biometric data.

**How long are the sessions?**
All sessions are 60 seconds (1 minute). The app is designed for busy people who need quick stress relief that fits between meetings or during short breaks.

**What breathing techniques are included?**
21 techniques spanning: diaphragmatic breathing, coherent breathing, extended exhale, CO2 tolerance training, nervous system regulation, and acute stress recovery protocols.

### Technical Questions

**What devices are required?**
- iPhone with iOS 16+
- Apple Watch Series 4+ (full biometrics: heart rate + blood oxygen)
- OR AirPods Pro 3 (heart rate only)
- Audio-only mode available but does not record biometrics

**What metrics does Pausality track?**
- Heart rate (BPM) in real-time
- Blood oxygen saturation (SpO2) — Apple Watch only
- Heart rate recovery speed
- Session completion history

**Does it work offline?**
Yes. Sessions can be used offline once the app has been opened with internet connection. Biometric monitoring works independently of network status.

### Subscription Questions

**What does the free version include?**
- All Foundation category sessions
- Full biometric monitoring features
- Session recap and analytics
- Watch app access

**What does Premium include?**
- All 21 sessions (Foundation + Awareness + Mastery)
- Priced at $49.99/year
- Includes 3-day free trial

**Can I cancel anytime?**
Yes. Subscriptions can be managed through Apple's App Store subscription settings.

### Privacy Questions

**What data does Pausality collect?**
- Session completion data (anonymized)
- Biometric data during sessions (not shared)
- Crash reports (anonymized, no PII)

**Is my health data shared?**
No. Health data stays on your device and in Apple Health. Pausality does not share biometric data with third parties.

**What are Pausality's privacy policies?**
Pausality follows Apple HealthKit policies for health data. Biometric data stays on your device and in Apple Health. The app is designed with privacy-first principles.

---

## Document Maintenance

This PRD serves as the single source of truth for:
- Website copy and landing pages
- App Store listing content
- Social media messaging
- PR and media materials
- AEO (Answer Engine Optimization) content
- SEO keyword targeting
- Customer support responses

**Update Protocol:**
- Update this document when features change
- All marketing content should reference this PRD
- Version number should match app version

---

**Document Owner:** Somnistics Research Labs, Inc.
**Contact:** jason@somnistics.com

---

*Copyright © 2024-2026 Somnistics Research Labs, Inc. All rights reserved.*
