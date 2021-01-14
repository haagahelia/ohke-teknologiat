from events_by_date import get_sorted_events


def test_get_sorted_events():
    # testattava kutsu (tällä tehdään oikea pyyntö REST-apiin)
    events = get_sorted_events()

    # assertoidaan tulos:
    assert len(events) > 100

    for i in range(0, len(events) - 1):
        event0_date = events[i]["event_dates"]["starting_day"]
        event1_date = events[i+1]["event_dates"]["starting_day"]

        assert event0_date == None or event0_date <= event1_date
