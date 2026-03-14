---
id: "urn:srl:chat:chatgpt-prompt-creation-for-biofeedback"
type: chat-import
title: "Prompt creation for biofeedback"
status: draft
created: 2025-09-07
imported: 2026-03-14
platform: chatgpt
dc:source: "chatgpt-export:68bd94ef-c5cc-832f-be7d-27df120bc98c"
participants: ["Randy Graybeal", "ChatGPT"]
extracted_concepts: []
extracted_evidence: []
key_takeaways: []
message_count: 18
char_count: 88686
---
# Prompt creation for biofeedback

**Date:** 2025-09-07 | **Messages:** 18 | **~22171 tokens**

## Key Takeaways

- *Pending extraction*

## Extracted Nodes

- *Pending extraction*

---

## Transcript

**Randy:**

Role Prompt Engineer: Create a prompt to: 

FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. Biosensors collect signals from the user, an AI “machine” processes these signals and runs an influencing algorithm, and actuators deliver feedback to the user​. This conceptual diagram underpins the invention’s closed-loop approach, wherein the user’s physiological data guide the system’s feedback actions in real time.

---

**ChatGPT:**

Here’s a clean role prompt you can use to reliably generate outputs like the FIG. 1 closed-loop biofeedback description:  

---

### Prompt  
**Role:** Patent Technical Writer & Systems Architect  

**Instruction:**  
Generate a clear, formal description of a conceptual system diagram for a patent filing. The description should:  
- Identify each component in the diagram (e.g., biosensors, AI processor, actuators, human user).  
- Explain the flow of information/signals between components in sequence.  
- Emphasize the *closed-loop* nature of the system (data collected → processed by algorithm → feedback delivered → user responds → cycle repeats).  
- Use precise technical language suitable for patents (e.g., “in the loop,” “in real time,” “physiological data guide the system’s feedback actions”).  
- Avoid speculative or promotional language. Stick to factual, architectural description.  
- Provide enough detail that the figure can “stand alone” when paired with the text.  

**Example Output Style (applied to FIG. 1):**  
“FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. Biosensors collect physiological signals from the user, an AI machine processes the signals and executes an influencing algorithm, and actuators deliver feedback to the user. This conceptual diagram underpins the invention’s closed-loop approach, wherein the user’s physiological data guide the system’s feedback actions in real time.”  

---

Would you like me to extend this into a **template generator** (so you can drop in any new figure description and it will output a patent-ready paragraph automatically), or do you prefer just the static role prompt?

---

**Randy:**

template generator please

---

**ChatGPT:**

Here’s a **Template Generator Prompt** you can reuse to produce patent-ready descriptions of system diagrams like FIG. 1.  

---

## Template Generator Prompt  

**Role:** Patent Technical Writer & Systems Architect  

**Instruction:**  
You are given a figure reference and a list of system components. Your task is to generate a formal description suitable for a patent specification.  

Follow this structure:  
1. **Figure Callout:** Begin with “FIG. X illustrates…”  
2. **System Architecture:** List all major components (human user, sensors, processors, algorithms, actuators, communication channels).  
3. **Signal/Data Flow:** Describe the directional flow of information between components in logical order.  
4. **Closed-Loop Emphasis:** Explicitly state that the architecture is a closed-loop system, where user data informs feedback and the cycle repeats.  
5. **Patent Style:** Use precise, neutral, technical language. Avoid marketing or speculative claims. Ensure the description can “stand alone” if read without the figure.  

---

### Example Input
```
Figure: FIG. 1
Components: Human user, biosensors, AI processor, influencing algorithm, actuators
Focus: Closed-loop biofeedback, real-time physiological data guiding actions
```

### Example Output
```
FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. Biosensors collect physiological signals from the user, an AI processor executes an influencing algorithm to interpret the signals, and actuators deliver corresponding feedback to the user. This configuration establishes a closed-loop cycle, wherein the user’s physiological data guide the system’s feedback actions in real time, enabling continuous adaptation to the user’s state.
```

---

### Reusable Prompt Template
```
Figure: [Insert Figure Label]
Components: [List all system elements here]
Focus: [Specify the central mechanism or property, e.g., closed-loop, adaptive feedback, multimodal sensing]

Task: Generate a patent-style figure description following the template rules.
```

---

Would you like me to turn this into a **ready-to-run AI prompt** (so you can paste in new figures/components and instantly get the output), or a **clickable form/table** (so your team can fill in blanks for each figure systematically)?

---

**Randy:**

Role: Patent Technical Writer & Systems Architect

Instruction:
Generate a clear, formal description of a conceptual system diagram for a patent filing. The description should:
	•	Identify each component in the diagram (e.g., biosensors, AI processor, actuators, human user).
	•	Explain the flow of information/signals between components in sequence.
	•	Emphasize the closed-loop nature of the system (data collected → processed by algorithm → feedback delivered → user responds → cycle repeats).
	•	Use precise technical language suitable for patents (e.g., “in the loop,” “in real time,” “physiological data guide the system’s feedback actions”).
	•	Avoid speculative or promotional language. Stick to factual, architectural description.
	•	Provide enough detail that the figure can “stand alone” when paired with the text.

Example Output Style (applied to FIG. 1):
“FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. Biosensors collect physiological signals from the user, an AI machine processes the signals and executes an influencing algorithm, and actuators deliver feedback to the user. This conceptual diagram underpins the invention’s closed-loop approach, wherein the user’s physiological data guide the system’s feedback actions in real time.”

---

**ChatGPT:**

Got it. Here’s the **ready-to-run template generator** you can use for any figure in your patent filings. Just drop in the figure number, components, and focus, and it will produce a patent-style description:  

---

## Patent Figure Description Generator  

**Role:** Patent Technical Writer & Systems Architect  

**Instruction:**  
Generate a clear, formal description of a conceptual system diagram for a patent filing.  

The description must:  
- Identify each component in the diagram.  
- Explain the flow of information/signals between components in sequence.  
- Emphasize the closed-loop nature of the system (data collected → processed → feedback delivered → user responds → cycle repeats).  
- Use precise, neutral technical language suitable for patents.  
- Avoid speculative or promotional language.  
- Provide enough detail that the figure can “stand alone” when paired with the text.  

---

### Input Template
```
Figure: [Insert Figure Label, e.g., FIG. 2]
Components: [List of all elements, e.g., sensors, processors, databases, communication links, actuators, human user]
Focus: [Specify mechanism or property, e.g., closed-loop biofeedback, multimodal integration, adaptive learning, cloud connectivity]
```

---

### Output Template
```
[FIG. X] illustrates [a general/specific] [system type] architecture incorporating [human user if relevant] within the loop. 
[First component(s)] acquire [data/signals] from [source, e.g., user or environment]. 
These signals are transmitted to [processing unit, e.g., AI processor, controller], which executes [algorithm/logic]. 
Based on the processed signals, [actuators/feedback mechanisms] deliver corresponding output to [the user/environment]. 
This establishes a closed-loop cycle, wherein [user/environment] responses continuously inform subsequent system actions, enabling [real-time/adaptive] operation.
```

---

### Example Run  

**Input**  
```
Figure: FIG. 1
Components: Human user, biosensors, AI processor, influencing algorithm, actuators
Focus: Closed-loop biofeedback, real-time physiological data guiding actions
```

**Output**  
```
FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. Biosensors collect physiological signals from the user, an AI processor executes an influencing algorithm to interpret the signals, and actuators deliver corresponding feedback to the user. This configuration establishes a closed-loop cycle, wherein the user’s physiological data guide the system’s feedback actions in real time, enabling continuous adaptation to the user’s state.
```

---

Would you like me to **convert this into a ClickUp-ready SOP/checklist format** so your team can quickly generate figure descriptions at scale, or keep it as a plain text template for now?

---

**Randy:**

Create the image: Role: Patent Technical Writer & Systems Architect

Instruction:
Generate a clear, formal description of a conceptual system diagram for a patent filing. The description should:
	•	Identify each component in the diagram (e.g., biosensors, AI processor, actuators, human user).
	•	Explain the flow of information/signals between components in sequence.
	•	Emphasize the closed-loop nature of the system (data collected → processed by algorithm → feedback delivered → user responds → cycle repeats).
	•	Use precise technical language suitable for patents (e.g., “in the loop,” “in real time,” “physiological data guide the system’s feedback actions”).
	•	Avoid speculative or promotional language. Stick to factual, architectural description.
	•	Provide enough detail that the figure can “stand alone” when paired with the text.

 Output Style (applied to FIG. 1):
“FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. Biosensors collect physiological signals from the user, an AI machine processes the signals and executes an influencing algorithm, and actuators deliver feedback to the user. This conceptual diagram underpins the invention’s closed-loop approach, wherein the user’s physiological data guide the system’s feedback actions in real time.”

---

**ChatGPT:**

{"prompt":"FIG. 1 illustrates a general closed-loop biofeedback architecture integrating a human user in the loop. The diagram shows: (1) a human user; (2) biosensors attached to the user, collecting physiological signals; (3) an AI processor receiving the biosensor signals; (4) an influencing algorithm running inside the AI processor; (5) actuators delivering feedback to the user. Arrows connect the components in sequence: biosensors → AI processor → algorithm → actuators → back to the human user, forming a closed-loop cycle. The emphasis is on the real-time nature of the loop, where the user’s physiological data guide the feedback actions.","size":"1024x1024","n":1}

---

**Randy:**

Keeping this in mind, help me understand and build on my previous work: Great! I will structure the Somnistics Taxonomy (S.T.E.P. 2.0) within a known traditional taxonomy framework, aligning it as an ontology mapped to established medical and neuroscience knowledge structures like SNOMED CT, Cognitive Atlas, and neuroinformatics databases.
I'll create a visual representation (knowledge graph, hierarchical tree, or multidimensional scaling) to illustrate its relationships and applications. This will serve as the foundation for an AI-driven adaptive system and research database that supports SME-driven educational content.
I'll get back to you with a detailed mapping and visual representation.
Research completed in 6m · 24 sources
Somnistics Taxonomy (S.T.E.P. 2.0) Ontology Overview
The Somnistics Taxonomy (S.T.E.P. 2.0) is a comprehensive ontology that integrates domains of human physiology, cognition, emotion, sleep, and performance into a unified hierarchical framework. It is designed for AI-driven adaptive systems, aligning with established medical and neuroscience knowledge bases for interoperability. Each concept in the taxonomy is defined with formal attributes and linked to standard identifiers (e.g. SNOMED CT codes for clinical terms, Cognitive Atlas IDs for cognitive processes) to ensure consistency​
bioportal.bioontology.org
​
cognitiveatlas.org
. The hierarchy organizes broad domains (parent categories) into progressively specific sub-concepts (children), capturing “entities and the relationships between them” in a multi-level structure​
falkordb.com
​
falkordb.com
. This structured approach enables semantic reasoning across diverse fields – from clinical biofeedback data to cognitive training exercises – facilitating an adaptive learning platform that can personalize interventions.
 Figure: Example of a multi-level knowledge graph bridging psychological and biological concepts, analogous to the Somnistics ontology. Cognitive constructs (e.g. Working Memory Updating, green) link to neural systems (e.g. Dorsolateral Prefrontal Cortex, gold) and even molecular pathways (e.g. Dopamine D1 receptor, red), illustrating how our taxonomy connects cognitive processes with brain regions and biomarkers​
researchgate.net
. Such a layered ontology aligns with frameworks like the Cognitive Atlas and RDoC, relating mental functions to neural circuits and gene pathways in a research knowledge base.
Hierarchical Structure and Parent–Child Relationships
The Somnistics S.T.E.P. 2.0 ontology is organized into several top-level domains, each of which contains more granular child concepts. Below is an outline of the hierarchy, showing parent categories, their definitions, and key sub-concepts (with examples of attributes and interdependencies):
Physiological Regulation – Parent domain covering bodily states and autonomic functions that underlie mind-body integration. This aligns with SNOMED CT’s physiological and clinical findings hierarchy (e.g. heart rate,

*[message truncated — full text in source]*

---

**ChatGPT:**

Randy — love where you’re taking S.T.E.P. 2.0. Below is a tight, build-ready package: quick summary, then concrete artifacts you can paste into your repo (schema, JSON-LD, relation vocab, example nodes, rules, and visualization). No fluff—just scaffolding you can run with.

# Summary → What’s Next
- **Lock the ontology spine** (classes + relations) so every script, module, and dataset binds the same way.
- **Stand up a minimal KG** with 6–10 exemplar concepts (HRV, Respiratory Rate, Attention, Working Memory, DLPFC, Stress Response, Flow State) + 3 modules (HRV biofeedback, Paced Breathing, N-Back).
- **Wire the loop**: sensor → feature → concept node → policy → intervention module → outcome → concept update.
- **Governance**: semantic versioning (e.g., `step-2.0.0`), change log, curator roles, mapping file per external standard.

---

# Deep Dive (build pieces you can copy/paste)

## 1) Ontology skeleton (classes)
- `Concept` (abstract)  
  - `PhysiologicalMetric` (e.g., HRV, RespiratoryRate)  
  - `PhysiologicalProcess` (AutonomicState, SleepStage)  
  - `CognitiveProcess` (Attention, WorkingMemory, CognitiveFlexibility)  
  - `AffectiveState` (StressResponse, Mood)  
  - `InteroceptiveSkill` (InteroceptiveSensitivity, Mind-BodyIntegration)  
  - `SocialProcess` (Empathy, TheoryOfMind)  
  - `IntegratedPerformanceState` (FlowState, MindfulCalm)  
  - `NeuralSystem` (DLPFC, Insula, Networks)  
  - `InterventionModule` (HRV_Biofeedback, PacedBreathing, NBack_Training)  
  - `AssessmentTask` (PVT, NBack_Test, HeartbeatCounting)  
  - `Observation` (typed value events: HRV_SDNN, SleepScore, PANAS)  
- `Reference` (external codes: SNOMED, UMLS, Cognitive Atlas, NeuroLex, IEEE 11073/LOINC)
- `Policy` (adaptive rules, eligibility, dosage)
- `UserState` (per-user overlays)

## 2) Relation vocabulary (keep it small + expressive)
- Hierarchy: `isA`, `partOf`
- Semantics: `influences`, `regulates`, `correlatesWith`, `implementedBy` (Cognitive→Neural), `measuredBy` (Concept→AssessmentTask), `trains` (InterventionModule→Concept), `targets` (InterventionModule→Concept), `contraindicatedFor` (Module→Condition)
- Operational: `updatedBy` (Concept←Observation), `precedes` (Module/Concept→Module), `requires` (Module→Skill/Prereq), `evidenceFrom` (Concept→Reference)

> Keep relation names verb-first, single tense. You’ll thank yourself later when querying.

## 3) JSON-LD @context (portable, future-proof)
```json
{
  "@context": {
    "id": "@id",
    "type": "@type",
    "Concept": "https://somnistics.org/step/Concept",
    "PhysiologicalMetric": "https://somnistics.org/step/PhysiologicalMetric",
    "PhysiologicalProcess": "https://somnistics.org/step/PhysiologicalProcess",
    "CognitiveProcess": "https://somnistics.org/step/CognitiveProcess",
    "AffectiveState": "https://somnistics.org/step/AffectiveState",
    "InteroceptiveSkill": "https://somnistics.org/step/InteroceptiveSkill",
    "IntegratedPerformanceState": "https://somnistics.org/step/IntegratedPerf

*[message truncated — full text in source]*

---

**Randy:**

This feels very incomplete as to both the scope of the interventions as well as the cognitive, physiologic, emotional, and anatomic targets. 

Role: you have been hired as a professional Advanced Library Science consultant. Review and recommend steps for the Somnistics Research Lab team. 

---

**ChatGPT:**

Randy — agreed. To make S.T.E.P. 2.0 truly operable, we need a **library-grade knowledge organization system (KOS)** that covers the **full intervention universe** and the **full target universe** across cognition, physiology, affect, and anatomy—plus governance, evidence control, and retrieval. Below is a professional library-science plan you can hand to the team.

---

# 1) Scope expansion: controlled vocabularies (facets)

## 1A. Intervention Facets (what we *do*)
Define each intervention by the following **facets** (each facet is a controlled vocabulary; any intervention = a combination of facet values).

- **Modality** *(primary)*:  
  Breathwork ▸ Biofeedback (HRV, RSA, GSR, EMG) ▸ Neurofeedback (EEG bands, SCP) ▸ Cognitive Training (attention, WM, inhibition, set-shifting) ▸ Somatic Practices (progressive relaxation, yoga asana families, tai chi, Feldenkrais) ▸ Interoceptive Awareness (body scan, heartbeat detection) ▸ Visual/Auditory/Haptic Guidance (pacer, binaural beats, vibrotactile cues) ▸ Behavioral Protocols (sleep hygiene, light therapy, stimulus control) ▸ Social/Relational (compassion, perspective-taking, co-regulation) ▸ Psychoeducation ▸ Environmental (light, temperature, scent, posture) ▸ Pharmacologic adjuncts *(placeholder for future; keep off by default)*.
- **Breathwork subtype**:  
  Coherent breathing (~6 bpm), Box (4-4-4-4), 4-7-8, Double inhale/long exhale, Extended exhale, Apnea training (hypo/hypercapnia ladders), Alternate nostril, Ujjayi, Bhramari (humming), Pursed-lip, Resistance devices.
- **Feedback channel(s)**: Visual ▸ Auditory ▸ Haptic ▸ Multimodal.
- **Sensor requirement(s)**: PPG/HRV ▸ ECG ▸ Resp belt/camera ▸ GSR ▸ EMG ▸ EEG ▸ Actigraphy ▸ Pupillometry ▸ Camera micro-expressions ▸ IMU/balance.
- **Dose**: duration (sec/min), reps, sets, weekly frequency, progression rule.
- **Intensity**: low / moderate / high; *or* numeric scale tied to CO₂ load or cognitive load.
- **Delivery context**: pre-op, night routine, in-between cases, commute, post-stress decompression, pre-performance, pediatric family session, clinic.
- **Objective(s)** *(link to Targets below)*: down-regulate sympathetic arousal, increase vagal tone, increase sustained attention, increase WM span, improve sleep onset, etc.
- **Evidence level**: GRADE or Somnistics Evidence Tier (A/B/C/D) with citation keys.
- **Contraindications & cautions**: asthma, panic disorder w/ interoceptive focus, pregnancy, migraines (for hyperventilation), epilepsy (for flashing visuals), PTSD triggers; supervision required Y/N.
- **Prerequisites**: skills or baseline measures required.
- **Population tags**: CRNA on-call, pediatrics caregiver, high-altitude, post-concussion, ADHD, anxiety-spectrum, elite athlete.

> Deliverable: a CSV/JSON master list for each facet; every intervention record must pick at least one value from each mandatory facet.

---

## 1B. Target Facets (what we *change*)
Map each intervention to explicit targets across four planes. These beco

*[message truncated — full text in source]*

---

**Randy:**

Role: You are an advanced library scientist consulting on this project. Analyze and create recommendations for organizing

---

**ChatGPT:**

Randy — stepping into full **Library Science consultant mode**, here’s a structured analysis and recommendations for how Somnistics Research Labs should organize S.T.E.P. 2.0 as a living knowledge infrastructure.  

---

# 1. Core Organizing Principles

### Controlled Vocabularies (Faceted Classification)
- **Facets** = dimensions you catalog every entity/intervention against.  
  - *Who/What it targets* (Physiology, Cognition, Affect, Anatomy/Networks)  
  - *What is done* (Intervention modality, sub-technique, dose, delivery context)  
  - *How it is measured* (Assessment tasks, biomarkers, devices)  
  - *Evidence tier* (A–D scale, linked citations)  
  - *Safety/Contraindications* (population flags, conditions, supervision requirements)

### Polyhierarchy vs. Tree
- Use a **polyhierarchical model**: one concept can appear in multiple hierarchies (e.g., “PTSD” under both *Emotional* and *Physiological Stress Disorders*).  
- This mimics SNOMED CT’s multi-axiality and prevents artificial silos.

### Crosswalks
- Every node must carry **external codes**:  
  - SNOMED CT, LOINC (physiology, clinical findings)  
  - Cognitive Atlas IDs (cognition, tasks)  
  - NeuroLex/Allen Atlas IDs (anatomy)  
  - RDoC domains (functional/psychiatric research alignment)  
  - IEEE 11073 (biosignal/device standards)

---

# 2. Structural Recommendations

### A. Multi-faceted Catalog
Treat each **Intervention Record** and **Target Record** like catalog entries in a library:
- Required fields: ID, label, definition, mappings, evidence, attributes, contraindications, provenance.
- Optional fields: scripts, media, contextual notes.

### B. Ontology Schema (Classes)
- **Concepts**: PhysiologicalMetric, PhysiologicalProcess, CognitiveProcess, AffectiveState, InteroceptiveSkill, NeuralSystem, IntegratedPerformanceState  
- **Modules**: InterventionModule, AssessmentTask, BiofeedbackDevice, ContentModule  
- **Operational**: Observation, UserState, PolicyRule  

### C. Relationships (Semantic Edges)
- `isA`, `partOf`, `implementedBy`, `measuredBy`, `trains`, `targets`, `contraindicatedFor`, `requires`, `precedes`, `evidenceFrom`

### D. Governance
- **Versioned ontology repo** (semver, changelog, curator review)  
- **Evidence curation workflow**: every new intervention must include an appraisal paragraph + citations.  
- **Safety gate**: librarian + SME co-sign before publishing new modules.

---

# 3. Retrieval & Access Model

### Catalog Queries
Support the most common user queries:
- “Show me safe, ≤2 minute interventions targeting vagal tone, no sensors.”  
- “List all Tier A/B interventions mapped to DLPFC.”  
- “What interventions co-train Attention + Stress Recovery?”  

### Indexes
- Duration  
- Sensor requirements  
- Primary targets  
- Evidence tier  
- Safety class  

### Views
- **Knowledge Graph** (for researchers)  
- **Hierarchical tree** (for clinicians, SMEs)  
- **Faceted search UI** (for product users or app integration)

---

# 4. Evidence & Safet

*[message truncated — full text in source]*

---

**Randy:**

copy and paste the last answer into the appropriately named file inside of the most appropriate SRL folder

---

**ChatGPT:**

Right now I can’t directly copy a block of text into your SRL Google Drive or local filesystem — I don’t have write access to your folders.  

What I *can* do is:  
- Package the last answer (the advanced library science analysis + recommendations) into a clean file format (Markdown, DOCX, PDF, etc.) and hand it back to you here.  
- You can then drop it into the most appropriate SRL subfolder yourself (likely under something like `SRL/BLIP_Clinic_Organized/03_RESEARCH_FRAMEWORKS/Taxonomy_Development/` or `SRL/Knowledge_Structures/Library_Science_Consulting/`).  

---

### Next step options:
1. ✅ I generate a `Somnistics_Taxonomy_LibraryScience_Recommendations.md` (or `.docx`) containing the full structured answer.  
2. You download it and move it into the SRL folder where you’re keeping ontology/consulting notes.  

Would you like me to prep it as **Markdown**, **Word**, or **PDF**?

---

**Randy:**

markdown

---

**ChatGPT:**

I’ve created the file in Markdown format:  

**`Somnistics_Taxonomy_LibraryScience_Recommendations.md`**  

You can download it here: [Download File](sandbox:/mnt/data/Somnistics_Taxonomy_LibraryScience_Recommendations.md)  

Once downloaded, drop it into your `SRL/BLIP_Clinic_Organized/03_RESEARCH_FRAMEWORKS/` folder (or whichever SRL subdirectory you prefer for ontology/consulting notes).  

Would you like me to also generate a **ClickUp-ready SOP checklist** version of this so your team can act on it directly?

---

