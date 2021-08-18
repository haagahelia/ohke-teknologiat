# Python

Oppitunnilla tavoitteemme on päästä vauhtiin Python-koodin kirjoittamisessa. Tavoitteena ei ole oppia kielen koko syntaksia tai kaikkia rakenteita, vaan saada jokin käsitys kielen piirteistä sekä siihen liittyvistä työtavoista. Viikon itsenäisen työn osuudessa pystytte itsenäisesti omaksumaan  lisää syntaksia ja tutustumaan kielen perusrakenteisiin.

Tämän viikon oppimistavoitteena on pystyä toteuttamaan kohtuullisen yksinkertainen Python-skripti, joka hyödyntää ulkopuolisesta palvelusta ladattavaa JSON-muotoista aineistoa.

Pythonia käsitellessämme odotamme jo kohtuullisen vahvaa osaamista Javan ja JavaScriptin syntakseista ja standardikirjastoista. Jos haluat päästä nopeasti vauhtiin, voit lukea esimerkiksi tutoriaalin ["Learn Python in 10 minutes"](https://www.stavros.io/tutorials/python/) tai tutustua [Cheat sheet -muistiinpanoihin](https://www.pythoncheatsheet.org/).

Tämän GitHub-repositorion oppimateriaali on tarkoitettu oppitunnin rungoksi, eikä se riitä pääasialliseksi Python-materiaaliksi kurssilla. Laajempia ja laadukkaita oppimateriaaleja löytyy mm. seuraavista lähteistä:

* Lappeenrannan Yliopiston Python 3 –ohjelmointiopas: https://lutpub.lut.fi/handle/10024/162088
* Pythonin oma "The Python Tutorial": https://docs.python.org/3/tutorial/
* Mooc.fi:n Ohjelmoinnin perusteet Pythonilla -kurssi: https://python-k20.mooc.fi/
* Codecademy:n "Learn Python 3" -kurssi: https://www.codecademy.com/courses/learn-python-3/

Lisää hyvä lähteitä löydät hakukoneilla. Jaathan vinkkejä hyvistä materiaaleista myös kurssin Teamsissa!


# Videot

**[Osa 1: Python-kielen perusrakenteet ja komentorivikäyttö](https://web.microsoftstream.com/video/497d7df3-1629-49f9-b460-82c1d479b03d)** *43:09*

**[Osa 2: Pythonin tietorakenteet, ehtolauseet ja toistolauseet](https://web.microsoftstream.com/video/0f31953b-417b-4669-915d-ca35917bfbc0)** *1:03:17*



# Oppitunnin aiheet

Oppitunnilla käytämme aluksi Pythonia komentoriviltä interaktiivisella tulkilla, jotta opimme nopeasti kokeilemisen kautta käyttämään Pythonin perusrakenteita. Tämän jälkeen tutustumme Python-tiedostojen editointiin VS Codella.

Lopuksi tutustumme myös muihin tapoihin hyödyntää Pythonia: "Python as a swiss army knife".

## "Python as a calculator"

> *"Python can be used as a calculator to compute arithmetic operations like addition, subtraction, multiplication and division. Python can also be used for trigonometric calculations and statistical calculations."*
>
> *Peter D. Kazarinoff. Problem Solving with Python. [Python as a Calculator.](https://problemsolvingwithpython.com/03-The-Python-REPL/03.01-Python-as-a-Calculator/)*

### REPL (Read–eval–print loop)

Pythonia voidaan käyttää interaktiivisen tulkin avulla. Se onkin helpoin tapa tutustua kielen ominaisuuksiin. Python käynnistyy oletuksena interaktiivisessa tilassa komennolla `python3`, tai asennuksestasi riippuen esim. `python` tai `py`.

```
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Interaktiivisella tulkilla lausekkeiden tuloksia ei tarvitse erikseen tulostaa, vaan sijoittamattomat arvot näytetään automaattisesit ruudulla.

Kokeile Pythonin laskuoperaatioita sivun https://www.pythoncheatsheet.org/#Python-Basics ohjeiden mukaan!

### Kommentit


```python
# tämä on yksirivinen kommentti

""" tämä on monirivinen merkkijono, joita
    käytetään pythonissa myös usein kommentteina """
```

```python
// tämä ei ole kommentti!
```

### Muuttujat ja tietotyypit

```python
kaupunki = "Helsinki"
vakiluku = 648_553

type(kaupunki) # str
type(vakiluku) # int
```


### Merkkijonot

Pythonin merkkijonoissa voidaan käyttää joko heittomerkkejä `'` tai lainausmerkkejä `"`. Moniriviset merkkijonot aloitetaan ja päätetään kolmella merkillä. Merkkijonojen yhdistämiseen voidaan käyttää `+` -merkkiä, joskin Python 3:ssa merkkijonojen yhdistelemiseksi on myös parempi tapa: [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals):

```python
>>> kaupunki = "Helsinki"
>>> vakiluku = 648_553
>>> print(f'Kaupungissa {kaupunki} on {vakiluku} asukasta!')
```

```
Kaupungissa Helsinki on 648553 asukasta!
```

Huomaa, että yllä muotoiluja sisältävän merkkijonon eteen on laitettu f-kirjain `f''`!

### Tulostaminen

Tulostaminen tapahtuu `print`-funktiolla, jolle voidaan antaa tarvittaessa useampia tulostettavia arvoja:

```python
>>> print('Hello world!')
>>> print('Hello', 'world!')
```


### Merkkijonojen käsittely

Pythonissa merkkijonojen merkkejä ja osamerkkijonoja voidaan hakea indeksien avulla aivan kuten listojen alkioita. Yksi numero tarkoittaa yksittäistä merkkiä, kun taas `i:j` tarkoittaa väliä. Jos alku- tai loppuindeksi jätetään ilmoittamatta, käytetään alkuna nollaa ja loppuna merkkijonon viimeistä merkkiä. Python sallii myös negatiiviset indeksit, jotka lasketaan merkkijonon lopusta lähtien!

```python
kaupunki = 'Helsinki'
kaupunki[0]     # 'H'
kaupunki[0:2]   # 'He'
kaupunki[2:4]   # 'ls'
kaupunki[-1]    # 'i'
kaupunki[-2:]   # 'ki'
```

Tavallisten `upper` ja `lower` -metodien lisäksi Pythonin merkkijonoilla on kätevä `title`-metodi:

```python
kaupunki = 'vantaa'
kaupunki.upper() # 'VANTAA'
kaupunki.lower() # 'vantaa'
kaupunki.title() # 'Vantaa'
```

Merkkijonojen sisältämiä osamerkkijonoja voidaan selvittää `in`-operaation avulla:

```python
>>> 'java' in 'javascript'
True
>>> 'ham' in 'hamster'
True
```

### Syötteiden lukeminen

```python
>>> nimi = input('Mikä on nimesi? ')
```


### Lukujen tyyppimuunnokset ja pyöristäminen

Merkkijonoja voidaan muuttaa eri lukutyypeiksi, ja lukutyyppejä voidaan muuttaa toisiksi `int`- ja `float`-funktioilla:

```python
kymmenen = int('10')

ika = int(input('Kerro ikäsi: '))
```

```python
pii = float('3.14')

hinta = float(input('Syötä pizzan hinta: '))
```

Pyöristäminen onnistuu `round`-funktiolla, jolle voidaan myös kertoa, kuinka monen desimaalin tarkkuudella pyöristys halutaan tehdä:

```python
>>> round(3.14)
3
>>> round(3.14, 1)
3.1
```

Luvut voidaan muuttaa merkkijonoiksi `str`-funktiolla:

```python
>>> hinta = 9.90
>>> print("Hinta: " + str(hinta))
Hinta: 9.9
```

Sama koodi ei toimisi ilman `str`-muunnosta, koska Python ei salli katenoida lukuja sekä merkkijonoja:

```python
>>> hinta = 9.90
>>> print("Hinta: " + hinta)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str
```


### import-käsky

Pythonissa sekä kielen standardikirjaston moduulit että omat ja `pip`-komennolla asennetut moduulit voidaan ottaa käyttöön `import`-käskyllä:

```python
>>> import math
>>> math.pi
3.141592653589793
>>> round(math.pi, 5)
3.14159
>>> math.floor(math.pi)
3
>>> math.ceil(math.pi)
4
```

Yksittäisiä funktioita, arvoja tai luokkia voidaan ottaa käyttöön syntaksilla `from moduuli import asia`:

```python
>>> from math import log2
>>> log2(50_000)
15.609640474436812
```

**Bonus**: Kokeile myös seuraavia:

```python
import __hello__
import antigravity
import this
```

### Totuusarvot ja vertailuoperaatiot

https://www.pythoncheatsheet.org/#Flow-Control

Pythonissa on kaksi totuusarvoa:

```python
tosi = True
epatosi = False
```

Lisäksi kaikki muut arvot voidaan esittää totuusarvoina `bool`-funktion avulla. Pääsääntöisesti kaikki nollaa vastaavat sekä tyhjät arvot ovat epätosia, kun taas muut arvot ovat tosia:

```python
>>> bool(0)
False
>>> bool(100)
True
>>> bool('')
False
>>> bool('hello')
True
>>> bool('False') # kaikki ei-tyhjät merkkijonot ovat tosia!
True
>>> bool('0')     # kaikki ei-tyhjät merkkijonot ovat tosia!
True
```

Vertailuoperaatiot ovat samat kuin muissa kielissä:

```python
1 < 2
4 > 2
1 != 2
1 == 1
```

Monista muista kielistä poiketen merkkijonojen vertailu onnistuu sekä `==` että `<` ja `>`-operaattoreilla!

```python
>>> "a" < "b"
True
>>> "teksti" == "teksti"
True
```

Totuusarvojen yhdistäminen ja negaatio toimivat `and`, `or`, `is` ja `not` -operaatioilla.

### Ehtorakenteet

Pythonin if-else -rakenne on hyvin samankaltainen kuin muissa kielissä:

```python
kaupunki = 'Helsinki'
vakiluku = 648_553

if vakiluku > 500_000:
    print(f'{kaupunki} on iso kaupunki')
else:
    print(f'{kaupunki} on pieni kaupunki')
```

Tehdessäsi pitkiä ehtorakenteita, huomaa, että `else if` on Pythonissa `elif`.


### Toistorakenteet

Pythonin `while`-toistorakenne sekä `break`- ja `continue`-komennot toimivat kuten monissa muissakin kielissä:

```python
while True:
    vastaus = input('Mikä komento lopettaa toiston? ')
    if vastaus == 'break':
        print('Oikein!')
        break
    else:
        print('Väärin...')
```

`for`-toistorakennetta puolestaan käytetään pääsääntöisesti *for-each*-tyyliseen arvojen läpikäyntiin:

```python
kaupungit = ["HELSINKI", "ESPOO", "VANTAA"]

for kaupunki in kaupungit:
    print(kaupunki.title())
```

Jos tarkoituksena on käydä läpi kokonaislukuja (vrt. `for (int i=0; i < raja; i++)`), toteutetaan se tyypillisesti arvojen läpikäyntinä `range`-funktion avulla:

```python
>>> for luku in range(5, 10):
...     print(luku)
... 
5
6
7
8
9
```


### Listat

Listan luominen, arvojen lisääminen, poistaminen sekä listojen yhdistäminen:

```python
kaupungit = ["Helsinki", "Espoo", "Vantaa"]

# append lisää loppuun
kaupungit.append("Kauniainen")

# insert lisää annettuun indeksiin
kaupungit.insert(0, "Turku")

# del poistaa listalta
del kaupungit[0]

# extend lisää annetun listan arvot
kaupungit.extend(["Lahti", "Tampere"])

# + yhdistää, mutta ei muuta alkuperäistä listaa
yhdistetty = kaupungit + ["Oulu", "Rovaniemi"]
```

Listan arvojen hakeminen toimii täsmälleen kuten merkkijonojen tapauksessa:

```python
>>> kaupungit[0]    # Yksittäinen arvo
'Turku'
>>> kaupungit[0:2]  # Arvot väliltä [0, 2[
['Turku', 'Helsinki']
>>> kaupungit[-2:]  # Arvot lopusta alkaen toiseksi viimeisestä
['Lahti', 'Tampere']
```

Arvojen etsiminen listalta tapahtuu `in`-operaatiolla:

```python
"Helsinki" in kaupungit # True
```

Listoille on lisäksi erilaisia operaatioita, kuten järjestäminen:

```python
kaupungit = ['Vantaa', 'Helsinki', 'Espoo']
kaupungit.sort()
kaupungit # ['Espoo', 'Helsinki', 'Vantaa']
```

**Edistynyt esimerkki:** erilaisia listoja voidaan luoda kätevästi "list comprehension"-syntaksilla:

```python
isolla = [k.upper() for k in kaupungit]
isolla # ['HELSINKI', 'ESPOO', 'VANTAA']
```

### Monikot (tuple)

Listojen lisäksi pythonissa on kiinteäpituuksinen kokoelma **monikko**, eli **tuple**:

```python
monikko = ('monta', 'arvoa')
```

Monikkoja, kuten listoja, voidaan purkaa kätevästi muuttujiin sijoitusoperaatiolla:

```python
numerot = (1, 2, 3, 4)

yksi, kaksi, kolme, nelja = numerot
```

Monikoita käytetään "pellin alla" monissa tilanteissa, kuten esimerkiksi sanakirjarakenteen avain-arvo-parien läpikäynnissä.


### Sanakirjat (dict)

Pythonin sanakirjarakenne muistuttaa monilla tavoilla JSON-tietorakenteita, JavaScript-kielen objekteja sekä Javan map-tietorakenteita. Ne ovat siis kokoelmia avain-arvo-pareja:

```python
vakiluvut = {
    'Helsinki': 648553,
    'Espoo': 285018,
    'Vantaa': 229593
}
```

Arvojen hakeminen, lisääminen ja korvaaminen toimivat kuten JavaScriptissä:

```python
>>> # Arvon hakeminen:
>>> vakiluvut['Helsinki']
648553
>>> 
>>> # Arvon lisääminen:
>>> vakiluvut['Turku'] = 186_756
>>>
>>> # Arvon asettaminen (ja hakeminen):
>>> vakiluvut['Helsinki'] = vakiluvut['Helsinki'] + 1
```

Sanakirjan avaimet ja arvot omina kokoelminaan:

```python
>>> vakiluvut.keys()
dict_keys(['Helsinki', 'Espoo', 'Vantaa', 'Turku'])
>>>
>>> vakiluvut.values()
dict_values([648554, 285018, 229593, 186756])
```

Jos haluat selvittää, löytyykö tiettyä avainta tai arvoa sanakirjasta, voit käyttää `in`-operaatiota:

```python
>>> 'Helsinki' in vakiluvut
True
>>>
>>> # in tarkistaa vain avaimista:
>>> 648554 in vakiluvut
False
>>> 
>>> # voit tehdä tarkistuksen myös suoraan sanakirjan arvoihin
>>> 648554 in vakiluvut.values()
True

```

Sanakirjan avaimia ja arvoja voidaan käsitellä myös pareina (monikkoina):

```python
>>> vakiluvut.items()
dict_items([('Helsinki', 648554), ('Espoo', 285018), ('Vantaa', 229593), ('Turku', 186756)])
```

Sanakirjan avaimet voidaan käydä läpi yksinkertaisella `for`-toistorakenteella:

```python
>>> for avain in vakiluvut:
...     print(avain)
... 
Helsinki
Espoo
Vantaa
Turku
```

Jos toistossa halutaan käsitellä sekä avaimia että arvoja, kannattaa ne käydä läpi pareina (ks. yllä items() sekä monikot):

```python
>>> for nimi, luku in vakiluvut.items():
...     print(f'{nimi} ({luku})')
... 
Helsinki (648554)
Espoo (285018)
Vantaa (229593)
Turku (186756)
```

### Funktiot

Pythonin funktiot muistuttavat hyvin suuresti esim. JavaScriptin funktioita. Parametrien ja paluuarvojen välitys tapahtuu samalla tavoin, ainoastaan syntaksissa on pieniä eroja:

```python
def laske_summa(lista_numeroista):
    summa = 0
    for n in lista_numeroista:
        summa += n
    return summa
```

Pythonista löytyy **paljon** perusoperaatioita myös valmiina, eli oman `laske_summa`-funktion sijaan voimme kutsua Pythonin valmista `sum`-funktiota.


### Muita hyödyllisiä komentoja

**help** -funktio näyttää ohjeita sille annetun arvon tai funktion käyttämiseksi:

    >>> help(print)
    Help on built-in function print in module builtins:

    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.

**type** -funktio kertoo sille annetun arvon tyypin:

    >>> type(mysteerimuuttuja)
    <class 'list'>

**dir** -funktio kertoo moduulin sisältämät arvot, funktiot ja luokat:

    >>> import math
    >>> dir(math)
    ['__doc__', '__loader__', '__name__', '__package__', 
    '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 
    'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 
    'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 
    'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
    'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 
    'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 
    'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 
    'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 
    'trunc']


### Luokat ja oliot

Emme hyödynnä tällä kurssilla luokkia ja olioita, mutta voit tutustua itsenäisesti Pythonin olio-ohjelmointipuoleen.

## "Python as a swiss army knife"

Seuraavissa esimerkeissä käytämme `curl`-komentoa, jonka voit asentaa Ubuntussa seuraavasti: `sudo apt install curl`. Lisätietoja komennosta löydät [Ubuntun manuaalista](https://manpages.ubuntu.com/manpages/focal/man1/curl.1.html).

```bash
$ curl https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json
```

### JSON-työkalu: **json.tool**

Python 3:ssa on mukana `json.tool`-niminen moduuli, jonka avulla voidaan mm. muotoilla JSON-tietorakenteita helpommin luettavaan muotoon.

Kokeillaan seuraavaksi putkittaa curl-komennon tulostama sisentämätön JSON-tietorakenne `json.tool`-työkalulle:

```bash
$ curl https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json | python3 -m json.tool
```

Sama voidaan tehdä myös tiedostolle (ensimmäinen komento lataa tiedoston paikalliseen hakemistoon):

```
$ curl https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json > postinumerot.json
$ cat postinumerot.json | python3 -m json.tool
```

Data saadaan ladattua, muotoiltua ja tallennettua myös yhdellä rivillä:

```
$ curl https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json | python3 -m json.tool > postinumerot.json
```

https://docs.python.org/3/library/json.html#json-commandline

### HTTP-palvelin: **http.server**

```
python3 -m http.server
```

https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server


### Venv (Virtual environments)

Tällä kurssilla emme käytä Pythonin virtuaalisia ympäristöjä, koska kaikki harjoitukset ja esimerkit tehdään lähtökohtaisesti virtualisoimalla koko käyttöjärjestelmä. Jos sinulla on tarpeen kehittää samalla käyttöjärjestelmällä useita toisistaan riippumattomia Python-projekteja, näiden erittely omiksi ympäristöikseen `venv`-työkalulla on tedennäköisesti kannattavaa: https://docs.python.org/3/tutorial/venv.html


### Muut kurssilla myöhemmin käytettävät työkalut

* Pytest
* cProfile
* coverage

## Python as a programming language

Python on monen paradigman kieli. Tunnilla tutustumme Python-kehitykseen hyödyntäen VS Codea sekä muita ohjelmistokehityksen työkaluja.

Tutustu tarvittaessa itsenäisesti kurssin videotallenteisiin tämän osion tiimoilta.


# Koodaustehtävä

Tämän koodaustehtävän tavoitteena on luoda pohja seuraavien viikkojen tehtäville, joissa käsittelemme dataa ja testaamme ohjelmistoja Python-kielellä. Kaikkien mahdollisten Pythonin rakenteiden opetteleminen etukäteen ei ole kurssin kannalta tarkoituksenmukaista, mutta tehtäväksi on valittu sellainen, jonka kautta opimme soveltamaan Pythonin perusrakenteita.

Tehtävät saa ratkaista yhteistyössä kaverin kanssa, mutta molempien on osallistuttava aktiivisesti ongelmien ratkaisemiseen ja koodattava sekä palautettava omat ratkaisunsa. Tehtävien toimintalogiikan ja käyttöliittymän ei tarvitse noudattaa täsmällisesti annettuja esimerkkejä, mutta toimintalogiikan tulee olla samankaltainen.

Tehtävien tausta-aineistona käytämme GitHubissa julkaistua postinumeroaineistoa, jonka tarkemmat ohjeet käsitellään seuraavaksi.

## Postinumeroaineisto

GitHubista löytyy valmis projekti https://github.com/theikkila/postinumerot, jonka avulla voidaan hakea Postin tietokannasta kaikki postinumerotiedot. Projektissa on myös mukana valmiiksi koostettuja JSON-tiedostoja postinumeroista. 

Tässä tehtävässä sinun tulee käyttää postinumerotiedostoa [postcode_map_light.json](https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json), joka sisältää JSON-olion, jossa postinumerot ovat avaimia ja postitoimipaikat arvoja, esimerkiksi:

```json
{
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}
```

JSON-muotoisen merkkijonon parsiminen Pythonin tietorakenteiksi onnistuu standardikirjaston `json`-kirjastolla: https://docs.python.org/3/library/json.html:

```python
>>> import json
>>>
>>> json.loads("""{
...     "74701": "KIURUVESI",
...     "35540": "JUUPAJOKI",
...     "74700": "KIURUVESI",
...     "73460": "MUURUVESI"
... }""")
{'74701': 'KIURUVESI', '35540': 'JUUPAJOKI', '74700': 'KIURUVESI', '73460': 'MUURUVESI'}
>>>
```

> *"Data on postin ja sitä koskee kaikki http://www.posti.fi/liitteet-yrityksille/ehdot/postinumeropalvelut-palvelukuvaus-ja-kayttoehdot.pdf dokumentin käyttöehdot."*
>
> *"JSON-muunnokset ovat vapaasti käytettävissä ja muunneltavissa."*
>
> Lähde: https://github.com/theikkila/postinumerot

## Tehtävän arviointi

Hyväksyttyyn suoritukseen sinun ei tarvitse toteuttaa kumpaakaan tehtävää täydellisesti. Palauta siis ohjelmat siinä kunnossa mihin saat ne toteutettua. Arviointi skaalataan suuntaa-antavasti siten, että ensimmäisen tehtävän ratkaisulla saat arvosanan 3 ja **molemmat tehtävät** ratkaisemalla arvosanan 5.


## Osa 1 (arvosanatavoite 3)

Kirjoita Python-kielinen ohjelma `postitoimipaikka.py`, joka kysyy  käyttäjältä postinumeron ja kertoo, mihin postitoimipaikkaan kyseinen postinumero kuuluu. 

Tehtävän ratkaisemiseksi sinun tulee kysyä käyttäjältä syötettä ja etsiä postinumeroaineistosta syötettä vastaava arvo. Voit joko tallentaa postinumeroaineiston koneellesi ja [lukea sen levyltä](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) tai toteuttaa ohjelmasi [lukemaan tiedoston suoraan verkosta](https://docs.python.org/3/howto/urllib2.html).

Esimerkkisuoritus:

    $ python3 postitoimipaikka.py
    
    Kirjoita postinumero: 00100
    HELSINKI

## Osa 2 (arvosanatavoite 5)

Kirjoita Python-kielinen ohjelma `postinumerot.py`, joka kysyy käyttäjältä postitoimipaikan nimen, ja listaa kaikki kyseisen postitoimipaikan postinumerot.

Tehtävän voi ratkaista useilla tavoilla, joten käytä hetki ongelman pohtimiseen ennen kuin ryhdyt koodaamaan. Olisiko esimerkiksi helpompaa jäsentää postinumeroaineisto etukäteen uudenlaiseksi tietorakenteeksi, vai käydä avain-arvo-pareja läpi yksi kerrallaan postinumeroiden löytämiseksi. Seuraavalla viikolla käsittelemme hieman lähemmin tietorakenteiden ja algoritmien suunnittelua ja tehokkuutta.

Esimerkkisuoritus:

    $ python3 postinumerot.py

    Kirjoita postitoimipaikka: Porvoo
    Postinumerot: 06100, 06401, 06151, 06150, 06101, 06500, 06450, 06400, 06200

Yritä toteuttaa ohjelma siten, että syötetyn postitoimipaikan kirjainkoolla ei ole merkitystä. Huolehdi myös siitä, että tuntemattoman nimen syöttäminen ei kaada ohjelmaa.


## Lähteitä

Pythonin dict-tietorakenne, eli sanakirja, muistuttaa Javan map-tietorakennetta. Tulet tarvitsemaan sanakirjaa tausta-aineiston käsittelemisessä: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Tiedoston lataaminen verkosta onnistuu esim Python 3: standardikirjastoon kuuluvalla `urllib`-kirjastolla: https://docs.python.org/3/howto/urllib2.html.

JSON-muotoisen merkkijonon parsiminen Pythonin listoiksi, sanakirjoiksi ja muiksi tietorakenteiksi onnistuu standardikirjaston `json`-kirjastolla: https://docs.python.org/3/library/json.html


## Tehtävien palauttaminen

Palauta koodaamasi lähdekooditiedostot sellaisenaan, eli **ei pakattuna** Teamsissa olevaan palautuslaatikkoon **Teams-tehtävässä ilmoitettuun määräaikaan mennessä**.


## Seminaariaiheita

Python-aiheiset seminaarityöt voivat käsitellä esimerkiksi Pythonin [Django](https://www.djangoproject.com/)- tai [Flask](https://flask.palletsprojects.com/)-sovelluskehysten käyttöönottoa tai Pythonin tietokantaohjelmointiin perehtymistä.