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