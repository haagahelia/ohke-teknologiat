const express = require('express');
const app = express();

const { createEventDateFilter } = require('./events/dates');
const { getEventsAsync } = require('./events/client');

app.get('/', async function (req, res) {
    let events = await getEventsAsync();

    let { min_date, max_date } = req.query;
    let dateFilter = createEventDateFilter(min_date, max_date);
    let filtered = events.filter(dateFilter);
    res.json(filtered);

});

let port = parseInt(process.env.PORT) || 3000;

app.listen(port, () => console.log(`running on port ${port}`));