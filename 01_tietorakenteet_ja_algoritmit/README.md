# Tietorakenteet ja algoritmit


> *Algoritmi (algorithm) on toimintaohje, jota seuraamalla voimme ratkaista jonkin laskennallisen ongelman. Algoritmille annetaan syöte (input), joka
kuvaa ratkaistavan ongelman tapauksen, ja algoritmin tulee tuottaa tuloste (output), joka on vastaus sille annettuun syötteeseen*
>
> *Antti Laaksonen, [Tietorakenteet ja algoritmit -kirja](https://github.com/pllk/tirakirja/raw/master/tirakirja.pdf)*


## Tavoitteet

Tällä viikolla ohjelmistokehityksen teknologioita -kurssilla tavoitteena on perehtyä tietorakenteiden ja algoritmien peruskäsitteisiin. Opettelemme arvioimaan karkeasti erilaisten algoritmisten lähestymistapojen soveltuvuutta kohtaamiimme ohjelmointiongelmiin. 

Tavoitteenamme ei ole oppia laskemaan tai esittämään algoritmiemme tarkkaa tehokkuutta matemaattisilla kaavoilla, vaan käytämme laskukaavoja apuvälineenä ymmärtääksemme, miksi jokin algoritmi suoriutuu samasta tehtävästä tehokkaammin kuin toinen. Emme myöskään harjoittele optimoimaan ohjelmiemme suorituskykyä, vaikka suorituskyky toimiikin tärkeänä mittarina tällä viikolla.

Ohjelmointiongelmien ratkaisemisessa algoritmien lisäksi myös tietorakenteilla on erittäin merkittävä rooli. Tietorakenteiden sisäinen toteutus, esimerkiksi linkitetty lista tai taulukkolista, vaikuttaa merkittävästi sen soveltuvuuteen erilaisten ongelmien ratkaisemisessa. 

Tallentaessamme itse tietoa ohjelmiimme voimme itse vaikuttaa suuresti siihen, kuinka helposti ja nopeasti tallentamamme tieto on ohjelmakoodissa saatavilla. Vertaa esimerkiksi seuraavia mahdollisia tietorakenteita postinumeroiden ja postitoimipaikkojen tietojen tallentamiseksi:

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

Jos tarkoituksesi olisi selvittää postinumeroa 74700 vastaava postitoimipaikan nimi, mitä sen selvittäminen vaatisi eri tietorakenteilla? Entä kumpi tietorakenne olisi myöhemmin helpommin laajennettavissa, jos postinumeroalueita varten halutaan tallentaa toimipaikan nimen lisäksi myös muita tietoja? Olisiko näiden kahden tietorakenteen hyvät puolet jollain tavoin yhdistettävissä?

## Ennakkotehtävät

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




## Oppitunti

### Minkälaisten algoritmien kanssa olet päivittäin tekemisissä?

* Suosittelualgoritmi?
* Hakualgoritmi?
* Paikannusalgoritmi?
* Reitinhakualgoritmi?
* Pakkausalgoritmi?
* Pelialgoritmit?
* Kuvanparannusalgoritmit?

### Minkälaisia ongelmanratkaisuperiaatteita eri algoritmit hyödyntävät?

* Brute force           <!-- Vertaillaan kaikkia toisiinsa -->
* Divide and conquer    <!-- järjestetään esim. mergesortilla. Pilkotaan reitinhaku a-c paloiksi a-b ja a-c -->
* Dynamic               <!-- matemaattisempi, esim. reitinhaku pisteestä a pisteeseen b kun tiedetään reitit a-b ja b-c -->
* Evolutionary          <!-- kokeillaan vastata kyselyyn eri tavoilla ja katsotaan mikä saa parhaan tuloksen. Muutetaan parasta tulosta n. kertaa satunnaisesti ja toistetaan. -->
* Graph traversal       <!-- verkon läpikäynti, esim. optimaaliset reitit. Shakki, ristinolla! -->
* Greedy                <!-- esim. paikannus, käytetään vain kolmea satelliittia vaikka olisi yhteys kymmeneen -->
* Heuristic             <!-- Valitaan suosituin. Valitaan eka. Valitaan halvin. Suositellaan seuraavaa viestiä, jolla on yhteinen tagi. -->
* Learning              <!-- esim. historiaan perustuva päätöksenteko. Pelit? -->
* Mathematical optimization
  * Modeling            <!-- matemaattinen -->
  * Recursion           <!-- liittyy divide and conquer -ajatukseen ja graafien läpikäyntiin: esim. pilkotaan kunnes osataan ratkaista -->

https://en.wikipedia.org/wiki/Algorithmic_technique#General_techniques

<!-- Tietoa voidaan varastoida tietokoneen muistiin lukuisilla tavoilla. Tapoja, joilla tieto jäsennetään, kutsutaan tietorakenteiksi. Esimerkiksi meille tuttu tietorakenne **lista** mahdollistaa datan tallentamisen, lisäämisen ja etsimisen peräkkäisten arvojen avulla. Listat voidaan toteuttaa "konepellin alla" useilla erilaisilla tavoilla, kuten linkitettynä listana tai taulukkoon perustuvana listana.-->


## Teoriaosuus ja "koodiprojekti"

Tämän oppitunnin tavoitteena on kirjoittaa ohjelma, joka lukee listat suomen- ja englanninkielisistä sanoista ja selvittää, mitkä sanat esiintyvät molemmissa kielissä. Aihe on lainattu [Helsingin yliopiston Antti Laaksosen luennolta](https://www.cs.helsinki.fi/u/ahslaaks/tira19/luento1/) ja sovellettu omiin tarpeisiimme.

Aineistona käytämme [Kotimaisten kielten tutkimuskeskuksen nykysuomen sanalistaa](http://kaino.kotus.fi/sanat/nykysuomi/) sekä Linuxin sanalistaa `/usr/share/dict/words`. Nykysuomen sanalista [kotus-sanalista-suomi.txt](src/kotus-sanalista-v1/kotus-sanalista-suomi.txt) sisältää 94&nbsp;110 sanaa ja Linux-jakelusta riippuen englanninkielinen sanalista voi sisältää esimerkiksi 102&nbsp;401 sanaa. Tämä aineisto on riittävän suuri, jotta pystymme huomaamaan merkittäviä eroja erilaisissa tietorakenteissa ja algoritmeissa, joilla yritämme selvittää yhteiset sanat.


### 1. Mitkä samat sanat esiintyvät molemmissa kielissä?

Kirjoitetaan Python-skripti, joka lukee kaikki sanat kahdesta tiedostosta listoille. Kun listat on muodostettu, etsitään listalta A kaikki sanat, jotka esiintyvät myös listalla B! Lopuksi tulostetaan löytyneet sanat:


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

* Kuinka kauan algoritmin suoritus kestää?
* Mistä kesto johtuu?
* Mikä on algoritmin kokonaisaikavaatimus tällä hetkellä?
* Mikä on Pythonin `x in list`-operaation aikavaatimus? https://wiki.python.org/moin/TimeComplexity


#### Algoritmin tehokkuuden arviointi

> *Algoritmin tehokkuus riippuu siitä, montako askelta se suorittaa. Tavoitteemme on nyt arvioida algoritmin askelten määrää suhteessa syötteen kokoon n. Esimerkiksi jos syötteenä on taulukko, n on taulukon koko, ja jos syötteenä on merkkijono, n on merkkijonon pituus.*
>
> *Antti Laaksonen, [Tietorakenteet ja algoritmit -kirja](https://github.com/pllk/tirakirja/raw/master/tirakirja.pdf)*

Koska edellä esitetyssä koodissa käydään aina koko suomenkielinen sanalista läpi, on ulomman toistorakenteen tehokkuus suoraan suhteessa suomenkielisten sanojen määrään (n). Jokaista suomenkielistä sanaa kohden käydään läpi lista englanninkielisiä sanoja `word in english_words` -operaatiolla. Sisäisesti tämä operaatio vertailee etsittävää sanaa kaikkiin englanninkielisen listan sanoihin (m). 

Vertailuoperaatioita tehdään siis jopa n * m kappaletta<!--, joka meidän aineistollamme tarkoittaa jopa 9&nbsp;000&nbsp;000&nbsp;000 vertailuoperaatiota-->.

Algoritmin tehokkuus  | Vertailujen määrä             | Suoritusaika
----------------------|-------------------------------|--------------
O(n * m)              | ?                             | ?


### 2. Miten voimme nopeuttaa algoritmin toimintaa?

Tiedämme, että molemmat aineistot ovat aakkosjärjestyksessä. Sen sijaan, että kävisimme listan yksi kerrallaan alusta alkaen läpi,  voimmekin aloittaa etsimisen keskeltä ja rajata etsittävästä aineistosta puolet pois, riippuen siitä, onko etsittävä arvo aakkosissa ennen vai jälkeen keskikohdassa olevaa alkiota!

Kun lista on järjestyksessä, voidaan etsiminen aloittaa keskeltä ja rajata etsimistä aina siten, että pystymme puolittamaan etsittävän alueen! Tätä kutsutaan binäärihauksi eli puolitushauksi: https://www.cs.usfca.edu/~galles/visualization/Search.html

```python
>>> etsittava = "villa"
>>> keskikohta = len(finnish_words) // 2 # 47055
>>> finnish_words[keskikohta]
'nimivakuus'
```

Koska yllä olevassa esimerkissä etsitty sana `'villa'` on suurempi kuin keskimmäinen sana `'nimivakuus'`, sanat 0-47055 voidaan rajata pois! Tätä voidaan toistaa niin kauan, kunnes olemme löytäneet etsityn sanan, tai puolittaneet aineiston loppuun.

Muutetaan vaiheessa 1 kehitettyä sovellusta siten, että puolitamme etsittävän aineiston. Toteutetaan siis oma binäärihaku! 

```python
# tiedosto binary_search.py
# tutustu myös valmiiseen toteutukseen https://docs.python.org/3/library/bisect.html
def binary_search(word, list_of_words):
    left = 0
    right = len(list_of_words) - 1

    while left <= right:
        middle = int((left + right) / 2)
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

    for word in finnish_words:
        if binary_search(word, english_words):
            print(word)


if __name__ == '__main__':
    main()
```

```bash
python3 -m cProfile -s calls sanalistat.py
```

* Kuinka kauan ohjelman suoritus kestää tällä kertaa? 
* Onko ero havaittava edelliseen versioon nähden? 
* Mikä on puolitushaun aikavaatimus?
* Mikä on algoritmin kokonaisaikavaatimus nyt?
* Riittäisikö meille, jos vain toinen aineisto olisi järjestetty?


#### Binäärihaun tehokkuuden arviointi

Algoritmimme uudessa versiossa suomenkielinen sanalista käydään edelleen läpi kokonaisuudessaan, eli n kertaa. Englanninkielistä sanalistaa puolestaan ei enää käydä läpi kokonaan jokaista suomenkielistä sanaa kohden, vaan sanalistaa puolitetaan, kunnes aineisto on saatu pilkottua loppuun.

Entä kuinka monta kertaa aineisto voidaan puolittaa, jotta jäljelle jää vielä jotain puolitettavaa?

1. luku kaksi voidaan puolittaa kerran
1. luku neljä voidaan puolittaa kaksi kertaa
1. luku kahdeksan voidaan puolittaa kolme kertaa
1. luku kuusitoista voidaan puolittaa neljä kertaa...

Toisin sanoen, tietty lista voidaan aina puolittaa sen pituuden kaksikantaisen logaritmin verran kertoja. Tämä on valtava parannus aikaisempaan lineaariseen hakuun verrattuna, koska nyt yhden sanan hakeminen esimerkiksi 102&nbsp;401 sanan aineistosta vaatii korkeintaan 17 vertailuoperaatiota! Maksimissaan vertailuja tehdään siis yhteensä enää alle 1&nbsp;600&nbsp;000 kappaletta.

```python
>>> import math
>>>
>>> math.log2(102_401) # maksimimäärä puolitusoperaatioita tämän kokoiselle aineistolle
16.64387027852469
```

Algoritmin tehokkuus  | Vertailujen määrä     | Suoritusaika
----------------------|-----------------------|--------
O(n * log(m))         | ?                     | ?


**Huom!** Oikeassa ohjelmistoprojektissa käyttäisit Pythonin valmista [bisect](https://docs.python.org/3/library/bisect.html)-moduulia, mutta koska haluamme oppia, toteutamme algoritmin itse.

### 3. Miten käytetty tietorakenne vaikuttaa ohjelman nopeuteen?

Suomenkielisen sanalistan läpikäyntiä voi olla mahdotonta nopeuttaa, koska haluamme yhä käydä kaikki sanat läpi. Sen sijaan voimme yrittää nopeuttaa englanninkielisten sanojen hakua entisestään käyttämällä jotain muuta tietorakennetta kuin listoja.

Olisiko meillä muita tietorakenteita, joita voisimme käyttää listojen sijasta? Mikä tietorakenne olisi nopea hakujen tekemiseen?

Hajautustaulut (sanakirja), toimivat eri periaatteella kuin listat. Listoilla arvot esiintyvät peräkkäin ja esimerkiksi merkkijono 'nimi' voi olla listan ensimmäisenä tai viimeisenä, riippuen listan muusta sisällöstä. Hajautettavat tietorakenteet toimivat puolestaan eri toimintaperiaatteella. Jokaiselle arvolle lasketaan sijainti tietorakenteessa hajautusfunktion avulla, joten teoriassa arvon löytyminen edellyttää vain yhden arvon tarkastamisen tietorakenteesta: O(1):

```python
>>> hash('python')
1263623612
>>> hash('java')
362104960
>>> hash('javascript')
-2131589936
```

Meidän tarvitsee luoda sanakirja vain siitä listasta, josta etsimme sanoja:

```python
def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    english_dict = {word: True for word in english_words}
    for word in finnish_words:
        if word in english_dict:
            print(word)


if __name__ == '__main__':
    main()

```

* Kuinka kauan suoritus kestää tällä kertaa?
* Mistä ero johtuu?
* Mikä on dict-tietorakenteen `x in dict`-operaation aikavaatimus? https://wiki.python.org/moin/TimeComplexity
* Sanakirjan muodostaminen: toistorakenne vs. [dict comprehension](https://www.python.org/dev/peps/pep-0274/)

#### Sanakirjatoteutuksen tehokkuuden arviointi

Sanakirjasta hakeminen vie keskimäärin yhden operaation, vaikka teoreettisesti epätasaisesti jakautuneet sanakirjat voivat vaatia jopa kokonsa verran hakuoperaatiota, mikäli hajautusfunktio toimii tehottomasti. Sanakirjan muodostaminen vie aikaa saman verran kuin sanakirjasta hakeminen, eli englanninkielisen aineiston koko `m` vaikuttaa samassa suhteessa tarvittavien operaatioiden määrään sanakirjaa muodostettaessa. Hakuoperaatioita tehdään edelleen `n` kappaletta, joten tehokkuus on suuruusluokkaa O(m + n) tai O(n).

Algoritmin tehokkuus  | Operaatioiden määrä  | Suoritusaika
----------------------|----------------------|--------
O(n)                  | ?                    | ?

### 4. Ongelman muotoilu toisella tavalla

Määritellään ongelma uudelleen joukko-opin näkökulmasta: yhden kielen sanat on joukko sanoja. Kahden kielen yhteiset sanat ovat kahden joukon leikkaus. Käyttämällä [Pythonin joukkoja (set)](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset), haluttu osajoukko saadaan selville ilman yhtään itse kirjoitettua toisto-, vertailu- tai hakuoperaatiota:

```python
>>> {'rodeo', 'mafia', 'villa', 'peruna', 'riisi'} & {'rodeo', 'mafia', 'villa', 'potato', 'rice'}
{'rodeo', 'mafia', 'villa'}
```

Joukoiksi muutettuna koodi näyttää esimerkiksi seuraavalta:

```python
def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    intersection = set(finnish_words) & set(english_words)
    for word in intersection:
        print(word)


if __name__ == '__main__':
    main()
```

* Mikä on suoritusaika nyt?
* Mikä on set-tietorakenteen leikkauksen aikavaatimus? https://wiki.python.org/moin/TimeComplexity



## Lajittelualgoritmit ja suoritusajan kasvu tietomäärän kasvaessa

> *Lajittelualgoritmit eli järjestämisalgoritmit ovat varsin keskeisiä algoritmeja ohjelmistotekniikassa. Lajittelualgoritmin tarkoitus on järjestää lista sovittuun järjestykseen, esimerkiksi numero- tai aakkosjärjestykseen. Lajittelualgoritmeilla on keskeinen merkitys sovelluksissa, jotka käsittelevät suuria tietomääriä. Lajittelualgoritmien nopeutta on tutkittu ohjelmistotekniikassa verrattain paljon niiden merkittävyyden vuoksi. Parhaiden yleiskäyttöisten lajittelualgoritmien asymptoottinen suoritusaika on luokkaa O(nlog n).*
>
> https://fi.wikipedia.org/wiki/Lajittelualgoritmi


"Parhaiden yleiskäyttöisten lajittelualgoritmien asymptoottinen suoritusaika on luokkaa O(nlog n)", mitä se tarkoittaa? Entä onko esim n<sup>2</sup> merkittävästi huonompi suoritusaika?

Tehokkuus       | Opiskelijoita (n = 50)  | Tapahtumia (n = 4000) | Sanoja (n = 100 000)  | Kansalaisia (n = 5 500 000)
----------------|---------------------|-------------------|-------------------|------------------------
O(1)            | 1                   | 1                 | 1                 | 1
O(n)            | 50                  | 4 000             | 100 000           | 5 500 000
O(log(n))       | ?                   | ?                 | ?                 | ?
O(n * log(n))   | ?                   | ?                 | ?                 | ?
O(n * n)        | ?                   | ?                 | ?                 | ?




## Viikon koodaustehtävä

Tämän viikon tehtävänä on harjoitella vapaavalintaisen järjestämisalgoritmin toteuttamista. Voit valita toteutettavan järjestämisalgoritmin esimerkiksi seuraavista:

* Lisäyslajittelu eli Insertion Sort: https://en.wikipedia.org/wiki/Insertion_sort

	<a title="Simpsons contributor / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" href="https://commons.wikimedia.org/wiki/File:Insertion_sort.gif"><img width="128" alt="Insertion sort" src="https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif"></a>

* Lomituslajittelu eli Merge Sort: https://en.wikipedia.org/wiki/Merge_sort

	<a title="Swfung8 / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" href="https://commons.wikimedia.org/wiki/File:Merge-sort-example-300px.gif"><img width="256" alt="Merge-sort-example-300px" src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif"></a>

* Kuplalajittelu eli Bubble Sort: https://en.wikipedia.org/wiki/Bubble_sort

	<a href="https://commons.wikimedia.org/wiki/File:Bubble-sort-example-300px.gif#/media/File:Bubble-sort-example-300px.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" alt="Bubble-sort-example-300px.gif"></a>

* Pikalajittelu eli Quicksort: https://en.wikipedia.org/wiki/Quicksort
	
	<a href="https://commons.wikimedia.org/wiki/File:Sorting_quicksort_anim.gif#/media/File:Sorting_quicksort_anim.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif" alt="Sorting quicksort anim.gif"></a>

Voit valita itsellesi mieluisen algoritmin esimerkiksi tutustumalla ensin niiden tehokkuuteen, tai valita sen, joka vaikuttaa toteutukseltaan sopivan yksinkertaiselta. Muista myös, että voit kysyä Teamsissa neuvoa mihin vain tehtävässä kohtaamaasi haasteeseen liittyen. Todennäköisesti samojen haasteiden parissa kamppailee myös moni muu kurssilainen.

**Huom!** Oikeassa ohjelmistoprojektissa käyttäisit Pythonin valmiita järjestämisfunktioita, joita esitellään esimerkiksi osoitteessa https://docs.python.org/3/howto/sorting.html. Tämän harjoituksen tavoitteena on kuitenkin opetella itse toteuttamaan jokin tunnettu järjestämisalgoritmi.


### Järjesteltävä aineisto

MyHelsinki Open API on Helsinki Marketingin tarjoama avoin REST-rajapinta kaupungin tapahtumien, paikkojen ja aktiviteettien tietoihin. Rajapinnan dokumentaatio löytyy Swagger-muodossa osoitteesta http://open-api.myhelsinki.fi/doc. Kyseisessä osoitteessa on dokumentoituna niin resurssien osoitteet, niiden tukemat parametrit kuin palautettujen JSON-tietueiden rakenne.

Tässä tehtävässä hyödynnetään tapahtumarajapinnan tarjoamaa aineistoa osoitteesta http://open-api.myhelsinki.fi/v1/events/. Tapahtumat palautetaan rajapinnasta epäjärjestyksessä, joten joudut itse huolehtimaan tapahtumien järjestämisestä alkamisajan mukaan. 

Huomaa, että **kaikilla rajapinnan palauttamilla tapahtumilla ei välttämättä ole alkamisaikaa**. Tällaisten tapahtumien kohdalla voit itse päättää, jätätkö tapahtumat huomioimatta vai kehitätkö niille vapaavalintaisen erillisen logiikan. Osalle tapahtumista on myös annettu nimet useilla eri kielillä, kun taas joiltain nimiä puuttuu. Myös tällaisten tapahtumien kohdalla saat itse päättää, miten käsittelet tapahtumat.

> *Some examples where you can find direct application of sorting techniques include: Sorting by price, popularity etc in e-commerce websites*
>
> *https://u.osu.edu/cstutorials/2016/11/21/7-algorithms-and-data-structures-every-programmer-must-know/*

### Koodaustehtävä: events_by_date.py

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

...
```

Arvioi tehtävää ratkaistessasi järjestämiseen kuluvaa aikaa. Miten esimerkiksi aineiston koon kaksinkertaistaminen vaikuttaisi ohjelmasi suoritusaikaan? 

### Tehtävän arviointi

Ratkaisu, joka sisältää toimivan itse mallin mukaan toteutetun järjestelyalgoritmin, hyväksytään arvosanalla 5. Myös puutteelliset ratkaisut hyväksytään eri arvosanoin, kunhan niissä osoitetaan selvää yritystä tehtävän ratkaisemiseksi.

Toiminnallisesti oikea ratkaisu, joka oman järjestelyalgoritmin sijasta hyödyntää Pythonin valmiita [sort-operaatioita](https://docs.python.org/3/howto/sorting.html), oikeuttaa arvosanaan 3.

### Tehtävän palauttaminen

Palauta koodaamasi lähdekooditiedosto(t) sellaisenaan, eli **ei pakattuna** Teamsissa olevaan palautuslaatikkoon seuraavaan oppituntiin mennessä.


----

## Suomenkielisen sanalistan tekijänoikeudet 

    Copyright (C) Kotimaisten kielten tutkimuskeskus 2006
    Kotimaisten kielten tutkimuskeskuksen nykysuomen sanalista, versio 1
    Julkaistu 15.12.2006

    Sanalista julkaistaan GNU LGPL -lisenssillä.
    Lisenssiteksti luettavissa osoitteessa http://www.gnu.org/licenses/lgpl.html