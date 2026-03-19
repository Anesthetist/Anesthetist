#!/usr/bin/env python3
"""Parse extraction report markdown files into structured JSON for the review GUI."""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

EXTRACTIONS_DIR = Path(__file__).parent.parent / "outputs" / "extractions"
OUTPUT_FILE = Path(__file__).parent / "review-data.json"

# Provenance inference keywords
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
    if "very high" in lower or "extraction confidence: high" in lower or "confidence: high" in lower or "confidence:** high" in lower:
        return "high"
    if "confidence: medium" in lower or "confidence:** medium" in lower:
        return "medium"
    if "confidence: low" in lower or "confidence:** low" in lower or "likely skip" in lower:
        return "low"
    return "medium"


def parse_detailed_report(filepath: Path) -> dict:
    """Parse a detailed extraction report (3 verification batch files)."""
    text = filepath.read_text()
    result = {
        "file": filepath.name,
        "concepts": [],
        "enrichments": [],
        "evidence": [],
        "observations": [],
        "flags": []
    }

    # Extract header metadata
    source_match = re.search(r'\*\*Source:\*\*\s*(.+)', text)
    date_match = re.search(r'\*\*Date processed:\*\*\s*(.+)', text)
    source_date_match = re.search(r'\*\*Source date:\*\*\s*(.+)', text)
    summary_match = re.search(r'## Summary\n\n(.+?)(?=\n##)', text, re.DOTALL)

    result["source"] = source_match.group(1).strip() if source_match else ""
    result["date_processed"] = date_match.group(1).strip() if date_match else ""
    result["source_date"] = source_date_match.group(1).strip() if source_date_match else ""
    result["summary"] = summary_match.group(1).strip() if summary_match else ""

    # Parse concept candidates
    concept_blocks = re.split(r'### Candidate \d+:', text)
    for block in concept_blocks[1:]:  # Skip first split (before first candidate)
        title_match = re.search(r'^\s*(.+?)$', block, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown"

        # Extract YAML id
        id_match = re.search(r'id:\s*(urn:srl:\S+)', block)
        concept_id = id_match.group(1) if id_match else f"urn:srl:concept:{title.lower().replace(' ', '-')}"

        # Extract body
        body_match = re.search(r'\*\*Body:\*\*\s*(.+?)(?=\n\n\*\*|\n---|\Z)', block, re.DOTALL)
        body = body_match.group(1).strip() if body_match else ""

        # Extract Randy's voice
        voice_match = re.search(r"\*\*Randy's voice.*?\*\*\s*(.+?)(?=\n\n\*\*|\n---|\Z)", block, re.DOTALL)
        randy_voice = voice_match.group(1).strip() if voice_match else ""

        # Extract confidence line
        conf_match = re.search(r'\*\*Extraction confidence:\*\*\s*(.+?)(?=\n|\Z)', block)
        conf_text = conf_match.group(1).strip() if conf_match else ""

        # Extract subjects from YAML
        subjects_match = re.search(r'dc:subject:\s*\[(.+?)\]', block)
        subjects = [s.strip().strip('"').strip("'") for s in subjects_match.group(1).split(",")] if subjects_match else []

        # Extract SKOS relationships
        broader_match = re.search(r'skos:broader:\s*\[(.+?)\]', block)
        related_match = re.search(r'skos:related:\s*\[(.+?)\]', block)
        broader = [s.strip().strip('"').strip("'") for s in broader_match.group(1).split(",")] if broader_match else []
        related = [s.strip().strip('"').strip("'") for s in related_match.group(1).split(",")] if related_match else []

        full_text = block + " " + conf_text + " " + randy_voice
        provenance = infer_provenance(full_text)
        confidence = infer_confidence(full_text)

        result["concepts"].append({
            "id": concept_id,
            "title": title,
            "category": "new-concept",
            "provenance": provenance,
            "confidence": confidence,
            "body": body,
            "randy_voice": randy_voice,
            "confidence_note": conf_text,
            "subjects": subjects,
            "broader": broader,
            "related": related,
            "source_file": filepath.name,
            "decision": None,
            "notes": ""
        })

    # Parse enrichment candidates
    enrichment_blocks = re.split(r'### Enrichment \d+:', text)
    for block in enrichment_blocks[1:]:
        title_match = re.search(r'^\s*(\S+)', block, re.MULTILINE)
        target = title_match.group(1).strip() if title_match else "unknown"

        addition_match = re.search(r'\*\*Addition.*?\*\*\s*(.+?)(?=\n\n\*\*|\n###|\n---|\n## |\Z)', block, re.DOTALL)
        addition = addition_match.group(1).strip() if addition_match else block.strip()[:500]

        status_match = re.search(r'\*\*Status:\*\*\s*(.+?)(?=\n|\Z)', block)
        status = status_match.group(1).strip() if status_match else ""

        voice_match = re.search(r"\*\*Randy's voice.*?\*\*\s*(.+?)(?=\n\n\*\*|\n---|\Z)", block, re.DOTALL)
        randy_voice = voice_match.group(1).strip() if voice_match else ""

        result["enrichments"].append({
            "id": f"enrich-{target}-{len(result['enrichments'])}",
            "target_concept": target,
            "category": "enrichment",
            "addition": addition,
            "status": status,
            "randy_voice": randy_voice,
            "source_file": filepath.name,
            "decision": None,
            "notes": ""
        })

    # Parse evidence candidates
    evidence_blocks = re.split(r'### Evidence \d+:', text)
    for block in evidence_blocks[1:]:
        title_match = re.search(r'^\s*(.+?)$', block, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown"

        dc_title_match = re.search(r'\*\*Title:\*\*\s*(.+)', block)
        dc_creator_match = re.search(r'\*\*dc:creator:\*\*\s*(.+)', block)
        dc_date_match = re.search(r'\*\*dc:date:\*\*\s*(.+)', block)
        dc_type_match = re.search(r'\*\*dc:type:\*\*\s*(.+)', block)
        dc_id_match = re.search(r'\*\*dc:identifier:\*\*\s*(.+)', block)
        relevance_match = re.search(r'\*\*Relevance:\*\*\s*(.+)', block)
        status_match = re.search(r'\*\*Status:\*\*\s*(.+)', block)

        result["evidence"].append({
            "id": f"evidence-{len(result['evidence'])}",
            "title": (dc_title_match.group(1).strip() if dc_title_match else title),
            "category": "evidence",
            "creator": dc_creator_match.group(1).strip() if dc_creator_match else "",
            "date": dc_date_match.group(1).strip() if dc_date_match else "",
            "type": dc_type_match.group(1).strip() if dc_type_match else "",
            "identifier": dc_id_match.group(1).strip() if dc_id_match else "",
            "relevance": relevance_match.group(1).strip() if relevance_match else "",
            "status": status_match.group(1).strip() if status_match else "",
            "source_file": filepath.name,
            "decision": None,
            "notes": ""
        })

    # Parse observation candidates
    obs_blocks = re.split(r'### Observation \d+:', text)
    for block in obs_blocks[1:]:
        title_match = re.search(r'^\s*(.+?)$', block, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown"

        id_match = re.search(r'id:\s*(urn:srl:\S+)', block)
        obs_id = id_match.group(1) if id_match else f"urn:srl:observation:{title.lower().replace(' ', '-')[:40]}"

        body_match = re.search(r'\*\*Body:\*\*\s*(.+?)(?=\n\n\*\*|\n---|\n###|\Z)', block, re.DOTALL)
        body = body_match.group(1).strip() if body_match else ""

        voice_match = re.search(r"\*\*Randy's voice.*?\*\*\s*(.+?)(?=\n\n\*\*|\n---|\n###|\Z)", block, re.DOTALL)
        randy_voice = voice_match.group(1).strip() if voice_match else ""

        result["observations"].append({
            "id": obs_id,
            "title": title,
            "category": "observation",
            "body": body,
            "randy_voice": randy_voice,
            "source_file": filepath.name,
            "decision": None,
            "notes": ""
        })

    # Parse flags
    flags_match = re.search(r'## Flagged for Review\n\n(.+?)(?=\n## |\Z)', text, re.DOTALL)
    if flags_match:
        flag_lines = re.findall(r'\d+\.\s*\*\*(.+?)\*\*\s*[-—]\s*(.+?)(?=\n\d+\.|\Z)', flags_match.group(1), re.DOTALL)
        for item, description in flag_lines:
            result["flags"].append({
                "item": item.strip(),
                "description": description.strip(),
                "source_file": filepath.name
            })

    return result


def parse_batch_report(filepath: Path) -> dict:
    """Parse the batch extraction report (compressed format)."""
    text = filepath.read_text()
    result = {
        "file": filepath.name,
        "concepts": [],
        "enrichments": [],
        "evidence": [],
        "observations": [],
        "flags": []
    }

    # Split by file sections
    file_sections = re.split(r'## File \d+:', text)

    for section in file_sections[1:]:
        source_match = re.search(r'^\s*(.+\.md)', section, re.MULTILINE)
        source_name = source_match.group(1).strip() if source_match else "unknown"

        # Parse new concepts (numbered bold items)
        concepts_match = re.search(r'### New Concepts.*?\n(.+?)(?=\n###|\n---|\Z)', section, re.DOTALL)
        if concepts_match:
            items = re.findall(r'\d+\.\s*\*\*(.+?)\*\*\s*[—-]\s*(.+?)(?=\n\d+\.|\n\n|\Z)', concepts_match.group(1))
            for name, desc in items:
                slug = name.strip().lower().replace(' ', '-')
                broader_match = re.search(r'Broader:\s*(\S+)', desc)
                broader = [broader_match.group(1)] if broader_match else []
                desc_clean = re.sub(r'\s*Broader:.*$', '', desc).strip()

                # Check for flags
                flag_match = re.search(r'FLAG:\s*(.+)', desc)

                result["concepts"].append({
                    "id": f"urn:srl:concept:{slug}",
                    "title": name.strip(),
                    "category": "new-concept",
                    "provenance": "unclassified",
                    "confidence": "medium",
                    "body": desc_clean,
                    "randy_voice": "",
                    "confidence_note": "",
                    "subjects": [],
                    "broader": broader,
                    "related": [],
                    "source_file": filepath.name,
                    "batch_source": source_name,
                    "decision": None,
                    "notes": ""
                })

        # Parse enrichments
        enrichments_match = re.search(r'### Key Enrichments\n(.+?)(?=\n###|\n---|\Z)', section, re.DOTALL)
        if enrichments_match:
            items = re.findall(r'[-*]\s*\*\*(.+?)\*\*:\s*(.+?)(?=\n[-*]|\n\n|\Z)', enrichments_match.group(1))
            for target, addition in items:
                result["enrichments"].append({
                    "id": f"enrich-batch-{target.strip().lower()}-{len(result['enrichments'])}",
                    "target_concept": target.strip().lower(),
                    "category": "enrichment",
                    "addition": addition.strip(),
                    "status": "",
                    "randy_voice": "",
                    "source_file": filepath.name,
                    "batch_source": source_name,
                    "decision": None,
                    "notes": ""
                })

    return result


def main():
    reports = []
    all_concepts = []
    all_enrichments = []
    all_evidence = []
    all_observations = []
    all_flags = []

    for md_file in sorted(EXTRACTIONS_DIR.glob("*.md")):
        if "batch" in md_file.name.lower():
            parsed = parse_batch_report(md_file)
        else:
            parsed = parse_detailed_report(md_file)

        reports.append({
            "file": parsed["file"],
            "source": parsed.get("source", ""),
            "date_processed": parsed.get("date_processed", ""),
            "source_date": parsed.get("source_date", ""),
            "summary": parsed.get("summary", "")
        })

        all_concepts.extend(parsed["concepts"])
        all_enrichments.extend(parsed["enrichments"])
        all_evidence.extend(parsed["evidence"])
        all_observations.extend(parsed["observations"])
        all_flags.extend(parsed["flags"])

    output = {
        "generated": datetime.now().isoformat(),
        "sources": reports,
        "candidates": {
            "concepts": all_concepts,
            "enrichments": all_enrichments,
            "evidence": all_evidence,
            "observations": all_observations
        },
        "flags": all_flags,
        "stats": {
            "total_concepts": len(all_concepts),
            "total_enrichments": len(all_enrichments),
            "total_evidence": len(all_evidence),
            "total_observations": len(all_observations),
            "total_flags": len(all_flags)
        }
    }

    OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    print(f"Extracted {len(all_concepts)} concepts, {len(all_enrichments)} enrichments, "
          f"{len(all_evidence)} evidence, {len(all_observations)} observations, "
          f"{len(all_flags)} flags")
    print(f"Output: {OUTPUT_FILE}")

    # Also embed into HTML if --embed flag
    if "--embed" in sys.argv:
        gui_path = Path(__file__).parent / "review-gui.html"
        if gui_path.exists():
            html = gui_path.read_text()
            embedded = html.replace(
                'const REVIEW_DATA = null;',
                f'const REVIEW_DATA = {json.dumps(output)};'
            )
            out_path = Path(__file__).parent / f"review-gui-{datetime.now().strftime('%Y-%m-%d')}.html"
            out_path.write_text(embedded)
            print(f"Embedded GUI: {out_path}")


if __name__ == "__main__":
    main()
