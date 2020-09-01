import urllib.request
import json
from datetime import datetime


def get_places():
    with urllib.request.urlopen('http://open-api.myhelsinki.fi/v1/places/') as response:
        return json.loads(response.read())['data']


places = get_places()


def is_currently_open(place):
    if 'opening_hours' not in place or 'hours' not in place['opening_hours'] or not place['opening_hours']['hours']:
        return False

    time = datetime.now()

    today = place['opening_hours']['hours'][time.weekday()]
    if today['open24h']:
        return True

    if today['opens'] and today['closes']:
        if today['opens'] <= str(time.time()) <= today['closes']:
            return True
    return False


def name(place):
    return place['name']['fi'] or place['name']['en']


for place in places:
    if is_currently_open(place):
        print(name(place))
