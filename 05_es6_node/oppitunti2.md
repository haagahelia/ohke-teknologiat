# Oppitunti 12.3.2021

Tällä oppitunnilla jatkamme JavaScript-kielen ja Node.js:n parissa. Tutustumme suosittuun [Express](https://expressjs.com/)-sovelluskehykseen, jonka avulla voimme toteuttaa JavaScript-pohjaisen verkkopalvelun. Lisäksi sivuamme JavaScriptin yksikkötestausta [Mocha](https://mochajs.org/)-työkalun avulla.



# ES6-syntaksien kertaus

Edellisellä oppitunnilla käsittelimme mm. seuraavassa koodiesimerkissä esiintyviä syntakseja:

```js
function helloAgent({ names }) {
    let { first, last } = names;
    console.log(`My name is ${last}, ${first} ${last}`);
}

module.exports = { helloAgent };
```

Miten tässä moduulissa määritettyä `helloAgent`-funktiota voitaisiin kutsua toisesta Node.js-moduulista?


# Users ja Posts -tehtävän malliratkaisu

[Edellisen oppitunnin](oppitunti1.md) tehtävässä teidän tuli yhdistellä Post-olioita User-olioihin hyödyntäen kuvitteellisen blogin JSON-tietorakenteita.

Tehtävän ratkaisemiseksi oli useita erilaisia lähestymistapoja, ja tällä tunnilla tutustumme funktionaaliseen lähestymistapaan, jossa käsittelemme aineiston map- ja filter-operaatioiden avulla.


# JS-koodin yksikkötestaaminen

Koodin testaamiseksi tarvitsemme testaustyökalun, joka voi olla esimerkiksi [Mocha](https://mochajs.org/). Mocha kannattaa asentaa NPM-työkalun avulla, ja jotta NPM käsittelee koodiamme projektina, tulee se alustaa seuraavalla komennolla:

```
$ npm init
```

Tämän jälkeen voimme asentaa mocha-riippuvuuden NPM:n avulla:

```
$ npm install --save-dev mocha
```

Seuraavissa vaiheissa seuraamme Mochan dokumentaatiossa [https://mochajs.org/#getting-started](https://mochajs.org/#getting-started) olevia työvaiheita.

Testejä varten luodaan uusi kansio "test":

```
$ mkdir test
```

Package.json-tiedoston `test`-skriptiksi asetetaan `mocha`-komento:

```diff
 "scripts": {
+  "test": "mocha"
-  "test": "echo \"Error: no test specified\" && exit 1"
 },
```

Nyt testit voidaan suorittaa `npm`-komennon avulla:

```
$ npm test
```

```js
const assert = require('assert');
const { getUsers, getPosts, combineUsersAndPosts, getPostsByUser } = require('../blog/functions');

describe('Users and posts', function () {

    it('should get posts for a single user', function () {
        let user = { id: 1, name: 'John Doe' };
        let posts = [{ id: 1, userId: 1 }, { id: 2, userId: 2 }, { id: 3, userId: 1 }];

        let result = getPostsByUser(user, posts);
        assert.deepStrictEqual(result, [posts[0], posts[2]]);
    });

    it('should connect posts to users', function () {
        let users = [{ id: 1 }, { id: 2 }];
        let posts = [{ id: 1, userId: 1 }, { id: 2, userId: 1 }];

        let result = combineUsersAndPosts(users, posts);

        assert.deepStrictEqual(result, [
            {
                id: 1,
                posts: [{ id: 1, userId: 1 }, { id: 2, userId: 1 }]
            },
            {
                id: 2,
                posts: []
            }
        ]);
    });
});


describe('Fetch requests', function () {

    it('returns 10 users', async function () {
        let users = await getUsers();
        assert.strictEqual(users.length, 10);
    });

    it('returns 100 posts', async function () {
        let posts = await getPosts();
        assert.strictEqual(posts.length, 100);
    })
});
```


## Vertailu JavaScriptillä

Yllä esitellyissä testeissä sekä oppitunnin esimerkissä vertailu tehdään `assert.deepStrictEqual`-funktion avulla, eikä yhtäsuuruusmerkeillä. Tämä johtuu siitä, että JavaScript vertailee taulukoita ja olioita eri tavalla kuin esimerkiksi Python. 

### Taulukoiden vertailu

Taulukoita vertailtaessa JavaScript tutkii, onko kyseessä sama taulukko. __Taulukoiden sisältöjä ei vertailla.__

```js
> [1, 2, 3] === [1, 2, 3]
false
> [1, 2, 3] == [1, 2, 3]
false
```

### Olioiden vertailu

Kuten taulukoiden kanssa, myös olioita vertailtaessa tarkastetaan ovatko oliot samat. __Olioiden sisältöjä ei vertailla.__

```js
> { language: "JavaScript" } === { language: "JavaScript" }
false
> { language: "JavaScript" } == { language: "JavaScript" }
false
```

Eri kielet toimivat vertailujen osalta eri logiikalla. Esimerkiksi Python vertailee tietorakenteiden sisältöä:

```python
>>> [1, 2, 3] == [1, 2, 3] # Python
True
>>> { "language": "JavaScript" } == { "language": "JavaScript" } # Python
True
>>>
```

### deepStrictEqual

Koska olioiden vertaileminen vertailee vain, ovatko oliot samat, joudumme hyödyntämään erillistä vertailulogiikkaa. Node-yksikkötesteissä voimme hyödyntää esimerkiksi `assert`-moduulin `deepStrictEqual`-metodia, joka vertailee rekursiivisesti sille annettuja arvoja:

```js
const assert = require('assert');

assert.deepStrictEqual([1, 2, 3], [1, 2, 3]):
assert.deepStrictEqual({ language: "JavaScript" }, { language: "JavaScript" });
```

https://nodejs.org/api/assert.html#assert_assert_deepstrictequal_actual_expected_message


### Totuusarvojen vertailu

JavaScriptissä vertailuoperaatiot tehdään usein kolmella merkillä eli `===` tai `!==`. Kolmen merkin vertailuoperaatiot tarkastavat, että vertailtavien arvojen tyyppi on sama. Mikäli tyyppitarkastus jätetään tekemättä, JavaScript vertailee tyhjiä ja nollaan vertautuvia arvoja epäloogisesti.

Kahden yhtäsuuruusmerkin vertailut tuottavat epäloogisia tuloksia esimerkiksi seuraavissa tapauksissa:

```js
> 1 == true
true
> "1" == true
true
> "0" == false  // nolla merkkijonona ja false
true
> [] == false   // tyjä taulukko ja false
true
> 0 == false    // nolla ja false
true
> 0 == "0"      // nolla merkkijonona ja nolla
true
> 0 == "+00000" // "pitkä nolla" etumerkillä merkkijonona
true
> 0 == []       // nolla ja tyhjä taulukko
true
> "0" == []     // molemmat ovat false, mutta silti keskenään erisuuruiset!! 🤯
false
```

Vertailu kolmella merkillä on helpommin arvattavissa, koska vertailussa sekä tyypin että arvon tulee olla sama:

```js
> 1 === true
false
> "1" === true
false
> "0" === false
false
> [] === false
false
> 0 === false
false
> 0 === "0"
false
> 0 === []
false
> "0" === []
false
```

Voit tutustua aiheeseen syvällisemmin YouTube-videolla [JavaScript == VS === (Web Dev Simplified)](https://www.youtube.com/watch?v=C5ZVC4HHgIg).


----


# Fetch-harjoitus

Tähän asti olemme lukeneet käyttäjien ja postausten JSON-rakenteet paikallisesta tiedostosta `require`-funktiolla. Tämä on tapahtunut synkronisesti, eli lukeminen on tehty loppuun ennen seuraavalle riville etenemistä.

Tyypillisesti tiedostojen lukeminen, tietokantakyselyt ja http-pyynnöt tapahtuvat kuitenkin JavaScriptissä asynkronisesti, eli vastausta ei jäädä odottamaan, vaan ohjelman suoritus siirtyy suoraan eteenpäin. Asynkronisten operaatioiden valmistumisen jälkeen niiden tuloksia pystytään hyödyntämään esimerkiksi Promise-olioiden ja then-metodin avulla.

Selaimissa HTTP-pyyntöjä tehdään usein JavaScriptin [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)-funktiolla. Nodessa ei ole valmista toteutusta fetch-funktiolle, mutta vastaava funktio saadaan asennettua `node-fetch`-pakettina:

> *"node-fetch: a light-weight module that brings window.fetch to Node.js"*
>
> https://www.npmjs.com/package/node-fetch

Node-fetch voidaan asentaa seuraavasti:

```
$ npm install node-fetch
```

HTTP-pyyntö voidaan tehdä nyt sovelluksessa seuraavasti:

```js
const fetch = require('node-fetch');

let httpPromise = fetch('https://jsonplaceholder.typicode.com/users');
```

Fetch-funktion sijasta voisimme käyttää myös muita HTTP-asiakaskirjastoja, kuten [axios](https://www.npmjs.com/package/axios). Tällä oppitunnilla käytämme fetch-funktiota, koska se on hyödynnettävissä suoraan eri selaimissa.


## Fetch, Promiset, async ja await

Asynkroniset kutsut, kuten `fetch`, palauttavat Promise-oliota:

> *"A Promise is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise to supply the value at some point in the future.*"
>
> [MDN web docs. Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

Promise-olion tapahtumankuuntelija asetetaan kutsumalla Promisen `then`-metodia ja antamalla sille funktio, jota kutsutaan, kun promisen operaatio on valmistunut:

```js
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => console.log(users[0].name))
```

Peräkkäisiä Promise-olioita voidaan myös ketjuttaa, jolloin ensimmäisenä Promisen `then`-metodille annettu funktio suoritetaan aina ennen seuraavia kutsuja, ja edeltävän funktion palauttama arvo välitetään aina seuraavalle funktiolle. Tästä käytetään myös termiä ketjutus eli chaining.

Voit tutustua itsenäisesti tarkemmin `fetch`-funktioon sekä sen palauttamien `Promise`-olioiden käyttämiseen seuraavien YouTube-videoiden avulla:

**[Google Chrome Developers: Using the Fetch API](https://youtu.be/Ri7WRoRcl_U)**

> *"The Fetch API is a modern replacement for XMLHttpRequest. It includes much of the code you used to write for yourself: handling redirection and error codes, and decoding the result. This video gives you an easy introduction."*

**[Google Chrome Developers: Intro to Promises (incl async/await)](https://youtu.be/7unX6hn5NA8)**

> *"Promises make asynchronous programming much easier than the traditional event-listener or callback approaches. This video explains promises, promise-chaining, and complex error-handling."*

## Tuntiesimerkki: fetch-kutsujen ja asynkronisuuden hyödyntäminen

Asynkroninen ohjelmointityyli tekee koodin kirjoittamisesta ajoittain hankalaa. Erityisesti tilanteissa, joissa tarvitsemme useita asynkronisia resursseja, joudumme kiinnittämään suoritusjärjestykseen enemmän huomiota kuin olemme tottuneet tekemään Javan ja Pythonin kanssa.

Asynkronisuudesta on kuitenkin myös hyötyjä: voimme käynnistää useita asynkronisia operaatioita helposti ilman, että meidän täytyy odottaa ensimmäisten operaatioiden valmistumista.

Tällä tunnilla tutustumme siihen, miten Users ja Posts -esimerkki voidaan muuntaa tekemään käyttäjien ja postausten haku rinnakkain.


----


# Express.js

Nodelle on olemassa useita web-sovelluskehyksiä, joista [express](https://www.npmjs.com/package/express) on hyvin suosittu:

> *"Fast, unopinionated, minimalist web framework for node."*
>
> https://www.npmjs.com/package/express

Asennetaan express seuraavasti:

```
$ npm install express
```

Liitetään seuraavaksi tapahtumien käsittely osaksi Expressin esimerkkisovellusta. Tavoitteemme on, että palvelimemme vastaa pyyntöihin JSON-rakenteella, joka on rajattu annettujen päivämäärien mukaan ja järjestetty kronologiseen järjestykseen. Lisäominaisuuksina voimme toteuttaa myös "limit"-ominaisuuden tapahtumien määrän rajoittamiseksi.

```js
// https://www.npmjs.com/package/express
const express = require('express');
const app = express();
 
app.get('/', function (req, res) {
  res.send('Hello World');
})
 
app.listen(3000);
```

Tämän viikon harjoituksissa hyödynnämme ainakin seuraavia express:in ominaisuuksia:


## JSON-datan palauttaminen

https://expressjs.com/en/4x/api.html#res.json

```js
app.get('/users', async function (req, res) {
    let users = await getUsers();
    res.json(users);
});
```

Käyttäessäsi json-metodia, express lisää HTTP-vastaukseen oikean `Content-Type`-otsikon:

```
$ curl -I localhost:3000/users
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 28712
```

## Parametrien käsittely

https://expressjs.com/en/4x/api.html#req.query

```js
app.get('/users/', async function (req, res) {
  let id = Number(req.query.id));
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

Node.js-palvelin täytyy uudelleenkäynnistää aina koodimuutosten jälkeen. Uudelleenkäynnistys voidaan automatisoida `nodemon`-komennon avulla:

> *"nodemon is a tool that helps develop node.js based applications by automatically restarting the node application when file changes in the directory are detected.*
>
> *nodemon does not require any additional changes to your code or method of development. nodemon is a replacement wrapper for node. To use nodemon, replace the word node on the command line when executing your script."*
>
> nodemon. https://www.npmjs.com/package/nodemon

Tällä oppitunnilla käytämme nodemon-työkalua seuraavasti:

```
$ npm install -g nodemon
$ nodemon index.js
```

Nodemon voidaan asentaa myös projektikohtaisesti:

```
$ npm install --save-dev nodemon
$ npm start
```

Projektikohtaisessa asennuksessa nodemon täytyy käynnistää esim. `npm start`-komennolla ja `package.json`-tiedostoon täytyy lisätä `start`-skripti:

```
"scripts": {
  "start": "nodemon index.js"
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

Tämän viikon tehtävässä sinun tulee hyödyntää Node.js:ää, npm:ää sekä [express](https://www.npmjs.com/package/express)-kirjastoa ja toteuttaa HTTP-palvelu, joka palauttaa postitoimipaikkojen nimiä sekä postinumeroita.

Tavoitteenamme on asynkronisen web-ohjelmoinnin opettelun lisäksi kerrata tietorakenteiden läpikäyntiä. Mikäli tehtävät eivät tarjoa tarvittavaa haastetta tai haluat oppia välimuistituksesta, voit tehdä lisäksi valinnaisen lisätehtävän.


## JSON-tiedoston hakeminen ja parametrin käsittely (arvosanatavoite 3)

Toteuta express-sovellus, jolta voidaan kysyä postinumeron avulla postitoimitoimipaikan nimi. Postinumero annetaan HTTP-pyynnön parametrina esimerkiksi seuraavasti:

```
curl http://localhost:3000/postitoimipaikka?numero=99999
```

Vastaus tulee palauttaa JSON-muodossa esimerkiksi seuraavasti:

```json
{
  "postinumero": "99999",
  "toimipaikka": "KORVATUNTURI"
}
```

Varaudu myös tilanteeseen, jossa annettua postinumeroa ei löydy. Tällöin voit palauttaa toimipaikaksi esimerkiksi `null`-arvon.

[Postinumeroaineisto](https://github.com/theikkila/postinumerot) löytyy GitHubista [JSON-muodossa](https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json). JSON-aineisto tulee ladata JavaScript-koodissa dynaamisesti esimerkiksi fetch-funktiolla tai axios-kirjastolla. Älä siis tallenna aineistoa staattiseksi tiedostoksi.

Voit lukea tarkemman kuvauksen käsiteltävästä aineistosta [Python-tehtävän tehtävänannosta](../01_python#postinumeroaineisto).


## Polun käsittely ja JSON-tietorakenteen läpikäynti (arvosanatavoite 5)

Toteuta edellä ohjeistetun tehtävän lisäksi palvelimelle toinen polku, josta voidaan etsiä postitoimipaikan nimellä kaikki siihen kuuluvat postinumerot. Postitoimipaikan nimi tulee antaa osana polkua, esimerkiksi seuraavasti:

```
curl http://localhost:3000/postitoimipaikka/porvoo/
```

Vastaus tulee palauttaa JSON-muodossa esimerkiksi seuraavasti:

```json
{
  "toimipaikka": "porvoo",
  "postinumerot": ["06100", "06401", "06151", "06150", "06101", "06500", "06450", "06400", "06200"]
}
```

Ohjelman tulee löytää postinumerot annetun nimen kirjainkoosta riippumatta. Varaudu myös parhaaksi katsomallasi tavalla tapaukseen, että pyydettyä postitoimipaikkaa ei löydy aineistosta.

**Vinkki**

Python-harjoitusten yhteydessä käytimme aineiston läpikäynnissä Pythonin dict-tietorakenteen `keys()`-, `values()`- ja `items()`-metodeja. JavaScriptin Object-luokasta löytyy vastaavat metodit `Object.keys(data)`, `Object.values(data)` ja `Object.entries(data)`, jotka mahdollisesti ovat hyödyksi tehtävän ratkaisussa:

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries

## Postinumeroaineiston välimuistitus (extra)

Postinumeroaineiston hakeminen verkosta on tämän ohjelman suorituskyvyn kannalta suurin haaste. Lisäksi useat rajapinnat rajoittavat niihin tehtävien kutsujen määrää, joten rajapinta saattaisi lakata vastaamasta tekemiimme toistuviin kutsuihin:

> *"Rate limiting is a strategy for limiting network traffic. It puts a cap on how often someone can repeat an action within a certain timeframe – for instance, trying to log in to an account. Rate limiting can help stop certain kinds of malicious bot activity. It can also reduce strain on web servers."*
>
> Cloudflare. What Is Rate Limiting? https://www.cloudflare.com/learning/bots/what-is-rate-limiting/

Aineiston lataaminen etukäteen tai vain ohjelman käynnistyessä ratkaisisi ongelman, mutta aineistoon tulevat päivitykset eivät tulisi omaan palveluumme automaattisesti saataville.

Näiden ongelmien ratkaisemiseksi aineistoa voidaan pitää ohjelman muistissa tietyn aikaa, jonka jälkeen aineisto haetaan uudelleen. Tällaisista [välimuisteista](https://fi.wikipedia.org/wiki/V%C3%A4limuisti) käytetään termiä cache.

HTTP-vastaukset sisältävät hyvin usein tietoa mm. niiden välimuistituksesta. GitHub-palvelin pyytää JSON-tiedostoa ladattaessa HTTP-headerin avulla asiakasta välimuistittamaan vastauksen 5 minuutin ajaksi:

```
$ curl -I https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json
HTTP/2 200 
cache-control: max-age=300
content-security-policy: default-src 'none'; style-src 'unsafe-inline'; sandbox
content-type: text/plain; charset=utf-8
etag: "0c7eee999e998c6d959353abc9abeccb56d0ddaaac9a5d46dac0b123d68d0c41"
strict-transport-security: max-age=31536000
x-content-type-options: nosniff
x-frame-options: deny
x-xss-protection: 1; mode=block
x-github-request-id: 621C:574F:16BD8FE:17E9826:6049E5B7
accept-ranges: bytes
date: Thu, 11 Mar 2021 09:43:46 GMT
via: 1.1 varnish
x-served-by: cache-bma1627-BMA
x-cache: HIT
x-cache-hits: 1
x-timer: S1615455827.977461,VS0,VE1
vary: Authorization,Accept-Encoding
access-control-allow-origin: *
x-fastly-request-id: 88772d1f4b3180348997fd9230c44aad01afcef0
expires: Thu, 11 Mar 2021 09:48:46 GMT
source-age: 155
content-length: 114651
```

Yllä olevissa HTTP-otsikoissa on välimuistin ajan lisäksi muitakin välimuistitukseen liittyvää tietoa tietoja, kuten `etag` ja `x-cache`.

Välimuistitus voidaan toteuttaa ohjelmassa monella eri tavalla. Yksi vaihtoehto on välimuistittaa HTTP-pyyntöjen vastauksia käyttämällä HTTP-asiakaskirjastoa, joka huolehtii välimuistituksesta automaattisesti. Tällöin emme tarvitse muutoksia omaan koodiimme.

Toinen vaihtoehto on toteuttaa välimuistitus osaksi omaa ohjelmaamme:

> *"You could then wrap your API call in a helper function which checks the cache, and returns the value if it's present. If it's not it makes the API request, adds it to the cache, then returns it."*
>
> Nick Mitchinson. Proper way to cache data from API call with nodejs. https://stackoverflow.com/a/15608809

Välimuistiin asettamisen ja sieltä hakemisen lisäksi vanhentuneet vastaukset tulee luonnollisesti poistaa välimuistista, jolloin data haetaan uudestaan API-rajapinnasta.

Tehtävän lisäosion ratkaisemisessa voit halutessasi käyttää hyödyksi esimerkiksi fetch-kutsuja välimuistittavaa [node-fetch-cache](https://www.npmjs.com/package/node-fetch-cache)-kirjastoa tai sanakirjan tavoin toimivaa [node-cache](https://www.npmjs.com/package/node-cache)-kirjastoa. Voit myös toteuttaa oman välimuistituslogiikan. Riippuvuuksia asentaessasi on hyvä muistaa, että npm-paketit ovat erinäisten tahojen julkaisemaa suoritettavaa koodia. Niitä asennettaessa kannattaa perehtyä projektien laatuun ja luotettavuuteen esimerkiksi niiden GitHub-sivujen avulla: [node-cache](https://github.com/node-cache/node-cache), [node-fetch-cache](https://github.com/mistval/node-fetch-cache).



## Tehtävän palauttaminen

Myös osittain ratkaistut palautukset hyväksytään ja arvostellaan suhteessa niiden valmiusasteeseen. Palauta kaikki ratkaisuusi liittyvät lähdekoodit erillisinä tiedostoina, eli ei pakattuna. Tehtävän DL on seuraava oppitunti. 

**Nimeä `.js`-päätteiset tiedostot `.js.txt`-päätteisiksi, mikäli Teams ei hyväksy tiedostojasi tietoturvasyistä.**
