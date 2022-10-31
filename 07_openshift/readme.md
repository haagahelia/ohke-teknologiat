# Dockerin hyödyntäminen paikallisesti sekä pilvessä

Tämän oppitunnin demossa luodaan kontteja Python- ja JS-sovelluksille, joita julkaistaan Docker-konttirekisterissä sekä OpenShift-pilvessä.

Kokonaisuutena pilvipalveluiden infrastruktuuri on erittäin laaja, ja siitä riittäisi asiaa useammaksikin kurssiksi. Tällä oppitunnilla on tarkoitus tutustua terminologiaan ja työvaiheisiin siinä määrin, että aiheiden parissa on mahdollista jatkaa itseopiskelua esimerkiksi seminaarityön puitteissa.


## Miksi ajaa sovelluksia konteissa?

> *"Rakkaalla lapsella on monta nimeä: kontti, säiliö, docker, virtualisointiympäristö, eristetty itsenäinen prosessi… Asian ymmärtämiseksi ei kuitenkaan tarvitse olla koodari tai sysadmin.*
>
> *Kontit ovat virtuaalipalvelimia huomattavasti kevyempi ja joustavampi tapa paketoida ja ajaa Windows- ja Linux-sovelluksia. Ne ovat tekniikka sovellusten kehittämiseen, julkaisemiseen ja ylläpitämiseen. Kontit ovat tulleet korvaamaan virtuaalipalvelimet ja Gartnerin arvion mukaan 75 % yrityksistä käyttää vuoden 2022 loppuun mennessä kontteja ohjelmistojen ajamiseen.*
>
> *Konttia voi luonnehtia itsenäiseksi ohjelmistoksi, jota voi ajaa joustavasti niin omalla työasemalla, rautapalvelimella, virtuaalipalvelimella tai pilvessä sellaisenaan ilman ohjelmiston koodiin tarvittavia muutoksia. Se toimii kaikissa ympäristöissä samalla tavalla, koska se on eriytetty prosessitasolla ja sillä on oma tiedostojärjestelmä."*
>
> Otaverkko. OpenShift palveluna. https://otaverkko.fi/palvelukategoria/openshift/



## Oppitunnin videot

1. [Konttien luonti, käyttäminen ja peruskäsitteet](https://web.microsoftstream.com/video/a542ef0a-fc3e-41b3-aab8-0e734bc75050) *55:31*

2. [Konttien julkaisu konttirekisterissä ja verkkopalveluna](https://web.microsoftstream.com/video/b0490fff-c024-4882-94ec-a99859d1f620) *50:30*

3. [Konttien hyödyntäminen kehitysympäristössä](https://web.microsoftstream.com/video/81928ca0-8a61-4aea-a495-5e0d8851a8bf) *12:57*


## Missä näitä teknologioita käytetään?

Tällä viikolla käsiteltävät teknologiat ovat yleistyneet hyvin nopeasti, ja kaikki suurimmat pilvipalvelualustat tarjoavat omat palvelunsa niiden käyttämiseksi. Lisätietoa eri pilvialustojen palveuista löydät esimerkiksi seuraavista lähteistä:

Docker-konttirekistereitä (container registry)

* Docker hub: https://hub.docker.com/
* Azure Container Registry: https://azure.microsoft.com/en-us/services/container-registry/
* Google Container Registry: https://cloud.google.com/container-registry
* Amazon Elastic Container Registry: https://aws.amazon.com/ecr/
* GitHub packages: https://github.com/features/packages


Kubernetes-pilviratkaisuja

* Azure Kubernetes Service: https://azure.microsoft.com/en-us/services/kubernetes-service/
* Amazon Elastic Kubernetes Service: https://aws.amazon.com/eks/
* Google Kubernetes Engine: https://cloud.google.com/kubernetes-engine
* CSC Rahti: https://rahti.csc.fi/


## Kurssin yksityinen pilvi

Kurssilla on käytössä [Otaverkon tarjoama OpenShift-ympäristö](https://otaverkko.fi/palvelukategoria/openshift/), eli "yksityinen pilvi". Yksityinen pilvi tarkoittaa tässä sitä, että käyttöömme on varattu skaalautuva alusta, jonne voimme luoda uusia palveluita hyvin joustavasti.

> *"OpenShift on sovelluskehittäjien palvelualusta, joka on ratkaisu sovelluskehitysympäristöjen automatisointiin ja konttien hallintaan. Saat DevOps-tiimisi tarvitsemat työkalut, eikä asiakkaasi tarvitse tehdä ohjelmistoprojekteissasi valintaa laadun ja nopeuden välillä."*
>
> Otaverkko. OpenShift palveluna. https://otaverkko.fi/palvelukategoria/openshift/

Ohjeet käyttäjätunnusten saamiseksi löytyvät kurssin Teams-kanavalta.

OpenShift-konsoliin kirjautuminen onnistuu selaimella osoitteessa https://console-openshift-console.apps.hhocp.otaverkko.fi/. Palveluissamme on valitettavasti toistaiseksi self-signed sertifikaatit, eli on odotettua, että selain varoittaa epäluotettavasta sertifikaatista.

Kirjautumisen jälkeen ensimmäinen työvaihe kirjautumisen jälkeen on tyypillisesti oman projektin luominen. Projekti luodaan oppitunnin 2. videolla.

Konttirekisteri löytyy osoitteesta `default-route-openshift-image-registry.apps.hhocp.otaverkko.fi`. Rekisteri ei ole käytettävissä selaimella, vaan sitä käytetään `docker`-komennon kautta (vaihtoehtoisesti `podman`). Lisätiedot esimerkkeineen ja OAuth-ohjeistuksineen löydät alempaa ja oppitunnin tallenteelta.

Voit tarvittaessa ottaa ssh-yhteyden ympäristömme kuormantasaajaan osoitteella `hhocp.otaverkko.fi`. Kuormantasaajalta löytyy `oc`- ja `kubectl`-komennot, joita voit tarvita mahdollisesti edistyneempien operaatioiden parissa seminaarityössä.


## Mikä on kontti?

> *"Containers are a technology based on operating system kernel features that allow the creation of isolated environments sharing a kernel. For example, container features make it possible to have several isolated root filesystems, network stacks and process trees that all use the same kernel. These isolated environments are similar in functionality to lightweight virtual machines, but there are some key differences between virtual machines and containers. The biggest one is that virtual machines always have their own kernels, while containers share the host system's kernel."*
>
> https://docs.csc.fi/cloud/rahti/containers/

**Seuraavat käsitteet käsitellään oppitunnin videotallenteilla:**

* Image
* Container
* Volume
* Image stream
* Container Registry (paremminkin Container Image Registry)


## Mikä on Kubernetes?

> *"The power of Kubernetes (and OpenShift) is in the relatively simple abstractions that they provide for complex tasks such as load balancing, software updates for a distributed system, or autoscaling"*
>
> https://docs.csc.fi/cloud/rahti/concepts/


**Seuraavat käsitteet käsitellään oppitunnin videotallenteilla:**

* Service
* Pod
* Container
* Volume


# Docker-kontti Python-sovellukselle

Tässä esimerkissä jatkokehitämme "sorting and filtering" -tehtävässä kehitettyä logiikkaa ja toteutamme [Flask](https://flask.palletsprojects.com/):in avulla ohjelmallemme http-rajapinnan. Esimerkin lähtötilanne löytyy tiedostosta [upcoming_events.py](https://gist.github.com/swd1tn002/8f2e49c5b416671856d31c40b0d0c521).

Dockerin dokumentaatiossa https://docs.docker.com/language/python/build-images/ on suoraviivainen kuvaus vaiheista, joita seuraamme seuraavaksi.

## 1. Flaskin käyttöönotto ja app.py

```python
from flask import Flask, jsonify
from upcoming_events import filter_next_month, get_events, quicksort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/api/events')
def events_next_month():
    all_events = get_events()
    next_month = filter_next_month(all_events)
    sorted_events = quicksort(next_month)

    return jsonify(sorted_events)
```

Flask voidaan käynnistää komennolla:

    $ python3 -m flask run


Tämän jälkeen palvelimen pitäisi vastata osoitteissa http://localhost:5000 ja http://localhost:5000/api/events.


## 2. Dockerfile:n luonti

Dockerfile:n komennot on kuvailtu rivikohtaisesti ohjeessa https://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-python.

Tuloksena syntyy seuraavankaltainen tiedosto:

```dockerfile
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
```

Imagen ("levykuva") luonti onnistuu nyt komennolla:

    docker build --tag flask-events .

Kun image on valmis, se löytyy `image ls`-listauksesta:

    docker image ls

Image voidaan nyt käynnistää uudessa kontissa seuraavasti:

    docker run -it --rm -p 5000:5000 flask-events

Käynnistyskomennossa käytetyt parametrit on selitetty dokumentaatiossa seuraavasti:

**-it**

> *"For interactive processes (like a shell), you must use `-i` `-t` together in order to allocate a tty for the container process. `-i` `-t` is often written `-it` as you’ll see in later examples."*
>
> https://docs.docker.com/engine/reference/run/

**--rm**

> *"By default a container’s file system persists even after the container exits. This makes debugging a lot easier (since you can inspect the final state) and you retain all your data by default. But if you are running short-term foreground processes, these container file systems can really pile up. If instead you’d like Docker to automatically clean up the container and remove the file system when the container exits, you can add the --rm flag"*
>
> https://docs.docker.com/engine/reference/run/#clean-up---rm

**-p 5000:5000**

> *"To expose a container’s internal port, an operator can start the container with the -P or -p flag. The exposed port is accessible on the host and the ports are available to any client that can reach the host."*
>
> https://docs.docker.com/engine/reference/run/#expose-incoming-ports

Kun kontti on käynnissä se näkyy komennolla:

    docker container ls --all

Jos kontteja jää "roikkumaan" taustalle, niitä voidaan poistaa komennolla:

    docker container rm KONTTI


### Tiedostojen jättäminen imagen ulkopuolelle (dockerignore)

Yllä esitetyssä esimerkissä `COPY . ./` kopioi **kaikki** nykyisen hakemiston tiedostot luotavalle imagelle. Tämä voi olla monessa tapauksessa erittäin epätoivottavaa, koska työhakemisto saattaa sisältää esimerkiksi `.env`-tiedostoja, joissa esiintyy salaisuuksia, tai `node_modules`- tai `target`-hakemistoja, jotka on tarkoitus luoda kontin luonnin yhteydessä osana buildia.

Tiedostoja voidaan jättää imagen ulkopuolelle `.dockerignore`-tiedoston avulla, joka toimii monella tavoin samoin kuin `.gitignore`. Voit lukea tiedostosta lisää Dockerin dokumentaatiosta: https://docs.docker.com/engine/reference/builder/#dockerignore-file.

Tiedosto voi kielestä ja käytetyistä teknologioista riippuen sisältää esim. seuraavia rivejä:

```
.git
.vscode
.gitignore
.env
node_modules
target
```

Vinkki: `.dockerignore`-tiedostoa luodessasi voi olla hyvä katsoa, mitä projektin `.gitignore`-tiedostossa on jo listattuna.


## 3. Imagen julkaisu konttirekisterissä

Ennen julkaisua imagelle on tarpeen lisätä tagi, joka vastaa sen sijaintia konttirekisterissä: https://docs.docker.com/engine/reference/commandline/tag/. Konttirekisterissä osoite sisältää projektin nimen, joten varmista että olet luonut itsellesi projektin OpenShiftiin ja että käytät samaa nimeä. Projektin nimen jälkeen tuleva imagen nimi on vapaavalintainen.

Kurssin OpenShift-pilven konttirekisteri sijaitsee osoitteessa `default-route-openshift-image-registry.apps.hhocp.otaverkko.fi`.

Seuraava esimerkki näyttää miten `login`, `tag` ja `push` toimivat `oauth-openshift.apps.hhocp.otaverkko.fi`-rekisterin kanssa:

    # 1. Kirjautuminen konttirekisteriin.
    # Salasanan sijasta käytetään OAuth-tokenia, jonka saat 
    # osoitteesta https://oauth-openshift.apps.hhocp.otaverkko.fi/oauth/token/request
    docker login default-route-openshift-image-registry.apps.hhocp.otaverkko.fi

    # 2. Tagin lisääminen aikaisemmin luodulle imagelle.
    # Uudessa tagissa on mukana konttorekisterin URL, projekti ja imagen nimi:
    docker tag flask-events default-route-openshift-image-registry.apps.hhocp.otaverkko.fi/PROJEKTI/IMAGE:latest

    # 3. Julkaisu
    docker push default-route-openshift-image-registry.apps.hhocp.otaverkko.fi/PROJEKTI/IMAGE:latest

⚠ **Huom!** Koska konttirekisteri käyttää itse allekirjoitettua sertifikaattia, Docker ei oletuksena suostu muodostamaan siihen yhteyttä. Tämä on saatu kierrettyä oppitunnin esimerkissä lisäämällä tiedostoon `C:\Users\TUNNUS\.docker\daemon.json` uusi attribuutti nimeltä `insecure-registries`:

```json
{
    "insecure-registries": [
        "default-route-openshift-image-registry.apps.hhocp.otaverkko.fi"
    ]
}
```

Lisätiedot tästä ratkaisusta löydät osoitteesta https://docs.docker.com/registry/insecure/#deploy-a-plain-http-registry. Asetusten muuttamisen jälkeen Docker tulee käynnistää uudelleen.

🔐 **Huom!** Kirjautumisessa käytetään salasanan sijasta OAuth-tokenia, jonka saat selville osoitteesta https://oauth-openshift.apps.hhocp.otaverkko.fi/oauth/token/request. Lisätiedot löydät oppitunnin 2. videolta.


## 4. Kontin deployment OpenShiftissä

1. Projektin luonti

    *An OpenShift project is an alternative representation of a Kubernetes namespace.*

2. Resurssin lisääminen projektiin

    *Deploy an existing Image from an Image registry or **Image stream tag***

3. Esimerkki jatkuu oppitunnin videotallenteessa...


# Konttien lisääminen OpenShiftin katalogista

https://catalog.redhat.com/software/containers/search

Katalogista löydät esimerkiksi valmiin pohjan MySQL-tietokantaa tai muita tyypillisiä tietokantoja varten.


# Continuous integration, rolling deployment, autoscaling etc.

> *"Image streams provide a means of creating and updating container images in an on-going way. As improvements are made to an image, tags can be used to assign new version numbers and keep track of changes."*
>
> [Managing image streams. docs.openshift.com](https://docs.openshift.com/container-platform/4.10/openshift_images/image-streams-manage.html)

> *"A rolling deployment slowly replaces instances of the previous version of an application with instances of the new version of the application. The rolling strategy is the default deployment strategy used if no strategy is specified on a DeploymentConfig object.*
>
> *A rolling deployment typically waits for new pods to become ready via a readiness check before scaling down the old components. If a significant issue occurs, the rolling deployment can be aborted."*
>
> [Deployment strategies. docs.openshift.com](https://docs.openshift.com/container-platform/4.10/applications/deployments/deployment-strategies.html#deployments-rolling-strategy_deployment-strategies)


# Node.js-esimerkki

Node.js esimerkkiprojekti: https://github.com/nodeshift-starters/devfile-sample

Tämän kurssin esimerkit:

* Users & Posts: https://github.com/swd1tn002/express-oppitunti-2022/
* Node.js postalcodes: https://github.com/swd1tn002/nodejs-postalcodes/

Konttien luominen "käsin" ei ole aina, erityisesti pienten esimerkkien kanssa välttämätöntä, vaan voimme käyttää myös "Source-to-image"-strategiaa:

> *"You can use the Red Hat Software Collections images as a foundation for applications that rely on specific runtime environments such as Node.js, Perl, or Python. Special versions of some of these runtime base images are referred to as Source-to-Image (S2I) images. With S2I images, you can insert your code into a base image environment that is ready to run that code."*
>
> [Source-to-image. docs.openshift.com](https://docs.openshift.com/container-platform/4.10/openshift_images/using_images/using-s21-images.html)


# Tehtävä

Tämä on kurssin viimeinen viikkotehtävä, ja sen saa halutessaan tehdä yksin, parin kanssa tai ryhmässä. Tehtävässä ei ole tarkkaa toiminnallista vaatimusta, joten voitte soveltaa aiheita sen mukaan, oletteko enemmän kiinnostuneita esimerkiksi Dockerista tai Kuberneteksesta, tai haluatteko kokeilla esimerkiksi oman sovelluksen julkaisua PaaS-palvelussa. Mikäli teette työn ryhmässä, merkitkää raporttiinne selvästi kaikki tekijät. Mikäli jaoitte työtä eri kirjoittajien kesken, eritelkää kuka teki minkäkin vaiheen.

Tehtävänä on soveltaa yllä ja videoissa käsiteltyjä aiheita oman sovelluksen kanssa esimerkiksi julkaisemalla oma tai ryhmän harjoitustyö konttirekisterissä tai OpenShift-alustalla. Julkaistava sovellus voi olla esimerkiksi jokin tämän kurssin viikkoharjoituksista, ohjelmistoprojekti II:lla kehitettävä projekti tai palvelinohjelmointi- tai fronttikurssin harjoitustyö.

Tehtävää tehdessäsi kirjaa itsellesi ylös eri työvaiheet, käyttämäsi komennot sekä hyödyntämäsi nettilähteet. Oletettavaa on, että kaikki työvaiheet eivät tule onnistumaan ensimmäisellä yrityksellä, joten kirjaa eri välivaiheet ja niistä oppimasi asiat. Kirjaa myös ylös osoitteet, joista julkaisemasi Docker image tai web-palvelu on tarkasteltavissa tehtävän arvioinnin yhteydessä, mikäli sait julkaisun tehtyä valmiiksi.

Palauta lopuksi kirjoittamasi raportti Teamsiin. Raportti voi olla muodoltaan tekstitiedosto (md, txt) tai pdf, eikä sen tarvitse noudattaa erityistä raportointiohjetta. Käytetyt lähteet tulee kirjata (esim. tutoriaalit, tekniset dokumentit, stack overflow), mutta lähdeviitteet ovat täysin vapaamuotoisia. Kuvankaappausten käyttäminen raportissa voi olla hyvä idea. Jos haluat, voit toteuttaa raportin myös osana GitHub-repositoriota, jolloin riittää, että palautat Teamsiin linkin repositorioosi.

## Arviointi

Tehtävän arviointi perustuu tehtävässä opittuihin asioihin. Raportit, joissa opiskelija tai ryhmä selvästi osoittaa oppineensa uusia asioita ja soveltaneensa niitä käytännössä, arvioidaan oletuksena arvosanalla 5.

Raportit, joissa on selvästi tehty erilaisia osin satunnaisia kokeiluja, mutta opitut asiat ovat heikosti yksilöitävissä, arvioidaan oletuksena arvosanalla 3.

Huomatkaa, että sovelluksen julkaisun ei tarvitse lopulta onnistua, vaan täydet pisteet voi saada myös tilanteessa, jossa yritys on epäonnistunut, mutta siitä on selvästi opittu ja tehdyt vaiheet on raportoitu asianmukaisesti.

Tehtävän ratkaisu voi olla teknisesit ja laajuudeltaan hyvinkin yksinkertainen, eli sen ei tarvitse tavoitella esimerkiksi tunnilla esitettyjen esimerkkien laajuutta. Voit halutessasi jatkaa aiheen parissa työskentelyä kurssin seminaariosuudessa.


## Vaihtoehtoisia ideoita tehtävään

Seuraavat ovat vaihtoehtoisia ideoita, joita voit soveltaa vapaasti. Jos Ohjelmistoprojekti II -kurssin projektinne ei sovellu tehtävään, voit käyttää sen sijaan muilla kursseilla kehittämiäsi projekteja.

**1. Luo Docker-levykuva Ohjelmistoprojekti II -projektinne backendistä**

Luo tarvittava Dockerfile-tiedosto, joka asentaa ja käynnistää esimerkiksi projektikurssinne backend-sovelluksen. Voit julkaista Docker-levykuvan esimerkiksi [Docker hub](https://hub.docker.com/) -palvelussa, mutta se ei ole välttämätöntä, mikäli pystyt osoittamaan hyvää oppimista jo kontin luomisen ja sen paikallisen käytön perusteella.

Selosta raportissa mitä opit eri työvaiheista ja minkälaisia haasteita kohtasit. Entä miten kehittäisit luomaasi konttia jatkossa?


**2. Luo Docker-levykuva Ohjelmistoprojekti II -projektin frontendistä**

Luo tarvittava Dockerfile-tiedosto, joka suorittaa frontend-sovelluksenne riippuvuuksien asennuksen ja projektin buildaamisen. Huomaa, että tuotantokäytössä React-sovellusta ei kannata tarjoilla React-kehityspalvelimen avulla, vaan staattisina tiedostoina esimerkiksi Nginx-palvelimen avulla. Löydät lisätietoja esimerkiksi Google-haulla ["dockerizing react app"](https://www.google.com/search?q=dockerizing+react+app).

Kuten edellisessä vaihtoehdossa, voit julkaista levykuvan esimerkiksi [Docker hub](https://hub.docker.com/) -palvelussa, mutta se ei ole välttämätöntä.


**3. Julkaise Ohjelmistoprojekti II -kurssin backend valitsemassasi PaaS-palvelussa**

Heroku on monelle opiskelijalle tuttu aikaisemmilta kursseilta, mutta sen ilmainen käyttö on suurilta osin päättymässä. Näin ollen erilaisille ilmaisille tai edullisille vaihtoehtoisille ratkaisuille on kova kysyntä opiskelijoiden keskuudessa.

Tässä tehtävävaihtoehdossa tutustu saatavilla oleviin vaihtoehtoisiin PaaS-palveluihin ja kokeile julkaista oma sovellus valitsemassasi palvelussa. Tehtävässä ei ole välttämätöntä soveltaa Dockeria, mikäli se ei ole valitun palvelun kannalta mielekästä.

[Helsingin yliopiston full stack open](https://fullstackopen.com/osa3/sovellus_internetiin#sovellus-internetiin) -kurssilla on esitelty Herokulle vaihtoehtoisina palveluina seuraavia:

* [Fly.io](https://fly.io/)
* [Render.com](https://render.com/)

Näissä palveluissa pitäisi olla ilmaiset kokeiluversiot, jotka riittävät tehtävän tekemiseksi. Kurssin opiskelijat ovat lisäksi ehdottaneet seuraavia palveluita:

* [Railway](https://railway.app/)
* [Replit.com](https://replit.com/)
* [CodeSandBox](https://codesandbox.io/)

Näiden lisäksi löytyy lukuisia vaihtoehtoisia pilvialustoja, joten voit hyvin valita palvelun myös näiden listojen ulkopuolelta.

Muista raportoida edistymisesi tehtävässä. Huomaa, että kaikkia vaiheita ei tarvitse saada valmiiksi, kunhan osoitat oppineesi eri työvaiheista. Valitsemasi pilvipalvelun valintaperusteet ovat jo itsessään hyvää sisältöä raporttiin.


**4. Kontin julkaisu OpenShift-ympäristössä (Docker & Kubernetes)**

Tätä kurssia varten on luotu OpenShift-ympäristö, jota käsitellään laajasti oppitunnin 2. videolla. Voitte pyytää tähän ympäristöön käyttäjätunnukset lähettämällä koulun sähköpostiosoitteesta sähköpostiviestin osoitteeseen `support at otaverkko piste fi`. Viestin sisällöksi pitäisi riittää: "Tarvitsen pääsyn Haaga-Helian OpenShiftiin."

Tunnusten luomisessa voi kestää jopa päiviä, joten viesti kannattaa lähettää hyvissä ajoin ennen tehtävän varsinaista aloitusta. Tarvittaessa ota opettajiin yhteyttä Teams-kanavalla tunnusten luomiseksi.

Saatuanne käyttäjätunnuksen ja salasanan, voitte kokeilla kirjautua sisään osoitteessa https://console-openshift-console.apps.hhocp.otaverkko.fi/. Kirjautuminen tapahtuu "IPA Login" -vaihtoehdolla (IPA = Identity, Policy & Audit). 

Huom! Kurssin OpenShift-palvelun kaikki https-sertifikaatit ovat itse allekirjoitettuja (self signed), eli selain tulee vaatimaan sertifikaatin hyväksymistä manuaalisesti, kuten oppitunnin videolla esitellään.
