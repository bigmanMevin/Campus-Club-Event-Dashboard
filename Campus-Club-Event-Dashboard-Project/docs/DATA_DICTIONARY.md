# Data dictionary and metric definitions

Source: synthetic records generated for this portfolio project. No actual institution or student data. Period: January–June 2026. Grain: one row per completed event.

| Column | Type | Meaning |
|---|---|---|
| Event_ID | Text | Unique event key |
| Event_Name | Text | Fictional event name |
| Club | Text | Hosting club, not student membership |
| Category | Text | Performance, Workshop, Competition, Social or Volunteering |
| Event_Date | Date | Event date, ISO format in CSV |
| Registrations | Whole number | Registered participants |
| Attendees | Whole number | Registered participants who attended |
| Budget_AED | Whole number | Planned event spending in AED |
| Actual_Cost_AED | Whole number | Actual event spending in AED |
| Feedback_Responses | Whole number | Attendees submitting one rating each |
| Feedback_Points | Whole number | Sum of respondent ratings, each between 1 and 5 |

## Cleaning rules
1. Preserve the raw CSV.
2. Trim whitespace from Club.
3. Trim Category and standardize title case.
4. Remove the exact repeated row identified by Event_ID. Conflicting duplicates in other data require investigation.
5. Convert six numeric columns to whole numbers and Event_Date to a date.

Original input: 37 records. Clean result: 36. Three club names contained extra spaces, three category names were lowercase, and EVT008 was duplicated.

## Metrics
| Metric | Calculation | Meaning |
|---|---|---|
| Total Events | Distinct count of Event_ID | Completed events in filter context |
| Active Clubs | Distinct count of Club | Hosting clubs in filter context |
| Total Registrations | Sum of Registrations | Event registrations, not unique students |
| Total Attendance | Sum of Attendees | Event visits, not unique students |
| Attendance Rate | Total Attendance / Total Registrations | Registration-to-attendance conversion |
| Total Budget | Sum of Budget_AED | Planned spending |
| Total Spend | Sum of Actual_Cost_AED | Actual spending |
| Budget Remaining | Total Budget − Total Spend | Negative indicates overspending |
| Feedback Responses | Sum of Feedback_Responses | Submitted ratings |
| Average Feedback | Sum of Feedback_Points / Feedback Responses | Response-weighted rating out of 5 |
| Feedback Response Rate | Feedback Responses / Total Attendance | Share of attendances with a response |
| Cost per Attendance | Total Spend / Total Attendance | AED per event visit |

Ratios with a zero denominator return blank in DAX and a dash in the browser. Do not sum or simply average individual event rates. The same filter context must apply to numerator and denominator.

## Assumptions
All attendees registered. No walk-ins. No more than one rating per respondent per event. Counts are nonnegative and responses <= attendees <= registrations. Rating points are between 1 and 5 times responses. Real-world outcomes cannot be inferred from synthetic data.
