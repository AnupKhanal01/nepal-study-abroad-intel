"""Single source of truth for the knowledge_base.xlsx column layout and dropdown values.

Import this from parse_intake.py (and any future tooling) instead of redefining the
field list elsewhere.
"""

AGENCIES = [
    "AECC",
    "AHZ",
    "NEXT",
    "ALFABETA",
    "EXPERT",
    "REALDREAM",
    "FRANKLIN",
    "OTHER",
]

REGIONS = ["Europe", "Asia", "Australia/Oceania", "North America"]

INTAKES = [
    "Jan 2027",
    "Apr 2027",
    "Sep 2027",
    "Jan 2028",
    "Other",
]

STATUS_VALUES = ["draft", "verified", "outdated"]

LEVELS = [
    "Foundation",
    "Diploma",
    "Bachelor",
    "Master",
    "PhD",
    "Pathway/Bridging",
]

# Column order for knowledge_base.xlsx. Keep this list and docs/field_schema.md in sync.
COLUMNS = [
    "row_id",
    "date_captured",
    "captured_by",
    "source_agency",
    "source_post_url_or_ref",
    "source_post_date",
    "status",
    "university_name",
    "country",
    "region",
    "city_location",
    "program_name",
    "level",
    "intake",
    "academic_requirement",
    "english_requirement",
    "interview_condition",
    "initial_deposit",
    "application_charge",
    "process_duration",
    "visa_requirement_notes",
    "insurance_cost_estimate",
    "travel_cost_estimate",
    "cost_of_living_estimate",
    "banking_income_requirement",
    "application_deadline",
    "other_details",
]
