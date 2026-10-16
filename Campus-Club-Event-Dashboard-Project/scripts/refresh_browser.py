"""Rebuild clean CSV, JSON and embedded browser data from the raw CSV.
Uses Python standard library only. Does not modify Excel or Power BI source.
"""
from pathlib import Path
import csv, json, re
root=Path(__file__).resolve().parents[1]
with (root/'data/campus_events_raw.csv').open(newline='') as f:
    source=list(csv.DictReader(f))
rows=[]; seen=set()
for item in source:
    r=item.copy()
    if r['Event_ID'] in seen:
        continue
    seen.add(r['Event_ID'])
    r['Club']=r['Club'].strip()
    r['Category']=r['Category'].strip().title()
    for key in list(r)[5:]:
        r[key]=int(r[key])
    assert 0<=r['Feedback_Responses']<=r['Attendees']<=r['Registrations']
    assert r['Feedback_Responses']<=r['Feedback_Points']<=5*r['Feedback_Responses']
    rows.append(r)
assert rows, 'No data rows'
(root/'data/events.json').write_text(json.dumps(rows,indent=2))
with (root/'data/campus_events_clean_reference.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
page=root/'index.html'
html=page.read_text()
payload=json.dumps(rows).replace('<','\\u003c')
html,n=re.subn(r'const DATA=.*?;\nconst \$=',lambda _: 'const DATA='+payload+';\nconst $=',html,count=1,flags=re.S)
assert n==1,'Embedded dataset not found'
page.write_text(html)
print(f'Updated browser data: {len(source)} raw rows to {len(rows)} clean events.')
