let { data } = require('./events.json');
let { isBetweenDates } = require('./filters');

function compareEventDates(event1, event2) {
    let event1date = event1.event_dates.starting_day || '';
    let event2date = event2.event_dates.starting_day || '';

    return event1date.localeCompare(event2date);
}

let now = new Date();
let nextWeek = new Date();
nextWeek.setDate(now.getDate() + 7);

let nextWeekFilter = isBetweenDates(now, nextWeek);

data = data.filter(nextWeekFilter);

data.sort(compareEventDates);

let lines = data.map((e) => e.event_dates.starting_day + ' ' + e.name.fi);

lines.forEach((eventString) => console.log(eventString));
