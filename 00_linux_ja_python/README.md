
# Linux ja Python

Kurssin ensimmäisellä viikolla asennamme kurssilla tarvittavat kehitysympäristöt, tutustumme Linux-käyttöjärjestelmän peruskäyttöön ja perehdymme Python-ohjelmointikielen perusteisiin.

Johdannon käytettäviin työkaluihin löydät kurssin [etusivulta](../README.md#Työkalut).

**Tulet tekemään osan ensimmäisen viikon työskentelystä itsenäisesti jo ennen lukujärjestykseen merkittyä oppituntia. Kysy kohtaamistasi ongelmista rohkeasti Teamsissa keskustelukanavalla jo ennen ensimmäistä oppituntia.**

## Tavoite 

Tämän viikon tavoitteina on päästä alkuun komentorivityöskentelyssä sekä oppia käyttämään ohjelmoinnin perusrakenteita Python-ohjelmointikielellä.

## Ennakkotehtävät

Ennen ensimmäistä oppituntia sinun tulee valmistella itsellesi toimiva unix-pohjainen ympäristö, jossa voit kehittää ja suorittaa Python-kielistä koodia. 

Mikäli sinulla on jo valmiiksi hyvä ympäristö tai olet kiinnostunut esimerkiksi, [Dockerin](https://www.docker.com/), [Raspberry Pi](https://www.raspberrypi.org/):n tai [DigitalOceanin](https://www.digitalocean.com/github-students/) käytöstä, voit käyttää myös niitä, mutta  emme voi luvata niihin käyttötukea.

### Windows + VirtualBox + Linux

Windows-käyttäjille suosittelemme Oraclen ilmaisen [VirtualBox](https://www.virtualbox.org/)-virtualisointiympäristön sekä [Ubuntu](https://ubuntu.com/)-käyttöjärjestelmän asentamista. Virtuaalikoneeseen tekemäsi asennukset eivät vaikuta tietokoneesi normaaliin käyttöön, ja käyttämällä virtuaalikonetta saat käyttötukea myös kurssin puolesta. 

Hyvä ohje asennuksiin löytyy esimerkiksi osoitteesta https://itsfoss.com/install-linux-in-virtualbox/:

> *Using Linux in a virtual machine gives you the option to try Linux within Windows. This step-by-step guide shows you how to install Linux inside Windows using VirtualBox.*
>
> https://itsfoss.com/install-linux-in-virtualbox/

Mikäli virtuaalikoneen asennuksessa on ongelmia, pyritään pääsääntöisesti ratkaisemaan ne jo ennen ensimmäistä oppituntia Teams-työtilan chatissa.

### Linuxin komentorivikäyttö

Suorita Linuxin komentorivikäyttöä koskeva tutoriaali osoitteessa https://ubuntu.com/tutorials/command-line-for-beginners

> *This tutorial will teach you a little of the history of the command line, then walk you through some practical excercises to become familiar with a few basic commands and concepts. We’ll assume no prior knowledge, but by the end we hope you’ll feel a bit more comfortable the next time you’re faced with some instructions that begin “Open a terminal”.*
>
> https://ubuntu.com/tutorials/command-line-for-beginners


Huom! Kurssin ensimmäinen kyselynä toteutettu viikkotehtävä Teamsissa koskee tätä tutoriaalia. Vastaa Teams-tehtävään seuratessasi tutoriaalia.

### Git-asennus

Kurssilla käytetään oppimateriaalin ja esimerkkikoodien jakelussa Git-versionhallintaa. Asenna itsellesi valmiiksi Git-työkalut. Ubuntussa Git-asennus tapahtuu komentorivillä seuraavasti (saat komentorivin auki näppäinyhdistelmällä `CTRL + ALT + T`):

```shell
$ sudo apt install git
$ git clone https://github.com/haagahelia/swd4tn023.git
```

### Python 3 + Pip

Python 3 on esiasennettuna Ubuntun työpöytäversiossa. Lisäksi tarvitset `pip`-pakettienhallintatyökalun, joka voidaan asentaa seuraavasti:

```shell
$ sudo apt install python3-pip
```

> *pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.*
> 
> https://pypi.org/project/pip/


### Visual Studio Coden asennus

Viimeisenä asennuksena suosittelemme asentamaan Visual Studio Code -kehitysympäristön. Se löytyy ilmaiseksi helpoiten Ubuntun ohjelmistokaupasta. Ohjelmistokaupan voit avata painamalla Windows-painiketta ja kirjoittamalla hakukenttään "Ubuntu Software". Etsi kyseisestä sovelluksesta "Visual Studio Code" ja valitse "install".

Visual Studio Code voidaan asentaa Linuxiin myös [lukuisilla muilla tavoilla](https://code.visualstudio.com/docs/setup/linux).

#### Laajennokset ja asetukset

Tulemme käyttämään VS Codessa ainakin seuraavia laajennoksia, jotka voit asentaa etukäteen tai tarpeen mukaan:

1. `Python` koodieditori
1. `Pylint` koodin tarkistus
1. `Rope` refaktorointi
1. `autopep8` koodin muotoilu

Lisäksi suosittelemme muuttamaan editorin asetuksista koodin automaattisen muotoilun päälle tallennettaessa ja liitettäessä koodia:

Avaa "User settings". Etsi hakukentän avulla valinnat `Format on save` sekä `Format on paste` ja aseta rastit molempiin ruutuihin.

### Extra: Guest additions sekä leikepöydän käyttö

Perusasennuksen lisäksi suosittelemme sinua asentamaan VirtualBoxin "guest additions" -lisäosat virtualisoidulle Linux-koneelle. Lisäosien avulla esimerkiksi VirtualBox-ikkunan koon muuttaminen muuttaa automaattisesti virtualisoidun työpöydän resoluutiota ikkunan koon mukaiseksi. Ohjeita lisäosan lisäosan asentamiseksi löydät [Googlella](https://www.google.com/search?q=virtualbox+install+guest+additions).

Virtuaalikoneen ja "host"-koneen välillä on myös mahdollista synkronoida leikepöytä. Tällöin pystyt kopioimaan ja liittämään tekstiä kätevästi eri järjestelmien välillä. Käynnissä olevan virtuaalikoneen "Devices"-valikosta löytyy kohta "Shared clipboard", jonka avulla voit valita leikepöydän toimintalogiikan haluamaksesi.
