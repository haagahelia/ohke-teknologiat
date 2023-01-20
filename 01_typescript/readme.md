
# TypeScript


> *"TypeScript is a language for application-scale JavaScript. TypeScript adds optional types to JavaScript that support tools for large-scale JavaScript applications for any browser, for any host, on any OS. TypeScript compiles to readable, standards-based JavaScript."*
>
> https:/,/github.com/microsoft/TypeScript/

TypeScript on:

- [x] JavaScriptin laajennos
- [x] Vahvasti tyypitetty kieli
 Suuri osa TypeScriptin "uusista ominaisuuksista" on osa EcmaScriptin seuraavia versioita, "future JavaScript"
- [x] MicroSoftin kehittämä
- [x] Yhteensopiva JavaScriptin ja mm. olemassa olevien NPM-pakettien kanssa
- [x] Yhteensopiva myös JavaScriptin vanhojen versioiden kanssa

https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html

<!--StackOverflow 2022 developer survey: https://survey.stackoverflow.co/2022-->

## Suositellut videot

[Programming with Mosh: TypeScript Tutorial for Beginners](https://www.youtube.com/watch?v=d56mG7DezGs)

[Fireship: TypeScript - The Basics](https://www.youtube.com/watch?v=ahCwqrYpIuM)


### TypeScriptin asentaminen

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

💡 **Huom!** Monissa

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

## Transpilointi

TypeScript Tooling in 5 minutes: https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html

TypeScript Playground: https://www.typescriptlang.org/play

Kokeile transpiloida TS-koodia, jossa esiintyy moderneja ominaisuuksia kuten `async` tai `await`, vanhalle JavaScript-versiolle. [Mitä saat tulokseksi?](https://www.typescriptlang.org/play?target=0#code/MYewdgzgLgBA5gUygVQggThGBeGBDCATzGBgAoBKHAPhgG0BvGASwBMAuGARgBoYw8AWwScA5AEEANs2AJRMAL4BdANxA)

### Npx

> *"\[npx\] command allows you to run an arbitrary command from an npm package (either one installed locally, or fetched remotely), in a similar context as running it via `npm run`.*"
>
> https://docs.npmjs.com/cli/v9/commands/npx

### Ts-node

> *"`ts-node` is a TypeScript execution engine and REPL for Node.js. It JIT transforms TypeScript into JavaScript, enabling you to directly execute TypeScript on Node.js without precompiling. "*
>
> https://www.npmjs.com/package/ts-node

### Tsc

Jos haluat kääntää kirjoittamasi ohjelman TypeScript-kielestä JavaScriptiksi, onnistuu se `tsc`-komennolla (TypeScript compiler).

```
$ npx tsc
```

`tsc`-komento kääntää kirjoittamasi TypeScript-tiedostot JavaScript-tiedostoiksi, jotka voidaan suorittaa Node.js:llä aivan kuten mitkä tahansa `.js`-tiedostot:

```
$ node helloWorld.js
```


### Tsconfig

> *"The strict flag enables a wide range of type checking behavior that results in stronger guarantees of program correctness. Turning this on is equivalent to enabling all of the strict mode family options, which are outlined below. You can then turn off individual strict mode family checks as needed."*
>
> https://www.typescriptlang.org/tsconfig#strict


https://www.contentful.com/blog/what-is-typescript-and-why-should-you-use-it/


## Tyypit

### Valmiit tyypit

https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

### Funktioiden tyypit

### Omat tyypit

Muuttujalle erikseen määritetty tyyppi:

```ts
let user: { id: number, name: string } = { id: 1, name: 'Alice'};
```

Alias-tyyppi:

```ts
type User = {
    id: number;
    name: string;
};

let user: User  = { id: 1, name: 'Alice'};
```

Valinnaiset attribuutit:

```ts
type User = {
    id: number;
    name: string;
    email?: string;
};

let user: User  = { id: 1, name: 'Alice'};
```


### Union types

```ts
type Size = 's' | 'm' | 'l';
```

<!-- narrowing typeof x === y -->

### Intersection types

```ts
type Coordinate = { lat: number, lon: number };
type Address = { street: string, city: string };

type MapMarker = Address & Coordinate;
```

## Valinnaisia harjoituksia

TypeScript exercises: https://typescript-exercises.github.io/


## Palautettava tehtävä


