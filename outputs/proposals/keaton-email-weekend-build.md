Keaton,

Really enjoyed meeting you today. What you're building — an anesthesia app with Claude, selling it, running Instagram ads, trading influencer deals while still in school — that's exactly the kind of energy this profession needs. Your dad raised a builder.

I wanted to share what I built this weekend because I think you'll appreciate it as someone who's already deep in the AI tooling. It took about 48 hours of working sessions with Claude, and what came out of it surprised even me.

Here's the short version of what happened:

I started with a problem. I have 861 ChatGPT conversation files from the last six months — every strategic decision, clinical insight, concept I've developed, and research thread for Somnistics Research Labs. All of it trapped in chat transcripts. Unusable. I also have a knowledge graph in Obsidian with 180+ linked notes covering our science, evidence, concepts, and clinical observations. But the two systems weren't connected, and the graph wasn't growing on its own.

Over the weekend I built a system called Vigil — named for the watchfulness that defines what we do as anesthesia providers. It's an AI orchestrator that manages six specialized bots, each with its own identity, skills, run protocol, and self-improvement loop. Here's what each one does:

1. Transcript Triage — scans and prioritizes those 861 files by extraction value
2. Knowledge Miner — reads each transcript and extracts only my original thinking, not the AI's elaboration
3. Vault Writer — validates everything against our metadata standards and writes it into the knowledge graph
4. Review Accelerator — auto-resolves 80% of flagged items so I only review what truly needs clinical judgment
5. Citation Resolver — verifies every study citation against PubMed so nothing hallucinated gets into the system
6. Extraction Coordinator — manages the pipeline, tracks progress, runs retrospectives

The bots improve every run. They write retrospectives after each batch, accumulate pattern libraries, and feed each other feedback. The review accelerator learns from my accept/reject decisions and handles more autonomously over time.

In the first 48 hours, the system:
- Created 59 new vault notes (evidence, concepts, observations)
- Wired 155 graph edges linking concepts to evidence
- Ran 3 PubMed literature scans (interoception, clinician durability, surgeon performance psychology)
- Ingested 46 peer-reviewed studies and verified all citations against PubMed
- Caught and corrected 3 citation errors before they went public
- Built a 58-person contact tracker from mentions across the vault
- Produced a 700-word article on clinician durability training sourced entirely from the graph

Then the founder of Audible emailed my co-founder Jason with three hard questions about our product. I pointed Vigil at the knowledge graph, it ran a same-day PubMed scan, sourced every claim to verified studies — three published that same month — and I had a response drafted within hours. From a living knowledge base, not from memory.

The whole system runs on an Obsidian vault with three metadata standards (Dublin Core for sources, SKOS for concept relationships, PROV-O for provenance chains), an MCP server that lets Claude read and write to the vault, and prompt-based bot definitions — no code, just markdown files that Claude reads and executes.

I'm telling you this because you're already building with Claude and you understand what's possible. This isn't science fiction. It's 42 markdown files, a Python MCP server, and a clear architecture. The vault grows while I sleep. The bots get better every run. And every claim traces back to a verified source.

Keep building. What you're doing with the anesthesia app — getting it to market, running ads, trading influencer deals — that's the hardest part. The AI just makes the knowledge layer compoundable.

Would love to stay connected and see where your app goes. And if you ever want to nerd out about Claude workflows or the intersection of anesthesia and AI, I'm here for it.

Run well,
Randy


Randy Graybeal, MSN CRNA
Co-Founder, Somnistics Research Labs
AANA #071955
