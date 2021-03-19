import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.LinkedList;

/**
 * Tämän esimerkin tarkoituksena on havainnollistaa olioiden monimuotoisuutta ja
 * rajapintojen käyttämistä.
 */
public class ListaesimerkkiEiMonimuotoinenVersio {

    public static void main(final String[] args) {
        List<Integer> numeroLista = new LinkedList<>();
        numeroLista.add(1);
        numeroLista.add(2);
        numeroLista.add(3);
        numeroLista.add(1);
        System.out.println(laskeEsiintymat(numeroLista));

    }

    /**
     * 
     * 
     * @param list
     * @return Metodi palauttaa Mapin, jossa on avaimena parametrina saadun Listan
     *         objekti ja keynä lukumäärä kuinka monta samaa objektia listassa oli.
     */
    private static Map<Integer, Integer> laskeEsiintymat(List<Integer> list) {
        Map<Integer, Integer> tulos = new HashMap<>();
        for (Integer numero : list) {
            if (tulos.containsKey(numero)) {
                tulos.put(numero, tulos.get(numero) + 1);
            } else {
                tulos.put(numero, 1);
            }
        }
        return tulos;
    }
}