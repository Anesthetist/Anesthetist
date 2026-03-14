"""
Vault loader for the SRL Knowledge Graph.
Parses markdown files with YAML frontmatter into an in-memory index.
"""

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import frontmatter


@dataclass
class NoteRecord:
    id: str
    slug: str
    type: str
    title: str
    status: str
    metadata: dict
    body: str
    file_path: Path


class VaultIndex:
    """In-memory index of all structured notes in the vault."""

    INDEXED_DIRS = ["concepts", "evidence", "observations", "audiences", "outputs"]

    def __init__(self, vault_root):
        self.vault_root = Path(vault_root)
        self.notes_by_id: dict[str, NoteRecord] = {}
        self.notes_by_slug: dict[str, NoteRecord] = {}
        self.notes_by_type: dict[str, list[NoteRecord]] = {}
        self.notes_by_subject: dict[str, list[NoteRecord]] = {}
        self.notes_by_status: dict[str, list[NoteRecord]] = {}
        self._file_mtimes: dict[Path, float] = {}

    def _slug_from_urn(self, urn: str) -> str:
        """Extract slug from URN like urn:srl:concept:interoception -> interoception."""
        if urn.startswith("urn:srl:"):
            parts = urn.split(":")
            if len(parts) >= 4:
                return parts[3]
        return urn

    def _slug_from_path(self, path: Path) -> str:
        return path.stem

    def _parse_file(self, filepath: Path) -> Optional[NoteRecord]:
        try:
            post = frontmatter.load(filepath)
        except Exception:
            return None

        meta = dict(post.metadata)
        note_id = meta.get("id", "")
        slug = self._slug_from_path(filepath)
        note_type = meta.get("type", "unknown")
        title = meta.get("title", slug)
        status = meta.get("status", "draft")

        return NoteRecord(
            id=note_id,
            slug=slug,
            type=note_type,
            title=title,
            status=status,
            metadata=meta,
            body=post.content,
            file_path=filepath,
        )

    def load(self):
        """Full scan of all indexed directories."""
        self.notes_by_id.clear()
        self.notes_by_slug.clear()
        self.notes_by_type.clear()
        self.notes_by_subject.clear()
        self.notes_by_status.clear()
        self._file_mtimes.clear()

        for dir_name in self.INDEXED_DIRS:
            dir_path = self.vault_root / dir_name
            if not dir_path.exists():
                continue
            for filepath in sorted(dir_path.glob("*.md")):
                note = self._parse_file(filepath)
                if note is None:
                    continue

                self._file_mtimes[filepath] = filepath.stat().st_mtime
                self._index_note(note)

    def _index_note(self, note: NoteRecord):
        if note.id:
            self.notes_by_id[note.id] = note
        self.notes_by_slug[note.slug] = note

        self.notes_by_type.setdefault(note.type, [])
        if note not in self.notes_by_type[note.type]:
            self.notes_by_type[note.type].append(note)

        self.notes_by_status.setdefault(note.status, [])
        if note not in self.notes_by_status[note.status]:
            self.notes_by_status[note.status].append(note)

        subjects = note.metadata.get("dc:subject", []) or []
        for subj in subjects:
            self.notes_by_subject.setdefault(subj, [])
            if note not in self.notes_by_subject[subj]:
                self.notes_by_subject[subj].append(note)

    def refresh_if_needed(self):
        """Re-parse any files that changed since last load, and pick up new files."""
        changed = False

        # Check for new or modified files
        for dir_name in self.INDEXED_DIRS:
            dir_path = self.vault_root / dir_name
            if not dir_path.exists():
                continue
            for filepath in sorted(dir_path.glob("*.md")):
                mtime = filepath.stat().st_mtime
                if filepath not in self._file_mtimes or self._file_mtimes[filepath] < mtime:
                    changed = True
                    note = self._parse_file(filepath)
                    if note:
                        self._file_mtimes[filepath] = mtime
                        # Remove old version if exists
                        old = self.notes_by_slug.get(note.slug)
                        if old:
                            self._remove_note(old)
                        self._index_note(note)

        # Check for deleted files
        for filepath in list(self._file_mtimes.keys()):
            if not filepath.exists():
                changed = True
                slug = self._slug_from_path(filepath)
                old = self.notes_by_slug.get(slug)
                if old:
                    self._remove_note(old)
                del self._file_mtimes[filepath]

    def _remove_note(self, note: NoteRecord):
        self.notes_by_id.pop(note.id, None)
        self.notes_by_slug.pop(note.slug, None)
        for lst in self.notes_by_type.values():
            if note in lst:
                lst.remove(note)
        for lst in self.notes_by_status.values():
            if note in lst:
                lst.remove(note)
        for lst in self.notes_by_subject.values():
            if note in lst:
                lst.remove(note)

    def get_note(self, slug_or_id: str) -> Optional[NoteRecord]:
        """Look up a note by slug or full URN."""
        if slug_or_id in self.notes_by_slug:
            return self.notes_by_slug[slug_or_id]
        if slug_or_id in self.notes_by_id:
            return self.notes_by_id[slug_or_id]
        # Try extracting slug from URN
        slug = self._slug_from_urn(slug_or_id)
        return self.notes_by_slug.get(slug)

    def get_by_type(self, note_type: str) -> list[NoteRecord]:
        return self.notes_by_type.get(note_type, [])

    def get_by_subject(self, subject: str) -> list[NoteRecord]:
        return self.notes_by_subject.get(subject, [])

    def get_by_status(self, status: str) -> list[NoteRecord]:
        return self.notes_by_status.get(status, [])

    def get_evidence_chain(self, slug_or_id: str, max_depth: int = 3) -> list[NoteRecord]:
        """Resolve prov:wasDerivedFrom recursively up to max_depth."""
        start = self.get_note(slug_or_id)
        if not start:
            return []

        result = []
        visited = set()
        queue = [(start, 0)]

        while queue:
            note, depth = queue.pop(0)
            if depth > 0:
                result.append(note)
            if depth >= max_depth:
                continue

            derived_from = note.metadata.get("prov:wasDerivedFrom", []) or []
            for ref in derived_from:
                ref_slug = self._slug_from_urn(ref)
                if ref_slug in visited:
                    continue
                visited.add(ref_slug)
                ref_note = self.get_note(ref_slug)
                if ref_note:
                    queue.append((ref_note, depth + 1))

        return result

    def get_relationships(self, slug_or_id: str) -> dict:
        """Return SKOS broader/narrower/related with resolved titles."""
        note = self.get_note(slug_or_id)
        if not note:
            return {"broader": [], "narrower": [], "related": []}

        result = {}
        for rel_type in ["skos:broader", "skos:narrower", "skos:related"]:
            refs = note.metadata.get(rel_type, []) or []
            resolved = []
            for ref in refs:
                ref_slug = self._slug_from_urn(ref)
                ref_note = self.get_note(ref_slug)
                if ref_note:
                    resolved.append({"slug": ref_note.slug, "title": ref_note.title, "id": ref_note.id})
                else:
                    resolved.append({"slug": ref_slug, "title": ref_slug, "id": ref})
            key = rel_type.split(":")[1]
            result[key] = resolved

        return result

    def get_audience_concepts(self, audience_slug: str) -> list[NoteRecord]:
        """Extract [[wikilinks]] from an audience note body and resolve them."""
        note = self.get_note(audience_slug)
        if not note:
            return []

        wikilinks = re.findall(r"\[\[([^\]]+)\]\]", note.body)
        concepts = []
        seen = set()
        for link in wikilinks:
            slug = link.strip().lower()
            if slug in seen:
                continue
            seen.add(slug)
            linked = self.get_note(slug)
            if linked and linked.type == "concept":
                concepts.append(linked)

        return concepts

    def search(self, query: str) -> list[NoteRecord]:
        """Simple substring search across title, body, and subjects."""
        query_lower = query.lower()
        results = []
        for note in self.notes_by_slug.values():
            if query_lower in note.title.lower():
                results.append(note)
                continue
            if query_lower in note.body.lower():
                results.append(note)
                continue
            subjects = note.metadata.get("dc:subject", []) or []
            if any(query_lower in s.lower() for s in subjects):
                results.append(note)
        return results

    # ── Write operations ──────────────────────────────────────────────

    def _type_to_dir(self, note_type: str) -> str:
        mapping = {
            "concept": "concepts",
            "evidence": "evidence",
            "observation": "observations",
            "audience": "audiences",
            "output": "outputs",
        }
        return mapping.get(note_type, note_type)

    def create_note(self, note_type: str, slug: str, frontmatter_dict: dict, body: str) -> Path:
        """Create a new note file and add it to the index."""
        dir_name = self._type_to_dir(note_type)
        dir_path = self.vault_root / dir_name
        dir_path.mkdir(exist_ok=True)

        filepath = dir_path / f"{slug}.md"
        if filepath.exists():
            raise FileExistsError(f"Note already exists: {filepath}")

        self._write_note_file(filepath, frontmatter_dict, body)

        note = self._parse_file(filepath)
        if note:
            self._file_mtimes[filepath] = filepath.stat().st_mtime
            self._index_note(note)

        return filepath

    def update_note(self, slug_or_id: str, frontmatter_updates: dict = None, body: str = None) -> Optional[Path]:
        """Update an existing note's frontmatter and/or body."""
        note = self.get_note(slug_or_id)
        if not note:
            return None

        filepath = note.file_path
        post = frontmatter.load(filepath)

        if frontmatter_updates:
            for k, v in frontmatter_updates.items():
                post.metadata[k] = v

        if body is not None:
            post.content = body

        self._write_note_file(filepath, dict(post.metadata), post.content)

        # Re-index
        self._remove_note(note)
        new_note = self._parse_file(filepath)
        if new_note:
            self._file_mtimes[filepath] = filepath.stat().st_mtime
            self._index_note(new_note)

        return filepath

    def promote_status(self, slug_or_id: str, new_status: str) -> Optional[Path]:
        """Change a note's status (draft -> review -> canonical)."""
        valid = ["draft", "review", "canonical"]
        if new_status not in valid:
            raise ValueError(f"Invalid status '{new_status}'. Must be one of: {valid}")
        return self.update_note(slug_or_id, {"status": new_status})

    def add_evidence_link(self, concept_slug: str, evidence_urn: str) -> Optional[Path]:
        """Add an evidence URN to a concept's prov:wasDerivedFrom list."""
        note = self.get_note(concept_slug)
        if not note:
            return None
        derived = note.metadata.get("prov:wasDerivedFrom", []) or []
        if evidence_urn not in derived:
            derived.append(evidence_urn)
        return self.update_note(concept_slug, {"prov:wasDerivedFrom": derived})

    def add_skos_relation(self, slug: str, relation_type: str, target_slug: str) -> Optional[Path]:
        """Add a SKOS relationship (broader, narrower, related) to a concept."""
        valid_rels = ["skos:broader", "skos:narrower", "skos:related"]
        if relation_type not in valid_rels:
            raise ValueError(f"Invalid relation '{relation_type}'. Must be one of: {valid_rels}")
        note = self.get_note(slug)
        if not note:
            return None
        rels = note.metadata.get(relation_type, []) or []
        if target_slug not in rels:
            rels.append(target_slug)
        return self.update_note(slug, {relation_type: rels})

    def _write_note_file(self, filepath: Path, metadata: dict, body: str):
        """Write a note file with YAML frontmatter."""
        post = frontmatter.Post(body, **metadata)
        with open(filepath, "w") as f:
            f.write(frontmatter.dumps(post))
            f.write("\n")
