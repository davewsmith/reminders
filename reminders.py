from collections import defaultdict
from datetime import datetime
from pathlib import Path


today = datetime.today()
today = datetime(today.year, today.month, today.day)
# Adjusting from UTC left as an exercise. Not an issue for
# the server I'll be running this on

events = []
names = set()

for p in Path('.').iterdir():
    if p.suffix == '.dates':
        with p.open() as f:
            for line in f:
                if line == '\n' or line.startswith('#'):
                    continue
                first, rest = line.split(' ', 1)

                try:
                    dt = datetime.strptime(first, '%Y-%m-%d')
                except ValueError:
                    # TODO consider something other than silent discards
                    continue

                if dt < today:
                    continue

                name = rest.strip()
                if name in names:
                    continue
                names.add(name)

                events.append({
                   'dt': dt,
                   'days': (dt - today).days,
                   'name': name,
                })

events = sorted(events, key=lambda e: e['dt'])

for event in events:
    print(event['dt'], event['days'], event['name'])
