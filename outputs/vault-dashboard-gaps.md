---
created: '2026-03-14'
creator: Randy Graybeal
dc:subject:
- dashboard
- dataview
- quality-assurance
- metadata-gaps
id: urn:srl:output:vault-dashboard-gaps
modified: '2026-03-14'
output_type: dashboard
status: draft
target_audience: internal
title: 'Vault Dashboard: Gaps, Missing Data, and Promotion Readiness'
type: output
---

# Vault Dashboard: Gaps, Missing Data, and Promotion Readiness

> This note uses [Dataview](https://github.com/blackfishZYC/obsidian-dataview) queries. Install the Dataview community plugin, then toggle to Reading View (Cmd+E) to see live tables.

---

## Empty Clinical Interpretations

Evidence notes where Randy's clinical interpretation has not been written yet. These are the highest-leverage gaps — your 28 years of expertise belongs here.

```dataview
TABLE dc_date AS "Year", dc_publisher AS "Journal", evidence_level AS "Level"
FROM "evidence"
WHERE clinical_interpretation = "" OR clinical_interpretation = null
SORT evidence_level ASC
```

---

## Missing DOIs / Identifiers

Evidence notes with no `dc:identifier` — needed for citation, cross-referencing, and academic credibility.

```dataview
TABLE dc_date AS "Year", dc_publisher AS "Publisher", dc_type AS "Type"
FROM "evidence"
WHERE !contains(file.frontmatter["dc:identifier"], "doi") AND !contains(file.frontmatter["dc:identifier"], "isbn") AND !contains(file.frontmatter["dc:identifier"], "pmid")
SORT dc_date ASC
```

---

## Notes Stuck in Draft

All notes that have never been promoted beyond draft status. Sorted by type so you can prioritize concepts first (they're the hubs everything else connects to).

```dataview
TABLE type AS "Type", file.folder AS "Folder"
FROM ""
WHERE status = "draft"
SORT type ASC, file.name ASC
```

---

## Evidence by Level (Strongest First)

The full evidence library sorted by evidence level — your strongest citations at the top.

```dataview
TABLE evidence_level AS "Level", title AS "Title", dc_date AS "Year", dc_publisher AS "Journal/Publisher"
FROM "evidence"
WHERE evidence_level != null
SORT evidence_level ASC
```

---

## Evidence Without Level Classification

Evidence notes that still need an `evidence_level` assigned.

```dataview
TABLE dc_date AS "Year", dc_publisher AS "Publisher", dc_type AS "Type"
FROM "evidence"
WHERE evidence_level = null OR evidence_level = ""
SORT dc_date ASC
```

---

## Orphaned Notes (No Incoming Links)

Notes that nothing else links to. These may be disconnected from the graph or may need to be wired in.

```dataview
TABLE type AS "Type", status AS "Status"
FROM ""
WHERE length(file.inlinks) = 0
SORT type ASC
```

---

## Concepts by Evidence Count

Which concepts have the most evidence backing them? Which ones are under-supported?

```dataview
TABLE length(file.frontmatter["prov:wasDerivedFrom"]) AS "Evidence Links", status AS "Status"
FROM "concepts"
SORT length(file.frontmatter["prov:wasDerivedFrom"]) DESC
```

---

## Recently Modified

What's been touched today or this week?

```dataview
TABLE type AS "Type", status AS "Status"
FROM ""
WHERE modified >= date("2026-03-14")
SORT modified DESC
```

---

## Quick Stats

```dataview
TABLE length(rows) AS "Count"
FROM ""
GROUP BY type
```
