## Suositeltavat ennakkovideot

Software Testing Explained: How QA is Done Today, https://www.youtube.com/watch?v=oLc9gVM8FBM


What is Automated Testing?
 https://www.youtube.com/watch?v=Nd31XiSGJLw



## Oppitunnin tavoitteet

Oppitunnin tavoitteena on oppia erityisesti yksikkötestauksen käsitteet, mutta sovellamme pytest-moduulia myös ohjelmamme ja rajapinnan integraation testaamiseen. 

Ohjelman rakenteesta riippuen sen testaaminen voi olla hyvin hankalaa. Ulkoiset riippuvuudet, kuten riippuvuus API-rajapinnasta, vaikuttavat testien tuloksiin, joten testattavan aineiston muuttuessa myös testien tulokset voivat muuttua.

## Oppitunnin sisältö

Tällä oppitunnilla kokeilemme testausta eri tasoilla hyödyntäen Pythonin `pytest`-moduulia. Testattava ohjelmisto on aikaisemmalta viikolta tuttu ohjelma, joka hakee Helsingin kaupungin REST-rajapinnasta tapahtumat ja näyttää ne käyttäjälle kronologisessa järjestyksessä.

Voit asentaa pytest-moduulin itsellesi komennolla:

`pip install pytest`

Pytest-moduulia voidaan käyttää joko järjestelmän luoneella `pytest`-komennolla tai `python`-komennon kautta valitsemalla `-m` -vivulla moduuliksi `pytest`. Voit varmistaa asennuksen toimivuuden esimerkiksi seuraavasti:

```
$ python3 -m pytest
======== test session starts =========
collected 0 items

======= no tests ran in 0.12s ========
```

Tässä tapauksessa `pytest` etsi testitiedostoja, mutta koska niitä ei löytynyt, ei suorittanut vielä yhtään testiä.

## Testauksen tasot

Testauksen käsitteistöön kuuluu oleellisena osana eri tasot, joilla erityisesti automatisoitua testausta suoritetaan. Jyväskylän Yliopiston Informaatioteknologian tiedekunnan materiaali kuvaa testauksen tasot selkeänä kokonaisuutena, johon voit tutustua osoitteessa
http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot.


### Yksikkötestaus

> "Yksikkötestauksella tarkoitetaan pienimmän mahdollisen ohjelman osan, esimerkiksi aliohjelman, toiminnan testaamista. Yksikkötesteillä varmistetaan, että ohjelman pienimmät osat toimivat odotetulla tavalla, ja että mahdolliset virhetilanteet on niiden osalta ennakoitu."
>
> "Yksikkötestauksen hyödyt näkyvät kehitysprosessin aikana erityisesti silloin, kun jo kirjoitettuun koodiin joudutaan tekemään muutoksia. Automatisoiduilla yksikkötesteillä voidaan nopeasti todeta, aiheuttavatko tehdyt muutokset virheitä."
>
> *Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. [Testauksen tasot](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot)*

Katsotaan ensimmäiseksi lajittelualgoritmitehtävän malliratkaisussa olevaa funktiota, joka vaihtaa listalta kahdessa indeksissä olevat alkiot keskenään:

```python
def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
```

Tätä funktiota voitaisiin testata esimerkiksi seuraavalla koodilla:

```python
# tiedosto test_events_by_date.py

import events_by_date

# kaikki testitapaukset alkavat test_ -etuliitteellä:
def test_swap_first_and_last():
    # alustus:
    my_list = ['this', 'is', 'sample', 'data']

    # testattava operaatio:
    events_by_date.swap(my_list, 0, 3)

    # assertio, eli tuloksen varmistaminen:
    assert my_list == ['data', 'is', 'sample', 'this']
```

Tämä testi luo ensin listan merkkijonoista, minkä jälkeen se yrittää vaihtaa kahden merkkijonon paikkoja. Lopuksi testi hyödyntää `assert` -komentoa varmistaakseen, että lopputulos vastaa odotuksia.

Assert-komento toimii hyvin yksinkertaisesti siten, että jos sen jälkeen on epätosi arvo, aiheutuu `AssertionError`, jonka `pytest` tulkitsee epäonnistuneeksi testiksi:

```
>>> assert 1 < 3 # True, ei aiheuta poikkeusta:
>>> 
>>> assert 1 > 3 # False, aiheuttaa poikkeuksen:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

Testi voidaan suorittaa `pytest`-moduulilla, joka etsii `test_`-alkuiset tiedostot ja funktiot ja suorittaa ne:

```
$ python3 -m pytest
======== test session starts =========
collected 1 item

src\test_events_by_date.py .      [100%]

========= 1 passed in 0.06s ==========
```

#### Testidata eli "fixturet"

Testien kirjoittamisen ja onnistumisen kannalta testattava data on avainasemassa. Jos testattava data vaihtelee, myös testien tulokset vaihtelevat. On myös tärkeää käyttää sellaista dataa, joka vastaa riittävän kattavasti oikeassa datassa kohdattavia vaihteluita.

Tapahtumien osalta vaihtelua aiheuttavat ainakin tapahtumat, joilla ei ole tunnettua suomenkielistä nimeä eikä alkupäivämäärää. Tällaisen tapahtuman toimivuutta ohjelmassa voitaisiin testata esimerkiksi seuraavanlaisella tietorakenteella:

```python
UNKNOWN_EVENT = {
    "name": {
        "fi": None,
        "en": "Event with no date"
    },
    "event_dates": {
        "starting_day": None
    }
}
```

Lisäksi voimme luoda esimerkiksi vuoden ensimmäisenä päivänä ja jouluaattona tapahtuvat tapahtumat testiaineistoomme:

```python
JANUARY_1ST_EVENT = {
    "name": {
        "fi": None,
        "en": "January first"
    },
    "event_dates": {
        "starting_day": '2022-01-01T12:00:00Z'
    }
}

CHRISTMAS_EVENT = {
    "name": {
        "fi": "Joulu",
        "en": "Christmas"
    },
    "event_dates": {
        "starting_day": '2022-12-24T12:00:00Z'
    }
}
```

Näillä tapahtumilla voimme jo luoda listan, jossa kaikki tapahtumat ovat väärissä paikoissa. Tämän listan voimme puolestaan antaa toteuttamallemme `bubble_sort`-funktiolle, minkä jälkeen listan tulee olla tunnetussa oikeassa järjestyksessä:

```python
def test_bubble_sort_with_three_events():
    # Testiaineisto: lista väärässä järjestyksessä
    events = [CHRISTMAS_EVENT, UNKNOWN_EVENT, JANUARY_1ST_EVENT]

    events_by_date.bubble_sort(events)

    assert events == [UNKNOWN_EVENT, JANUARY_1ST_EVENT, CHRISTMAS_EVENT]
```

Tietokantapohjaisessa ohjelmistossa sama ennalta määrätty testidata syötetään tyypillisesti tietokantaan ennen jokaista testiä.

#### Test driven development

Aikaisemman viikon malliratkaisussa on havaittu bugi, joka on raportoitu GitHubiin issuena. Bugin seurauksena kaikkien tapahtumien ajankohdat on ilmoitettu UTC-ajassa, eli ne eivät vastaa Suomen paikallisia aikoja.

Tämä on kiusallinen ongelma, joka korjataan seuraavaksi.

`pip install python-dateutil`

#### Miten testata koodia, jonka tulos vaihtelee?

Ohjelmakoodiin toteuttamamme `get_events_by_date` on riippuvainen toisesta funktiosta nimeltä `get_events`, joka tekee REST-kutsun ja parsii vastauksena saadun JSON-olion listaksi sanakirjoja. Koska eri ajankohtina REST-rajapinnasta saadaan eri vastauksia, on tuloksen oikeellisuus vaikea varmistaa. Oikea pyyntö REST-palveluun voi myös viedä tarpeettoman paljon aikaa, joten sitä ei haluta tehdä yksikkötestissä.

Yksikkötesteissä korvataan usein riippuvuuksia mock'eilla, joiden avulla saadaan rajattua testi vain tiettyyn osaan koodista, vaikka testattavalla koodinpätkällä olisikin riippuvuuksia. Riippuvuudet voivat olla niin ulkoisiin rajapintoihin kuin vaikka kellonaikoihin liittyviä.

Käyttämämme Pytest-moduulin `pytest-mock`-laajennus voidaan asentaa seuraavasti:

`pip install pytest-mock`

Pystest-mock (https://pypi.org/project/pytest-mock/) lisää testeihin käytettäväksi `mocker`-olion, joka saadaan injektoitua testifunktioon kirjoittamalla testin parametrimuuttujiin `mocker`:

```python
# dependency injection huolehtii `mocker`-olion injektoimisesta:
def test_get_events_by_date_with_mock(mocker):
    pass
```

Näin Pytest tietää kutsua tätä testifunktiota aina mocker-olion kanssa. Kun mocker on injektoitu, sen avulla voidaan korvata esimerkiksi funktioita uusilla funktioilla, jotka palauttavat aina haluamamme ennalta määrätyn arvon:

```python
# Asetetaan get_events palauttamaan aina sama lista:
mocker.patch('events_by_date.get_events', return_value=palauta_aina_tama_lista)
```

Mocker-olio ja injektointi huolehtivat siitä, että funktiota ei korvata pysyvästi, vaan kyseisen testin suorittamisen jälkeen `get_events` on taas ennallaan. `get_events_by_date` voidaan siis testata korvaamalla sen riippuvuus staattisella paluuarvolla, jonka tuloksen tiedämme ennalta:

```python
# dependency injection huolehtii `mocker`-olion injektoimisesta:
def test_get_events_by_date_with_mock(mocker):

    # Tapahtumat epäjärjestyksessä:
    mock_response = [CHRISTMAS_EVENT, UNKNOWN_EVENT, JANUARY_1ST_EVENT]

    # Asetetaan get_events palauttamaan yllä oleva lista tapahtumista:
    mocker.patch('events_by_date.get_events', return_value=mock_response)

    # get_events_by_date kutsuu sisäisesti get_events-funktiota, joka palauttaa mock-vastauksen!
    result = events_by_date.get_events_by_date()

    # get_events_by_date on nyt palauttanut tunnetut tapahtumat oikeassa järjestyksessä:
    assert result == [UNKNOWN_EVENT, JANUARY_1ST_EVENT, CHRISTMAS_EVENT]
```


### Integraatiotestaus

> "Integraatiotestauksessa testataan useiden komponenttien yhteistoimintaa tavoitteena löytää virheitä, jotka eivät tulleet esiin yksikkötesteissä. Testeissä suoritetaan tiettyjä suorituspolkuja, jotka hyödyntävät useita eri yksiköitä tai laajempia komponentteja, ja tarkastellaan toiminnan tuloksia."
>
> *Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. [Testauksen tasot](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot)*



```python
# Tämä testifunktio kutsuu API:a ja lajittelee tapahtumat oikeasti. Se voi olla siis hyvin hidas.
def test_get_events_by_date_with_real_api_call():

    # Nyt rajapintaa kutsutaan oikeasti ja oikeat tapahtumat lajitellaan:
    result = events_by_date.get_events_by_date()

    # Testi edellyttää rajapinnalta aina vähintään 100 tapahtumaa, vaikka oikea määrä on tuntematon:
    assert len(result) > 10

    # Vertaillaan että alkamisaika on joko None tai peräkkäiset ovat oikeassa järjestyksessä:
    for i in range(len(result) - 1):
        assert result[i]['event_dates']['starting_day'] == None or result[i]['event_dates']['starting_day'] < result[i + 1]['event_dates']['starting_day']
```


### Järjestelmätestaus

> "Järjestelmätestauksessa testataan kokonaista ohjelmaa, ja tarkastellaan vastaako ohjelma sille asetettuja vaatimuksia ja käyttötarkoitusta.  Aitoon ympäristöön kuuluvat mm. käytettävä laitteisto, tietokannat ja käyttäjät."
>
> *Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. [Testauksen tasot](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot)*


<!--
## Testaus Pythonilla

* doctest
* pytest
* unittest
* VS Code


* `pip install pytest`
* `pip install python-dateutil`

## Mock

`pip install pytest-mock`

https://pypi.org/project/pytest-mock/

## Capture

https://docs.pytest.org/en/stable/capture.html

## Dateutil parser

https://dateutil.readthedocs.io/en/stable/parser.html


## Datetime

https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone

```python
from dateutil import tz, parser
```

```python
def str_to_datetime(dt_str):
    dt = parser.isoparse(dt_str)
    hki_timezone = tz.gettz('Europe/Helsinki')
    return dt.astimezone(hki_timezone)
```

## Pytest

1. tiedostonimi test_foo.py
1. testifunktio
1. `assert`-komento



## `pytest` ja `pytest-mock`

## Mock

## Fixture

## Capture

# Kotitehtävä

-->