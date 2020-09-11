# events_by_date-tehtävän malliratkaisu

Tässä malliratkaisussa käsitellään koodin profilointia sekä automatisoitua testausta, joita ei oppitunnilla käsitelty ja joita ei odotettu tai toivottu huomioitavan vielä omissa tehtäväpalautuksissa. 

> Kirjoita Python-skripti `events_by_date.py`, joka hakee events-rajapinnasta kaikki tapahtumat. Järjestä tapahtumat järjestykseen alkamisaikansa mukaan itse toteuttamallasi vapaasti valittavalla järjestämisalgoritmilla. Koodisi tulee järjestellä kokonaisia tapahtumatietueita, eli et saa poimia aineistosta järjesteltäväksi esimerkiksi pelkkiä nimiä ja alkamisaikoja.

Malliratkaisussa järjestelyalgoritmiksi valittiin toteutukseltaan yksinkertainen [kuplalajittelu eli "bubble sort"](https://en.wikipedia.org/wiki/Bubble_sort). Kuplalajittelussa aineistoa käydään toistuvasti läpi alusta loppuun, vaihtaen kahden peräkkäisen epäjärjestyksessä olevan alkion paikkoja, kunnes tulee ensimmäinen kierros, jolla yhtään vaihtoa ei tehdä:

```python
def bubble_sort(events):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(events) - 1):
            if get_start_time(events[i]) > get_start_time(events[i+1]):
                swapped = True
                swap(events, i, i+1)
```

Tässä koodissa kahden peräkkäisen tapahtuman alkamisaikoja vertaillaan `get_start_time`-nimisen funktion avulla, joka palauttaa annetun tapahtuman alkamisajan merkkijonona. Varsinainen järjestys perustuu siis tavallaan päivämäärien "aakkosjärjestykseen". Tehtävässä annettiin vapaus valita miten toimitaan päivämäärättömien tapahtumien kanssa. Tässä toteutuksessa päivämäärättömille tapahtumille palautetaan alkuajaksi tyhjä merkkijono, jolloin ne asettuvat merkkijonojen vertailussa ennen päivämäärällisiä tapahtumia:

```python
def get_start_time(event):
    return event['event_dates']['starting_day'] or ''
```

Varsinainen kahden epäjärjestyksessä olevan alkion vaihtaminen keskenään on toteutettu `swap`-nimisellä funktiolla, joka vaihtaa kahdessa indeksissä olevat alkiot keskenään. Python tarjoaa tähän varsin kätevän syntaksin:

```python
def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]
```

Tapahtumien hakeminen REST-rajapinnasta on toteutettu `urllib.request.urlopen`-funktion avulla siten, että rajapinnan osoite on asetettu moduulitasolle omaan muuttujaansa.

```python
EVENTS_API_URL = 'http://open-api.myhelsinki.fi/v1/events/'

# ...

def get_events():
    with urllib.request.urlopen(EVENTS_API_URL) as response:
        json_response = json.load(response)
        return json_response['data']  # 'data' on lista tapahtumista
```

Tapahtumien hakeminen ja järjestäminen on puolestaan toteutettu erilliseen funktioon, jolloin sekä hakemista että järjestämistä voidaan tehdä toisistaan riippumatta.

```python
def get_sorted_events():
    all_events = get_events()
    bubble_sort(all_events)
    return all_events
```

Tapahtumien tulostaminen tapahtuu `main`-funktiossa, jossa ensin haetaan järjestetyt tapahtumat, jonka jälkeen ne käydään läpi toistorakenteella:

```python
def main():
    events = get_sorted_events()

    latest_date = ''

    for event in events:
        # esim. '2022-01-01T12:00:00Z' tai ''
        event_start = get_start_time(event)

        date = event_start[:10]     # '2022-01-01' tai ''
        time = event_start[11:16]   # '12:00' tai ''
        name = get_name(event)

        if date != latest_date:
            print()
            print(date)  # tulostetaan uusi päivämäärä
            latest_date = date

        print(f' { time } { name }')
```

Yllä olevassa koodissa `latest_date` pitää muistissa merkkijonoa, joka vastaa viimeisimmän tulostetun tapahtuman päivämäärää, esim. `'2022-01-01'`. Kun läpikäytävän päivän päivämäärä ei vastaa viimeisimmän tulostetun päivämäärää (`date != latest_date`), tulostetaan taas uusi päivämäärä. Jokaisen tapahtuman kohdalla tulostetaan alkamisajankohdan kellonaika ja tapahtuman nimi:

```python
name = get_name(event)
# ...
print(f' { time } { name }')
```

Tapahtuman nimi saadaan apufunktion avulla, joka ottaa tapahtuman tietorakenteesta suomen- tai englanninkielisen nimen, tai tyhjän merkkijonon, jos kumpaakaan ei ole määritetty:

```python
def get_name(event):
    return (event['name']['fi'] or event['name']['en'] or '').strip()
```

Lopuksi ohjelman tuloste on kutakuinkin seuraava:

```
2021-06-21
 15:30 Kiss

2021-06-25
 14:00 Seurasaaren juhannusvalkeat 2021

2021-06-30
 21:01 Craft Beer Helsinki 2021
 21:01 Helsinki Chamber Music Festival 2021

2021-07-01
 21:01 Tuska Festival 2021

2021-07-16
 14:00 Sunrise Avenue
 14:00 Sunrise Avenue

2021-07-17
 14:00 Sunrise Avenue

2021-07-23
 21:01 Odysseus-festivaali 2021

2021-07-29
 21:01 Magnesia Festival 2021

2021-08-05
 21:01 Weekend Festival 2021

2021-08-13
 07:00 Flow Festival 2021

2021-08-18
 21:01 Taiteiden yö 2021
 21:01 Helsingin juhlaviikot 2021
...
```

## Tunnetut bugit

Ohjelman päivämäärien käsittelyssä ei ole huomioitu aikavyöhykkeitä ja tapahtumien ajankohdat esitetäänkin UTC-ajassa, eikä Suomen paikallisessa ajassa. Tähän voimme palata testaus-aiheen yhteydessä, jolloin voimme kirjoittaa yksikkötestit virheelliselle koodille.

## Pythonin valmis sort-funktio!

Tämän harjoituksen tavoitteena on kuitenkin opetella itse toteuttamaan jokin tunnettu järjestämisalgoritmi. Oikeassa ohjelmistoprojektissa käyttäisit Pythonin valmiita järjestämisfunktioita. [Pythonin listojen sort-metodia](https://docs.python.org/3/library/stdtypes.html#list.sort) voidaan käyttää minkä tahansa arvojen järjestämiseksi, kunhan metodille annetaan parametrina funktio, jota `sort` käyttää vertaillakseen listan arvoja:

```python
def get_start_time(event):
    return event['event_dates']['starting_day'] or ''

events = get_events()
events.sort(key=get_start_time)
```

Tässä siis **annamme parametrina funktion** get_start_time, jota `sort` kutsuu sisäisesti vertaillakseen listamme arvoja.

> *key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used for the entire sorting process.*
>
> https://docs.python.org/3/library/stdtypes.html#list.sort

Pythonin standardikirjaston avulla aineiston järjestäminen vie suuruusluokkaa sekunnin tuhannesosia:

```python
>>> import time
>>>
>>> events = get_events()
>>>
>>> # otetaan talteen alkuaika, järjestetään ja otetaan loppuaika:
>>> start = time.time(); events.sort(key=get_start_time); end = time.time()
>>>
>>> # Loppu- ja alkuajan erotus on välissä olleen operaation kesto:
>>> end - start
0.004011631011962891
```

## Koodi kokonaisuudessaan ja testit

Python-koodia on mahdollista dokumentoida koodiesimerkein, jotka ovat oikeaa suoritettavaa Python-koodia. Malliratkaisun pidemmässä versiossa on hyödynnetty doctest-moduulia yksittäisten funktioiden testaamiseksi esimerkkikoodien avulla. Katso lisää osoitteesta https://docs.python.org/3/library/doctest.html.

Lähdekooditiedosto löytyy erillisenä tiedostona täältä: [src/events_by_date.py](src/events_by_date.py).

```python
import urllib.request
import json

EVENTS_API_URL = 'http://open-api.myhelsinki.fi/v1/events/'

def swap(elements, i, j):
    """ Vaihtaa kahden elementin paikkaa listalla indeksien mukaan:

    >>> nimet = ['Matti', 'Teppo', 'Paula']
    >>> swap(nimet, 0, 2)
    >>> nimet
    ['Paula', 'Teppo', 'Matti']
    """
    elements[i], elements[j] = elements[j], elements[i]


def get_start_time(event):
    """ Palauttaa annetun tapahtuman aloitusajan merkkijonona, 
    tai tyhjän merkkijonon, jos tapahtumalla ei ole  aloitusaikaa.

    >>> tapahtuma = { 'event_dates': { 'starting_day': '2022-01-01T12:00:00Z' }}
    >>> get_start_time(tapahtuma)
    '2022-01-01T12:00:00Z'

    >>> tapahtuma['event_dates']['starting_day'] = None
    >>> get_start_time(tapahtuma)
    ''
    """
    return event['event_dates']['starting_day'] or ''


def get_name(event):
    """ Palauttaa annetun tapahtuman nimen suomeksi, englanniksi tai
    tyhjänä, jos kumpaakaan kieliversiota ei löydy.

    >>> tapahtuma = { 'name': { 'fi' : None, 'en': 'Christmas' }}
    >>> get_name(tapahtuma)
    'Christmas'
    >>> tapahtuma['name']['fi'] = 'Joulu'
    >>> get_name(tapahtuma)
    'Joulu'
    """
    return (event['name']['fi'] or event['name']['en'] or '').strip()


def bubble_sort(events):
    """ Järjestää annetut tapahtumat alkuajan mukaan.

    >>> joulukuu24 = { 'event_dates': { 'starting_day': '2022-12-24T12:00:00Z' }}
    >>> tammikuu1 = { 'event_dates': { 'starting_day': '2022-01-01T12:00:00Z' }}
    >>> tapahtumat = [joulukuu24, tammikuu1]
    >>> bubble_sort(tapahtumat)
    >>> tapahtumat == [tammikuu1, joulukuu24]
    True
    """

    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(events) - 1):
            if get_start_time(events[i]) > get_start_time(events[i+1]):
                swapped = True
                swap(events, i, i+1)


def get_events():
    with urllib.request.urlopen(EVENTS_API_URL) as response:
        json_response = json.load(response)
        return json_response['data']  # 'data' on lista tapahtumista


def get_sorted_events():
    all_events = get_events()
    bubble_sort(all_events)
    return all_events


def main():
    events = get_sorted_events()

    latest_date = ''

    for event in events:
        # esim. '2022-01-01T12:00:00Z' tai ''
        event_start = get_start_time(event)

        date = event_start[:10]     # '2022-01-01' tai ''
        time = event_start[11:16]   # '12:00' tai ''
        name = get_name(event)

        if date != latest_date:
            print()
            print(date)  # tulostetaan uusi päivämäärä
            latest_date = date

        print(f' { time } { name }')


if __name__ == "__main__":
    main()
```

## Lajittelualgoritmin tehokkuus

Malliratkaisuun valittu kuplalajittelu on erittäin hidas, ja koodin suorittaminen kirjoitushetkellä vei lähes minuutin. Kirjoitushetkellä rajapinnasta saatiin vastaukseksi 5&nbsp;379 tapahtumaa, mikä on kohtuullisen pieni aineisto.

Jotta ymmärtäisimme paremmin, mihin aika suorituksessa kului ja kuinka monta operaatiota ohjelma suoritti, voimme profiloida ohjelmamme suorituksen.

> *In software engineering, profiling ("program profiling", "software profiling") is a form of dynamic program analysis that measures, for example, the space (memory) or time complexity of a program, the usage of particular instructions, or the frequency and duration of function calls. Most commonly, profiling information serves to aid program optimization.*
>
> https://www.semanticscholar.org/topic/Profiling-(computer-programming)/1793

### Koodin profilointi

Pythonin [standardikirjastoon kuuluu profilointimoduuli cProfile](https://docs.python.org/3/library/profile.html). Tämä moduuli voidaan käynnistää `python3 -m cProfile` -komennolla, jonka jälkeen annetaan profiloitavan tiedoston nimi:

```
$ python3 -m cProfile -s calls events_by_date.py
```

Ylimääräinen optio `-s calls` järjestää raportin funktioittain niihin tehtyjen kutsujen määrän mukaan:

```
$ python3 -m doctest -v events_by_date.py


        63977937 function calls (63977142 primitive calls) in 47.800 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 56808006   24.439    0.000   24.439    0.000 events_by_date.py:16(get_start_time)
  7107450    1.300    0.000    1.300    0.000 events_by_date.py:5(swap)
7517/7394    0.005    0.000    0.005    0.000 {built-in method builtins.len}
     6014    1.293    0.000    1.293    0.000 {built-in method builtins.print}
     5384    0.002    0.000    0.002    0.000 {method 'strip' of 'str' objects}
...
...
```

Profiloijan raportista selviää, että `get_start_time`-funktio suoritettiin 56&nbsp;808&nbsp;006 kertaa ja `swap`-funktio 7&nbsp;107&nbsp;450 kertaa. Noin puolet ohjelman suoritusajasta kului `get_start_time`-funktiossa:


```
 56808006   24.439    0.000   24.439    0.000 events_by_date.py:16(get_start_time)
  7107450    1.300    0.000    1.300    0.000 events_by_date.py:5(swap)
```


Algoritmien teoriaosuuden perusteella tiedämme, että kuplalajittelun asymptoottinen suoritusaika on O(n<sup>2</sup>). 5&nbsp;379 tapahtuman aineistolla tämä tarkoittaisi noin 29 miljoonaa vertailuoperaatiota:

```python
>>> events = get_events()
>>> n = len(events)
>>> n # Tapahtumien määrä
5 379
>>> n**2
28 933 641
```

Profiloinnin perusteella tapahtumien alkuaika selvitettiin `get_start_time`-funktiolla 56&nbsp;808&nbsp;006 kertaa, mikä on noin kaksi kertaa enemmän kuin n<sup>2</sup>. Tämä johtuu siitä, että jokaista vertailua kohden molempien vertailtavien tapahtumien alkamisaika selvitettiin uudelleen.

Ensimmäinen ajatus koodin tehostamiseksi voisi olla alkuajan ottaminen talteen siten, että `get_start_time`-funktiota kutsuttaisiin vain kerran jokaista tapahtumaa kohden. Profiloinnin perusteella koodin suorittaminen veisi kuitenkin edelleen nykyisellä aineistolla kymmeniä sekunteja ja suuremmalla aineistolla hyvin pitkiä aikoja, joten tämä korjaus ei olisi riittävä. 


## Testit

Malliratkaisussa on hyödynnetty Pythonin standardikirjaston [doctest](https://docs.python.org/3/library/doctest.html)-moduulia yksittäisten funktioiden testaamiseksi esimerkkikoodien avulla. Katso lisää osoitteesta https://docs.python.org/3/library/doctest.html.

Testit voidaan suorittaa komennolla:

    $python3 -m doctest -v events_by_date.py

Parametri `-v` tarkoittaa, että testeistä tulostetaan ruudulle pidempi raportti:

```
Trying:
    joulukuu24 = { 'event_dates': { 'starting_day': '2022-12-24T12:00:00Z' }}
Expecting nothing
ok
Trying:
    tammikuu1 = { 'event_dates': { 'starting_day': '2022-01-01T12:00:00Z' }}
Expecting nothing
ok
Trying:
    tapahtumat = [joulukuu24, tammikuu1]
Expecting nothing
ok
Trying:
    bubble_sort(tapahtumat)
Expecting nothing
ok
Trying:
    tapahtumat == [tammikuu1, joulukuu24]
Expecting:
    True
ok
Trying:
    tapahtuma = { 'name': { 'fi' : None, 'en': 'Christmas' }}
Expecting nothing
ok
Trying:
    get_name(tapahtuma)
Expecting:
    'Christmas'
ok
Trying:
    tapahtuma['name']['fi'] = 'Joulu'
Expecting nothing
ok
Trying:
    get_name(tapahtuma)
Expecting:
    'Joulu'
ok
Trying:
    tapahtuma = { 'event_dates': { 'starting_day': '2022-01-01T12:00:00Z' }}
Expecting nothing
ok
Trying:
    get_start_time(tapahtuma)
Expecting:
    '2022-01-01T12:00:00Z'
ok
Trying:
    tapahtuma['event_dates']['starting_day'] = None
Expecting nothing
ok
Trying:
    get_start_time(tapahtuma)
Expecting:
    ''
ok
Trying:
    nimet = ['Matti', 'Teppo', 'Paula']
Expecting nothing
ok
Trying:
    swap(nimet, 0, 2)
Expecting nothing
ok
Trying:
    nimet
Expecting:
    ['Paula', 'Teppo', 'Matti']
ok
4 items had no tests:
    events_by_date
    events_by_date.get_events
    events_by_date.get_sorted_events
    events_by_date.main
4 items passed all tests:
5 tests in events_by_date.bubble_sort
4 tests in events_by_date.get_name
4 tests in events_by_date.get_start_time
3 tests in events_by_date.swap
16 tests in 8 items.
16 passed and 0 failed.
Test passed.
```

Palaamme testaukseen tarkemmin kurssin myöhemmillä viikoilla.