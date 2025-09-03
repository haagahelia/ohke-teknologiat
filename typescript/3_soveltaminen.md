# TypeScript-oppitunti 3: tyyppien soveltaminen koodin testaaminen ja express-kirjasto

Tässä oppitunnissa tutustumme TypeScriptin edistyneisiin tyyppeihin, kuten union- ja intersection-tyyppeihin, geneerisiin tyyppeihin sekä tyyppien yhdistämiseen. Lisäksi opettelemme kirjoittamaan yksikkötestejä JavaScript/TypeScript-koodille käyttäen Jest-testauskehystä. Lopuksi tutustumme lyhyesti Express.js-kehykseen, joka on suosittu web-sovellusten kehitykseen tarkoitettu Node.js-kirjasto.

Aiheen opiskelun jälkeen osaat kirjoittaa TS/JS-funktioillesi yksikkötestit ja tiedät mistä lähteä liikkeelle, kun sinulle tulee tarve kirjoittaa automatisoituja testejä. Osaat myös huomioida testausnäkökulmaa jäsentäessäsi TS/JS-ohjelmiasi eri moduuleihin ja funktioihin.



## JS-koodin yksikkötestaaminen

Koodin testaamiseksi tarvitsemme testaustyökalun, joka voi olla esimerkiksi [Jest](https://jestjs.io/) tai [Mocha](https://mochajs.org/). [Facebookin kehittämän Jestin](https://github.com/facebook/jest) suosio on erityisesti React-kirjaston myötä noussut niin suureksi, että olemme valinneet tälle kurssille työkaluksi Jest:in.

Seuraavissa vaiheissa seuraamme Jestin dokumentaatiossa [https://jestjs.io/docs/getting-started](https://jestjs.io/docs/getting-started) olevia työvaiheita.


### Suositellut videot

**[What is Automated Testing? - The Startup Lab](https://www.youtube.com/watch?v=Nd31XiSGJLw)**

[![What is Automated Testing?](https://img.youtube.com/vi/Nd31XiSGJLw/mq3.jpg)](https://www.youtube.com/watch?v=Nd31XiSGJLw)

> *"In this video we start diving into the world of quality assurance and discuss automated testing for our web and mobile applications..."*
>
> The Startup Lab. [What is Automated Testing?](https://www.youtube.com/watch?v=Nd31XiSGJLw)

&nbsp;


**[Introduction To Testing In JavaScript With Jest - Web Dev Simplified](https://www.youtube.com/watch?v=FgnxcUQ5vho)**

[![Introduction To Testing In JavaScript With Jest - Web Dev Simplified](https://img.youtube.com/vi/FgnxcUQ5vho/mq2.jpg)](https://www.youtube.com/watch?v=FgnxcUQ5vho)

&nbsp;


**[Jest Basics - Web Dev Simplified](https://courses.webdevsimplified.com/view/courses/javascript-simplified-advanced/729109-Testing/2126286-38-Jest-Basics)**

<a href="https://courses.webdevsimplified.com/view/courses/javascript-simplified-advanced/729109-Testing/2126286-38-Jest-Basics"><img src="https://d31ezp3r8jwmks.cloudfront.net/uxoz8jjx52plpakesnwh34d3h25x" width="320" height="180"></a>


### Asentaminen

Voit asentaa Jest-työkalun itsellesi komennolla:

```sh
$ npm install --save-dev jest
```

Jest asennetaan kehitysaikaiseksi riippuvuudeksi (`--save-dev`), koska se on tarkoitettu vain kehitysvaiheessa käytettäväksi eikä sitä tarvita tuotantoympäristössä.


### TypeScript-tuki

Jest:in avulla voidaan testata niin "tavallista" JS-koodia, TS-koodia kuin React- ja Express-sovelluksia. Hyödyntääksesi testeissäsi TypeScriptiä ja testataksesi TypeScript-kielistä koodia, tarvitset kääntäjän (preprocessor), joka tulkitsee lennossa TypeScript-kieliset lähdekoodit JavaScript-muotoon:

> *"[ts-jest](https://github.com/kulshekhar/ts-jest) is a TypeScript preprocessor with source map support for Jest that lets you use Jest to test projects written in TypeScript."*
>
> https://jestjs.io/docs/getting-started#via-ts-jest

`ts-jest` sekä Jestin tyyppimääritykset asentuvat projektiin kehityksenaikaisiksi riippuvuuksiksi seuraavasti:

```sh
$ npm install --save-dev ts-jest @types/jest
```


### Jest:in tyyppimääritykset

> *"You can use type definitions which ships with Jest and will update each time you update Jest. Install the `@jest/globals` package."*
>
> https://jestjs.io/docs/getting-started#type-definitions

```sh
$ npm install --save-dev @jest/globals
```

Nyt Jestin funktiot voidaan ottaa käyttöön testeissä:

```ts
import { describe, it, expect } from '@jest/globals';
```


### Jest config file

> *"By default, Jest can run without any config files, but it will not compile `.ts` files. To make it transpile TypeScript with `ts-jest`, we will need to create a configuration file that will tell Jest to use a `ts-jest` preset."*
>
> https://kulshekhar.github.io/ts-jest/docs/getting-started/installation/#jest-config-file

Alla on toimivaksi havaittu yksinkertainen konfiguraatio `package.json`-tiedostoon, jonka avulla voidaan testata node.js-sovelluksia:

```ts
{
  "jest": {
    "preset": "ts-jest",
    "testEnvironment": "node",
    "testPathIgnorePatterns": [
      "/node_modules/",
      "/build/",
      "/.git/"
    ]
  }
}
```

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

 PASS  src/creditCard.test.ts
  maskCreditCardNumber
    √ should mask a 16-digit credit card number with default 4 visible digits (5 ms)
    √ should mask a 16-digit credit card number with custom visible digits (1 ms)
    √ should handle short credit card numbers (1 ms)
    √ should handle empty string (1 ms)
    √ should handle showNumbers larger than card length (1 ms)
    √ should mask Amex style card (1 ms)

---------------|---------|----------|---------|---------|-------------------
File           | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
---------------|---------|----------|---------|---------|-------------------
All files      |   91.66 |       50 |     100 |   91.66 |
 creditCard.ts |   91.66 |       50 |     100 |   91.66 | 7
---------------|---------|----------|---------|---------|-------------------
Test Suites: 1 passed, 1 total
Tests:       6 passed, 6 total
Snapshots:   0 total
Time:        1.415 s
```


### Testien kattavuus

Testien kattavuutta voidaan mitata lukuisilla eri tavoilla. Tyypillisiä tapoja on mitata testeissä suoritettujen rivien tai vaihtoehtoisten suorituspolkujen määrää. Edellä olevassa raportissa Jest on tilastoinut lausekkeet, suorituspolut, funktiot ja rivit. Vaikka testit suorittivat kaikki funktiot, ei se tullut testanneeksi kaikkia rivejä ja suorituspolkuja.

Testatussa funktiossa on myös (ainakin) yksi bugi, joka jäi löytämättä.

> [!NOTE]
> Tuntitehtävä: suorita testit ja tarkista kattavuusraportti. Selvitä, mitkä rivit tai suorituspolut jäivät testaamatta.
>
> Kirjoita testit puuttuville suorituspoluille ja korjaa niillä löytämäsi bugi(t).
>
> https://stackblitz.com/github/ohjelmistokehitys/ts-oppitunti-2025


### Erilaisten arvojen vertailu

JavaScriptissä vertailuoperaatiot tehdään pääsääntöisesti kolmella merkillä eli `===` tai `!==`. Kolmen merkin vertailuoperaatiot tarkastavat, että vertailtavien arvojen tyyppi on sama. Mikäli tyyppitarkastus jätetään tekemättä eli vertaillaan kahdella merkillä `==`, vertailee JavaScript eri tyyppisiä arvoja toisinaan hyvin epäloogisesti.

```js
1 == ["1"];     // true ❌
0 == [];        // true ❌

1 === ["1"];    // false 🆗
```

Voit tutustua aiheeseen syvällisemmin artikkelissa [Equality comparisons and sameness (MDN web docs)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) tai YouTube-videolla [JavaScript == VS === (Web Dev Simplified)](https://www.youtube.com/watch?v=C5ZVC4HHgIg). Myös tämä [JavaScript-Equality-Table](https://dorey.github.io/JavaScript-Equality-Table/)-taulukko havainnollistaa erinomaisesti eri arvojen käyttäytymistä `===`-, `==`- ja `if`-operaatioissa.


### Olioiden vertailu

Perustietotyyppien vertailu on melko suoraviivaista, mutta olioiden ja taulukoiden vertailu voi olla haastavampaa:

```js
// This comparison will always be 'false' since JavaScript
// compares arrays by reference and not their content:
const numbers1 = [1, 2, 3];
const numbers2 = [1, 2, 3];
numbers1 === numbers2;

// The same goes for objects. This comparison is always 'false':
const alice1 = { name: 'Alice' };
const alice2 = { name: 'Alice' };
alice1 === alice2;
```


### Vertailu Jest:llä

Jest-testaustyökalussa on oma [expect](https://jestjs.io/docs/expect)-funktionsa, jota voidaan käyttää arvojen vertailemiseksi. `expect` nodattaa suosittua ["BDD"-syntaksia](https://en.wikipedia.org/wiki/Behavior-driven_development), jossa testattavat kutsut ja niihin vertailtavat arvot ketjutetaan metodikutsuilla sillä tavoitteella, että ne muistuttaisivat selkokielisiä lauseita:

```ts
import { test, expect } from '@jest/globals';

// https://jestjs.io/docs/getting-started
test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);              // ok
});

test('array equality', () => {
    expect([1, 2, 3]).toEqual([1, 2, 3]);   // ok
});
```

## TypeScriptin soveltavat tyypit

Uusien tyyppien määritteleminen olemassa olevia tyyppejä yhdistelemällä tai soveltamalla on melko tavanomaista TypeScriptissä. Yksinkertaisimmillaan voit määritellä uuden tyypin, joka on sama kuin jokin olemassa oleva tyyppi:

```ts
type ApiKey = string
```

Tämän jälkeen voit käyttää `ApiKey`-tyyppiä kuten mitä tahansa muuta tyyppiä:

```ts
function getApiKey(): ApiKey {
    return '12345';
}
```


### typeof

Mikäli ohjelmakoodissa on olemassa jo jokin vakioarvo, sen tyypistä voidaan muodostaa kätevästi uudelleenkäytettävä alias `typeof`-operaattorilla. Otetaan esimerkiksi seuraava olio, joka sisältää kolme muuttujaa, kaksi merkkijonoa ja yhden totuusarvon:

```ts
const takeOutTrash = {
  title: 'Take out the trash',
  description: 'Empty the trash bin and recyclables',
  completed: false,
};
```

Tätä olemassa olevaa oliota voidaan nyt hyödyntää esimerkiksi uuden `Task`-tyypin määrittelemiseksi:

```ts
type Task = typeof takeOutTrash; // tyyppi { title: string; description: string; completed: boolean; }
```

Nyt `Task`-tyyppiä voidaan käyttää missä tahansa, missä tarvitaan olio, joka sisältää `title`, `description` ja `completed`-attribuutit oikeilla tyypeillä.

Lisätietoja `typeof`-operaattorista löydät TypeScriptin [käsikirjasta](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html).

> ![NOTE]
> On hyvä huomioida, että TypeScriptin `typeof`-operaattori liittyy TypeScriptin tyyppien määrittelemiseen, kun taas [JavaScriptin `typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) on ajonaikaisesti suoritettava lauseke.
>
> Hieman epäonnisesti nämä kaksi operaatiota ovat nimetty täysin samalla tavalla, mutta tekevät eri asioita 😕:
>
> * TS: https://www.typescriptlang.org/docs/handbook/2/typeof-types.html
> * JS: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof


## keyof

TypeScriptissä voit luoda myös uuden tyypin, joka sisältää vakiot kaikista olemassa olevan toisen tyypin avaimista, eli käytännössä muuttujien nimistä. Tämä tapahtuu [`keyof`-operaattorilla](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html).

```ts
interface Color {
    red: number;
    green: number;
    blue: number;
}

type KeysOfColor = keyof Color; // red | green | blue
```

Tämä on erityisen hyödyllistä tapauksissa, joissa sinun tarvitsee käsitellä olion muuttujia, mutta et etukäteen tiedä mitä muuttujista milloinkin käytetään.

Ajattele esimerkiksi seuraavia funktioita, jotka käsittelevät värin punaista, sinistä tai vihreää komponenttia:

```ts
function incrementComponent(color: Color, component: keyof Color, percent: number) {
    color[component] *= 1 + percent / 100;
}

function swapColorComponents(color: Color, componentA: keyof Color, componentB: keyof Color) {
    [color[componentA], color[componentB]] = [color[componentB], color[componentA]];
}

let myColor: Color = { red: 255, green: 10, blue: 15 };

incrementComponent(myColor, 'blue', 10);
swapColorComponents(myColor, 'red', 'green');
```

Nyt yllä määritellyt funktiot toimivat millä tahansa värin komponentilla. TypeScript osaa silti varmistaa, että annettu merkkijono löytyy oikeasti `Color`-tyypistä, eli seuraava funktiokutsu aiheuttaisi käännettäessä virheen:

:::warning käännösvirhe
```ts
incrementComponent(myColor, 'yellow', 10);
```
**Argument of type '"yellow"' is not assignable to parameter of type 'keyof Color'**
:::


## Soveltava esimerkki

Kuten useissa muissakin tapauksissa, TypeScriptin tyyppijärjestelmä taipuu myös `typeof`- ja `keyof`-operaattoreiden kanssa moneen. Niitä voidaan siis esimerkiksi yhdistellä samaan lausekkeeseen.

Esimerkiksi seuraavassa esimerkissä luodaan olio, jossa avaimina on t-paidan kokojen lyhenteet ja arvoina koko tekstinä. Alemmalla rivillä muodostetaan uusi `Size`-tyyppi, jossa `sizes`-oliosta otetaan ensin tyyppi `typeof`-operaatiolla, ja tästä tyypistä otetaan avaimet `keyof`-operaatiolla. Lopputuloksena on `Size`-tyyppi, joka on unioni arvoista `s`, `m` ja `l`:

```ts
let sizes = {
    's': 'small',
    'm': 'medium',
    'l': 'large'
} as const;

type SizeKey = keyof typeof sizes; // 's' | 'm' | 'l'
type SizeText = typeof sizes[SizeKey]; // 'small' | 'medium' | 'large'


const someSize: SizeText = "slim"; // Error
```

Vaikka tämänkaltaiset käyttötapaukset ovat usein tarpeettomia, oikein käytettyinä niiden avulla voidaan vähentää koodin duplikointia ja edistää ylläpidettävyyttä, kun tyyppien määritykset päivittyvät automaattisesti, mikäli koodiin lisätään myöhemmin esimerkiksi uusia kokoja, kuten `xs` ja `xl`.


### Union (`number | string`)

Uusia tyyppejä voidaan myös luoda yhdistelemällä vakioita tai olemassa olevia tyyppejä:

```ts
type Size = 's' | 'm' | 'l'; // sallii vain nämä ennalta määrätyt merkkijonot

type Shirt = {
    size: Size;
}

let smallShirt = { size: 's' }; // ok

let unknownShirt = { size: 'tall' }; // käännösvirhe!
```

Yleinen käyttötapaus union-tyypeille on myös esimerkiksi joko numeron tai merkkijonon salliminen parametrina:

```ts
// https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types
function printId(id: number | string) {
  console.log("Your ID is: " + id);
}
```

### Intersection (`&`)

Uusia tyyppejä voidaan myös yhdistellä olemassa olevista tyypeistä *intersection* -operaatiolla. Seuraavassa esimerkissä on määritetty tyypit `Coordinate` ja `Address`, sekä `MapMarker`, joka sisältää molempien edellä mainittujen tyyppien attribuutit:

```ts
type Coordinate = { lat: number, lon: number };
type Address = { street: string, city: string };

type MapMarker = Address & Coordinate;

let haagaHelia: MapMarker = {
    lat: 60,
    lon: 24,
    street: 'Ratapihantie 13',
    city: 'Helsinki'
};
```

Eri tyyppien yhdistäminen voi olla kätevää esimerkiksi tapauksissa, joissa käyttäisit perintää. Esimerkiksi tietokannasta luettujen tietojen yhteiset osat `id`, `createdAt` ja `updatedAt` voidaan sisällyttää muihin tyyppeihi, kuten `Author` ja `Book`:

```ts
type Entity = {
    id: number,
    createdAt: Date,
    updatedAt: Date,
    deletedAt?: Date    // undefined if not marked as deleted
};

type Author = Entity & { name: string };
type Book = Entity & { title: string, author: Author };
```


### "Record" ja avain-arvo-pareja sisältävät oliot

JavaScriptissä olioita (object) käytetään usein avain-arvo-pareja sisältävänä map-tietorakenteena. Tämä poikkeaa edellä esitellyistä esimerkeistä siten, että avainten nimet eivät ole ennalta tiedossa, vaikka sekä avainten että arvojen tyypit tiedetäänkin. TypeScript mahdollistaa ns. [index signaturen](https://basarat.gitbook.io/typescript/type-system/index-signatures#declaring-an-index-signature), jolla voidaan määritellä objektin avainten sekä arvojen tyypit:

```ts
let emojis: { [key: string]: string } = {};
emojis['smile'] = '🙂';
emojis['laugh'] = '😄';


// objektin kaikki avaimet saadaan array:na JS:n Object.keys-metodilla:
console.log(Object.keys(emojis));   // [ 'smile', 'laugh' ]

// objektin kaikki arvot saadaan array:na JS:n Object.values-metodilla:
console.log(Object.values(emojis)); // [ '🙂', '😄' ]


// TypeScript ei takaa, että avaimelle löytyy arvoa:
console.log(emojis['angry']);       // undefined

// avain voidaan tarkastaa `in`-operaatiolla:
if ('smile' in emojis) {
    console.log(emojis['smile']);   // 🙂
}

console.table(emojis); /* ┌─────────┬────────┐
                          │ (index) │ Values │
                          ├─────────┼────────┤
                          │  smile  │  '🙂'  │
                          │  laugh  │  '😄'  │
                          └─────────┴────────┘ */

```

TypeScriptin "utility types" -tyypeistä löytyy myös valmis `Record`, jonka avulla objektin avainten ja arvojen tyypit on määritettävissä vielä astetta selkeämmin:

> ***Record<Keys, Type>***
>
> *"Constructs an object type whose property keys are Keys and whose property values are Type. This utility can be used to map the properties of a type to another type."*
>
> https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type


```ts
let weekdays: Record<string, string> = {};
weekdays['monday'] = 'maanantai';
weekdays['tuesday'] = 'tiistai';

console.log(weekdays);                  // { monday: 'maanantai', tuesday: 'tiistai' }
console.log('tuesday' in weekdays);     // true
console.log(weekdays['wednesday']);     // undefined
```


# Geneeriset tyypit

TypeScript tukee geneerisiä tyyppejä (generics) niin [tyyppien määrityksissä](https://www.typescriptlang.org/docs/handbook/2/objects.html#generic-object-types) kuin esimerkiksi [funktioiden parametreissa ja paluuarvoissa](https://www.typescriptlang.org/docs/handbook/2/functions.html#generic-functions). Lyhyesti kuvailtuna geneeriset tyypit edesauttavat koodin uudelleenkäytettävyyttä tilanteissa, joissa sama funktio tai tyyppi voi käsitellä monen tyyppistä dataa.

Aiheeseen perehtymiseksi suosittelemme seuraavaa lyhyttä videota:

[**Learn TypeScript Generics In 13 Minutes. Web Dev Simplified. YouTube**](https://www.youtube.com/watch?v=EcCTIExsqmI)


## Geneeriset funktiot

Mikäli haluat toteuttaa esimerkiksi funktion, joka palauttaa merkkijonotaulukosta satunnaisen arvon, voisit toteuttaa sen esimerkiksi seuraavasti:

```ts
/** Returns a random string from the given array of strings */
function getRandom(collection: string[]): string {
    let randomIndex = Math.trunc(Math.random() * collection.length);
    return collection[randomIndex];
}

console.log(getRandom(['kivi', 'paperi', 'sakset']));
```

Funktion parametreissa määritellään, että se saa parametrinaan merkkijonotaulukon `string[]` ja että se palauttaa merkkijonon. Funktion sisällä ei kuitenkaan ole lainkaan merkkijonoihin liittyvää logiikkaa, joten samaa koodia voitaisiin uudelleenkäyttää minkä tahansa tyyppisen taulukon käsittelemiseksi. Materiaalin [aikaisemmassa osassa](./01-tyyppijarjestelma.md) esittelimme `any`-tyypin, joka tavallaan voisi olla osa ratkaisua. Mikäli vaihtaisimme parametrin tyypiksi `any[]` ja paluuarvon tyypiksi `any`, koodi toimisi minkä tahansa tyyppisten taulukkojen kanssa. Tällöin paluuarvo olisi kuitenkin tyyppiä `any`, joka aiheuttaisi ylimääräistä työtä funktiota kutsuvassa koodissa. Sen sijaan voimme määritellä funktiolle geneerisen tyyppiparametrin, jonka avulla sekä parametrin että paluuarvon tyyppi saadaan määritettyä samaksi:

> *"In TypeScript, generics are used when we want to describe a correspondence between two values. We do this by declaring a type parameter in the function signature."*
>
> Microsoft. More on Functions. [typescriptlang.org](https://www.typescriptlang.org/docs/handbook/2/functions.html#generic-functions)

Tyyppiparametri määritellään funktion nimen ja sulkujen välissä kulmasulkujen (`<` `>`) sisällä. Tyyppiparametrin nimi voidaan valita itse, mutta tyypillisesti parametrin nimenä käytetään kirjaimia `T`, `U`, `V`...

Kun funktion otsikoksi määritellään `function getRandom<T>(collection: T[]): T` funktio hyväksyy minkä tahansa taulukon ja TypeScript tietää paluuarvon olevan aina samaa tyyppiä kuin annettu taulukko. Tämän muutoksen jälkeen funktiota voidaankin kutsua yhtä hyvin merkkijono- kuin numerotaulukon kanssa:

```ts
/** Returns a random item from the given array */
function getRandom<T>(collection: T[]): T {
    let randomIndex = Math.trunc(Math.random() * collection.length);
    return collection[randomIndex];
}

console.log(getRandom(['kivi', 'paperi', 'sakset']));
console.log(getRandom([0, 1, 2]));
```


## Geneeriset tyyppimäärittelyt

Toisinaan on myös tarpeen määritellä tyyppejä, joiden attribuutteina voi olla eri tyyppisiä arvoja. Seuraavassa koodiesimerkissä onkin määriteltynä tyyppi `Box`, jonka sisältönä voi olla eri tyyppisiä arvoja:

```ts
interface Box<Type> {
    contents: Type;
}


const greeting: Box<string> = { contents: 'hello' }

// TypeScript tarkastaa parametrisoidun tyypin ja huomaa virheen:
greeting = { contents: 1 } // error


// uusi alias `Box`-tyypille, joka sisältää merkkijonon:
type StringBox = Box<string>

const feedback: StringBox = { contents: 'good job!' }
```

Eräs hyvin yleinen parametrisoitu tyyppi on JavaScriptin `Promise`, joka käyttötapauksesta riippuen pitää sisällään eri tyyppisiä arvoja. [TypeScriptin lähdekoodissa](https://github.com/microsoft/TypeScript/blob/main/src/lib/es5.d.ts) `Promise`-tyyppi onkin määritetty seuraavasti:

```ts
interface Promise<T> {
  //...
}
```

Voit lukea aiheesta lisää [TypeScriptin käsikirjasta](https://www.typescriptlang.org/docs/handbook/2/objects.html#generic-object-types).
