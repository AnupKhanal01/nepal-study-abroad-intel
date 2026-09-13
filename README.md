# Nepal Study Abroad Intel

A knowledge-management workflow for tracking foreign-university recruitment activity aimed at
Nepalese students, sourced from the social media promotions of major Nepal-based education
consultancy agencies (AECC, AHZ, NEXT, ALFABETA, EXPERT, REALDREAM, FRANKLIN, and others),
with a priority focus on **January and April 2027 intakes**.

## Why this exists / how it works

Facebook, Instagram, and TikTok do not allow automated scraping of business pages without
official API access and page-owner permission — so this project is **not** a bot that silently
crawls agency accounts. Instead it is a lightweight **capture → structure → consolidate**
pipeline:

1. **Capture** — Whenever you (or a team member) see a relevant post from one of the tracked
   agencies, drop a quick note into `data/intake/` using the template (`_template.md`). Paste the
   post text, a screenshot reference, or a link, plus whatever fields you can read off the post.
2. **Structure** — Run `scripts/parse_intake.py`, or ask Claude Code to do it. It reads every
   unprocessed file in `data/intake/`, extracts the structured fields, appends one row per
   university/program to `data/knowledge_base.xlsx`, and moves the source file to
   `data/processed/`.
3. **Consolidate** — `data/knowledge_base.xlsx` is the single source of truth: one row per
   university/program offer, with a `status` column (`draft` / `verified`) so unverified
   agency claims are never confused with confirmed facts.

Immigration/visa rules for major destination countries (reference material, not agency claims)
live separately in `immigration_rules/`, organized by region.

## Folder structure

```
data/
  intake/            <- drop new capture notes here (one file per post/offer)
  processed/          <- capture notes already merged into the workbook
  knowledge_base.xlsx <- the master workbook (one row per university/program offer)
immigration_rules/
  europe/, asia/, australia/, north_america/
  each country file: visa route, financial/bank requirement, English requirement,
  health insurance, work rights, post-study work route, dependents, notes
scripts/
  parse_intake.py     <- turns data/intake/*.md into workbook rows
  schema.py           <- single source of truth for the field list / dropdown values
docs/
  field_schema.md     <- what every column in the workbook means
  agencies.md         <- the tracked agencies and notes on each
  workflow.md          <- day-to-day operating steps
```

## Important caveats

- **Nothing in `data/knowledge_base.xlsx` is verified fact until `status = verified`.** Agency
  social posts are marketing material; fees, deposits, and deadlines should be confirmed against
  the university's own offer letter or official page before being relied on.
- **Immigration rule figures change.** Financial thresholds, visa fees, and processing times are
  updated by governments periodically (often yearly). Every file in `immigration_rules/` carries
  a "last verified" field — treat it as a starting checklist, not a legal reference, and confirm
  current figures on the destination country's official immigration site before advising a
  student.
- This project stores no student personal data. Keep it that way — only university/program/policy
  information belongs here.

## Getting started

```bash
pip install openpyxl
python scripts/parse_intake.py   # processes anything sitting in data/intake/
```
