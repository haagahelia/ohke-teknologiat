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

<!--
## Map: etäisyyden lisääminen kaikille tapahtumille

Meille erityisen hyödyllinen `map`-operaation käyttötapaus voisi olla etäisyyden lisääminen tapahtuman tietoihin. Kaikilla tapahtumilla on koordinaatit, joten meidän tulee vain laskea etäisyys kunkin tapahtuman koordinaattipisteen ja oman pisteemme välillä. Etäisyyden laskeminen on sen verran monimutkainen operaatio, että emme halua toteuttaa sitä omaan koodiimme. Sen sijaan käytämm evalmista `geolib`-kirjastoa:

> *"Library to provide basic geospatial operations like distance calculation, conversion of decimal coordinates to sexagesimal and vice versa, etc."*
>
> https://www.npmjs.com/package/geolib

Kirjasto asentuu `npm install`-komennolla seuraavasti:

```
npm install geolib
```

Nyt `geolib` voidaan ottaa käyttöön myös omassa koodissa:

```js
const geolib = require('geolib');

const helsinkiCoordinates = { lat: 60.1733244, lon: 24.9410248 };

let eventsWithDistance = events.map(event => {
    let eventCoordinates = { lat, lon } = event.location;
    return {
        ...event, // "object spread"
        distance: geolib.getDistance(helsinkiCoordinates, eventCoordinates) // lisätään uusi attribuutti!
    }
});
```

Huomaa, että yllä oleva koodi ei muuta alkuperäistä `events`-taulukkoa eikä sillä olevia olioita, vaan se luo uuden taulukon, joka täytetään kopioilla tapahtumista.


### Currying

Yllä olevassa koodiesimerkissä `map`-operaatiolle annettu funktio on sidottu `helsinkiCoordinates`-muuttujaan. Haluaisimme kuitenkin ohjelmassamme todennäköisesti laskea etäisyyksiä monipuolisesti, joten eri etäisyysfunktiot olisi tarpeen sitoa eri muuttujien arvoihin:

```js
const helsinkiCoordinates = { lat: 60.1733244, lon: 24.9410248 };
const espooCoordinates = { lat: 60.205491, lon: 24.655900 };
const rovaniemiCoordinates = { lat: 66.503059, lon: 25.726967 };
```

Voimme ratkaista ongelman soveltaen currying-tekniikkaa! Ensin lukitsemme koordinaattipisteen ja sen jälkeen kutsumme sisempää funktiota tapahtumaolioiden kanssa!

```js
function getDistanceTo(point) {
    return function (event) {
        return geolib.getDistance(point, event.location);
    }
}

// sama kuin:
let getDistanceTo = (point) => (event) => geolib.getDistance(point, event.location);
```

Nyt etäisyysfunktioita voidaan luoda kutsumalla `getDistanceTo`-funktioita eri koordinaattipisteillä. Funktio palauttaa aina uuden funktion, jonka sulkeumassa annettu koordinaattipiste on tallessa:

```js
// etäisyysfunktiot Helsinkiin ja Tukholmaan
let distanceFuncHelsinki = getDistanceTo(helsinkiCoordinates);
let distanceFuncStockholm = getDistanceTo(stockholmCoordinates);

// etäisyysfunktioiden hyödyntäminen tapahtuman kanssa:
let distaceHki = distanceFuncHelsinki(events[0]);
let distaceSto = distanceFuncStockholm(events[0]);

// etäisyyden lisääminen kaikkiin tapahtumiin!
let eventsWithCoordinates = events.map(event => ({ ...event, distance: distanceFuncHelsinki(event) }) );
events.forEach(event => event.distance = distanceFuncHelsinki(event));
```

**Pohdittavaa**

JavaScriptin taulukoilla on myös `forEach`-funktio, jonka avulla tietty funktio voidaan suorittaa taulukon jokaiselle arvolle. Miten `forEach`-funktion käyttäminen poikkeaa `map`-funktion käyttämisestä seuraavassa esimerkissä? Mitkä ovat niiden vahvuudet ja heikkoudet?

```js
// map:
let eventsWithCoordinates = events.map(event => ({ ...event, distance: distanceFuncHelsinki(event) }) );

// forEach:
events.forEach(event => event.distance = distanceFuncHelsinki(event));
```
-->
<!--
```js
function addDistanceTo(coordinates) {
    return function(event) {
        return {
            ...event,
            distance: geolib.getDistance(coordinates, event.location)
        }
    }
}
```

Nyt tapahtumille saadaan lisättyä etäisyys Helsingin koordinaateista suoraviivaisesti:

```js
let addDistanceToHelsinki = addDistanceTo(helsinkiCoordinates);
let eventsWithDistanceFromHelsinki = events.map(addDistanceToHelsinki);
```
-->

<!--
### Tapahtumien järjestäminen etäisyyden mukaan

Kun tapahtumille on lisätty uusi attribuutti `distance`, voidaan tätä käyttää hyväksi myös tapahtumien järjestämisessä etäisyyden mukaan. Seuraavan koodiesimerkin nuolifunktio vertailee kahta tapahtumaa niiden `distance`-attribuutin mukaan:

```js
// Jos etäisyys 1 on pienempi kuin etäisyys 2, on tuloksena negatiivinen luku:
eventsWithDistances.sort((event1, event2) => event1.distance - event2.distance);
```

Katso lisätietoa järjestämisestä ylempää kodasta "Järjestäminen alkamisajan mukaan".
-->


---



# Koodaustehtävä: postinumerot-backend

Tämän viikon tehtävässä sinun tulee hyödyntää Node.js:ää, npm:ää sekä [express](https://www.npmjs.com/package/express)-sovelluskehystä ja toteuttaa HTTP-palvelu, joka palauttaa aikaisemmilta viikoilta tuttuja postitoimipaikkojen nimiä sekä postinumeroita. Tarkemman tehtävänannon löydät Teamsin tehtävät-välilehdeltä.

