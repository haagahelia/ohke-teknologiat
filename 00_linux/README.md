# Kurssin johdanto, ympäristöt ja Linux/Unix-komentorivi

Kurssin ensimmäisellä viikolla asennamme kurssilla tarvittavat kehitysympäristöt ja tutustumme Linux-käyttöjärjestelmän peruskäyttöön.

Ohjeet kurssille tarvittavan ympäristön asentamiseksi löydät [täältä](asennukset.md). Toivomme että asennat tarvitsemasi ympäristön valmiiksi ennen ensimmäistä tapaamista. Kysy kohtaamistasi ongelmista rohkeasti Teamsissa keskustelukanavalla.

## Luentovideot

1. [**Kurssin yleiset asiat**](https://web.microsoftstream.com/video/f0e0dc26-379c-4a03-9e6b-f7f42d49f950) *28:34*
1. [**Linux-komennot**](https://web.microsoftstream.com/video/41d6925c-4e99-4218-a413-2190b22acbf8) *45:37*
1. [**GitHub classroom -kotitehtävä**](https://web.microsoftstream.com/video/58895df6-7b17-4a51-b448-1b064d3efbf1) *17:56*

<!--Todo: video Linux-palomuurista-->

👆 Näiden videoiden katsominen edellyttää kirjautumista MS Stream -palveluun Haaga-Helian tunnuksillasi. Sinun tulee olla myös jäsenenä kurssin Teams-ryhmässä.

Löydät tämän kurssin omien materiaalien lisäksi netistä lukuisia hyviä video- ja tekstimuotoisia ohjeita. Halutessasi voit käyttää myös muita materiaaleja ja aloittaa esimerkiksi videosta [15+ Terminal Commands Every Developer Must Know (Web Dev Simplified)](https://youtu.be/CV-ven_rxhw) sekä [Ubuntun komentorivitutoriaalista](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview).

## Linuxin ja komentorivin perusteet

Linux ja muut Unix-pohjaiset käyttöjärjestelmät, kuten MacOS, ovat kehittäjien keskuudessa paljon käytettyjä. [Stackoverflown 2020 kehittäjillä tekemän vuosittaisen tutkimuksen](https://insights.stackoverflow.com/survey/2020) mukaan Linuxia [on edellisen vuoden aikana käyttänyt 55% kehittäjistä](https://insights.stackoverflow.com/survey/2020#technology-platforms). Yksi syy tälle lienee se, että palvelimia käytetään tyypillisesti ainoastaan etäyhteyksillä, eikä niissä ole näyttöjä, näppäimistöjä tai graafisia käyttöliittymiä.

[![Terminal forever <3](https://www.commitstrip.com/wp-content/uploads/2016/12/Strip-Lignes-de-commande-english650-final-2.jpg)](https://www.commitstrip.com/en/2016/12/22/terminal-forever/?)

Unix-pohjaiset käyttöjärjestelmät tarjoavat paljon työkaluja, jotka helpottavat kehittäjän työtä. Niillä on helppo myös työskennellä komentorivin kautta vahvoilla komennoilla, joilla pystyy esimerkiksi käsittelemään ohjelmistojen lokitiedostoja, ajastamaan komentoja jne. Komentojen toinen vahvuus on se, että ne on helposti ajastettavissa suoritettavaksi automaattisesti, ja eri komentosarjoja voidaan yhdistää skripteiksi.

Komentorivityöskentely on tärkeä taito myös esimerkiksi sulautettujen järjestelmien ja mikrotietokoneiden yhteydessä.


### Unix-pohjaisten järjestelmien komentorivi

Unix-pohjaisten järjestelmien komentorivi on kehittäjille monipuolinen ja voimakas työkalu. Komentorivi mahdollistaa paitsi erilaisten työkalujen nopean asentamisen, tiedostojärjestelmän helpon selaamisen, erilaisten ympäristöjen pystyttämisen jne. Käydään tässä läpi esimerkkien kautta Linux-järjestelmän kehittäjälle hyödyllisiä perusasioita ja komentoja, suurin osa asioista toimii myös muissa Unix-pohjaisissa järjestelmissä.

Alkuun mainittakoon yleisesti, että Linux-komentojen keskeyttäminen tarvittaessa tapahtuu `CTRL + C`:llä. Vielä voimakkaampi yhdistelmä on `CTRL + Z`, joka ei anna processille mahdollisuutta yrittää sulavaa siistiä lopettamista.



#### Unix-komentoja

Print working directory, tulostaa kansion jossa olet.

```shell
$ pwd
/home/user/
```

Change directoy -komennolla (`cd`) liikutaan kansioissa. Tabulatoria käyttämällä voi automaattitäydentää syötteitään, eli jos aloittaa kirjoittamaan jotain ja painaa tabulaattoria, niin järjestelmä täydentää siihen mahdollisen ainoan vaihtoehdon tai sitten tulostaa syötteen alun perusteella mahdolliset vaihtoehdot:

```shell
$ cd kansionnimi            # siirtyy kansioon nykyisen kansion alla
$ cd /home/user/kansionnimi # siirtyy kansioon absoluuttisella polulla
$ cd ..                     # siirtyy hierarkiassa edelliseen kansioon
$ cd ../kansionnimi         # siirtyy hierarkiassa edelliseen alikansioon ja sen alla olevaan kansioon
$ cd ~                      # siirtyy käyttäjän kotikansioon
$ cd -                      #siirtyy kansioon, jossa olit ennen tätä
```

`ls`-komento listaa kansion tiedostot ja alihakemistot:

```shell
$ ls
```

`ls`-komento tulostaa `-l`-vivulla myös mm. tiedostojen luontipäivämäärän, käyttöoikeudet ja koon. `-a`-vivulla tulostuu myös piilotiedostot, joiden nimet alkavat pisteellä:

```shell
$ ls -la
```

Linuxin komentoja voi putkittaa, eli yhden komennon tuloste voidaan ohjata toiselle komennolle syötteeksi `|`-merkillä. Putkitus esimerkiksi `more`-komennon kanssa tulostaa kansiorakenteen sivu kerrallaan, josta voi edetä enterillä rivi kerrallaan. `CTRL + C` tai `q` lopettaa.

```shell
$ ls -l | more
```

Linuxissa komennon syötteen voi ajaa myös tiedostoon `>` -ohjausmerkillä:

```shell
$ ls -l > tiedosto.txt

# Kahdella >> -merkillä syöte lisätään tiedoston loppuun, kuten 
# tässä käyttäjän kotihakemistossa olevan .bashrc-tiedoston loppuun.

$ echo "export EDITOR='/usr/bin/nano'" >> ~/.bashrc
```

Manual komennolla (`man`) saa esiin tietyn kommennon ohjeen ja näkee mm. mitä lisävipuja komennolle voi antaa:

```shell
$ man ls
```

Tiedoston sisällön voi tulostaa `cat`-komennolla:

```shell
$ cat tiedosto.txt
```

Tiedoston voi luoda tai kaksi tiedostoa yhdistää kolmanteen tiedostoon myös catilla:

```shell
$ cat > uusi.txt
$ cat log1.txt log2.txt > yhdistetty.txt
```

Tiedostoja voi kopioida `cp`-komennolla. Käyttämällä `-R`-vipua (recursive) voit kopioida kokonaisia kansiorakenteita:

```shell
$ cp tiedosto.txt ../                       # kopioi tiedoston "ylempään" kansioon
$ cp skripti.sh skripti.sh.bak              # tekee "varmuuskopion"
$ cp -R hakemisto /Users/me/toinenhakemisto # kopioi hakemiston toiseen hakemistoon
```

Tiedostoja voi siirtää tai uudelleennimetä `mv`-komennolla:

```shell
$ mv teidosto.txt tiedosto.txt
$ mv tiedosto.txt ../ # siirtää tiedoston hierarkiassa edelliseen kansioon
```

Kansioita voi luoda `mkdir`-komennolla:

```shell
$ mkdir hienokansio
```

Tiedostoja voi poistaa `rm`-komennolla. `-r` tai `--recursive` -parametrin kanssa voit poistaa kokonaisia kansiorakenteita:

```shell
$ rm tiedosto
$ rm -r kansiorakenne # jos hakemisto ei ole tyhjä, tarvitset lisäksi f -vivun eli "force"
$ yes | rm -R kansiorakenne # jotkin unix-järjestelmät kysyvät joka tiedoston kohalla yes-varmistetta, sen voi automatisoida putkittamalla yes-komennon
```

Tyhjän tiedoston voi luoda `touch` komennolla:

```shell
$ touch tiedosto.txt
```

Tiedostoja voi muokata Unix-järjestelmien lukuisilla eri tekstieditoreilla, kuten hyvin perinteisellä vi:llä, nano:lla tai monesta järjestelmästä löytyvällä emacs:lla. Git käyttää useassa tapauksessa oletuseditorina vi:tä, joka voi tuntua käytettävyydeltään varsin haastavalta. [Gitin oletuseditorin voi myös vaihtaa esim. nano:ksi.](https://www.google.com/search?q=git+change+editor+to+nano)

Editoreilla on omat näppäinkomentonsa eri asioille, kuten tiedoston muutosten tallentamiselle ja editorin sulkemiselle.

```shell
$ vi tiedosto.txt
$ nano tiedosto.txt
$ emacs tiedosto.txt
```

Tiedostoja voi etsiä tiedostonimen perusteella `find`-komennolla. `*`-merkkiä voi käyttää tarkoittamaan, että mitkä tahansa merkit tähden ja seuraavan merkin välillä kelpaa hakuun:

```shell
$ find -name tiedo*.txt
```

Tiedostojen sisällä olevaan tekstiä voi etsiä ja tekstin sisältävän rivin tulostaa grep-komennolla. `-R` etsii rekursiivisesti koko kansiorakenteesta. Grepille annettava etsintäavain tulkitaan [Regular expression -formaatissa](https://en.wikipedia.org/wiki/Regular_expression), eli sitä voi käyttää hyvin monipuoliseen etsintään:

```shell
$ grep "kissa" tiedosto.txt # sisältääkö sanan kissa
$ grep -R "kissa" * # etsi tämän kansion kaikista alikansioista ja tiedostoista sanaa kissa
$ grep -E "koira|kissa" tiedosto.txt # Sovella regex-patternia, eli etsi sekä koiraa, että kissaa.
```

Tiedoston lopun voi tulostaa `tail`-komennolla. Tämä komento on erityisen hyödyllinen logitiedostojen seuraamiseen `-f`-vivulla (`--follow`), jolloin se jää seuraamaan tiedostojen päivittymistä ja jatkaa muutosten tulostamista ruudulla. 

`tail`-komennon voi myös putkittaa `grep`:in kanssa ja seurata tiedostossa esimerkiksi vain tietyn patternin mukaisia rivejä, kuten virheitä. Komennosta voi poistua `CTRL + C`:llä.

```shell
$ tail --follow server.log
$ tail -f server.log | grep -E "ERROR"
```

Kahden tiedoston eroavaisuudet voi listata diff komennolla:

```shell
$ diff tiedosto1.txt tiedosto2.txt
```

`chmod`-komennolla voi muokata tiedoston tai kansion oikeuksia, eli kenellä on oikeus tehdä tiedostoon minkälaisia muutoksia. Komennolla voi antaa tietylle tiedostolle oikeuksia kolmella eri tasolla: käyttäjä (u), käyttäjäryhmä (g) ja miten muut (o).

Tiedostolle voi antaa omalle käyttäjälleen luku-, suoritus- ja muokkausoikeudet, saman käyttäjäryhmän ihmisille luku- ja suoritusoikeudet ja muille ei mitään oikeuksia (edes tiedoston lukemiseen).

Oikeudet ilmaistaan tyypillisesti numeerisessa muodossa siten, että kukin oikeus vastaa yhtä bittiä kolmen bitin numerossa `rwx`. Esimerkiksi luku- ja suoritusoikeudet annetaan biteillä `101`, joka vastaa numeroa 5. Tästä komennosta voi lukea lisää vaikka [täältä](https://www.computerhope.com/unix/uchmod.htm).

```shell
$ chmod 750 mysqlscript.sh # user = read+write+execute (7), group = read+execute (5), others = (0)
$ chmod u+x mysqlscript.sh # annetaan käyttäjälle (u) suoritus (x=exceute) oikeudet
```

`chown`-komennolla voi siirtää tiedoston omistajuuden tietylle käyttäjälle.

```shell
$ chown mysqlUser mysqlscript.sh
```

`sudo` ("Switch User and Do this command") -komennolla vältetään nykyään käyttäjien tarvetta vaihtaa käyttäjätiliä root-käyttäjäksi suorittaaksen jonkin enemmän käyttöoikeuksia vaativan asian kuten vaikka uuden ohjelman asentamisen. Jos käyttäjälle on myönnetty sudo-oikeudet käyttöjärjestelmään, niin hän voi siis vaihtaa itsensä hetkellisesti superkäyttäjäksi ja ajaa jonkin enemmän oikeuksia vaativan komennon.

```shell
$ sudo apt install mysql
```

Unix-järjestelmissä voi määritellä ympäristömuuttujia, kuten `PATH` ja `HOME`. Suorittaessasi komentoa, käyttöjärjestelmä etsii sitä yksi kerrallaan `PATH`-muuttujaan lisätyistä hakemistoista. Path-muuttujan nykyisen sisällön voi tulostaa echo-komennon avulla:

```shell
$ echo $PATH
$ echo $HOME
```


export-komennolla voit lisätä PATH-muuttujaan uusia hakemistoja. Alla oleva komento siis sanoo, että uusi `PATH`-ympäristömuuttuja on nykyinen `PATH`-ympäristömuuttujan arvo, ja lisäksi siihen lisätään `/usr/me/uusihakemisto`-polku.

```shell
# Katso https://github.com/sindresorhus/guides/blob/main/npm-global-without-sudo.md
$ export PATH="$PATH:${HOME}/.npm-packages/bin"
```

Processes (`ps`) komennolla voi listata esimerkiksi kaikki kyseisen käyttäjän käynnissä olevat prosessit. Niihin liittyen voi tulostaa `ps`-komennolla monipuolisesti tietoja eri prosesseista, kuten niiden muistin ja prosessorin käyttömäärän. 

Näiden perusteella voi tehdä johtopäätöksiä, jos joki prosessi (esimerkiksi serveri) on jäänyt jumiin tai esimerkiksi jokin ohjelma ikuiseen silmukkaan. 

```shell
$ ps axu
```

`ps`-komennon ajamisen jälkeen voi joskus olla tarpeen tappaa jokin prosessi sen prosessi id:n (PID) perusteella. Tähän käytetään `kill`-komentoa, jonka käytössä kannattaa olla jossain määrin varovainen, sillä voi myös sammuttaa koko käyttöjärjestelmän, tai saattaa sen virheellisesti toimivaan tilaan:

```shell
$ kill 1234     # annetaan prosessille mahdollisuus vielä ajaa jotain komentoja
$ kill -9 1234  # jos prosessi ei vielä edellisellä kuollut, niin tällä lähtee.
```

Käyttäjiä voi lisätä Linux-järjestelmissä `useradd`-komennolla ja salasana lisätään `passwd`-komennolla

```shell
$ sudo useradd username
$ sudo passwd username
```

Unix-järjestelmissä on yleensä myös monia tietoliikenteeseen liittyviä käteviä komentoja:

```shell
$ ping www.haaga-helia.fi   # vastaako palvelin pyyntöihin, ja kuinka nopeasti?
$ whois haaga-helia.fi      # tietoja tunnuksesta (whois pitää asentaa apt:lla ubuntussa)
$ ssh host.jotain.fi        # avataan ssh-etäyhteys etäpalvelimeen
$ wget https://osoite.fi/kuva.jpeg  # ladataan tiedosto internetistä

# Haetaan curl komennolla rajapinnasta json-tiedosto, 
# siistitään se kivasti riveittäin pythonin json.tool:illa ja 
# tulostetaan grepin avulla vain tietyn sanan sisältävät rivit. 
# Komennolle annetaan parametreina lokaaleista ympäristömuuttujista APP_ID ja APP_KEY:
$ curl https://external.api.yle.fi/v1/programs/items.json?app_id=${APP_ID}\&app_key=${APP_KEY} | python3 -m json.tool | grep '"fi"' 
```

Ohjelmistokehittäjä pystyy ajamaan unix-järjestelmissä lukuisia kehitystyöhön liittyviä ohjelmia. Tässä vielä niistä muutamia esimerkkejä:

```shell
$ node
$ python
$ java
$ mysql
$ mongo
```

### Esimerkki: Sanuli ja grep

Sanuli (https://www.sanuli.fi) on uusi kotimainen avoimen lähdekoodin peli, joka on [herättänyt paljon kiinnostusta vuoden 2022 alussa](https://www.is.fi/digitoday/esports/art-2000008531907.html). Tässä kohdassa kokeilemme oppitunnin videotallenteella Linuxin komentorivin mahdollisuuksia Sanulin ratkaisemisen avustamisessa. Hyödynnä esimerkissä Kotus-sanalistaa, joka löytyy hakemistosta [04_tietorakenteet_ja_algoritmit/src/kotus-sanalista-v1/](../04_tietorakenteet_ja_algoritmit/src/kotus-sanalista-v1/).

Sanulin on kehittänyt Jaakko Husso ja se on julkaistu MIT-lisenssillä GitHubissa: https://github.com/Cadiac/sanuli.

Disclaimer: Tämän esimerkin tarkoitus ei ole kannustaa "huijaamaan" Sanulissa, eikä ohjata teitä pelaamaan Sanulia oppitunnin aikana.


#### Unix-skriptit ja chron

Unix-pohjaisissa käyttöjärjestelmissä on mahdollista luoda skriptitiedostoja, joiden avulla voi esimerkiksi yhdistää monta komentoa yhdeksi komennoksi. Myös esimerkiksi yksinkertaisen haarautumislogiikan (if-else) ja silmukoiden toteuttaminen on mahdollista. Tarkemmin skriptien-kirjoittamisesta voi lukea esimerkiksi [tästä perusoppaasta](https://docs.csc.fi/support/tutorials/env-guide/linux-bash-scripts/).

```shell
$ nano skripti.sh #luodaan skriptitiedosto
```

```bash
#!/bin/bash #skriptit avataan yleensä tällä kommentilla joka kertoo käytettävän komentorivitulkin 

# Tulostetaan teksti echo-komennolla
echo "Skripti käynnistyy"

# Ajetaan kyseisen kansion sisällöstä tiedostoon sellaiset rivit,
# jotka sisältävät käyttäjän skriptille antaman ensimmäisen parametrin sanan:
ls -l | grep $1 > tamakansio.txt 
```

Edellä luotu skripti voidaan puolestaan suorittaa seuraavasti:

```shell
$ chmod u+x skripti.sh # annetaan käyttäjälle suoritusoikeudet skriptiin, muuten sitä ei voi ajaa.
$ ./skripti.sh hello   # ajetaan skripti ja annetaan sille parametrina sana "hello"
```

Unix-pohjaisissa järjestelmissä on komentojen ajastuksen mahdollistava [cron-prosessi](https://opensource.com/article/17/11/how-use-cron-linux). `crontab`-komennolla voi määritellä ajastettavia komentojan "ajastustauluun" (cron table). `crontab`-komento luo käyttäjälle ajastustaulutiedoston `/var/spool/cron`-kansioon. Crontaulun ajastussyntaksi seuraa tiettyä kaavaa. *-merkki tarkoittaa, että kyseinen ajanmääre voi olla mitä vain.

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
$ crontab -e # Komento avaa oletustekstieditorin, johon voi syöttää haluamansa ajastuksen
5 0 * * * /Users/me/skripti.sh hello # Aja tämä komento kello 0:05 joka päivä
```

## Tehtävät

Tämän viikon tehtävä koostuu sekä Linux-ympäristön käyttöönotosta että Linux-komentoja harjoittavasta tehtävästä. Katso tarkemmat ohjeet Teamsin tehtävät-välilehdeltä.

-------

Tämän oppimateriaalin on kehittänyt Ohto Rainio ja sitä on muokannut Teemu Havulinna.