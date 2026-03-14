---
id: "urn:srl:chat:chatgpt-board-report-comparison"
type: chat-import
title: "Board report comparison"
status: draft
created: 2025-09-14
imported: 2026-03-14
platform: chatgpt
dc:source: "chatgpt-export:68c6b6a0-d4d4-8332-8ea7-6b6e861b6b21"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: 2
char_count: 10789
---
# Board report comparison

**Date:** 2025-09-14 | **Messages:** 2 | **~2697 tokens**

## Key Takeaways

- *Pending extraction*

## Extracted Nodes

- *Pending extraction*

---

## Transcript

**Randy:**

Role: advisor. Consider the following. Present a board report to this board and produce recommendstions.

Here’s what I found, cross-checked and sourced, on Headspace vs Calm in terms of their publicly declared SOC 2 / security / privacy posture. Some gaps remain, especially for Calm. Use this to benchmark and to sensitize what evidence you might demand or must replicate.

⸻

Headspace

What is publicly known

Based on multiple sources, Headspace (including its enterprise / medical services side) has a relatively mature compliance posture:
	1.	SOC 2 Type II, HITRUST, ISO 27001 / ISO 27002
Headspace claims official certification in SOC 2 Type II, HITRUST, and ISO 27001 & 27002.  
	2.	HIPAA compliance (for certain services) + Business Associate Agreement (BAA)
	•	The enterprise / clinical side (Headspace Care, etc.) will sign a BAA and handle PHI / ePHI (protected / electronic HIPAA health data).  
	•	The consumer-facing meditation app (non-clinical side) is not under HIPAA for PHI (unless tied to clinical services).  
	3.	Security & Privacy Practices
	•	They maintain a risk-based security & privacy program with written policies, risk assessments, monitoring, threat identification, etc.  
	•	Physical & environmental security: their data centers meet SSAE 18, ISAE 3402, ISO 27001, HITRUST, FedRAMP standards.  
	•	Employee training & awareness is part of their program (via Litmos) for privacy, security, HIPAA, etc.  
	4.	Audit / Assurance
	•	They have external audits (HITRUST, SOC 2 etc.) and roles in the organization focused on managing those audits.  
	•	They emphasize continuous review and improvement of controls.  

⸻

What is less clear or missing in public sources
	•	I didn’t find a public copy of the SOC 2 Type II report (i.e. the full attestation) for Headspace: who the auditor is, the exact period, or whether any exceptions were noted.
	•	The scope of what systems / data are included under their SOC2 / HITRUST isn’t fully spelled out publicly (which parts of their stack, clinical vs non-clinical, third parties, etc.).
	•	For the consumer-side, what level of PHI / privacy / confidentiality is included (or excluded) beyond the general statements.

⸻

Calm

What is publicly known

Information on Calm’s SOC 2 / similar compliance is more limited / ambiguous, based on what I found.
	1.	Data Processing Agreement (DPA)
Calm has a DPA (since Dec. 2022) specifying some commitments around how they act as processor or controller, which indicates they take customer data handling and data protection seriously.  
	2.	Security / Privacy Disclosures
	•	Calm’s privacy policy details rights, opt-outs, etc.  
	•	Calm is part of Microsoft 365 App Certification (“Calm - Microsoft 365 App Certification (Teams)”) which includes responses about data retention, access control, vulnerability management, etc. As part of that, Calm reports having:
• Data retention and disposal process.  
• Data access management.  
• Process for identifying and risk ranking security vu

*[message truncated — full text in source]*

---

**ChatGPT:**

Here’s a board-level report based on your Headspace vs. Calm research. I’ve structured it to brief the board on findings, implications, and concrete recommendations for Somnistics Research Labs (SRL).  

---

# 📑 Board Report: SOC 2 Benchmarking (Headspace vs. Calm)  

## Executive Summary
We benchmarked Headspace and Calm’s publicly available security, compliance, and privacy posture.  
- **Headspace** demonstrates a mature compliance framework, claiming SOC 2 Type II, HITRUST, ISO 27001/27002, and HIPAA/BAA readiness.  
- **Calm** offers far less transparency; no verifiable SOC 2 attestation surfaced, though they publish a Data Processing Agreement and participate in Microsoft 365 App Certification.  

**Implication for SRL**: Enterprise healthcare partners (e.g., Mayo Clinic, University of Washington Medical Center) will expect *Headspace-level assurance* (SOC 2, HIPAA, continuous monitoring). Calm’s lighter posture highlights the credibility gap we can exploit—but also warns that opacity will trigger buyer hesitation.  

---

## Findings

### Headspace  
✅ **SOC 2 Type II** – public claim, though full auditor report not accessible.  
✅ **HITRUST, ISO 27001/27002** – strong signals of systematic controls.  
✅ **HIPAA + BAA** – available for clinical services (not consumer meditation app).  
✅ **Security & Privacy Program** – documented policies, risk-based controls, training.  
✅ **Audits & Continuous Review** – external audits are a recurring commitment.  
⚠️ **Gaps** – No public SOC 2 report details (auditor, scope, exceptions); consumer vs. clinical scope not fully clear.  

### Calm  
❓ **SOC 2** – no verifiable public claim or attestation.  
⚠️ **HIPAA / BAA** – unclear whether Calm handles PHI under HIPAA.  
✅ **Data Processing Agreement (2022)** – limited commitments around controller/processor roles.  
✅ **Microsoft 365 App Certification** – discloses vulnerability, retention, and recovery practices.  
✅ **Privacy Policy & Mozilla Review** – show consumer protections but also flagged gaps in data use transparency.  
⚠️ **Gaps** – No SOC 2 / ISO / HITRUST certifications disclosed; evidence fragmented; limited transparency compared to Headspace.  

---

## Comparative Snapshot  

| Capability | Headspace | Calm |
|------------|-----------|------|
| **SOC 2 Type II** | ✅ Public claim | ❓ None found |
| **HITRUST / ISO 27001** | ✅ Yes | ❌ None found |
| **HIPAA / BAA** | ✅ Yes (clinical) | ❓ Not confirmed |
| **Audit & External Certifications** | ✅ Multiple | ⚠️ Microsoft App Cert only |
| **Transparency of Evidence** | Higher | Lower |

---

## Implications for SRL  
1. **Healthcare enterprise bar**: Mayo, UW, and similar partners will require at minimum **SOC 2 Type II + HIPAA BAA** for trust and procurement clearance.  
2. **Strategic moat**: Headspace demonstrates that meditation/wellness apps *must* show compliance maturity when moving into clinical and enterprise sales. Calm’s opacity leaves them vulnerable to enterprise pushback.  


*[message truncated — full text in source]*

---

