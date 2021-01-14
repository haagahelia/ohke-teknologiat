import json


def load_events():
    with open('events.json') as file:
        json_str = file.read()
        return json.loads(json_str)


e = load_events()
events = e['data']

print(len(events))

# tapahtumien haku listalta
e1 = events[0]
e2 = events[1]

# aloitusaikojen hakeminen:
d1 = e1['event_dates']['starting_day']
d2 = e2['event_dates']['starting_day']

# debug:
print(d1, d2)

# vertailu:
print(d1 < d2)
