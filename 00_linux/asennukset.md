# Kurssin kehitysympäristön asentaminen

**Kysy kohtaamistasi ongelmista rohkeasti Teamsissa keskustelukanavalla.**

Kurssilla tarvitset toimivaa Unix-pohjaista ympäristöä, jossa voit harjoitella mm. komentorivin käyttöä sekä DevOps-taitoja.

Mikäli sinulla on valmiiksi käytössäsi Linux tai muu Unix-pohjainen käyttöjärjestelmä, kuten macOS, voit käyttää sitä kurssilla. Myös Raspberry Pi tai etäyhteydellä käytettävät Linux-ympäristöt, kuten [DigitalOcean](https://www.digitalocean.com/github-students/), [AWS](https://aws.amazon.com/ec2/), [Azure](https://azure.microsoft.com/en-us/services/virtual-machines/) sopivat kurssin tarkoituksiin, mutta niihin pystymme tarjoamaan vain vähäistä käyttötukea.


## Windows + VirtualBox + Linux

Graafiseen käyttöliittymään tottuneille käyttäjille yksi miellyttävä tie Linuxiin tutustumiseksi on [Ubuntu](https://ubuntu.com/desktop)- tai [Xubuntu](https://xubuntu.org/)-käyttöjärjestelmä graafisella käyttöliittymällä. Ubuntu voidaan asentaa "virtuaalikoneena" Oraclen ilmaisen [VirtualBox](https://www.virtualbox.org/)-virtualisointiympäristön avulla esimerkiksi [Ubuntun tutoriaalia seuraamalla](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview).

> *"VirtualBox is a general purpose virtualiser that is available across Linux, Mac OS and Windows. It’s a great way to experience Ubuntu regardless of your current operating system."*
>
> https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox

💡 Linux voidaan asentaa myös tietokoneen pääkäyttöjärjestelmäksi tai "dual boot"-vaihtoehdolla nykyisen käyttöjärjestelmän rinnalle, mutta näitä vaihtoehtoja ei kurssin puolesta suositella niihin liittyvien riskien vuoksi.

Virtuaalikoneeseen tekemäsi asennukset eivät vaikuta tietokoneesi normaaliin käyttöön, ja voit tarvittaessa poistaa kaiken kurssilla asentamasi kerralla poistamalla virtuaalikoneen. Hyviä ohjeita asennuksiin löytyy sekä YouTubesta että Googlesta. Jaa myös löytämäsi hyvät ohjeet muille Teamsissa!

Windows-käyttäjänä joudut mahdollisesti [kytkemään päälle Windowsin Hyper-V -ominaisuuden](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v#enable-the-hyper-v-role-through-settings) tai [kytkemään virtualisoinnin päälle tietokoneesi BIOS-asetuksista](https://www.google.com/search?q=enable+virtualization+bios).

Mikäli virtuaalikoneen asennuksessa on ongelmia, pyritään pääsääntöisesti ratkaisemaan ne kurssin yhteisessä Teams-chatissa!


### Linux-palvelimet kurssin Debian

Haaga-Helian Linux-palvelimet kurssilla käytetään Debian-käyttöjärjestelmää VirtualBox-alustalla, mikä sopii hyvin myös tälle kurssille. Edellä mainittu Ubuntu itse asiassa perustuu juuri Debianiin. Asennusohjeet Debianin asentamiseksi löydät Tero Karvisen kotisivulta https://terokarvinen.com/2021/install-debian-on-virtualbox/.



## VS Code Remote Development

Kurssilla hyödynnettävä VS Code -editori tukee "etäkehitystä" (remote development), jonka avulla on mahdollista luoda kevyitä Linux-pohjaisia kehitysympäristöjä. Myös tämä vaihtoehto voi olla toimiva ratkaisu erillisen Linux-asennuksen sijasta tai sellaisen lisäksi. Lisätietoja löydät mm. [Visual Studio Code:n ohjeista](https://code.visualstudio.com/docs/remote/containers).

Uutena vaihtoehtona GitHub tarjoaa ilmaiseksi rajatun määrän käyttöaikaa [Codespaces-palveluun](https://github.com/features/codespaces). Codespaces on edistynyt pilvipohjainen Linux- ja VS Code -kehitysympäristö, jonka avulla pääset nopeasti liikkeelle eri teknologioiden harjoittelussa.

> *"A codespace is a development environment that's hosted in the cloud. You can customize your project for GitHub Codespaces by configuring dev container files to your repository (often known as Configuration-as-Code), which creates a repeatable codespace configuration for all users of your project."*
>
> https://github.com/features/codespaces


# Ohjelmien asentaminen

Kun olet saanut kehitysympäristösi käyttökuntoon, tarvitset vielä siihen joitakin erillisiä asennuksia. Suosittelemme asentamaan aluksi ainakin Gitin, Node.js:n ja Pythonin. Suosittelemme kurssilla koodieditoriksi VS Codea, mutta saat käyttää myös muita editoreja.

Seuraavat kohdat käsittelevät tarvittavien ohjelmien asentamista erityisesti Ubuntu-ympäristössä.


## Komentorivin avaaminen

Ubuntussa useat paketit ja ohjelmat asennetaan komentorivityökaluilla. Komentorivin saat auki Ubuntun valikosta nimellä "Terminal", tai näppäinyhdistelmällä `CTRL + ALT + T`.

Mikäli komentorivin käyttö tuottaa ongelmia, hyvä tutoriaali komentorivin käytöstä löytyy osoitteessa https://ubuntu.com/tutorials/command-line-for-beginners. Voit myös aina kysyä neuvoa kurssin opettajilta ja muilta opiskelijoilta kurssin Teams-kanavilla!


## APT (Advanced Package Tool)

Ubuntun asennustyökalu on nimeltään Advanced Package Tool eli APT:

> *APT eli Advanced Package Tool on Debian-projektin kehittämä työkalu Linux-käyttöjärjestelmän pakettienhallinnan helpottamiseen. Se huolehtii mm. asennettavien pakettien riippuvuussuhteista ja niiden päivittämisestä. Se hakee asennettavat paketit netistä. APT-nimitystä käytetään sekä paketinhallintakirjastosta (jota voi käyttää monen käyttöliittymän kautta) että sitä käyttävästä komentorivityökalusta.*
>
> Linux.fi-wiki, https://www.linux.fi/wiki/APT


## Päivitysten asentaminen

> *"As always we recommend opening a terminal and running sudo apt update && sudo apt upgrade -y and then sudo snap refresh to get everything updated to the latest versions."*
>
> https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#4-explore-virtual-box

Käynnistettyäsi kehitysympäristön ensimmäistä kertaa, suosittelemme päivittämään sen pakettilistauksen ja asentamaan saatavilla olevat päivitykset:

```bash
$ sudo apt update   # downloads and updates package lists
$ sudo apt upgrade  # upgrades the existing packages on the machine
$ sudo snap refresh # upgrades packages installed with the snap tool
```

## Ohjelmien asentaminen

APT:in avulla sovellusten asennus tapahtuu kirjoittamalla komento muodossa:

    apt install ohjelma

Koska ohjelmien asennus vaatii pääkäyttäjäoikeudet, ei normaalilla käyttäjätunnuksella voida suoraan tehdä asennuksia. Yksittäisiä komentoja saa suoritettua pääkäyttäjäoikeuksilla [`sudo`-komennon avulla](https://wiki.ubuntu-fi.org/Sudo). Käytännössä tulet siis tekemään asennukset seuraavasti:

    sudo apt install ohjelma


⚠ **Huom!** APT asentaa koneellesi suoritettavia ohjelmia, joiden kanssa tulee aina huomioida myös tietoturva. Pääsääntöisesti Ubuntun pakettivarastot ovat turvallisia, mutta uusien pakettivarastojen lisääminen saattaa aiheuttaa riskejä. Tällä kurssilla teemme asennuksia vain Ubuntun omista pakettivarastoista. Voit lukea aiheesta lisää artikkelista [Can I get a virus by using "sudo apt-get install"?](https://askubuntu.com/a/818022)


## Git-asennus

Kurssilla käytetään oppimateriaalin ja esimerkkikoodien jakelussa Git-versionhallintaa. Asenna itsellesi valmiiksi Git-työkalut:

```shell
sudo apt install git
```

Asennuksen jälkeen Gitille täytyy vielä kertoa sähköpostiosoite ja nimi, joita käytetään tehdessäsi committeja. Nämä tiedot tulevat esim. GitHubin kautta kaikkien saataville, voit itse valita käytätkö oikeaa nimeäsi ja oikeaa sähköpostiosoitettasi. [GitHub tarjoaa myös mahdollisuuden käyttää anonyymiä sähköpostiosoitetta.](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address)

```bash
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

Lopuksi voit kloonata tämän repositorion itsellesi (vapaaehtoista):

```bash
$ git clone https://github.com/haagahelia/swd4tn023.git
```

⚠ **Huom!** Tehdessäsi kirjautumista vaativia operaatioita GitHubiin komentoriviltä, et voi tietoturvasyistä käyttää tunnistautumisessa käyttäjätunnusta ja salasanaa, vaan joudut luomaan itsellesi "personal access tokenin". Lue tarkempia ohjeita GitHubin ohjesivuilta: https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line. Access token ei ole välttämätön vielä tässä vaiheessa, mutta asia on hyvä huomioida tulevaisuudessa.

Jos et halua syöttää käyttäjätunnustasi ja tokenia joka kerta tehdessäsi kirjautumista vaativia Git-operaatioita, voit asettaa Gitin pitämään kirjautumistietosi muistissa:

```shell
$ git config --global credential.helper cache
```

Yllä oleva komento pitää tiedot tilapäisessä muistissa, josta ne poistuvat automaattisesti myöhemmin. Vaihtoehtoisesti voit [kirjautua GitHubiin SSH-avaimilla](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) tai asettaa Gitin [tallentamaan access tokenin tiedostoon](https://unix.stackexchange.com/questions/379272/storing-username-and-password-in-git), mitä emme suosittele.


## Node.js ja npm

Tulemme tällä kurssilla hyöyntämään Node.js-suoritusympäristöä. Node-paketeille on lisäksi oma paketinhallintasovellus nimeltä **npm** (Node Package Manager). Nämä voidaan asentaa apt-komennoilla seuraavasti:

```shell
sudo apt install nodejs
sudo apt install npm
```

APT-työkalu asentaa tyypillisesti version, joka on pitkään tuettu ja kattavasti testattu. Tämän vuoksi versiot saattavat joskus olla suhteellisen vanhoja. Halutessasi viimeisimmän version, voit käyttää myös [snap-pakettienhallintaa](https://github.com/nodejs/snap).

Asennuksen jälkeen voit lisäksi konfiguroida npm:n siten, että et tarvitse pääkäyttäjäoikeuksia globaalien pakettien asentamiseen: https://github.com/sindresorhus/guides/blob/main/npm-global-without-sudo.md.

⚠ **Huom!** NPM-paketit sisältävät suoritettavaa ohjelmakoodia, joten niiden kanssa tulee huomioida tietoturva, aivan kuten muidenkin suoritettavien ohjelmien kanssa. Tunnettujen ja laajasti käytettyjen pakettien käyttäminen voi olla turvallisempaa kuin heikommin tunnettujen tai vähäisessä käytössä olevien.


## PIP

APT-komennon lisäksi Linuxille on lukuisia muita pakettienhallintaohjelmia, joista useat ovat erikoistuneet jonkin tietyn ohjelmointikielen kirjastojen asentamiseen.

Python 3 tulee Ubuntussa valmiiksi asennettuna, mutta Python-kirjastojen asentamisessa tarvittavan `pip`-työkalun joudumme asentamaan itse:

> *pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.*
>
> https://pypi.org/project/pip/

`pip` voidaan asentaa edellä esitellyn `apt`:in ja `sudo`:n avulla seuraavasti:

```shell
sudo apt install python3-pip
```

## Visual Studio Code

Viimeisenä asennuksena suosittelemme asentamaan Visual Studio Code -kehitysympäristön. Se löytyy ilmaiseksi helpoiten Ubuntun ohjelmistokaupasta. Ohjelmistokaupan voit avata painamalla Windows-painiketta ja kirjoittamalla hakukenttään "Ubuntu Software". Etsi hakukentän avulla "Visual Studio Code" ja valitse "install".

Visual Studio Code voidaan asentaa Linuxiin myös [lukuisilla muilla tavoilla](https://code.visualstudio.com/docs/setup/linux).


<!--### VS Coden laajennokset ja asetukset

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

Lisäksi suosittelemme muuttamaan VS Code:n asetuksista koodin automaattisen muotoilun päälle tallennettaessa ja liitettäessä koodia seuraavasti:

> Avaa "User settings". Etsi hakukentän avulla valinnat `Format on save` sekä `Format on paste` ja aseta rastit molempiin ruutuihin.

**Huom!** Python-paketit sisältävät suoritettavaa ohjelmakoodia, joten niiden kanssa tulee huomioida tietoturva, aivan kuten muidenkin suoritettavien ohjelmien kanssa. Paketteja ei kannata ladata tuntemattomista lähteistä. Tunnettujen ja laajasti käytettyjen pakettien käyttäminen voi myös olla turvallisempaa kuin heikommin tunnettujen tai vähäisessä käytössä olevien. Lisätietoa pip-pakettienhallinnan turvallisuudesta löydät esimerkiksi artikkelista ["Look before you pip"](https://www.ayrx.me/look-before-you-pip).


-->

## Extra: VirtualBox Guest additions sekä leikepöydän käyttö

Perusasennuksen lisäksi suosittelemme sinua asentamaan VirtualBoxin "guest additions" -lisäosat virtualisoidulle Linux-koneelle. Lisäosien avulla esimerkiksi VirtualBox-ikkunan koon muuttaminen muuttaa automaattisesti virtualisoidun työpöydän resoluutiota ikkunan koon mukaiseksi.

Asennus tapahtuu helpoiten syöttämällä virtuaalikoneeseen virtuaalinen asennus CD virtuaalikoneen ollessa käynnissä:

![Install guest additions](guest-additions.png)

Lisää ohjeita löydät [Googlella](https://www.google.com/search?q=virtualbox+install+guest+additions).

Virtuaalikoneen ja "host"-koneen välillä on myös mahdollista synkronoida leikepöytä. Tällöin pystyt kopioimaan ja liittämään tekstiä kätevästi eri järjestelmien välillä. Käynnissä olevan virtuaalikoneen "Devices"-valikosta löytyy kohta "Shared clipboard", jonka avulla voit valita leikepöydän toimintalogiikan haluamaksesi.


## Loppusanat

Jos sait yllä olevat kohdat suoritettua, olet erinomaisesti valmistautunut kurssin tehtäviä varten. Mikäli törmäsit ongelmaan, kysythän neuvoa [Teamsissa](http://teams.microsoft.com/). Myös oppitunneilla on mahdollista kysyä neuvoa.
