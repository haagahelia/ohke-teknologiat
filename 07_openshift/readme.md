# OpenShift-kokeilut ja esimerkit

Tässä demossa **yritetään** viedä kohtuullisen yksinkertainen tietokantapohjainen Java-sovellus Rahti-palveluun. Esimerkkejä ei ole tarkoitus toistaa itse demon aikana.


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

Dockerin dokumentaatiossa https://docs.docker.com/language/python/build-images/ on suoraviivainen kuvaus vaiheista, joita seuraamme.

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

Imagen tagin lisääminen: https://docs.docker.com/engine/reference/commandline/tag/

    # kirjautuminen konttirekisteriin
    docker login -u unused docker-registry.rahti.csc.fi --password-stdin

    # tagin lisääminen
    docker tag flask-events docker-registry.rahti.csc.fi/app-deployment-demo/flask-events:latest

    # julkaisu
    docker push docker-registry.rahti.csc.fi/app-deployment-demo/flask-events:latest


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
