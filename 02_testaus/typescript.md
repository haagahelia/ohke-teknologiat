# Testaus

Tämän oppitunnin tavoitteena on tutustua testauksen eri tasoihin yksikkötesteistä järjestelmätesteihin ja tutustua testiautomaation käsitteistöön ja työkaluihin.

Aiheen opiskelun jälkeen osaat kirjoittaa Python-funktioillesi yksikkötestit ja tiedät mistä lähteä liikkeelle, kun sinulle tulee tarve kirjoittaa automatisoituja testejä. Osaat myös huomioida testausnäkökulmaa jäsentäessäsi Python-ohjelmiasi eri moduuleihin ja funktioihin.


## Suositellut videot

### [What is Automated Testing? - The Startup Lab](https://www.youtube.com/watch?v=Nd31XiSGJLw)

[![What is Automated Testing?](https://img.youtube.com/vi/Nd31XiSGJLw/mq3.jpg)](https://www.youtube.com/watch?v=Nd31XiSGJLw)

> *"In this video we start diving into the world of quality assurance and discuss automated testing for our web and mobile applications..."*
>
> The Startup Lab. [What is Automated Testing?](https://www.youtube.com/watch?v=Nd31XiSGJLw)

&nbsp;

### [Introduction To Testing In JavaScript With Jest - Web Dev Simplified](https://www.youtube.com/watch?v=FgnxcUQ5vho)

[![Introduction To Testing In JavaScript With Jest - Web Dev Simplified](https://img.youtube.com/vi/FgnxcUQ5vho/mq2.jpg)](https://www.youtube.com/watch?v=FgnxcUQ5vho)

&nbsp;

### [Jest Basics - Web Dev Simplified](https://courses.webdevsimplified.com/view/courses/javascript-simplified-advanced/729109-Testing/2126286-38-Jest-Basics)

<a href="https://courses.webdevsimplified.com/view/courses/javascript-simplified-advanced/729109-Testing/2126286-38-Jest-Basics"><img src="https://d31ezp3r8jwmks.cloudfront.net/uxoz8jjx52plpakesnwh34d3h25x" width="320" height="180"></a>

<!--# Oppitunnin videot

**[Node.js osa 1/3: malliratkaisu, npm, Jest ](https://web.microsoftstream.com/video/c714b986-1990-478a-a2d8-aef39daeb4bb)** *55:37*

Tällä videolla kerrataan edellisen viikon syntaksit konkreettisen esimerkin avulla. Käymme läpi users & posts -tehtävän malliratkaisun, perehdymme Noden pakettienhallintaan ja teemme yksikkötestejä Jest-testaustyökalulla.

**[Node.js osa 2/3: npm, Jest, async/await](https://web.microsoftstream.com/video/631fa660-c0ec-44df-b948-79bd875edf5e)** *48:11*

Tällä videolla käsittelemme yksikkötestausta Jestillä sekä eri tyyppisten arvojen vertailua JavaScriptillä. Asennamme `node-fetch`-kirjaston, jonka avulla voimme tehdä asynkronisia HTTP-pyyntöjä Node.js-koodistamme. Tämän oppitunnin esimerkkikoodit löytyvät osoitteesta https://github.com/swd1tn002/express-oppitunti-2022.

**[ Node.js osa 3/3: npm, Jest, Express ](https://web.microsoftstream.com/video/0ba8a483-aaee-41d4-96c2-459d86ef1264)** *29:59*

Tällä videolla asennamme express-kirjaston, jonka avulla toteutamme yksinkertaisen http-palvelun edellisissä videoissa käsitellyn datan tarjoamiseksi web-selaimelle. Käsittelemme videon lopussa myös tämän viikon harjoitustehtävän tehtävänantoa. Tämän oppitunnin esimerkkikoodit löytyvät osoitteesta https://github.com/swd1tn002/express-oppitunti-2022.


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
-->

## Sorting & Filtering -tehtävän malliratkaisu

Edellisen oppitunnin tehtävässä teidän tuli suodattaa ja lajitella MyHelsinki-rajapinnan tapahtumia.

Oppitunnin aluksi tutustumme tehtävän malliratkaisuun ja sen yksikkötesteihin.


## Yksikkötestaus

> *"Yksikkötestauksella tarkoitetaan **pienimmän mahdollisen ohjelman osan**, esimerkiksi aliohjelman, toiminnan testaamista. Yksikkötesteillä varmistetaan, että ohjelman pienimmät osat toimivat odotetulla tavalla, ja että mahdolliset virhetilanteet on niiden osalta ennakoitu."*
>
> *"Yksikkötestauksen hyödyt näkyvät kehitysprosessin aikana erityisesti silloin, kun jo kirjoitettuun koodiin joudutaan tekemään muutoksia. Automatisoiduilla yksikkötesteillä voidaan **nopeasti** todeta, aiheuttavatko tehdyt muutokset virheitä."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. Testauksen tasot.<!--http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot-->


### Testitapaus

Yksinkertaisimmillaan voimme kirjoittaa yksittäisen testifunktion, **eli testitapauksen**, joka kutsuu yksittäistä testattavaa funktiota ja tarkistaa sen palauttaman tuloksen.

> *"A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.*"
>
> Python Software Foundation. Unit testing framework. https://docs.python.org/3/library/unittest.html


Esimerkiksi alla oleva testitapaus on yksikkötesti, jossa tarkistetaan, että `sortEventsByStartDate` palauttaa sille annetut tapahtumat taulukkona oikeassa järjestyksessä:

```ts
test('events are sorted in correct order', () => {
    let sorted = sortEventsByStartDate([third, first, second]);

    assert.deepEqual(sorted, [first, second, third]);
});
```

Yllä oleva esimerkki edellyttää, että testiä varten on ennalta luotu tapahtumat `first`, `second` ja `third`. Voit tutustua testin konkreettiseen toteutukseen [aikaisemman tehtävän testeissä](https://github.com/harjoitukset/typescript-sorting-and-filtering/blob/main/src/sorting.test.ts).


## JS-koodin yksikkötestaaminen

Koodin testaamiseksi tarvitsemme testaustyökalun, joka voi olla esimerkiksi [Jest](https://jestjs.io/) tai [Mocha](https://mochajs.org/). [Facebookin kehittämän Jestin](https://github.com/facebook/jest) suosio on erityisesti React-kirjaston myötä noussut niin suureksi, että olemme valinneet tälle kurssille työkaluksi Jest:in.

Seuraavissa vaiheissa seuraamme Jestin dokumentaatiossa [https://jestjs.io/docs/getting-started](https://jestjs.io/docs/getting-started) olevia työvaiheita.

Voit asentaa Jest-työkalun itsellesi komennolla:

```sh
$ npm install --save-dev jest
```

### TypeScript-tuki

Jest:in avulla voidaan testata niin "tavallista" JS-koodia, TS-koodia kuin React- ja Express-sovelluksia. Hyödyntääksesi testeissäsi TypeScriptiä ja testataksesi TypeScript-kielistä koodia, tarvitset kääntäjän (preprocessor), joka tulkitsee lennossa TypeScript-kieliset lähdekoodit JavaScript-muotoon:

> *"[ts-jest](https://github.com/kulshekhar/ts-jest) is a TypeScript preprocessor with source map support for Jest that lets you use Jest to test projects written in TypeScript."*
>
> https://jestjs.io/docs/getting-started#via-ts-jest

`ts-jest` asentuu projektiin kehityksenaikaiseksi riippuvuudeksi seuraavasti:

```sh
$ npm install --save-dev ts-jest
```


### Jest:in tyyppimääritykset

> *"You can use type definitions which ships with Jest and will update each time you update Jest. Install the `@jest/globals` package."*
>
> https://jestjs.io/docs/getting-started#type-definitions

```sh
$ npm install --save-dev @jest/globals
```


### Jest config file

> *"By default, Jest can run without any config files, but it will not compile `.ts` files. To make it transpile TypeScript with `ts-jest`, we will need to create a configuration file that will tell Jest to use a `ts-jest` preset."*
>
> https://kulshekhar.github.io/ts-jest/docs/getting-started/installation/#jest-config-file

Alla on toimivaksi havaittu yksinkertainen konfiguraatio `jest.config.js`, jonka avulla voidaan testata node.js-sovelluksia:

```ts
/** @type {import('ts-jest').JestConfigWithTsJest} */
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testPathIgnorePatterns: ['/node_modules/', '/bin/', '/build/', '/.git/'],
};
```

Huomaa, että kyseessä on JS-tiedosto eikä TypeScript-tiedosto, koska konfiguraatiota luettaessa Jest ei vielä käytä TypeScript-asetuksia. Ylimmän rivin `@type`-kommentti auttaa editoriasi tarkastamaan, että kirjoittamasi konfiguraatio on sallitun muotoinen.


### Testien suorittaminen

Jest on nyt asennettu ja konfiguroitu, joten se voidaan suorittaa tutulla `npx`-komennolla:

```sh
$ npx jest
```

Testit suoritetaan usein erillisellä `npm test`-komennolla, joka voidaan määritellä `package.json`-tiedostossa `script`-lohkoon esim. seuraavasti:

```diff
 "scripts": {
+  "test": "jest"
-  "test": "echo \"Error: no test specified\" && exit 1"
 }
```

Halutessasi voit määritellä Jest-työkalulle myös lisäpatametreja, kuten `--verbose` ja `--coverage`, joilla saat huomattavasti kattavamman raportin testien suorituksesta:

```
"scripts": {
  "test": "jest --verbose --coverage"
}
```

`--verbose` *"Display individual test results with the test suite hierarchy."* ([jestjs.io](https://jestjs.io/docs/cli))

`--coverage` *"Indicates that test coverage information should be collected and reported in the output."* ([jestjs.io](https://jestjs.io/docs/cli))

Nyt testit voidaan suorittaa `npm test`-komennon avulla ja saamme testeistä kattavan raportin, esimeriksi:

```
$ npm test

PASS  src/filtering.test.ts
filtering events
    ✓ events with no date are excluded
    ✓ past events are excluded
    ✓ future events are excluded
    ✓ events in the range are included
    ✓ function does not modify the given array

--------------|---------|----------|---------|---------|-------------------
File          | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
--------------|---------|----------|---------|---------|-------------------
All files     |     100 |      100 |     100 |     100 |
 filtering.ts |     100 |      100 |     100 |     100 |
--------------|---------|----------|---------|---------|-------------------
Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
Snapshots:   0 total
Time:        3.224 s
```



## Testien kattavuus

Testien kattavuutta voidaan mitata lukuisilla eri tavoilla. Tyypillisiä tapoja on mitata testeissä suoritettujen rivien tai vaihtoehtoisten suorituspolkujen määrää. Edellä olevassa raportissa Jest on tilastoinut lausekkeet, suorituspolut, funktiot ja rivit. Vaikka testaisit ohjelmasi kaikki rivit, on silti mahdollista, että et ole tullut testanneeksi kaikkia suorituspolkuja, mikäli yksittäiset rivit sisältävät itsessään eri suorituspolkuja:

```ts
let name = person.names?.first ?? 'anonymous';
```

### Totuusarvojen vertailu

JavaScriptissä vertailuoperaatiot tehdään pääsääntöisesti kolmella merkillä eli `===` tai `!==`. Kolmen merkin vertailuoperaatiot tarkastavat, että vertailtavien arvojen tyyppi on sama. Mikäli tyyppitarkastus jätetään tekemättä eli vertaillaan kahdella merkillä `==`, vertailee JavaScript eri tyyppisiä arvoja toisinaan hyvin epäloogisesti.

Voit tutustua aiheeseen syvällisemmin artikkelissa [Equality comparisons and sameness (MDN web docs)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) tai YouTube-videolla [JavaScript == VS === (Web Dev Simplified)](https://www.youtube.com/watch?v=C5ZVC4HHgIg).


### Vertailu Jest:llä

Jest-testaustyökalussa on oma [expect](https://jestjs.io/docs/expect)-funktionsa, jota voidaan käyttää arvojen vertailemiseksi. `expect` nodattaa suosittua ["BDD"-syntaksia](https://en.wikipedia.org/wiki/Behavior-driven_development), jossa testattavat kutsut ja niihin vertailtavat arvot ketjutetaan metodikutsuilla sillä tavoitteella, että ne muistuttaisivat selkokielisiä lauseita:

```ts
import { expect } from '@jest/globals';


// https://jestjs.io/docs/getting-started
test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});
```

Metodikutsujen ketjuttaminen saattaa kuitenkin helposti edellyttää ohjelmarakenteita, joita kehittäjä ei normaalisti ohjelmakoodissaan käyttäisi, kuten:

```ts
// https://jestjs.io/docs/expect#expectnotarraycontainingarray
const expected = ['Samantha'];

it('matches if the actual array does not contain the expected elements', () => {
    expect(['Alice', 'Bob', 'Eve']).toEqual(
        expect.not.arrayContaining(expected),
    );
});
```

Tällä oppitunnilla poikkeamme tyypillisistä Jest-esimerkeistä ja käytämme Node.js:n standardikirjaston [assert-moduulia](https://nodejs.org/api/assert.html), joka on yhdenmukaisempi mm. JUnit- ja pytest-kirjastojen kanssa:

```ts
import { strict as assert } from 'node:assert';
```

Yllä `import`-käskyllä `assert`-moduulista on tuotu `strict`-niminen objekti, jonka nimeksi on asetettu tuttu `assert`. Strict-objektin avulla kaikki vertailut tehdään oikeaoppisesti esim. `===`-syntaksilla `==`-syntaksin sijasta.

> *"In strict assertion mode, non-strict methods behave like their corresponding strict methods."*
>
> https://nodejs.org/api/assert.html#strict-assertion-mode

Tällä tunnilla käytämme `assert`-syntaksia, koska sen avulla on luontevampaa käyttää testeissä samankaltaisia rakenteita, kuin mitä olemme tottuneet käyttämään varsinaisen ohjelmakoodin toteutuksessa:

```ts
import { expect } from '@jest/globals';
import { strict as assert } from 'node:assert';

// ...

// BDD (https://jestjs.io/docs/getting-started):
expect(sum(1, 2)).toBe(3);

// Assert:
assert.equal(sum(1, 2), 3);
```

```ts
// BDD (https://jestjs.io/docs/expect#expectnotstringcontainingstring):
expect('How are you?').toEqual(expect.not.stringContaining('Hello world!'));

// Assert:
assert.equal('How are you?'.includes('Hello world!'), false);
```

Saat halutessasi käyttää omissa ratkaisuissasi kumpaa tahansa syntaksia.


### Taulukoiden vertailu (JS / TS)

Taulukoita vertailtaessa JavaScript tutkii, onko kyseessä sama taulukko, mutta __taulukoiden sisältöjä ei vertailla.__

```js
> [1, 2, 3] === [1, 2, 3]
false
```

Yllä kahden taulukon vertailu tuottaa siis tulokseksi `false`, vaikka taulukoiden sisältö on sama. Jos taulukon sisältöä halutaan vertailla testeissä, voidaan se tehdä esimerkiksi [`assert.deepEqual`](https://nodejs.org/api/assert.html#assertdeepequalactual-expected-message)-metodilla:

```ts
assert.deepEqual([1, 2, 3], [1, 1 + 1, 1 + 1 + 1]);
```


### Olioiden vertailu

Kuten taulukoiden kanssa, myös olioita vertailtaessa tarkastetaan ovatko oliot samat, eli __olioiden sisältöjä ei vertailla.__

```js
> { language: 'TypeScript' } === { language: 'TypeScript' }
false
```

Eri kielet toimivat vertailujen osalta eri logiikalla. Esimerkiksi Python vertailee automaattisesti listojen ja sanakirjojen sisältöä, kun taas JavaScript ja Java eivät.

`deepEqual`-metodi vertailee rekursiivisesti myös sille annettuja olioita:

```js
assert.deepEqual({ language: "JavaScript" }, { language: "Java" + "Script" });
```
https://nodejs.org/api/assert.html#assert_assert_deepstrictequal_actual_expected_message


## Yksikkötestauksen haasteet

Ohjelman rakenteesta riippuen sen testaaminen voi olla hyvin hankalaa. Esimerkiksi globaalit muuttujat, ulkoiset riippuvuudet ja "spagettikoodi" vaikeuttavat testausta merkittävästi. Jos testattavassa koodissa tehdään esimerkiksi HTTP-pyyntöjä tai tietokantakyselyjä, näiden operaatioiden tulokset vaikuttavat testien tuloksiin, joten testattavan aineiston muuttuessa myös testien tulokset voivat muuttua, vaikka koodi edelleen toimisi toivotulla tavalla.

Tällaisia riippuvuuksia korvataan tyypillisesti testien aikana testikohtaisilla *mock*-toteutuksilla, joista voit lukea lisää esim. Jest:in dokumentaatiosta: https://jestjs.io/docs/mock-function-api.


<!--## Testidata
Test fixtures.
-->


## Integraatiotestaus

> *"Integraatiotestauksessa testataan useiden komponenttien yhteistoimintaa tavoitteena löytää virheitä, jotka eivät tulleet esiin yksikkötesteissä. Testeissä suoritetaan tiettyjä suorituspolkuja, jotka hyödyntävät useita eri yksiköitä tai laajempia komponentteja, ja tarkastellaan toiminnan tuloksia."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. Testauksen tasot. <!--http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot-->

Koska edellisissä testeissä käytimme itse luotua keinotekoista dataa, ei testit välttämättä paljasta kaikkia virheitä, jotka ilmenevät rajapinnan oikeassa datassa. Siksi on tärkeää testata myös oman ohjelmamme ja rajapinnan välistä yhteistoimintaa integraatiotestillä.

Integraatiotestit voivat olla luonteeltaan yksikkötestejä monimutkaisempia ja hitaampia, joten niitä suoritetaan tyypillisesti keskitetyssä CI-järjestelmässä (continuous integration) eikä välttämättä vain kehittäjän omalla työasemalla.

Integraatiotestejä voidaan toteuttaa samoilla teknologioilla kuin yksikkötestejä. Käytännössä voisimme toteuttaa integraatiotestin oman sovelluksemme ja JSON-rajapinnan välille kirjoittamalla samankaltaisen testin kuin aikaisemmin, mutta ilman mock-vastausta.


## Järjestelmätestaus

> *"Järjestelmätestauksessa testataan kokonaista ohjelmaa, ja tarkastellaan vastaako ohjelma sille asetettuja vaatimuksia ja käyttötarkoitusta. Aitoon ympäristöön kuuluvat mm. käytettävä laitteisto, tietokannat ja käyttäjät."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. Testauksen tasot <!--http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot-->

Järjestelmätestauksella varmistetaan usein monivaiheisia käyttötapauksia. Testattava käyttötapaus voisi pitää sisällään esimerkiksi kirjautumisen järjestelmään, jonkin datan muokkaamisen ja muokatun datan tarkastelemisen.

Järjestelmätestejä tehdäänkin usein eri työkaluilla kuin yksikkötestejä. Yksi järjestelmätesteissä hyödyllinen testityökalu on kotimaista alkuperää oleva [Robot Framework](https://robotframework.org/), jolla voidaan erilaisten laajennusten kanssa testata verkkosivuja tai vaikka matkapuhelinverkkoja. Robot Frameworkilla on oma kielensä, jolla testitapaukset voivat näyttää esim. tältä: https://github.com/robotframework/WebDemo/blob/master/login_tests/valid_login.robot.


<!--
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
-->