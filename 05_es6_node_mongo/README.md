
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

# Aloitus: staattisen aineiston hakeminen


    $ # Asennetaan curl
    $ sudo apt install curl

`curl`-komennon avulla voimme hakea raakadatan REST-rajapinnasta.

    $ curl http://open-api.myhelsinki.fi/v1/events/

`python3 -m json.tool` auttaa muotoilemaan JSON-merkkijonot oikein sisennetyiksi merkkijonoiksi:

    $ curl http://open-api.myhelsinki.fi/v1/events/ | python3 -m json.tool

`>` ohjaa komennon tulosteet tiedostoksi, joten voimme lopulta ohjata ladatun ja muotoillun JSON-tietorakenteen tiedostoon seuraavasti:

    $ curl http://open-api.myhelsinki.fi/v1/events/ | python3 -m json.tool > events.json

events.json on iso tiedosto, luokkaa 6-7 megatavua, joten sen käsitteleminen tekstieditorilla on melko raskasta.

Ilman npm:ää. Ilman riippuvuuksia:

```js
$ node
> let jsonFile = require('./events.json')
> let events = jsonFile['data']
> events.length
5527
>
> // alkamispäivän tarkastaminen satunnaiselta tapahtumalta
> let e = events[2500]
> e.event_dates.starting_day
'2020-10-23T07:00:00.000Z'
>
> // vertailu johonkin muuhun päivämäärään 
> e.event_dates.starting_day > '2020-10-07T00:00:00.000Z'
true
```

# Filter

```js
> // filter luo uuden listan, jolle valitaan sellaiset arvot, joille funktio palauttaa `true`:
> let allTrue = events.filter(e => true);
> allTrue.length
5527 // kaikki valittiin!
> 
>
> // vastaavasti jos palautetaan false:
> let allFalse = events.filter(e => false);
> allFalse.length
0 
> // mitään ei valittu!
>
> // valitaan päivämäärän mukaan!
> let now = new Date().toISOString()
> now
'2020-10-01T11:57:39.687Z'
>
> let nextWeek = new Date();
> nextWeek.setDate(nextWeek.getDate() + 7); # kasvatetaan 7 päivää
> let maxDate = nextWeek.toISOString()
>
> // nyt meillä on rajat:
> [now, maxDate]
[ '2020-10-01T11:57:39.687Z', '2020-10-08T12:01:11.231Z' ]
```

Seuraavaksi halutaan rajata tapahtumat, joilla on alkuaika, ja joilla se sijoittuu kahden päivän väliin:

```js
> // tapahtumia yhteensä:
> events.length
5527
>
> // filtteröidään tapahtumat, joilla on ylipäänsä alkuaika:
> events.filter(e => e.event_dates.starting_day != null).length
5433
> 
> // Tapahtumat, joiden alkuaika on viikon sisällä:
> let eventsNextWeek = events
    .filter(e => e.event_dates.starting_day != null)
    .filter(e => e.event_dates.starting_day > now)
    .filter(e => e.event_dates.starting_day < maxDate)
> eventsNextWeek.length
612 // enää 612 tapahtumaa!
```

Miten voisimme siistiä koodia siten, että yllä oleva koodi ei tekisi kolmea filtteriä eikä sääntöjä kirjoitettaisin filter-metodin sisään?

Tätä varten voimme kirjoittaa filtteröintifunktion erilleen filtteröinnistä!

```js
function isNextWeek(event) {
    let day = event.event_dates.starting_day; 
    return day != null && day >= now && day <= maxDate;
}
```

```js
> // huom! isNextWeek-funktiota ei kutsuta, vaan se annetaan parametrina:
> let eventsNextWeek = events.filter(isNextWeek)
> eventsNextWeek.length
612
```

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

