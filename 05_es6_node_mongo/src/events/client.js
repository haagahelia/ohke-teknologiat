const fetch = require('node-fetch');

async function getEventsAsync() {
    let response = await fetch('http://open-api.myhelsinki.fi/v1/events/');
    let json = await response.json();
    let events = json.data;
    return events;
}

module.exports = { getEventsAsync };