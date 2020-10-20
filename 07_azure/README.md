# Azure

In this module we shall demonstrate and practice the use of [Azuren](https://azure.microsoft.com/) and the variety of services available there.

## Goals

PaaS, IaaS, cloud functions, deploying to Azure, Machine learning, clustering and K-means based recommendations with the help of Azure Machine Learning studio.

## Registering to Azure 

[Student registration](https://azure.microsoft.com/en-us/free/students/)

## Demo 1: Azure as a cloud provider

<!--
-Millainen ubuntuserveri voidaan pystyttää.
-Jos deployaisi helsingin kaupungin dataa hakevan sovelluksen Azureen? Voitaisiin näyttää mikropalvelun deployaaminen.
-dokkerointi
-pilvifunktiot
-> Tällä saisi näytettyä mitä on PaaS & IaaS.
-->

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
