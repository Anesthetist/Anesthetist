#!/usr/bin/env python3
"""
Generate review queue JSON for the SRL Review GUI.

Modes:
  --extractions     Parse extraction reports (existing behavior)
  --clinical        Pull concepts with "Pending review" clinical_interpretation
  --custom FILE     Load a custom review queue JSON (Vigil-generated)
  --all             Run all available modes

Output: tools/review-data.json (loaded by review-gui.html)
"""

import json
import re
import sys
import os
from pathlib import Path
from datetime import datetime
import yaml

VAULT_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = VAULT_ROOT / "concepts"
EVIDENCE_DIR = VAULT_ROOT / "evidence"
OBSERVATIONS_DIR = VAULT_ROOT / "observations"
EXTRACTIONS_DIR = VAULT_ROOT / "outputs" / "extractions"
OUTPUT_FILE = Path(__file__).parent / "review-data.json"

# ─── Extraction report parsing (from extract-review-data.py) ───

RANDY_SIGNALS = [
    "randy uses", "randy's voice", "randy coined", "randy named",
    "randy's term", "randy provided", "randy directed", "randy commissioned",
    "randy explicitly", "randy asks", "randy specified", "our concept of",
    "randy's canonical", "possessive", "randy describes"
]
LLM_SIGNALS = [
    "chatgpt proposed", "chatgpt's", "synthesized by chatgpt",
    "chatgpt-generated", "chatgpt's marketing", "chatgpt coined",
    "chatgpt built", "likely skip", "marketing language"
]
ESTABLISHED_SIGNALS = [
    "established", "foundational reference", "known scientific",
    "standard engineering term", "literature term"
]


def infer_provenance(text: str) -> str:
    lower = text.lower()
    randy_score = sum(1 for s in RANDY_SIGNALS if s in lower)
    llm_score = sum(1 for s in LLM_SIGNALS if s in lower)
    established_score = sum(1 for s in ESTABLISHED_SIGNALS if s in lower)
    if established_score > 0 and randy_score == 0:
        return "established-science"
    if randy_score > llm_score:
        return "randy-originated"
    if llm_score > randy_score:
        return "llm-generated"
    if randy_score > 0 and llm_score > 0:
        return "collaborative"
    return "unclassified"


def infer_confidence(text: str) -> str:
    lower = text.lower()
    if "very high" in lower or "confidence: high" in lower or "confidence:** high" in lower:
        return "high"
    if "confidence: medium" in lower or "confidence:** medium" in lower:
        return "medium"
    if "confidence: low" in lower or "confidence:** low" in lower or "likely skip" in lower:
        return "low"
    return "medium"


def parse_yaml_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    match = re.match(r'^---\s*\n(.+?)\n---', text, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)) or {}
        except:
            return {}
    return {}


def parse_body(text: str) -> str:
    """Extract body content after YAML frontmatter."""
    match = re.match(r'^---\s*\n.+?\n---\s*\n(.*)', text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()


# ─── Clinical interpretation queue ───

def build_clinical_queue() -> list:
    """Find all concept notes with 'Pending review' clinical interpretation."""
    items = []
    if not CONCEPTS_DIR.exists():
        return items

    for md_file in sorted(CONCEPTS_DIR.glob("*.md")):
        text = md_file.read_text()
        if "Pending review" not in text:
            continue

        fm = parse_yaml_frontmatter(text)
        body = parse_body(text)

        # Extract first paragraph as preview
        body_lines = [l for l in body.split('\n') if l.strip() and not l.startswith('#')]
        preview = body_lines[0] if body_lines else ""

        slug = md_file.stem
        items.append({
            "id": fm.get("id", f"urn:srl:concept:{slug}"),
            "slug": slug,
            "title": fm.get("title", slug),
            "category": "clinical-interpretation",
            "review_type": "clinical",
            "status": fm.get("status", "draft"),
            "subjects": fm.get("dc:subject", []),
            "broader": fm.get("skos:broader", []),
            "related": fm.get("skos:related", []),
            "body": body[:2000],
            "preview": preview[:300],
            "source_file": str(md_file.relative_to(VAULT_ROOT)),
            "prompt": "Add your clinical interpretation — what does this mean for CRNA practice?",
            "decision": None,
            "notes": ""
        })

    return items


# ─── Status promotion queue ───

def build_promotion_queue() -> list:
    """Find all notes in 'draft' or 'review' status that could be promoted."""
    items = []
    for note_dir in [CONCEPTS_DIR, EVIDENCE_DIR, OBSERVATIONS_DIR]:
        if not note_dir.exists():
            continue
        for md_file in sorted(note_dir.glob("*.md")):
            text = md_file.read_text()
            fm = parse_yaml_frontmatter(text)
            status = fm.get("status", "")
            if status not in ("draft", "review"):
                continue
            note_type = fm.get("type", note_dir.name.rstrip("s"))
            slug = md_file.stem
            body = parse_body(text)
            body_lines = [l for l in body.split('\n') if l.strip() and not l.startswith('#')]
            preview = body_lines[0] if body_lines else ""

            items.append({
                "id": fm.get("id", f"urn:srl:{note_type}:{slug}"),
                "slug": slug,
                "title": fm.get("title", slug),
                "category": "promotion",
                "review_type": "promotion",
                "note_type": note_type,
                "status": status,
                "subjects": fm.get("dc:subject", []),
                "body": body[:1000],
                "preview": preview[:300],
                "source_file": str(md_file.relative_to(VAULT_ROOT)),
                "prompt": f"Promote from '{status}' to next level?",
                "decision": None,
                "notes": ""
            })

    return items


# ─── Extraction report parsing (preserved from original) ───

def parse_detailed_report(filepath: Path) -> dict:
    text = filepath.read_text()
    result = {"file": filepath.name, "concepts": [], "enrichments": [],
              "evidence": [], "observations": [], "flags": []}

    source_match = re.search(r'\*\*Source:\*\*\s*(.+)', text)
    date_match = re.search(r'\*\*Date processed:\*\*\s*(.+)', text)
    summary_match = re.search(r'## Summary\n\n(.+?)(?=\n##)', text, re.DOTALL)

    result["source"] = source_match.group(1).strip() if source_match else ""
    result["date_processed"] = date_match.group(1).strip() if date_match else ""
    result["summary"] = summary_match.group(1).strip() if summary_match else ""

    # Parse concept candidates
    concept_blocks = re.split(r'### Candidate \d+:', text)
    for block in concept_blocks[1:]:
        title_match = re.search(r'^\s*(.+?)$', block, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown"
        id_match = re.search(r'id:\s*(urn:srl:\S+)', block)
        concept_id = id_match.group(1) if id_match else f"urn:srl:concept:{title.lower().replace(' ', '-')}"
        body_match = re.search(r'\*\*Body:\*\*\s*(.+?)(?=\n\n\*\*|\n---|\Z)', block, re.DOTALL)
        body = body_match.group(1).strip() if body_match else ""
        voice_match = re.search(r"\*\*Randy's voice.*?\*\*\s*(.+?)(?=\n\n\*\*|\n---|\Z)", block, re.DOTALL)
        randy_voice = voice_match.group(1).strip() if voice_match else ""
        conf_match = re.search(r'\*\*Extraction confidence:\*\*\s*(.+?)(?=\n|\Z)', block)
        conf_text = conf_match.group(1).strip() if conf_match else ""
        subjects_match = re.search(r'dc:subject:\s*\[(.+?)\]', block)
        subjects = [s.strip().strip('"').strip("'") for s in subjects_match.group(1).split(",")] if subjects_match else []
        broader_match = re.search(r'skos:broader:\s*\[(.+?)\]', block)
        related_match = re.search(r'skos:related:\s*\[(.+?)\]', block)
        broader = [s.strip().strip('"').strip("'") for s in broader_match.group(1).split(",")] if broader_match else []
        related = [s.strip().strip('"').strip("'") for s in related_match.group(1).split(",")] if related_match else []
        full_text = block + " " + conf_text + " " + randy_voice
        result["concepts"].append({
            "id": concept_id, "title": title, "category": "new-concept",
            "review_type": "extraction", "provenance": infer_provenance(full_text),
            "confidence": infer_confidence(full_text), "body": body,
            "randy_voice": randy_voice, "confidence_note": conf_text,
            "subjects": subjects, "broader": broader, "related": related,
            "source_file": filepath.name, "decision": None, "notes": ""
        })

    # Parse enrichments
    enrichment_blocks = re.split(r'### Enrichment \d+:', text)
    for block in enrichment_blocks[1:]:
        title_match = re.search(r'^\s*(\S+)', block, re.MULTILINE)
        target = title_match.group(1).strip() if title_match else "unknown"
        addition_match = re.search(r'\*\*Addition.*?\*\*\s*(.+?)(?=\n\n\*\*|\n###|\n---|\n## |\Z)', block, re.DOTALL)
        addition = addition_match.group(1).strip() if addition_match else block.strip()[:500]
        status_match = re.search(r'\*\*Status:\*\*\s*(.+?)(?=\n|\Z)', block)
        status = status_match.group(1).strip() if status_match else ""
        result["enrichments"].append({
            "id": f"enrich-{target}-{len(result['enrichments'])}", "target_concept": target,
            "category": "enrichment", "review_type": "extraction", "addition": addition,
            "status": status, "source_file": filepath.name, "decision": None, "notes": ""
        })

    # Parse evidence
    evidence_blocks = re.split(r'### Evidence \d+:', text)
    for block in evidence_blocks[1:]:
        title_match = re.search(r'^\s*(.+?)$', block, re.MULTILINE)
        dc_title = re.search(r'\*\*Title:\*\*\s*(.+)', block)
        relevance = re.search(r'\*\*Relevance:\*\*\s*(.+)', block)
        result["evidence"].append({
            "id": f"evidence-{len(result['evidence'])}",
            "title": (dc_title.group(1).strip() if dc_title else title_match.group(1).strip() if title_match else "Unknown"),
            "category": "evidence", "review_type": "extraction",
            "relevance": relevance.group(1).strip() if relevance else "",
            "source_file": filepath.name, "decision": None, "notes": ""
        })

    # Parse observations
    obs_blocks = re.split(r'### Observation \d+:', text)
    for block in obs_blocks[1:]:
        title_match = re.search(r'^\s*(.+?)$', block, re.MULTILINE)
        body_match = re.search(r'\*\*Body:\*\*\s*(.+?)(?=\n\n\*\*|\n---|\n###|\Z)', block, re.DOTALL)
        result["observations"].append({
            "id": f"obs-{len(result['observations'])}",
            "title": title_match.group(1).strip() if title_match else "Unknown",
            "category": "observation", "review_type": "extraction",
            "body": body_match.group(1).strip() if body_match else "",
            "source_file": filepath.name, "decision": None, "notes": ""
        })

    return result


def parse_batch_report(filepath: Path) -> dict:
    text = filepath.read_text()
    result = {"file": filepath.name, "concepts": [], "enrichments": [],
              "evidence": [], "observations": [], "flags": []}

    file_sections = re.split(r'## File \d+:', text)
    for section in file_sections[1:]:
        source_match = re.search(r'^\s*(.+\.md)', section, re.MULTILINE)
        source_name = source_match.group(1).strip() if source_match else "unknown"
        concepts_match = re.search(r'### New Concepts.*?\n(.+?)(?=\n###|\n---|\Z)', section, re.DOTALL)
        if concepts_match:
            items = re.findall(r'\d+\.\s*\*\*(.+?)\*\*\s*[—-]\s*(.+?)(?=\n\d+\.|\n\n|\Z)', concepts_match.group(1))
            for name, desc in items:
                slug = name.strip().lower().replace(' ', '-')
                broader_match = re.search(r'Broader:\s*(\S+)', desc)
                broader = [broader_match.group(1)] if broader_match else []
                desc_clean = re.sub(r'\s*Broader:.*$', '', desc).strip()
                result["concepts"].append({
                    "id": f"urn:srl:concept:{slug}", "title": name.strip(),
                    "category": "new-concept", "review_type": "extraction",
                    "provenance": "unclassified", "confidence": "medium",
                    "body": desc_clean, "subjects": [], "broader": broader,
                    "related": [], "source_file": filepath.name,
                    "batch_source": source_name, "decision": None, "notes": ""
                })

        enrichments_match = re.search(r'### Key Enrichments\n(.+?)(?=\n###|\n---|\Z)', section, re.DOTALL)
        if enrichments_match:
            items = re.findall(r'[-*]\s*\*\*(.+?)\*\*:\s*(.+?)(?=\n[-*]|\n\n|\Z)', enrichments_match.group(1))
            for target, addition in items:
                result["enrichments"].append({
                    "id": f"enrich-batch-{target.strip().lower()}-{len(result['enrichments'])}",
                    "target_concept": target.strip().lower(), "category": "enrichment",
                    "review_type": "extraction", "addition": addition.strip(),
                    "source_file": filepath.name, "batch_source": source_name,
                    "decision": None, "notes": ""
                })

    return result


def build_extraction_queue() -> dict:
    all_concepts, all_enrichments, all_evidence, all_observations = [], [], [], []
    if not EXTRACTIONS_DIR.exists():
        return {"concepts": all_concepts, "enrichments": all_enrichments,
                "evidence": all_evidence, "observations": all_observations}

    for md_file in sorted(EXTRACTIONS_DIR.glob("*.md")):
        parsed = parse_batch_report(md_file) if "batch" in md_file.name.lower() else parse_detailed_report(md_file)
        all_concepts.extend(parsed["concepts"])
        all_enrichments.extend(parsed["enrichments"])
        all_evidence.extend(parsed["evidence"])
        all_observations.extend(parsed["observations"])

    return {"concepts": all_concepts, "enrichments": all_enrichments,
            "evidence": all_evidence, "observations": all_observations}


# ─── Custom queue (Vigil-generated) ───

def load_custom_queue(filepath: str) -> list:
    """Load a custom review queue JSON file."""
    with open(filepath) as f:
        return json.load(f)


# ─── Main ───

def main():
    args = set(sys.argv[1:])
    if not args or "--all" in args:
        args = {"--extractions", "--clinical"}

    output = {
        "generated": datetime.now().isoformat(),
        "queue_types": [],
        "queues": {}
    }

    if "--extractions" in args:
        extraction_data = build_extraction_queue()
        output["queues"]["extractions"] = extraction_data
        output["queue_types"].append({
            "key": "extractions",
            "label": "Extraction Candidates",
            "tabs": [
                {"key": "concepts", "label": "Concepts"},
                {"key": "enrichments", "label": "Enrichments"},
                {"key": "evidence", "label": "Evidence"},
                {"key": "observations", "label": "Observations"}
            ],
            "actions": ["approve", "maybe", "reject"]
        })
        total_ext = sum(len(v) for v in extraction_data.values())
        print(f"Extractions: {total_ext} items")

    if "--clinical" in args:
        clinical_items = build_clinical_queue()
        output["queues"]["clinical"] = clinical_items
        output["queue_types"].append({
            "key": "clinical",
            "label": "Clinical Interpretations",
            "tabs": [],
            "actions": ["submit", "skip", "flag"]
        })
        print(f"Clinical interpretations: {len(clinical_items)} pending")

    if "--promotions" in args:
        promo_items = build_promotion_queue()
        output["queues"]["promotions"] = promo_items
        output["queue_types"].append({
            "key": "promotions",
            "label": "Status Promotions",
            "tabs": [],
            "actions": ["promote", "hold", "demote"]
        })
        print(f"Promotions: {len(promo_items)} pending")

    # Custom queue
    custom_files = [a for a in sys.argv[1:] if a.startswith("--custom=")]
    for cf in custom_files:
        filepath = cf.split("=", 1)[1]
        custom_data = load_custom_queue(filepath)
        key = Path(filepath).stem
        output["queues"][key] = custom_data
        output["queue_types"].append({
            "key": key,
            "label": key.replace("-", " ").title(),
            "tabs": [],
            "actions": custom_data[0].get("actions", ["approve", "reject"]) if custom_data else []
        })
        print(f"Custom ({key}): {len(custom_data)} items")

    OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    print(f"\nOutput: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
