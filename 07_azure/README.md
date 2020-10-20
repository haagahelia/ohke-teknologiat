# Azure

In this module we shall demonstrate and practice the use of [Azuren](https://azure.microsoft.com/) and the variety of services available there.

## Goals

PaaS, IaaS, cloud functions, deploying to Azure, Vizualising data

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

## Demo 2: Visualizing data, Clustering data, machine learning.

<!--
https://azure.microsoft.com/en-us/services/machine-learning/
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/machine-learning-initialize-model-clustering (klusterointimoduuli yleinen)
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/k-means-clustering (k-means, moduuli)
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/assign-data-to-clusters (assign new data to clusters, after training)
https://gallery.azure.ai/Experiment/60cf8e46935c4fafbf86f669121a24f0 (yritysten k-means klusterointia wikipediadatan perusteella)
https://docs.microsoft.com/en-us/azure/architecture/example-scenario/ai/movie-recommendations (movie recommendation examples)
https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/ai/real-time-recommendation (build realtime recommendation api with Azure, "the industry way")
-->

<!--
1. Create machine learning studio classic workspace.
1. Näytetään ? kuvakkeen kautta "tour", jossa luodaan malli tulojen ennustamiseen.
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

1. Tehdään moviedata esimerkki ja siten että vaihdetaan datasetti painotettuun datasettiin livenä ja sitten painotettuun jossa on myös kohinaa. Voidaan ehkä vaihtaa myös clustereiden määrää johonkin muuhun kuin ilmiselvään kolmeen ja katsoa miltä clusterointi näyttää.
1. Visualisointi voidaan otaa suoraan Train Clustering modelilta oikealla klikillä, Visualisointi pyrkii laittamaan 2d tasoon eri luokat suhteessa toisiinsa kuten kuvattu täällä https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/k-means-clustering.
1. Jokaisen pisteen assignementti voidaan katsoa edit metadatan tai convert to datasetin visualize -menuitemin kautta.
1. Set up web service
1. Deploy web service
1. Käytetään ensin TEST:in kautta.
1. Sitten voidaan klikata request/response api help -page linkkiä ja katsoa pythonkoodi jolla kutsua apia (api key pitää vaihtaa)
-->

## Demo 3: Enterprise Azure, Houston Inc.

## Assignements

### Assignement 7.1
<!--Pieni laajennus Teemun demoon. Mietitään mikä voisi olla fiksua omana palvelunaan (esim tapahtuman lähellä olevien bussipysäkkien näyttäminen..).
-->
