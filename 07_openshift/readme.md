# OpenShift-kokeilut ja esimerkit

Tässä demossa **yritetään** julkaista Python- ja JS-sovelluksia OpenShift-pilvessä sekä konttien että pelkän lähdekoodin avulla. Esimerkkejä ei ole tarkoitus toistaa itse demon aikana.

Kokonaisuutena pilvipalveluiden infrastruktuuri on erittäin laaja, ja siitä riittäisi asiaa useammaksikin kurssiksi. Tällä oppitunnilla on tarkoitus tutustua terminologiaan ja työvaiheisiin siinä määrin, että aiheiden parissa on mahdollista jatkaa itseopiskelua esimerkiksi seminaarityön puitteissa.


## Missä näitä teknologioita käytetään?

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


## Mikä on kontti?

> *"Containers are a technology based on operating system kernel features that allow the creation of isolated environments sharing a kernel. For example, container features make it possible to have several isolated root filesystems, network stacks and process trees that all use the same kernel. These isolated environments are similar in functionality to lightweight virtual machines, but there are some key differences between virtual machines and containers. The biggest one is that virtual machines always have their own kernels, while containers share the host system's kernel."*
>
> https://docs.csc.fi/cloud/rahti/containers/


**Käsitteitä:**

* Image
* Container
* Volume
* Image stream
* Container Registry (paremminkin Container Image Registry)


## Mikä on Kubernetes?

> *"The power of Kubernetes (and OpenShift) is in the relatively simple abstractions that they provide for complex tasks such as load balancing, software updates for a distributed system, or autoscaling"*
>
> https://docs.csc.fi/cloud/rahti/concepts/


**Käsitteitä:**

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


## 3. Imagen julkaisu konttirekisterissä

Ennen julkaisua imagelle on tarpeen lisätä tagi, joka vastaa sen sijaintia konttirekisterissä: https://docs.docker.com/engine/reference/commandline/tag/

Kurssin OpenShift-pilven konttirekisteri sijaitsee osoitteessa `default-route-openshift-image-registry.apps.hhocp.otaverkko.fi`. Oppituntiin mennessä kyseistä rekisteriä ei ole kuitenkaan vielä saatu otettua onnistuneesti käyttöön.

Seuraava esimerkki näyttää miten `login`, `tag` ja `push` toimivat `docker-registry.rahti.csc.fi`-rekisterin kanssa:

    # 1. Kirjautuminen konttirekisteriin.
    # Salasanan sijasta käytetään OAuth-tokenia, jonka saat 
    # osoitteesta https://oauth-openshift.apps.hhocp.otaverkko.fi/oauth/token/request
    docker login default-route-openshift-image-registry.apps.hhocp.otaverkko.fi

    # 2. Tagin lisääminen. Uudessa tagissa on mukana konttorekisteri, projekti ja imagen nimi
    docker tag flask-events  docker push default-route-openshift-image-registry.apps.hhocp.otaverkko.fi/PROJEKTI/IMAGE:latest

    # 3. Julkaisu
    docker push default-route-openshift-image-registry.apps.hhocp.otaverkko.fi/PROJEKTI/IMAGE:latest

**Huom!**

Koska konttirekisteri käyttää itse allekirjoitettua sertifikaattia, Docker ei oletuksena suostu muodostamaan siihen yhteyttä. Tämä on saatu kierrettyä oppitunnin esimerkissä lisäälällä tiedostoon `C:\Users\TUNNUS\.docker\daemon.json` uusi attribuutti nimeltä `insecure-registries`:

```json
{
	"insecure-registries": [
		"default-route-openshift-image-registry.apps.hhocp.otaverkko.fi"
	]
}
```

Asetusten muuttamisen jälkeen Docker tulee käynnistää uudelleen.

Kirjautumisessa salasanan sijasta käytettävän OAuth-tokenin saat pyydettyä osoitteesta https://oauth-openshift.apps.hhocp.otaverkko.fi/oauth/token/request.


## 4. Kontin deployment OpenShiftissä

1. Projektin luonti

    *An OpenShift project is an alternative representation of a Kubernetes namespace.*

2. Resurssin lisääminen projektiin

    *Deploy an existing Image from an Image registry or **Image stream tag***

3. ...


# Konttien lisääminen OpenShiftin katalogista

https://catalog.redhat.com/software/containers/search


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

Tämä on kurssin viimeinen viikkotehtävä, ja sen saa halutessaan tehdä yksin, parin kanssa tai ryhmässä. Tehtävässä ei ole tarkkaa toiminnallista vaatimusta, joten voitte soveltaa aiheita sen mukaan, oletteko enemmän kiinnostuneita esimerkiksi Dockerista vai Kuberneteksesta. Mikäli teette työn ryhmässä, merkitkään raporttiinne selvästi kaikki tekijät. Mikäli jaoitte työtä eri kirjoittajien kesken, eritelkää kuka teki minkäkin vaiheen.

Tehtävänä on soveltaa tunnilla käsiteltyjä aiheita oman sovelluksen kanssa esimerkiksi julkaisemalla oma tai ryhmän harjoitustyö konttirekisterissä tai OpenShift-alustalla. Julkaistava sovellus voi olla esimerkiksi palvelinohjelmointi-kurssin harjoitustyö, tämän kurssin viikkoharjoitus tai ohjelmistoprojekti II:lla kehitettävä projekti.

Tehtävää tehdessäsi kirjaa itsellesi ylös eri työvaiheet, käyttämäsi komennot sekä hyödyntämäsi nettilähteet. Oletettavaa on, että julkaisu ei tule onnistumaan ensimmäisellä yrityksellä, joten kirjaa eri välivaiheet ja niistä oppimasi asiat. Kirjaa ylös osoitteet, joista julkaisemasi image tai web-palvelu on tarkasteltavissa tehtävän arvioinnin yhteydessä. Lopuksi palauta Teamsiin kirjoittamasi raportti. Raportti voi olla muodoltaan tekstitiedosto, docx tai pdf eikä sen tarvitse noudattaa erityistä raportointiohjetta. Lähdeviitteet vaaditaan, mutta ne ovat vapaamuotoisia, ja kuvankaappausten käyttäminen raportissa voi olla hyvä idea.

Tehtävän arviointikriteerit perustuvat tehtävässä opittuihin asioihin. Raportit, joissa opiskelija selvästi osoittaa oppineensa uusia asioita ja soveltaneensa niitä käytännössä, arvioidaan oletuksena arvosanalla 5. Raportit, joissa on selvästi tehty erilaisia osin satunnaisia kokeiluja, mutta opitut asiat ovat heikosti yksilöitävissä, arvioidaan oletuksena arvosanalla 3. Huomatkaa, että sovelluksen julkaisun ei tarvitse lopulta onnistua, vaan täydet pisteet voi saada myös tilanteessa, jossa yritys on epäonnistunut, mutta siitä on selvästi opittu ja tehdyt vaiheet on raportoitu asianmukaisesti.

Tehtävän ratkaisusi voi olla laajuudeltaan hyvinkin yksinkertainen, eli sen ei tarvitse tavoitella esimerkiksi tunnilla esitettyjen esimerkkien laajuutta. Voit halutessasi jatkaa OpenShiftin parissa työskentelyä kurssin seminaariosuudessa.

## Esimerkkiaihe

Kohtuullisen haastava ja edistynyt tehtävän sisältö voisi olla esimerkiksi seuraava:

1. Luo OpenShiftiin projekti palvelinohjelmointi-kurssin harjoitustyötäsi varten
2. Lisää projektiin MySQL-tietokantapalvelin OpenShiftin katalogista
3. Konfiguroi sovelluksesi joko tiedostojen tai ympäristömuuttujien avulla käyttämään OpenShiftiin lisäämääsi MySQL-tietokantaa
4. Lisää sovelluksesi projektiin GitHubista suoraan lähdekoodeista [source-to-image -lähestymistavalla](https://docs.openshift.com/container-platform/4.10/openshift_images/using_images/using-s21-images.html)

Raportoi edistymisesi tehtävässä. Huomaa, että kaikkia vaiheita ei tarvitse saada valmiiksi, kunhan osoitat oppineesi eri työvaiheista.
