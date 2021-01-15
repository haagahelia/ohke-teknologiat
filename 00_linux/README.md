# Kurssin johdanto, ympäristöt ja Linux/Unix-komentorivi

Kurssin ensimmäisellä viikolla asennamme kurssilla tarvittavat kehitysympäristöt, tutustumme Linux-käyttöjärjestelmän peruskäyttöön.

**Tulet tekemään osan ensimmäisen viikon työskentelystä itsenäisesti jo ennen lukujärjestykseen merkittyä oppituntia. Kysy kohtaamistasi ongelmista rohkeasti Teamsissa keskustelukanavalla jo ennen ensimmäistä oppituntia.**

## &lt;ennakkotehtävät&gt;

Ennen ensimmäistä oppituntia sinun tulee valmistella itsellesi toimiva unix-pohjainen ympäristö, jossa voit kehittää ja suorittaa jatkossa kurssilla kehittämiämme koodeja. 

Mikäli sinulla on jo valmiiksi hyvä ympäristö tai olet kiinnostunut esimerkiksi, [Dockerin](https://www.docker.com/), [Raspberry Pi](https://www.raspberrypi.org/):n tai [DigitalOceanin](https://www.digitalocean.com/github-students/) käytöstä, voit käyttää myös niitä, mutta  emme voi luvata niihin käyttötukea.

### Windows + VirtualBox + Linux

Windows-käyttäjille suosittelemme Oraclen ilmaisen [VirtualBox](https://www.virtualbox.org/)-virtualisointiympäristön sekä [Ubuntu](https://ubuntu.com/desktop)-käyttöjärjestelmän asentamista. Virtuaalikoneeseen tekemäsi asennukset eivät vaikuta tietokoneesi normaaliin käyttöön, ja käyttämällä virtuaalikonetta saat käyttötukea myös kurssin puolesta. Kurssin opettajalla on käytössä Ubuntun stabiili LTS-versio 20.04 (Long Term Support), joka on varmuudella toimiva tälle kurssille.

> *Using Linux in a virtual machine gives you the option to try Linux within Windows. This step-by-step guide shows you how to install Linux inside Windows using VirtualBox.*
>
> https://itsfoss.com/install-linux-in-virtualbox/

Hyviä ohjeita asennuksiin löytyy sekä YouTubesta että Googlesta. Toimiviksi havaittuja ohjeita ovat mm. video ["How to Install Ubuntu 20.04 LTS on VirtualBox in Windows 10"](https://www.youtube.com/watch?v=x5MhydijWmc) ja artikkeli ["Install Linux Inside Windows Using VirtualBox"](https://itsfoss.com/install-linux-in-virtualbox/).


Windows-käyttäjänä joudut mahdollisesti [kytkemään päälle Windowsin Hyper-V -ominaisuuden](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v#enable-the-hyper-v-role-through-settings) tai [kytkemään virtualisoinnin päälle tietokoneesi BIOS-asetuksista](https://www.google.com/search?q=enable+virtualization+bios).

Mikäli virtuaalikoneen asennuksessa on ongelmia, pyritään pääsääntöisesti ratkaisemaan ne jo ennen ensimmäistä oppituntia Teams-työtilan chatissa!



### Linuxin komentorivikäyttö ja pakettien asentaminen

Ubuntussa useat paketit ja ohjelmat asennetaan komentorivityökaluilla. Komentorivin saat auki Ubuntun valikosta nimellä "Terminal", tai näppäinyhdistelmällä `CTRL + ALT + T`.

Mikäli komentorivin käyttö tuottaa ongelmia, hyvä tutoriaali komentorivin käytöstä löytyy osoitteessa https://ubuntu.com/tutorials/command-line-for-beginners. Lisäksi tämän osion lopussa on käsitelty Linux-komentorivin perusteita.

Voit myös aina kysyä neuvoa kurssin opettajilta ja muilta opiskelijoilta kurssin Teams-kanavilla!


**APT**

Ubuntun asennustyökalu on nimeltään Advanced Package Tool eli APT:

> *APT eli Advanced Package Tool on Debian-projektin kehittämä työkalu Linux-käyttöjärjestelmän pakettienhallinnan helpottamiseen. Se huolehtii mm. asennettavien pakettien riippuvuussuhteista ja niiden päivittämisestä. Se hakee asennettavat paketit netistä. APT-nimitystä käytetään sekä paketinhallintakirjastosta (jota voi käyttää monen käyttöliittymän kautta) että sitä käyttävästä komentorivityökalusta.*
>
> Linux.fi-wiki, https://www.linux.fi/wiki/APT

APT:in avulla sovellusten asennus tapahtuu kirjoittamalla komento muodossa:

    apt install ohjelma

Koska ohjelmien asennus vaatii pääkäyttäjäoikeudet, ei normaalilla käyttäjätunnuksella voida suoraan tehdä asennuksia. Yksittäisiä komentoja saa suoritettua pääkäyttäjäoikeuksilla [`sudo`-komennon avulla](https://wiki.ubuntu-fi.org/Sudo). Käytännössä tulet siis tekemään asennukset seuraavasti:

    sudo apt install ohjelma


APT asentaa koneellesi suoritettavia ohjelmia, joiden kanssa tulee aina huomioida myös tietoturva. Pääsääntöisesti Ubuntun pakettivarastot ovat turvallisia, mutta uusien pakettivarastojen lisääminen saattaa aiheuttaa riskejä. Tällä kurssilla teemme asennuksia vain Ubuntun omista pakettivarastoista. Voit lukea aiheesta lisää artikkelista [Can I get a virus by using "sudo apt-get install"?](https://askubuntu.com/a/818022)

### Git-asennus

Kurssilla käytetään oppimateriaalin ja esimerkkikoodien jakelussa Git-versionhallintaa. Asenna itsellesi valmiiksi Git-työkalut. 

```shell
sudo apt install git
```

Asennuksen jälkeen voit kloonata tämän repositorion itsellesi (vapaaehtoista):

```shell
git clone https://github.com/haagahelia/swd4tn023.git
```

**Node.js ja npm**

Tulemme tällä kurssilla ohjelmoimaan JavaScriptillä, johon tarvitsemme Node.js-suoritusympäristön. Node-paketeille on lisäksi oma paketinhallintasovellus nimeltä **npm** (Node Package Manager). Nämä voidaan asentaa apt-komennoilla seuraavasti:

```shell
sudo apt install nodejs
sudo apt install npm
```

Halutessasi voit lisäksi konfiguroida npm:n siten, että et tarvitse pääkäyttäjäoikeuksia pakettien asentamiseen: https://blua.blue/article/how-to-install-global-npm-packages-without-sudo-on-ubuntu/



**PIP**

APT-komennon lisäksi Linuxille on lukuisia muita pakettienhallintaohjelmia, joista useat ovat erikoistuneet jonkin tietyn ohjelmointikielen kirjastojen asentamiseen. 

Python-kirjastojen asentamisessa käytämme `pip`-työkalua.

> *pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.*
> 
> https://pypi.org/project/pip/

`pip` voidaan asentaa edellä esitellyn `apt`:in ja `sudo`:n avulla seuraavasti:

```shell
sudo apt install python3-pip
```

### Visual Studio Coden asennus

Viimeisenä asennuksena suosittelemme asentamaan Visual Studio Code -kehitysympäristön. Se löytyy ilmaiseksi helpoiten Ubuntun ohjelmistokaupasta. Ohjelmistokaupan voit avata painamalla Windows-painiketta ja kirjoittamalla hakukenttään "Ubuntu Software". Etsi hakukentän avulla "Visual Studio Code" ja valitse "install".

Visual Studio Code voidaan asentaa Linuxiin myös [lukuisilla muilla tavoilla](https://code.visualstudio.com/docs/setup/linux).

#### Laajennokset ja asetukset

Tulemme käyttämään VS Codessa ainakin seuraavia laajennoksia, jotka voit asentaa etukäteen tai tarpeen mukaan:

1. `Python`-tuki VS Codelle

    https://marketplace.visualstudio.com/items?itemName=ms-python.python

1. `Pylint` koodin tarkistus

     `pip3 install pylint`

1. `Rope` refaktorointi

     `pip3 install rope`

1. `autopep8` koodin muotoilu

    `pip3 install autopep8`

Huomaa, että pip-asennukset ovat käyttäjäkohtaisia, eli niitä ei tehdä `sudo`-komennon avulla.

Lisäksi suosittelemme muuttamaan VS Code:n asetuksista koodin automaattisen muotoilun päälle tallennettaessa ja liitettäessä koodia:

Avaa "User settings". Etsi hakukentän avulla valinnat `Format on save` sekä `Format on paste` ja aseta rastit molempiin ruutuihin.

Huom! Python-paketit sisältävät suoritettavaa ohjelmakoodia, joten niiden kanssa tulee huomioida tietoturva, aivan kuten muidenkin suoritettavien ohjelmien kanssa. Paketteja ei kannata ladata tuntemattomista lähteistä. Tunnettujen ja laajasti käytettyjen pakettien käyttäminen voi myös olla turvallisempaa kuin heikommin tunnettujen tai vähäisessä käytössä olevien. Lisätietoa pip-pakettienhallinnan turvallisuudesta löydät esimerkiksi artikkelista ["Look before you pip"](https://www.ayrx.me/look-before-you-pip).


### Extra: Guest additions sekä leikepöydän käyttö

Perusasennuksen lisäksi suosittelemme sinua asentamaan VirtualBoxin "guest additions" -lisäosat virtualisoidulle Linux-koneelle. Lisäosien avulla esimerkiksi VirtualBox-ikkunan koon muuttaminen muuttaa automaattisesti virtualisoidun työpöydän resoluutiota ikkunan koon mukaiseksi. 

Asennus tapahtuu helpoiten syöttämällä virtuaalikoneeseen virtuaalinen asennus CD virtuaalikoneen ollessa käynnissä:

![Install guest additions](guest-additions.png)

Lisää ohjeita löydät [Googlella](https://www.google.com/search?q=virtualbox+install+guest+additions).

Virtuaalikoneen ja "host"-koneen välillä on myös mahdollista synkronoida leikepöytä. Tällöin pystyt kopioimaan ja liittämään tekstiä kätevästi eri järjestelmien välillä. Käynnissä olevan virtuaalikoneen "Devices"-valikosta löytyy kohta "Shared clipboard", jonka avulla voit valita leikepöydän toimintalogiikan haluamaksesi.


## &lt;/ennakkotehtävät&gt;

Jos sait yllä olevat kohdat suoritettua, olet erinomaisesti valmistautunut viikon oppituntia ja tehtäviä varten. Mikäli törmäsit ongelmaan, kysythän neuvoa [Teamsissa](http://teams.microsoft.com/). Mikäli ongelmat eivät ratkea ennen oppituntia, älä lannistu. Myös oppitunnilla on mahdollista kysyä neuvoa.


## Linuxin ja komentorivin perusteet

Linux ja muut Unix-pohjaiset käyttöjärjestelmät, kuten MacOS, ovat kehittäjien keskuudessa paljon käytettyjä. [Stackoverflown 2020 kehittäjillä tekemän vuosittaisen tutkimuksen](https://insights.stackoverflow.com/survey/2020) mukaan Linuxia [on edellisen vuoden aikana käyttänyt 55% kehittäjistä](https://insights.stackoverflow.com/survey/2020#technology-platforms). Unix-pohjaiset käyttöjärjestelmät tarjoavat toisaalta paljon työkaluja, jotka helpottavat kehittäjän työtä (kuten automaattiset paketinhallintatyökalut kuten apt) ja niillä on helppo myös työskennellä komentorivin kautta vahvoilla komennoilla, joilla pystyy esimerkiksi käsittelemään ohjelmistojen lokitiedostoja, ajastamaan komentoja jne.

Komentorivityöskentely on tärkeä taito myös esimerkiksi sulautettujen järjestelmien kehittämisessä ja mikrotietokoneiden käsittelyssä (Raspberry Pi, ESP32 jne).

### Unix-pohjaisten järjestelmien komentorivi

Unix-pohjaisten järjestelmien komentorivi on kehittäjille monipuolinen ja voimakas työkalu. Komentorivi mahdollistaa paitsi erilaisten työkalujen nopean asentamisen, tiedostojärjestelmän helpon selaamisen, erilaisten testiympäristöjen pystyttämisen jne. Käydään tässä läpi esimerkkien kautta Linux-järjestelmän kehittäjälle hyödyllisiä perusasioita ja komentoja, suurin osa asioista toimii myös muissa Unix-pohjaisissa järjestelmissä.

Alkuun mainittakoon yleisesti, että Linux-komentojen keskeyttäminen tarvittaessa tapahtuu CTRL^C:llä (tai vielä voimakkaampi yhdistelmä on CTRL^Z, joka ei anna processille mahdollisuutta yrittää sulavaa siistiä lopettamista).

#### Unix-komentoja

Print working directory, tulostaa kansion jossa olet.
```shell
$ pwd
/Users/myusername/Documents/
```
Change directoy komennolla liikutaan kansioissa. Tabulatoria käyttämällä voi automaattitäydentää syötteitään, eli jos aloittaa kirjoittamaan jotain ja painaa tabulaattoria, niin järjestelmä täydentää siihen mahdollisen ainoan vaihtoehdon tai sitten tulostaa syötteen alun perusteella mahdolliset vaihtoehdot. 
```shell
$ cd kansionnimi #siirtyy kansioon kyseisen kansion alla
$ cd /Users/kansionnimi #siirtyy absoluuttiseen kansioon tiedostorakenteen juuressa
$ cd .. #Siirtyy hiearkiassa edelliseen kansioon
$ cd ../kansionnimi #Siirtyy hierarkiassa edelliseen alikansioon ja sen alla olevaan kansioon
$ cd #siirtyy käyttäjän kotikansioon
$ cd -#siirtyy kansioon, jossa olit ennen tätä
```
Listaa kyseisen kansion tiedostot ja kansiot
```shell
$ ls
```
-l-vivulla ls-komento tulostaa myös mm. tiedostojen luontipäivämäärän ja koon. a-vivulla tulostuu myös piilotiedostot, jotka ovat tiedostonäkymässä siis .-alkuisia tiedostoja.
```shell
$ ls -la 
```
Linuxin komentoja voi putkittaa (merkillä |). Putkitus more-komennon kanssa tulostaa kansiorakenteen sivu kerrallaan, josta voi edetä enterillä tiedosto kerrallaan (pagedown/up tai u ja d toimii mahdollisesti hieman unix-järjestelmästä riippuen myös), CTRL^C (tai q) lopettaa.
```shell
$ ls -l | more
```
Linuxissa komennon syötteen voi ajaa myös tiedostoon >-merkillä. 
```shell
$ ls -l > tiedosto.txt
#Kahdella >>-merkillä syöte lisätään tiedoston loppuun, kuten 
#tässä käyttäjän kotihakemistossa olevan bashrc-tiedoston loppuun.
$ echo "export EDITOR=\"/polku/jossa/ohjelma/sijaitsee/ohjelma\"" >> ~/.bashrc
```
Manual komennolla (man) saa esiin tietyn kommennon ohjeen ja näkee mm. mitä lisävipuja komennolle voi antaa.
```shell
$ man ls
```
Tiedoston sisällön voi tulostaa cat-komennolla
```shell
$ cat tiedosto.txt
```
Tiedoston voi luoda tai kaksi tiedostoa yhdistää kolmanteen tiedostoon myös catilla
```shell
$ cat >luouusitiedosto.txt
$ cat tiedosto1.txt tiedosto2.txt >yhdistetty.txt
```
Tiedostoja voi kopioida cp-komennolla. Käyttämällä -R (recursive) -vipua voi kopioida kokonaisia kansiorakenteita
```shell
$ cp tiedosto.txt ../ #kopioi tiedoston hierarkiassa edelliseen kansioon
$ cp -R hakemisto /Users/me/toinenhakemisto #kopioi hakemiston toiseen hakemistoon
```
Tiedostoja voi siirtää tai uudelleennimetä mv-komennolla. 
```shell
$ mv tiedosto.txt tiedostonuusinimi.txt
$ mv tiedosto.txt ../ #siirtää tiedoston hierarkiassa edelliseen kansioon
```
Kansioita voi luoda mkdir-komennolla 
```shell
$ mkdir hienokansio
```
Tiedostoja voi poistaa rm-komennolla -R-vivulla voi poistaa kokonaisia kansiorakenteita. 
```shell
$ rm tiedosto
$ rm -R kansiorakenne
$ yes | rm -R kansiorakenne #jotkin unix-järjestelmät kysyvät joka tiedoston kohalla yes-varmistetta, sen voi automatisoida putkittamalla yes-komennon
```
Tyhjän tiedoston voi luoda touch komennolla
```shell
$ touch tiedosto.txt
```
Tiedostoja voi muokata Unix-järjestelmien lukuisilla eri tekstieditoreilla, kuten hyvin perinteinen vi:llä (komennot pitää muistaa aikalailla ulkoa), nano:lla tai monesta järjestelmästä löytyvällä emacs:lla. Editoreilla on omat shortcut-komennot eri asioille kuten tiedoston muutosten tallentamiselle ja editorin sulkemiselle. 
```shell
$ vi tiedosto.txt
$ nano tiedosto.txt
$ emacs tiedosto.txt
```
Tiedostoja voi etsiä tiedostonimen perusteella find-komennolla. *-merkkiä voi käyttää tarkoittamaan, että mitkä tahansa merkit tähden ja seuraavan merkin välillä kelpaa hakuun.
```shell
$ find -name tiedo*.txt
```
Tiedostojen sisällä olevaan tekstiä voi etsiä (ja tekstin sisältävän rivin tulostaa) grep-komennolla. -R etsii rekursiivisesti koko kansiorakenteesta. Grepille annettava etsintäavain tulkitaan [Regular expression -formaatissa](https://en.wikipedia.org/wiki/Regular_expression), eli sitä voi käyttää hyvin monipuoliseen etsintään. 
```shell
$ grep "kissa" tiedosto.txt #sisältääkö sanan kissa
$ grep -R "kissa" * #etsi tämän kansion kaikista alikansioista ja tiedostoista sanaa kissa
$ grep -E "koira|kissa" tiedosto.txt # Sovella regex-patternia, eli etsi sekä koiraa, että kissaa.
```
Tiedoston lopun voi tulostaa tail-komennolla. Tämä komento on erityisen hyödyllinen logitiedostojen seuraamiseen -F-vivulla, jolloin se jää seuraamaan tiedostojen päivittymistä ja jatkaa muutosten tulostamista ruudulla. Tailin voi myös putkittaa grep:in kanssa ja seurata tiedostossa esimerkiksi vain tietyn patternin mukaisia muutoksia. Komennosta voi poistua CTRL^C:llä
```shell
$ tail -F server.log
$ tail -F server.log | grep "ERROR"
```
Kahden tiedoston eroavaisuudet voi listata diff komennolla.
```shell
$ diff tiedosto1.txt tiedosto2.txt
```
chmod-komennolla voi muokata tiedoston tai kansion oikeuksia, eli kenellä on oikeus tehdä tiedostoon minkälaisia muutoksia. Komennolla voi antaa tietylle tiedostolle oikeuksia kolmella eri tasolla. Eli miten tiedostoa saa käyttää sen luonut käyttäjä, miten käyttäjän kanssa samaan ryhmään kuuluvat käyttäjät ja miten muut. Eli tiedostolle voi antaa omalle käyttäjälleen luku-, suoritus- ja muokkausoikeudet, saman käyttäjäryhmän ihmisille luku- ja suoritusoikeudet ja muille ei mitään oikeuksia (edes tiedoston lukemiseen). Tästä monimutkaisesta komennosta voi lukea lisää vaikka [täältä](https://www.computerhope.com/unix/uchmod.htm).
```shell
$ chmod 750 mysqlscript.sh
$ chmod u+x mysqlscript.sh #annetaan käyttäjälle (u) suoritus (x=exceute) oikeudet

```
chown-komennolla voi siirtää tiedoston omistajuuden tietylle käyttäjälle.
```shell
$ chown mysqlUser mysqlscript.sh
```
Sudo ("Switch User and Do this command") -komennolla vältetään nykyään käyttäjien tarvetta vaihtaa käyttäjätiliä root-käyttäjäksi suorittaaksen jonkin enemmän käyttöoikeuksia vaativan asian kuten vaikka uuden ohjelman asentamisen. Jos käyttäjälle on myönnetty sudo-oikeudet käyttöjärjestelmään, niin hän voi siis vaihtaa itsensä hetkellisesti superkäyttäjäksi ja ajaa jonkin enemmän oikeuksia vaativan komennon.
```shell
#&-merkillä laitetaan komento ajautumaan järjestelmässä taustalla, jolloin 
#terminaalin käyttämistä voi jatkaa muihin asioihin.
$ sudo apt install mysql &
```
Unix-järjestelmissä voi määritellä ympäristömuuttujia kuten PATH-muuttujan. Käyttöjärjestelmä etsii komentoja PATH-muuttujaan lisätyistä hakemistoista. Path-muuttujan nykyisen sisällön voi tulostaa echo-komennon avulla.
```shell
$ echo $PATH
```
export-komennolla voit lisätä PATH-muuttujaan uusia hakemistoja. Alla oleva komento siis sanoo, että uusi PATH-ympäristömuuttuja on nykyinen PATH-ympäristömuuttujan arvo ja lisäksi siihen lisätään /usr/me/uusihakemisto-polku.
```shell
$ export PATH=$PATH:/usr/me/uusihakemisto
```
Processes (ps) komennolla voi listata esimerkiksi kaikki kyseisen käyttäjän käynnissä olevat prosessit. Niihin liittyen voi tulostaa ps-komennolla monipuolisesti tietoja eri prosesseista, kuten niiden muistin ja prosessorin käyttömäärän. Näiden perusteella voi tehdä johtopäätöksiä, jos joki prosessi (esimerkiksi serveri) on jäänyt jumiin tai esimerkiksi jokin ohjelma ikuiseen silmukkaan. 
```shell
$ ps ux
```
ps-komennon ajamisen jälkeen (jossa näkyy prosessi id, eli PID) voi joskus olla tarpeen tappaa jokin prosessi sen prosessi id:n (PID) perusteella. Tähän käytetään kill-komentoa, jonka käytössä kannattaa olla jossain määrin varovainen, sillä voi myös sammuttaa koko käyttöjärjestelmän.
```shell
$ kill 1234 #annetaan prosessille mahdollisuus vielä ajaa jotain komentoja
$ kill -9 1234 #Jos prosessi ei vielä edellisellä kuollut, niin tällä lähtee.
```
Käyttäjiä voi lisätä Linux-järjestelmissä useradd-komennolla ja salasana lisätään passwd-komennolla
```shell
$ sudo useradd username
$ sudo passwd username
```
Unix-järjestelmissä on yleensä myös monia tietoliikenteeseen liittyviä käteviä komentoja.
```shell
$ ping www.haaga-helia.fi #miten nopeasti osoite vastaa, voi testata vaikka omaa tuotantopalvelinta
$ whois haaga-helia.fi #tietoja tunnuksesta, whois pitää asentaa apt:lla ubuntussa.
$ ssh host.jotain.fi  #avataan ssh-etäyhteys etäpalvelimeen
$ wget https://osoite.fi/kuva.jpeg  #Ladataan tiedosto internetistä
```
Ohjelmistokehittäjä pystyy ajamaan unix-järjestelmissä lukuisia kehitystyöhön liittyviä ohjelmia. Tässä vielä niistä muutamia esimerkkejä.
```shell
$ node
$ python
$ java
$ mysql
$ mongo
```

#### Unix-skriptit ja chron

Unix-pohjaisissa käyttöjärjestelmissä on mahdollista luoda skriptitiedostoja, joiden avulla voi esimerkiksi yhdistää monta komentoa yhdeksi komennoksi. Myös esimerkiksi yksinkertaisen haarautumislogiikan (if-else) ja silmukoiden toteuttaminen on mahdollista. Tarkemmin skriptien-kirjoittamisesta voi lukea esimerkiksi [tästä perusoppaasta](https://docs.csc.fi/support/tutorials/env-guide/linux-bash-scripts/).
```shell
$ nano skripti.sh #luodaan skriptitiedosto
```
```bash
#!/bin/bash #skriptit avataan yleensä tällä kommentilla joka kertoo käytettävän komentorivitulkin 
echo "Hello World" #tulostetaan huvikseen teksti echo-komennolla
ls -l | grep $1 > tamakansio.txt #ajetaan kyseisen kansion sisällöstä tiedostoon sellaiset rivit, 
#jotka sisältävät käyttäjän skriptille antaman ensimmäisen parametrin sanan.
```
```shell
$ chmod u+x skripti.sh #annetaan käyttäjälle suoritusoikeudet skriptiin, muuten sitä ei voi ajaa.
$ ./skripti.sh hello #ajetaan skripti ja annetaan sille parametrina sana "hello"
```

Unix-pohjaisissa järjestelmissä on komentojen ajastuksen mahdollistava [cron-prosessi](https://opensource.com/article/17/11/how-use-cron-linux). crontab-komennolla voi määritellä ajastettavia komentojan "ajastustauluun" (cron table). crontab-komento luo käyttäjälle ajastustaulutiedoston /var/spool/cron-kansioon. Crontaulun ajastussyntaksi seuraa tiettyä kaavaa. *-merkki tarkoittaa, että kyseinen ajanmääre voi olla mitä vain.
```shell
1 2 3 4 5 /polku/komento argumentit_komennolle
```
jossa:
* 1: Minuutit (0-59)
* 2: Tunnit (0-23)
* 3: Päivä (0-31)
* 4: Kuukausi (0-12 [12 == Joulukuu])
* 5: Viikonpäivä (0-7 [7 tai 0 == sunnuntai])

```shell
crontab -e #Komento avaa oletustekstieditorin, johon voi syöttää haluamansa ajastuksen
5 0 * * * /Users/me/skripti.sh hello #Aja skripti.sh viisi minuuttia keskiyön jälkeen joka päivä
```

## Tehtävät

### Tehtävä 0.1 (100% kierroksen arvosanasta)

Kirjoita scripti (lokittaja.sh), joka kirjoittaa tiedoston *loki.log* loppuun tämän hetken päivämäärä ja kellonaika aikaleiman ja tekstin “heippa”. Käytä googlea selvittääksesi miten parhaiten saat aikaleiman tulostettua scriptiin. Ajasta scripti chronilla pyörimään minuutin välein. Kirjoita toinen scripti (tyhjentaja.sh), joka kopioi *loki.log*-tiedoston sisällön *vanhatlogit.log*-tiedoston loppuun ja sitten poistaa *loki.log*-tiedoston. Ajasta tyhjentaja-scripti pyörimään chronissa joka keskiyö. Palauta luomasi kaksi linux-skriptiä (lokittaja.sh ja tyhjentaja.sh) sekä tiedostossa /var/spool/cron/crontabs/kayttajatunnus sijaitseva cron-tiedosto, josta näkyy tekemäsi ajastukset. Vinkki: cron-tiedoston käsittelyyn (palautusta varten) tarvitset todennäköisesti sudo-komentoa.
