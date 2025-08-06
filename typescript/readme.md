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

Lue lisää kielestä esimerkiksi sivulta https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html.


## Tunnin aihe

Tällä tunnilla perehdymme TypeScriptin ominaisuuksiin ja työkaluihin. Kirjoittamme TS-koodia ilman muita riippuvuuksia, kuten Reactia ja Express:iä, jotta aihe pysyy hieman yksinkertaisempana.


## Suositellut videot

Mikäli opiskelet tämän viikon aiheen itsenäisesti, suosittelemme perehtymään seuraaviin videoihin:

**[Programming with Mosh: TypeScript Tutorial for Beginners](https://www.youtube.com/watch?v=d56mG7DezGs)**

*"TypeScript Tutorial for Beginners. Learn TypeScript to write better large-scale JavaScript apps. This tutorial helps you get started quickly."*

**[Fireship: TypeScript - The Basics](https://www.youtube.com/watch?v=ahCwqrYpIuM)**

*"TypeScript has forever altered the lives of JavaScript developers. Learn why TS is so awesome and the basic concepts required to be successful using it."*

**[Fireship: How to use TypeScript with React... But should you?](https://www.youtube.com/watch?v=ydkQlJhodio)**

*"Learn how to setup React with TypeScript. Compare the pros and cons of using TypeScript in an React project."*

**[Don't Learn TypeScript](https://youtu.be/kRiD6ZpAN_o)**

*Spoiler alert: älä aloita opettelemalla TypeScriptin "teoriaa", vaan aloita kirjoittamalla JavaScriptiä TS-tiedostoon.*


## TypeScriptin asentaminen

TypeScript voidaan asentaa joko globaalisti koko käyttöjärjestelmään tai paikallisesti yksittäiseen projektiin. Globaali asennus [jakaa mielipiteitä](https://github.com/loopbackio/loopback.io/issues/509) ja tämän kurssin esimerkeissä asennus tehdään aina paikallisesti.

Paikallisen asennuksen etuina koko projekti riippuvuuksineen asentuu kerralla yhdellä komennolla (`npm install`) ja kaikilla kehittäjillä on käytössään sama versio TypeScriptistä. Myös mm. suositut [Vite-](https://vite.dev/) ja [Expo-työkalut](https://expo.dev/) asentavat TypeScriptin paikallisesti kuhunkin projektiin.

Paikallisen asennuksen jälkeen `tsc`-kääntäjää voidaan käyttää komennolla `npx tsc` ([npx -- execute npm package binaries](https://www.npmjs.com/package/npx)).

> *"TypeScript is available as a package on the npm registry available as "typescript". You will need a copy of Node.js as an environment to run the package. Then you use a dependency manager like npm, yarn or pnpm to download TypeScript into your project."*
>
> ```
> npm install typescript --save-dev
> ```
>
> *"You can then run the TypeScript compiler using one of the following commands:*"
>
> ```
> npm exec tsc
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
      "typescript": "^5"
  }
}
```

Kuten yltä huomaat, TypeScript asennetaan development-vaiheen riippuvuudeksi. TypeScriptiä ei tarvita varsinaisessa tuotantoympäristössä lainkaan, koska koodi käännetään ensin JavaScriptiksi, jota suoritetaan sellaisenaan esimerkiksi selaimessa tai Node.js-ympäristössä.


## Kääntäminen eli transpilointi

TypeScriptin omissa dokumenteissa käytetään pääsääntöisesti termiä "kääntäminen" (compiling), kun puhutaan TS-koodin muuntamisesta JS-koodiksi. Kääntämiselle tarkoitetaan kuitenkin perinteisesti operaatiota, jossa ihmisen luettava lähdekoodi muunnetaan matalamman abstraktiotason muotoon, joka on tyypillisesti konekielistä ja ihmisen vaikeasti luettavaa. TS-koodi käännetään kuitenkin saman abstraktiotason JavaScript-koodiksi, joten monissa lähteissä tästä käytetään termiä "transpilointi" (transpiling). [(StackOverflow: Compiling vs Transpiling)](https://stackoverflow.com/a/44932758)

TypeScript-koodin transpilointia tai kääntämistä voidaan kokeilla kätevästi sivulla [TypeScript Playground](https://www.typescriptlang.org/play).

Lue lisää TypeScriptin työkaluista artikkelista [Tooling in 5 minutes](https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html).

Transpilointi mahdollistaa viimeisintä syntaksia hyödyntävän TypeScript-koodin muuntamisen yhteensopivaksi myös vanhojen JS-versioiden kanssa. [Kokeile esimerkiksi transpiloida TS-koodia, jossa esiintyy moderneja ominaisuuksia kuten `async` tai `await`](https://www.typescriptlang.org/play?target=0#code/MYewdgzgLgBA5gUygVQggThGBeGBDCATzGBgAoBKHAPhgG0BvGASwBMAuGARgBoYw8AWwScA5AEEANs2AJRMAL4BdANxA).


## TypeScript-työkalut

Koska TypeScript ja JavaScript ovat osittain sama asia, monet JS-koodin kehittämiseksi käytettävät työkalut soveltuvat myös TS-koodin kehitykseen. Esimerkiksi VS Code sekä Node.js ja npm toimivat hyvin yhteen TypeScript-projektien kanssa.


### Npx

Jos et asentanut [TypeScript-pakettia](https://www.npmjs.com/package/typescript) globaalisti, se suoritetaan paikallisen projektin `node_modules`-hakemistosta. Tämä onnistuu joko komennolla `npm exec tsc` tai lyhyemmin `npx`-komennon avulla:

> *"\[npx\] command allows you to run an arbitrary command from an npm package (either one installed locally, or fetched remotely), in a similar context as running it via `npm run`.*"
>
> https://docs.npmjs.com/cli/v9/commands/npx

```bash
npx tsc   # suorittaa `tsc`-komennon, eikä edellytä globaalia asennusta
```

`npx`-komennon pitäisi löytyä sinulta valmiiksi, jos sinulla on `npm` asennettuna.


### Ts-node

> *"`ts-node` is a TypeScript execution engine and REPL for Node.js. It JIT transforms TypeScript into JavaScript, enabling you to directly execute TypeScript on Node.js without precompiling."*
>
> https://www.npmjs.com/package/ts-node


```bash
npm install ts-node --save-dev    # asentaa ts-noden paikallisesti

npx ts-node src/skripti.ts        # suorittaa skriptin `src/skripti.ts`

npx ts-node                       # käynnistää ts-noden REPL-tilan
```

`ts-node` mahdollistaa TypeScript-koodin suorittamisen ilman etukäteen tehtävää käännösvaihetta. Se on suosittu ja yksinkertainen työkalu, mutta sille on viime vuosien aikana tullut myös paljon kilpailijoita, kuten [tsx](https://www.npmjs.com/package/tsx). [Node.js:n viimeisimmät versiot tukevat osittain TypeScriptiä](https://nodejs.org/api/typescript.html), mutta toistaiseksi tyyppien tarkastamisen, eri moduulijärjestelmien ja `tsconfig.json`-tiedoston tuen vuoksi on suositeltavaa käyttää työkaluja kuten `ts-node` tai `tsx`.


### Tsx

> *"tsx stands for TypeScript Execute and it's a Node.js enhancement to run TypeScript.*
>
> *For starters, think of tsx as an alias to node and use it the same way."*
>
> https://tsx.is/

```bash
# https://nodejs.org/api/typescript.html
npm install --save-dev tsx
npx tsx your-file.ts 
```


### Tsc

Kun haluat kääntää kirjoittamasi TypeScript-kielisen ohjelman lähdekoodit JavaScript-kielisiksi lähdekoodeiksi, onnistuu se `tsc`-komennolla (TypeScript compiler):

```bash
npx tsc                   # kaikki .ts-tiedostot (edellyttää tsconfig-tiedostoa)
npx tsc helloWorld.ts     # yksi .ts-tiedosto
```

`tsc`-komento kääntää kirjoittamasi TypeScript-tiedostot JavaScript-tiedostoiksi, jotka voidaan suorittaa Node.js:llä tai selaimessa aivan kuten mitkä tahansa `.js`-tiedostot:

```bash
node helloWorld.js
```


### Tsconfig.json

TypeScript-kääntäjä sekä työkalut, kuten `ts-node`, tukevat lukuisia TS-koodin kääntämiseen liittyviä asetuksia. Nämä asetukset voidaan antaa komentoriviparametreina, mutta tyypillisesti niitä on niin paljon, että ne kannattaa tallentaa erilliseen asetustiedostoon.

> *"The presence of a tsconfig.json file in a directory indicates that the directory is the root of a TypeScript project. The tsconfig.json file specifies the root files and the compiler options required to compile the project"*
>
> https://www.typescriptlang.org/docs/handbook/tsconfig-json.html

`tsconfig.json`-asetustiedostoon voidaan määritellä lukuisia kääntäjän toimintaan vaikuttavia asetuksia. Voit luoda itsellesi uuden `tsconfig.json`-tiedoston `tsc`-komennon avulla:

```bash
npx tsc --init
```
```
Created a new tsconfig.json with:

  target: es2016
  module: commonjs
  strict: true
  esModuleInterop: true
  skipLibCheck: true
  forceConsistentCasingInFileNames: true


You can learn more at https://aka.ms/tsconfig
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


## Perustyypit

Monet TypeScriptin oppaat keskittyvät omien tyyppien määrittelyyn, mutta pääset hyvin liikkeelle myös ilman omia tyyppejä. TypeScriptissä on mm. valmiit tyypit `string`, `number` ja `boolean`, jotka vastaavat JavaScriptin arvoja:

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

Tyyppien määrittely tällä tarkkuudella on kuitenkin usein turhaa, koska TypeScript osaa päätellä asiayhteydestä mm. muuttujien sekä funktioiden paluuarvojen tyypit.

> *"For the most part you don’t need to explicitly learn the rules of inference. If you’re starting out, try using fewer type annotations than you think - you might be surprised how few you need for TypeScript to fully understand what’s going on."*
>
> https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

Ilman yllä esitettyä vapaaehtoista tyyppien määrittelyä koodi näyttääkin JavaScriptiltä, joskin kääntäjä päättelee tyypit ja osaa huomioida ne myöhemmin näitä muuttujia käytettäessä:

```ts
let language = 'TypeScript';        // language: string

let wholeNumber = 2023;             // wholeNumber: number
let decimalNumber = 3.14;           // decimalNumber: number

let positive = [1, 2, 3, 4];        // positive: number[]
let negative = [-1, -2, -3, -4];    // negative: number[]
```

Tyypin määritteleminen eksplisiittisesti on välttämätöntöntä erityisesti silloin, kun luot tyhjiä tietorakenteita, joista TS ei pysty päättelemään niiden myöhempää tyyppiä:

```ts
let empty = [];                     // never[] -> tähän ei voida lisätä arvoja, koska tyyppiä ei tiedetä
let numbers: number[] = [];         // number[] -> tähän voidaan jatkossa lisätä vain numeroita
```

### Funktioiden tyypit

> *"Functions are the primary means of passing data around in JavaScript. TypeScript allows you to specify the types of both the input and output values of functions."*
>
> https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions

```ts
// funktion parametrille ja paluuarvolle määritellään tyypit:
function shout(str1: string): string {
    return str1.toUpperCase() + '!!!';
}
```

TypeScript ei osaa päätellä parametrin tyyppiä, joten sen määritteleminen on tarpeen. Sen sijaan yllä **paluuaron tyyppi** `string` voidaan päätellä automaattisesti `return`-lausekkeessa olevasta tyypistä, eikä sitä tarvitse välttämättä kirjoittaa itse.


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
    bar.toUpperCase();  // ei virhettä käännettäessä, mutta kaatuu suoritettaessa!
}

doSomething(1);
doSomething('hello');
```

`unknown` ei puolestaan salli mahdollisesti virheellisiä operaatioita:

```ts
function doSomething(bar: unknown) {
    bar.toUpperCase();  // käännösvirhe!
}

doSomething(1);
doSomething('hello');
```

Kun tiedon tyyppi ei ole ennalta tiedossa, voidaan se selvittää ajonaikaisesti ehtorakenteilla ja mm. JavaScriptin `typeof`-operaation avulla:

```ts
function doSomething(bar: unknown) {
    if (typeof bar === 'string') {
        // TypeScript osaa nyt tunnistaa `bar`-arvon tyypiksi merkkijonon:
        console.log(bar.toUpperCase());
    } else {
        console.log(bar);
    }
}

doSomething(0);         // 0
doSomething('hello');   // 'HELLO'
```

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
let thing = all.at(-1)!;            // thing: (string | number)

// `as`-avainsanalla voidaan ohittaa tyypin päättely ja kertoa se itse:
let answer = all.at(-1) as number;  // answer: number

console.table({ something, thing, answer });
```

Vaikka edellä kolmen viimeisen muuttujan tyypit ovat TypeScriptin näkökulmasta eri, on niissä luonnollisesti tasan sama arvo, eli taulukon viimeinen numero `42`:

```
┌───────────┬────────┐
│  (index)  │ Values │
├───────────┼────────┤
│ something │   42   │   // string | number | undefined
│   thing   │   42   │   // string | number
│  answer   │   42   │   // number
└───────────┴────────┘
```

Edellä käytetty `at`-metodi toimii sekä positiivisilla että negatiivisilla indekseillä:

> *"The at() method takes an integer value and returns the item at that index, allowing for positive and negative integers. Negative integers count back from the last item in the array."*
>
> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at


### Tuplet (monikko)

TS tukee JavaScriptin taulukoille myös erityistä [tuple-tyyppiä](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types), jossa voidaan ennalta määritellä taulukon pituus ja kunkin eri indeksin tyyppi:

```ts
type NameAndAge = [string, number];

let alice: NameAndAge = ['Alice', 29];  // ok!
let bob: NameAndAge = ['Bob', 28, 1];   // käännösvirhe! `Source has 3 element(s) but target allows only 2`
```


### Suorituksen aikaiset tyypit (runtime)

Koska TypeScript-koodi käännetään JavaScriptiksi, ei koodia suoritettaessa voida käyttää TypeScriptin tyyppejä. Kaikki tieto TypeScriptin tyypeistä "katoaakin" suoritettaessa ja jäljelle jää vain JavaScriptin tyypit:

```ts
class Cat {
    constructor(public name: string) {
    }
}

class Car {
    constructor(public make: string, public model: string) {
     }
}

let animal = new Cat('kisu');
let automobile = new Car('VW', 'Beetle');
let strings = ['apotti', 'sarastia'];


// tieto "luokista" katoaa käännettäessä:
console.log(typeof animal);     // 'object'
console.log(typeof automobile); // 'object'
console.log(typeof strings);    // 'object'


// JS:n perustyyppien osalta `typeof` palauttaa kuitenkin oikeat tiedot:
console.log(typeof 1);          // 'number'
console.log(typeof true);       // 'boolean'
console.log(typeof 'hello');    // 'string'
```


## Omat tyypit

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
    email?: string;  // `?` tarkoittaa valinnaista arvoa
};

let user1: User = { id: 1, name: 'Alice' };
let user2: User = { id: 2, name: 'Bob', email: 'bob@example.com' };

console.log(user2.email.toLowerCase());   // käännösvirhe, koska email saattaa olla `undefined`
console.log(user2.email?.toLowerCase());  // JS:n "optional chaining" -> ei virhettä
```


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

### Muita kiinnostavia ominaisuuksia

TypeScript mahdollistaa useita erilaisia käteviä tapoja edistää oman koodin ylläpidettävyyttä, kuten `private` ja `readonly` -attribuutit sekä `as const`:

```ts
const days = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'] as const;
days[0] = 'måndag'; // error: "Index signature in type 'readonly string[]' only permits reading."
```

JavaScriptin `const` varmistaa, että muuttujaan ei voida asettaa uutta arvoa. `const`-muuttujaan asetetun arvon muuttaminen on kuitenkin mahdollista, esimerkiksi lisäämällä listaan uusia arvoja. TypeScriptin `as const` varmistaa muuttujan lisäksi myös siihen asetetun arvon muuttumattomuuden. Näihin ominaisuuksiin voit perehtyä lisää itsenäisesti.


## JavaScript-koodin tyyppimäärittelyt

TypeScriptillä kirjoittamasi ohjelmat hyödyntävät tyypillisesti erilaisia kirjastoja, jotka saattavat olla alun perin JavaScriptillä toteutettuja. Kuinka TypeScript osaa auttaa sinua näiden projektien tyyppien tarkastamisessa ja oikeiden tyyppien ehdottamisessa?

> *"Throughout the sections you’ve read so far, we’ve been demonstrating basic TypeScript concepts using the built-in functions present in all JavaScript runtimes. However, almost all JavaScript today includes many libraries to accomplish common tasks. Having types for the parts of your application that aren’t your code will greatly improve your TypeScript experience. Where do these types come from?"*
>
> Type Declarations, https://www.typescriptlang.org/docs/handbook/2/type-declarations.html


### "Standardikirjastot"

> *"TypeScript includes a default set of type definitions for built-in JS APIs (like Math), as well as type definitions for things found in browser environments (like document). TypeScript also includes APIs for newer JS features matching the target you specify; for example the definition for Map is available if target is ES6 or newer."*
>
> https://www.typescriptlang.org/tsconfig#lib

Suoritusympäristöstäsi riippuen voit ottaa käyttöön eri suoritusympäristöistä riippuvaisia tyyppimäärityksiä, kuten `document` ja `window`, lisäämällä `tsconfig.json`-tiedostoosi `lib`-osioon kirjastoja. Tyypillinen kirjasto on `DOM`, joka sisältää [Document Object Model -api:in](https://developer.mozilla.org/en-US/docs/Glossary/DOM) määritetyt tyypit.

`tsconfig.json`-tiedoston lisäksi tyyppimäärityksiä [voidaan lisätä npm-pakettien avulla `node_modules`-hakemistoon](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-beta/#supporting-lib-from-node_modules), josta TypeScript lukee ne automaattisesti. Tyypillinen `npm`-pakettina asennettava tyyppikirjasto on esimerkiksi `node`, joka voidaan asentaa seuraavasti:

```sh
$ npm install --save-dev @types/node    # https://www.npmjs.com/package/@types/node
```

Tyyppimääritykset saattavat myös asentua automaattisesti projektisi riippuvuuksien kautta. Esimerkiksi asentaessamme `ts-node`-paketin, asentuu sen kautta myös yllä esitetty `@types/node`:

```sh
$ npm ls -a
ts-oppitunti-2023-08-31@ /workspaces/ts-oppitunti-2023-08-31
├─┬ ts-node@10.9.1
│ ├─┬ @cspotcode/source-map-support@0.8.1
│ │ └─┬ @jridgewell/trace-mapping@0.3.9
│ │   ├── @jridgewell/resolve-uri@3.1.1
│ │   └── @jridgewell/sourcemap-codec@1.4.15
│ ├── UNMET OPTIONAL DEPENDENCY @swc/core@>=1.2.50
│ ├── UNMET OPTIONAL DEPENDENCY @swc/wasm@>=1.2.50
│ ├── @tsconfig/node10@1.0.9
│ ├── @tsconfig/node12@1.0.11
│ ├── @tsconfig/node14@1.0.3
│ ├── @tsconfig/node16@1.0.4
│ ├── @types/node@20.5.9    <--------- Node.js:n tyyppimääritykset
│ ├── acorn-walk@8.2.0
│ ├── acorn@8.10.0
│ ├── arg@4.1.3
│ ├── create-require@1.1.1
│ ├── diff@4.0.2
│ ├── make-error@1.3.6
│ ├── typescript@5.2.2 deduped
│ ├── v8-compile-cache-lib@3.0.1
│ └── yn@3.1.1
└── typescript@5.2.2
```


### JavaScriptillä toteutettujen pakettien "tyypitys"

TypeScript-määrittelyjä voidaan kirjoittaa esim. olemassa oleville npm-paketeille itse, mutta se on suosituille projekteille pääsääntöisesti tarpeetonta. Kehittäjäyhteisö ylläpitää yhteistä keskitettyä lähdettä kirjastojen tyyppimäärityksille:

> *"DefinitelyTyped / @types*
>
> *The [DefinitelyTyped repository](https://github.com/DefinitelyTyped/DefinitelyTyped/) is a centralized repo storing declaration files for thousands of libraries. The vast majority of commonly-used libraries have declaration files available on DefinitelyTyped.*
>
> *Definitions on DefinitelyTyped are also automatically published to npm under the @types scope. The name of the types package is always the same as the name of the underlying package itself. For example, if you installed the react npm package, you can install its corresponding types by running*
>
> `npm install --save-dev @types/react`
>
> *TypeScript automatically finds type definitions under node_modules/@types, so there’s no other step needed to get these types available in your program."*
>
> Type Declarations. https://www.typescriptlang.org/docs/handbook/2/type-declarations.html#external-definitions

Kirjoitushetkellä tyyppikirjastosta löytyy tyypit noin 7672:lle paketille, ja lukumäärä kasvaa koko ajan.


## Tyyppimäärittelyjen luonti omille käännetyille JS-tiedostoille

Mikäli TypeScriptillä kirjoitettu projekti julkaistaan esimerkiksi npm-palvelussa, voidaan sille generoida tyyppimäärittelyt automaattisesti. Näin pakettisi käyttäjät saavat TypeScript-tyypit automaattisesti käyttöönsä:

```shell
$ npx tsc --declaration
```

Itse tyyppimääritykset, kuten `koodi.d.ts`, näyttävät esim. seuraavilta:

```ts
declare let merkkijono: string;
declare let merkkijonot: string[];
declare let numerot: number[];
```

Lue lisää esimerkiksi artikkelista [Quick Tip — Generating a TypeScript Declaration File](https://gilfink.medium.com/quick-tip-generating-a-typescript-declaration-file-5db708c45d4b).



## Valinnaisia harjoituksia

Voit tutustua itsenäisesti TypeScriptin tyyppijärjestelmään esimerkiksi sivustolla https://typescript-exercises.github.io/.
