# TypeScript

> *"TypeScript is a language for application-scale JavaScript. TypeScript adds optional types to JavaScript that support tools for large-scale JavaScript applications for any browser, for any host, on any OS. TypeScript compiles to readable, standards-based JavaScript."*
>
> https://github.com/microsoft/TypeScript/

TypeScriptin piirteitä:

- [x] JavaScriptin laajennos
- [x] Vahvasti tyypitetty kieli
- [x] Microsoftin kehittämä, [mutta avointa lähdekoodia](https://github.com/microsoft/TypeScript/blob/main/LICENSE.txt)
- [x] Yhteensopiva olemassa olevien JavaScript-sovellusten ja NPM-pakettien kanssa
- [x] Sisältää jo etukäteen JavaScriptin tulevia ominaisuuksia: "future JavaScript"
- [x] Käännettävissä yhteensopivaksi myös JavaScriptin vanhojen versioiden kanssa

Lue lisää kielestä esimerkiksi sivulta https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html.


## Tunnin aihe

Tällä tunnilla perehdymme TypeScriptin ominaisuuksiin ja työkaluihin. Kirjoittamme TS-koodia aluksi ilman riippuvuuksia, kuten Reactia ja Express:iä, jotta perusasiat eivät huku eri kirjastojen ja työkalujen ominaisuuksien alle.


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


## Elokuva

**[TypeScript Origins: The Documentary (YouTube, kesto 1:21:35) ](https://www.youtube.com/watch?v=U6s2pdxebSo)**

*The documentary features core contributors and community members like Anders Hejlsberg, Steve Lucco, Luke Hoban, Daniel Rosenwasser, Ryan Cavanaugh, Amanda Silver, Matt Pocock, Josh Goldberg & many more! It also covers adoption stories and insights from JetBrains, Xata, AG_Grid, Deno, Visual Studio Code and Tech at Bloomberg.*


## TypeScriptin asentaminen

TypeScript voidaan asentaa joko globaalisti koko käyttöjärjestelmään tai paikallisesti yksittäiseen projektiin. Globaali asennus [jakaa mielipiteitä](https://github.com/loopbackio/loopback.io/issues/509) ja myös TypeScriptin omissa ohjeissa asennusta tehdään eri tavoilla ([globaalisti](https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html#installing-typescript) ja [paikallisesti](https://github.com/microsoft/TypeScript/?tab=readme-ov-file#installing)). Tämän kurssin esimerkeissä asennus tehdään aina paikallisesti yksittäiseen projektiin.

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

Node.js:n uusimmat versiot tukevat *periaatteessa* TypeScript-koodin suorittamista suoraan, mutta merkittävillä rajoituksilla. Esimerkiksi `tsconfig.json`-tiedoston asetuksia ei tueta ja oletuksena koodissa saa olla vain sellaisia ominaisuuksia, jotka voidaan yksinkertaisesti poistaa:

> *"By default Node.js will execute TypeScript files that contains only erasable TypeScript syntax. Node.js will replace TypeScript syntax with whitespace, and no type checking is performed."*
>
> https://nodejs.org/docs/v24.12.0/api/typescript.html#type-stripping

Node.js:n dokumentaation artikkeli [Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively) tarjoaa lisätietoja TypeScript-koodin suorittamisesta Node.js:ssä. Käytännössä edistyneemmän TypeScript-koodin suorittamiseksi on kaksi lähestymistapaa: joko kääntää koodi JavaScriptiksi etukäteen TypeScript-kääntäjällä (ahead-of-time) tai käyttää työkaluja, jotka kääntävät TypeScriptiä samalla kun sitä suoritetaan (just-in-time).


### Npx

Jos et asentanut [TypeScript-pakettia](https://www.npmjs.com/package/typescript) globaalisti, se suoritetaan paikallisen projektin `node_modules`-hakemistosta. Tämä onnistuu joko komennolla `npm exec tsc` tai lyhyemmin `npx`-komennon avulla:

> *"\[npx\] command allows you to run an arbitrary command from an npm package (either one installed locally, or fetched remotely), in a similar context as running it via `npm run`.*"
>
> https://docs.npmjs.com/cli/v9/commands/npx

```bash
npx tsc   # suorittaa `tsc`-komennon, eikä edellytä globaalia asennusta
```

`npx`-komennon pitäisi löytyä sinulta valmiiksi, jos sinulla on `npm` asennettuna.


### Tsc (TypeScript compiler)

**Tsc** on TypeScript-kääntäjä, joka tarkastaa TypeScript-lähdekoodisi virheiden varalta sekä kääntää koodisi standardin mukaiseksi JavaScriptiksi. Kun siis haluat kääntää kirjoittamasi ohjelman TypeScript-kielestä JavaScriptiksi, onnistuu se `npx`- ja `tsc`-komennoilla:

```sh
npx tsc
```

Jos kääntäminen onnistuu, syntyy tuloksena JavaScript-tiedostoja, jotka voidaan suorittaa Node.js:llä tai muissa JavaScript-ympäristöissä ilman TypeScriptiä. Jos koodissa on virheitä, `tsc`-kääntäjä ilmoittaa niistä ja käännös ei onnistu ennen kuin virheet on korjattu.


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


### Ts-node

> *"`ts-node` is a TypeScript execution engine and REPL for Node.js. It JIT transforms TypeScript into JavaScript, enabling you to directly execute TypeScript on Node.js without precompiling."*
>
> https://www.npmjs.com/package/ts-node


```bash
npm install ts-node --save-dev    # asentaa ts-noden paikallisesti

npx ts-node src/skripti.ts        # suorittaa skriptin `src/skripti.ts`

npx ts-node                       # käynnistää ts-noden REPL-tilan
```

`ts-node` mahdollistaa TypeScript-koodin suorittamisen ilman etukäteen tehtävää käännösvaihetta. Se on suosittu ja yksinkertainen työkalu, mutta sille on viime vuosien aikana tullut myös paljon kilpailijoita, kuten [tsx](https://www.npmjs.com/package/tsx).


### Tsconfig.json

TypeScript-kääntäjä sekä työkalut, kuten `tsx` ja `ts-node`, tukevat lukuisia TS-koodin kääntämiseen liittyviä asetuksia. Nämä asetukset voidaan antaa komentoriviparametreina, mutta tyypillisesti niitä on niin paljon, että ne kannattaa tallentaa erilliseen asetustiedostoon.

> *"The presence of a tsconfig.json file in a directory indicates that the directory is the root of a TypeScript project. The tsconfig.json file specifies the root files and the compiler options required to compile the project"*
>
> https://www.typescriptlang.org/docs/handbook/tsconfig-json.html

`tsconfig.json`-asetustiedostoon voidaan määritellä lukuisia kääntäjän toimintaan vaikuttavia asetuksia. Voit luoda itsellesi uuden `tsconfig.json`-tiedoston `tsc`-komennon avulla `--init`-parametrilla:

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

Asetustiedosto voi näyttää esimerkiksi tältä:

```js
/* Visit https://aka.ms/tsconfig to read more about this file */
{
    "compilerOptions": {
        /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */
        "target": "es2024",

        /* Specify what module code is generated. */
        "module": "nodenext",

        /* Specify the root folder within your source files. */
        "rootDir": "./src/",

        /* Specify an output folder for all emitted files. */
        "outDir": "./build/",

        /* Emit additional JavaScript to ease support for importing CommonJS modules. This enables 'allowSyntheticDefaultImports' for type compatibility. */
        "esModuleInterop": true,

        /* Enable all strict type-checking options. */
        "strict": true,

        /* see https://www.typescriptlang.org/docs/handbook/modules/theory.html#module-resolution */
        "moduleResolution": "nodenext",

    },
    "exclude": [
        "node_modules",
        "build"
    ]
}
```

Projektinhallintatyökalut, kuten [Vite](https://vite.dev/) ja [Expo](https://expo.dev/), luovat tyypillisesti automaattisesti sopivan `tsconfig.json`-tiedoston projektin juureen, joten sinun ei välttämättä tarvitse luoda tai muokata sitä itse.

Eri asetukset riippuvat merkittävästi siitä, millaisessa ympäristössä sovellustasi ajetaan. Esimerkiksi selainpohjaisessa React-sovelluksessa voi olla aivan erilaiset vaatimukset kuin Node.js-palvelimella ajettavassa Express-sovelluksessa tai npm-pakettina jaettavassa kirjastossa.


### Bun, Deno, Yarn, pnpm ja muut vaihtoehtoiset työkalut

Viime vuosina on julkaistu useita Node.js:n kanssa kilpailevia JavaScript- ja TypeScript-suoritusympäristöjä, kuten [Deno](https://deno.land/) ja [Bun](https://bun.sh/). Useimmat uudet ympäristöt tukevat TypeScriptiä joko natiivisti tai erillisten laajennosten avulla.

Vaikka vaihtoehtoiset ratkaisut tarjoavat useita mielenkiintoisia ominaisuuksia sekä laadullisia parannuksia niin tietoturvan kuin suorituskyvyn osalta, on Node.js:n asema yhä vahva. Suositut JS-kirjastot niin selain- kuin palvelinpuolella on rakennettu ensisijaisesti Node.js:n ympäristöön. Lisäksi Node.js on laajasti käytössä eri tutoriaaleissa ja eri pavelinymäristöissä.

Pakettienhallinnan osalta Node.js:n [npm](https://www.npmjs.com/) on vakiintunut de facto -standardiksi, jota myös monet muut ympäristöt tukevat. Myös npm:lle on saatavilla useita vaihtoehtoisia työkaluja, kuten [Yarn](https://yarnpkg.com/) ja [pnpm](https://pnpm.io/).


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

Tyyppien määrittely tällä tarkkuudella on usein turhaa, koska TypeScript osaa päätellä asiayhteydestä mm. muuttujien sekä funktioiden paluuarvojen tyypit.

> *"For the most part you don’t need to explicitly learn the rules of inference. If you’re starting out, try using fewer type annotations than you think - you might be surprised how few you need for TypeScript to fully understand what’s going on."*
>
> https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

Ilman yllä esitettyä vapaaehtoista tyyppien määrittelyä koodi näyttääkin JavaScriptiltä. Kääntäjä päättelee tyypit automaattisesti ja se osaa huomioida ne myöhemmin näitä muuttujia käytettäessä:

```ts
let language = 'TypeScript';        // language: string

let wholeNumber = 2023;             // wholeNumber: number
let decimalNumber = 3.14;           // decimalNumber: number

let positive = [1, 2, 3, 4];        // positive: number[]
let negative = [-1, -2, -3, -4];    // negative: number[]
```

Tyypin määritteleminen eksplisiittisesti on välttämätöntöntä erityisesti silloin, kun luot tyhjiä tietorakenteita, joista TS ei pysty päättelemään niiden myöhempää tyyppiä:

```ts
let empty = [];                     // tyyppiä ei tässä vaiheessa vielä tiedetä
let numbers: number[] = [];         // number[] -> tyhjälle taulukolle määritellään tyyppi
```

### Funktioiden tyypit

> *"Functions are the primary means of passing data around in JavaScript. TypeScript allows you to specify the types of both the input and output values of functions."*
>
> https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions

```ts
// funktion parametrille ja paluuarvolle määritellään tyypit:
function shout(text: string): string {
    return text.toUpperCase() + '!!!';
}
```

TypeScript ei osaa päätellä parametrien tyyppiä, joten niiden tyyppien määritteleminen on <abbr title="pun intended">tyypillisesti</abbr> tarpeen. **Paluuarvon tyyppi** voidaan kuitenkin päätellä usein automaattisesti `return`-lausekkeessa olevasta tyypistä, eikä sitä tarvitse välttämättä kirjoittaa itse.


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

Myös kokoelmat ovat tyypitettyjä, esim. `string[]` tai `number[]`. Seuraavat esimerkit näyttävät, miten puuttuviin arvoihin varautuminen voidaan ohittaa (`!`) ja miten tietyn arvon tyyppi voidaan itse määrittää `as`:

```ts
let faces = ['😀', '🙁'];          // string[]
let numbers = [1337, 67, 42];       // number[]

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
