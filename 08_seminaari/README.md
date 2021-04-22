# Seminaariaiheita

Tälle sivulle on koottu esimerkkiaiheita kurssin seminaaritehtävää varten. Voit melko vapaasti jalostaa ideoita vastaamaan omaa vaatimustasoasi ja kiinnostuksen kohteitasi.

## Python

* **Web-palvelu Pythonilla:**

    Python-aiheiset seminaarityöt voivat käsitellä esimerkiksi Pythonin [Django](https://www.djangoproject.com/)- tai [Flask](https://flask.palletsprojects.com/)-sovelluskehysten käyttöönottoa tai Pythonin tietokantaohjelmointiin perehtymistä.

* **Mikrokontrollerin ohjelmointi MicroPythonilla:**

    Keväälle 2021 tarjotaan myös mahdollisuus perehtyä ESP32-mikrokontrollerien ohjelmointiin [MicroPython](https://micropython.org/)-kielellä. Mahdollisia projekteja voivat olla esimerkiksi sääasema, peruutustutka, Telegram-bottina toteutettu  liiketunnistin tai nopeustesti-peli.


## Tietorakenteet ja algoritmit

* **Tunnetun algoritmin toteuttaminen:**

    Tutustu syvyyshakuun, rekursioon ja graafeihin ja toteuta syvyyshaku itse valitsemaasi aineistoon. Halutessasi voit esimerkiksi toteuttaa algoritmin, joka etsii tien ulos labyrintistä. Katso esim: https://en.wikipedia.org/wiki/Maze_solving_algorithm.

    Algoritmiaiheeseen sopii myös esimerkiksi minimax-algoritmilla toimiva ristinollaa pelaava botti: https://medium.com/ai-in-plain-english/coding-the-perfect-tic-tac-toe-bot-a0827e966a74

* **Vapaavalintaisen tietorakenteen toteuttaminen:**

    Toteuta esimerkiksi labyrintin tai sanaristikon generoiva algoritmi. Voit käyttää pohjana tunnettua valmista logiikkaa, josta teet oman toteutuksesi. Katso esim: https://en.wikipedia.org/wiki/Maze_generation_algorithm

    Huom! Kokonaista peliä ja sen käyttöliittymää ei tarvitse toteuttaa. Riittää, että algoritmi on jollain tavoin todennettavissa toimivaksi.


## Ohjelmistoarkkitehtuurit ja patternit

* **Ohjelmistoprojekti 2 refaktorointi:**
Refaktoroi ohjelmistoprojekti 2 -projektinne käyttämään mielestäsi optimaalista arkkitehtuuriratkaisua joiltain osin. Kuvaa tämä arkkitehtuuri myös kaaviona.

* **FRP-ohjelmointi:**

    Tutustu [FRP-ohjelmointiin](https://stackoverflow.com/questions/1028250/what-is-functional-reactive-programming/1030631#1030631) ja tee (tietynlainen) ohjelma RxJS:llä (tai bacon.js:llä). Myös [Node-RED](https://nodered.org/)-ympäristöä voi miettiä tähän vaiheeseen.

* **Mikropalvelu:**

    Mikropalveluihin perustuvan pienen palvelun rakentaminen (esim autentikointipalvelu pyörii omana palvelunaan).

## Testaus

* **Yksikkötestaus:**

    Testaa jokin osa ohjelmistoprojekti II -kurssin projektistanne yksikkötesteillä.

* **Järjestelmätestaus:**

    Tutustu [Robot Framework](https://robotframework.org/):iin, Cucumber:iin tai Selenium Framework:iin ja toteuta valitsemasi työkalun avulla yksinkertainen järjestelmätesti jollekin omalle tai julkiselle palvelulle.

    Mahdollinen lähde: https://www.theseus.fi/handle/10024/341637


## Infra ja automaatiotyökalut

* **Continuous Integration / Continuous Delivery:**

    Rakenna CI/CD monitorointi ja tuotantoputki ohjelmistoprojekti 2 -projektillenne.

* **Docker ja Docker Compose:**

    Rakenna Dockerin ja Docker composen avulla ohjelmistoprojekti 2 -projektistanne konttipohjainen sovellus, joka voidaan deployata Azureen tai AWS:ään.


## ES6, JavaScript, node (+MongoDB)

* **MERN-stack:**

    MongoDB (+ Mongoose), Express, React, Node. Huom! Toteuta ominaisuuksiensa puolesta pieni sovellus ja keskity opettelemaan jokin uusi tekninen asia, kuten MongoDB:n hyödyntäminen JavaScriptillä.

* **Reaktiivinen ohjelmointi JS:llä** *(ks. ohjelmistoarkkitehtuurit ja patternit)*:

    Tutustu [FRP-ohjelmointiin](https://stackoverflow.com/questions/1028250/what-is-functional-reactive-programming/1030631#1030631) ja tee (tietynlainen) ohjelma RxJS:llä (tai bacon.js:llä). Myös [Node-RED](https://nodered.org/)-ympäristöä voi miettiä tähän vaiheeseen.

* **Paketin julkaisu NPM:ssä:**

    Tutustu NPM-palvelun pakettien julkaisemiseen ja julkaise oma pieni paketti. Julkaistava paketti voi olla esimerkiksi asiakaskirjasto MyHelsinki Open API:n tapahtumien hakemiseksi. Asiakaskirjaston ominaisuuksiin voi kuulua erilaiset rajaukset tai järjestämiset päivämäärien mukaan tai vaikka rajaus tapahtumiin, joiden otsikossa tai kuvauksessa esiintyy tietty teksti.


## Koneoppiminen

* **Koneoppimismallin kouluttaminen:**

Kouluta koneoppimismalli jostain datasta ja laadi sillä ennusteita (esim. keraksella kuvien tunnistamista). Voi liittyä ohjelmistoprojekti 2:seen mieluusti.
    
* **Koneoppimistutkielma:**

Laadi tutkielma ja raportti siitä mitä koneoppiminen (ja esim neuroverkot) ovat ja mihin niitä voi hyödyntää. Voit syventyä myös esimerkiksi luonnollisen kielen tulkintaan (NLP) ja sanavektoreihin.

* **Vahvistusoppiminen:**

Kouluta vahvistusoppimisella (reinforcement learning) jonkin pelin tekoäly. Tässä esimerkiksi on [youtube-playlista](https://www.youtube.com/playlist?list=PLTWFMbPFsvz3CeozHfeuJIXWAJMkPtAdS), jolla koulutetaan tekoäly pelaamaan Segan Sonic the hedgehog -peliä [Open AI:n](https://openai.com/) ja [Neatin](https://neat-python.readthedocs.io/en/latest/neat_overview.html) avulla. 

## Azure tai vastaava pilvipalvelu

* **Koneoppiminen:**

    Build a machine learning model with some interesting data related to e.g. your software project assignment with the help of Azure machine learning studio. You can e.g. build a recommendation system with the help of k-means clustering. You can deploy your service as a Web API.

* **Azure Functions:**

    Toteuta jokin itsenäinen ominaisuus Ohjelmistoprojekti II -kurssisi projektin tueksi Azuren pilvifunktiona.
