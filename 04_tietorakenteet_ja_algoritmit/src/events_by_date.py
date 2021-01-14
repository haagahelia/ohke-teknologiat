import urllib.request
import json

EVENTS_API_URL = 'http://open-api.myhelsinki.fi/v1/events/'


def swap(elements, i, j):
    """ Vaihtaa kahden elementin paikkaa listalla indeksien mukaan:

    >>> nimet = ['Matti', 'Teppo', 'Paula']
    >>> swap(nimet, 0, 2)
    >>> nimet
    ['Paula', 'Teppo', 'Matti']
    """
    elements[i], elements[j] = elements[j], elements[i]


def get_start_time(event):
    """ Palauttaa annetun tapahtuman aloitusajan merkkijonona, 
    tai tyhjän merkkijonon, jos tapahtumalla ei ole  aloitusaikaa.

    >>> tapahtuma = { 'event_dates': { 'starting_day': '2022-01-01T12:00:00Z' }}
    >>> get_start_time(tapahtuma)
    '2022-01-01T12:00:00Z'

    >>> tapahtuma['event_dates']['starting_day'] = None
    >>> get_start_time(tapahtuma)
    ''
    """
    return event['event_dates']['starting_day'] or ''


def get_name(event):
    """ Palauttaa annetun tapahtuman nimen suomeksi, englanniksi tai
    tyhjänä, jos kumpaakaan kieliversiota ei löydy.

    >>> tapahtuma = { 'name': { 'fi' : None, 'en': 'Christmas' }}
    >>> get_name(tapahtuma)
    'Christmas'
    >>> tapahtuma['name']['fi'] = 'Joulu'
    >>> get_name(tapahtuma)
    'Joulu'
    """
    return (event['name']['fi'] or event['name']['en'] or '').strip()


def bubble_sort(events):
    """ Järjestää annetut tapahtumat alkuajan mukaan.

    >>> joulukuu24 = { 'event_dates': { 'starting_day': '2022-12-24T12:00:00Z' }}
    >>> tammikuu1 = { 'event_dates': { 'starting_day': '2022-01-01T12:00:00Z' }}
    >>> tapahtumat = [joulukuu24, tammikuu1]
    >>> bubble_sort(tapahtumat)
    >>> tapahtumat == [tammikuu1, joulukuu24]
    True
    """

    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(events) - 1):
            if get_start_time(events[i]) > get_start_time(events[i+1]):
                swapped = True
                swap(events, i, i+1)


def get_events():
    with urllib.request.urlopen(EVENTS_API_URL) as response:
        json_response = json.load(response)
        return json_response['data']  # 'data' on lista tapahtumista


def get_sorted_events():
    all_events = get_events()
    bubble_sort(all_events)
    return all_events


def main():
    events = get_sorted_events()

    latest_date = ''

    for event in events:
        # esim. '2022-01-01T12:00:00Z' tai ''
        event_start = get_start_time(event)

        date = event_start[:10]     # '2022-01-01' tai ''
        time = event_start[11:16]   # '12:00' tai ''
        name = get_name(event)

        if date != latest_date:
            print()
            print(date)  # tulostetaan uusi päivämäärä
            latest_date = date

        print(f' { time } { name }')


if __name__ == "__main__":
    main()
