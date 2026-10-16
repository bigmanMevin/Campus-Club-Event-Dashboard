# Connect the Power BI report to Excel
The shipped model embeds the original CSV and cleans it in Power Query. To use your edited workbook instead:

1. Open the Power BI project.
2. Home > Transform data. Select Events.
3. Open Advanced Editor.
4. Replace the query with the following, changing the path to your downloaded workbook.
5. Close & Apply, then save.

```powerquery
let
    Source = Excel.Workbook(File.Contents("C:\Users\YOUR_NAME\Documents\campus-club-event-dashboard\data\campus_events_clean.xlsx"), null, true),
    Events = Source{[Item="Events", Kind="Table"]}[Data],
    Typed = Table.TransformColumnTypes(Events, {
        {"Event_ID", type text}, {"Event_Name", type text},
        {"Club", type text}, {"Category", type text},
        {"Event_Date", type date}, {"Registrations", Int64.Type},
        {"Attendees", Int64.Type}, {"Budget_AED", Int64.Type},
        {"Actual_Cost_AED", Int64.Type}, {"Feedback_Responses", Int64.Type},
        {"Feedback_Points", Int64.Type}
    })
in
    Typed
```

Keep the table and column names unchanged so the measures and visuals continue to resolve. Refresh after editing and saving Excel.

