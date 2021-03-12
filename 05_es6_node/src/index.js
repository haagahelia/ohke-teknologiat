// https://www.npmjs.com/package/express
const express = require('express');
const { getUsers, getPosts } = require('./blog/api');

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', function (req, res) {
    res.send('Hello World');
});

app.get('/users', async function (req, res) {
    let users = await getUsers();
    res.json(users);
});

app.get('/users/:id(\\d+)', async function (req, res) {
    let id = Number(req.params.id);
    let users = await getUsers();
    let user = users.find(u => u.id === id);
    res.json(user || null);
});

app.get('/posts', async function (req, res) {
    let posts = await getPosts();
    let id = req.query.id;

    if (id) {
        let post = posts.find(p => p.id === Number(id));
        res.json(post || null);
    } else {
        res.json(posts);
    }
});

app.listen(PORT, () => console.log(`Palvelin käynnissä portissa ${PORT}`));
