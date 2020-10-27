# Azure

> *"The Azure cloud platform is more than 200 products and cloud services designed to help you bring new solutions to life—to solve today’s challenges and create the future. Build, run, and manage applications across multiple clouds, on-premises, and at the edge, with the tools and frameworks of your choice.*"
>
> [Microsoft. What is Azure?](https://azure.microsoft.com/en-us/overview/what-is-azure/)

In this module, we shall demonstrate and practice the use of [Azure](https://azure.microsoft.com/) and a few selected services available there.


## Goals

Understanding the concepts [PaaS](https://azure.microsoft.com/en-us/overview/what-is-saas/) and [IaaS](https://azure.microsoft.com/en-us/overview/what-is-iaas/). Learning how to deploy a Node.js application in Azure in multiple different ways. Learning how to implement an application as serverless cloud functions. Machine learning, clustering and K-means based recommendations with the help of Azure Machine Learning studio.


## Registering to Azure 

You can log in [Azure Portal](https://portal.azure.com/) using your Haaga-Helia account. You may receive free credits in your account if you register using [student registration](https://azure.microsoft.com/en-us/free/students/). 


## Demo application

During this session we will use the following application to demonstrate the workflows and concepts:

https://github.com/haagahelia/app-deployment-demo

The demo application contains two HTTP endpoints and runs on top of [Express](https://expressjs.com/). You can check the contents of index.js [here](https://github.com/haagahelia/app-deployment-demo/blob/master/index.js).

In short, the server root `/` will return a list of events from Helsinki Open API and the `/health` path will return a JSON object describing the status of the application.


## Demo 1: Azure as a cloud provider

In Azure, there are typically multiple supported ways of achieving the same goals. Typically documents published by Microsoft will explain how resources are managed and updated using either VS Code extensions or other Azure specific tools.

This demonstration presents an opinionated view on how to develop and deploy web applications. Generic tools, such as Git, are favored over Azure specific tools. Command line is favored over graphical interfaces, as the GUIs tend to hide some of the details that help us understand how the systems work.


<!--
-Millainen ubuntuserveri voidaan pystyttää.
-Jos deployaisi helsingin kaupungin dataa hakevan sovelluksen Azureen? Voitaisiin näyttää mikropalvelun deployaaminen.
-dokkerointi
-pilvifunktiot
-> Tällä saisi näytettyä mitä on PaaS & IaaS.
-->

### IaaS (virtual machines)

> *"Infrastructure as a service (IaaS) is an instant computing infrastructure, provisioned and managed over the internet."*
>
> *"IaaS provides all the infrastructure to support web apps, including storage, web and application servers, and networking resources. Organizations can quickly deploy web apps on IaaS and easily scale infrastructure up and down when demand for the apps is unpredictable."*
>
> [Microsoft. What is IaaS.](https://azure.microsoft.com/en-us/overview/what-is-iaas/)

The following video demonstrates how to create a new virtual machine in Azure and how to deploy your application code there:

**[Video: Azure part 1 - Ubuntu virtual machine](https://web.microsoftstream.com/video/8eb8e43c-3972-4f73-bd75-d5269e45c82e)**

The newly created Ubuntu server contains outdated packages and is missing the Node.js installation. The system is first updated and Node.js is installed with the following commands:

```bash
$ sudo apt update

$ sudo apt upgrade

$ sudo apt install node
```

After updating the server and installing Node.js, the application can be cloned, installed and started:

```bash
$ git clone https://github.com/haagahelia/app-deployment-demo.git

$ cd app-deployment-demo

$ npm install --production

$ npm start # port 3000

$ sudo PORT=80 node index.js # port 80 requires sudo privileges
```

You can check the results at http://20.54.83.139/health. The server may be shut down after the class.

<!--
Benefits:

* freedom to install and configure everything
* ability to install multiple apps, databases etc.

Weaknesses:

* replication
* scalability
* ...

(source)-->

### PaaS (App Service)

> *"Platform as a service (PaaS) is a complete development and deployment environment in the cloud, with resources that enable you to deliver everything from simple cloud-based apps to sophisticated, cloud-enabled enterprise applications. You purchase the resources you need from a cloud service provider on a pay-as-you-go basis and access them over a secure Internet connection."*
>
> *"PaaS provides a framework that developers can build upon to develop or customize cloud-based applications. ... Cloud features such as scalability, high-availability, and multi-tenant capability are included, reducing the amount of coding that developers must do."*
>
> [Microsoft. What is PaaS.](https://azure.microsoft.com/en-us/overview/what-is-paas/)

The following video demonstrates how to create a new app in Azure and how to deploy your application code there:

**[Video 2: Azure part 2 - App service](https://web.microsoftstream.com/video/615a4f88-4a10-4b39-9ef5-f5f60c4a4c1b)**

Because our demo application is a standard Node.js app built with [Express](https://expressjs.com/), it can be deployed as an App as-is. Azure App Service supports a multitude of different deployment methods, but in our case, we prefer to deploy the application with Git.

As in the video, the deployment can be done by adding the app's Git repository as a remote and deploying the master branch there.

```bash
$ git remote add azure AZURE_REPOSITORY_URL

$ git push azure master
```

After the application is deployed, you can visit it at https://app-deployment-demo.azurewebsites.net/health.

<!--Benefits:

* scalability
* replication

Weaknesses:

* no control over the operating environment-->

### Cloud functions ("serverless")

> *"Azure Functions extends the PaaS concept by providing developers with complete abstraction from the underlying infrastructure through a pay-per-execution billing model that automatically scales based on trigger invocations."*
>
> [Mashkowski, N. Introducing Azure Functions](https://azure.microsoft.com/en-us/blog/introducing-azure-functions/)

> *"Azure Functions is an event driven, compute-on-demand experience that extends the existing Azure application platform with capabilities to implement code triggered by events occurring in Azure or third party service as well as on-premises systems. Azure Functions allows developers to take action by connecting to data sources or messaging solutions thus making it easy to process and react to events. Developers can leverage Azure Functions to build HTTP-based API endpoints accessible by a wide range of applications, mobile and IoT devices. Azure Functions is scale-based and on-demand, so you pay only for the resources you consume.*"
>
> [Mashkowski, N. Introducing Azure Functions](https://azure.microsoft.com/en-us/blog/introducing-azure-functions/)

[Quickstart: Create a function in Azure that responds to HTTP requests](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function-azure-cli?tabs=bash%2Cbrowser&pivots=programming-language-javascript)


[Quickstart: Create a function in Azure using Visual Studio Code](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-javascript)


    # installing the 'func' command:
    npm install --global azure-functions-core-tools

    # creating a function app
    func init

    # adding a new function (http trigger)
    func new

    # starting the development server
    func start

During class we extend our demo application with two cloud functions.

### Docker (containers)

> *"Fundamentally, a container is nothing but a running process, with some added encapsulation features applied to it in order to keep it isolated from the host and from other containers. One of the most important aspects of container isolation is that each container interacts with its own private filesystem; this filesystem is provided by a Docker image. An image includes everything needed to run an application - the code or binary, runtimes, dependencies, and any other filesystem objects required."*
>
> [Docker. Orientation and setup.](https://docs.docker.com/get-started/)

The video ["Docker For Beginners: From Docker Desktop to Deployment"](https://www.youtube.com/watch?v=i7ABlHngi1Q) explains key concepts and workflows for Docker.

For orientation about Docker, see [Orientation and setup](https://docs.docker.com/get-started/) at Docker docs.

Recommended reading: 

* The ["Dockerizing a Node.js web app" tutorial from Node.js](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/) covers creating, building and running a Docker container for a Node.js application.

* Dockerhub contains official [pre-built Node.js images](https://hub.docker.com/_/node) that can be extended by your Dockerfile. In our Dockerfile, we use `12-slim`, which is a very small image running the latest version `12.x` of Node.js.

* You can read more about the different commands in a Dockerfile from the official [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

#### Dockerignore

To exclude certain folders being copied from our host system into the container we exclude them in a `.dockerignore` file:

```
node_modules
npm-debug.log
```

### Dockerfile

Our Dockerfile follows the example at https://nodejs.org/en/docs/guides/nodejs-docker-webapp/:

```docker
FROM node:12-slim

WORKDIR /usr/src/app

ENV PORT=80

COPY package*.json ./

RUN npm install

COPY . ./

EXPOSE 80

CMD [ "node", "index.js" ]
```

For explanations why `package*.json` files are copied first and the rest of the source code later or why we start the app with `node` and not `npm`, see the ["Docker For Beginners: From Docker Desktop to Deployment"](https://www.youtube.com/watch?v=i7ABlHngi1Q) video.

Another good resource for understanding the Dockerfile is [Anatomy of a dockerfile](https://gist.github.com/adamveld12/4815792fadf119ef41bd).


#### Building the image

Docker images need to be built before running. The builds consist of layers that are cached. Caching makes the builds fast, as when we update our source code, Docker only needs to re-build the topmost layers.

The following command will build the container using the current folder `.` as context and tag the image with the tag `docker-demo`:

```sh
$ docker build -t docker-demo .
```

To deploy our image to Azure, we want to add a specific tag to it, which contains the container registry URL as well our image name (docker-demo) and version (latest):

```sh
$ docker build -t swd4tn023.azurecr.io/docker-demo:latest .
```

We will use this tag later when we deploy the image. This time the build will be instant, as Docker already has all layers cached.


#### Running the image in a local container

The image can be started with `docker run` command and the tag. In our Dockerfile we defined the container to internally listen to port 80. To be able to access that port from our host operating system, we need to [bind a port on our local system](https://docs.docker.com/engine/reference/commandline/run/#publish-or-expose-port--p---expose) to the one inside the container using the `-p` flag.

```sh
$ docker run -p 3000:80 swd4tn023.azurecr.io/docker-demo:latest
```

Now port `3000` on the host system is directed to port `80` inside the container and we can access our app at the URL http://localhost:3000/health.


#### Azure Container Registry

Now that we have our Docker image built and running locally, the next step is to publish it and run it on top of Azure infrastructure. For this we use Azure Container Registry:

> *"Azure Container Registry is a managed, private Docker registry service based on the open-source Docker Registry 2.0. Create and maintain Azure container registries to store and manage your private Docker container images and related artifacts.*"
>
> [Microsoft. Introduction to private Docker container registries in Azure.](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-intro)

There are other container registries as well, such as [Docker Hub](https://hub.docker.com/) and [GitHub Packages](https://github.com/features/packages).

First, we [create a new private container registry in Azure](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal). In our demo, the registry is called `swd4tn023` and located at `swd4tn023.azurecr.io`.

Before pushing our container in the registry, we first need to log in:

```sh
$ docker login swd4tn023.azurecr.io
```

Username for the container registry is the same as the registry name (swd4tn023) and the password can be found in the Azure Portal.

When authentication is complete, we use `docker push` command with our **tag**:

```sh
$ docker push swd4tn023.azurecr.io/docker-demo:latest
```

Notice that the tag `swd4tn023.azurecr.io/docker-demo:latest` contains the URL of the registry as well as the container name and version.


#### Using the container in a Web Application

When the container is published we can create a new webapp in App Service. One possible way for achieving this is explained in ["Migrate custom software to Azure App Service using a custom container"](https://docs.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux#configure-app-service-to-deploy-the-image-from-the-registry) at Microsoft Docs. Unlike in the previous App Service example, this time we choose to deploy a container, not code. In our example, we are using `app-deployment-demo-docker` as the name of our application.

By using the Azure portal, we can also configure our app to trigger a new deployment when the Docker image is updated in the registry. After the container app is running, we can visit it at:

https://app-deployment-demo-docker.azurewebsites.net/health


#### Continuous integration for the container

Finally, we can automate our workflow by using a continuous integration system, such as GitHub actions or Travis.

In our example, we use [Publish Docker Container](https://github.com/actions/starter-workflows/blob/b4fa2522d2fe556c03cc194dcf659b1eb9f03b77/ci/docker-publish.yml) action at GitHub and customize it to use Azure Container Registry instead of [GitHub Packages](https://github.com/features/packages).

The results of the action can be [observed at GitHub](https://github.com/haagahelia/app-deployment-demo/actions?query=workflow%3ADocker).

The Container Registry password must not be included in the automation file in plain text. Instead, it is defined as a [GitHub secret](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets) and injected to the `docker login` command as follows:

    echo "${{ secrets.CR_PAT }}" | docker login swd4tn023.azurecr.io -u swd4tn023 --password-stdin

See the entire `docker-publish.yml` file [here](https://github.com/haagahelia/app-deployment-demo/blob/master/.github/workflows/docker-publish.yml).


## Demo 2: Machine learning, K-means Clustering recommendations.

In this demo we shall build a K-means clustering model for movie recommendations with the help of [Azure machine learning studio](https://studio.azureml.net/). We will deploy the trained model as a web service and ask for a new recommendation.

Here are listed some useful links related to this demo:
1. [Machine learning in general from Azure documentation](https://azure.microsoft.com/en-us/services/machine-learning/)
1. [Clustering modules in Azure general introduction](https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/machine-learning-initialize-model-clustering)
1. [K-Means clustering](https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/k-means-clustering)
1. [Azure's comprehensive documentation related to artificial intelligence and e.g. Azure reference architectures for different machine learning scenarios](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/ai-overview)
1. [An example of building a K-means clustering for S&P 500 companies based on their wikipedia data](https://gallery.azure.ai/Experiment/60cf8e46935c4fafbf86f669121a24f0)

![Machine learning studio](img/azure_machine_learning13.png)
![K-means clustering of data](img/azure_machine_learning12.png)

<!--
1. Tehdään moviedata esimerkki ja siten että vaihdetaan datasetti painotettuun datasettiin livenä ja sitten painotettuun jossa on myös kohinaa. Voidaan ehkä vaihtaa myös clustereiden määrää johonkin muuhun kuin ilmiselvään kolmeen ja katsoa miltä clusterointi näyttää.
1. Visualisointi voidaan otaa suoraan Train Clustering modelilta oikealla klikillä, Visualisointi pyrkii laittamaan 2d tasoon eri luokat suhteessa toisiinsa kuten kuvattu täällä https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/k-means-clustering.
1. Jokaisen pisteen assignementti voidaan katsoa edit metadatan tai convert to datasetin visualize -menuitemin kautta.
1. Set up web service
1. Deploy web service
1. Käytetään ensin TEST:in kautta web serviceä.
1. Sitten voidaan klikata request/response api help -page linkkiä ja katsoa pythonkoodi jolla kutsua apia (api key pitää vaihtaa)
1. Näytetään ? kuvakkeen kautta "tour", jossa luodaan malli tulojen ennustamiseen.
-->

<!--
Helsinki datan esimerkki jos sitä hieman näytetään:
1. Create machine learning studio classic workspace.
1. Create experimentin kautta lähdetään luomaan mallia.
1. Valitaan helsinkiData.csv dataksi
1. (Laiteaan feature hashing mukaan.) -> ei vaikuta tässä
1. Valitaan k-means clustering (kokeillaan säätää sen parametreja, centroids 3 esim ja sitten kohti 8:aa)
1. Valitaan Select columns in Dataset ()
1. Valitaan Train clustering model, johon syötetään sekä k-means clustering että select columns.
1. Valitaan edit metadata, johon syötetään Train clusteringin oikeasta liittymästä tulokset
1. Valitaan edit metadatasta (oikea klikki) -> Result dataset -> Visualize
1. Klikataan name-kolumnia ja valitaan että "compare to assignements".
1. Kun k-means klusteringin centroidien määrää kasvattaa (esim. ensin 3 -> 5 ja sitten 5 -> 7), niin rupeaa löytymään erilaisia teattereita (kolme eri teatteriklusteria, 3:lla kaikki menee samaan), tämän voi havainnollistaa klikkaamalla tag2-kolumnia ja siitä compare to assignements.
-->

## Demo 3: Enterprise Azure, Houston Inc.

## Assignements

### Assignement 7.1
<!--Pieni laajennus Teemun demoon. Mietitään mikä voisi olla fiksua omana palvelunaan (esim tapahtuman lähellä olevien bussipysäkkien näyttäminen..).
-->
### Seminar assignement 1
Build a machine learning model with some interesting data related to e.g. your software project assignement with the help of Azure machine learning studio. You can e.g. build a recommendation system with the help of k-means clustering. You can deploy your service as a Web API.
