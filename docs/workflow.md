# Day-to-day workflow

1. **See a post** from a tracked agency (AECC, AHZ, NEXT, ALFABETA, EXPERT, REALDREAM, FRANKLIN,
   ...) promoting a university/program relevant to the Jan 2027 or Apr 2027 intake.
2. **Copy `data/intake/_template.md`** into a new file named
   `YYYY-MM-DD_agency_university-shortname.md`, e.g. `2026-09-20_aecc_ulster.md`.
3. **Fill in every field you can read off the post.** Leave the rest blank — never guess a
   number. Paste the raw post text (or describe the screenshot) under the
   `--- RAW POST CONTENT ---` divider.
4. **One file per university/program.** A single carousel post advertising 4 universities becomes
   4 intake files.
5. **Run the parser**: `python scripts/parse_intake.py` (or ask Claude Code to run it). This
   appends rows to `data/knowledge_base.xlsx` and archives the source file into
   `data/processed/`.
6. **Open `knowledge_base.xlsx`**, sort/filter as needed (by region, intake, deadline, status).
   New rows always land as `status = draft`.
7. **Verify before relying on it.** When you (or someone) confirms a row's figures against the
   university's own materials, edit its `status` cell to `verified`.
8. **Immigration rules** live in `immigration_rules/<region>/<country>.md` — these are reference
   checklists, not agency claims. Update them when a destination country changes a visa/financial
   rule, and bump the `last_verified` date at the top of the file.

## Weekly review

A short weekly pass is enough to keep this useful:
- Skim `data/knowledge_base.xlsx` for rows still `draft` older than ~2 weeks — verify or drop.
- Skim deadlines coming up in the next 4–6 weeks for the Jan/Apr 2027 intakes and flag them.
- Spot-check one `immigration_rules` file per region for anything you've heard has changed.
