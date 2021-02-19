import urllib.request
import json


def fetch_events():
    with urllib.request.urlopen('https://open-api.myhelsinki.fi/v1/events/') as response:
        data = response.read()

    events = json.loads(data)
    return events['data']
