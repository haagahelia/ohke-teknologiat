function isBetweenDates(minDate, maxDate) {
    let min = minDate.toISOString();
    let max = maxDate.toISOString();
    return function (event) {
        let { starting_day } = event.event_dates; // object destructuring
        return starting_day && min <= starting_day && starting_day <= max;
    }
}

module.exports = { isBetweenDates };
