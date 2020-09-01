# Tietorakenteet ja algoritmit


> *Algoritmi (algorithm) on toimintaohje, jota seuraamalla voimme ratkaista jonkin laskennallisen ongelman. Algoritmille annetaan syöte (input), joka
kuvaa ratkaistavan ongelman tapauksen, ja algoritmin tulee tuottaa tuloste (output), joka on vastaus sille annettuun syötteeseen*
>
> *Antti Laaksonen, [Tietorakenteet ja algoritmit -kirja](https://github.com/pllk/tirakirja/raw/master/tirakirja.pdf)*


## Tavoitteet

Tällä viikolla ohjelmistokehityksen teknologioita -kurssilla on perehtyä tietorakenteiden ja algoritmien peruskäsitteisiin ja opetella arvioimaan karkeasti arilaisten algoritmisten lähestymistapojen soveltuvuutta ohjelmointiongelmiin. 

Tavoitteenamme ei ole oppia laskemaan tai esittämään algoritmiemme tarkkaa tehokkuutta matemaattisilla kaavoilla, vaan käytämme laskukaavoja apuvälineenä ymmärtääksemme miksi jokin algoritmi suoriutuu samasta tehtävästä tehokkaammin kuin toinen.

Ohjelmointiongelmien ratkaisemisessa myös tietorakenteilla on erittäin merkittävä rooli. Tietorakenteiden sisäinen toteutus, esimerkiksi linkitetty lista vs. taulukkolista, vaikuttaa merkittävästi sen soveltuvuuteen erilaisten ongelmien ratkaisemisessa. 

Tallentaessamme itse tietoa ohjelmiimme voimme myös vaikuttaa suuresti siihen, kuinka helposti ja nopeasti tallentamamme tieto on ohjelmakoodissa saatavilla.

Vertaa esimerkiksi seuraavia mahdollisia tietorakenteita postinumeroiden ja postitoimipaikkojen tietojen tallentamiseksi:

```json
[
    {"postalCode": "74701", "name": "KIURUVESI"},
    {"postalCode": "35540", "name": "JUUPAJOKI"},
    {"postalCode": "74700", "name": "KIURUVESI"},
    {"postalCode": "73460", "name": "MUURUVESI"}
]
```

```json
{
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}
```

Jos tarkoituksesi olisi selvittää postinumeroa 74700 vastaava postitoimipaikan nimi, mitä sen selvittäminen vaatisi eri tietorakenteilla? Entä kumpi tietorakenne olisi myöhemmin helpommin laajennettavissa, jos postinumeroalueita varten halutaan tallentaa toimipaikan nimen lisäksi myös muita tietoja?

## Ennakkotehtävät

Tietojenkäsittelyssä sama ongelma voidaan tyypillisesti ratkaista lukemattomilla erilaisilla tavoilla. Onkin olemassa lukuisia tunnettuja algoritmeja esimerkiksi listan arvojen järjestelemiseksi tai yksittäisen arvon etsimiseksi listalta. 

Katso seuraavat kolme videota, joka esittelevät ohjelmistokehittäjän perusosaamisen kannalta keskeisiä algoritmeja sekä tietorakenteita, sekä iso-O -notaation, jonka avulla vertailemme algoritmien tehokkuutta eri kokoisilla syötteillä:

### Video 1: [What Is an Algorithm?](https://youtu.be/PY82qqyWJJs) 7:54

[![What Is an Algorithm?](https://img.youtube.com/vi/PY82qqyWJJs/mq1.jpg)](https://youtu.be/PY82qqyWJJs)


> *We evaluate an algorithm mainly based on how many steps the algorithm takes to solve its problem* &mdash; *[What Is an Algorithm?](https://youtu.be/PY82qqyWJJs)*


### Video 2: [Practical Big-O Notation](https://youtu.be/e6UZ2kzmmdA) 12:59

[![Practical Big-O Notation](https://img.youtube.com/vi/e6UZ2kzmmdA/mq2.jpg)](https://youtu.be/e6UZ2kzmmdA)

> *Big-O notation is how the efficiency of algorithms is typically described. Figuring out the O-notation of an algorithm can look tricky, but as this video shows, for the majority of situations, it's pretty straightforward.* &mdash; *[Practical Big-O Notation](https://youtu.be/e6UZ2kzmmdA)*

### Video 3: [Data Structures You Must Know (as a Software Developer)](https://youtu.be/sVxBVvlnJsM) 7:22

[![Data Structures You Must Know (as a Software Developer)](https://img.youtube.com/vi/sVxBVvlnJsM/mq1.jpg)](https://youtu.be/sVxBVvlnJsM)

> *Linked Lists, Arrays, Hash Table, Stack, Queue, Graph, Tree, Binary Search Tree...*



## Oppitunti

Oppitunnin materiaalit päivitetään tänne.


## Tehtävä (Luonnos - tehtävä saattaa vielä muuttua)

Tämän viikon tehtävänä on harjoitella vapaavalintaisen järjestämisalgoritmin toteuttamista. Voit valita toteutettavan järjestämisalgoritmin esimerkiksi seuraavista:

* Lisäyslajittelu eli Insertion Sort: https://en.wikipedia.org/wiki/Insertion_sort
* Lomituslajittelu eli Merge Sort: https://en.wikipedia.org/wiki/Merge_sort
* Kuplalajittelu eli Bubble Sort: https://en.wikipedia.org/wiki/Bubble_sort
* Pikalajittelu eli Quicksort: https://en.wikipedia.org/wiki/Quicksort

Oikeassa ohjelmistoprojektissa käyttäisit Pythonin valmiita järjestämisfunktioita, joita esitellään esimerkiksi osoitteessa https://docs.python.org/3/howto/sorting.html. Tämän harjoituksen tavoitteena on kuitenkin opetella itse toteuttamaan jokin tunnettu järjestämisalgoritmi.


### Järjesteltävä aineisto

MyHelsinki Open API on Helsinki Marketingin tarjoama avoin REST-rajapinta kaupungin tapahtumien, paikkojen ja aktiviteettien tietoihin. Rajapinnan dokumentaatio löytyy Swagger-muodossa osoitteesta http://open-api.myhelsinki.fi/doc. Kyseisessä osoitteessa on dokumentoituna niin resurssien osoitteet, niiden tukemat parametrit kuin palautettujen JSON-objektien rakenne.

Tässä tehtävässä hyödynnetään tapahtumarajapinnan tarjoamaa aineistoa osoitteesta http://open-api.myhelsinki.fi/v1/events/. Tapahtumat palautetaan rajapinnasta epäjärjestyksessä, joten joudut itse huolehtimaan tapahtumien järjestämisestä alkamisajan mukaan. 

Huomaa, että **kaikilla rajapinnan palauttamilla tapahtumilla ei välttämättä ole alkamisaikaa**. Tällaisten tapahtumien kohdalla voit itse päättää, jätätkö tapahtumat huomioimatta vai kehitätkö niille vapaavalintaisen erillisen logiikan. Osalle tapahtumista on annettu nimet useilla eri kielillä, mutta joiltain nimiä puuttuu. Myös tällaisten tapahtumien kohdalla saat päättää miten käsittelet tapahtumat.


### events_by_date.py

Kirjoita Python-skripti `events_by_date.py`, joka hakee events-rajapinnasta kaikki tapahtumat. Järjestä tapahtumat järjestykseen alkamisaikansa mukaan itse toteuttamallasi vapaasti valittavalla järjestämisalgoritmilla (ks. linkit yllä). Koodisi tulee järjestellä kokonaisia tapahtumatietueita, eli et saa poimia aineistosta järjesteltäväksi esimerkiksi pelkkiä nimiä ja alkamisaikoja.

Kun aineisto on järjestetty, tulosta tapahtumien nimet ja ajankohdat kronologisessa järjestyksessä. Tulosteen muodolla ei ole tehtävän arvioinnin kannalta merkitystä. Yksi varteenotettava tapa on näyttää tapahtumat ryhmiteltynä päivän mukaan (suurin osa tulosteesta poistettu '...'):

```
2020-12-05

  08:30 Taaperodisko
  09:00 Jazz for Kids: 5-vuotissynttärit
  09:00 Robin Rekku & Jekkuorkesteri
  09:30 Los Tres Cerros
  10:00 Tatu Ja Patu Helsingissä
  ...
  17:00 SIIRRETTY: Räjäyttäjät, Ninni Forever Band – A la Malmi
  18:00 DIVET SHOW - 15-vuotisjuhlashow

2020-12-06

  11:00 Kaarela-seuran perinteinen itsenäisyyspäivän juhla
  14:00 Kaikkien itsenäisyyspäivän juhla PERUUNTUNUT – Juhla-ateria ja monipuolista ohjelmaa
  14:00 Itsenäisyyspäivä 2020
  15:00 Iltasatutuokiot

2020-12-07

  07:30 SYTO-MYSSYT
  08:00 Ohjattu liikuntatuokio leikkipuistossa
  08:00 Muskari Olarin asukaspuistossa
  08:00 Bonkei, pienoispuutarhani – Taideneuvola
  ...
  17:00 Emilia Lajunen: Vainaan perua
  17:00 Iliza

2020-12-08

  07:00 Avoin keramiikkapaja
  07:00 Biljardiryhmä
  07:15 Tenavakino: Kanelia kainaloon, Tatu ja Patu
  07:30 Taaperotuokio
  07:30 Satutuokio
 
...
```

### Tehtävän arviointi

Ratkaisu, joka sisältää toimivan itse mallin mukaan toteutetun järjestelyalgoritmin, hyväksytään arvosanalla 5. Myös puutteelliset ratkaisut hyväksytään, kunhan niissä osoitetaan selvää yritystä tehtävän ratkaisemiseksi.

Toiminnallisesti oikeellinen ratkaisu, joka oman järjestelyalgoritmin sijasta hyödyntää Pythonin valmiita [sort-operaatioita](https://docs.python.org/3/howto/sorting.html) oikeuttaa arvosanaan 3.

### Tehtävän palauttaminen

Palauta koodaamasi lähdekooditiedosto(t) sellaisenaan, eli **ei pakattuna** Teamsissa olevaan palautuslaatikkoon seuraavaan oppituntiin mennessä.
