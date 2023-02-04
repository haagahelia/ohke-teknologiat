# Testaus

Tämän oppitunnin tavoitteena on tutustua testauksen eri tasoihin yksikkötesteistä järjestelmätesteihin ja tutustua testiautomaation käsitteistöön ja työkaluihin.

Aiheen opiskelun jälkeen osaat kirjoittaa Python-funktioillesi yksikkötestit ja tiedät mistä lähteä liikkeelle, kun sinulle tulee tarve kirjoittaa automatisoituja testejä. Osaat myös huomioida testausnäkökulmaa jäsentäessäsi Python-ohjelmiasi eri moduuleihin ja funktioihin.


<!--# Oppitunnin videot

**[Node.js osa 1/3: malliratkaisu, npm, Jest ](https://web.microsoftstream.com/video/c714b986-1990-478a-a2d8-aef39daeb4bb)** *55:37*

Tällä videolla kerrataan edellisen viikon syntaksit konkreettisen esimerkin avulla. Käymme läpi users & posts -tehtävän malliratkaisun, perehdymme Noden pakettienhallintaan ja teemme yksikkötestejä Jest-testaustyökalulla.

**[Node.js osa 2/3: npm, Jest, async/await](https://web.microsoftstream.com/video/631fa660-c0ec-44df-b948-79bd875edf5e)** *48:11*

Tällä videolla käsittelemme yksikkötestausta Jestillä sekä eri tyyppisten arvojen vertailua JavaScriptillä. Asennamme `node-fetch`-kirjaston, jonka avulla voimme tehdä asynkronisia HTTP-pyyntöjä Node.js-koodistamme. Tämän oppitunnin esimerkkikoodit löytyvät osoitteesta https://github.com/swd1tn002/express-oppitunti-2022.

**[ Node.js osa 3/3: npm, Jest, Express ](https://web.microsoftstream.com/video/0ba8a483-aaee-41d4-96c2-459d86ef1264)** *29:59*

Tällä videolla asennamme express-kirjaston, jonka avulla toteutamme yksinkertaisen http-palvelun edellisissä videoissa käsitellyn datan tarjoamiseksi web-selaimelle. Käsittelemme videon lopussa myös tämän viikon harjoitustehtävän tehtävänantoa. Tämän oppitunnin esimerkkikoodit löytyvät osoitteesta https://github.com/swd1tn002/express-oppitunti-2022.-->


## ES6-syntaksien kertaus

Edellisellä oppitunnilla käsittelimme mm. seuraavassa koodiesimerkissä esiintyviä syntakseja:

```js
function helloAgent({ names }) {
    let { first, last } = names;
    console.log(`My name is ${last}, ${first} ${last}`);
}

module.exports = { helloAgent };
```

Miten tässä moduulissa määritettyä `helloAgent`-funktiota voitaisiin kutsua toisesta Node.js-moduulista?


<!--## Users ja Posts -tehtävän malliratkaisu

[Edellisen oppitunnin](oppitunti1.md) tehtävässä teidän tuli yhdistellä Post-olioita User-olioihin hyödyntäen kuvitteellisen blogin JSON-tietorakenteita.

Tehtävän ratkaisemiseksi oli useita erilaisia lähestymistapoja. Oppitunnin aluksi tutustumme funktionaaliseen lähestymistapaan, jossa käsittelemme aineiston map- ja filter-operaatioiden avulla.-->


## JS-koodin yksikkötestaaminen

Koodin testaamiseksi tarvitsemme testaustyökalun, joka voi olla esimerkiksi [Jest](https://jestjs.io/) tai [Mocha](https://mochajs.org/). [Facebookin kehittämän jestin](https://github.com/facebook/jest) suosio on erityisesti React-kirjaston myötä noussut niin suureksi, että olemme valinneet tälle kurssille työkaluksi Jest:in.

Työkalut kannattaa asentaa npm-paketinhallinnan avulla. Jotta npm käsittelee koodihakemistoamme projektina, tulee se alustaa seuraavalla komennolla:

```
$ npm init
```

Tämän jälkeen voimme asentaa testityökalut NPM:n avulla:

```
$ npm install --save-dev jest
```

Seuraavissa vaiheissa seuraamme Jestin dokumentaatiossa [https://jestjs.io/docs/getting-started](https://jestjs.io/docs/getting-started) olevia työvaiheita.

Testejä varten luodaan uusi kansio "test":

```
$ mkdir test
```

Package.json-tiedoston `test`-skriptiksi asetetaan `jest`-komento:

```diff
 "scripts": {
+  "test": "jest"
-  "test": "echo \"Error: no test specified\" && exit 1"
 },
```

Nyt testit voidaan suorittaa `npm test`-komennon avulla:

```
$ npm test
```

Seuraavat testit varmistavat, että:

1. `filterPostsByUser` palauttaa vain sille annetun käyttäjän postaukset
1. `mergeUsersAndPosts` yhdistää annetut käyttäjät postauksiin (kuten tehtävässä)
1. `getUsers` palauttaa onnistuneesti 10 käyttäjää
1. `getPosts` palauttaa onnistuneesti 100 postausta


```js
const assert = require('assert').strict;
const { getUsers, getPosts, filterPostsByUser, mergeUsersAndPosts } = require('../blog/functions');
const { test } = require('@jest/globals');

test('getUsers returns an array of 10 users', () => {
    let users = getUsers();

    assert.equal(users.length, 10, `Should have 10 users but had ${users.length}`);
});

test('getPosts returns 100 posts', () => {
    let posts = getPosts();

    assert.equal(posts.length, 100, `Should have 100 posts but had ${posts.length}`);
});

test('filtering posts for single user', () => {
    let users = getUsers();
    let allPosts = getPosts();
    let user = users[0];

    let filtered = filterPostsByUser(user, allPosts);

    assert.equal(filtered.length, 10);
    assert.ok(filtered.every(post => post.userId === user.id));
});

test('merging posts into users', () => {
    let users = getUsers();
    let posts = getPosts();

    let merged = mergeUsersAndPosts(users, posts);

    assert.equal(merged.length, 10, 'Must still have 10 users');
    assert.ok(Array.isArray(merged[0].posts), 'Users must have a posts array');

    for (let user of merged) {
        assert.equal(user.posts.length, 10);
        assert.ok(user.posts.every(post => post.userId === user.id));
    }
});
```

### Taulukoiden vertailu

Taulukoita vertailtaessa JavaScript tutkii, onko kyseessä sama taulukko. __Taulukoiden sisältöjä ei vertailla.__

```js
> [1, 2, 3] === [1, 2, 3]
false
```

Yllä kahden taulukon vertailu tuottaa siis tulokseksi `false`, vaikka taulukoiden sisältö on sama.

### Olioiden vertailu

Kuten taulukoiden kanssa, myös olioita vertailtaessa tarkastetaan ovatko oliot samat. __Olioiden sisältöjä ei vertailla.__

```js
> { language: "JavaScript" } === { language: "JavaScript" }
false
```

Eri kielet toimivat vertailujen osalta eri logiikalla. Esimerkiksi Python vertailee automaattisesti listojen sisältöä.

### deepEqual

Koska olioiden vertaileminen JavaScriptissä vertailee vain, ovatko oliot samat, joudumme hyödyntämään erillistä vertailulogiikkaa. Node-yksikkötesteissä voimme hyödyntää Noden standardikirjaston `assert`-moduulia ja sieltä löytyvää `deepEqual`-metodia, joka vertailee rekursiivisesti sille annettuja arvoja:

```js
const assert = require('assert').strict;

assert.deepEqual([1, 2, 3], [1, 2, 3]);
assert.deepEqual({ language: "JavaScript" }, { language: "JavaScript" });
```

https://nodejs.org/api/assert.html#assert_assert_deepstrictequal_actual_expected_message


### Totuusarvojen vertailu

JavaScriptissä vertailuoperaatiot tehdään usein kolmella merkillä eli `===` tai `!==`. Kolmen merkin vertailuoperaatiot tarkastavat, että vertailtavien arvojen tyyppi on sama. Mikäli tyyppitarkastus jätetään tekemättä, JavaScript vertailee tyhjiä ja nollaan vertautuvia arvoja toisinaan epäloogisesti.

Voit tutustua aiheeseen syvällisemmin artikkelissa [Equality comparisons and sameness (MDN web docs)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) tai YouTube-videolla [JavaScript == VS === (Web Dev Simplified)](https://www.youtube.com/watch?v=C5ZVC4HHgIg).


### Vertailu Jest:llä

Jest-testaustyökalussa on oma [expect](https://jestjs.io/docs/expect)-funktionsa, jota voidaan käyttää arvojen vertailemiseksi. Tällä oppitunnilla käytämme kuitenkin assert-tyyliä, joka on yhdenmukaisempi aikaisemmin käsiteltyjen JUnit- ja pytest-kokemusten kanssa.


# Fetch-harjoitus

Tähän asti olemme lukeneet käyttäjien ja postausten JSON-rakenteet paikallisesta tiedostosta `require`-funktiolla. Tämä on tapahtunut synkronisesti, eli lukeminen on tehty loppuun ennen seuraavalle riville etenemistä. Tämä on ollut hyvin helppoa ja suoraviivaista.

Tyypillisesti tiedostojen lukeminen, tietokantakyselyt ja http-pyynnöt tapahtuvat kuitenkin JavaScriptissä asynkronisesti, eli vastausta ei jäädä odottamaan, vaan ohjelman suoritus siirtyy suoraan eteenpäin. Asynkronisten operaatioiden valmistumisen jälkeen niiden tuloksia pystytään hyödyntämään esimerkiksi **Promise**-olioiden ja **then**-metodin avulla.

Selaimissa HTTP-pyyntöjä tehdään tyypillisesti JavaScriptin [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)-funktiolla. Nodessa ei ole vielä valmista toteutusta fetch-funktiosta, [mutta sellainen on tulossa versiossa 18](https://blog.logrocket.com/fetch-api-node-js/). Toistaiseksi `fetch` saadaan käyttöön asentamalla erillinen `node-fetch`-paketti:

> *"node-fetch: a light-weight module that brings window.fetch to Node.js"*
>
> https://www.npmjs.com/package/node-fetch

Node-fetch voidaan asentaa seuraavasti:

```
$ npm install node-fetch@^2
```

Vaihtoehtoisesti voit käyttää [cross-fetch](https://www.npmjs.com/package/cross-fetch)-pakettia, joka toimii myös selain- ja React Native -ympäristöissä:

```
$ npm install cross-fetch
```

Fetch-paketin asentamisen jälkeen HTTP-pyyntö voidaan tehdä koodissa seuraavasti:

```js
const fetch = require('node-fetch'); // tai require('cross-fetch');

let httpPromise = fetch('https://jsonplaceholder.typicode.com/users');
```

*Fetch-funktion sijasta voisimme käyttää myös muita HTTP-asiakaskirjastoja, kuten [axios](https://www.npmjs.com/package/axios). Tällä oppitunnilla käytämme fetch-funktiota, koska se on hyödynnettävissä suoraan eri selaimissa, sekä tulevaisuudessa Node.js:ssä.*


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

Peräkkäisiä Promise-olioita voidaan ketjuttaa, kuten yllä, jolloin ensimmäisenä Promisen `then`-metodille annettu funktio suoritetaan aina ennen seuraavia kutsuja, ja edeltävän funktion palauttama arvo välitetään aina seuraavalle funktiolle. Tästä käytetään myös termiä ketjutus eli chaining.

Voit tutustua itsenäisesti tarkemmin `fetch`-funktioon sekä sen palauttamien `Promise`-olioiden käyttämiseen seuraavien YouTube-videoiden avulla:

**[Google Chrome Developers: Using the Fetch API](https://youtu.be/Ri7WRoRcl_U)**

> *"The Fetch API is a modern replacement for XMLHttpRequest. It includes much of the code you used to write for yourself: handling redirection and error codes, and decoding the result. This video gives you an easy introduction."*

**[Google Chrome Developers: Intro to Promises (incl async/await)](https://youtu.be/7unX6hn5NA8)**

> *"Promises make asynchronous programming much easier than the traditional event-listener or callback approaches. This video explains promises, promise-chaining, and complex error-handling."*


## Tuntiesimerkki: fetch-kutsujen ja asynkronisuuden hyödyntäminen

Asynkroninen ohjelmointityyli tekee koodin kirjoittamisesta ajoittain hankalaa. Erityisesti tilanteissa, joissa tarvitsemme useita asynkronisia resursseja, joudumme kiinnittämään suoritusjärjestykseen enemmän huomiota, kuin olemme tottuneet tekemään Javan ja Pythonin kanssa.

Asynkronisuudesta on kuitenkin myös hyötyjä: voimme käynnistää useita asynkronisia operaatioita helposti ilman, että meidän täytyy odottaa ensimmäisten operaatioiden valmistumista.


[Introduction To Testing In JavaScript With Jest](https://www.youtube.com/watch?v=FgnxcUQ5vho)

[Jest Basics](https://courses.webdevsimplified.com/view/courses/javascript-simplified-advanced/729109-Testing/2126286-38-Jest-Basics)