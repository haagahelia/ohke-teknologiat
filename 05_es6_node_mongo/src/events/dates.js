function createEventDateFilter(min = '0000-00-00', max = '9999-12-31') {
    return function (event) {
        let { starting_day } = event.event_dates;
        return min <= starting_day && starting_day <= max;
    }
}

module.exports = {
    createEventDateFilter
};

