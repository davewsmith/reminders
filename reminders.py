from datetime import datetime
from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader


today = datetime.today()
today = datetime(today.year, today.month, today.day)
# Adjusting from UTC left as an exercise. Not an issue for
# the server I'll be running this on

jinja_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=True,
)

events = []
names = set()

for p in Path('.').iterdir():
    if p.suffix == '.dates':
        with p.open() as f:
            line_no = 0
            for line in f:
                line_no += 1
                if line == '\n' or line.startswith('#'):
                    continue
                first, rest = line.split(' ', 1)

                try:
                    dt = datetime.strptime(first, '%Y-%m-%d')
                except ValueError:
                    sys.stderr.write(f"{p}:{line_no}: {line}")
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


context = {
    'events': events,
}
print(jinja_env.get_template('index.html').render(**context))
