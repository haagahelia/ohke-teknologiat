
# TypeScript

> *"TypeScript is a language for application-scale JavaScript. TypeScript adds optional types to JavaScript that support tools for large-scale JavaScript applications for any browser, for any host, on any OS. TypeScript compiles to readable, standards-based JavaScript."*
>
> https://github.com/microsoft/TypeScript/

TypeScriptin ominaisuuksia:

- [x] JavaScriptin laajennos
- [x] Vahvasti tyypitetty kieli
- [x] Sisältää jo etukäteen JavaScriptin tulevia ominaisuuksia: "future JavaScript"
- [x] Microsoftin kehittämä, [mutta avointa lähdekoodia](https://github.com/microsoft/TypeScript/blob/main/LICENSE.txt)
- [x] Yhteensopiva olemassa olevien JavaScript-sovellusten ja NPM-pakettien kanssa
- [x] Käännettävissä yhteensopivaksi myös JavaScriptin vanhojen versioiden kanssa

https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html

<!--StackOverflow 2022 developer survey: https://survey.stackoverflow.co/2022-->

## Tunnin aihe

Tällä tunnilla perehdymme TypeScriptin ominaisuuksiin ja työkaluihin. Kirjoittamme TS-koodia ilman muita riippuvuuksia, kuten Reactia ja Express:iä, jotta aihe pysyy hieman yksinkertaisempana.


## Suositellut videot

Mikäli opiskelet tämän viikon aiheen itsenäisesti, suosittelemme perehtymään seuraaviin videoihin:

**[Programming with Mosh: TypeScript Tutorial for Beginners](https://www.youtube.com/watch?v=d56mG7DezGs)**

"TypeScript Tutorial for Beginners. Learn TypeScript to write better large-scale JavaScript apps. This tutorial helps you get started quickly."

**[Fireship: TypeScript - The Basics](https://www.youtube.com/watch?v=ahCwqrYpIuM)**

"TypeScript has forever altered the lives of JavaScript developers. Learn why TS is so awesome and the basic concepts required to be successful using it."

**[How to use TypeScript with React... But should you?](https://www.youtube.com/watch?v=ydkQlJhodio)**

"Learn how to setup React with TypeScript. Compare the pros and cons of using TypeScript in an React project."


## TypeScriptin asentaminen

TypeScript voidaan asentaa joko globaalisti koko käyttöjärjestelmään tai paikallisesti yksittäiseen projektiin. Globaali asennus [jakaa mielipiteitä](https://github.com/loopbackio/loopback.io/issues/509) ja tämän kurssin esimerkeissä asennus tehdään aina paikallisesti. Paikallisen asennuksen myötä koko projekti asentuu kerralla `npm install`-komennolla ja kaikilla kehittäjillä on käytössään sama versio TypeScriptistä.

> *"TypeScript is available as a package on the npm registry available as "typescript".*
>
> *You will need a copy of Node.js as an environment to run the package. Then you use a dependency manager like npm, yarn or pnpm to download TypeScript into your project.*"
>
> ```
> npm install typescript --save-dev
> ```
>
> *"You can then run the TypeScript compiler using one of the following commands:*"
>
> ```
> npm run tsc
> npx tsc
> yarn tsc
> pnpm tsc
> ```
>
> https://www.typescriptlang.org/download

Asennuksen jälkeen `package.json`-tiedostosi näyttää esim. seuraavalta:

```json
{
  "devDependencies": {
      "typescript": "^4"
  }
}
```

Kuten yltä huomaat, TypeScript asennetaan development-vaiheen riippuvuudeksi. TypeScriptiä ei tarvita varsinaisessa tuotantoympäristössä lainkaan, koska koodi käännetään ensin JavaScriptiksi, jota suoritetaan sellaisenaan esimerkiksi selaimessa tai Node.js-ympäristössä.

<!--
JavaScriptin päivämäärien ongelmat

Taulukoiden vertailu

Minimin ja maksimin etsiminen

Numeroiden sorttaus

case leftpad

jne...

```ts
let a = ['c', 'b', 'a'];
let b = [42, 10, 2, 55];

a.sort();
b.sort();

// a + b
let c = [...a, ...b];

c.forEach(x => {
    if (typeof x === 'string') {
        console.log(x.toUpperCase());
    } else {
        console.log(x);
    }
});
```

Joko-tai -tyyliset tyypit:

type Index = number | undefined;

Etäisyyden lisääminen olemassa olevaan tyyppiin:

type PlaceWithDistance = Place & { distance: number };
-->

## Kääntäminen / transpilointi

TypeScriptin omissa dokumenteissa käytetään pääsääntöisesti termiä "kääntäminen" (compiling), kun puhutaan TS-koodin muuntamisesta JS-koodiksi. Kääntämiselle tarkoitetaan kuitenkin perinteisesti operaatiota, jossa ihmisen luettava lähdekoodi muunnetaan matalamman abstraktiotason muotoon, joka on tyypillisesti konekielistä ja ihmisen vaikeasti luettavaa. TS-koodi käännetään kuitenkin saman abstraktiotason JavaScript-koodiksi, joten monissa lähteissä tästä käytetään termiä "transpilointi" (transpiling).

Lue lisää TypeScriptin työkaluista artikkelista [Tooling in 5 minutes](https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html).

TypeScript-koodin transpilointia tai kääntämistä voidaan kokeilla kätevästi sivulla [TypeScript Playground](https://www.typescriptlang.org/play).

Transpilointi mahdollistaa viimeisintä syntaksia hyödyntävän TypeScript-koodin muuntamisen yhteensopivaksi myös vanhojen JS-versioiden kanssa. [Kokeile esimerkiksi transpiloida TS-koodia, jossa esiintyy moderneja ominaisuuksia kuten `async` tai `await`](https://www.typescriptlang.org/play?target=0#code/MYewdgzgLgBA5gUygVQggThGBeGBDCATzGBgAoBKHAPhgG0BvGASwBMAuGARgBoYw8AWwScA5AEEANs2AJRMAL4BdANxA).


## TypeScript-työkalut

Monet JS-koodin kehittämiseksi käytettävät työkalut soveltuvat myös TS-koodin kehitykseen.

### Npx

> *"\[npx\] command allows you to run an arbitrary command from an npm package (either one installed locally, or fetched remotely), in a similar context as running it via `npm run`.*"
>
> https://docs.npmjs.com/cli/v9/commands/npx

```bash
$ tsc       # edellyttää TypeScriptin asennusta globaalisti
$ npx tsc   # suorittaa `tsc`-komennon paikallisesta asennuksesta
```

### Ts-node

> *"`ts-node` is a TypeScript execution engine and REPL for Node.js. It JIT transforms TypeScript into JavaScript, enabling you to directly execute TypeScript on Node.js without precompiling. "*
>
> https://www.npmjs.com/package/ts-node

`ts-node` mahdollistaa TypeScript-koodin suorittamisen ilman etukäteen tehtävää käännösvaihetta:

```bash
$ npx ts-node src/skripti.ts
```

### Tsc

Jos haluat kääntää kirjoittamasi TypeScript-kielisen ohjelman lähdekoodit JavaScriptiksi, onnistuu se `tsc`-komennolla (TypeScript compiler):

```
$ npx tsc
```

`tsc`-komento kääntää kirjoittamasi TypeScript-tiedostot JavaScript-tiedostoiksi, jotka voidaan suorittaa Node.js:llä tai selaimessa aivan kuten mitkä tahansa `.js`-tiedostot:

```
$ node helloWorld.js
```


### Tsconfig.json

> *"The presence of a tsconfig.json file in a directory indicates that the directory is the root of a TypeScript project. The tsconfig.json file specifies the root files and the compiler options required to compile the project"*
>
> https://www.typescriptlang.org/docs/handbook/tsconfig-json.html

`tsconfig.json`-asetustiedostoon voidaan määritellä lukuisia kääntäjän toimintaan vaikuttavia asetuksia. Voit luoda itsellesi uuden `tsconfig.json`-tiedoston `tsc`-komennon avulla:

```bash
$ npx tsc --init
```

Monet tiedoston asetukset liittyvät kääntäjän tekemiin tarkastuksiin, kuten siihen, sallitaanko funktion parametreissa tai paluuarvoissa puuttuvia tietotyyppejä. Kääntäjän tekemät tarkastukset ja varoitukset ovat  lähtökohtaisesti hyödyllisiä, joten suosittelemme hyödyntämään niitä laajasti. `strict`-asetuksella saadaankin asetettua kerralla monet erilliset asetukset päälle:

> *"The strict flag enables a wide range of type checking behavior that results in stronger guarantees of program correctness. Turning this on is equivalent to enabling all of the strict mode family options, which are outlined below. You can then turn off individual strict mode family checks as needed."*
>
> https://www.typescriptlang.org/tsconfig#strict

Minimalistinen mutta toimiva asetustiedosto voi näyttää esimerkiksi tältä:

```js
/* Visit https://aka.ms/tsconfig to read more about this file */
{
    "compilerOptions": {
        /* Set the JavaScript language version for emitted JavaScript
         * and include compatible library declarations. */
        "target": "es2016",

        /* Specify the root folder within your source files. */
        "rootDir": "./src/",

        /* Specify an output folder for all emitted files. */
        "outDir": "./build/",

        /* Emit additional JavaScript to ease support for importing CommonJS modules.
         * This enables 'allowSyntheticDefaultImports' for type compatibility. */
        "esModuleInterop": true,

        /* Enable all strict type-checking options. */
        "strict": true,
    }
}
```

<!--https://www.contentful.com/blog/what-is-typescript-and-why-should-you-use-it/-->


## Tyypit

TypeScriptissä on valmiit tyypit `string`, `number` ja `boolean`, jotka vastaavat JavaScriptin arvoja:

```ts
// merkkijonot eli 'string'
let language: string = 'TypeScript';

// 'number' käsittää sekä kokonais- että liukuluvut:
let wholeNumber: number = 2023;
let decimalNumber: number = 3.14;

// taulukot voidaan määritellä joko `tyyppi[]` tai `Array<tyyppi>`
let positive: number[] = [1, 2, 3, 4];
let negative: Array<number> = [-1, -2, -3, -4];
```

Tyyppien määrittely tällä tarkkuudella on kuitenkin usein tarpeetonta, koska TypeScript osaa päätellä asiayhteydestä mm. muuttujien sekä funktioiden paluuarvojen tyypit.

> *"For the most part you don’t need to explicitly learn the rules of inference. If you’re starting out, try using fewer type annotations than you think - you might be surprised how few you need for TypeScript to fully understand what’s going on."*
>
> https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

Nämä tyypit päätellään automaattisesti, joten tyyppejä ei tarvitse itse erikseen mainita:

```ts
let language = 'TypeScript';

let wholeNumber = 2023;
let decimalNumber = 3.14;

let positive = [1, 2, 3, 4];
let negative = [-1, -2, -3, -4];
```

### Funktioiden tyypit

> *"Functions are the primary means of passing data around in JavaScript. TypeScript allows you to specify the types of both the input and output values of functions."*
>
> https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions

```ts
// funktioiden parametrien tyypit tulee määritellä eksplisiittisesti:
function shout(str1: string): string {
    return str1.toUpperCase() + '!!!';
}
```

Yllä paluuaron tyyppi `string` voidaan jättää myös TypeScriptin itse pääteltäväksi.


### Any ja unknown

Toisinaan datan tyyppi ei ole tiedossa tai sillä ei ole merkitystä:

```ts
// `any` tyyppiä voidaan käyttää silloin, kun arvon tyypillä ei ole merkitystä:
function logAnything(thing: any) {
    console.log(new Date(), thing);
}

// usein on kuitenkin parempi käyttää tyyppiä `unknown`:
function logUnknown(thing: unknown) {
    console.log(new Date(), thing);
}
```

Edellä esitetyistä tyypeistä `any` on siinä mielessä riskialttiimpi, että sen kautta tehtävien operaatioiden osalta TS ei tee tarkastuksia:

```ts
function doSomething(bar: any) {
    bar.toUpperCase();  // ei virhe käännettäessä, mutta kaatuu suoritettaessa!
}

doSomething(1);
```

`unknown` ei puolestaan salli mahdollisesti virheellisiä operaatioita:

```ts
function doSomething(bar: unknown) {
    bar.toUpperCase();  // käännösvirhe!
}

doSomething(1);
```

Kun tiedon tyyppi ei ole ennalta tiedossa, voidaan se selvittää ajonaikaisesti ehtorakenteilla ja mm. JavaScriptin `typeof`-operaation avulla.


### Taulukot (array)

Taulukot ovat tyypitettyjä siinä missä yksittäiset muuttujat, esim. `string[]` tai `number[]`. Eri tyyppisiä arvoja lisättäessä TS luo "union"-tyyppejä, kuten `(string | number)[]`.

Seuraavat esimerkit näyttävät, miten puuttuviin arvoihin varautuminen voidaan ohittaa (`!`) ja miten tietyn arvon tyyppi voidaan itse määrittää `as`:

```ts
let faces = ['😀', '🙁'];          // string[]
let numbers = [7, 100, 42];         // number[]

let all = [...faces, ...numbers];   // (string | number)[]

// `at` saattaa palauttaa merkkijonon, numeron tai `undefined`:
let something = all.at(-1);         // something: (string | number | undefined)

// huutomerkki `!` kertoo TypeScriptille, että arvo on olemassa:
let thing = all.at(-1)!;            // thing: (string | number | undefined)

// `as`-avainsanalla voidaan ohittaa tyypin päättely ja kertoa se itse:
let hundred = all.at(-1) as number; // hundred: number

console.table({ something, thing, hundred });
```

Vaikka edellä kolmen viimeisen muuttujan tyyppi onkin eri, on niissä luonnollisesti tasan samat arvot, eli taulukon viimeinen numero:

```
┌───────────┬────────┐
│  (index)  │ Values │
├───────────┼────────┤
│ something │   42   │
│   thing   │   42   │
│  hundred  │   42   │
└───────────┴────────┘
```

### Omat tyypit

TypeScriptistä on merkittävää hyötyä silloin, kun omassa ohjelmalogiikassa hyödynnetään eri tyyppisiä olioita. Yksinkertaisimmillaan "oliotyyppi" voidaan määritellä suoraan muuttujaan:

```ts
let user: { id: number, name: string } = { id: 1, name: 'Alice'};
```

Tyypin määritteleminen muuttujaan on kuitenkin usein huono idea, erityisesti siksi, että tyyppiä joudutaan määrittelemään tällöin jokaiseen muuttujaan erikseen. Tyypeille voidaankin määritellä "aliaksia", jotka tekevät niistä uudelleenkäytettäviä:

```ts
type User = {
    id: number;
    name: string;
};

let user1: User = { id: 1, name: 'Alice' };
let user2: User = { id: 2, name: 'Bob' };
```

Eri tyypeissä voi olla myös valinnaisia attribuutteja:

```ts
type User = {
    id: number;
    name: string;
    email?: string;  // `string` tai `undefined`
};

let user1: User = { id: 1, name: 'Alice' };
let user2: User = { id: 2, name: 'Bob', email: 'bob@example.com' };
```


### "Union" (|) ja "intersection" (&)

Uusia tyyppejä voidaan myös luoda yhdistelemällä vakioita tai olemassa olevia tyyppejä:

```ts
type Size = 's' | 'm' | 'l';

type Shirt = {
    size: Size;
}

let smallShirt = { size: 's' };
```

https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types

<!-- narrowing typeof x === y -->


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

> *Record<Keys, Type>*
>
> *"Constructs an object type whose property keys are Keys and whose property values are Type. This utility can be used to map the properties of a type to another type."*
>
> https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type

```ts
let weekdays: Record<string, string> = {};
weekdays['monday'] = 'maanantai';
weekdays['tuesday'] = 'tiistai';

console.log(weekdays);              // { monday: 'maanantai', tuesday: 'tiistai' }
console.log('tuesday' in weekdays); // true
console.log(weekdays['wednesday']); // undefined
```

## Valinnaisia harjoituksia

Voit tutustua itsenäisesti TypeScriptin tyyppijärjestelmään esimerkiksi sivustolla https://typescript-exercises.github.io/.


## Palautettava tehtävä

Tämän viikon tehtävässä harjoittelemme TypeScriptin käyttöä postinumeroaineiston käsittelyn merkeissä. Katso tarkemmat ohjeet Teamsin tehtävät-välilehdeltä.

