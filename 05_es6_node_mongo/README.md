# ES6, JavaScript, node (+mongo)

Opintojen tässä vaiheessa olette käyttäneet JavaScriptiä useissa eri tilanteissa. Tämän oppitunnin tarkoituksena on esitellä JavaScript-kielen taustalla olevan ECMAScript-standardin versiossa 6 mukaan tulleita ominaisuuksia käytännössä.

JavaScriptillä voidaan soveltaa monia erilaisia ohjelmointityylejä. Se onkin ns. monen paradigman kieli. Voit siis soveltaa sekä olio-ohjelmointia että esimerkiksi funktionaalista ohjelmointia. Tämän kurssin aikana perehdymme JavaScriptin funktionaaliseen puoleen ja erityisesti funktioihin `map`, `filter` ja `reduce`.

## Oppitunnin tavoitteet

Oppitunnin tavoitteena on oppia erityisesti lukemaan koodia ja ymmärtämään miten yleisimmät JavaScript-kieliset esimerkkikoodit toimivat. Sivuamme funktionaalista ohjelmointia hyödyntämällä funktioiden vaiheittaista suorittamista (currying) ja funktioiden antamista parametreina toisille funktioille.

ES6:n ajoittain erikoiset syntaksit tekevät usein koodista suoraviivaista, mutta toisinaan syntaksien liikakäyttö väärissä tilanteissa hankaloittaa koodin ymmärtämistä ja ylläpitoa. Tämän tunnin jälkeen tunnistat joitakin tilanteita, joissa on tarkoituksenmukaista hyödyntää eri ominaisuuksia.


## Ennakkokysymyksiä

Mitä seuraavat esimerkkikoodit tekevät? Mitkä ovat muuttujien arvot ennen näitä rivejä ja näiden rivien jälkeen?

### Array destructuring

```js
let [ first, last ] = name;

// sama kuin
let first = name[0];
let last = name[1];
```
https://javascript.info/destructuring-assignment#array-destructuring

### Object destructuring

```js
let { first, last } = name;

// sama kuin 
let first = name.first;
let last = name.last;
```

```js
const { PI } = Math;

// sama kuin
const PI = Math.PI;
```

https://javascript.info/destructuring-assignment#object-destructuring

### Property value shorthand

```js
let name = { first, last };

// Luo uuden olion kahden olemassa olevan muuttujan arvoilla. Sama kuin:
let name = { first: first, last: last };
```

https://javascript.info/object#property-value-shorthand

### Object destructuring ja Property value shorthand yhdessä

Yhdistämällä kaksi edellistä, voimme luoda esimerkiksi koordinaattipisteen tapahtumaolion sisältä löytyvän `location`-rakenteen avulla:

```js
let point = { lat, lon } = event.location;
```

### Array spread

```js
let data = [ ...colors, 'red', 'green', 'blue', ...fruits, 'apple', 'banana' ];
```
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax


### Object spread

```js
let person = { ...name, hobby: 'Kung-fu' };

// luo uuden olion, jossa on kaikki name-olion attribuutit, ja sen lisäksi hobby-attribuutti
```

> *"copies own enumerable properties from a provided object onto a new object."*
>
> [MDN web docs, Spread syntax (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

### Rest in Object Destructuring

```js
let { name, ...theRest } = person;

// theRest sisältää kaikki arvot, paitsi ne, jotka poimittiin person-oliosta nimen perusteella
```

> *"Rest properties collect the remaining own enumerable property keys that are not already picked off by the destructuring pattern."*
>
> [MDN web docs, Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

### Nuolifunktiot

```js
let multiply = (a, b) => a * b;

// sama kuin:
function multiply(a, b) {
    return a * b;
}
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

### Currying

```js
let multiply = (a) => (b) => a * b;

// sama kuin:
function multiply(a) {
    return function(b) {
        return a * b;
    }
}
```

Milloin funktioiden osittaisesta määrittelystä olisi meille hyötyä? Jos haluamme laskea etäisyyden kahden koordinaatin välillä, voimme ensin lukita ensimmäisen koordinaattipisteen, ja sen jälkeen käyttää palautettua funktiota yhdellä parametriarvolla!

```js
function getDistanceTo(point) {
    return function (event) {
        return geolib.getDistance(point, event.location);
    }
}

// sama kuin:
let getDistanceTo = (point) => (event) => geolib.getDistance(point, event.location);
```

Funktiota voitaisiin kutsua nyt seuraavasti:

```js
let distance = getDistanceTo(helsinki)(event);
```

"Normaaliin" funktiokutsuun nähden yllä oleva kutsu ei tuo juuri parannusta, se jopa tekee koodista vaikeammin luettavaa. Sen sijaan voimme ottaa ensimmäisen funktion palauttaman funktion talteen, ja kutsua sitä eri yhteydessä:

```js
let distanceToHelsinki = getDistanceTo(helsinki);

events.forEach(event => event.distance = distanceToHelsinki(event));
```

https://javascript.info/currying-partials



# Tapahtumien käsitteleminen `map`, `filter` ja `reduce` -operaatioilla

Tunnilla harjoittelemme `map`, `filter` ja `reduce` -operaatioita [MyHelsinki Open API](http://open-api.myhelsinki.fi/doc) -rajapinnan tapahtumien avulla.

## Esivalmistelu: staattisen aineiston hakeminen

> *curl  is  a tool to transfer data from or to a server, 
> using one of the supported protocols [...].
> The command is designed to work without user interaction.*
>
> `man curl`

curl voidaan asentaa seuraavasti:

    $ sudo apt install curl

`curl`-komennon avulla voimme hakea raakadatan REST-rajapinnasta:

    $ curl http://open-api.myhelsinki.fi/v1/events/

Edellinen komento tulostaa saadun vastauksen suoraan terminaaliin. `python3 -m json.tool` auttaa muotoilemaan JSON-merkkijonot oikein sisennetyiksi merkkijonoiksi:

    $ curl http://open-api.myhelsinki.fi/v1/events/ | python3 -m json.tool

Nyt saimme terminaaliin siistimmin jäsennellyn JSON-tietorakenteen. Voimme ohjata saamamme tulosteet tiedostoksi `>`-operaatiolla seuraavasti:

    $ curl http://open-api.myhelsinki.fi/v1/events/ | python3 -m json.tool > events.json

Huom! `events.json` on iso tiedosto, luokkaa 6-7 megatavua, joten sen käsitteleminen tekstieditorilla on melko raskasta.

## Tapahtuma JSON:in tuominen Node REPL:iin (Read-Evaluate-Print-Loop)

Ilman npm:ää. Ilman riippuvuuksia:

```js
$ node
> let jsonFile = require('./events.json')
> let events = jsonFile['data']
> events.length
5527
```

`events` sisältää nyt meille aikaisemmilta viikoilta tutun listan tapahtumista. Tällä kertaa tapahtumat ovat JavaScript-olioita. Niillä on täysin sama rakenne kuin aikaisemmilla Pythonin sanakirjoilla:

```js
> // alkamispäivän tarkastaminen satunnaiselta tapahtumalta
> let e = events[2500]
> e['event_dates']['starting_day']
'2020-10-23T07:00:00.000Z'
>
> // JavaScriptillä luonnollisempi tapa käsitellä sisäkkäisiä 
> // rakenteita on pistenotaatio:
> e.event_dates.starting_day
'2020-10-23T07:00:00.000Z'
>
> // vertailu johonkin muuhun päivämäärään 
> e.event_dates.starting_day > '2020-10-07T00:00:00.000Z'
true
```

## Filter-metodi

```js
> // filter luo uuden listan, jolle valitaan alkuperäiseltä listalta 
> // sellaiset arvot, joille antamamme funktio palauttaa `true`:
> let allTrue = events.filter(e => true);
> allTrue.length
5527 // kaikki valittiin!
> 
> // vastaavasti jos palautetaan false:
> let allFalse = events.filter(e => false);
> allFalse.length
0 // mitään ei valittu!
>
> // valitaan päivämäärän mukaan!
> let now = new Date().toISOString()
> now
'2020-10-09T10:47:00.111Z'
>
> let nextWeek = '2020-10-16T10:47:00.111Z';
```

Seuraavaksi halutaan rajata tapahtumat, joilla on alkuaika, ja joilla se sijoittuu kahden ajankohdan väliin:

```js
> // Tapahtumat, joilla on alkuaika, ja se sijoittuu kahden ajankohdan väliin:
> let eventsNextWeek = events
    .filter(e => e.event_dates.starting_day != null)
    .filter(e => e.event_dates.starting_day >= now)
    .filter(e => e.event_dates.starting_day <= nextWeek)
>
> eventsNextWeek.length
612 // enää 612 tapahtumaa!
```

Miten voisimme siistiä koodia siten, että yllä oleva koodi ei tekisi kolmea filtteriä eikä sääntöjä kirjoitettaisin filter-metodin sisään? Tätä varten voimme kirjoittaa filtteröintifunktion erilleen filtteröinnistä!

```js
function isBetweenDates(event) {
    let { starting_day } = event.event_dates;
    return starting_day != null && starting_day >= now && starting_day <= nextWeek;
}
```

Nyt `isBetweenDates` voidaan antaa parametrina `filter`-operaatiolle:

```js
> // huom! isBetweenDates-funktiota ei kutsuta heti, vaan se annetaan parametrina.
> // Filter-metodi huolehtii antamamme funktion kutsumisesta.
> let eventsNextWeek = events.filter(isBetweenDates)
> eventsNextWeek.length
612
```

Yllä olevassa koodissa `isBetweenDates` on "kovakoodattu" vertailemaan tapahtuman alkuaikaa aina samoihin arvoihin `now` ja `nextWeek`. Olisikin paljon parempi, jos voisimme määritellä funktion kahdessa vaiheessa: ensin annetaan päivämäärät, ja sen jälkeen vertaillaan tapahtumaa:

```js
function isBetweenDates(minDate, maxDate) {
    return function (event) {
        let { starting_day } = event.event_dates;
        return starting_day && minDate <= starting_day && starting_day <= maxDate;
    }
}
```

Tämän funktion avulla voimme ensin luoda filtterin `isNextWeek`, joka annetaan `filter`-operaatiolle. Filter kutsuu ajonaikaisesti luotua `isNextWeek`-funktiota jokaiselle tapahtumalla, ja valikoi uudelle `eventsNextWeek`-listalle ehdot täyttävät tapahtumat:

```js
let isNextWeek = isBetweenDates('2020-10-09T00:00:00', '2020-10-16T24:00:00');
let eventsNextWeek = events.filter(isNextWeek);
```

## Funktion parametrien oletusarvot

JavaScriptin uusimmilla versioilla voimme antaa parametreille oletusarvot, joita käytetään, mikäli funktion kutsussa on jätetty parametriarvo antamatta tai sen arvo on `undefined`:

```js
function isBetweenDates(minDate = '0000-01-01', maxDate = '9999-12-31') {
    return function (event) {
        let { starting_day } = event.event_dates;
        return starting_day && minDate <= starting_day && starting_day <= maxDate;
    }
}
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters



## Map 

> *The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.*
>
> [MDN web docs. Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

Tässä esimerkissä luomme tapahtumia sisältävän listan perusteella uuden, pelkät `id`-arvot sisältävän listan:

```js
> // map:lle annettava funktio palauttaa jokaista tapahtumaa kohden sen id-arvon:
> let ids = events.map(event => event.id)
> ids
[ 'helmet:214000', 'helmet:216844', 'helmet:216842', 'helmet:211890', 'helmet:214001', ... ]
```

### Etäisyyden lisääminen kaikille tapahtumille

Toinen, selvästi hyödyllisempi käyttötapaus voisi olla etäisyyden lisääminen tapahtuman tietoihin `map`-operaatiolla:

```js
const geolib = require('geolib');

const helsinkiCoordinates = { lat: 60.1733244, lon: 24.9410248 };

let eventsWithDistance = events.map(event => {
    let eventCoordinates = { lat, lon } = event.location;
    return {
        ...event, // kopioidaan tapahtuman tiedot palautettavaan olioon
        distance: geolib.getDistance(helsinkiCoordinates, eventCoordinates)
    }
});
```

Huomaa, että yllä oleva koodi ei muuta alkuperäistä `events`-taulukkoa eikä sillä olevia olioita, vaan se luo uuden listan, joka täytetään kopioilla tapahtumista.

Jotta sijainti olisi helposti vaihdettavissa myös joksikin muuksi kuin Helsingiksi, kannattaa tässäkin tapauksessa etäisyydet lisäävä funktio määritellä kahdessa osassa:

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


## Tapahtumien järjestäminen: Array.sort

> *"The sort() method sorts the elements of an array in place and returns the sorted array."*
>
> *"If compareFunction is supplied, all non-undefined array elements are sorted according to the return value of the compare function. If compareFunction(a, b) returns less than 0, sort a to an index lower than b (i.e. a comes first). If compareFunction(a, b) returns 0, leave a and b unchanged with respect to each other, but sorted with respect to all different elements."*
>
> [MDN web docs. Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

### Järjestäminen etäisyyden mukaan

Kun tapahtumille on lisätty uusi attribuutti `distance`, voidaan tätä käyttää hyväksi myös tapahtumien järjestämisessä etäisyyden mukaan:

```js
eventsWithDistances.sort((event1, event2) => event1.distance - event2.distance);
```

### Järjestäminen alkamisajan mukaan

Vastaavasti voimme vertailla alkamisaikoja ja järjestää tapahtumat alkamisajan mukaan järjestykseen alkamisajankohtia vertailevalla funktiolla:

```js
function eventDateComparator(event1, event2) {
    let event1date = event1.event_dates.starting_day || '';
    let event2date = event2.event_dates.starting_day || '';

    return event1date.localeCompare(event2date);
}

events.sort(eventDateComparator);
```

## Fetch ja Promiset

Asynkroniset fetch- ja json-kutsut palauttavat Promise-oliota. Promise-olion tapahtumankuuntelija asetetaan kutsumalla Promisen then-metodia ja antamalla sille callback-funktio. Peräkkäisiä Promise-oliota voidaan myös ketjuttaa seuraavasti, jolloin ensimmäisenä Promisen then-metodille annettu funktio suoritetaan aina ennen seuraavia kutsuja, ja edellisen then-kuuntelijan palauttama arvo välitetään parametrina seuraavalle kuuntelijalle:

## Yksikkötestaus JavaScriptillä



RxJS esimerkin koodaaminen promiseilla? https://stackblitz.com/edit/rxjs-type-ahead?file=index.ts


https://github.com/Team-RyTy/tapahtuma-info/blob/master/components/Eventlist.js

https://github.com/Team-RyTy/tapahtuma-info/blob/master/components/Restaurants.js

Babel : ES6 importit yms?

https://babeljs.io/repl

Geolokaatio : Geolib

# Koodin lukeminen

Yksi tämän oppitunnin tavoitteista on oppia lukemaan koodia. Esimerkkejä seuraamalla ja kopioimalla saamme toteutettua logiikkaa, mutta emme aina välttämättä ymmärrä kaikkia ohjelmointirakenteita omassa koodissamme. Mitä esimerkiksi seuraavassa esimerkissä olevat kaksi kohtaa tarkoittavat? Miten kertoisit sanallisesti, mitä riveillä tapahtuu? Osaisitko kirjoittaa samat rivit "perinteisempään" muotoon?

```javascript
// https://nodejs.org/api/modules.html#modules_modules_commonjs_modules
const { PI } = Math; // mitä tämä tarkoittaa?

exports.area = (r) => PI * r ** 2; // mitä tämä tarkoittaa?

exports.circumference = (r) => 2 * PI * r;
```

# JavaScription vertailuoperaatiot


### Vertailu kahdella yhtäsuuruusmerkillä

```js
> "0" == false  // nolla merkkijonona ja false
true
> [] == false   // tyjä lista ja false
true
> 0 == false    // nolla ja false
true
> 0 == "0"      // nolla merkkijonona ja nolla
true
> 0 == "+00000" // "pitkä nolla" etumerkillä merkkijonona
true
> 0 == []       // nolla ja tyhjä lista
true
> "0" == []     // molemmat false, mutta silti keskenään erisuuruiset!!
false
```

### Vertailu kolmella yhtäsuuruusmerkillä

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

### Listojen vertailu

Listoja vertailtaessa `==` ja `===` molemmat tarkastavat, onko kyseessä sama lista. __Listojen sisältöjä ei vertailla.__

```js
> [1, 2, 3] === [1, 2, 3]
false
> [1, 2, 3] == [1, 2, 3]
false
```

### Olioiden vertailu

Kuten listoilla, myös olioita vertailtaessa tarkastetaan ovatko oliot **samat**, eikä niiden sisältöä vertailla.

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
assert.deepStrictEqual([1, 2, 3], [1, 2, 3])
assert.deepStrictEqual({ language: "JavaScript" }, { language: "JavaScript" 
```

https://nodejs.org/api/assert.html#assert_assert_deepstrictequal_actual_expected_message

# Array spread

```js
> let a = [1, 2, 3]
> let b = [4, 5, 6]
> [...a, ...b]
[ 1, 2, 3, 4, 5, 6 ]
> [...a, ...b, 7, 8, 9]
[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
```

# Array destructuring

```js
> let [first, second, third, ...rest] = [1, 2, 3, 4, 5, 6, 7]
> first
1
> second
2
> third
3
> rest
[ 4, 5, 6, 7 ]
```

# Object methods

Object.keys() https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys

Object.values() https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values

# Object initializer

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer

```js
const a = 'foo';
const b = 42;
const c = {};
const object2 = { a: a, b: b, c: c };
const object3 = { a, b, c };
```

# Object spread ja destructuring

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment:

```js
const user = {
    id: 42,
    is_verified: true
};

const {id, is_verified} = user;
```

```js
> const user = {name: 'Teemu', id: 42};
>
> const userWithPosts = { ...user, posts: [] }
{ name: 'Teemu', id: 42, posts: [] }
```


# Filter



# "Currying" eli funktion kutsumien osissa

`isNextWeek` on hyvä funktio, mutta se on sidottu "globaaleihin" arvoihin `now` ja `maxDate`. Kyseiset arvot voitaisiin toki laskea myös tässä funktiossa, mutta mitä jos tarvitsemme samassa ohjelmassa logiikan kuukauden sisällä filtteröintiin?

Voimme kirjoittaa funktion, joka palauttaa funktion! https://javascript.info/currying-partials

```js
// source: https://blog.bitsrc.io/understanding-currying-in-javascript-ceb2188c339
function multiply(a, b, c) {
    return a * b * c;
}
multiply(1,2,3); // 6
```
Voidaan siis kirjoittaa muotoon:

```js
// source: https://blog.bitsrc.io/understanding-currying-in-javascript-ceb2188c339
function multiply(a) {
    return (b) => {
        return (c) => {
            return a * b * c
        }
    }
}
log(multiply(1)(2)(3)) // 6
```

`isNextWeek` voidaan siis toteuttaa myös funktiolla, joka palauttaa funktion:

```js
function createDateFilter(min, max) {
    return function(event) {
        let day = event.event_dates.starting_day; 
        return day != null && day >= min && day <= max;
    }
}
```

Nyt kutsutaan siis ensin `createDateFilter`-funktiota kahdella päivämäärällä, ja tämän palauttamaa uutta funktiota kutsutaan tapahtumaoliolla:

```js
createDateFilter(now, maxDate)(events[100])
> false
```

Miksi tämä on hyödyllistä?

```js
> let nextWeekFilter = createDateFilter(now, nextWeek)
> let nextMonthFilter = createDateFilter(now, nextMonth)
> // jne.
>
> let nextWeekEvents = events.filter(nextWeekFilter)
> nextWeekEvents.length
612
```

# Map

```js
> // Luodaan uusi lista, jossa on vain tapahtumien id:t
> let ids = events.map(event => event.id)
> ids.slice(0, 10)
[ 'helmet:214000',
  'helmet:216844',
  'helmet:216842',
  'helmet:211890',
  'helmet:214001',
  'helmet:216843',
  'helmet:211891',
  'helmet:211896',
  'helmet:211889',
  'helmet:212889' ]

```

Käydään tapahtumia läpi ja logitetaan


# Filter -> Map -> Reduce

filter, map ja reduce löytyvät suurimmasta osasta ohjelmointikieliä, mukaan lukien Java, Python ja JavaScript.

```js
> let ids = events.map(event => event.id)
```

Kirjoitetaan operaatiot eri moduuliin kuin mitä suoritetaan!

https://medium.com/poka-techblog/simplify-your-javascript-use-map-reduce-and-filter-bd02c593cc2d

Filtteröidään päivämäärien mukaan, tagien mukaan jne.

Mäpätään tapahtumien nimiin?

Etsitään jokin redusoitava asia tapahtumista?

Ketjutetaan ja rajoitetaan määrä: `slice()`

Reducella voidaan vaikka koota tapahtumat tagien mukaan!


# JSON ja Noden http-serveri

Tarjoillaan redusoitu data HTTP:n yli selaimelle.


# Pakettien asennus / npm init

npm init...

## node-fetch

Asennetaan fetch ja haetaan data oikeasta rajapinnasta -> asynkronisuus!

## Async / await

Tarvitaan monta eri endpointtia ja parametreja: lisätään Express

## Halutaan filtteröidä etäisyyden mukaan ja näyttää etäisyys annettuun pisteeseen:

Lisätään `geolib`. Käytetään ...event -syntaksia mäppäyksessä.

Ehkä käytetään currying? `getDistance(point1, point2) => getDistance(point1)(point2)`


# Tehtävä

Toteuta JavaScriptillä HTTP-palvelu, joka hakee REST-rajapinnasta käyttäjiä ja postauksia, ja palauttaa käyttäjät siten, että kunkin käyttäjän kirjoittamat postaukset ovat listattu käyttäjän yhteyteen.

> *"{JSON} Placeholder*
>
> *Free to use fake Online REST API for testing and prototyping*
>
> *Powered by JSON Server + LowDB"*
>
> https://jsonplaceholder.typicode.com/

Data tulee hakea dynaamisesti (ei etukäteen) seuraavista osoitteista:

* käyttäjät: https://jsonplaceholder.typicode.com/users
* postaukset: https://jsonplaceholder.typicode.com/posts

Saat itse valita, palauttaako HTTP-palvelusi datan JSON-muodossa (helpointa) vai muodostatko datan perusteella HTML-sivun esimerkiksi pug-templaten avulla.

Lopputuloksena palvelusi tulee palauttaa lista käyttäjistä, jossa kunkin käyttäjän postaukset ovat ryhmiteltynä käyttäjän alle listaksi. Yksittäisen käyttäjän osalta lopputulos voi olla esimerkiksi seuraava:

```json
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
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
            },
            {
                "userId": 1,
                "id": 4,
                "title": "eum et est occaecati",
                "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
            },
            {
                "userId": 1,
                "id": 5,
                "title": "nesciunt quas odio",
                "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
            },
            {
                "userId": 1,
                "id": 6,
                "title": "dolorem eum magni eos aperiam quia",
                "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
            },
            {
                "userId": 1,
                "id": 7,
                "title": "magnam facilis autem",
                "body": "dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas"
            },
            {
                "userId": 1,
                "id": 8,
                "title": "dolorem dolore est ipsam",
                "body": "dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae"
            },
            {
                "userId": 1,
                "id": 9,
                "title": "nesciunt iure omnis dolorem tempora et accusantium",
                "body": "consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas"
            },
            {
                "userId": 1,
                "id": 10,
                "title": "optio molestias id quia eum",
                "body": "quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error"
            }
        ]
    }
]
```

Tämän tehtävän ratkaisemiseksi et tarvitse välttämättä ulkoisia kirjastoja tai `npm`-komentoa. Pelkkä Node.js voi riittää. Sinulle saattaa kuitenkin olla hyötyä kirjastoista, kuten express, axios tai node-fetch.

Koska HTTP-pyynnöt ovat JavaScriptissä asynkronisia, JSON-tiedostojen lataaminen voidaan tehdä samanaikaisesti tai yksi kerrallaan. Tämän tehtävän kannalta ei ole merkitystä kumman tavan valitset, mutta harjoituksen vuoksi suosittelen pyrkimään lataamaan tiedostot samanaikaisesti. Tähän ei tarvita erillisiä työkaluja, mutta `Promise.all`-funktiosta voi olla apua.

Vinkki: Käyttäjien ja heidän postauksiensa yhdistämiseksi yksi lähestymistapa on käydä käyttäjät läpi `map`-metodilla ja muodostaa jokaisesta käyttäjästä uusi olio, jolla on lista postauksia. Postauslista puolestaan voidaan rakentaa kullekin käyttäjälle `filter`-metodin avulla, valitsemalla listalta ne postaukset, joiden `userId` vastaa kyseisen käyttäjän `id`:tä.

Vaihtoehtoisesti voit myös ratkaista tehtävän täysin ilman `map`, `filter`, `reduce` yms. ES6-metodeja perinteisillä ehto- ja  toistorakenteilla. Oppimisen kannalta suosittelemme kuitenkin tutustumaan tunnilla esitettyihin ratkaisutapoihin.

Palauta kaikki ratkaisuusi liittyvät lähdekoodit sekä mahdollinen `package.json` erillisinä tiedostoina Teamsiin ennen seuraavaa oppituntia. Nimeä `.js`-päätteiset tiedostot `.js.txt`-päätteisiksi, mikäli Teams ei hyväksy tiedostojasi tietoturvasyistä.

