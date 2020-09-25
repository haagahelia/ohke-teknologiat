from events_by_date import swap, bubble_sort, str_to_datetime, get_sorted_events
from datetime import datetime, date, time

UNKNOWN_EVENT = {
    "name": {
        "fi": None,
        "en": "Event with no date"
    },
    "event_dates": {
        "starting_day": None
    }
}

JANUARY_1ST_EVENT = {
    "name": {
        "fi": None,
        "en": "January first"
    },
    "event_dates": {
        "starting_day": '2022-01-01T12:00:00Z'
    }
}

CHRISTMAS_EVENT = {
    "name": {
        "fi": "Joulu",
        "en": "Christmas"
    },
    "event_dates": {
        "starting_day": '2022-12-24T12:00:00Z'
    }
}


def test_swap_changes_positions_of_two_strings():
    my_list = ['a', 'b', 'c']

    swap(my_list, 0, 2)

    assert my_list == ['c', 'b', 'a']


def test_swap_changes_positions_of_events():
    events = [CHRISTMAS_EVENT, UNKNOWN_EVENT, JANUARY_1ST_EVENT]

    swap(events, 0, 1)

    assert events == [UNKNOWN_EVENT, CHRISTMAS_EVENT, JANUARY_1ST_EVENT]


def test_bubble_sort_with_three_events():
    events = [CHRISTMAS_EVENT, JANUARY_1ST_EVENT, UNKNOWN_EVENT]

    bubble_sort(events)

    assert events == [UNKNOWN_EVENT, JANUARY_1ST_EVENT, CHRISTMAS_EVENT]


def test_str_to_datetime_returns_time_in_helsinki_timezone():
    # testin alustus
    time_str = '2021-08-13T07:00:00.000Z'

    # testattava operaatio
    dt = str_to_datetime(time_str)

    # assertiot
    assert dt.time() == time(10, 0)
    assert dt.date() == date(2021, 8, 13)


def test_str_to_datetime_returns_correct_time_in_winter():
    # testin alustus
    time_str = '2021-12-13T07:00:00.000Z'

    # testattava operaatio
    dt = str_to_datetime(time_str)

    # assertiot
    assert dt.time() == time(9, 0)
    assert dt.date() == date(2021, 12, 13)


def test_get_sorted_events_with_mock(mocker):
    # alustus on nyt vähän pidempi:
    my_events = [CHRISTMAS_EVENT, JANUARY_1ST_EVENT, UNKNOWN_EVENT]
    mocker.patch('events_by_date.get_events', return_value=my_events)

    # testattava kutsu (tällä on riippuvuus mockattuun funktioon)
    response_list = get_sorted_events()

    # assertoidaan tulos:
    assert response_list == [UNKNOWN_EVENT, JANUARY_1ST_EVENT, CHRISTMAS_EVENT]
