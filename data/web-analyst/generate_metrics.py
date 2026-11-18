"""Rebuild the fictional Happy Masks store's classroom metrics (no real customers)."""
from pathlib import Path
import csv
import random

rng = random.Random(2026)
rows = []
for month in (9, 10):
    for day in range(1, 29):
        for channel, base in [('organic', 350), ('paid', 250), ('email', 120), ('direct', 180)]:
            for device in ('desktop', 'mobile'):
                sessions = round(base * (1.4 if device == 'mobile' else 1) * rng.uniform(.85, 1.15))
                if month == 10 and channel == 'paid':
                    sessions = round(sessions * 1.15)
                rate = {'organic': .045, 'paid': .025, 'email': .07, 'direct': .05}[channel]
                if device == 'mobile':
                    rate *= .8
                    if month == 10:
                        rate *= .45
                orders = round(sessions * rate * rng.uniform(.92, 1.08))
                revenue = round(orders * rng.uniform(29, 33), 2)
                rows.append({'date': f'2026-{month:02d}-{day:02d}', 'channel': channel,
                             'device': device, 'sessions': sessions, 'orders': orders,
                             'revenue': revenue})
path = Path(__file__).with_name('daily_metrics.csv')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(f'Wrote {len(rows)} fictional daily segment rows.')
