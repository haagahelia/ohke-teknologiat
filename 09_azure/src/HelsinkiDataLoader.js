/**
 * Load data from Helsinki API and run to a CSV-file
 */
const fetch = require('node-fetch');

const fs = require('fs');

async function getEventsAsync() {
    let response = await fetch('http://open-api.myhelsinki.fi/v1/events/');
    let json = await response.json();
    let events = json.data;
    return events;
}

//TODO: Pitäsikö eventit ajaa map-rakenteeseen, jossa eventin nimi olisi avaimena, eli
//ei otettaisi samannimisiä eventtejä useaan kertaan, vaan poimittaisiin niistä vain yksi..
async function getOnlyEventNamesAndTagsForXEvents(howManyEvents = 100) {
    let events = await getEventsAsync();
    let onlyNEvents = events.slice(0, howManyEvents);
    return onlyNEvents.map(event => ({ name: event.name.fi, tags: event.tags.map(tag => tag.name) }));
}

function removeEventsWithEmptyEventName(events) {
    return events.filter(event => !!event.name);
}

function removeEventsWithFewerThanXTags(events, x = 1) {
    return events.filter(event => event.tags.length >= x);
}

function replaceCommasWithSpaces(string) {
    return string.split(",").join(" ");
}

function chooseFirstIfNotEmpty(first, second) {
    return !!first ? first : second;
}

function convertEventsToCSV(events) {
    let csvContent = "name,tag1,tag2,tag3\n"
        + events.map(e => "" + replaceCommasWithSpaces(e.name) + "," + e.tags[0]
            + "," + chooseFirstIfNotEmpty(e.tags[1], e.tags[0]) + "," + chooseFirstIfNotEmpty(e.tags[2], e.tags[0])).join("\n");
    return csvContent;
}

function writeToFile(content) {
    fs.writeFile('helsinkiData.csv', content, err => {
        if (err) throw err;
    });
}

getOnlyEventNamesAndTagsForXEvents(200).then(response => {
    let eventsWithoutEmptyTags = removeEventsWithFewerThanXTags(response, 1);
    let eventsWithoutEmptyNamesOrTags = removeEventsWithEmptyEventName(eventsWithoutEmptyTags)
    let eventsInCSV = convertEventsToCSV(eventsWithoutEmptyNamesOrTags);
    writeToFile(eventsInCSV);
    console.log(eventsInCSV + "\nEventtien lopullinen määrä: " + eventsWithoutEmptyNamesOrTags.length);
})