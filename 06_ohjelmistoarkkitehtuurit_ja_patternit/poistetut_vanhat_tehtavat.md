# Poistetut vanhat tehtävät - Ei tarvitse lukea

### Tehtävä 6.2 (30% kierroksen arvosanasta):

[DIPTehtava.java](src/exercises/DIPTehtava.java) tiedostosta löytyy useampi Java-luokka, jotka kuvaavat yksinkertaista moottoripyörien tai autojen käsittelyyn tehtyä järjestelmää. Sinun tehtäväsi olisi refaktoroida tiedostossa olevat luokat siten, että järjestelmän arkkitehtuuri seuraa Dependency inversion-periaatetta (DIP) ja hyödyntää olioiden monimuotoisuutta.
 
Kaikki luokat on kirjoitettu tehtävän palautuksen helpottamiseksi samaan
tiedostoon.
  
Tiedoston voi kääntää komennolla: *javac DIPTehtava.java*
Kun kääntäminen on onnistunut, niin luodun .class-luokan voi ajaa 
komennolla: *java DIPTehtava*.

Palauta lopuksi sama tiedosto Teamsiin.

*Lisäpohdintaa tehtävään: Jos haluat tehtävän tekemisen jälkeen vielä pohtia DIP:tä ja olioiden monimuotoisuutta lisää, niin kokeile toteuttaa myös Moottoripyörän ja Auton ajoneuvoveron laskeminen DIP-arkkitehtuurimallin mukaisesti. Ajoneuvoveron suuruus riippuu nyt käyttämättömistä fieldeistä, eli siitä onko kyseessä kevytmoottoripyörä tai vastaavasti auton tapauksessa farmariauto. Voit vaikka harjoituksen vuoksi toteuttaa laskennat kaavalla, jossa ajoneuvovero määräytyy: (ajoneuvon käyttövuodet)x100 ja kevytmoottoripyörälle lisäksi jaetaan tuo summa kahdella ja farmariautolla kerrotaan 1.2:lla. Tämä siis tarkoittaa, että tarvitset nykyisen BusinessLuokan lisäksi omat businessluokat myös Moottoripyörälle ja Autolle. Näiden businessluokkien tulee myös toteuttaa yhteinen rajapinta, jossa on laskeAjoneuvovero()-metodi. Sovelluksen konfigurointivaiheessa tulee sitten injektoida asianmukaiset toteuttavat luokat paikoilleen, jotta laskenta menee oikein.*


-----------

📣 **Huom! Vierailijaluennon vuoksi lyhensimme ohjelmistoarkkitehtuurien ja patternien osuutta yhden viikon pituiseksi, joten seuraavat tehtävät korvataan uusilla.**

### <del>Tehtävä 6.3 (20% kierroksen arvosanasta):</del>

1. Piirrä arkkitehtuurikaavio joko komponenteista ja teknologioista TAI luokkakaavio ohjelmistoprojekti2-järjestelmästänne (mikäli järjestelmänne on arkkitehtuurillisesti mielestäsi kohtalaisen haastava ja kiinnostava). Et voi palauttaa samaa kaaviota tiimikaverisi kanssa, eli tehtävä tulee tehdä itsenäisesti, toki asioista voi keskustella tiimikavereiden kanssa.

1. Toinen vaihtoehto on laatia luokkakaavio [LentokoneConfig-esimerkistä](src/examples/LentokoneConfig.java). Piirrä siis tehtävän luokat ja rajapinnat sekä osoita nuolilla luokkien/rajapintojen suhteet. Jos luokka käyttää toista luokkaa/rajapintaa, merkitse se yhtenäisellä nuolella ja jos luokka toteuttaa rajapinnan, merkitse se katkonuolella. Merkitse rajapinnat joko katkoviivalaatikkoina tai \<\<\<interface>>>-merkinnällä rajapinnan nimen perässä. Kaavio on siis samankaltainen kuin olio-ohjelmoinnin yhteydessä [esitelty UML-kaavio](img/UML-luokkakaavio.png).

Arkkitehtuurikaavion voit piirtää haluamallasi työkalulla, esimerkiksi google-slides riittää ihan hyvin. Palauta tehtävässä lopulta siis png-kuvatiedostona  arkkitehtuurikaavio.

### <del>Tehtävä 6.4 (20% kierroksen arvosanasta):</del>

[Redux](https://redux.js.org/tutorials/essentials/part-1-overview-concepts) on kirjasto, jota käytetään monesti React-sovellusten yhteydessä. Reduxin tarkoitus olisi selkeyttää sovelluksen tilan hallintaa tilanteissa, joissa tila uhkaa hajautua sekavasti eri komponentteihin. 
Reduxin käyttäminen perustuu omaan pieneen suunnittelumalliin, eli arkkitehtuurimalliin. Malli koostuu kolmesta ydinkomponentista: [Actioneista](https://redux.js.org/basics/actions), [Reducerista](https://redux.js.org/basics/reducers) sekä [Säiliöstä](https://redux.js.org/basics/store) (Store). Tässä mallissa Actionit kertovat mitä halutaan tehdä (ja välittävät tämän tiedon Reducerille). Reducer päättää miten Actionin haluama asia tehdään ja miten uusi tila määritellään. Reducer-komponentin idea pohjautuu funktionaalisen ohjelmoinnin [reduce (toiselta nimeltä fold tai accumulate) funktioon](https://en.wikipedia.org/wiki/Fold_%28higher-order_function%29). (Funktionaalisen ohjelmoinnin Reduce-funktiolle annetaan parametrina lista ja tavoitteena on palauttaa vain yksi redusoitu/accumuloitu arvo. Redusoivaa funktiota sovelletaan listan alkioihin (tai tässä tapauksessa tämänhetkiseen tila-arvoon) ja lopulta palautetaan lopputulos, joka syntyy redusoivan funktion soveltamisesta yksi kerrallaan listan arvoihin.) Funktionaalisen ohjelmoinnin periaatteiden mukaisesti Reducer ei muokkaa vanhaa tilaa, vaan palauttaa kokonaan uuden tilan, Reducerin tulee muutenkin olla ns. ["puhdas funktio"](https://en.wikipedia.org/wiki/Pure_function) ilman sivuvaikutuksia.

![Redux](img/redux.png) 

Reduxia voi käyttää (ja sen periaatteita seurata) myös ilman Reactia. Tiedostossa [Reduxperiaatteet.js](src/exercises/Reduxperiaatteet.js) on luotu tiedostopohja, josta löytyy metodipohja Reducer-metodille, kahdelle Action-metodille sekä Redux säiliön luomiselle (lisäksi samassa src-kansiossa on npm:lle tarpeellinen [package.json](src/exercises/package.json)). Sinun tehtäväsi on täydentää Reducer-metodia sekä kahta Action metodia siten, että Redux-säiliö palauttaa tiedostossa kuvatun halutun lopputuloksen. Tärkeintä tässä tehtävässä olisi tutustua Reduxin arkkitehtuurin toimintaperiaatteita Reduxin dokumentaatiota ja googlea hyödyntäen ja yrittää toteuttaa tämä pieni ohjelma Reduxin arkkitehtuuriperiaatteita seuraten. Reduxista ja sen periaatteista voi lukea myös esim [täältä](https://redux.js.org/introduction/getting-started). (muista ajaa src-kansiossa *npm install* komento alkuun, jolloin npm asentaa Redux-kirjaston, johon on määritelty riippuvuus src-kansion package.json-tiedostossa).

Palauta lopuksi sama tiedosto Teamsiin (HUOM: Teams ei anna palauttaa .js-päätteistä tiedostoa, joten muuta tai lisää päätteeksi .txt, niin palautus onnistuu. Pahoittelut tästä. HUOM2: Tehtävässä pohjaksi annettu versio ilman korjauksia heittää ajettaessa Redux-kirjastolta virheen, eli se ei suostu ajamaan sellaisenaan ilman muutoksia.).
