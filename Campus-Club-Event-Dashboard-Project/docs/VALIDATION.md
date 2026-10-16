# Validation record

## Completed checks
- 37 raw records cleaned to 36 unique event records. Six clubs and five categories.
- All source rows satisfy responses <= attendances <= registrations and rating point bounds.
- Exported Excel workbook contains 36 populated data rows in Events, with the expected numerical totals. Clean and raw sheet previews were visually inspected.
- All Power BI visual field references resolve to a supplied column or measure.
- 24 report/project definition documents validated against Microsoft's published JSON schemas, including visual configuration and semantic-query references. This covers PBIR and definition property JSON, not execution of the tabular model.
- Browser JavaScript logic tested using a lightweight DOM stand-in: all-data totals, Music Club (6 events), Workshop (12 events), date filtering, no-result state, sorting and resetting.
- Static analytical PNG preview generated from the clean dataset and visually inspected.

## Expected unfiltered outputs
36 events; 3,517 registrations; 2,628 attendances; 74.7% attendance rate; AED 44,700 planned; AED 44,079 spent; AED 621 remaining; 1,861 feedback responses; 4.10/5 average feedback.

## Validation limits
Power BI Desktop is not available in the creation environment. The project has not been opened, refreshed, rendered or saved as .pbix in Desktop. DAX and Power Query M execution have not been tested in their native engines. JSON schema validation cannot establish native application behavior.

The browser companion's logic was tested, but a real-browser visual/interaction test was unavailable. The preview PNG is an independently generated static analytical view, not a Power BI or browser screenshot.

## Recheck locally
1. Extract the complete folder and open index.html in a browser. Confirm totals and filter behavior.
2. Open powerbi/Campus.pbip in Power BI Desktop, refresh, and compare the metrics above.
3. Confirm both pages render, slicers filter their page and ratings use a meaningful axis.
4. Save and reopen in Desktop. Replace the preview with a native screenshot if desired.
5. Optional: with Node.js installed, run `node scripts/verify_dashboard.mjs` from the repository root to repeat the browser logic checks.

The project uses generated sample data and AI-assisted source authoring. Validation status should remain accurate when sharing it.
