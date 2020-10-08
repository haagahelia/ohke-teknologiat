# ES6, JavaScript, node (+MongoDB)

- [ES6, JavaScript, node (+MongoDB)](#es6-javascript-node-mongodb)
  - [Oppitunnin tavoitteet](#oppitunnin-tavoitteet)
  - [JavaScriptin ohjelmointityylit](#javascriptin-ohjelmointityylit)
  - [Uusien ominaisuuksien selaintuki](#uusien-ominaisuuksien-selaintuki)
  - [ES6](#es6)
  - [Muut tunnilla käsiteltävät tekniikat](#muut-tunnilla-käsiteltävät-tekniikat)
- [Tapahtumien käsitteleminen `map`, `filter` ja `reduce` -operaatioilla](#tapahtumien-käsitteleminen-map-filter-ja-reduce--operaatioilla)
  - [Esivalmistelu: staattisen aineiston hakeminen](#esivalmistelu-staattisen-aineiston-hakeminen)
  - [Tapahtuma JSON:in tuominen Node REPL:iin (Read-Evaluate-Print-Loop)](#tapahtuma-jsonin-tuominen-node-repliin-read-evaluate-print-loop)
  - [Filter-metodi](#filter-metodi)
  - [Map](#map)
  - [Express-harjoitus](#express-harjoitus)
  - [Fetch, Promiset, async ja await](#fetch-promiset-async-ja-await)
  - [Fetch-harjoitus](#fetch-harjoitus)
  - [Reduce](#reduce)
  - [Bonus: JavaScriptin totuusarvot ja niiden vertailu](#bonus-javascriptin-totuusarvot-ja-niiden-vertailu)
- [Tehtävä](#tehtävä)
  - [Tehtävän data](#tehtävän-data)
  - [Valmiiden kirjastojen käyttäminen](#valmiiden-kirjastojen-käyttäminen)
  - [Pyyntöjen samanaikaisuus](#pyyntöjen-samanaikaisuus)
  - [Vinkit datan käsittelyyn](#vinkit-datan-käsittelyyn)
  - [Tehtävän palauttaminen](#tehtävän-palauttaminen)

## Alkusanat

Opintojen tässä vaiheessa olette käyttäneet JavaScriptiä eri kursseilla ja useissa useissa eri tilanteissa. JavaScriptiä on melko suoraviivaista "käyttää" ilman varsinaista ymmärrystä siitä, miten ohjeissa esitetyt syntaksit oikeasti toimivat.

JavaScript-projekteissa käytetään usein erilaisia kielen natiiviominaisuuksiin kuulumattomia ominaisuuksia, kuten JSX-syntaksia:

```jsx
// https://reactjs.org/docs/introducing-jsx.html
const element = <h1>Hello, world!</h1>;

// Sama koodi muutettuna JavaScriptiksi https://babeljs.io/repl-työkalulla:
var element = React.createElement("h1", null, "Hello, world!");
```

Kaikki koodi, joka kirjoitetaan JavaScriptillä, ei siis ole välttämättä suoraan suoritettavissa ilman erilaisia käännösvaiheita. Kääntäminen tehdään usein taustalla [Babel](http://babeljs.io/)-työkalulla, joka muuttaa esimerkiksi yllä olevan JSX-koodin tavallisiksi JavaScript-rakenteiksi. Samoin Babel osaa muuntaa JavaScriptin modernimmilla versioilla toteutetut syntaksit vanhempien selainten tukemaan muotoon. Muunnoksista johtuen voi joskus olla haastavaa hahmottaa, mitkä asiat ovat "natiivi JavaScriptiä" ja mitkä eri kirjastoihin tai ohjelmistokehyksiin liittyviä ominaisuuksia.

Aiheessa esiintyvä MongoDB-tietokanta ei ole osa oppitunnin sisältöä eikä oppituntiin liittyvää kotitehtävää, vaan osa tämän aihealueen seminaariosuutta.


## Oppitunnin tavoitteet

Oppitunnin tavoitteena on oppia erityisesti lukemaan koodia ja ymmärtämään, miten yleisimmät JavaScript-kieliset esimerkkikoodit toimivat. Sivuamme funktionaalista ohjelmointia hyödyntämällä funktioiden antamista parametreina toisille funktioille (callback) sekä funktioiden vaiheittaista suorittamista (currying).

ES6:n ajoittain erikoiset syntaksit tekevät usein koodista suoraviivaista, mutta toisinaan syntaksien liikakäyttö väärissä tilanteissa hankaloittaa koodin ymmärtämistä ja ylläpitoa. Tämän tunnin jälkeen tunnistat joitakin tilanteita, joissa on tarkoituksenmukaista hyödyntää eri ominaisuuksia.

Itseopiskelumateriaalina voit hyödyntää hyviä sivustoja kuten:

* https://javascript.info/
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/
* https://medium.com/poka-techblog/simplify-your-javascript-use-map-reduce-and-filter-bd02c593cc2d


## JavaScriptin ohjelmointityylit

JavaScriptillä voidaan soveltaa monia erilaisia ohjelmointityylejä, eli se on monen paradigman kieli. Voit siis soveltaa JavaScriptillä olio-ohjelmointia tai funktionaataulukko ohjelmointia tai halutessasi sekoittaa niitä. Monipuolisuuden heikkoutena JavaScriptillä ei aina ole yhtä vahvoja "parhaita käytäntöjä" kuin yhden paradigman kielillä. Tämän oppitunnin aikana perehdymme erityisesti JavaScriptin funktionaaliseen puoleen: nuolifunktioihin sekä map-, filter- ja reduce-operaatioihin.


## Uusien ominaisuuksien selaintuki

Erityisesti verkkoselaimella käytettävien sovellusten kehittämisessä on huomioitava vaihtelevat suoritusympäristöt, joissa selain joko tukee tai ei tue kirjoittamaasi koodia. Selaintuki on perinteisesti ollut merkittävä ongelma, koska JavaScript on jaeltu selaimille suoritettavaksi sellaisenaan. Nykyään selainyhteensopivuus ei ole yhtä merkittävä ongelma, koska myös selaimelle tarkoitettu koodi usein "transpiloidaan", jolloin esimerkiksi koodi:

```js
let { first, last } = names;
```

Muuttuu automaattisesti paremmin tuettuun muotoon:

```js
var _names = names,
  first = _names.first,
  last = _names.last;
```


## ES6

Tämän oppitunnin tarkoituksena on esitellä JavaScript-kielen taustalla olevan ECMAScript-standardin versiossa 6 mukaan tulleita ominaisuuksia käytännössä ja pohtia esimerkkien avulla, miten uusi syntaksi voi hyödyttää meitä "oikeassa ohjelmassa".

Syntaksien opetteleminen on tärkeää lähinnä siksi, että ymmärrät kohtaamiasi esimerkkikoodeja ja käyttämiäsi valmiita koodipohjia. Koodin "modernisointi" on muuten usein toisarvoista.


### Array destructuring

> *"Destructuring assignment is a special syntax that allows us to “unpack” arrays or objects into a bunch of variables, as sometimes that’s more convenient. Destructuring also works great with complex functions that have a lot of parameters, default values, and so on."*
>
> [Kantor, I. Destructuring assignment. JavaScript.info](https://javascript.info/destructuring-assignment#array-destructuring)

```js
let [ first, last ] = names;

// sama kuin
let first = names[0];
let last = names[1];
```


### Object destructuring

> *"We have an existing object at the right side, that we want to split into variables. The left side contains a “pattern” for corresponding properties. In the simple case, that’s a list of variable names in {...}."*
>
> [Kantor, I. Object destructuring. JavaScript.info](https://javascript.info/destructuring-assignment#object-destructuring)


```js
let { first, last } = names;

// sama kuin
let first = names.first;
let last = names.last;
```

Destructuring on usein käytössä myös silloin, kun valitsemme jostain riippuvuudesta tietyt arvot tai funktiot käytettäväksi omassa koodissamme:

```js
const { PI } = Math;

// sama kuin
const PI = Math.PI;
```

### Property value shorthand

> *"The use-case of making a property from a variable is so common, that there’s a special property value shorthand to make it shorter."*
>
> [Kantor, I. Property value shorthand. JavaScript.info](https://javascript.info/object#property-value-shorthand)


```js
let first = 'Chuck';
let last = 'Norris';

let names = { first, last };

// Luo uuden olion kahden olemassa olevan muuttujan arvoilla. Sama kuin:
let names = { first: first, last: last };
```


### Object destructuring ja Property value shorthand yhdessä

Yhdistämällä kaksi edellistä, voimme luoda esimerkiksi koordinaattipisteen tapahtumaolion sisältä löytyvän `location`-rakenteen avulla:

```js
let point = { lat, lon } = event.location;

// sama kuin
let point = {
    lat: event.location.lat,
    lon: event.location.lon
};
```

### Array spread

> *"Spread syntax (...) allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected."*
>
> [MDN web docs, Spread syntax (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)


```js
> let a = [1, 2, 3]
> let b = [4, 5, 6]
>
> [...a, ...b]
[ 1, 2, 3, 4, 5, 6 ]
>
> [...a, ...b, 7, 8, 9]
[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
```


https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax


### Object spread

> *"copies own enumerable properties from a provided object onto a new object."*
>
> [MDN web docs, Spread syntax (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

Samankaltainen kuin taulukoiden spread-operaatio, mutta olioille sovellettuna:

```js
let person = { ...names, hobby: 'Kung-fu' };

// luo uuden olion, jossa on kaikki names-olion attribuutit, 
// ja sen lisäksi hobby-attribuutti.

// sama kuin:
let person = Object.assign({}, names);
person.hobby = 'Kung-fu';
```


### Rest in Object Destructuring


> *"Rest properties collect the remaining own enumerable property keys that are not already picked off by the destructuring pattern."*
>
> [MDN web docs, Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

```js
let { name, description, ...theRest } = event;

// theRest sisältää kaikki arvot, paitsi ne, jotka poimittiin event-oliosta attribuuttien nimien perusteella
```

## Muut tunnilla käsiteltävät tekniikat

### Nuolifunktiot

> *"An arrow function expression is a compact alternative to a traditional function expression, but is limited and can't be used in all situations."*
>
> [MDN web docs, Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

Nuolifunktioiden kaltaiset anonyymit funktiot ovat yleisiä myös muissa kielissä, kuten Javassa ja Pythonissa. Niissä funktioita kutsutaan "lambdoiksi".

Funktion määrittelystä voidaan nuolifunktioiden avulla jättää pois sana `function` sekä, mikäli funktiossa on vain yksi lauseke, myös `return`-avainsana:

```js
let multiply = (a, b) => a * b;

// sama kuin:
function multiply(a, b) {
    return a * b;
}
```

### Currying

Eräs JavaScriptin yhteydessä kasvavassa määrin hyödynnetty tekniikka, joka ei suoraan liity pelkästään ES6:een tai vain JavaScriptiin on "currying":

> *"Currying is an advanced technique of working with functions. It’s used not only in JavaScript, but in other languages as well.*
>
> *Currying is a transformation of functions that translates a function from callable as f(a, b, c) into callable as f(a)(b)(c)."*
>
> [Kantor, I. Currying. JavaScript.info](https://javascript.info/currying-partials)

Currying-tekniikalla voimme siis pilkkoa useita parametreja sisältäviä funktioita siten, että yksittäisellä funktiokutsulla sidotaan yksi muuttuja. Funktiot palauttavat uusia funktioita, jotka voidaan ottaa tarvittaessa talteen ja kutsua muualla. 

Kutsuessamme toista funktiota, ensimmäisessä funktiokutsussa annetut parametrit ovat edelleen voimassa, koska ne ovat saman "sulkeuman" sisällä:

```js
function multiply(a) {
    return function(b) {
        // tässä funktiossa on voimassa sekä ensin annettu 
        // 'a' että tälle funktiolle annettava 'b'.
        return a * b;
    }
}

// yllä oleva määrittely on sama kuin:
let multiply = (a) => (b) => a * b;

// suoritetaan ensimmäinen funktio kahteen kertaan
// ja otetaan palautetut funktiot talteen:
let sentitTuumiksi = multiply(0.393700787);
let markatEuroiksi = multiply(0.16818792646);

// nyt palautettuja funktioita voidaan hyödyntää uusissa kutsuissa:
let tuumat = sentitTuumiksi(200);
let eurot = markatEuroiksi(100);
```

Milloin funktioiden osittaisesta määrittelystä on meille erityisesti hyötyä?

"Currytetty" funktio voidaan antaa suoraan esimerkiksi `map`-funktiolle, joista kerromme lisää myöhemmin tässä materiaalissa:

```js
let markat = [200, 123, 99, 10, 4521];
let eurot = markat.map(markatEuroiksi);
```

# Tapahtumien käsitteleminen `map`, `filter` ja `reduce` -operaatioilla

Tunnilla harjoittelemme `map`, `filter` ja `reduce` -operaatioita [MyHelsinki Open API](http://open-api.myhelsinki.fi/doc) -rajapinnan tapahtumien avulla. `filter`, `map` ja `reduce` löytyvät suurimmasta osasta ohjelmointikieliä, mukaan lukien Java, Python ja JavaScript.


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

`events` sisältää nyt meille aikaisemmilta viikoilta tutun taulukon tapahtumista. Tällä kertaa tapahtumat ovat JavaScript-olioita. Niillä on täysin sama rakenne kuin aikaisemmilla Pythonin sanakirjoilla:

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
> // filter luo uuden taulukon, jolle valitaan alkuperäiseltä taulukolta 
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

Tämän `isBetweenDates`-funktion avulla voimme ensin luoda uuden funktion `isNextWeek`:

```js
let isNextWeek = isBetweenDates('2020-10-09T00:00:00', '2020-10-16T24:00:00');
```

Kun `isNextWeek` annetaan `filter`-operaatiolle, filter kutsuu antamaamme `isNextWeek`-funktiota jokaiselle tapahtumalle ja valikoi uudelle `eventsNextWeek`-taulukkolle ne tapahtumat, joille `isNextWeek` palauttaa arvon `true`:

```js
let eventsNextWeek = events.filter(isNextWeek);
```

Nyt melko monimutkainen operaatio, joka edellyttäisi perinteisesti taulukon luomisen, toistorakenteen, ehtorakenteen ja taulukkoon lisäykset, saadaan toteutettua suoraviivaisesti.


### Funktioiden parametrien oletusarvot

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

### Järjestäminen alkamisajan mukaan

JavaScriptin taulukoilla on valmis `sort`-metodi, jonka avulla sen sisältö voidaan järjestää. Tarvitset vain vertailufunktion, joka vertailee kahta tapahtumaa, ja kertoo kumman tulisi olla järjestyksessä ensimmäisenä:

> *"The sort() method sorts the elements of an array in place and returns the sorted array."*
>
> *"If compareFunction is supplied, all non-undefined array elements are sorted according to the return value of the compare function. If compareFunction(a, b) returns less than 0, sort a to an index lower than b (i.e. a comes first). If compareFunction(a, b) returns 0, leave a and b unchanged with respect to each other, but sorted with respect to all different elements."*
>
> [MDN web docs. Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

Voimme vertailla alkamisaikoja ja järjestää tapahtumat alkamisajan mukaan järjestykseen alkamisajankohtia vertailevalla funktiolla:

```js
function eventDateComparator(event1, event2) {
    // jos starting_day on undefined, käytetään tyhjää merkkijonoa:
    let event1date = event1.event_dates.starting_day || '';
    let event2date = event2.event_dates.starting_day || '';

    // Palauttaa negatiivisen luvun, nollan tai positiivisen luvun riippuen merkkijonojen aakkosjärjestyksestä.
    // Tämä toimii, koska starting_day on aina ISO-muotoinen String, kuten "2020-10-16T24:00:00".
    return event1date.localeCompare(event2date);
}

events.sort(eventDateComparator);
```

----

## Express-harjoitus

Miten voisimme hyödyntää toteuttamaamme logiikkaa osana verkkopalvelua? Nodelle on olemassa useita web-sovelluskehyksiä, joista *express* on hyvin suosittu:

> *"Fast, unopinionated, minimalist web framework for node."*
>
> https://www.npmjs.com/package/express

Asennetaan express seuraavasti:

```
$ npm install express --save
```

Liitetään tapahtumien näyttäminen osaksi Expressin esimerkkisovellusta. Tarvoitteemme on, että palvelimemme vastaa pyyntöihin JSON-rakenteella, joka on rajattu annettujen päivämäärien mukaan ja järjestetty kronologiseen järjestykseen. Lisäominaisuuksina voimme toteuttaa myös "limit"-ominaisuuden tapahtumien määrän rajoittamiseksi.

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
        ...event, // kopioidaan tapahtuman tiedot palautettavaan olioon
        distance: geolib.getDistance(helsinkiCoordinates, eventCoordinates) // lisätään myös distance
    }
});
```

Huomaa, että yllä oleva koodi ei muuta alkuperäistä `events`-taulukkoa eikä sillä olevia olioita, vaan se luo uuden taulukon, joka täytetään kopioilla tapahtumista.


### Currying

Yllä olevassa koodiesimerkissä `map`-operaatiolle annettu funktio on sidottu `helsinkiCoordinates`-muuttujaan. Haluaisimme kuitenkin ohjelmassamme todennäköisesti laskea etäisyyksiä monipuolisesti, joten eri etäisyysfunktiot olisi tarpeen sitoa eri muuttujien arvoihin. 

Voimme ratkaista ongelman soveltaen currying-tekniikkaa! Ensin lukitsemme koordinaattipisteen ja sen jälkeen kutsumme sisempää funktiota tapahtumaolioiden kanssa!


```js
// ensimmäinen funktiokutsu sitoo `point`-muuttujan arvon sulkeumaan:
function getDistanceTo(point) {
    // toista funktiota kutsutaan vain tapahtumaolion kanssa:
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


## Fetch, Promiset, async ja await

Asynkroniset fetch- ja json-kutsut palauttavat Promise-oliota. Promise-olion tapahtumankuuntelija asetetaan kutsumalla Promisen `then`-metodia ja antamalla sille callback-funktio, jota kutsutaan, kun promisen operaatio on valmistunut. Peräkkäisiä Promise-oliota voidaan myös ketjuttaa, jolloin ensimmäisenä Promisen `then`-metodille annettu funktio suoritetaan aina ennen seuraavia kutsuja, ja edeltävän funktion palauttama arvo välitetään aina seuraavalle funktiolle. Tästä käytetään myös termiä "putkitus" eli piping.

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

Tähän asti olemme lukeneet tapahtumien JSON-rakenteen levyltä synkronisesti `require`-funktiolla. Tämä on tapahtunut synkronisesti, eli lukeminen on tehty loppuun ennen seuraavalle riville etenemistä. Tyypillisesti tiedostojen lukeminen, tietokantakyselyt ja http-pyynnöt tapahtuvat kuitenkin asynkronisesti, eli vastausta ei jäädä odottamaan, vaan ohjelman suoritus siirtyy suoraan eteenpäin. Asynkronisten operaatioiden valmistumisen jälkeen niiden tuloksia pystytään hyödyntämään esimerkiksi Promise-olioiden ja then-metodin avulla.

Asennetaan ensin `node-fetch`-niminen paketti, jonka avulla pystymme käyttämään selaimista tuttua `fetch`-funktioita http-pyyntöjen tekemiseen:

> *"node-fetch: a light-weight module that brings window.fetch to Node.js"*
>
> https://www.npmjs.com/package/node-fetch

```
$ npm install node-fetch
```

HTTP-pyyntö voidaan tehdä nyt sovelluksessa seuraavasti:

```js
const fetch = require('node-fetch');

let httpPromise = fetch('http://open-api.myhelsinki.fi/v1/events/');
```

**Tuntidemo asynkronisesta ohjelmoinnista, putkituksesta sekä async/await.***

----

## Reduce

> *"The reduce() method executes a reducer function (that you provide) on each element of the array, resulting in single output value."*
>
> [MDN web docs. Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

Reducen avulla voidaan tyypillisesti selvittää esimerkiksi kokoelman suurin tai pienin arvo, kaikkien arvojen summa tai muita vastaavia operaatioita. Reducen avulla voidaan kuitenkin toteuttaa myös muunlaisia operaatioita, joissa käsitellään yksi kerrallaan kokoelman arvot.

```js
let tulos = taulukko.reduce(( koottuArvo, nykyinenArvo ) => {
    /* operaatio, jonka paluuarvoa käytetään seuraavana koottunaArvona */
    return X;
}, kokoojanAlkuarvo);
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

Kuten kurssin aikaisemmalla oppitunnilla todettiin, JavaScriptissä vertailuoperaatiot tehdään usein kolmella merkillä eli `===` tai `!==`. Kolmen merkin vertailuoperaatiot tarkastavat, että vertailtavien arvojen tyyppi on sama. Mikäli tyyppitarkastus jätetään tekemättä, JavaScript vertailee tyhjiä ja nollaan vertautuvia arvoja epäloogisesti.

### Vertailu kahdella yhtäsuuruusmerkillä

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

Vertailu kolmella merkillä on helpommin arvattavissa, koska sekä tyypin että arvon tulee olla sama:

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

Taulukoita vertailtaessa `==` ja `===` molemmat tarkastavat, onko kyseessä sama taulukko. __Taulukoiden sisältöjä ei vertailla.__

```js
> [1, 2, 3] === [1, 2, 3]
false
> [1, 2, 3] == [1, 2, 3]
false
```

### Olioiden vertailu

Kuten taulukoiden kanssa, myös olioita vertailtaessa tarkastetaan ovatko oliot **samat**, eikä niiden sisältöä vertailla.

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



# Tehtävä

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

Saat itse valita, palauttaako HTTP-palvelusi datan JSON-muodossa (helpointa) vai muodostatko datan perusteella HTML-sivun esimerkiksi pug-templaten avulla.

Lopputuloksena palvelusi tulee palauttaa taulukko käyttäjistä, jossa kunkin käyttäjän postaukset ovat ryhmiteltynä käyttäjän alle taulukkoksi. Yksittäisen käyttäjän osalta lopputulos voi olla esimerkiksi seuraava:

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

Tämän tehtävän ratkaisemiseksi et tarvitse välttämättä ulkoisia kirjastoja tai `npm`-komentoa. Pelkkä Node.js voi hyvin riittää. Sinulle saattaa kuitenkin olla hyötyä kirjastoista, kuten [express](https://www.npmjs.com/package/express), [axios](https://www.npmjs.com/package/axios) tai [node-fetch](https://www.npmjs.com/package/node-fetch). Myös apukirjastojen, kuten [lodash](https://www.npmjs.com/package/lodash) käyttäminen on sallittua.

## Pyyntöjen samanaikaisuus

Koska HTTP-pyynnöt ovat JavaScriptissä asynkronisia, käyttäjien ja postausten lataaminen voidaan tehdä joko rinnakkain tai yksi kerrallaan. 

Tämän tehtävän kannalta ei ole merkitystä kumman tavan valitset, mutta harjoituksen vuoksi suosittelen pyrkimään lataamaan tiedostot samanaikaisesti rinnakkain. Tähän ei tarvita erillisiä työkaluja, vaan riittää että käsittelet Promiset "tavallisina olioina", joiden then-metodia ei ole pakko kutsua välittömästi. Voit siis itse valita, missä haluat kunkin Promise-olion tulosta käyttää. Myös `Promise.all`-funktiosta voi olla apua.

## Vinkit datan käsittelyyn

Käyttäjien ja heidän postauksiensa yhdistämiseksi yksi lähestymistapa on käydä käyttäjät läpi `map`-metodilla ja muodostaa jokaisesta käyttäjästä uusi olio, jolla on taulukko postauksia. Postaustaulukko puolestaan voidaan rakentaa kullekin käyttäjälle `filter`-metodin avulla, valitsemalla taulukosta ne postaukset, joiden `userId` vastaa kyseisen käyttäjän `id`:tä.

Vaihtoehtoisesti voit myös ratkaista tehtävän täysin ilman `map`, `filter`, `reduce` yms. ES6-metodeja perinteisillä ehto- ja  toistorakenteilla. Oppimisen kannalta suosittelemme kuitenkin tutustumaan tunnilla esitettyihin ratkaisutapoihin.

## Tehtävän palauttaminen

Palauta kaikki ratkaisuusi liittyvät lähdekoodit sekä mahdollinen `package.json` erillisinä tiedostoina Teamsiin ennen seuraavaa oppituntia. Nimeä `.js`-päätteiset tiedostot `.js.txt`-päätteisiksi, mikäli Teams ei hyväksy tiedostojasi tietoturvasyistä.

