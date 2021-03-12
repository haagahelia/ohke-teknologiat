const fetch = require('node-fetch');

async function getUsers() {
    let response = await fetch('https://jsonplaceholder.typicode.com/users');
    let users = await response.json();
    return users;
}

async function getPosts() {
    return fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => response.json());
}


module.exports = { getPosts, getUsers };