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

### Video 1: [What Is an Algorithm?](https://youtu.be/PY82qqyWJJs)

[![What Is an Algorithm?](https://img.youtube.com/vi/PY82qqyWJJs/mq1.jpg)](https://youtu.be/PY82qqyWJJs)


> *We evaluate an algorithm mainly based on how many steps the algorithm takes to solve its problem* &mdash; *[What Is an Algorithm?](https://youtu.be/PY82qqyWJJs)*


### Video 2: [Practical Big-O Notation](https://youtu.be/e6UZ2kzmmdA)

[![Practical Big-O Notation](https://img.youtube.com/vi/e6UZ2kzmmdA/mq2.jpg)](https://youtu.be/e6UZ2kzmmdA)

> *Big-O notation is how the efficiency of algorithms is typically described. Figuring out the O-notation of an algorithm can look tricky, but as this video shows, for the majority of situations, it's pretty straightforward.* &mdash; *[Practical Big-O Notation](https://youtu.be/e6UZ2kzmmdA)*

### Video 3: [Data Structures You Must Know (as a Software Developer)](https://youtu.be/sVxBVvlnJsM)

[![Data Structures You Must Know (as a Software Developer)](https://img.youtube.com/vi/sVxBVvlnJsM/mq1.jpg)](https://youtu.be/sVxBVvlnJsM)

> *Linked Lists, Arrays, Hash Table, Stack, Queue, Graph, Tree, Binary Search Tree...*

