# Postinumerot-tehtävien malliratkaisut

Tehtävien malliratkaisuissa käsitellään lukuisia asioita, joita ei Python-oppitunnilla käsitelty ja joita ei odotettu tai toivottu huomioitavan vielä omissa tehtäväpalautuksissa. 

Vaihtoehtoisten toteutustapojen ja aiheen syventävämmän käsittelyn tavoitteena on, että myös ne, jotka saivat tehtävän täysin oikein, hyötyisivät ongelmien käsittelemisestä vaihtoehtoisista näkökulmista.

## `postitoimipaikka.py`

> *Kirjoita Python-kielinen ohjelma postitoimipaikka.py, joka kysyy käyttäjältä postinumeron ja kertoo, mihin postitoimipaikkaan kyseinen postinumero kuuluu.*

Tämä toteutus ratkaisee tehtävän suoraviivaisesti, mutta on toteutettu ongelmallisesti. Moduulitasolle kirjoitettu koodi tekee logiikan testaamisesta hankalaa. `hae_postinumerot`-funktio voisi olla hyödyllinen myös toisessa Python-moduulissa, mutta moduulitasolle toteutettu logiikka estää tämän funktion hyödyntämisen toisesta moduulista:

```python
import urllib.request
import json

def hae_postinumerot():
    # https://docs.python.org/3/howto/urllib2.html
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        # https://docs.python.org/3/library/json.html
        return json.loads(response.read())

postinumerot = hae_postinumerot()

postinumero = input('Kirjoita postinumero: ').strip()

if postinumero in postinumerot:
    postitoimipaikka = postinumerot[postinumero]
    print(postitoimipaikka.title())
else:
    print('Postitoimipaikkaa ei löytynyt :(')
```

Parannellussa versiossa aineiston hakeminen, syötteen kysyminen ja muu logiikka on kirjoitettu omaan `main`-funktioonsa. Funktiota kutsutaan moduulin lopussa, mikäli ohjelma on käynnistetty tästä moduulista:

```python
if __name__ == '__main__':
    main()
```

Voit tutustua `__name__`-muuttujaan ja sen `__main__`-erikoisarvoon esimerkiksi osoitteessa https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3.

```python
import urllib.request
import json

def hae_postinumerot():
    # https://docs.python.org/3/howto/urllib2.html
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        # https://docs.python.org/3/library/json.html
        return json.loads(response.read())

def main():
    postinumerot = hae_postinumerot()

    postinumero = input('Kirjoita postinumero: ').strip()

    if postinumero in postinumerot:
        postitoimipaikka = postinumerot[postinumero]
        print(postitoimipaikka.title())
    else:
        print('Postitoimipaikkaa ei löytynyt :(')

# main-funktio suoritetaan vain, jos tämä moduuli on "pääohjelma"
if __name__ == '__main__':
    main()
```

## `postinumerot.py`

> *Kirjoita Python-kielinen ohjelma postinumerot.py, joka kysyy käyttäjältä postitoimipaikan nimen, ja listaa kaikki kyseisen postitoimipaikan postinumerot.*

Tässä tehtävässä tarkoituksena oli herättää ajatuksia siitä, kannattaako annettua kaupunkia etsiä esimerkiksi toistorakenteella, vai kannattaisiko annettu dict-tietorakenne muuttaa toiseen muotoon, josta halutut tiedot selviäisivät suoraan.

Ensimmäisessä ratkaisuversiossa postinumeroiden hakeminen on toteutettu "imperatiivisesti", eli käymällä tietorakenne toistorakenteen avulla läpi ja poimimalla yksi kerrallaan ehdot täyttäviä postinumeroita uudelle listalle:

```python
from postitoimipaikka import hae_postinumerot


def main():
    numerot_ja_toimipaikat = hae_postinumerot()

    etsittava = input('Kirjoita postitoimipaikka: ').strip().upper()

    loydetyt = []

    for postinumero, toimipaikka in numerot_ja_toimipaikat.items():
        if etsittava == toimipaikka:
            loydetyt.append(postinumero)

    if loydetyt:
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
```

Yllä oleva ratkaisu toimii ja toteuttaa tehtävänannon. Python-kielessä on kuitenkin myös muita tapoja rakentaa tietorakenteita, kuten listoja ja sanakirjoja. Pystymmekin toteuttamaan postinumeroiden valitsemisen listalle "deklaratiivisemmalla" lähestymistavalla, hyödyntäen list comprehension -syntaksia:

> *List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.*
>
> *https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions*

```python
loydetyt = [
    numero for numero, toimipaikka in numerot_ja_toimipaikat.items()
    if toimipaikka == etsittava
]
```

Tämän tehtävän kannalta yllä esitetyt ratkaisut ovat tarkoituksenmukaisia ja nopeita, mutta mikäli ohjelmassa kysyttäisiin useita eri postitoimipaikkoja, tulisi alkuperäinen liki 5000 alkion tietorakenne käydä kokonaisuudessaan läpi jokaista käyttäjän syötettä varten. Myöhempiä hakuja voidaan nopeuttaa huomattavasti jäsentämällä sanakirja ensin toiseen muotoon, jossa avaimina ovat toimipaikkojen nimet ja avaimina lista postinumeroista:

```json
{
  "SALO": [ "24102", "24280", "24100", "24101", "24130", "24240", "24260" ],
  "LASSILA": [ "29680" ],
  "KELTAKANGAS": [ "46860" ],
  "NAUVO": [ "21661", "21660" ]
}
```

Tästä tietorakenteesta voidaan hakea yhtä toimipaikan nimeä vastaavat postinumerot erittäin nopeasti myös useita kertoja:

```python
from postitoimipaikka import hae_postinumerot


def main():
    numerot_ja_toimipaikat = hae_postinumerot()

    toimipaikat_ja_numerot = {}

    for numero, toimipaikka in numerot_ja_toimipaikat.items():
        # alustetaan toimipaikka, jos sitä ei ole vielä sanakirjassa:
        if toimipaikka not in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka] = []

        toimipaikat_ja_numerot[toimipaikka].append(numero)

    etsittava = input('Kirjoita postitoimipaikka: ').strip().upper()

    if etsittava in toimipaikat_ja_numerot:
        postinumerot = toimipaikat_ja_numerot[etsittava]
        print('Postinumerot: ' + ', '.join(postinumerot))
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
```