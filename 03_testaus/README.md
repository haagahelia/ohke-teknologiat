# Testaus

Tämän oppitunnin tavoitteena on tutustua testauksen eri tasoihin yksikkötesteistä järjestelmätesteihin ja tutustua testiautomaation käsitteistöön ja työkaluihin.

Aiheen opiskelun jälkeen osaat kirjoittaa Python-funktioillesi yksikkötestit ja tiedät mistä lähteä liikkeelle, kun sinulle tulee tarve kirjoittaa automatisoituja testejä.

## Suositeltavat ennakkovideot

### Video 1: [Software Testing Explained: How QA is Done Today](https://www.youtube.com/watch?v=oLc9gVM8FBM)

[![Software Testing Explained: How QA is Done Today](https://img.youtube.com/vi/oLc9gVM8FBM/mq3.jpg)](https://www.youtube.com/watch?v=oLc9gVM8FBM)

> Tämä video käsittelee testauksen eri tapoja ja käsitteistöä yleisellä tasolla.

### Video 2: [What is Automated Testing?](https://www.youtube.com/watch?v=Nd31XiSGJLw)

[![What is Automated Testing?](https://img.youtube.com/vi/Nd31XiSGJLw/mq3.jpg)](https://www.youtube.com/watch?v=Nd31XiSGJLw)

> *In this video we start diving into the world of quality assurance and discuss automated testing for our web and mobile applications...*


## Oppitunnin tavoitteet

Oppitunnin tavoitteena on oppia erityisesti yksikkötestauksen käsitteet, mutta sovellamme pytest-moduulia myös ohjelmamme ja REST-rajapinnan integraation testaamiseen. 

Ohjelman rakenteesta riippuen sen testaaminen voi olla hyvin hankalaa. Ulkoiset riippuvuudet, kuten riippuvuus REST-rajapinnasta, vaikuttavat testien tuloksiin, joten testattavan aineiston muuttuessa myös testien tulokset voivat muuttua.

Ulkoisten riippuvuuksien vaikutuksen minimoimiseksi testit suoritetaan usein erillisessä QA-ympäristössä (quality assurance), jossa rajapintojen vastaukset toiminta on hallittavissa. Tällä oppitunnilla meillä ei ole käytössä QA-ympäristöä, joten testaamme integraatiota Helsingin kaupungin tuotantorajapintaa vasten.


## Oppitunnin sisältö

Tällä oppitunnilla kokeilemme testausta eri tasoilla hyödyntäen Pythonin `pytest`-moduulia. Testattava ohjelmisto on aikaisemmalta viikolta tuttu ohjelma, joka hakee Helsingin kaupungin REST-rajapinnasta tapahtumat ja näyttää ne käyttäjälle järjestyksessä tapahtuman ajankohdan mukaan.

Testejä voitaisiin kirjoittaa myös muita työkaluja, kuten Pythonin unittest-moduulia, hyödyntäen. `pytest` on valittu kurssille siksi, että se ei edellytä minkään ulkoisten riippuvuuksien käyttämistä testikoodeissasi, vaan voit kirjoittaa testit kuten kirjoittaisit mitä tahansa muutakin Python-koodia.


# Testauksen tasot

Testauksen käsitteistöön kuuluu oleellisena osana eri tasot, joilla erityisesti automatisoitua testausta suoritetaan. [Jyväskylän Yliopiston Informaatioteknologian tiedekunnan testaussivusto](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot) kuvaa testauksen tasot selkeänä kokonaisuutena ja kyseisen sivuston määritelmiä noudatetaan myös tällä oppitunnilla.


## Yksikkötestaus

> *"Yksikkötestauksella tarkoitetaan **pienimmän mahdollisen ohjelman osan**, esimerkiksi aliohjelman, toiminnan testaamista. Yksikkötesteillä varmistetaan, että ohjelman pienimmät osat toimivat odotetulla tavalla, ja että mahdolliset virhetilanteet on niiden osalta ennakoitu."*
>
> *"Yksikkötestauksen hyödyt näkyvät kehitysprosessin aikana erityisesti silloin, kun jo kirjoitettuun koodiin joudutaan tekemään muutoksia. Automatisoiduilla yksikkötesteillä voidaan **nopeasti** todeta, aiheuttavatko tehdyt muutokset virheitä."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. [Testauksen tasot](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot)

Katsotaan ensimmäiseksi lajittelualgoritmitehtävän malliratkaisussa olevaa funktiota, joka vaihtaa listalta kahdessa indeksissä olevat alkiot keskenään:

```python
def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
```

Miten tätä funktiota voitaisiin testata? 

Tehdään testit ensin kokonaan ilman `pytest`-moduulia Pythonin omilla funktioilla!

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


## assert-komento

Python-kielessä on valmiina [assert-komento](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement), jolla voidaan hyvin suoraviivaisesti varmistaa että tietyn lausekkeen arvo on `True`. Mikäli arvo on epätosi, aiheuttaa komento `AssertionError`-poikkeuksen.

```python
assert len('hello') == 5 # True, ei aiheuta poikkeusta

assert len('welcome') == 5 # False, aiheuttaa poikkeuksen:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

Testeissä `assert`-komentoa käytetään hyvin yksinkertaisesti varmistamaan, että testatun koodin tulos on se mitä pitäisi. Jos koodi ei aiheuta poikkeusta, `pytest` tulkitsee testin onnistuneeksi. Jos taas koodista aiheutuu `AssertionError`, `pytest` tulkitsee testin epäonnistuneeksi:

```python
assert my_list == ['the', 'list', 'must', 'be', 'equal', 'to', 'this']
```

## Testien suorittaminen pytest-moduulilla

Testi voidaan suorittaa kutsumalla `test_swap_first_and_last`-funktiota itse, mutta testin automatisoimiseksi käytämme `pytest`-moduulia. Pytest huolehtii testitiedostojen ja niiden sisältämien testifunktioiden etsimisestä ja suorittamisesta automaattisesti. Se myös tuottaa selkokielisen raportin testien tuloksista.

Voit asentaa Pythonin pytest-moduulin itsellesi seuraavalla komennolla:

`pip3 install pytest`

Pytest-moduulia voidaan käyttää joko erillisellä `pytest`-komennolla tai `python3`-komennon kautta valitsemalla `-m` -vivulla moduuliksi `pytest`. Voit varmistaa asennuksen toimivuuden esimerkiksi seuraavasti:

```
$ python3 -m pytest
======== test session starts =========
collected 1 item

src/test_events_by_date.py .      [100%]

========= 1 passed in 0.06s ==========

# pytest voidaan käynnistää myös omalla komennollaan:

$ pytest
======== test session starts =========
collected 1 item

src/test_events_by_date.py .      [100%]

========= 1 passed in 0.06s ==========
```

`test_swap_first_and_last`-testissä vaihdoimme kahden merkkijonon paikkaa, mikä periaatteessa riittää kyseisen funktion testaamiseksi. Usein tarvitsemme kuitenkin paljon realistisempaa testidataa, jotta tiedämme, että koodi toimii esimerkiksi käyttämämme rajapinnan tapahtumia vastaavien tietorakenteiden kanssa.

## Testidata eli "fixturet"

Testien kirjoittamisen ja hyödyllisyyden kannalta testattava data on avainasemassa. Jos testattava data vaihtelee, myös testien tulokset vaihtelevat. On myös tärkeää käyttää sellaista dataa, joka vastaa riittävän kattavasti oikeassa datassa kohdattavia vaihteluita.

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

Näillä tapahtumilla voimme jo luoda listan, jossa kaikki tapahtumat ovat väärissä paikoissa, ja testata tapahtumien vaihtamisen keskenään:

```python
# uusi versio testissä, tällä kertaa vaihdetaan tapahtumia eikä merkkijonoja:
def test_swap_first_and_last():
    my_list = [CHRISTMAS_EVENT, UNKNOWN_EVENT, JANUARY_1ST_EVENT]

    events_by_date.swap(my_list, 0, 2)

    assert my_list == [JANUARY_1ST_EVENT, UNKNOWN_EVENT, CHRISTMAS_EVENT]
```

Oikeita tapahtumia vastaavalla testidatalla voimme testata myös `bubble_sort`-funktion toimintaa. Ensin luodaan testissä käytettävä lista, sen jälkeen kutsutaan testattavaa funktiota ja lopuksi varmistetaan odotettu lopputulos:

```python
def test_bubble_sort_with_three_events():
    # Testiaineisto: lista väärässä järjestyksessä
    events = [CHRISTMAS_EVENT, UNKNOWN_EVENT, JANUARY_1ST_EVENT]

    # Testattava operaatio:
    events_by_date.bubble_sort(events)

    # Tuloksen varmistaminen:
    assert events == [UNKNOWN_EVENT, JANUARY_1ST_EVENT, CHRISTMAS_EVENT]
```

Tietokantapohjaisessa ohjelmistossa sama ennalta määrätty testidata syötetään tyypillisesti tietokantaan ennen jokaista testiä, jotta jokaisen testin alussa tietokannan sisältämä tila on varmasti sama.

## Testien ajaminen VS Codessa

> *Testing in Python is disabled by default. To enable testing, use the Python: **Configure Tests** command on the Command Palette. This command prompts you to select a test framework, the folder containing tests, and the pattern used to identify test files.*
>
> Python testing in Visual Studio Code. https://code.visualstudio.com/docs/python/testing


VS Codessa on oma erillinen näkymänsä testeille. Tämän näkymän kautta testien suoritusta voidaan nopeuttaa ja tehdä vielä havainnollisemmaksi kuin komentoriviltä. Ota testausominaisuudet käyttöön seuraamalla oppituntia tai ohjeita sivulla: https://code.visualstudio.com/docs/python/testing

## Test driven development

Tietorakenteet ja algoritmit -aiheen malliratkaisussa on havaittu bugi, joka [on raportoitu GitHubiin issuena](https://github.com/haagahelia/swd4tn023/issues/1). Bugin seurauksena kaikkien tapahtumien ajankohdat on ilmoitettu UTC-ajassa, eli ne eivät vastaa Suomen paikallisia aikoja.

Tämä on kiusallinen ongelma, joka korjataan seuraavaksi.

Päivämäärien käsittelemiseksi asennamme `dateutil`-paketin, joka helpottaa aikavyöhykkeiden käyttämistä ja merkkijonomuotoisten päivämäärien parsimista:

`pip3 install python-dateutil`

Dateutil-paketin dokumentaatio löytyy osoitteesta https://dateutil.readthedocs.io/en/stable/

### Testin kirjoittaminen

Bugiraportissa todetaan elokuussa 2021 klo 10 alkavan tapahtuman kellonaikana näkyvän virheellisesti klo 7:00. Virhe johtuu siitä, että aika poimitaan ISO-muotoillusta merkkijonosta huomioimatta lainkaan aikavyöhykettä. Oikea ajankohta syötteelle `'2021-08-13T07:00:00.000Z'` olisikin 13.8.2021 **klo 10:00 Suomen aikaa**.

Tätä varten voidaan kirjoittaa testi `str_to_datetime`-funktiolle. Huomaa, että emme ole vielä toteuttaneet kyseistä testattavaa funktiota.

```python
def test_str_to_datetime_in_helsinki_timezone():
    dt = events_by_date.str_to_datetime('2021-08-13T07:00:00.000Z')

    assert dt.date() == date(2021, 8, 13)
    assert dt.time() == time(10, 0)
```

Kun tarvittava testi on kirjoitettu, voimme ryhtyä toteuttamaan itse `str_to_datetime`-funktiota. Tässä meille tulee avuksi dateutil-kirjaston `parser` ja `tz`, joilla voimme lukea ISO-merkkijonon päiväksi ja käsitellä Helsingin aikavyöhykettä:

```python
from dateutil import parser, tz

dt = parser.isoparse('2021-08-13T07:00:00.000Z') # muodostaa datetime-olion

hki_timezone = tz.gettz('Europe/Helsinki') # Helsingin aikavyöhyke
```
<!--
```python
from dateutil import parser, tz

def str_to_datetime(dt_str):
    dt = parser.isoparse(dt_str)
    hki_timezone = tz.gettz('Europe/Helsinki')
    return dt.astimezone(hki_timezone)
```
-->

Ratkaisussa tarvitaan myös Pythonin standardikirjaston `datetime`-moduulin dokumentaatiota: https://docs.python.org/3/library/datetime.html.

### Koodin korjaaminen

Kun **yksikkö** eli `str_to_datetime` on testattu toimivaksi, se voidaan ottaa käyttöön myös main-funktiossa. Datetime-oliolta saadaan selvitettyä päivämäärä ja kellonaika kotimaisessa muodossa seuraavien `strftime`-metodikutsujen avulla.

```python
date = datetime.strftime('%d.%m.%G')
time = datetime.strftime('%H:%M')
```

Oikeat muotoilumääreet selviävät datetime-moduulin dokumentaatiosta: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

Lopulta voimme myös suorittaa koodin ja varmistaa että korjaus tuotti toivotun lopputuloksen.


## Miten testata koodia, jolla on riippuvuuksia?

> *"Some of the parts of our application may have dependencies for other libraries or objects. To isolate behaviour of our parts we need to substitue external dependencies. Here comes the mocking. We mock external API to have certain behaviours such as proper return values that we previously defined."*
>
> Krzysztof Żuraw, 2016. https://krzysztofzuraw.com/blog/2016/mocks-monkeypatching-in-python

Ohjelmakoodiin toteuttamamme `get_events_by_date` on riippuvainen toisesta funktiosta nimeltä `get_events`, joka tekee REST-kutsun ja parsii vastauksena saadun JSON-olion listaksi sanakirjoja:

```
get_events_by_date -> get_events -> urllib.request.urlopen -> REST-api
```

Koska eri ajankohtina REST-rajapinnasta saadaan eri vastauksia, on tuloksen oikeellisuus vaikea varmistaa. Oikea pyyntö REST-palveluun ja vastauksen käsittely voi myös viedä tarpeettoman paljon aikaa, joten sitä ei haluta tehdä yksikkötestissä.

Yksikkötesteissä korvataan usein riippuvuuksia mock'eilla, joiden avulla saadaan rajattua testi vain tiettyyn osaan koodista, vaikka testattavalla koodinpätkällä olisikin riippuvuuksia:

```
get_events_by_date -> get_events=Mock([test0, test1, test2, test3])
```

Riippuvuudet voivat olla niin ulkoisiin rajapintoihin kuin vaikka kellonaikoihin liittyviä.

### pytest-mock

Käyttämämme Pytest-moduulin `pytest-mock`-laajennus voidaan asentaa seuraavasti:

`pip3 install pytest-mock`

Pystest-mock (https://pypi.org/project/pytest-mock/) lisää testeihin käytettäväksi `mocker`-olion, joka saadaan **injektoitua** testifunktioon kirjoittamalla testin parametrimuuttujiin `mocker`:

```python
# dependency injection huolehtii `mocker`-olion injektoimisesta:
def test_get_events_by_date_with_mock(mocker):
    pass
```

Koska määrittelimme parametrin `mocker`-nimiseksi, Pytest tietää, että tätä testiä varten täytyy injektoida mocker-olio. Kun mocker on injektoitu funktioon, sen avulla voidaan korvata tilapäisesti esimerkiksi funktioita uusilla mock-funktioilla, joilla on aina sama paluuarvo:

```python
mocker.patch('moduuli.funktio', return_value=palauta_aina_tama_vastaus)
```

Korvataankin nyt `get_events`-funktion uudella funktiolla, joka palautaa ennalta määrätyn arvon:

```python
mocker.patch('events_by_date.get_events', return_value=my_list_of_test_events)
```

Mocker-olio ja injektointi huolehtivat siitä, että `get_events`-funktiota ei korvata pysyvästi, vaan kyseisen testin suorittamisen jälkeen `get_events` ja kaikki muut korvatut funktiot palautetaan taas ennalleen. `get_events_by_date` voidaan siis testata korvaamalla sen riippuvuus staattisella paluuarvolla, jonka tuloksen tiedämme ennalta:

```python
# dependency injection huolehtii `mocker`-olion injektoimisesta:
def test_get_events_by_date_with_mock(mocker):

    # Tapahtumat epäjärjestyksessä:
    mock_response = [CHRISTMAS_EVENT, UNKNOWN_EVENT, JANUARY_1ST_EVENT]

    # Asetetaan get_events palauttamaan yllä oleva lista tapahtumista:
    mocker.patch('events_by_date.get_events', return_value=mock_response)

    # get_events_by_date kutsuu sisäisesti get_events-funktiota
    result = events_by_date.get_events_by_date()

    # get_events_by_date on nyt palauttanut tunnetut tapahtumat oikeassa järjestyksessä:
    assert result == [UNKNOWN_EVENT, JANUARY_1ST_EVENT, CHRISTMAS_EVENT]
```


## Integraatiotestaus

> *"Integraatiotestauksessa testataan useiden komponenttien yhteistoimintaa tavoitteena löytää virheitä, jotka eivät tulleet esiin yksikkötesteissä. Testeissä suoritetaan tiettyjä suorituspolkuja, jotka hyödyntävät useita eri yksiköitä tai laajempia komponentteja, ja tarkastellaan toiminnan tuloksia."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. [Testauksen tasot](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot)

Koska edellisissä testeissä käytimme itse luotua keinotekoista dataa, ei testit välttämättä paljasta kaikkia virheitä, jotka ilmenevät rajapinnan oikeassa datassa. Siksi on tärkeää testata myös oman ohjelmamme ja rajapinnan välistä yhteistoimintaa integraatiotestillä.

Integraatiotestit voivat olla luonteeltaan yksikkötestejä monimutkaisempia ja hitaampia, joten niitä suoritetaan tyypillisesti keskitetyssä CI-järjestelmässä (continuous integration) eikä välttämättä vain kehittäjän omalla työasemalla. Meidänkin tapauksessamme on odotettavaa, että bubble sort -toteutuksen testaaminen vie ainakin minuutin jokaisella testikerralla.

Integraatiotestejä voidaan toteuttaa samoilla teknologioilla kuin yksikkötestejä, ja voisimme esimerkiksi testata `get_events_by_date`-funktiomme seuraavasti:

```python
# Tämä testifunktio kutsuu API:a ja lajittelee tapahtumat oikeasti. Se voi olla siis hyvin hidas.
def test_get_events_by_date_integration_test():

    # Nyt rajapintaa kutsutaan oikeasti ja oikeat tapahtumat lajitellaan:
    result = events_by_date.get_events_by_date()

    # Testi edellyttää rajapinnalta aina vähintään 100 tapahtumaa, vaikka oikea määrä on tuntematon:
    assert len(result) > 10

    # Vertaillaan että alkamisaika on joko None tai peräkkäiset ovat oikeassa järjestyksessä:
    for i in range(len(result) - 1):
        assert result[i]['event_dates']['starting_day'] == None or result[i]['event_dates']['starting_day'] < result[i + 1]['event_dates']['starting_day']
```

Tällä kertaa `get_events`-funktiota ei ole korvattu mock'illa, vaan se hakee tiedot oikeasta REST-rajapinnasta. Koska rajapinta palauttaa ajankohdasta riippuen eri tapahtumat, emme voi olla varmoja, kuinka monta tapahtumaa täsmälleen palautetaan. Testissä voidaan kuitenkin varmistaa, että tapahtumia löytyy ja että niiden päiväykset ovat nyt oikeassa järjestyksessä.

## Järjestelmätestaus

> *"Järjestelmätestauksessa testataan kokonaista ohjelmaa, ja tarkastellaan vastaako ohjelma sille asetettuja vaatimuksia ja käyttötarkoitusta. Aitoon ympäristöön kuuluvat mm. käytettävä laitteisto, tietokannat ja käyttäjät."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. [Testauksen tasot](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot)

Järjestelmätestauksella varmistetaan usein monivaiheisia käyttötapauksia. Testattava käyttötapaus voisi pitää sisällään esimerkiksi kirjautumisen järjestelmään, jonkin datan muokkaamisen ja muokatun datan tarkastelemisen. Järjestelmätestejä tehdäänkin usein eri työkaluilla kuin yksikkötestejä. Yksi järjestelmätesteissä hyödyllinen testityökalu on kotimaista alkuperää oleva [Robot Framework](https://robotframework.org/), jolla voidaan erilaisten laajennusten kanssa testata verkkosivuja tai vaikka matkapuhelinverkkoja. Robot Frameworkilla on oma kielensä, jolla testitapaukset voivat näyttää esim. tältä: https://github.com/robotframework/WebDemo/blob/master/login_tests/valid_login.robot.


# Extra: riippuvuuksien hallinta

Olemme tämän kurssin aikana asennelleet Pythonin kirjastoja yksi kerrallaan `pip3 install` -komennolla. Jotta kirjoittamamme koodi olisi asennettavissa toisen kehittäjän koneelle tai tulvaisuudessa CI- ja tuotantoympäristöihin, täytyy riippuvuudet dokumentoida. Pip-pakettienhallinta mahdollistaa asennettujen riippuvuuksien listaamisen kätevästi `pip3 freeze`-komennolla:

```
$ pip3 freeze

autopep8==1.5.4
pylint==2.5.3
pytest==6.0.1
pytest-mock==3.3.1
python-dateutil==2.8.1
rope==0.17.0

# ... ja monia muita riippuvuuksia
```

Pip mahdollistaa myös useiden riippuvuuksien asentamisen kerralla `requirements.txt` -tiedostojen avulla. Voit lukea lisää näistä tiedostoista [virallisesta dokumentaatiosta](https://pip.pypa.io/en/stable/user_guide/#requirements-files). Tätä omaa projektiamme varten voimme tallentaa riippuvuudet `requirements.txt`-tiedostoon listaamalla ne `freeze`-komennolla ja ohjaamalla `freeze`-komennon tulosteet `requirements.txt`-nimiseen tiedostoon:

```
$ pip3 freeze > requirements.txt
$
$ # Katsotaan tiedoston sisältö:
$ cat requirements.txt

autopep8==1.5.4
pylint==2.5.3
pytest==6.0.1
pytest-mock==3.3.1
python-dateutil==2.8.1
rope==0.17.0
```

Myöhemmin samat riippuvuudet on asennettavissa uuteen ympäristöön yksinkertaisesti kutsumalla `install`-komentoa `-r` -vivulla:

```
$ # Luetaan ensin ohje:
$ pip3 help install | grep "requirements"
  pip3 install [options] -r <requirements file> [package-index-options] ...
  pip also supports installing from "requirements files", which provide
  -r, --requirement <file>    Install from the given requirements file. This

$ # Nyt asennetaan  riippuvuudet tiedostosta:
$ pip3 install -r requirements.txt
```

# Extra: testien kattavuus (coverage)

Yksi tapa mitata testien laatua on testikattavuus (coverage), joka tarkoittaa niiden kirjoitettujen koodirivien osuutta, jotka suoritetaan testien aikana. Testikattavuutta voidaan rivien määrän lisäksi mitata myös erilaisten suorituspolkujen määrillä. Pythonin `coverage`-moduuli auttaa selvittämään, mitkä rivit tulevat suoritetuksi testien aikana. Voit halutessasi tutustua tähän työkaluun itsenäisesti.

```sh
$ pip3 install coverage     # coverage-moduulin asentaminen
```

Suoritetaan testit `coverage` -komennolla ja lasketaan testikattavuus testatulle events_by_date-tiedostolle:

```sh
$ coverage run --source=events_by_date -m pytest test_events_by_date.py
```

Katsotaan raportti:

```
$ coverage report

Name                Stmts   Miss  Cover
---------------------------------------
events_by_date.py      48      3    94%
```

Voit käyttää myös `coverage html`-komentoa, joka muodostaa raportin staattisen verkkosivun muodossa.


# Tehtävä

Tällä viikolla harjoitellaan koodin refaktorointia ja yksikkötestausta kirjoittamalla testejä aikaisemmin koodaamallesi `postinumerot.py`-tiedostolle. Mikäli aikaisempi tehtävä jäi sinulta palauttamatta tai et halua käyttää vanhaa koodiasi, voit käyttää myös tehtävän malliratkaisun tiedostoja:

* [postinumerot.py](../00_linux_ja_python/src/postinumerot.py)
* [postitoimipaikka.py](../00_linux_ja_python/src/postitoimipaikka.py)


## Refaktorointi

Mikäli käytät malliratkaisua tai oma toteutuksesi noudattaa malliratkaisun kaltaista arkkitehtuuria, jossa kaikki logiikka on toteutettu `main`-funktioon, joudut refaktoroimaan koodia testaamisen mahdollistamiseksi.

Voit toteuttaa esimerkiksi funktion, joka ottaa parametreinaan etsittävän postitoimipaikan nimen sekä sanakirjan postinumeroista ja postitoimipaikoista ja palauttaa annettua toimipaikkaa vastaavat postinumerot listana:

```python
def etsi_postinumerot(postitoimipaikka, postinumerot_sanakirja):
    pass # todo
```
Tämän funktion testaaminen on huomattavasti helpompaa kuin main-funktion, koska `etsi_postinumerot` ei kysy käyttäjältä mitään eikä tee tulostuksia.

## Testien laajuus ja kattavuus

Testaa toteuttamasi logiikka ainakin tapauksissa, joissa:

1. annettua nimeä ei löydy lainkaan aineistosta
1. postitoimipaikan nimellä löytyy yksi postinumero
1. postitoimipaikan nimellä löytyy useita postinumeroita

Saadaksesi täydet pisteet tehtävästä **sinun ei tarvitse** testata syötteitä pyytäviä tai tulosteita tekeviä kohtia koodista. Riittää siis, että testaat esimerkiksi pelkän edellä esitetyn `etsi_postinumerot`-funktion, mikäli päädyt refaktoroimaan sellaisen omaan koodiisi.

Voit oman harkintasi mukaan käyttää testeissä joko itse luomaasi testidataa tai antaa testattavan koodin lukea postinumeroaineiston verkosta tai levyltä. Testiaineiston käyttämisessä `pytest-mock` voi olla avuksi, mutta sitä ei ole välttämätöntä käyttää.

Tehtävän malliratkaisussa tulemme tutustumaan myös siihen, miten ohjelman tulosteet voidaan tarkistaa yksikkötestissä.


## Tehtävän arviointi

Ratkaisu, joka on refaktoroitu testauskuntoon ja testattu edellä esitetyillä kolmella testitapauksella hyväksytään arvosanalla 5. Myös puutteelliset ratkaisut hyväksytään eri arvosanoin, kunhan niissä osoitetaan selvää yritystä tehtävän ratkaisemiseksi.

## Tehtävän palauttaminen

Palauta koodaamasi testit sekä testattavat moduulit sellaisenaan, eli **ei pakattuna** Teamsissa olevaan palautuslaatikkoon **seuraavaan oppituntiin mennessä**.
