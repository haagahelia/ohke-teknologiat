# Tietorakenteet ja algoritmit


> *Algoritmi (algorithm) on toimintaohje, jota seuraamalla voimme ratkaista jonkin laskennallisen ongelman. Algoritmille annetaan syöte (input), joka kuvaa ratkaistavan ongelman tapauksen, ja algoritmin tulee tuottaa tuloste (output), joka on vastaus sille annettuun syötteeseen*
>
> *Antti Laaksonen, [Tietorakenteet ja algoritmit -kirja](https://github.com/pllk/tirakirja/raw/master/tirakirja.pdf)*


# Oppitunnin videot

Videoilla esiintyvät lähdekoodit löydät [täältä](./src/).

**[Osa 1: Johdanto tietorakenteisiin ja algoritmeihin](https://web.microsoftstream.com/video/0dc02d53-0eff-4780-a017-bb79a5c876a2)** *50:13*

Tällä videolla toteutamme yksinkertaisen listoja hyödyntävän toistorakenteen ja perehdymme sen tehokkuuteen.

**[Osa 2: Puolitushaku, asymptoottinen suoritusaika ja hajautustaulut](https://web.microsoftstream.com/video/0b5f8575-c72f-4521-9afc-5290ac54cd75)** *1:03:59*

Tällä videolla perehdymme vertaillen eri tietorakenteisiin sekä niihin liittyvien operaatioiden suoritusaikaan. Opimme arvioimaan oman koodimme suoritusaikaa ja valitsemaan tarpeet huomioiden tehokkaita tietorakenteita ja algoritmeja.

**[Osa 3: Viikon harjoitustehtävän tehtävänanto ja vinkit](https://web.microsoftstream.com/video/bfb30003-ff91-440c-8bb5-e4b982b8bad6)** *8:35*

Viikon harjoitustehtävän tehtävänanto.


## Tavoitteet

Tällä viikolla ohjelmistokehityksen teknologioita -kurssilla tavoitteena on perehtyä tietorakenteiden ja algoritmien peruskäsitteisiin. Opettelemme arvioimaan karkeasti erilaisten algoritmisten lähestymistapojen soveltuvuutta kohtaamiimme ohjelmointiongelmiin.

Ohjelmointikielinä esimerkeissä ja tehtävässä esiintyvät TypeScript ja Python, mutta myös muista yleisimmistä kielistä löytyy vastaavat tietorakenteet samoilla ominaispiirteillä.

Tavoitteenamme ei ole oppia laskemaan tai esittämään algoritmiemme tarkkaa tehokkuutta matemaattisilla kaavoilla, vaan käytämme laskukaavoja apuvälineenä ymmärtääksemme, miksi jokin algoritmi suoriutuu samasta tehtävästä tehokkaammin kuin toinen. Emme myöskään harjoittele optimoimaan ohjelmiemme suorituskykyä, vaikka suorituskyky toimiikin tärkeänä mittarina tällä viikolla.

Vaikka osa tietoperustasta voi tuntua matemaattisesti hankalalta, älä lannistu. Aiheen kotitehtävä ei ole matemaattinen, eikä sinun tarvitse osata laskea algoritmien suoritusaikoja itse.

Ohjelmointiongelmien ratkaisemisessa algoritmien lisäksi myös tietorakenteilla on erittäin merkittävä rooli. Tietorakenteiden sisäinen toteutus, esimerkiksi linkitetty lista (LinkedList) tai taulukkolista (ArrayList), vaikuttaa merkittävästi sen soveltuvuuteen erilaisten ongelmien ratkaisemisessa.

Tallentaessamme itse tietoa ohjelmiimme voimme itse vaikuttaa suuresti siihen, kuinka helposti ja nopeasti tallentamamme tieto on ohjelmakoodissa saatavilla. Vertaa esimerkiksi seuraavia mahdollisia tietorakenteita postinumeroiden ja postitoimipaikkojen tietojen tallentamiseksi:

```ts
`79700,Heinävesi
86240,Pyhänkoski
97390,Kierinki
00900,Helsinki
02760,Espoo
02140,Espoo`
```

```json
{
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}
```

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
    "KIURUVESI": ["74701", "74700"],
    "JUUPAJOKI": ["35540"],
    "MUURUVESI": ["73460"]
}
```

Jos tarkoituksesi olisi selvittää postinumeroa `74700` vastaava postitoimipaikan nimi, mitä sen selvittäminen vaatisi eri tietorakenteilla? Entä mikä tietorakenne olisi myöhemmin helpommin laajennettavissa, jos postinumeroalueita varten halutaan tallentaa toimipaikan nimen lisäksi myös muita tietoja? Olisiko näiden tietorakenteiden hyvät puolet jollain tavoin yhdisteltävissä?


## Suositeltu oheismateriaali

Tietojenkäsittelyssä sama ongelma voidaan tyypillisesti ratkaista lukemattomilla erilaisilla tavoilla. Onkin olemassa lukuisia tunnettuja algoritmeja esimerkiksi listan arvojen järjestelemiseksi tai yksittäisen arvon etsimiseksi listalta.

Katso seuraavat kolme videota, joka esittelevät ohjelmistokehittäjän perusosaamisen kannalta keskeisiä algoritmeja sekä tietorakenteita. Videoissa tutustut myös iso O -notaatioon, jonka avulla vertailemme algoritmien tehokkuutta eri kokoisilla syötteillä:

### Video 1: [What Is an Algorithm?](https://youtu.be/PY82qqyWJJs) 7:54

[![What Is an Algorithm?](https://img.youtube.com/vi/PY82qqyWJJs/mq1.jpg)](https://youtu.be/PY82qqyWJJs)


> *We evaluate an algorithm mainly based on how many steps the algorithm takes to solve its problem* &mdash; *[What Is an Algorithm?](https://youtu.be/PY82qqyWJJs)*


### Video 2: [Practical Big-O Notation](https://youtu.be/e6UZ2kzmmdA) 12:59

[![Practical Big-O Notation](https://img.youtube.com/vi/e6UZ2kzmmdA/mq2.jpg)](https://youtu.be/e6UZ2kzmmdA)

> *Big-O notation is how the efficiency of algorithms is typically described. Figuring out the O-notation of an algorithm can look tricky, but as this video shows, for the majority of situations, it's pretty straightforward.* &mdash; *[Practical Big-O Notation](https://youtu.be/e6UZ2kzmmdA)*

### Video 3: [Data Structures You Must Know (as a Software Developer)](https://youtu.be/sVxBVvlnJsM) 7:22

[![Data Structures You Must Know (as a Software Developer)](https://img.youtube.com/vi/sVxBVvlnJsM/mq1.jpg)](https://youtu.be/sVxBVvlnJsM)

> *Linked Lists, Arrays, Hash Table, Stack, Queue, Graph, Tree, Binary Search Tree...*

Tätä videota vastaava esittely tärkeistä tietorakenteista löytyy myös tekstimuodossa osoitteesta https://towardsdatascience.com/8-common-data-structures-every-programmer-must-know-171acf6a1a42


# Oppitunti

## Minkälaisten algoritmien kanssa olet päivittäin tekemisissä?

* Suosittelualgoritmi?
* Hakualgoritmi?
* Paikannusalgoritmi?
* Reitinhakualgoritmi?
* Pakkausalgoritmi?
* Pelialgoritmit?
* Kuvanparannusalgoritmit?
* ...

## Minkälaisia ongelmanratkaisuperiaatteita eri algoritmit hyödyntävät?

* Brute force           <!-- Vertaillaan kaikkia toisiinsa -->
* Divide and conquer    <!-- järjestetään esim. mergesortilla. Käännetään teksti ensin suomesta englanniksi, sitten englannista ruotsiksi -->
* Dynamic               <!-- matemaattisempi, esim. reitinhaku pisteestä a pisteeseen b kun tiedetään reitit a-b ja b-c -->
* Evolutionary          <!-- kokeillaan vastata kyselyyn eri tavoilla ja katsotaan mikä saa parhaan tuloksen. Muutetaan parasta tulosta n. kertaa satunnaisesti ja toistetaan. -->
* Graph traversal       <!-- verkon läpikäynti, esim. optimaaliset reitit. Shakki, ristinolla! -->
* Greedy                <!-- esim. paikannus, käytetään vain kolmea satelliittia vaikka olisi yhteys kymmeneen -->
* Heuristic             <!-- Valitaan suosituin. Valitaan eka. Valitaan halvin. Suositellaan seuraavaa viestiä, jolla on yhteinen tagi. -->
* Learning              <!-- esim. historiaan perustuva päätöksenteko. Pelit? -->
* Mathematical optimization
  * Modeling            <!-- matemaattinen -->
  * Recursion           <!-- liittyy divide and conquer -ajatukseen ja graafien läpikäyntiin: esim. pilkotaan kunnes osataan ratkaista -->
* ...

https://en.wikipedia.org/wiki/Algorithmic_technique#General_techniques

<!-- Tietoa voidaan varastoida tietokoneen muistiin lukuisilla tavoilla. Tapoja, joilla tieto jäsennetään, kutsutaan tietorakenteiksi. Esimerkiksi meille tuttu tietorakenne **lista** mahdollistaa datan tallentamisen, lisäämisen ja etsimisen peräkkäisten arvojen avulla. Listat voidaan toteuttaa "konepellin alla" useilla erilaisilla tavoilla, kuten linkitettynä listana tai taulukkoon perustuvana listana.-->


## Teoriaosuus ja "koodiprojekti"

Tämän oppitunnin tavoitteena on kirjoittaa ohjelma, joka lukee listat suomen- ja englanninkielisistä sanoista ja selvittää, mitkä sanat esiintyvät molemmissa kielissä. Idea on lainattu [Helsingin yliopiston Antti Laaksosen luennolta](https://tira.mooc.fi/syksy-2021/pages/materiaali.html) ja sovellettu omiin tarpeisiimme.

### Sanakirja-aineistot

Aineistona käytämme [Kotimaisten kielten tutkimuskeskuksen nykysuomen sanalistaa](http://kaino.kotus.fi/sanat/nykysuomi/) sekä Linuxin sanalistaa `/usr/share/dict/words`. [Nykysuomen sanalista](https://github.com/hugovk/everyfinnishword/blob/master/kaikkisanat.txt) sisältää noin 94&nbsp;000 sanaa ja Linux-jakelusta riippuen englanninkielinen sanalista sisältää esimerkiksi noin 102&nbsp;000 sanaa.

Nykysuomen sanalistan voit ladata esimerkiksi tästä: [kaikkisanat.txt](https://github.com/hugovk/everyfinnishword/blob/master/kaikkisanat.txt). Sanalistatiedoston on koonnut Hugo van Kemenade ja se löytyy [GitHubista omana projektinaan](https://github.com/hugovk/everyfinnishword).

`/usr/share/dict/words`-tiedosto on joissain Linux-jakeluissa esiasennettuna, mutta jos sitä ei löydy, [voit asentaa sen Debian-ympäristössä näillä komennoilla](https://howtoinstall.co/en/wamerican):

```sh
$ sudo apt update
$ sudo apt install wamerican
```

Mikäli käyttöjärjestelmällesi ei ole saatavilla tätä sanakirjaa, voit generoida oman sanakirjatiedoston osoitteessa http://app.aspell.net/create.

Esimerkeissä käytettävät aineistot ovat riittävän suuria, jotta pystymme huomaamaan merkittäviä eroja erilaisissa tietorakenteissa ja algoritmeissa, joilla yritämme selvittää yhteiset sanat.


### Listojen vertailu komentorivillä

Ensin voimme kokeilla selvittää yhteisten sanojen määrän komentorivillä Linuxin `comm`-komennolla. `comm`-komento edellyttää, että sille annettavat syötteet ovat valmiiksi aakkosjärjestyksessä, joten järjestämme ne `sort`-komennolla ja ohjaamme tulokset syötteiksi `<`-operaattorilla:

```sh
$ comm -1 -2 <(sort /usr/share/dict/words) <(sort kotus-sanalista-v1/kotus-sanalista-suomi.txt)
```

`comm`-komennon tarkemman dokumentaation löydät [täältä](https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html) ja lähdekoodin [GitHubista](https://github.com/coreutils/coreutils/blob/master/src/comm.c).

Jos haluamme selvittää ohjelman suorituksen keston, voimme käyttää Linuxin `time`-komentoa:

```
$ time comm -1 -2 <(sort /usr/share/dict/words) <(sort kotus-sanalista-v1/kotus-sanalista-suomi.txt) > /dev/null

real    0m0,161s
user    0m0,210s
sys     0m0,048s
```

Tässä tapauksessa yhteisten sanojen selvittäminen kesti noin 0,16 sekuntia (real). Miten käy, jos yritämme toteuttaa oman algoritmin saman tiedon selvittämiseksi?


### 1. Oma toteutus: mitkä samat sanat esiintyvät molemmissa kielissä?

Kirjoitetaan skripti, joka lukee kaikki sanat kahdesta tiedostosta listoille. Kun listat on muodostettu, etsitään listalta **A** kaikki sanat, jotka esiintyvät myös listalla **B**! Lopuksi tulostetaan löytyneet sanat:


```python
def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    for word in finnish_words:
        if word in english_words:
            print(word)


if __name__ == '__main__':
    main()
```

```ts
import { readFileSync } from 'fs';
import path from 'path';

function readWordsFromFile(filename: string): readonly string[] {
    return readFileSync(filename, 'utf-8')
        .trim().toLowerCase().split('\n');
}

const finnish = readWordsFromFile(path.join(__dirname, '..', 'finnish.txt'));
const english = readWordsFromFile('/usr/share/dict/words');

for (let fi of finnish) {
    if (english.includes(fi)) {
        console.log(fi);
    }
}
```

* Kuinka kauan algoritmin suoritus kestää?
* Mistä kesto johtuu?
* Mikä on algoritmin kokonaisaikavaatimus tällä hetkellä?
* Mikä on Pythonin `x in list`-operaation aikavaatimus? [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)


#### Ratkaisun tehokkuuden arviointi

> *Algoritmin tehokkuus riippuu siitä, montako askelta se suorittaa. Tavoitteemme on nyt arvioida algoritmin askelten määrää suhteessa syötteen kokoon n. Esimerkiksi jos syötteenä on taulukko, n on taulukon koko, ja jos syötteenä on merkkijono, n on merkkijonon pituus.*
>
> Antti Laaksonen. [Tietorakenteet ja algoritmit -kirja](https://github.com/pllk/tirakirja/raw/master/tirakirja.pdf)

Koska edellä esitetyssä koodissa käydään aina koko suomenkielinen sanalista läpi, on ulomman toistorakenteen tehokkuus suoraan suhteessa suomenkielisten sanojen määrään (n). Jokaista suomenkielistä sanaa kohden käydään läpi lista englanninkielisiä sanoja `word in english_words` tai `english.includes(fi)` -operaatiolla. Sisäisesti tämä operaatio vertailee etsittävää sanaa kaikkiin englanninkielisen listan sanoihin (m).

Vertailuoperaatioita tehdään siis jopa n * m kappaletta, joka meidän aineistollamme tarkoittaa jopa 10&nbsp;000&nbsp;000&nbsp;000 vertailuoperaatiota.

Algoritmin tehokkuus  | Vertailujen määrä | Suoritusaika
----------------------|-------------------|----------
O(n * m)              | ~10 000 000 000   | ?


### Bonus: ohjelman profilointi

Pythonissa on valmiina `cProfile`-niminen moduuli, jonka avulla voimme mitata eri funktioiden suoritusten määrää ja niihin kulunutta aikaa. Seuraavissa vaiheissa hyödynnetään myös profilointia:

```bash
$ python3 -m cProfile -s calls sanalistat.py
```

Yllä olevassa komennossa `-m cProfile` käynnistää profiloijan ja `-s calls` järjestää funktiot niiden suorituskertojen mukaan.


### 2. Miten voimme nopeuttaa algoritmin toimintaa?

Linuxin `comm`-komento edellytti, että aineistot ovat aakkosjärjestyksessä. Olisiko siis järjestyksessä olevien sanojen etsiminen nopeampaa?

Sen sijaan, että kävisimme listan yksi kerrallaan alusta alkaen läpi, voisimme aloittaa etsimisen keskeltä ja rajata etsittävästä aineistosta puolet pois, riippuen siitä, onko etsittävä sana aakkosissa ennen vai jälkeen keskikohdassa olevaa sanaa!

Hakua, jossa puolitamme haettavan aineiston aina keskeltä ja rajaamme seuraavan haun aina puolta pienempään aineistoon kutsutaan **puolitushauksi**, eli **binäärihauksi** ([binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm)).

Seuraavassa Python-koodissa etsitään sanaa "villa", ja verrataan sitä aineiston keskimmäiseen sanaan:

```python
>>> etsittava = "villa"
>>>
>>> keskikohta = len(finnish_words) // 2    # 47_055
>>> finnish_words[keskikohta]
'nimivakuus'
```

Koska yllä olevassa esimerkissä etsitty sana `'villa'` on suurempi kuin keskimmäinen sana `'nimivakuus'`, sanat 0-47055 voidaan rajata pois! Tätä voidaan toistaa niin kauan, kunnes olemme löytäneet etsityn sanan, tai puolittaneet aineiston loppuun.

Voit katsoa konkreettisen visualisoinnin algoritmin suorituksesta esimerkiksi osoitteesta https://www.cs.usfca.edu/~galles/visualization/Search.html tai alla olevasta animaatiosta:

> ![Binary Search by CC BY-SA 4.0. CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/c/c1/Binary-search-work.gif)
>
> *Binary Search by CC BY-SA 4.0. CC BY-SA 4.0. https://commons.wikimedia.org/wiki/File:Binary-search-work.gif*

Muutetaan vaiheessa 1 kehitettyä sovellusta siten, että puolitamme etsittävän aineiston. Toteutetaan siis oma binäärihaku!

#### Puolitushaku Pythonilla

```python
"""
Tiedosto binary_search.py
Tutustu myös valmiiseen toteutukseen https://docs.python.org/3/library/bisect.html
"""
def binary_search(word, list_of_words):
    left = 0
    right = len(list_of_words) - 1

    while left <= right:
        middle = (left + right) // 2
        if list_of_words[middle] < word:
            left = middle + 1
        elif list_of_words[middle] > word:
            right = middle - 1
        else:
            return True

    return False
```

```python
from binary_search import binary_search


def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    # Järjestetään sanat aakkosjärjestykseen
    finnish_words.sort()
    english_words.sort()

    for word in finnish_words:
        if binary_search(word, english_words):
            print(word)


if __name__ == '__main__':
    main()
```

```bash
$ python3 -m cProfile -s calls sanalistat.py
```

#### Puolitushaku TypeScriptillä

```ts
function binarySearch(word: string, sortedWords: readonly string[]): boolean {
    let min = 0;
    let max = sortedWords.length;

    while (min <= max) {
        let middleIndex = Math.trunc((min + max) / 2);
        let middleWord = sortedWords.at(middleIndex)!;

        if (middleWord === word) {
            return true;
        }
        if (word.localeCompare(middleWord) > 0) {
            // word comes after the middle point
            min = middleIndex + 1;
        } else {
            max = middleIndex - 1;
        }
    }
    return false;
}
```

```ts
for (let fi of finnish) {
    if (binarySearch(fi, english)) {
        console.log(fi);
    }
}
```

* Kuinka kauan ohjelman suoritus kestää tällä kertaa?
* Onko ero havaittava edelliseen versioon nähden?
* Mikä on puolitushaun aikavaatimus?
* Mikä on algoritmin kokonaisaikavaatimus nyt?
* Riittäisikö meille, jos vain toinen sanalista olisi järjestetty?


#### Binäärihaun tehokkuuden arviointi

Algoritmimme uudessa versiossa suomenkielinen sanalista käydään edelleen läpi kokonaisuudessaan, eli **n** kertaa. Englanninkielistä sanalistaa puolestaan ei enää käydä läpi kokonaan jokaista suomenkielistä sanaa kohden, vaan sanalistaa puolitetaan, kunnes aineisto on saatu pilkottua loppuun.

**Kuinka monta kertaa aineisto voidaan puolittaa?**

1. kahden pituinen lista voidaan puolittaa kerran (2 == 2<sup>1</sup>)
1. neljän pituinen lista voidaan puolittaa kaksi kertaa (4 == 2<sup>2</sup>)
1. kahdeksan pituinen lista voidaan puolittaa kolme kertaa (8 == 2<sup>3</sup>)
1. kuudentoista pituinen lista voidaan puolittaa neljä kertaa  (16 == 2<sup>4</sup>)
1. ...
1. miljoonan pituinen lista voidaan puolittaa alle 20 kertaa!
1. miljardin pituinen lista voidaan puolittaa alle 30 kertaa! (1 000 000 000 &lt; 2<sup>30</sup>)

Toisin sanoen, tietty lista voidaan aina puolittaa sen **pituuden kaksikantaisen logaritmin verran kertoja**.

> *"logaritmi \[on\] matemaattinen funktio, joka kertoo mihin potenssiin kantaluku on korotettava, jotta saataisiin haluttu luku"*
>
> Logaritmi. Wiktionary. https://fi.wiktionary.org/wiki/logaritmi

Tämä on valtava parannus aikaisempaan lineaariseen hakuun verrattuna, koska nyt yhden sanan hakeminen esimerkiksi 100&nbsp;000 sanan aineistosta vaatii korkeintaan 17 vertailuoperaatiota! Koska etsittäviä sanoja on 94&nbsp;110 kappaletta, vertailuoperaatioita tehdään yhteensä enää alle 1&nbsp;600&nbsp;000 kappaletta.

Seuraava koodiesimerkki havainnollistaa 2-kantaisen logaritmin käyttöä Pythonissa edellä esitetyn tuloksen saamiseksi:

```python
>>> import math
>>>
>>> math.log2(102_401) # maksimimäärä puolitusoperaatioita tämän kokoiselle aineistolle
16.64387027852469
```

Kääntäen ilmaistuna, 102&nbsp;401 sanan pituinen lista voidaan puolittaa kahteen osaan korkeintaan ~17 kertaa.

Algoritmin tehokkuus  | Vertailujen määrä | Suoritusaika
----------------------|-------------------|--------
O(n * log2(m))        | ~2 000 000        | ?


**Huom!** Oikeassa ohjelmistoprojektissa käyttäisit Pythonin valmista [bisect](https://docs.python.org/3/library/bisect.html)-moduulia. JavaScript-kielen standardikirjastossa ei ole binäärihakua valmiina, mutta seikkailunhaluiset voivat asentaa sellaisen jostain lukuisista [npm-paketeista](https://www.npmjs.com/search?q=binary%20search).


### 3. Miten käytetty tietorakenne vaikuttaa ohjelman nopeuteen?

Suomenkielisen sanalistan läpikäyntiä voi olla mahdotonta nopeuttaa, koska haluamme yhä käydä kaikki sanat läpi. Sen sijaan voimme yrittää nopeuttaa englanninkielisten sanojen hakua entisestään käyttämällä jotain muuta tietorakennetta kuin listoja.

Olisiko meillä muita tietorakenteita, joita voisimme käyttää listojen sijasta? Mikä tietorakenne olisi nopea hakujen tekemiseen?

Hajautustaulut (sanakirja), toimivat eri periaatteella kuin listat. Listoilla arvot esiintyvät peräkkäin ja esimerkiksi merkkijono `'tie'` voi olla listan missä tahansa indeksissä. Hajautettavat tietorakenteet toimivat puolestaan eri toimintaperiaatteella. Jokaiselle arvolle lasketaan sijainti tietorakenteessa **hajautusfunktion** avulla, joten teoriassa arvon löytyminen edellyttää vain yhden "indeksin" tarkastamisen tietorakenteesta:

```python
>>> hash('python')
1263623612

>>> hash('java')
362104960

>>> hash('javascript')
-2131589936
```

Sanakirjat ja objektit toimivat hajautusperiaatteella, joten kokeillaan muuttaa aineistoa seuraavasti:

```python
def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    # sanakirjan luominen, dictionary comprehension:
    english_dict = {word: True for word in english_words}

    for word in finnish_words:
        if word in english_dict:
            print(word)

if __name__ == '__main__':
    main()
```

```ts
// see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries
let englishObject = Object.fromEntries(english.map(w => [w, true]));

for (let fi of finnish) {
    if (fi in englishObject) {
        console.log(fi);
    }
}
```

* Kuinka kauan suoritus kestää tällä kertaa?
* Mistä ero johtuu?
* Mikä on dict-tietorakenteen `x in dict`-operaation aikavaatimus? https://wiki.python.org/moin/TimeComplexity
* Sanakirjan muodostaminen: toistorakenne vs. [dict comprehension](https://www.python.org/dev/peps/pep-0274/)

#### Tehokkuuden arviointi

Sanakirjasta tai objektista hakeminen vie keskimäärin yhden operaation. Teoreettisesti epätasaisesti jakautuneet sanakirjat voivat tosin vaatia jopa kokonsa verran hakuoperaatiota, mikäli hajautusfunktio toimii tehottomasti. Koska suomenkielisten sanojen läpikäynnin aikavaatimus on edelleen **O(n)**, mutta englanninkieliset sanat löytyvät vakioajassa, on uuden toteutuksen aikavaatimus **O(n)**:

```python
for word in finnish_words:    # O(n) => listan läpikäynti
    if word in english_dict:  # O(1) => sanakirjasta hakeminen
        print(word)
```

```ts
for (let fi of finnish) {       // O(n) => taulukon läpikäynti
    if (fi in englishObject) {  // O(1) => objektista hakeminen
        console.log(fi);
    }
}
```

Ohjelman suoritusajan laskeminen ei todellisuudessa ole aivan näin yksinkertaista, ja sanakirjan yhteydessä joudumme huomioimaan myös esimerkiksi sanakirjan muodostamiseen kuluvan ajan:

```python
# Dictionary comprehension käy läpi listan english_words, ja asettaa
# sanakirjaan avaimiksi kaikki sanat, ja niille arvoksi True:
english_dict = {word: True for word in english_words}
```

```ts
// map-funktio muodostaa jokaiselle sanalle (esim. "hello" ja "word") taulukon:
// [["hello", true], ["word", true]]. Näistä taulukoista puolestaan muodostetaan
// objekti muodossa { hello: true, word: true };
let englishObject = Object.fromEntries(english.map(w => [w, true]));
```

[Yhden arvon lisääminen vie aikaa saman verran kuin hakeminen](https://stackoverflow.com/q/31091772), eli englanninkielisen aineiston koko `m` vaikuttaa samassa suhteessa tarvittavien operaatioiden määrään sanakirjaa muodostettaessa: **O(m)**.

Näiden muutosten jälkeen ratkaisun tehokkuus on suuruusluokkaa **O(m) + O(n)**, eli lyhyemmin ilmaistuna **O(m + n)**. `m + n` kasvaa lineaarisesti alkioiden määrän mukaan, joten se esitetään tyypillisesti vain yhden muuttujan avulla  **O(n)**. Tämä toteutus on toistaiseksi kaikkein tehokkain.


Algoritmin tehokkuus  | Operaatioiden määrä  | Suoritusaika
----------------------|----------------------|--------
O(n)                  | ~200 000             | ?



### 4. Ongelman muotoilu toisella tavalla

Määritellään ongelma uudelleen joukko-opin näkökulmasta: yhden kielen sanat on **joukko sanoja**. Kahden kielen yhteiset sanat ovat **kahden joukon leikkaus**. Käyttämällä [Pythonin joukkoja (set)](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset), haluttu osajoukko saadaan selville ilman yhtään itse kirjoitettua toisto-, vertailu- tai hakuoperaatiota:

```python
>>> {'rodeo', 'mafia', 'villa', 'peruna', 'riisi'} & {'rodeo', 'mafia', 'villa', 'potato', 'rice'}
{'rodeo', 'mafia', 'villa'}
```

Joukoiksi muutettuna Python-koodi näyttää esimerkiksi seuraavalta:

```python
def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    intersection = set(finnish_words) & set(english_words)
    for word in intersection:
        print(word)


if __name__ == '__main__':
    main()
```

JavaScript-kielen standardikirjastosta löytyy vastaava [Set-tietorakenne](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set), mutta sille ei valitettavasti ole valmista leikkaus/intersection-operaatiota. Tällainen voidaan kuitenkin tarvittaessa [toteuttaa itse esim. taulukon filter-operaation avulla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#iterating_sets):

```ts
const englishSet = new Set(english);
const intersection = finnish.filter(fi => englishSet.has(fi));
```

* Mikä on suoritusaika nyt?
* Mikä on set-tietorakenteen leikkauksen aikavaatimus? https://wiki.python.org/moin/TimeComplexity
* Kuinka pärjäämme nyt suhteessa Linuxin `comm`-komentoon?


### 5. Ohjelman mahdolliset seuraavat optimoinnit

Yhteisten sanojen selvittämisen ongelma olisi ratkaistavissa edellä käsiteltyjen tapojen lisäksi monilla muillakin tavoilla. Yksi mahdollinen tapa voisi olla käydä suomen- ja englanninkielistä sanalistaa samanaikaisesti läpi siten, että edetään aina sillä listalla, jolla käsiteltävä sana on aakkosissa ensimmäisenä. Yhteiset sanat löytyisivät silloin, kun molemmilla listoilla käsiteltäisiin samaa sanaa.

Mikä olisi tämän ratkaisutavan aikavaatimus? Kannattaisiko jatkokehitys tehdä suorituskyvyn paranemisen toivossa?


## Lajittelualgoritmit ja suoritusajan kasvu tietomäärän kasvaessa

> *Lajittelualgoritmit eli järjestämisalgoritmit ovat varsin keskeisiä algoritmeja ohjelmistotekniikassa. Lajittelualgoritmin tarkoitus on järjestää lista sovittuun järjestykseen, esimerkiksi numero- tai aakkosjärjestykseen. Lajittelualgoritmeilla on keskeinen merkitys sovelluksissa, jotka käsittelevät suuria tietomääriä. Lajittelualgoritmien nopeutta on tutkittu ohjelmistotekniikassa verrattain paljon niiden merkittävyyden vuoksi. Parhaiden yleiskäyttöisten lajittelualgoritmien asymptoottinen suoritusaika on luokkaa O(nlog n).*
>
> https://fi.wikipedia.org/wiki/Lajittelualgoritmi


"Parhaiden yleiskäyttöisten lajittelualgoritmien asymptoottinen suoritusaika on luokkaa O(n * log n)", mitä se tarkoittaa? Entä onko esim n<sup>2</sup> merkittävästi huonompi suoritusaika?

Seuraava taulukko antaa käsityksen eri operaatioiden määrän suuruusluokista eri aineistojen koolla:

Tehokkuus       | Opiskelijoita (n = 50)| Tapahtumia (n = 4000) | Sanoja (n = 100 000)  | Kansalaisia (n = 5 500 000)
----------------|----------------------:|----------------------:|----------------------:|-----------------------:
O(1)            | 1                     | 1                     | 1                     | 1
O(log(n))       | ~6                    | ~12                   | ~17                   | ~22
O(n)            | 50                    | 4 000                 | 100 000               | 5 500 000
O(n * log(n))   | ~282                  | ~47 000               | ~1 000 000            | ~123 000 000
O(n * n)        | ~2 500                | ~16 000 000           | ~10 000 000 000       | ~30 000 000 000 000


**Yhteenveto**

1. Mihin tehokkuusluokkaan sijoittuu haku Pythonin listalta?
1. Mihin tehokkuusluokkaan sijoittuu haku Pythonin sanakirjasta?
1. Mihin tehokkuusluokkaan sijoittuu puolitushaku?
1. Mihin tehokkuusluokkaan sijoittuu hyvä lajittelualgoritmi?
1. Mihin tehokkuusluokkaan sijoittuu heikko lajittelualgoritmi?


# Tehtävät

Tämän viikon tehtävissä käsittelemme MyHelsinki Open API -rajapinnan tapahtumia, ja suodatamme ja lajittelemme tapahtumia niiden ajankohdan perusteella. Katso tarkemmat ohjeet Teamsin tehtävät-välilehdeltä.

----

# Lisenssit ja tekijänoikeudet

## Oppitunnin esimerkin idea

Idea suomen- ja englanninkielisten sanalistojen yhteisten sanojen selvittämisestä on lainattu [Helsingin yliopiston Antti Laaksosen luennolta](https://tira.mooc.fi/syksy-2021/pages/materiaali.html) ja sovellettu omiin tarpeisiimme.


## Suomenkielisen sanalistan tekijänoikeudet

    Copyright (C) Kotimaisten kielten tutkimuskeskus 2006
    Kotimaisten kielten tutkimuskeskuksen nykysuomen sanalista, versio 1
    Julkaistu 15.12.2006

    Sanalista julkaistaan GNU LGPL -lisenssillä.
    Lisenssiteksti luettavissa osoitteessa http://www.gnu.org/licenses/lgpl.html