# ES6, JavaScript, node (+MongoDB)

Tämä aihe on jaettu kahdelle eri viikolle. Ensimmäisellä viikolla tutustumme ES6:een, erilaisiin ohjelmointityyleihin sekä Node-ohjelmointiin yleisellä tasolla. Toisella viikolla sovellamme oppimaamme NPM:n ja Express-palvelinkirjaston yhteydessä.

Tunneilla käsittelemme samaa Helsinki Marketing -tapahtuma-aineistoa, jota käsittelimme myös tietorakenteiden ja algoritmien kotitehtävässä.

----

# Oppitunti 5.3.2021

Tämän oppitunnin tavoitteena on oppia erityisesti lukemaan koodia ja ymmärtämään, miten yleisimmät JavaScript-kieliset esimerkkikoodit toimivat. Sivuamme funktionaalista ohjelmointia hyödyntämällä funktioiden antamista parametreina toisille funktioille (callback) sekä funktioiden vaiheittaista suorittamista (currying).

Oppitunnin jälkeen osaat nimetä esimerkiksi seuraavassa koodissa käytettyjä ominaisuuksia:

```js
function helloAgent({ names }) {
    let { first, last } = names;
    console.log(`My name is ${last}, ${first} ${last}`);
}

module.exports = { helloAgent };
```

ES6:n ajoittain erikoiset syntaksit tekevät usein koodista suoraviivaista, mutta toisinaan syntaksien liikakäyttö väärissä tilanteissa hankaloittaa koodin ymmärtämistä ja ylläpitoa. Miten esimerkiksi saisit hyödynnettyä yllä esitettyä `helloAgent`-funktiota toisesta moduulista käsin? Tämän tunnin jälkeen tunnistat koodiesimerkin erikoisuudet ja tunnistat joitakin tilanteita, joissa on tarkoituksenmukaista hyödyntää eri ominaisuuksia.

Itseopiskelumateriaalina voit hyödyntää hyviä sivustoja, kuten:

* https://javascript.info/
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/
* https://medium.com/poka-techblog/simplify-your-javascript-use-map-reduce-and-filter-bd02c593cc2d

Aiheen otsikossa esiintyvä MongoDB-tietokanta ei ole osa oppituntien yhteistä sisältöä eikä oppituntiin liittyvää kotitehtävää, vaan MongoDB:tä on mahdollista hyödyntää kurssin syventävässä seminaariosuudessa.


## JavaScriptin ohjelmointityylit

JavaScript on ns. monen paradigman kieli, eli sillä voidaan soveltaa monia erilaisia ohjelmointityylejä. Voit siis soveltaa JavaScriptillä olio-ohjelmointia tai funktionaalista ohjelmointia, tai halutessasi sekoittaa eri tyylejä. Monipuolisuuden heikkoutena JavaScriptillä ei aina ole yhtä vahvoja "parhaita käytäntöjä" kuin joillain yhden paradigman kielillä. 

Tämän oppitunnin aikana perehdymme erityisesti JavaScriptin funktionaaliseen puoleen: nuolifunktioihin sekä map-, filter- ja reduce-operaatioihin.


## JavaScript-kielen laajennokset

Opintojen tässä vaiheessa olette käyttäneet JavaScriptiä eri kursseilla ja eri käyttötarkoituksissa. JavaScriptiä on mahdollista "käyttää" myös ilman varsinaista ymmärrystä siitä, miten ohjeissa esitetyt syntaksit oikeasti toimivat. Osa ymmärrettävyyden haasteista johtuu erilaisista sovelluskehyksistä ja työkaluista, kuten React, jotka hyödyntävät erilaisia kielen natiiviominaisuuksiin kuulumattomia ominaisuuksia, kuten JSX-syntaksia:

```jsx
// https://reactjs.org/docs/introducing-jsx.html
const element = <h1>Hello, world!</h1>;
```

Yllä oleva koodiesimerkki ei ole "puhdasta" JavaScriptiä, joten koodi ei ole suoraan suoritettavissa ilman erillistä käännösvaihetta. Kääntäminen tehdään usein taustalla [Babel](http://babeljs.io/)-työkalulla, joka muuttaa (transpile) esimerkiksi yllä olevan JSX-koodin tavallisiksi JavaScript-rakenteiksi:

```js
// Sama koodi transpiloituna https://babeljs.io/repl-työkalulla:
var element = React.createElement("h1", null, "Hello, world!");
```

Reactin ja muiden erityissyntaksien lisäksi Babel osaa muuntaa JavaScriptin modernimmilla versioilla toteutetut syntaksit vanhempien selainten tukemaan muotoon. Erilaisista muunnoksista johtuen voi joskus olla haastavaa hahmottaa, mitkä asiat ovat "natiivi JavaScriptiä" ja mitkä eri kirjastoihin tai ohjelmistokehyksiin liittyviä ominaisuuksia.


## Laajennosten ja uusien ominaisuuksien selaintuki

Erityisesti verkkoselaimella käytettävien sovellusten kehittämisessä on huomioitava vaihtelevat suoritusympäristöt, joissa selain joko tukee tai ei tue kirjoittamaasi koodia. Selaintuki on perinteisesti ollut merkittävä ongelma, koska JavaScript on jaeltu selaimille suoritettavaksi sellaisenaan ja eri selainten JavaScript-tuki on ollut vaihtelevaa. 

Tänä päivänä selainyhteensopivuus ei ole välttämättä merkittävä ongelma, koska selaimelle tarkoitettu koodi usein muunnetaan, eli "transpiloidaan" selainten varmasti tukemaan muotoon. Esimerkiksi seuraavassa koodiesimerkissä hyödynnetään JavaScriptin "object destructuring"-syntaksia, joka ei ole tuettu kaikissa vanhemmissa selaimissa:

```js
let { first, last } = names;
```

Koodia transpiloitaessa yllä oleva koodi voidaan kuitenkin muuttaa automaattisesti vanhempien selainten tukemaan muotoon:

```js
var _names = names,
  first = _names.first,
  last = _names.last;
```

Useat kehitystyökalut, kuten Reactin kehityspalvelin, huolehtivat transpiloinnista automaattisesti taustalla.


# ES6

JavaScript-kielen taustalla olevan ECMAScript-standardin versiossa 6 ja sen jälkeen kieleen on tullut mukaan useita erilaisia ominaisuuksia ja kirjoitusasuja, kuten edellä esitetty "object destructuring". Seuraavissa kappaleissa tutustumme esimerkkien avulla siihen, miten uudet syntaksit voivat hyödyttää meitä "oikeassa ohjelmassa". Oikea ohjelma tarkoittaa tässä tapauksessa esimerkiksi Node-sovellusta, joka hakee dataa REST-rajapinnasta ja tarjoaa asiakkailleen JSON-muotoista dataa.

Huom! Eri syntaksien opetteleminen on tärkeää lähinnä siksi, että ymmärrät kohtaamiasi esimerkkikoodeja ja käyttämiäsi valmiita koodipohjia. Hyvässä tapauksessa pystyt myös välttämään turhaa toistoa tai kompleksisuutta. Koodin "modernisointi" vain modernisoinnin vuoksi on muuten usein toisarvoista.


## Array destructuring


> *"Destructuring assignment is a special syntax that allows us to “unpack” arrays or objects into a bunch of variables, as sometimes that’s more convenient. Destructuring also works great with complex functions that have a lot of parameters, default values, and so on."*
>
> [Kantor, I. Destructuring assignment. JavaScript.info](https://javascript.info/destructuring-assignment#array-destructuring)

JavaScript-taulukosta voidaan purkaa arvoja yksittäisiin muuttujiin käyttämällä hakasulkujan muuttujien nimien määrittelyn ympärillä:

```js
let [ first, middle, last ] = names;
```

Omien muuttujiemme nimet voivat olla taulukoiden tapauksessa mitä tahansa, mutta niiden arvot määräytyvät samassa järjestyksessä kuin taulukon arvot. Yllä oleva koodi on käytännössä sama kuin:

```js
let first = names[0];
let middle = names[1];
let last = names[2];
```

### Array destructuring ja useState()

Olet mahdollisesti törmännyt taulukon purkamiseen esimerkiksi Reactin kanssa:

```js
const [count, setCount] = useState(0);
```

`useState` palauttaa arvon ja funktion taulukkona, joka puretaan tyypillisesti kahteen erilliseen muuttujaan hakasulkujen, eli array destructuring -operaation, avulla. Voit lukea aiheesta lisää dokumentaatiossa [Using the State Hook / What Do Square Brackets Mean?](https://reactjs.org/docs/hooks-state.html#tip-what-do-square-brackets-mean)


## Object destructuring

> *"We have an existing object at the right side, that we want to split into variables. The left side contains a “pattern” for corresponding properties. In the simple case, that’s a list of variable names in {...}."*
>
> [Kantor, I. Object destructuring. JavaScript.info](https://javascript.info/destructuring-assignment#object-destructuring)

JavaScript-olioista voidaan valita yksittäisiä attribuutteja eri muuttujiin käyttämällä aaltosulkuja muuttujien nimien ympärillä:

```js
let { first, middle, last } = names;
```

Tällä syntaksilla muuttujien nimien on oltava samat kuin oliosta purettavien attribuuttien nimet. Yllä olevakoodi vastaa pidemmin kirjoitettuna tätä:

```js
let first = names.first;
let middle = names.middle;
let last = names.last;
```

Destructuring on usein käytössä myös silloin, kun valitsemme jostain oliosta tietyt arvot tai funktiot käytettäväksi omassa koodissamme:

```js
const { PI } = Math; // sama kuin: const PI = Math.PI;
```

Object destructuring on yleinen myös import- ja require-operaatioiden yhteydessä, jos haluamme tuoda omaan koodiimme tietyt nimetyt arvot toisesta JS-tiedostosta:

```js
const { Event, Activity, Place } = require('./models');
```

Tai:

```js
import { Event, Activity, Place } from './models.js';
```

## Property value shorthand

> *"The use-case of making a property from a variable is so common, that there’s a special property value shorthand to make it shorter."*
>
> [Kantor, I. Property value shorthand. JavaScript.info](https://javascript.info/object#property-value-shorthand)


Tietyissä tapauksissa koodissa on jo olemassa useita muuttujia, joiden arvoja halutaan käyttää uuden olion attribuutteina. Meillä voi olla esimerkiksi seuraavat kaksi merkkijonoa:

```js
let first = 'Chuck';
let last = 'Norris';
```

Näiden muuttujien avulla voidaan muodostaa suoraviivaisesti uusi olio ilman, että joudumme toistamaan attribuuttien ja muuttujien nimiä:

```js
let names = { first, last };
```

Yllä oleva koodi luo siis olion, jossa on `first` ja `last` nimiset attribuutit, joiden arvot on poimittu samannimisistä muuttujista. Käytännössä koodi vastaa pidemmin kirjoitettuna seuraavaa:

```js
let names = { first: first, last: last };
```

Joissain tapauksissa sama koodi voidaan kirjoittaa myös monessa vaiheessa, joissa ensin luodaan olio, ja sen jälkeen asetetaan attribuutit:

```js
let names = {};
names.first = first;
names.last = last;
```

### Property value shorthand ja export

Node-moduulit "julkaisevat" ominaisuuksiaan toisille moduuleille `module.exports`-muuttujan kautta, esim. seuraavasti:

```js
module.exports.Event = Event;
module.exports.Activity = Activity;
module.exports.Place = Place;
```

Tämä toisteinen koodi on kirjoitettavissa paljon lyhyemmin:

```js
module.exports = { Event, Activity, Place };
```

ES6:n export-komentoa käyttävät moduulit hyödyntävät `module`-muuttujan sijaan pelkkää `export`-avainsanaa:

```js
export { Event, Activity, Place };
```

## Object destructuring ja property value shorthand yhdessä

Yhdistämällä kaksi aikaisempaa syntaksia, voimme luoda esimerkiksi koordinaattipisteen tapahtumaolion sisältä löytyvän `location`-rakenteen avulla:

```js
let point = { lat, lon } = event.location;

// sama kuin
let point = {
    lat: event.location.lat,
    lon: event.location.lon
};
```

## Array spread

> *"Spread syntax (...) allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected."*
>
> [MDN web docs, Spread syntax (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)


```js
let a = [1, 2, 3];
let b = [4, 5, 6];

let c = [...a, ...b];        // [ 1, 2, 3, 4, 5, 6 ]
let d = [...a, ...b, ...c];  // [ 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6  ]
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax


## Object spread

> *"copies own enumerable properties from a provided object onto a new object."*
>
> [MDN web docs, Spread syntax (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

Samankaltainen kuin taulukoiden spread-operaatio, mutta olioille sovellettuna:

```js
let person = { hobby: 'Kung-fu', ...names };

// luo uuden olion, jossa on kaikki names-olion attribuutit, 
// ja sen lisäksi hobby-attribuutti.

// sama kuin:
let person = Object.assign({}, names);
person.hobby = 'Kung-fu';
```

Yllä olevassa `names`-muuttujassa oletetaan olevan olion, joka sisältää esim. `firstName`- ja `lastName`-attribuutit.


### Oletusarvojen käyttäminen

Tyypillinen käyttökohde object spread -operaatiolle on esimerkiksi valinnaisten arvojen korvaaminen saaduilla parametreilla. Seuraavassa koodissa määritellään ensin `defaults`, jota myöhemmin laajennetaan `params`-olion arvoilla:

```js
const defaults = { brightness: 100, color: '#ffffff' };
const params = { brightness: 90 };

let light = { ...defaults, ...params };
```

Lopussa `brightness` on muutettu uusien parametrien mukaiseksi, mutta `color` on edelleen oletusarvossa:

```js
{ brightness: 90, color: '#ffffff' }
```

## Rest in Object Destructuring

> *"Rest properties collect the remaining own enumerable property keys that are not already picked off by the destructuring pattern."*
>
> [MDN web docs, Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

Aikaisemmissa object  destructuring -esimerkeissä valitsimme oliosta juuri tietyt attribuutit, jotka sijoitettiin muuttujiin. Jos haluamme poimia erikseen uuteen olioon kaikki loput attribuutit, onnistuu se seuraavasti:

```js
let { name, description, ...others } = event;
```

Tässä esimerkissä `others` sisältää uuden olion, jolla on kaikki muut `event`-olion attribuutit, paitsi ne, jotka poimittiin jo nimien perusteella.

# Muut tunnilla käsiteltävät tekniikat

## Nuolifunktiot

> *"An arrow function expression is a compact alternative to a traditional function expression, but is limited and can't be used in all situations."*
>
> [MDN web docs, Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

Nuolifunktioiden kaltaiset anonyymit funktiot ovat yleisiä myös muissa kielissä, kuten Javassa ja Pythonissa. Niissä vastaavia funktioita kutsutaan "lambdoiksi".

Funktion määrittelystä voidaan nuolifunktioiden tapauksessa jättää pois sana `function` sekä, mikäli funktiossa on vain yksi lauseke, myös `return`-avainsana. Mikäli funktion runko koostuu useista lausekkeista, tarvitaan lisäksi aaltosulut ja `return`.

```js
let multiply = (a, b) => a * b;

// sama kuin:
function multiply(a, b) {
    return a * b;
}
```

## Currying

Eräs JavaScriptin yhteydessä kasvavassa määrin hyödynnetty tekniikka, joka ei suoraan liity pelkästään ES6:een tai vain JavaScriptiin on "currying":

> *"Currying is an advanced technique of working with functions. It’s used not only in JavaScript, but in other languages as well.*
>
> *Currying is a transformation of functions that translates a function from callable as f(a, b, c) into callable as f(a)(b)(c)."*
>
> [Kantor, I. Currying. JavaScript.info](https://javascript.info/currying-partials)

Currying-tekniikalla voimme siis pilkkoa useita parametreja sisältäviä funktioita siten, että yksittäisellä funktiokutsulla sidotaan yksi muuttuja. Funktiot palauttavat uusia funktioita, jotka voidaan ottaa tarvittaessa talteen ja kutsua muualla. 

Kutsuessamme toista funktiota, ensimmäisessä funktiokutsussa annetut parametrit ovat edelleen voimassa, koska ne ovat saman "sulkeuman" (clojure) sisällä:

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
let tuumina = sentitTuumiksi(200);
let euroina = markatEuroiksi(100);
```

Milloin funktioiden osittaisesta määrittelystä on meille erityisesti hyötyä?

"Currytetty" funktio voidaan antaa suoraan esimerkiksi `map`-funktiolle, joista kerromme lisää myöhemmin tässä materiaalissa:

```js
let markat = [200, 123, 99, 10, 4521];
let eurot = markat.map(markatEuroiksi); // [ 33.637585292, 20.68711495458, 16.65060471954, 1.6818792646, 760.37761552566 ]
```

# ESLint

> *"lint, or a linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors, and suspicious constructs.[4] The term originates from a Unix utility that examined C language source code."*
>
> [lint (software). Wikipedia](https://en.wikipedia.org/wiki/Lint_(software))
```
$ npm install --global eslint
$ eslint --init
$ 
$ eslint tiedosto1.js tiedosto2.js
```

Lue lisää ESLintin komentorivikäytöstä osoitteessa [https://eslint.org/docs/user-guide/command-line-interface](https://eslint.org/docs/user-guide/command-line-interface).

`npm install --global` ei välttämättä onnistu ilman sudo-oikeuksia. Kurssin [asennusohjeissa](00_linux/asennukset.md#nodejs-ja-npm) on linkki konfigurointiohjeeseen, jolla npm-asennukset saadaan toimimaan Ubuntussa tietoturvallisemmin ilman pääkäyttäjäoikeuksia.


# Tapahtumien käsitteleminen `map`, `filter` ja `reduce` -operaatioilla

Tunnilla harjoittelemme `map`, `filter` ja `reduce` -operaatioita [MyHelsinki Open API](http://open-api.myhelsinki.fi/doc) -rajapinnan tapahtumien avulla. `map`, `filter` ja `reduce` löytyvät suurimmasta osasta ohjelmointikieliä, mukaan lukien Java, Python ja JavaScript.


## Esivalmistelu: staattisen aineiston hakeminen

Linux-pohjaisissa järjestelmissä HTTP-pyyntöjen tekemiseksi komentoriviltä käytetään usein `curl`-komentoa.

> *curl  is  a tool to transfer data from or to a server, 
> using one of the supported protocols [...].
> The command is designed to work without user interaction.*
>
> `man curl`

`curl` voidaan asentaa seuraavasti:

    $ sudo apt install curl

`curl`-komennon avulla voimme hakea raakadatan REST-rajapinnasta:

    $ curl http://open-api.myhelsinki.fi/v1/events/

Edellinen komento tulostaa saadun vastauksen suoraan terminaaliin. Pythonin standardikirjaston `json.tool` auttaa muotoilemaan JSON-dataa hyvin sisennetyiksi merkkijonoiksi. `curl`-komennon tuloste voidaan putkittaa `json.tool`-moduulille seuraavasti:

    $ curl http://open-api.myhelsinki.fi/v1/events/ | python3 -m json.tool

Nyt saimme terminaaliin siistimmin jäsennellyn JSON-tietorakenteen. Voimme ohjata saamamme tulosteet vielä tiedostoon `>`-operaatiolla seuraavasti:

    $ curl http://open-api.myhelsinki.fi/v1/events/ | python3 -m json.tool > events.json

Huom! `events.json` on iso tiedosto, luokkaa 6-7 megatavua, joten sen käsitteleminen tekstieditorilla voi olla raskasta.


## Tapahtuma JSON:in tuominen Node REPL:iin (Read-Evaluate-Print-Loop)

Ensimmäiset kokeilut teemme nodella ilman npm-pakettienhallintaa tai riippuvuuksia:

```js
$ node
> // luetaan JSON-tiedosto muuttujaan
> const jsonFile = require('./events.json')
>
> let events = jsonFile['data']
> events.length
5527
```

`events` sisältää nyt meille aikaisemmilta viikoilta tutun taulukon tapahtumista. Tällä kertaa tapahtumat ovat JavaScript-olioita. Niillä on silti täysin sama rakenne kuin aikaisemmissa tehtävissä käsittelemillämme Pythonin sanakirjoilla:

```js
> // alkamispäivän tarkastaminen satunnaiselta tapahtumalta
> let e = events[2500]
>
> // tapahtuman alkuajan selvittäminen
> e['event_dates']['starting_day']
'2020-10-23T07:00:00.000Z'
>
> // vaihtoehtoinen tapa käsitellä sisäkkäisiä rakenteita on pistenotaatio
> e.event_dates.starting_day
'2020-10-23T07:00:00.000Z'
>
> // vertailu johonkin muuhun päivämäärään 
> e.event_dates.starting_day > '2020-10-07T00:00:00.000Z'
true
```

## Filter-operaatio

> *"The filter() method creates a new array with all elements that pass the test implemented by the provided function."*
>
> [MDN web docs. Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

```js
> // filter luo uuden taulukon, jolle valitaan alkuperäiseltä taulukolta 
> // sellaiset arvot, joille antamamme funktio palauttaa `true`:
> let allTrue = events.filter(event => true);
> allTrue.length
5527 // kaikki valittiin!
> 
> // vastaavasti jos palautetaan false:
> let allFalse = events.filter(event => false);
> allFalse.length
0 // mitään ei valittu!
>
> // valitaan päivämäärän mukaan!
> let now = new Date().toISOString()
> now
'2020-10-09T10:47:00.111Z'
>
> let futureEvents = events.filter(event => {
      return event.event_dates.starting_day >= now;
  }
```

Seuraavaksi halutaan rajata tapahtumat, joilla on alkuaika, ja joilla se sijoittuu kahden ajankohdan väliin:

```js
> // Tapahtumat, joilla on alkuaika, ja se sijoittuu kahden ajankohdan väliin:
> let nextWeek = '2020-10-16T10:47:00.111Z';
>
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
    let { starting_day } = event.event_dates; // object destructuring
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

Yllä olevassa koodissa `isBetweenDates` on "kovakoodattu" vertailemaan tapahtuman alkuaikaa aina samoihin arvoihin `now` ja `nextWeek`. Olisikin paljon parempi, jos voisimme määritellä funktion kahdessa vaiheessa: ensin annetaan päivämäärät ja sen jälkeen vertaillaan tapahtumaa:

```js
function isBetweenDates(minDate, maxDate) {
    return function (event) {
        let { starting_day } = event.event_dates; // object destructuring
        return starting_day && minDate <= starting_day && starting_day <= maxDate;
    }
}
```

Tämän `isBetweenDates`-funktion avulla voimme ensin luoda uuden funktion `isNextWeek`:

```js
let isNextWeek = isBetweenDates('2020-10-09T00:00:00', '2020-10-16T24:00:00');
```

Kun `isNextWeek` annetaan `filter`-operaatiolle, filter kutsuu antamaamme `isNextWeek`-funktiota jokaiselle tapahtumalle. Funktio palauttaa `true` mikäli tapahtuman ajankohta sijoittuu seuraavalle viikolle, joten uudelle taulukkolle tulee vain seuraavan viikon tapahtumat:

```js
let eventsNextWeek = events.filter(isNextWeek);
```

Nyt melko monimutkainen operaatio, joka edellyttäisi perinteisesti taulukon luomisen, toistorakenteen, ehtorakenteen ja taulukkoon lisäykset, saatiin toteutettua kohtuullisen suoraviivaisesti.


## Funktioiden parametrien oletusarvot

JavaScriptin uusimmilla versioilla voimme antaa parametreille oletusarvot, joita käytetään, mikäli funktion kutsussa on jätetty parametriarvo antamatta tai sen arvo on `undefined`:

```js
function isBetweenDates(minDate = '0000-01-01', maxDate = '9999-12-31') {
    return function (event) {
        let { starting_day } = event.event_dates; // object destructuring
        return starting_day && minDate <= starting_day && starting_day <= maxDate;
    }
}
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters



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


## Järjestäminen alkamisajan mukaan

JavaScriptin taulukoilla on valmis `sort`-metodi, jonka avulla sen sisältö voidaan järjestää. Tarvitset tapahtumien järjestelemiseksi vertailufunktion, joka vertailee kahta tapahtumaa, ja kertoo kumman tulisi olla järjestyksessä ensimmäisenä:

> *"The sort() method sorts the elements of an array in place and returns the sorted array.*
>
> *If compareFunction is supplied, all non-undefined array elements are sorted according to the return value of the compare function. If compareFunction(a, b) returns less than 0, sort a to an index lower than b (i.e. a comes first). If compareFunction(a, b) returns 0, leave a and b unchanged with respect to each other, but sorted with respect to all different elements."*
>
> [MDN web docs. Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

Voimme vertailla alkamisaikoja ja järjestää tapahtumat alkamisajan mukaan järjestykseen alkamisajankohtia vertailevalla funktiolla:

```js
function eventDateComparator(event1, event2) {
    // jos starting_day on undefined, käytetään tyhjää merkkijonoa:
    let event1date = event1.event_dates.starting_day || '';
    let event2date = event2.event_dates.starting_day || '';

    // Palauttaa negatiivisen luvun, nollan tai positiivisen luvun 
    // riippuen merkkijonojen aakkosjärjestyksestä. Tämä toimii, koska 
    // starting_day on aina ISO-muotoinen String, esim. "2020-10-16T24:00:00".
    return event1date.localeCompare(event2date);
}

events.sort(eventDateComparator);
```

# Tehtävä 5.3.2021 (luonnos)

Tämän viikon tehtävässä harjoitellaan tunnilla esitettyjen ohjelmointitapojen hyödyntämistä. Tehtävänä on lukea kahdesta erillisestä JSON-tiedostosta käyttäjiä ja postauksia, ja yhdistellä käyttäjät postauksiin.


## Tehtävän data

Tässä tehtävässä käytetään testidataa JSON Placeholder -palvelusta:

> *"{JSON} Placeholder*
>
> *Free to use fake Online REST API for testing and prototyping*
>
> *Powered by JSON Server + LowDB"*
>
> https://jsonplaceholder.typicode.com/

Voit tallentaa JSON-tiedostot itsellesi seuraavista kahdesta osoitteesta:

* käyttäjät: https://jsonplaceholder.typicode.com/users
* postaukset: https://jsonplaceholder.typicode.com/posts

Mikäli haluat, voit myös toteuttaa tiedostojen lataamisen dynaamisesti JavaScriptillä. Tiedon dynaaminen hakeminen käsitellään kuitenkin vasta seuraavan viikon oppitunnilla.

## Osa 1 (arvosanatavoite 3)

Tehtävän 1. osassa sinun tulee kirjoittaa Node-skripti, joka lukee tiedostot ja tulostaa niissä olevien käyttäjien nimet (name) sekä postausten otsikot (title) siten, että kunkin käyttäjän nimen tulostamisen jälkeen tulostetaan kaikkien kyseisen käyttäjän postausten otsikot:

```
Leanne Graham
- sunt aut facere repellat provident occaecati excepturi optio reprehenderit
- qui est esse
- ea molestias quasi exercitationem repellat qui ipsa sit aut
- eum et est occaecati
- nesciunt quas odio
- dolorem eum magni eos aperiam quia
- magnam facilis autem
- dolorem dolore est ipsam
- nesciunt iure omnis dolorem tempora et accusantium
- optio molestias id quia eum 


Ervin Howell
- et ea vero quia laudantium autem
- in quibusdam tempore odit est dolorem
- dolorum ut in voluptas mollitia et saepe quo animi
- voluptatem eligendi optio
- eveniet quod temporibus
- sint suscipit perspiciatis velit dolorum rerum ipsa laboriosam odio
- fugit voluptas sed molestias voluptatem provident
- voluptate et itaque vero tempora molestiae
- adipisci placeat illum aut reiciendis qui
- doloribus ad provident suscipit at 

...
```



## Osa 2 (arvosanatavoite 5)

Arvosanatavoitteeseen 5 sinun tulee kirjoittaa edellisen lisäksi toinen skripti, joka esittää datan sisäkkäisinä JSON-tietorakenteina siten, että kunkin käyttäjän kirjoittamat postaukset ovat koottu käyttäjän yhteyteen omaksi taulukokseen. Yksittäisen käyttäjän osalta lopputulos voi olla esimerkiksi seuraava:

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

JavaScript-tietorakenteen muuttaminen merkkijonoksi onnistuu esimerkiksi [JSON.stringify-metodilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify):

```js
let merkkijonona = JSON.stringify(omaData, null, 2);
```

Muunnettu JSON-tietorakenne tulee tallentaa uuteen JSON-tiedostoon esimerkiksi Noden fs-moduulin [writeFileSync](https://stackoverflow.com/a/46356040)-metodilla:

```js
const fs = require('fs')

fs.writeFileSync('output.json', omaData)
```

Arvosanatavoitteeseen 5 sinun tulee hyödyntää oppitunnilla käsiteltyjä `map`-, `filter`- tai `reduce`-operaatiota vähintään kerran.



## Valmiiden kirjastojen käyttäminen

Näiden tehtävien ratkaisemiseksi et tarvitse ulkoisia kirjastoja tai `npm`-komentoa. Pelkkä Node.js riittää. Halutessasi saat kuitenkin käyttää apukirjastoja, kuten [lodash](https://www.npmjs.com/package/lodash). Kirjastojen käyttäminen ei vaikuta laskevasti arvosanaan.


## Vinkit datan käsittelyyn

Käyttäjien ja heidän postauksiensa yhdistämiseksi yksi lähestymistapa on käydä käyttäjät läpi `map`-metodilla ja muodostaa jokaisesta käyttäjästä uusi olio, jolla on taulukko postauksia. Postaustaulukko puolestaan voidaan rakentaa kullekin käyttäjälle `filter`-metodin avulla, suodattamalla kaikista postauksista ne, joiden `userId` vastaa kyseisen käyttäjän `id`:tä.


## Tehtävän palauttaminen

Myös osittain ratkaistut palautukset hyväksytään ja arvostellaan suhteessa niiden valmiusasteeseen. Palauta kaikki ratkaisuusi liittyvät lähdekoodit erillisinä tiedostoina Teamsiin ennen seuraavaa oppituntia. 

**Nimeä `.js`-päätteiset tiedostot `.js.txt`-päätteisiksi, mikäli Teams ei hyväksy tiedostojasi tietoturvasyistä.**


----

# Lisenssit ja tekijänoikeudet

## MyHelsinki Open API

> *"Note that all of the information provided over the API is open data with the exception of image files. When using images, please refer to the license terms included with each image.*"
> 
> MyHelsinki Open API. https://open-api.myhelsinki.fi/

MyHelsinki Open API:n aineisto on lisensoitu [Creative Commons BY 4.0](https://open-api.myhelsinki.fi/terms)-lisenssillä. Voit lukea tarkemmat käyttöehdot ositteesta https://open-api.myhelsinki.fi/terms.

## JSONPlaceholder

JSONPlaceholder-palvelun on kehittänyt [typicode](https://typicode.com) ja se on lisensoitu MIT-lisenssillä: [https://github.com/typicode/jsonplaceholder/blob/master/LICENSE](https://github.com/typicode/jsonplaceholder/blob/master/LICENSE)