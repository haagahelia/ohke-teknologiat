# Shiny for Python -sovellukset ja ajaminen selaimessa

Posit yhtiön rakentama Shinylive sivusto mahdollistaa **Shiny for Python** -sovellusten kehittämisen ja suorittamisen suoraan **verkkoselaimessa ilman Python-palvelinta**. Python-koodi (mukaan lukien Shiny- ja muut vaaditut kirjastot) ajetaan selaimessa käyttäen **WebAssemblya (WASM)** ja **Pyodidea**.

## Koodieditori ja esikatselu yhdessä

**Editori-näkymässä** voidaan muokata Python-koodia ja toisessa ikkunan ruudussa **esikatselu/ajettava sovellus** päivittyy automaattisesti, kun teet muutoksia. Tämä “live”-kokemus tekee koodin testaamisesta ja visualisoinnin tarkastelusta helppoa ja sujuvaa.

Jaettavia linkkejä voi käyttää esimerkiksi opetusmateriaaleissa, GitHub Gist -integraation kautta tai muissa tilanteissa, joissa koodi halutaan jakaa tai esitellä kevyesti.
* **Editor-URL**: Sisältää koodin ja editorin — ideaalinen yhteistyöhön tai koodin muokkaamiseen yhdessä.
* **App-URL**: Näyttää vain toimivan sovelluksen ilman editoria — esimerkiksi projektin jakamiseen käyttäjille.

## Staattinen deploy – ilman palvelinta

Shinylive-palvelin toimii ainoastaan **staattisena tiedostopalvelimena**, eikä siinä tarvitse ajaa Python-tai Shiny-engineä. Tämä mahdollistaa sovellusten jakamisen esim. GitHub Pagesilla, Netlifyllä tai muilla staattisia sivustoja tukevilla alustoilla.

## Vaivaton, skaalautuva ja turvallinen

* *Ei asennuksia*: Pythonia tai Shinyä ei tarvitse asentaa omalle koneelle.
* *Vaivaton jakaminen*: Sovellus toimii vain URL\:stä, ilman palvelininfrastruktuuria.
* *Helppo skaalautuvuus*: Sovellus skaalautuu käytännössä rajatta, koska palvelin ei kuormitu — laskenta tapahtuu käyttäjän selaimessa.
* *Parempi tietoturva*: API\:t ja koodi eivät ole palvelimella, vaan ajettuna selaimessa, jolloin riski haavoittuvuuksiin on vähäisempi.

## Rajoitukset

* *Kirjasto-rajoitteet*: Pyodide ei tue kaikkia Python-kirjastoja.
* *Latausaika*: Sovelluksen lataus saattaa olla hitaampi, koska Pythonin ja pakettien lataus tapahtuu selaimessa (yksi kerta, selain voi kuitenkin välimuistittaa).
* *Laskentateho riippuu käyttäjästä*: Tehokkaat laskutoimitukset voivat hidastaa suorituskykyä, sillä ne tehdään käyttäjän koneella.
* *Ei salaisia tietoja*: Koska koodi lähetetään selaimelle, sitä ei voi pitää piilossa — käyttö esimerkiksi luottamuksellisten datojen käsittelyyn vaatii harkintaa.

## Linkkejä lähteisiin

* [Shinylive: Shiny + WebAssembly – Shiny for Python - Posit](https://shiny.posit.co/py/get-started/shinylive.html)
* [How to Run Shiny for Python Apps Without a Python Server](https://www.appsilon.com/post/shiny-for-python-shinylive)


Loistavaa! Teen sinulle nyt **yksityiskohtaisen ohjeistuksen opiskelijoille**, jossa käydään läpi askel askeleelta, miten tehtävä voidaan tehdä: CSV-datan lukemisesta Shiny + Plotly -kaavion tekemiseen.

---

# Tehtävän ohjeistus: Väestökaavioiden tekeminen Shinyllä ja Plotlyllä

### **Tavoite**

Tehtävänä on tehdä interaktiivinen Python-Shiny-sovellus, jossa käyttäjä voi valita maan ja nähdä sen väestön kehityksen vuosien yli Plotly-kuvaajana.

CSV-datana käytetään tiedostoa GM-population-dataset (gm_pop.csv), jossa sarakkeet ovat:

```
geo;name;1800;1801;1802;...;2100
afg;Afghanistan;3280000;3280000;3280000;...
```

---

## **Vaihe 1: Tuo tarvittavat kirjastot**

```python
import pandas as pd
import plotly.express as px
from shiny.express import render, input, ui
from shinywidgets import render_plotly
from shiny import reactive
```

* `pandas` → datan käsittely
* `plotly.express` → kaavioiden piirtäminen
* `shiny` → interaktiivinen web-sovellus johon plottereita voidaan piirtää

---

## **Vaihe 2: Lue CSV ja tarkista data**

```python
# Huom: CSV:n erotin on puolipiste
from pathlib import Path

infile = Path(__file__).parent / "data.csv"
df = pd.read_csv("data.csv", sep=";")

# Tarkista sarakkeet ja muutama rivi
print(df.columns[:10])
print(df.head())
```

Tarkista, että ensimmäiset sarakkeet ovat `"geo"`, `"name"` ja sen jälkeen vuosiluvut.

---

## **Vaihe 3: Etsi vuosikolumnit ja muunna pitkäksi muodoksi**

```python
import re

# Valitse sarakkeet, jotka ovat nelinumeroisia vuosia
year_columns = [row for row in dff if re.fullmatch(r"\d{4}", row)]
print(year_columns)
```

---

## **Vaihe 4: Tee Shiny-käyttöliittymä**

```python
with ui.layout_columns():
    ...
    @render_plotly
    def plot_pop():
        infile = Path(__file__).parent / "data.csv"
        df = pandas.read_csv(infile, sep=";")
        dff = df[df["name"] == input.country()]
        year_columns = [row for row in dff if re.fullmatch(r"\d{4}", row)]
        df_long = dff.melt(
            id_vars=["geo", "name"],   # nämä pysyvät riveillä
            value_vars=year_columns,   # nämä sarakkeet muutetaan riveiksi
            var_name="year", 
            value_name="population"
        )
        return px.scatter(df_long, x=year_columns, y="population", title=f"{input.country()} - Väestönmäärä")
```

* `ui.input_select` → alasvetovalikko maiden valitsemiseen
* `ui.output_ui` → paikka, johon kaavio renderöidään
