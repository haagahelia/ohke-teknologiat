# Python

Oppitunnilla tavoitteemme on päästä vauhtiin Python-koodin kirjoittamisessa. Tavoitteena ei ole oppia kielen syntaksia tai rakenteita ulkoa, vaan saada käsitys työvaiheista ja saatavilla olevista hyvistä tietolähteistä, jotta pääsette konkreettisesti kirjoittamaan koodia.

Kurssilla käsittelemme Pythonia vertaillen sitä jo valmiiksi tuntemaamme Java-kieleen ja Javan standardikirjastoon.

Jos haluat päästä nopeasti vauhtiin, voit lukea esimerkiksi tutoriaalin ["Learn Python in 10 minutes"](https://www.stavros.io/tutorials/python/).

Laajempia ja laadukkaita oppimateriaaleja löytyy mm. seuraavista lähteistä:

* Lappeenrannan Yliopiston Python 3 –ohjelmointiopas: https://lutpub.lut.fi/handle/10024/162088
* Pythonin oma "The Python Tutorial": https://docs.python.org/3/tutorial/
* Mooc.fi:n Ohjelmoinnin perusteet Pythonilla -kurssi: https://python-k20.mooc.fi/

<!--## Oppitunnin tallenteet

[Osa 1: kurssin yleiset käytännöt ja johdanto 1. tehtävään](https://web.microsoftstream.com/video/3984ea5c-7782-484c-af51-ce6d50b049ad)

[Osa 2: Python-ohjelmointi](https://web.microsoftstream.com/video/bff8f1a1-025d-4c13-8287-7721032be43c)

[Lähdekoodit](src/)-->

# Oppitunnin aiheet

* Python-koodin suorittaminen ja kirjoittaminen
* Tietotyypit
* Ehto- ja toistorakenteet
* Funktiot
* Json
* Http-pyynnöt
* Sanakirjat

# Koodaustehtävä (luonnos)

Tämän koodaustehtävän tavoitteena on luoda pohja seuraavien viikkojen tehtäville, joissa käsittelemme dataa ja testaamme ohjelmistoja Python-kielellä. Kaikkien mahdollisten Pythonin rakenteiden opetteleminen etukäteen ei ole kurssin kannalta tarkoituksenmukaista, mutta tehtäväksi on valittu sellainen, jonka kautta opimme seuraavista Pythonin rakenteista:

* ehtolauseet
* toisto
* listat
* sanakirjat (dict)
* merkkijonot
* JSON

Tehtävien tausta-aineistona käytämme GitHubissa julkaistua postinumeroaineistoa, jonka tarkemmat ohjeet löytyvät alempana tästä dokumentista.

Tehtävät saa ratkaista yhteistyössä kaverin kanssa, mutta molempien on osallistuttava aktiivisesti ongelmien ratkaisemiseen ja palautettava omat ratkaisunsa. 

Tehtävien toimintalogiikan ja käyttöliittymän ei tarvitse noudattaa täsmällisesti annettuja esimerkkejä, mutta toimintaidean tulee olla samankaltainen.


## Tehtävien arviointi

Hyväksyttyyn suoritukseen sinun ei tarvitse toteuttaa kumpaakaan tehtävää täydellisesti. Palauta siis ohjelmat siinä kunnossa mihin saat ne toteutettua. Arviointi skaalataan suuntaa-antavasti siten, että ensimmäisen tehtävän ratkaisulla saat arvosanan 3 ja molemmat tehtävät ratkaisemalla arvosanan 5.


## Tehtävä 1

Kirjoita Python-kielinen ohjelma `postitoimipaikka.py`, joka kysyy  käyttäjältä postinumeron ja kertoo, mihin postitoimipaikkaan kyseinen postinumero kuuluu. 

Tehtävän ratkaisemiseksi sinun tulee kysyä käyttäjältä syötettä ja etsiä postinumeroaineistosta syötettä vastaava arvo. Voit joko tallentaa postinumeroaineiston koneellesi ja [lukea sen levyltä](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) tai toteuttaa ohjelmasi [lukemaan tiedoston suoraan verkosta](https://docs.python.org/3/howto/urllib2.html).

Esimerkkisuoritus:

    $ python3 postitoimipaikka.py
    
    Kirjoita postinumero: 00100
    HELSINKI

## Tehtävä 2

Kirjoita Python-kielinen ohjelma `postinumerot.py`, joka kysyy käyttäjältä postitoimipaikan nimen, ja listaa kaikki kyseisen postitoimipaikan postinumerot.

Tehtävän voi ratkaista useilla tavoilla, joten käytä hetki ongelman pohtimiseen ennen kuin ryhdyt koodaamaan. Olisiko esimerkiksi helpompaa jäsentää postinumeroaineisto etukäteen uudenlaiseksi tietorakenteeksi, vai käydä avain-arvo-pareja läpi yksi kerrallaan postinumeroiden löytämiseksi. Seuraavalla viikolla käsittelemme hieman lähemmin tietorakenteiden ja algoritmien suunnittelua ja tehokkuutta.

Esimerkkisuoritus:

    $ python3 postinumerot.py

    Kirjoita postitoimipaikka: Porvoo
    Postinumerot: 06100, 06401, 06151, 06150, 06101, 06500, 06450, 06400, 06200

Yritä toteuttaa ohjelma siten, että syötetyn postitoimipaikan kirjainkoolla ei ole merkitystä. Huolehdi myös siitä, että tuntemattoman nimen syöttäminen ei kaada ohjelmaa.


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

> *Data on postin ja sitä koskee kaikki http://www.posti.fi/liitteet-yrityksille/ehdot/postinumeropalvelut-palvelukuvaus-ja-kayttoehdot.pdf dokumentin käyttöehdot.*
>
> *JSON-muunnokset ovat vapaasti käytettävissä ja muunneltavissa.*
>
> Lähde: https://github.com/theikkila/postinumerot

## Lähteitä

Pythonin dict-tietorakenne, eli sanakirja, muistuttaa Javan map-tietorakennetta. Tulet tarvitsemaan sanakirjaa tausta-aineiston käsittelemisessä: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Tiedoston lataaminen verkosta onnistuu esim Python 3: standardikirjastoon kuuluvalla `urllib`-kirjastolla: https://docs.python.org/3/howto/urllib2.html.

JSON-muotoisen merkkijonon parsiminen Pythonin listoiksi, sanakirjoiksi ja muiksi tietorakenteiksi onnistuu standardikirjaston `json`-kirjastolla: https://docs.python.org/3/library/json.html

## Tehtävien palauttaminen

Palauta koodaamasi lähdekooditiedostot sellaisenaan, eli **ei pakattuna** Teamsissa olevaan palautuslaatikkoon seuraavaan oppituntiin mennessä.
