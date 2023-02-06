# Node, NPM, Express ja Promiset

Tällä oppitunnilla jatkamme JavaScript-kielen ja Node.js:n parissa. Tutustumme suosittuun [Express](https://expressjs.com/)-sovelluskehykseen (framework), jonka avulla voimme toteuttaa JavaScript-pohjaisen verkkopalvelun.

# Express.js

Node.js:lle on olemassa useita web-sovelluskehyksiä, joista [express](https://www.npmjs.com/package/express) on hyvin suosittu:

> *"Fast, unopinionated, minimalist web framework for node."*
>
> https://www.npmjs.com/package/express

Express voidaan asentaa olemassa olevaan npm-projektiimme seuraavasti:

```
$ npm install express
```

Express-sovelluskehystä voidaan nyt kokeilla omassa koodissa esimerkiksi [express.js:n koodiesimerkin](https://www.npmjs.com/package/express) mukaisesti:

```js
// https://www.npmjs.com/package/express
const express = require('express');
const app = express();

app.get('/', function (req, res) {
  res.send('Hello World');
});

app.listen(3000); // kuunneltava portti
```

Kun koodi on käynnissä, voit kokeilla vierailla osoitteessa [http://localhost:3000](http://localhost:3000).

Seuraavissa kappaleissa esiintyvä soveltavat käyttäjien ja postausten tarjoamista selaimille REST-rajapinnan kaltaisesti.


## JSON-datan palauttaminen

https://expressjs.com/en/4x/api.html#res.json

```js
app.get('/users', async function (req, res) {
    let users = await getUsers();
    res.json(users);
});
```

Käyttäessäsi json-metodia, express lisää HTTP-vastaukseen automaattisesti oikean `Content-Type`-otsikon:

```
$ curl -I localhost:3000/users
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 28712
```

## HTTP-parametrien käsittely

https://expressjs.com/en/4x/api.html#req.query

```js
app.get('/users/', async function (req, res) {
  let id = Number(req.query.id);
});
```

Esimerkkipyyntö:

```
curl http://localhost:3000/users/?id=10
```

## Polkumuuttujien käsittely

https://expressjs.com/en/guide/routing.html#route-parameters

```js
app.get('/users/:id(\\d+)', async function (req, res) {
    let id = Number(req.params.id);
});
```

Esimerkkipyyntö:

```
curl http://localhost:3000/users/10
```

## Node.js-palvelimen uudelleenkäynnistys

Node.js-palvelin täytyy uudelleenkäynnistää aina koodimuutosten jälkeen. Uudelleenkäynnistys voidaan myös automatisoida `nodemon`-komennon avulla:

> *"nodemon is a tool that helps develop node.js based applications by automatically restarting the node application when file changes in the directory are detected.*
>
> *nodemon does not require any additional changes to your code or method of development. nodemon is a replacement wrapper for node. To use nodemon, replace the word node on the command line when executing your script."*
>
> nodemon. https://www.npmjs.com/package/nodemon

Tällä oppitunnilla käytämme nodemon-työkalua seuraavasti:

```
$ npm install --save-dev nodemon
$ npm start
```

Nodemon voidaan asentaa myös globaalisti, jolloin sillä voidaan suorittaa ja uudelleenkäynnistää käytännössä mitä vain sovelluksia:

```
$ npm install -g nodemon
$ nodemon index.js
```

Projektikohtaisessa asennuksessa nodemon täytyy käynnistää esimerkiksi `npm start`-komennolla, ja `package.json`-tiedostoon täytyy lisätä `start`-skripti:

```diff
"scripts": {
+  "start": "nodemon index.js"
}
```

