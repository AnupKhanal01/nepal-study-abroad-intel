# Workbook field schema

Every row in `data/knowledge_base.xlsx` (sheet `offers`) is one university/program offer
captured from one agency post. Columns, in order:

| Column | Meaning |
|---|---|
| row_id | Auto-incrementing id assigned by `scripts/parse_intake.py`. |
| date_captured | Date the post was captured/noted (YYYY-MM-DD). |
| captured_by | Who logged it. |
| source_agency | One of: AECC, AHZ, NEXT, ALFABETA, EXPERT, REALDREAM, FRANKLIN, OTHER. |
| source_post_url_or_ref | Link to the post, or a description if no stable link exists (e.g. "IG story, AECC Kathmandu, 13 Sep"). |
| source_post_date | Date the agency actually posted it. |
| status | `draft` (unverified agency claim), `verified` (confirmed against university/official source), or `outdated` (superseded by a newer capture). |
| university_name | Name of the foreign university/institution being promoted. |
| country | Destination country. |
| region | Europe / Asia / Australia-Oceania / North America. |
| city_location | City/campus location. |
| program_name | Course/program name. |
| level | Foundation / Diploma / Bachelor / Master / PhD / Pathway. |
| intake | Target intake — prioritize "Jan 2027" and "Apr 2027". |
| academic_requirement | Minimum academic qualification (GPA/%/grade). |
| scholarship_information | Scholarship/fee-waiver availability, amount or %, and eligibility criteria mentioned in the post. |
| english_requirement | IELTS/PTE/TOEFL/Duolingo score or waiver condition. |
| interview_condition | Whether an interview (university or visa-focused) is required, and format. |
| initial_deposit | Deposit required to confirm the offer/CAS/I-20 etc. |
| application_charge | Application/processing fee charged by the university or agency. |
| process_duration | Typical time from application to offer/visa decision. |
| visa_requirement_notes | Visa route name and any notable conditions mentioned. |
| insurance_cost_estimate | Health insurance cost (e.g. UK IHS, OSHC for Australia, etc.). |
| travel_cost_estimate | Estimated flight/travel cost from Nepal. |
| cost_of_living_estimate | Estimated monthly/annual living cost at that location. |
| banking_income_requirement | Financial proof / maintenance funds / sponsor income requirement. |
| application_deadline | Deadline for the stated intake. |
| other_details | Anything else worth keeping (scholarships, conditions, promo terms). |

## Status discipline

Treat `draft` as "an agency said this in an ad." Before advising a student or publishing this
data anywhere external, cross-check deposit amounts, deadlines, and requirements against the
university's own offer/website and move the row to `verified`. If a later capture contradicts
an earlier `verified` row, mark the old row `outdated` rather than deleting it — the history is
useful.
