# Ohjelmistokehityksen teknologioita

Tervetuloa kurssille!

Ohjelmistokehittäjän työ on suurimmaksi osaksi muuta kuin jonkin tietyn ohjelmointikielen syntaksin suvereenia hallintaa. Tämän kurssin tavoitteena on esitellä ohjelmistokehittäjälle tärkeitä taitoja, työkaluja ja tekniikoita, joita ei suoraan ole tullut esille ohjelmoinnin peruskursseilla tai projektityökursseissa. Kurssi toimii samalla myös tukikurssina ohjelmistoprojekti 2 -kurssille, jossa tämän kurssin aiheita päästään soveltamaan osana isompaa projektia.

Opettajina kurssilla toimivat Teemu Havulinna ja Juhani Välimäki (etunimi.sukunimi@haaga-helia.fi). Kurssin sisältö perustuu suuresti myös kurssin aikaisemman opettajan, Ohto Rainion, työhön.


## Linkit

* [Opintojaksokuvaus](https://opinto-opas.haaga-helia.fi/course_unit/SOF009AS3A)
* [Teams](https://teams.microsoft.com/)


## Kurssin suoritustapa

Kurssin alkupuoliskolla käsitellään lukukausittain vaihtelevia aiheita ja opiskelijat tekevät niihin liittyviä harjoitustehtäviä. Jokaisesta esiteltävästä aiheesta on myös mahdollista tehdä laajempi seminaaritehtävä kurssin jälkimmäisellä puoliskolla.

**Seminaarivaiheessa**, kurssin jälkimmäisellä puoliskolla, jokainen opiskelija valitsee kurssin aiheista itseään eniten kiinnostavan ja tekee siihen liittyvän seminaaritehtävän. Seminaaritehtävän voi valita joko opettajien ehdotuksista tai seminaaritehtävän aihetta voi ehdottaa myös itse. Seminaaritehtävä voi liittyvä läheisesti opiskelijan ohjelmistoprojekti 2 -kurssin projektiin.

Saman seminaariaiheen valinneet opiskelijat osallistuvat yhteiseen seminaariin, jossa analysoidaan ja kommentoidaan myös muiden opiskelijoiden seminaaritöitä.


## Kurssin osallistumisen vahvistaminen

⚠ **Kurssin osallistumisen vahvistaminen edellyttää ensimmäisen ja toisen viikon viikkotehtävien hyväksyttyä suoritusta niiden määräaikaan mennessä.** Tehtäviin on saatavissa vinkkejä ja tukea kurssin Teams-kanavalla sekä oppitunneilla.

Ensimmäisten tehtävien ei ole tarkoitus karsia ketään pois kurssilta, vaan varmistaa, että työskentely kurssin työkaluilla ja ohjelmointikielillä lähtee kaikilla käyntiin. Tarvitset riittävät esitiedot näistä aiheista kurssin seuraavia viikkoja varten.

**Kurssin keskeyttäminen** ei ole Haaga-Helian linjauksia noudattaen mahdollista enää osallistumisen vahvistamisen jälkeen:

> *"Opettaja poistaa opetuksen alussa toteutukselta opiskelijat, jotka eivät osallistu ensimmäiseen opetuskertaan tai ilmoita poissaolostaan. Opiskelijoita ei enää myöhemmin poisteta toteutukselta, vaan kaikille annetaan arvosana hylätty-kiitettävä."*
>
> *https://mynet.haaga-helia.fi/group/pakki/toteutukselle-ilmoittautuminen*


## Opintojakson oppitunnit ja päivämäärät

**Huom!** Tämä sivu päivittyy kurssin edetessä ja sekä aikataulu että sisältö tarkentuvat.

Oppitunnit pidetään pääsääntöisesti **torstaisin klo 14-16.45**. Jos muuta ei ilmoiteta erikseen, kurssin Teams-kanavan viesteissä ja lukujärjestyksessä meillä on viikottainen **hybriditapaaminen luokassa ja Teamsissa**.

Toivomme että tutustutte mahdollisuuksien mukaan etukäteen kunkin aiheen videoihin ja materiaaleihin, jotta voimme tapaamisissa käyttää aikaa myös mm. tehtävien parissa.

<hr />

<details><summary><strong>To 22.8. <a href="00_linux/">Kurssin johdanto, ympäristöt ja Linux/Unix-komentorivi</a></strong></summary>

Videot:

* [📼 Linuxin peruskäyttö](https://youtu.be/HRqHfItALO4)
* [📼 GitHub classroom -tehtävien ohjeistus](https://youtu.be/9dA17XlzT-w)
* [📼 Kurssin koodausympäristöt (wsl2, Docker, Development containers, Codespace)](https://youtu.be/aC3xj4KXu3g)

Tehtävät (DL ke 28.8. klo 22:00):

* [📥 Kurssin kehitysympäristön asennus](00_linux/asennukset.md)
* 📥 Linux-komentorivi (Teams ja GitHub classroom)

<hr />
</details>


<!--details><summary--><strong>To 29.8. DevOps: Johdatus konttiteknologiaan, containers, images</strong> 
<!-- /summary -->

Keskustellaan yhdessä termien ja kuvien avulla käsitteistä, jotta itse docker-opiskelun suorittaminen sujuu jouhevammin:
Tiimin [DevOpsin tavoitetila periaatekuvana](01_docker/DockerCaseExample.pdf) ja [Dockerin keskeisiä käsitteitä](01_docker/DockerConceptsAndVocabulary.pdf) sanoiksi puettuina ja kuvina.

Suositellut videot: [Never install locally (Coderized)](https://youtu.be/J0NuOlA2xDc) ja [Virtual Machine (VM) vs Docker (IBM Technology)](https://youtu.be/a1M_thDTqmU).

Docker cheatsheettejä: [CLI cheat sheet pdf](https://docs.docker.com/get-started/docker_cheatsheet.pdf), [docker concepts](https://extremeautomation.io/cheatsheets/docker-cheatsheet/), [cheatsheet poikineen](https://dockerlabs.collabnix.com/docker/cheatsheet/).

Dockerin laaja ohjeisto [docs.docker.com](https://docs.docker.com/).

Käytämme Eficoden ja Helsingin yliopiston yhteistyönä syntynyttä [DevOps with Docker](https://devopswithdocker.com/) -kurssia:

0. [(Getting started)](https://devopswithdocker.com/getting-started) ja  [(Introduction to Part 1)](https://devopswithdocker.com/part-1/)
1. [Definitions and basic concepts](https://devopswithdocker.com/part-1/section-1), Tehtävät 1.1-1.2
1. [Running and stopping containers](https://devopswithdocker.com/part-1/section-2), Tehtävät 1.3-1.4
1. [In-depth dive to images](https://devopswithdocker.com/part-1/section-3), Tehtävät 1.5-1.8

[Example of learning notes for the part 1a](01_docker/DevOpsWithDocker_1a/DevOpsWithDocker_Part1a_learning_notes.md)

Tehtävä *DevOps with Docker part 1a* löytyy Teamsista ja GitHub classroomista. DL ke 4.9. klo 22:00.


<hr />
<!--/details-->

<!--details><summary--><strong>To 5.9. DevOps: Docker "volumet" ja portit</strong>
<!-- /summary -->

Tuetun työskentelyn vaiheet 2:

4. [Defining start conditions for the container](https://devopswithdocker.com/part-1/section-4)
5. [Interacting with the container via volumes and ports](https://devopswithdocker.com/part-1/section-5), Tehtävät 1.9-1.10
6. [Utilizing tools from the Registry](https://devopswithdocker.com/part-1/section-6), Tehtävät 1.11-1.14
7. [Summary](https://devopswithdocker.com/part-1/section-7)

[Summary for the part 1b](01_docker/DevOpsWithDocker_1b/DevOpsWithDocker_Part1b_learning_notes.md)<br />
&nbsp; &nbsp;[Docker Volumes](01_docker/DevOpsWithDocker_1b/DockerVolumes/)<br />
&nbsp; &nbsp;[Docker Ports](01_docker/DevOpsWithDocker_1b/DockerPorts/)<br />

Tehtävä *DevOps with Docker part 1b* löytyy Teamsista ja GitHub classroomista. DL ke 11.9. klo 22:00.

<hr />
<!--/details-->


<!--details><summary--><strong>To 12.9. DevOps: Johdatus Docker Compose:n käyttöön</strong><!-- /summary --> 

Tuetun työskentelyn vaiheet 3: [Part 2](https://devopswithdocker.com/part-2/)

1. [Migrating to Docker Compose](https://devopswithdocker.com/part-2/section-1), Tehtävät 2.1-2.3
2. [Docker networking](https://devopswithdocker.com/part-2/section-2), Tehtävät 2.4-2.5

Tästä lähtien jää lisämateriaaliksi:

3. ( [Volumes in action](https://devopswithdocker.com/part-2/section-3) )
4. ( [Containers in development](https://devopswithdocker.com/part-2/section-4) )

Tehtävävaihtoehdot: 1. DevOpsWithDocker -tehtävät 2a   TAI    2. Docker-monivalinta   (Molemmat ovat Teamsissä)

(Toki voi tehdä molemmat jos haluaa tehdä bonustehtävänä)

Monivalintatehtäviä dockerista (tasolle docker-composen pelkät perusteet ja esim. docker network:in pelkät perusteet). Muutamia materiaalilinkkejä ja videolinkkejä annettu ja sitten testi osaamsesta. Ihan perusymmärrystä haetaan. Sellaista että olette työhaastattelussa tai ekassa työpaikassa kärryillä siitä mitä dockerilla voi saada aikaan. Koko kurssin viikkotyömäärä on 8-9h, joten valmistaudu huolella ensin se max 7-8h.

Monivalintatehtävät perustuvat siis näissä tai alussa linkattujen materiaalien keskeisiin asioihin. Sellaisiin, joiden ymmärtäminen / osaaminen on auttanut kontituksessa. Joku yksityiskohtakin voidaan kysyä sieltä täältä. Mutta täyteen 5p ei vaadita täysiä monivalintapisteitä.

Docker-monivalintatehtäviä varten tutustu DevOps with Docker -kurssin osiin 1 ja 2 sekä jatka näistä [materiaaleista](01_docker/DockerMonivalintatehtavanLahteet.md)
<hr />
<!--/details-->



<strong>To 19.9. Kubernetes-vierailijaluento</strong>

Saamme kampukselle vierailijan SUSE:lta [(https://www.suse.com/)](https://www.suse.com/) kertomaan Kubernetesistä [(https://kubernetes.io/)](https://kubernetes.io/).

<!--
a. Full-stack -sovelluksen dockerointi/kontitus [Täältä sovelluksen lähtötiedot ja kaikkia komentoja, joita tarvittiin manuaalisessa asentamisessa](01_docker/fullstack_dockerized_task/Manual_Installation_commands.md)

TAI

b. Monivalintatehtäviä dockerista (tasolle docker-composen pelkät perusteet ja esim. docker network:in pelkät perusteet). Muutamia materiaalilinkkejä ja videolinkkejä annetaan ja sitten testi osaamsesta. Ihan perusymmärrystä haetaan. Sellaista että olette työhaastattelussa tai ekassa työpaikassa kärryillä siitä mitä dockerilla voi saada aikaan. Materiaalilinkit ilmestyvät ensin, ja monivalinta viimeistään perjantaina. Koko kurssin viikkotyömäärä on 8-9h, joten valmistaudu huolella ensin se max 7-8h.

Monivalintatehtävät perustuvat siis näissä tai alussa linkattujen materiaalien keskeisiin asioihin. Sellaisiin, joiden ymmärtäminen / osaaminen on auttanut kontituksessa. Joku yksityiskohtakin voidaan kysyä sieltä täältä. Mutta täyteen 5p ei vaadita täysiä monivalintapisteitä.

Docker-monivalintatehtävien [materiaalit](01_docker/DockerMonivalintatehtavanLahteet.md)
-->




<!-- <strong><del>To 22.2. intensiiviviikko</del></strong> -->

<details><summary><strong>To 26.9. TypeScript-kielen perusteet ja työkalut</strong></summary>

Vierailuluento peliohjelmoinnista.

[Oppitunnin muistiinpanot](./01_typescript)

Lisämateriaalina suosittelemme perehtymään lukuun "TypeScriptin perusteet" [typescript-ohjelmointi.github.io](https://typescript-ohjelmointi.github.io/)-sivustolla.

Tehtävä GitHub classroomissa, DL ke 2.10. klo 22.

</details>


<hr />

<details><summary><strong>To 3.10. JS/TS edistyneet ominaisuudet</strong></summary>

[TypeScript-projektin luonnista](https://github.com/valju/JS_ES_Features/blob/master/TS_basics/TypeScript_usage_understood.pdf) ... Samasta materiaalista löytyy mm. seuraavat linkit

[JavaScripti/ECMAScriptin ominaisuuksista (käytetään TypeScriptissä)](https://github.com/valju/JS_ES_Features/blob/master/ES_advanced/ES_advanced_or_tricky_features.md)

[TypeScriptin ominaisuuksia, joita käytettiin eräässä Softala-projektissa 2023-2024](https://github.com/valju/JS_ES_Features/blob/master/TS_basics/TS_in_a_fullstack_project.md)

Tehtävä GitHub classroomissa, DL ke 9.10. klo 22.

</details>

<details><summary><strong>To 10.10. JS/TS-koodin yksikkötestaus</strong></summary>

[Oppitunnin muistiinpanot](./02_testaus/typescript.md).

Tehtävä GitHub classroomissa, DL ke 23.10. klo 22.

<hr />
</details>

<br />
<strong><del>To 17.10. intensiiviviikko</del></strong>

<br />

<!-- >
<strong>Seuraavien aiheiden osalta aikataulu ja järjestys ovat suuntaa-antavia</strong>

<strong>Ohjelmistoarkkitehtuureista</strong>

* [Ohjelmistoarkkitehtuurit ja -patternit (engl. PDF)](06_ohjelmistoarkkitehtuurit_ja_patternit/SoftwareArchitecturesAndPatterns.pdf)
* [Ketterän dokumentoinnin periaatteet (engl. PDF)](06_ohjelmistoarkkitehtuurit_ja_patternit/documentation_principles_for_sw_projects.pdf)

Näistä molemmista aukeaa monivalintatehtävä/quiz torstaina. Sillä voi korvata viikon Docker-tehtävän

<hr>
-->



<details><summary><strong>To 24.10. Node.js backend -arkkitehtuuri</strong></summary>
Tehtävä Teamsissä, DL ke 30.10. klo 22.

<!-- Merkkaa keltaisella lisäykset/muutokset, tai kirjoita palautuksen alkuun lista parannuksista. -->

<hr />
</details>

<details><summary><strong>To 31.10. Seminaarien käynnistys</strong></summary>

[Seminaarityön ohjeistus](./08_seminaari)

<hr />
</details>

<details><summary><strong>To 7.11., 14.11., 21.11., 28.11. Seminaarityön tekemistä</strong></summary>

[Seminaarityön ohjeistus](./08_seminaari)

Yksilöllistä ohjausta Teamsissa tai sopimuksen mukaan kampuksella. Kurssin seminaarivaiheessa ei järjestetä yhteisiä tapaamisia, vaan tarjoamme yksilöllistä ohjausta etukäteen sovittavina ajankohtina.

<hr />
</details>

**Seminaariraportin palautus su 1.12. klo 22 mennessä.**

<!-- <strong><del>To 9.5. Helatorstai</del></strong> -->

<details><summary><strong>To 5.12. Seminaariesitykset</strong></summary>

[Katso seminaarityön ohjeet](./08_seminaari).

</details>

<hr />


<details><summary><strong>(To 12.12. Loput Seminaariesitykset tai joku kokoava esitys kurssista)</strong></summary>
</details>

<hr />

## Viestintäkanavat

Tällä kurssilla hyödynnetään MS Teams -palvelua. Teams tarjoaa luontevan kanavan kysyä ja keskustella myös oppituntien ulkopuolella. Jos jäät jumiin tehtävän kanssa tai et ymmärrä materiaaleja tai tehtävänantoja, kysy rohkeasti vinkkejä Teamsissa. Todennäköisesti samaa ongelmaa pohtii kanssasi myös moni muu, joten lähetäthän sisältöä ja tehtävänantoja koskevat kysymykset yhteiselle kanavalle eikä yksityisviestinä.

Kurssilla suositellaan käytettävän Teamsin työpöytäsovellusta. Kirjautuminen Teamsiin tapahtuu Haaga-Helian opiskelijatunnuksella.

Liittymisohje kurssin Teams-ryhmään löytyy sähköpostitse lähetetystä tiedotteesta sekä Moodlesta.

* [Teams Quick Start -ohje (pdf)](https://go.microsoft.com/fwlink/?linkid=2131456)
* [Teams](https://teams.microsoft.com/)
* [Teams-lataussivu](https://teams.microsoft.com/downloads)


## Työkalut

Kurssilla käytetään lukuisia eri teknologioita ja työkaluja, joten joudut mahdollisesti tekemään tietokoneellesi lukuisia erilaisia asennuksia.

Ohjelmistojen asentaminen ja käyttäminen eri käyttöjärjestelmillä poikkeaa toisistaan merkittävästi, minkä lisäksi saman ohjelmiston eri versiot toimivat joskus hyvin eri tavoilla. Asennus- ja yhteensopivuusongelmien minimoimiseksi kurssilla suositellaan vahvasti oman erillisen [Linux-virtuaalikoneen](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview), [WSL2-ympäristön](https://learn.microsoft.com/en-us/windows/wsl/install), [Docker-konttien](https://docs.docker.com/language/nodejs/develop/) tai [GitHub codespacen](https://github.com/features/codespaces) käyttöä kurssin tehtäviä tehdessäsi.

Virtualisoituun ympäristöön tekemäsi asennukset eivät vaikuta tietokoneesi normaaliin käyttöön. Käyttämällä kurssin suositusten mukaisia ympäristöjä saat myös todennäköisemmin vertaistukea muilta opiskelijoilta ja opettajilta.

Mikäli sinulla on valmiiksi käytössäsi Linux tai muu Unix-pohjainen käyttöjärjestelmä, kuten macOS, voit käyttää sitä kurssilla. Myös etäyhteydellä käytettävät Linux-ympäristöt, kuten [DigitalOcean](https://www.digitalocean.com/github-students/), [AWS](https://aws.amazon.com/ec2/) tai [Azure](https://azure.microsoft.com/en-us/services/virtual-machines/) voivat sopia kurssin tarkoituksiin, mutta niihin pystymme tarjoamaan vain vähäistä käyttötukea.

Lisää ohjeita löydät kurssin [ensimmäisen viikon materiaalista](00_linux).

⚠ Linux voidaan asentaa myös tietokoneen pääkäyttöjärjestelmäksi tai "dual boot"-vaihtoehdolla nykyisen käyttöjärjestelmän rinnalle, mutta näitä vaihtoehtoja ei kurssin puolesta suositella.

⚠ Kurssin aikana teemme asennuksia mm. Ubuntun `apt`-työkalulla, Noden `npm`-työkalulla, Dockerilla ja VS Codella. Kaikki nämä työkalut lisäävät tietokoneellesi suoritettavaa ohjelmakoodia, jonka yhteydessä tulee aina huomioida myös tietoturva. Asennusten tekeminen erillisessä virtuaalisessa ympäristössä on oiva lisä oman tietokoneesi suojaamiseksi, vaikka olemmekin pyrkineet valitsemaan vain erittäin tunnettuja ja hyvämaineisia ohjelmistoja tälle kurssille.


## Kurssin tehtävät

Kurssilla tehdään viikoittaisia tehtäviä, joiden arvioinnissa hyödynnetään mm. [GitHub classroom -palvelua](https://classroom.github.com/) sekä MS Teamsia. Sekä kurssin Classroom-tehtäväpalautukset että MS Teams -ryhmä poistetaan vaaditun säilytysajan päätyttyä. Jos haluat säilyttää kurssilla työstämäsi tehtävien ratkaisut pidempään, [teethän repositorioistasi kopiot omalle käyttäjätunnuksellesi GitHubissa](https://www.google.com/search?q=git+clone+and+push+to+new+repo). Vaihtoehtoisesti voit säilyttää tehtäviesi ratkaisut paikallisesti omilla laitteillasi.


## Arviointi

Kurssi arvioidaan asteikolla 0-5. Kurssin arviointi perustuu viikkoaiheiden yhteydessä suoritettuihin tehtäviin (60 % arvosanasta) sekä kurssin toisella puoliskolla tehtävään seminaarityöhön (40 %).

Kunkin tehtävän tai tehtäväkokonaisuuden painoarvo loppuarvioinnissa määräytyy sen laajuuden mukaan suhteessa muihin tehtäviin ja tehtäväkokonaisuuksiin. Pisteet skaalataan yhteneviksi vasta loppuarvosanaa varten.

Yksittäinen palauttamatta jäänyt tai arvosanalla 0 arvioitu osasuoritus ei estä seuraavien suoritusten tekemistä, kunhan kokonaisuutena kurssista muodostuu hyväksytty arvosana. Tämä koskee myös seminaarityötä. Poikkeuksena tähän on kahden ensimmäisen viikon tehtävät, jotka toimivat kurssille osallistumisen vahvistamisessa.


### Kurssin keskeyttäminen

Kurssin keskeyttäminen ei ole Haaga-Helian linjauksia noudattaen mahdollista enää kahden ensimmäisen viikon jälkeen:

> *"Opettaja poistaa opetuksen alussa toteutukselta opiskelijat, jotka eivät osallistu ensimmäiseen opetuskertaan tai ilmoita poissaolostaan. Opiskelijoita ei enää myöhemmin poisteta toteutukselta, vaan kaikille annetaan arvosana hylätty-kiitettävä."*
>
> https://mynet.haaga-helia.fi/group/pakki/toteutukselle-ilmoittautuminen


## Lähteiden käyttäminen ja yksilötyöskentely

Tämän kurssin materiaali perustuu suurelta osin valmiisiin netistä löytyviin dokumentaatioihin ja tutoriaaleihein. Tällä sivulla eri aihealueiden yhteydessä tarjotaan linkkejä aihetta koskeviin materiaaleihin, mutta **joudut sen lisäksi merkittävissä määrin etsimään itse tietoa aiheista**.

Ohjelmointiongelmiin löytyy usein valmiita tai osittaisia ratkaisuja ympäri Internetiä niin keskustelupalstoilta kuin tutoriaaleista. Nettilähteiden hyödyntäminen ja niistä mallin ottaminen on sallittua ja kannustettavaa, mutta **et saa vain kopioida ratkaisuja, vaan sinun tulee kirjoittaa koodisi itse ja myös ymmärtää, miten se toimii**. Koska kyseessä on korkeakoulun opintojakso, sinun tulee merkitä lähteet lainatessasi esimerkiksi StackOverflow:sta löytämääsi koodia. Lähdeviitteeksi riittää esimerkiksi verkkosivun osoite kommenttina lainatun koodin yhteydessä, tai käyttämäsi lähteen käyttöehtojen mukainen muu lähdeviite.

Tehtävien vastausten generointi tekoälyn avulla on kiellettyä. Et saa siis käyttää esim. ChatGPT:tä tai GitHub Copilot:ia ratkaistaksesi annetun tehtävän sellaisenaan. Saat kuitenkin hyödyntää näitä palveluita yksittäisten ongelmien ratkaisemiseksi.

Yhteistyö on kurssilla kannustettavaa, mutta **yksilötehtävissä kaikkien tulee silti tuottaa omat ratkaisut**. Voitte koodata yhdessä ja tehdä toiminnallisesti samanlaisia ratkaisuja, mutta suora kopiointi ei ole sallittua. Merkitkää kaikkiin yhteistyössä tehtyihin tehtäviin niitä työstäneiden opiskelijoiden nimet esimerkiksi lähdekoodin kommentteina.
