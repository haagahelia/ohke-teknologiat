/**
 * Load data from Helsinki API and run to a CSV-file
 */
const fetch = require('node-fetch');

async function getEventsAsync() {
    let response = await fetch('http://open-api.myhelsinki.fi/v1/events/');
    let json = await response.json();
    let events = json.data;
    return events;
}

//TODO: Pitäsikö eventit ajaa map-rakenteeseen, jossa eventin nimi olisi avaimena, eli
//ei otettaisi samannimisiä eventtejä useaan kertaan, vaan poimittaisiin niistä vain yksi..
async function getOnlyEventNamesAndTags(howManyEvents = 100) {
    let events = await getEventsAsync();
    let onlyNEvents = events.slice(0, howManyEvents);
    return onlyNEvents.map(event => ({ event: event.name.fi, tags: event.tags.map(tag => tag.name) }));
}

function removeEventsWithEmptyTags(events) {
    return events.filter(event => event.tags.length > 0);
}

function replaceCommasWithSpaces(string) {
    return string.split(",").join(" ");
}

function convertEventsToCSV(events) {

    //FIXME: Jos halutaan käyttää kaikki tägit...
    /*let csvContent = "name,tag1,tag2,tag3,"
        + events.map(e => "" + e.event + "," + e.tags.join(",")).join("\n");*/

    let csvContent = "name,tag1,tag2,tag3,\n"
        + events.map(e => "" + replaceCommasWithSpaces(e.event) + "," + e.tags[0]
            + "," + e.tags[1] + "," + e.tags[2]).join("\n");
    return csvContent;
}

getOnlyEventNamesAndTags(20).then(response => {
    let eventsWithoutEmptyTags = removeEventsWithEmptyTags(response);
    let eventsInCSV = convertEventsToCSV(eventsWithoutEmptyTags);
    console.log(eventsInCSV);
    //TODO: Ajetaan tulokset vielä csv-tiedostoon...
})

//module.exports = { getEventsAsync };