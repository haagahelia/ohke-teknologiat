
/**
 * 
 * Järjestelmässämme on yksi moottoripyörä (vm. 2015, ajetut kilometrit
 * 20500 ja se ei ole kevytmoottoripyörä).
 * 
 * Järjestelmässä on myös yksi auto (vm. 2018, ajetut kilometrit 
 * 56000 ja se on farmariauto).
 * 
 * Sinun tehtäväsi olisi refaktoroida tiedostossa olevat luokat
 * siten, että järjestelmän arkkitehtuuri seuraa
 * Dependency inversion-periaatetta (DIP) hyödyntäen olioiden
 * monimuotoisuutta ja samalla 
 * BusinessLuokalla voidaan käsitellä sekä Moottoripyöriä että Autoja.
 * Itse BusinessLuokasta voi olla järjestelmässä useampi instanssi, 
 * toinen moottoripyörille ja toinen autoille.
 * 
 * Kaikki luokat on kirjoitettu tehtävän palautuksen helpottamiseksi samaan
 * tiedostoon.
 * 
 * Tiedoston voi kääntää komennolla: "javac DIPTehtava.java"
 * Kun kääntäminen on onnistunut, niin luodun .class-luokan voi ajaa 
 * komennolla: "java DIPTehtava".
 */

import java.util.Calendar;

/**
 * Tämä on ohjelman käyttöliittymä, joka tulostaa haluamamme asiat. Tätä luokkaa
 * ei tarvitse muuttaa.
 */
public class DIPTehtava {

    private static BusinessLuokka businessLuokkaAutolle = DIPConfigurator.konfiguraatioAutolle();

    private static BusinessLuokka businessLuokkaMoottoripyoralle = DIPConfigurator.konfiguraatioMoottoripyorille();

    public static void main(String[] args) {
        System.out.println("Järjestelmän autolla on " + "ajettu keskimäärin vuodessa: "
                + businessLuokkaAutolle.laskeKeskimaaraisetKilometritPerVuosi() + " kilometriä");

        System.out.println("Järjestelmän moottoripyörälla on " + "ajettu keskimäärin vuodessa: "
                + businessLuokkaMoottoripyoralle.laskeKeskimaaraisetKilometritPerVuosi() + " kilometriä");
    }
}

/**
 * Tämän konfiguraattoriluokan tehtävä on rakentaa sovelluksen konfiguraatio.
 * Jos sovelluksesta halutaan erilainen konfiguraatio, niin tarvitsee muuttaa
 * vain tätä luokkaa, ei itse sovelluksen luokkia. Sovelluksen määrittelyt
 * voitaisiin myös antaa esimerkiksi XML-tiedostossa, jonka tämä luokka sitten
 * lataisi ja käsittelisi. Esim. Springissä on vastaava luokka.
 */
class DIPConfigurator {

    public static BusinessLuokka konfiguraatioAutolle() {
        BusinessLuokka businessLuokkaAutolle = new BusinessLuokka();
        // TODO: Konfiguroi luokka tässä järjestelmän Autolla
        return businessLuokkaAutolle;
    }

    public static BusinessLuokka konfiguraatioMoottoripyorille() {
        BusinessLuokka businessLuokkaMoottoripyoralle = new BusinessLuokka();
        // TODO: Konfiguroi luokka tässä järjestelmän Moottoripyoralla
        return businessLuokkaMoottoripyoralle;
    }
}

/**
 * Ajoneuvo-rajapinta
 */
interface Ajoneuvo {
    public int getAjetutKilometrit();

    public int getVuosimalli();
}

/**
 * Auto-luokka toteuttaa Ajoneuvo-rajapinnan asioita ja lisäksi sillä on
 * pelkästään Auto-tyyppiin liittyviä asioita 1 kpl.
 */
class Auto implements Ajoneuvo {
    private int km;
    private int vuosimalli;
    private boolean onkoFarmari;

    public Auto(int km, int vuosimalli, boolean onkoFarmari) {
        this.km = km;
        this.vuosimalli = vuosimalli;
        this.onkoFarmari = onkoFarmari;
    }

    public int getAjetutKilometrit() {
        return this.km;
    }

    public int getVuosimalli() {
        return this.vuosimalli;
    }

    public boolean onkoFarmari() {
        return this.onkoFarmari;
    }
}

/**
 * Moottoripyora-luokka toteuttaa Ajoneuvo-rajapinnan asioita ja lisäksi sillä
 * on pelkästään Moottoripyora-tyyppiin liittyviä asioita 1 kpl.
 */
class Moottoripyora implements Ajoneuvo {
    private int km;
    private int vuosimalli;
    private boolean onkoKevytMoottoripyora;

    public Moottoripyora(int km, int vuosimalli, boolean onkoKevytMoottoripyora) {
        this.km = km;
        this.vuosimalli = vuosimalli;
        this.onkoKevytMoottoripyora = onkoKevytMoottoripyora;
    }

    public int getAjetutKilometrit() {
        return km;
    }

    public int getVuosimalli() {
        return vuosimalli;
    }

    public boolean onkoKevytMoottoripyora() {
        return this.onkoKevytMoottoripyora;
    }
}

/**
 * Tämä luokka sisältää järjestelmän businesslogiikan, eli oikestaan sen kaikean
 * kiinnostavan järjestelmässä, mitä tuoteomistaja on meille määritellyt.
 */
class BusinessLuokka {
    /**
     * FIXME: Tämä on väärä paikka sanoa new avainsana, nyt BusinessLuokka riippuu
     * Auto-luokasta. Tämä luokka siis alustetaan tässä kiinteästi autolla. Mitä jos
     * haluaisin saman BusinessLuokan käsittelevänkin järjestelmän moottoripyörää?
     */
    Auto auto = new Auto(56000, 2018, true);

    public int laskeKeskimaaraisetKilometritPerVuosi() {
        return auto.getAjetutKilometrit() / (Calendar.getInstance().get(Calendar.YEAR) - auto.getVuosimalli());
    }

    // FIXME: Vinkki, tämmöinen metodi tarvitaan tähän luokkaan.
    public void setAjoneuvo(Ajoneuvo ajoneuvo) {

    }
}
