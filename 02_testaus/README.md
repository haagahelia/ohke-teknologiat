# Testaus

Tämän oppitunnin tavoitteena on tutustua testauksen eri tasoihin yksikkötesteistä järjestelmätesteihin ja tutustua testiautomaation käsitteistöön ja työkaluihin.

Aiheen opiskelun jälkeen osaat kirjoittaa Python-funktioillesi yksikkötestit ja tiedät mistä lähteä liikkeelle, kun sinulle tulee tarve kirjoittaa automatisoituja testejä. Osaat myös huomioida testausnäkökulmaa jäsentäessäsi Python-ohjelmiasi eri moduuleihin ja funktioihin.


# Oppitunnin videot


**[Osa 1: Python-tehtävän malliratkaisu ja orientaatio testaukseen](https://web.microsoftstream.com/video/8f0d594f-9277-4782-937e-9d215d7cf7c4)** *44:38*

Tällä videolla käymme läpi postitoimipaikka- ja postinumerot-tehtävien malliratkaisut ja tutustumme testaukseen yleisellä tasolla.

**[Osa 2: pytest-työkalu](https://web.microsoftstream.com/video/674aaa29-74eb-401f-8251-e6f14df7ae5d)** *45:43*

Tällä videolla tutustumme Pytest-työkaluun ja yksikkötestien automatisointiin. 

**[Osa 3: pytest-mock ja harjoitustehtävän tehtävänanto](https://web.microsoftstream.com/video/9c438228-0354-49bb-8fb1-1ad03e4222cd)** *33:10*

Tällä videolla harjoittelemme ulkoisten riippuvuuksien korvaamista testeissä ja käymme läpi viikkotehtävän tehtävänannon.


## Suositeltava oheisvideo: [What is Automated Testing?](https://www.youtube.com/watch?v=Nd31XiSGJLw)

[![What is Automated Testing?](https://img.youtube.com/vi/Nd31XiSGJLw/mq3.jpg)](https://www.youtube.com/watch?v=Nd31XiSGJLw)

> *"In this video we start diving into the world of quality assurance and discuss automated testing for our web and mobile applications..."*
>
> The Startup Lab. [What is Automated Testing?](https://www.youtube.com/watch?v=Nd31XiSGJLw)


# Oppitunnin sisältö ja tavoitteet

Oppitunnin tavoitteena on erityisesti tustua yksikkötestauksen käsitteisiin ja hahmottaa hyviä käytäntöjä testauksen toteuttamiseksi ja testattavan koodin kirjoittamiseksi.

Tällä oppitunnilla kokeilemme testausta eri tasoilla hyödyntäen Pythonin `pytest`-moduulia:

> *"pytest is a mature full-featured Python testing tool that helps you write better programs."*
>
> [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)

Testattava ohjelmisto on edellisen viikon kotitehtävästä tuttu ohjelma, joka hakee GitHubista JSON-muotoisen postinumeroaineiston ja näyttää käyttäjälle joko tiettyyn postinumeroon liittyvän postitoimipaikan nimen tai postitoimipaikkaan liittyvät postinumerot.

Pytestin sijaan testejä voitaisiin kirjoittaa myös muita työkaluja hyödyntäen, kuten Pythonin [unittest-moduulilla](https://docs.python.org/3/library/unittest.html). Pytest on kuitenkin valittu kurssille siksi, että se ei edellytä minkään ulkoisten riippuvuuksien käyttämistä testikoodeissasi, vaan voit kirjoittaa testit kuten kirjoittaisit mitä tahansa muutakin Python-koodia.

Mikäli haluat tutustua pytest-työkaluun oppituntia syvällisemmin, suosittelen lukemaan esimerkiksi artikkelin [Testing Python Applications with Pytest](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest).

# Testauksen käsitteet

<!--Testauksen käsitteistöön kuuluu oleellisena osana eri tasot, joilla erityisesti automatisoitua testausta suoritetaan. 

[Jyväskylän Yliopiston Informaatioteknologian tiedekunnan testaussivusto](http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot) kuvaa testauksen tasot selkeänä kokonaisuutena ja kyseisen sivuston määritelmiä noudatetaan myös tällä oppitunnilla.-->


## Yksikkötestaus

> *"Yksikkötestauksella tarkoitetaan **pienimmän mahdollisen ohjelman osan**, esimerkiksi aliohjelman, toiminnan testaamista. Yksikkötesteillä varmistetaan, että ohjelman pienimmät osat toimivat odotetulla tavalla, ja että mahdolliset virhetilanteet on niiden osalta ennakoitu."*
>
> *"Yksikkötestauksen hyödyt näkyvät kehitysprosessin aikana erityisesti silloin, kun jo kirjoitettuun koodiin joudutaan tekemään muutoksia. Automatisoiduilla yksikkötesteillä voidaan **nopeasti** todeta, aiheuttavatko tehdyt muutokset virheitä."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. Testauksen tasot.<!--http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot-->

Katsotaan ensimmäiseksi alla esitettyä funktiota, joka vaihtaa annetulta listalta kahdessa indeksissä olevat alkiot keskenään:

```python
# tiedosto swap.py

def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]
```

Tämä `swap`-funktio voisi olla yksi yksittäinen yksikkö esimerkiksi lajuttelualgoritmin toteuttavassa Python-moduulissa. Mutta miten tätä funktiota voitaisiin testata? 

### Testitapaus

Yksinkertaisimmillaan voimme kirjoittaa yksittäisen testifunktion, **eli testitapauksen**, joka kutsuu yllä esitettyä testattavaa funktiota ja tarkistaa sen tuloksen.

> *"A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.*"
>
> Python Software Foundation. Unit testing framework. https://docs.python.org/3/library/unittest.html

```python
# tiedosto test_swap.py

from swap import swap


def test_swapping_two_strings():
    lista = ['eka', 'vika']

    swap(lista, 0, 1)

    assert lista == ['vika', 'eka']

test_swapping_two_strings() # TODO: tästä halutaan myöhemmin eroon
```

Tämä testi luo ensin listan kahdesta merkkijonosta, minkä jälkeen se yrittää vaihtaa niiden paikkoja. Lopuksi testi hyödyntää `assert` -komentoa varmistaakseen, että lopputulos vastaa odotuksia.


### assert-komento

Python-kielessä on valmiina [`assert`-komento](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement), jolla voidaan suoraviivaisesti varmistaa, että tietyn lausekkeen arvo on `True`:

```python
assert len('hello') == 5 # True, ei aiheuta poikkeusta
```

Mikäli arvo puolestaan on epätosi, aiheuttaa `assert`-komento `AssertionError`-poikkeuksen.

```python
assert len('welcome') == 5 # False, aiheuttaa poikkeuksen:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

Testeissä `assert`-komentoa käytetään yksinkertaisesti varmistamaan, että testatun koodin tulos on se mitä pitäisi. Jos koodi ei aiheuta poikkeusta, `pytest` tulkitsee testin onnistuneeksi. Jos taas koodista aiheutuu `AssertionError`, `pytest` tulkitsee testin epäonnistuneeksi:

```python
sanat = ['ajattelen', 'siis', 'olen']

swap(lista, 0, 2)

assert sanat == ['olen', 'siis', 'ajattelen']
```

Tämä testitapaus tulee vielä kirjoittaa omaan funktioonsa, jotta se olisi yksittäinen testitapaus:

```python
def test_swapping_two_strings():
    sanat = ['ajattelen', 'siis', 'olen']

    swap(lista, 0, 2)

    assert sanat == ['olen', 'siis', 'ajattelen']

test_swapping_two_strings() # TODO: tästä halutaan myöhemmin eroon
```

## Testien suoritustyökalu: test runner

Suoritimme ensimmäisen testitapauksen ylempänä suorittamalla testitapauksen itse tiedoston lopussa:

```python
test_swapping_two_strings() # TODO: tästä halutaan myöhemmin eroon
```

Tämä ei kuitenkaan ole kovin kätevää, koska joutuisimme huolehtimaan itse siitä, että kaikki testitapaukset kaikissa eri testitiedostoissa tulevat suoritetuiksi. Tulokset olisi myös hyvä koostaa raportiksi. Lisäksi poikkeuksia heittävien testitapausten ei suotaisi lopettavan muiden testien suorittamista, vaan meidän tulisi kehittää sitä verten poikkeustenhallinta. Onkin paljon kätevämpää käyttää "test runner" -työkalua testien suorittamiseksi ja testiraportin generoimiseksi:

Testien automatisoimiseksi käytämme mieluummin aiemmin mainittua `pytest`-moduulia. Pytest huolehtii testitiedostojen ja niiden sisältämien testifunktioiden etsimisestä ja suorittamisesta automaattisesti. Se myös tuottaa selkokielisen raportin testien tuloksista.

Jotta Pytest käsittelee tiedostojamme testimoduuleina ja niissä olevia funktioita testitapauksina, sekä tiedostojen että funktioiden nimen alussa tulee olla etuliite `test_`.

### Pytest-moduulin asentaminen ja suorittaminen

Voit asentaa Pythonin pytest-moduulin itsellesi seuraavalla komennolla:

`pip3 install pytest`

Pytest-moduulia voidaan käyttää joko erillisellä `pytest`-komennolla tai `python3`-komennon kautta valitsemalla `-m` -vivulla moduuliksi `pytest`. Voit varmistaa asennuksen toimivuuden esimerkiksi seuraavasti:

```
$ python3 -m pytest
======== test session starts =========
collected 1 item

src/test_swap.py .      [100%]

========= 1 passed in 0.06s ==========
```

`pytest` voidaan käynnistää myös omalla komennollaan:

```
$ pytest
======== test session starts =========
collected 1 item

src/test_swap.py .      [100%]

========= 1 passed in 0.06s ==========
```

## Testien kattavuus

Testien kattavuutta voidaan mitata lukuisilla eri tavoilla. Tyypillisiä tapoja on mitata testeissä suoritettujen rivien tai vaihtoehtoisten suorituspolkujen määrää. Hyvällä testikirjastolla katamme kuitenkin myös koodin logiikan kannalta oleelliset tapaukset.

Edellä esitetyn `swap`-funktion testejä olisikin kenties syytä laajentaa vielä esim. seuraavilla testitapauksilla:

* kahden merkkijonon vaihtaminen pidemmällä listalla
* kahden kokonaisluvun paikan vaihtaminen
* merkkijonon ja kokonaisluvun paikkojen vaihtaminen
* sanakirjatyyppisten arvojen paikkojen vaihtaminen listalla
* ...

> "*A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.*"
>
> Python Software Foundation. Unit testing framework. https://docs.python.org/3/library/unittest.html



# Yksikkötestauksen haasteet

Ohjelman rakenteesta riippuen sen testaaminen voi olla hyvin hankalaa. Esimerkiksi globaalit muuttujat, ulkoiset riippuvuudet ja "spagettikoodi" vaikeuttavat testausta merkittävästi. Jos testattavassa koodissa tehdään esimerkiksi HTTP-pyyntöjä tai tietokantakyselyjä, näiden operaatioiden tulokset vaikuttavat testien tuloksiin, joten testattavan aineiston muuttuessa myös testien tulokset voivat muuttua, vaikka koodi edelleen toimisi toivotulla tavalla. Oppitunnilla sivuamme myös tällaisten riippuvuuksien korvaamista testikohtaisilla mock-toteutuksilla.

Ulkoisten riippuvuuksien vaikutuksen minimoimiseksi testit suoritetaan usein erillisessä QA-ympäristössä (quality assurance), jossa eri rajapintojen vastaukset ja toiminta on hallittavissa. Tällä oppitunnilla meillä ei ole käytössä QA-ympäristöä, joten testaamme integraatiota postinumeroaineiston "tuotantodataa" vasten.

# Oman postinumerologiikan testaaminen

Mikäli oma postinumerotehtävän ratkaisusi noudattaa malliratkaisun kaltaista arkkitehtuuria, jossa kaikki logiikka on toteutettu moduulin tasolle, joudut refaktoroimaan koodia testaamisen mahdollistamiseksi. Tämä johtuu siitä, että yksikkötestissä et halua kysyä syötettä käyttäjältä tai antaa ohjelman tulostaa konsoliin, vaan haluat itse ohjelmallisesti tarkistaa oikean lopputuloksen tietyllä syötteellä. 

Toinen ongelma alkuperäisessä toteutuksessamme on logiikan toteuttaminen "skriptinä", eli koodina, joka suoritetaan saman tien, mutta joka ei ole hyödynnettävissä muista Python-moduuleista.

> *"Python files which are used to run as a stand-alone Python app (top-level files) are usually designed to run as scripts and importing them would actually run the commands in the script.*"
>
> Pavloski, M. Python Modules: Creating, Importing, and Sharing. https://stackabuse.com/python-modules-creating-importing-and-sharing/

Koodin automaattisen suorittamisen sijaan haluamme suorittaa sen ainoastaan silloin, kun sitä ollaan suorittamassa skriptinä. Lue lisää aiheesta artikkelin kohdasta ["Dual-Mode Code"](https://stackabuse.com/python-modules-creating-importing-and-sharing/#dualmodecode):

```python
if __name__ == '__main__':
    main()
```

Kun testattavan moduulin `import` onnistuu, joudumme vielä muokkaamaan koodia siten, että se koostuu erikseen testattavissa olevista yksiköistä. Voimme toteuttaa esimerkiksi funktion, joka ottaa parametreinaan etsittävän postinumeron sekä sanakirjan postinumeroista ja postitoimipaikoista, ja palauttaa annettua toimipaikkaa vastaavan postinumeron nimen tulostusta varten muotoiltuna:

```python
def etsi_postitoimipaikka(postinumero, postinumerot_sanakirja):
    if postinumero in postinumerot_sanakirja:
        return postinumerot_sanakirja[postinumero].title()
    else:
        return None
```

Tämän funktion testaaminen yksikkötestillä onkin jo huomattavasti helpompaa, koska se ei kysy käyttäjältä mitään eikä tee tulostuksia.


# Yksikkötestien suorittaminen VS Codella

VS Codessa on oma erillinen näkymänsä testeille. Tämän näkymän kautta testien suoritusta voidaan nopeuttaa ja tehdä vielä havainnollisemmaksi kuin komentoriviltä.

> *Testing in Python is disabled by default. To enable testing, use the Python: **Configure Tests** command on the Command Palette. This command prompts you to select a test framework, the folder containing tests, and the pattern used to identify test files.*
>
> Python testing in Visual Studio Code. https://code.visualstudio.com/docs/python/testing


Ota testausominaisuudet käyttöön seuraamalla oppituntia tai ohjeita sivulla: https://code.visualstudio.com/docs/python/testing


# Testidata

<!--TODO: Usein tarvitsemme realistista testidataa, jotta tiedämme, että koodi toimii esimerkiksi erilaisten indeksien, eri pituisten listojen ja eri tyyppisten arvojen kanssa. -->

Testien kirjoittamisen ja hyödyllisyyden kannalta testattava data on avainasemassa. Jos testattava data vaihtelee, myös testien tulokset vaihtelevat. Lisäksi on tärkeää käyttää sellaista dataa, joka vastaa sopivan tarkasti oikeaa dataa, vaikka olisikin laajuudeltaan merkittävästi rajatumpaa.

> *"A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process."*
>
> Python Software Foundation. Unit testing framework. https://docs.python.org/3/library/unittest.html

Postinumerologiikkaa voitaisiin testata esimerkiksi seuraavanlaisella valmiilla tietorakenteella:

```python
TOIMIPAIKAT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}
```

Tämän testiaineiston pohjalta voidaan testata jo tapauksia, joissa samaa postitoimipaikkan nimeä kohden löytyy yksi, useampi tai ei yhtään postinumeroa. Lisäksi voisi olla hyvä testata erityistapauksia, joissa toimipaikan nimessä esiintyy esimerkiksi ääkkösiä, välilyöntejä tai välimerkkejä:

```python
ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST"
}
```

Tämän yksinkertaisen ohjelmalogiikan osalta testidata voidaan luoda yksinkertaisesti Pythonin sanakirjoina. Tietokantapohjaisessa ohjelmistossa ennalta määrätty testidata voidaan tyypillisesti syöttää tietokantaan ennen jokaista testiä, jotta jokaisen testin alussa tietokannan sisältö on varmasti sama.

Monissa tapauksissa tietokannan alustaminenkaan ei riitä testien alustamiseksi. Esimerkiksi postinumero-ohjelmassamme yksi funktio hakee HTTP-pyynnön avulla JSON-tietorakenteen, jonka sisältö jossain vaiheessa tulee muuttumaan. Näiden riippuvuuksien korvaaminen testidatalla onkin laajemman ohjelman testaamisessa keskeinen tehtävä.


## Miten testata koodia, jolla on riippuvuuksia?

> *"Some of the parts of our application may have dependencies for other libraries or objects. To isolate behaviour of our parts we need to substitue external dependencies. Here comes the mocking. We mock external API to have certain behaviours such as proper return values that we previously defined."*
>
> Krzysztof Żuraw, 2016. https://krzysztofzuraw.com/blog/2016/mocks-monkeypatching-in-python

Ohjelmakoodiin toteuttamamme `hae_postinumerot` tekee HTTP-kutsun ja parsii vastauksena saadun JSON-olion sanakirjaksi:

```python
def hae_postinumerot():
    with urllib.request.urlopen(URL) as response:
        data = response.read()
    return json.loads(data)
```

Koska HTTP-rajapinnasta saatava vastaus muuttuu Postin postinumeroiden muuttuessa, joten tuloksena saatava sanakirja vaihtelee ajan kuluessa. Tämän aineiston muuttumisnopeus ei välttämättä ole nopea, mutta ongelma olisi ilmeinen esimerkiksi hetkellisiä säähavaintoja haettaessa. Datan muuttumisen lisäksi oikea pyyntö HTTP:n yli ja vastauksen käsittely voi myös viedä tarpeettoman paljon aikaa, joten sitä ei haluta tehdä yksikkötestissä.

Yksikkötesteissä ulkoiset riippuvuudet korvataan usein ns. mock'eilla, joiden avulla testi suorittaa vain tietyn osaan koodista. Riippuvuudet voivat olla niin ulkoisiin rajapintoihin kuin vaikka kellonaikoihin liittyviä.

### pytest-mock

Käyttämämme Pytest-testityökalun `pytest-mock`-laajennus voidaan asentaa seuraavasti:

```
pip3 install pytest-mock
```

Pystest-mock (https://pypi.org/project/pytest-mock/) lisää testeihin käytettäväksi `mocker`-olion, joka saadaan **injektoitua** testifunktioon kirjoittamalla testin parametrimuuttujiin `mocker`:

```python
# dependency injection huolehtii `mocker`-olion injektoimisesta,
# kunhan olemme asentaneet pytest-mock-paketin:
def test_tama_testi_tarvitsee_mockerin(mocker):
    pass
```

Koska määrittelimme parametrin `mocker`-nimiseksi, Pytest tietää, että tätä testiä varten täytyy injektoida juuri mocker-olio. Muilla nimillä saisimme käyttöömme muita laajennoksia.

Kun mocker on injektoitu funktioon, sen avulla voidaan korvata tilapäisesti esimerkiksi funktioita uusilla mock-funktioilla, joilla on aina sama paluuarvo:

```python
def test_tassa_testissa_hae_postinumerot_on_mockattu(mocker):
    mocker.patch('http_pyynto.hae_postinumerot', return_value={ '00100': 'HELSINKI' })

```

Yllä oleva koodirivi korvaa testitapauksen suorituksen ajaksi `http_pyynto.hae_postinumerot`-funktion toisella, joka palauttaa aina saman vastauksen.

Mocker-olio ja injektointi huolehtivat siitä, että `hae_postinumerot`-funktiota ei korvata pysyvästi, vaan kyseisen testitapauksen suorittamisen jälkeen tämä ja kaikki muut korvatut funktiot palautetaan taas ennalleen. `hae_postinumerot` voidaan siis testata korvaamalla sen riippuvuus staattisella paluuarvolla, jonka tuloksen tiedämme ennalta.

<!--
## Test driven development

Tietorakenteet ja algoritmit -aiheen malliratkaisussa on havaittu bugi, joka [on raportoitu GitHubiin issuena](https://github.com/haagahelia/swd4tn023/issues/1). Bugin seurauksena kaikkien tapahtumien ajankohdat on ilmoitettu UTC-ajassa, eli ne eivät vastaa Suomen paikallisia aikoja.

Tämä on kiusallinen ongelma, joka korjataan seuraavaksi.

Päivämäärien käsittelemiseksi asennamme `dateutil`-paketin, joka helpottaa aikavyöhykkeiden käyttämistä ja merkkijonomuotoisten päivämäärien parsimista:

`pip3 install python-dateutil`

Dateutil-paketin dokumentaatio löytyy osoitteesta https://dateutil.readthedocs.io/en/stable/
-->

<!--
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


Ratkaisussa tarvitaan myös Pythonin standardikirjaston `datetime`-moduulin dokumentaatiota: https://docs.python.org/3/library/datetime.html.



### Koodin korjaaminen

Kun **yksikkö** eli `str_to_datetime` on testattu toimivaksi, se voidaan ottaa käyttöön myös main-funktiossa. Datetime-oliolta saadaan selvitettyä päivämäärä ja kellonaika kotimaisessa muodossa seuraavien `strftime`-metodikutsujen avulla.

```python
date = datetime.strftime('%d.%m.%G')
time = datetime.strftime('%H:%M')
```

Oikeat muotoilumääreet selviävät datetime-moduulin dokumentaatiosta: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

Lopulta voimme myös suorittaa koodin ja varmistaa että korjaus tuotti toivotun lopputuloksen.

-->

## Integraatiotestaus

> *"Integraatiotestauksessa testataan useiden komponenttien yhteistoimintaa tavoitteena löytää virheitä, jotka eivät tulleet esiin yksikkötesteissä. Testeissä suoritetaan tiettyjä suorituspolkuja, jotka hyödyntävät useita eri yksiköitä tai laajempia komponentteja, ja tarkastellaan toiminnan tuloksia."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. Testauksen tasot. <!--http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot-->

Koska edellisissä testeissä käytimme itse luotua keinotekoista dataa, ei testit välttämättä paljasta kaikkia virheitä, jotka ilmenevät rajapinnan oikeassa datassa. Siksi on tärkeää testata myös oman ohjelmamme ja rajapinnan välistä yhteistoimintaa integraatiotestillä.

Integraatiotestit voivat olla luonteeltaan yksikkötestejä monimutkaisempia ja hitaampia, joten niitä suoritetaan tyypillisesti keskitetyssä CI-järjestelmässä (continuous integration) eikä välttämättä vain kehittäjän omalla työasemalla. 

Integraatiotestejä voidaan toteuttaa samoilla teknologioilla kuin yksikkötestejä. Käytännössä voisimme toteuttaa integraatiotestin oman Python-sovelluksemme ja JSON-rajapinnan välille kirjoittamalla samankaltaisen testin kuin aikaisemmin, mutta ilman mock-vastausta.

## Järjestelmätestaus

> *"Järjestelmätestauksessa testataan kokonaista ohjelmaa, ja tarkastellaan vastaako ohjelma sille asetettuja vaatimuksia ja käyttötarkoitusta. Aitoon ympäristöön kuuluvat mm. käytettävä laitteisto, tietokannat ja käyttäjät."*
>
> Jyväskylän Yliopisto, Informaatioteknologian tiedekunta. Testauksen tasot <!--http://smarteducation.jyu.fi/projektit/systech/Periaatteet/suunnittelun-periaatteet/testaus/testauksen-tasot-->

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

Pip mahdollistaa myös useiden riippuvuuksien asentamisen kerralla `requirements.txt` -tiedostojen avulla. Voit lukea lisää näistä tiedostoista [virallisesta dokumentaatiosta](https://pip.pypa.io/en/stable/user_guide/#requirements-files). 

Tätä omaa projektiamme varten voimme tallentaa riippuvuudet `requirements.txt`-tiedostoon ohjaamalla `freeze`-komennon tulosteet `requirements.txt`-nimiseen tiedostoon:

```
$ pip3 freeze > requirements.txt
```

```
$ cat requirements.txt

autopep8==1.5.4
pylint==2.5.3
pytest==6.0.1
pytest-mock==3.3.1
python-dateutil==2.8.1
rope==0.17.0
```

Myöhemmin samat riippuvuudet on asennettavissa uuteen ympäristöön yksinkertaisesti käyttämällä `install`-komentoa `-r` -[vivulla](https://pip.pypa.io/en/stable/user_guide/#requirements-files):

```
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

Tällä viikolla harjoittelemme koodin refaktorointia ja yksikkötestausta kirjoittamalla testejä aikaisemmin koodatulle `postinumerot.py`-skriptille (edellisen viikon tehtävän 2. osa). Mikäli aikaisempi tehtävä jäi sinulta palauttamatta tai et halua käyttää vanhaa koodiasi, voit käyttää myös tehtävän malliratkaisun tiedostoja.

* [postinumerot.py](https://gist.github.com/swd1tn002/c9685aa2cc9fc47e30ffc9a9d9dfc968#file-postinumerot-py)
* [http_pyynto.py](https://gist.github.com/swd1tn002/c9685aa2cc9fc47e30ffc9a9d9dfc968#file-http_pyynto-py)


## Osa 1: postitoimipaikkalogiikan testaaminen (arvosanatavoite 3)

Kirjoita yksikkötestit edellisen viikon Python-tehtävän osan 2 ratkaisullesi. Mikäli kyseinen tehtävä jäi sinulta toteuttamatta, voit käyttää testattavana koodina tehtävän malliratkaisua.

Sinun ei tarvitse testata koko ohjelmalogiikkaa, vaan riittää, että testaat esimerkiksi malliratkaisussa esitetyn `ryhmittele_toimipaikoittain`-funktion. Lisäksi joudut refaktoroimaan Python-tiedostoa siten, että sen testaaminen on ylipäänsä mahdollista.

Testeissä kannattaa varmistaa ainakin seuraavien tapausten toiminta:

1. postitoimipaikan nimellä löytyy vain yksi postinumero
1. postitoimipaikan nimellä löytyy useita postinumeroita.

Saadaksesi täydet pisteet tästä osasta **sinun ei tarvitse** testata syötteitä pyytäviä tai tulosteita tekeviä kohtia koodista. Voit oman harkintasi mukaan käyttää testeissä joko kovakoodattua testidataa tai antaa testattavan koodin lukea postinumeroaineiston verkosta tai levyltä. Testiaineiston käyttämisessä `pytest-mock` voi olla avuksi, mutta sitä **ei ole välttämätöntä käyttää**.


## Osa 2: bugin testaus ja korjaus (arvosanatavoite 5)

`postinumerot.py`-tiedoston koodista löytyi oppitunnilla bugi, joka [raportoitiin GitHubiin](https://github.com/haagahelia/swd4tn023/issues/5). Arvosanatavoitteeseen 5 sinun tulee kirjoittaa tarvittavat yksikkötestit, jotka osoittavat tämän bugin olemassaolon. Lopuksi korjaa bugi, jolloin kirjoittamasi yksikkötestit menevät läpi.

[Bugiraportissa](https://github.com/haagahelia/swd4tn023/issues/5) esiintyvä kirjoitusvirheiden käsittely ei ole tarpeen täysiin pisteisiin, mutta voit halutessasi kokeilla myös sen ratkaisemista jos kaipaat lisähaastetta.

**Vinkki**: bugin korjauksessa voi olla avuksi, jos poistat kaikki välilyönnit [Pythonin replace-funktiolla](https://stackoverflow.com/questions/9452108/how-to-use-string-replace-in-python-3-x).

**Vinkki**: voit hyödyntää testeissäsi bugiraportissa valmiiksi raportoituja postinumero- ja toimipaikkatietoja.

<!--
Smart post -postinumerot kirjoitettu usealla eri tavalla

Postinumeroaineistossa postitoimipaikka "SMARTPOST" esiintyy myös kirjoitusasulla "SMART POST" sekä kirjoitusvirheellä "SMARTPSOT". Ohjelman tulee käsitellä "SMART POST", "SMART-POST" ja "SMARTPOST" samoina toimipaikkoina, eli jättää mahdolliset erot tyhjissä- ja välimerkeissä huomioimatta. Mahdolliset kahden peräkkäisen kirjaimen sekoittumiset voidaan myös yrittää korjata ("SMARTPSOT"), mutta se ei ole pakollista.

# Oikea toiminta

Postinumerolistausten toimipaikoille "smart post" ja "smartpost" tulee tuottaa sama lista kaikista näihin toimipaikkoihin merkityistä postinumeroista. Saman logiikan tulee toimia myös muiden välilyöntejä mahdollisesti sisältävien toimipaikkojen nimien yhteydessä.

# Virheen toistaminen

```
$ python3 postinumerot.py

Kirjoita postitoimipaikka: smart post

Postinumerot: 44884, 40934, 65374, 07114
```

```
$ python3 postinumerot.py

Kirjoita postitoimipaikka: smartpsot

Postinumerot: 08504, 00314, 89604
```

```
$ python3 postinumerot.py

Kirjoita postitoimipaikka: smartpost

Postinumerot: 74704, 73464, 03604, ... 96204, 21234, 28204
```
-->

<!--
## Huom: Sanakirjan sisällön testaaminen

Pythonin sanakirja `dict` on hajautusrakenne, joka ei lisää arvoja muistiin järjestyksessä peräkkäisille paikoille, vaan etsii arvoille paikat avaimien hajautusfunktioiden avulla. Hajautusfunktio nopeuttaa haku- ja lisäysoperaatioita, mutta tyypillisesti sillä kustannuksella, että tietorakenne ei säilytä tietoa arvojen lisäysjärjestyksestä. Sama ilmiö esiintyy mm. Javan HashMap-tietorakenteen kanssa. Tämä vaikeuttaa jossain tapauksissa testaamista, koska sanakirjan sisällön järjestystä ei välttämättä tiedetä ennalta.

Onneksi Python 3:n viimeisimmissä versioissa sanakirja on toteutettu niin, että hajautuksesta huolimatta arvot pidetään lisäysjärjestyksessä. Python 3 saattaa helpottaa koodisi testaamista, koska postinumerot ovat aina lisäysjärjestyksessä!

### Python 3

Alla olevassa koodissa luodaan sanakirja `{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}`.

Python 3.8:lla arvot `[1, 2, 3, 4, 5]` sekä avaimet `['a', 'b', 'c', 'd', 'e']` saadaan aina siinä järjestyksessä, jossa ne annetaan sanakirjaa luotaessa:

```python
$ python3
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
>>> 
>>> print({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} # sama järjestys!
>>> 
>>> print({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.values())
dict_values([1, 2, 3, 4, 5]) # sama järjestys!
>>> 
>>> print({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.keys())
dict_keys(['a', 'b', 'c', 'd', 'e']) # sama järjestys!
```

### Python 2

Alla olevassa koodissa luodaan sanakirja `{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}`.

Python 2.7:lla arvot `[1, 3, 2, 5, 4]` sekä avaimet `['a', 'c', 'b', 'e', 'd']` saadaan **eri järjestyksessä**, kuin missä ne annetaan sanakirjaa luotaessa. Järjestys voi myös muuttua hajautustaulun luomisen jälkeen.

```python
$ python2 
Python 2.7.18rc1 (default, Apr  7 2020, 12:05:55) 
>>> 
>>> print({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4} # eri järjestys!
>>> 
>>> print({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.values())
[1, 3, 2, 5, 4] # eri järjestys!
>>> 
>>> print({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.keys())
['a', 'c', 'b', 'e', 'd'] # eri järjestys!
```

-->

## Tehtävän palauttaminen

Palauta koodaamasi testit sekä testattavat moduulit sellaisenaan, eli **ei pakattuna** Teamsissa olevaan palautuslaatikkoon **Teams-tehtävässä ilmoitettuun määräaikaan mennessä**.


# Seminaariaihe-ehdotukset

## Robot Framework

Perehdy [Robot Framework](https://robotframework.org/) -testaustyökaluun ja toteuta sillä testit, joilla varmistat esimerkiksi Ohjelmistoprojekti II -ryhmäsi projektin toimivuuden sen käyttöliittymän kautta.