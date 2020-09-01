import urllib.request
import json
from datetime import datetime


def swap(list, first, second):
    temp = list[first]
    list[first] = list[second]
    list[second] = temp


def starting_date(e):
    return e["event_dates"]["starting_day"] or ''


def bubble_sort(items):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(items) - 1):
            if (starting_date(items[i]) > starting_date(items[i+1])):
                swapped = True
                swap(items, i, i+1)


def get_events():
    with urllib.request.urlopen('http://open-api.myhelsinki.fi/v1/events/') as response:
        return json.loads(response.read())['data']


events = get_events()

# Native sorting:
events.sort(key=lambda e: e["event_dates"]["starting_day"] or '')

# Bubble sort:
bubble_sort(events)

latest_date = ''
for event in events:
    day_str = starting_date(event)[0:10]
    if day_str != latest_date:
        print()
        print(day_str)
        latest_date = day_str

    name = (event['name']['fi'] or event['name']['en'] or '')
    print(f" { starting_date(event)[11:16] } { name.strip() }")
