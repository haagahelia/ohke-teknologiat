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

app.listen(3000, () => console.log('running'));