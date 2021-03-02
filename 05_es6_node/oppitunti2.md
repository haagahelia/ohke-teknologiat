# Oppitunti 12.3.2021 (luonnos)

Tällä oppitunnilla jatkamme JavaScript-kielen ja sen työkalujen parissa. Tutustumme suosittuun [Express](https://expressjs.com/)-sovelluskehykseen, jonka avulla voimme toteuttaa Node.js-pohjaisen verkkopalvelun. Lisäksi sivuamme JavaScriptin yksikkötestausta [Mocha](https://mochajs.org/)-työkalun avulla.

## Express-harjoitus

Miten voisimme hyödyntää toteuttamaamme logiikkaa osana verkkopalvelua? Nodelle on olemassa useita web-sovelluskehyksiä, joista [express](https://www.npmjs.com/package/express) on hyvin suosittu:

> *"Fast, unopinionated, minimalist web framework for node."*
>
> https://www.npmjs.com/package/express

Asennetaan express seuraavasti:

```
$ npm install express --save
```

Liitetään seuraavaksi tapahtumien käsittely osaksi Expressin esimerkkisovellusta. Tarvoitteemme on, että palvelimemme vastaa pyyntöihin JSON-rakenteella, joka on rajattu annettujen päivämäärien mukaan ja järjestetty kronologiseen järjestykseen. Lisäominaisuuksina voimme toteuttaa myös "limit"-ominaisuuden tapahtumien määrän rajoittamiseksi.

```js
// https://www.npmjs.com/package/express
const express = require('express');
const app = express();
 
app.get('/', function (req, res) {
  res.send('Hello World');
})
 
app.listen(3000);
```

Harjoituksessä käytämme query-parametreja päivämäärien rajaamiseksi:

* https://expressjs.com/en/4x/api.html#req.query

Palvelin vastaa pyyntöihin JSON-muodossa:

* https://expressjs.com/en/4x/api.html#res.json

----

## Map 

> *The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.*
>
> [MDN web docs. Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

Tässä esimerkissä luomme tapahtumia sisältävän taulukon perusteella uuden, pelkät `id`-arvot sisältävän taulukon:

```js
> // map:lle annettava funktio palauttaa jokaista tapahtumaa kohden sen id-arvon:
> let ids = events.map(event => event.id)
> ids
[ 'helmet:214000', 'helmet:216844', 'helmet:216842', 'helmet:211890', 'helmet:214001', ... ]
```

`map`-operaatio suoritti annetun funktion taulukon jokaiselle tapahtumalle ja muodosti funktion paluuarvoista uuden taulukon. Tässä tapauksessa funktio yksinkertaisesti palautti saamansa tapahtuman id:n, joten uusi lista koostuu id-arvoista.


### Etäisyyden lisääminen kaikille tapahtumille

Meille erityisen hyödyllinen `map`-operaation käyttötapaus voisi olla etäisyyden lisääminen tapahtuman tietoihin. Kaikilla tapahtumilla on koordinaatit, joten meidän tulee vain laskea etäisyys kunkin tapahtuman koordinaattipisteen ja oman pisteemme välillä. Etäisyyden laskeminen on sen verran monimutkainen operaatio, että emme halua toteuttaa sitä omaan koodiimme. Sen sijaan käytämm evalmista `geolib`-kirjastoa:

> *"Library to provide basic geospatial operations like distance calculation, conversion of decimal coordinates to sexagesimal and vice versa, etc."*
>
> https://www.npmjs.com/package/geolib

Kirjasto asentuu `npm install`-komennolla seuraavasti:

```
npm install geolib --save
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

### Tapahtumien järjestäminen etäisyyden mukaan

Kun tapahtumille on lisätty uusi attribuutti `distance`, voidaan tätä käyttää hyväksi myös tapahtumien järjestämisessä etäisyyden mukaan. Seuraavan koodiesimerkin nuolifunktio vertailee kahta tapahtumaa niiden `distance`-attribuutin mukaan:

```js
// Jos etäisyys 1 on pienempi kuin etäisyys 2, on tuloksena negatiivinen luku:
eventsWithDistances.sort((event1, event2) => event1.distance - event2.distance);
```

Katso lisätietoa järjestämisestä ylempää kodasta "Järjestäminen alkamisajan mukaan".

----

## Map-harjoitus

Lisätään express-sovellukseen logiikka etäisyyden lisäämiseksi, mikäli koordinaattipisteet on annettu HTTP-pyynnön parametreina.

----

## Fetch, Promiset, async ja await

Asynkroniset kutsut, kuten `fetch`, palauttavat Promise-oliota:

> *"A Promise is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise to supply the value at some point in the future.*"
>
> [MDN web docs. Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

Promise-olion tapahtumankuuntelija asetetaan kutsumalla Promisen `then`-metodia ja antamalla sille funktio, jota kutsutaan, kun promisen operaatio on valmistunut. Peräkkäisiä Promise-oliota voidaan myös ketjuttaa, jolloin ensimmäisenä Promisen `then`-metodille annettu funktio suoritetaan aina ennen seuraavia kutsuja, ja edeltävän funktion palauttama arvo välitetään aina seuraavalle funktiolle. Tästä käytetään myös termiä "putkitus" eli piping.

Katso seuraavat videot `fetch`-funktion ja sen palauttamien `Promise`-olioiden käyttämisestä:

**[Google Chrome Developers: Using the Fetch API](https://youtu.be/Ri7WRoRcl_U)**

[![Google Chrome Developers: Using the Fetch API](https://img.youtube.com/vi/Ri7WRoRcl_U/mqdefault.jpg)](https://youtu.be/Ri7WRoRcl_U)

> *"The Fetch API is a modern replacement for XMLHttpRequest. It includes much of the code you used to write for yourself: handling redirection and error codes, and decoding the result. This video gives you an easy introduction."*

&nbsp;

**[Google Chrome Developers: Intro to Promises (incl async/await)](https://youtu.be/7unX6hn5NA8)**

[![Google Chrome Developers: Intro to Promises (incl async/await)](https://img.youtube.com/vi/7unX6hn5NA8/mqdefault.jpg)](https://youtu.be/7unX6hn5NA8)

> *"Promises make asynchronous programming much easier than the traditional event-listener or callback approaches. This video explains promises, promise-chaining, and complex error-handling."*

----

## Fetch-harjoitus

Tähän asti olemme lukeneet tapahtumien JSON-rakenteen paikallisesta tiedostosta `require`-funktiolla. Tämä on tapahtunut synkronisesti, eli lukeminen on tehty loppuun ennen seuraavalle riville etenemistä. Tyypillisesti tiedostojen lukeminen, tietokantakyselyt ja http-pyynnöt tapahtuvat kuitenkin asynkronisesti, eli vastausta ei jäädä odottamaan, vaan ohjelman suoritus siirtyy suoraan eteenpäin. Asynkronisten operaatioiden valmistumisen jälkeen niiden tuloksia pystytään hyödyntämään esimerkiksi edellä videoissa käsiteltyjen Promise-olioiden ja then-metodin avulla.

Asennetaan ensin `node-fetch`-niminen paketti, jonka avulla pystymme käyttämään selaimista tuttua `fetch`-funktioita http-pyyntöjen tekemiseen:

> *"node-fetch: a light-weight module that brings window.fetch to Node.js"*
>
> https://www.npmjs.com/package/node-fetch

```
$ npm install node-fetch --save
```

HTTP-pyyntö voidaan tehdä nyt sovelluksessa seuraavasti:

```js
const fetch = require('node-fetch');

let httpPromise = fetch('http://open-api.myhelsinki.fi/v1/events/');
```

**Tuntidemo asynkronisesta ohjelmoinnista, putkituksesta sekä async/await.**

----

## Reduce

> *"The reduce() method executes a reducer function (that you provide) on each element of the array, resulting in single output value."*
>
> [MDN web docs. Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

Reducen avulla voidaan tyypillisesti selvittää esimerkiksi kokoelman suurin tai pienin arvo, kaikkien arvojen summa tai muita vastaavia operaatioita. Reducen avulla voidaan kuitenkin toteuttaa lähes mitä vain operaatioita, joissa käsitellään yksi kerrallaan jonkin tietyn kokoelman arvot.

```js
let tulos = taulukko.reduce(( koottuArvo, nykyinenArvo ) => {
    /* operaatio, jonka paluuarvoa on seuraava koottuArvo */
    return X;
}, vapaaehtoinenAlkuarvo);
```

Kokonaislukutaulukon summa voitaisiin laskea reducen avulla esimerkiksi seuraavasti:

```js
let numerot = [1, 2, 3, 4, 5];

let summa = numerot.reduce( (summa, seuraava) => { 
    return summa + seuraava; // palautetaan aina uusi summa
}, 0); // alkuarvo summalle on nolla

// sama kuin:
let summa = numerot.reduce( (summa, seuraava) => summa + seuraava, 0);
```

Sekä `map` että `filter` on toteutettavissa `reduce`:n avulla. Tällöin koottava arvo on uusi taulukko, ja alkuperäisen taulukon arvot redusoidaan uudelle taulukolle joko ehdon täyttyessä (filter) tai muutettuna (map):

```js
> // map toteutettuna reducen avulla:
let tuplattu = [1, 2, 3, 4, 5].reduce((uusiTaulukko, arvo) => { 
    uusiTaulukko.push(arvo * 2);
    return uusiTaulukko;
}, [] );
> console.log(tuplattu);
[ 2, 4, 6, 8, 10 ]
```

```js
> // filter toteutettuna reducen avulla:
> let suurempiKuinKolme = [1, 2, 3, 4, 5].reduce((uusiTaulukko, arvo) => {
    if (arvo > 3) {
        uusiTaulukko.push(arvo);
    } 
    return uusiTaulukko; 
}, [] );
> console.log(suurempiKuinKolme);
[ 4, 5 ]
```

Reduce onkin erittäin monikäyttöinen operaatio, ja sen avulla onnistuu luontevasti myös esimerkiksi taulukon arvojen ryhmitteleminen tietyn avaimen mukaan. Voit lukea aiheesta lisää Googlesta hakusanoilla "JavaScript reduce group by" tai [tästä artikkelista](https://learnwithparam.com/blog/how-to-group-by-array-of-objects-using-a-key/).


## Bonus: JavaScriptin totuusarvot ja niiden vertailu

JavaScriptissä vertailuoperaatiot tehdään usein kolmella merkillä eli `===` tai `!==`. Kolmen merkin vertailuoperaatiot tarkastavat, että vertailtavien arvojen tyyppi on sama. Mikäli tyyppitarkastus jätetään tekemättä, JavaScript vertailee tyhjiä ja nollaan vertautuvia arvoja epäloogisesti.

Voit tutustua aiheeseen syvällisemmin YouTube-videolla [JavaScript == VS === (Web Dev Simplified)](https://www.youtube.com/watch?v=C5ZVC4HHgIg).

### Vertailu kahdella yhtäsuuruusmerkillä

Kahden yhtäsuuruusmerkin vertailut tuottavat epäloogisia tuloksia esimerkiksi seuraavissa tapauksissa:

```js
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

### Vertailu kolmella yhtäsuuruusmerkillä

Vertailu kolmella merkillä on helpommin arvattavissa, koska vertailussa sekä tyypin että arvon tulee olla sama:

```js
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


<!--
  let title; // Tarkastetaan onko suomenkielistä name atribuuttia saatavilla
  if (props.item.name.fi !== null) {
    // jos ei ole käytetään englanninkieleistä
    title = props.item.name.fi;
  } else if (props.item.name.en !== null) {
    title = props.item.name.en;
  }
-->



# Tehtävä 12.3.2021

Tämän viikon tehtävässä harjoitellaan asynkronista ohjelmointia sekä tunnilla esitettyjen ohjelmointitapojen hyödyntämistä. Haemme tehtävässä dataa verkosta, mutta tällä kertaa yksi HTTP-pyyntö ei riitä, vaan tarvitsemme logiikassa kahden HTTP-pyynnön tuloksia. JavaScriptin asynkronisuus saattaa lisätä tähän haastetta, mutta se myös mahdollistaa kahden pyynnön suorittamisen samanaikaisesti kohtuullisen helposti.

Toteuta JavaScriptillä HTTP-palvelu, joka hakee valmiista REST-rajapinnasta käyttäjiä ja postauksia. Käyttäjät ja postaukset on ryhmiteltävä oman HTTP-palvelusi vastauksessa siten, että kunkin käyttäjän kirjoittamat postaukset ovat koottu käyttäjän yhteyteen omaksi taulukoksi.

## Tehtävän data

Tässä tehtävässä käytetään "dummy" dataa JSON Placeholder -palvelusta:

> *"{JSON} Placeholder*
>
> *Free to use fake Online REST API for testing and prototyping*
>
> *Powered by JSON Server + LowDB"*
>
> https://jsonplaceholder.typicode.com/

Data tulee hakea dynaamisesti jokaiselle pyynnölle, **eli ei tallentaa etukäteen** seuraavista osoitteista:

* käyttäjät: https://jsonplaceholder.typicode.com/users
* postaukset: https://jsonplaceholder.typicode.com/posts

Saat itse valita, palauttaako HTTP-palvelusi datan JSON-muodossa (helpointa) vai muodostatko datan perusteella HTML-sivun esimerkiksi [pug-sivupohjien avulla](https://expressjs.com/en/guide/using-template-engines.html) (haastava).

Lopputuloksena palvelusi tulee palauttaa JSON-taulukko tai HTML-sivu käyttäjistä, jossa kunkin käyttäjän omat postaukset ovat ryhmiteltynä käyttäjän alle. Yksittäisen käyttäjän osalta lopputulos voi olla esimerkiksi seuraava:

```
curl http://localhost:3000/users
```

```js
[
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        },
        "posts": [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
            },
            
            // + loput saman käyttäjän postaukset täällä...
        ]
    },
    
    // + loput käyttäjät...

]
```

## Valmiiden kirjastojen käyttäminen

Tämän tehtävän ratkaisemiseksi et tarvitse välttämättä ulkoisia kirjastoja tai `npm`-komentoa. Pelkkä Node.js voi hyvin riittää. Sinulle saattaa kuitenkin olla hyötyä kirjastoista, kuten [express](https://www.npmjs.com/package/express), [axios](https://www.npmjs.com/package/axios) tai [node-fetch](https://www.npmjs.com/package/node-fetch). Myös apukirjastojen, kuten [lodash](https://www.npmjs.com/package/lodash) käyttäminen on sallittua eivätkä ne vaikuta arvosanaan.


## Pyyntöjen samanaikaisuus

Koska HTTP-pyynnöt ovat JavaScriptissä asynkronisia, käyttäjien ja postausten lataaminen voidaan tehdä joko rinnakkain tai yksi kerrallaan. 

Tämän tehtävän tai sen arvosanan kannalta ei ole merkitystä kumman tavan valitset, mutta harjoituksen vuoksi suosittelen pyrkimään lataamaan tiedostot samanaikaisesti rinnakkain. Tähän ei tarvita erillisiä työkaluja, vaan riittää että muistat, että Promiset ovat "tavallisia olioita", jotka voit asettaa muuttujiin, ja joiden then-metodia ei ole pakko kutsua välittömästi. Myös `Promise.all`-funktiosta voi olla apua.


## Vinkit datan käsittelyyn

Käyttäjien ja heidän postauksiensa yhdistämiseksi yksi lähestymistapa on käydä käyttäjät läpi `map`-metodilla ja muodostaa jokaisesta käyttäjästä uusi olio, jolla on taulukko postauksia. Postaustaulukko puolestaan voidaan rakentaa kullekin käyttäjälle `filter`-metodin avulla, valitsemalla taulukosta ne postaukset, joiden `userId` vastaa kyseisen käyttäjän `id`:tä.

Vaihtoehtoisesti voit myös ratkaista tehtävän täysin ilman `map`, `filter`, `reduce` yms. ES6-metodeja perinteisillä ehto- ja  toistorakenteilla. Oppimisen kannalta suosittelemme kuitenkin tutustumaan tunnilla esitettyihin ratkaisutapoihin.

## Tehtävän palauttaminen

Myös osittain ratkaistut palautukset hyväksytään ja arvostellaan suhteessa niiden valmiusasteeseen. Palauta kaikki ratkaisuusi liittyvät lähdekoodit sekä mahdollinen `package.json` erillisinä tiedostoina Teamsiin ennen seuraavaa oppituntia. 

**Nimeä `.js`-päätteiset tiedostot `.js.txt`-päätteisiksi, mikäli Teams ei hyväksy tiedostojasi tietoturvasyistä.**

