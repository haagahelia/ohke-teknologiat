/**
 * Tämän esimerkin tarkoituksena on havainnollistaa olioiden monimuotoisuutta ja
 * Dependency Inversion -patternia.
 */
public class LentokoneConfig {

    private final Lentokone lentokone;
    private final Lentokone lentokone2;

    public LentokoneConfig() {
        lentokone = new Lentokone();
        Moottori moottori = new SuperMoottori();
        lentokone.setMoottori(moottori);

        lentokone2 = new Lentokone();
        Moottori moottori2 = new HalpaMoottori();
        lentokone2.setMoottori(moottori2);
    }

}

class Lentokone {
    private Moottori moottori;

    public void setMoottori(Moottori moottori) {
        this.moottori = moottori;
    }

    private void lenna() {
        moottori.kaynnista();
        moottori.kaytaMoottoria();
    }
}

interface Moottori {
    public void kaytaMoottoria();

    public boolean kaynnista();
}

class SuperMoottori implements Moottori {

    public void kaytaMoottoria() {
        // tee jotain superjuttuja
    }

    public boolean kaynnista() {
        // TODO Auto-generated method stub
        return false;
    }

}

class HalpaMoottori implements Moottori {

    public void kaytaMoottoria() {
        // aja hitaasti
    }

    public boolean kaynnista() {
        // TODO Auto-generated method stub
        return false;
    }

}
