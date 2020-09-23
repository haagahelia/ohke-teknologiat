import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.LinkedList;

/**
 * Tämän esimerkin tarkoituksena on havainnollistaa olioiden monimuotoisuutta ja
 * rajapintojen käyttämistä.
 */
public class Listaesimerkki {

    public static void main(final String[] args) {
        List<Integer> numeroLista = new LinkedList<>();
        numeroLista.add(1);
        numeroLista.add(2);
        numeroLista.add(3);
        numeroLista.add(1);
        System.out.println(laskeEsiintymat(numeroLista));

        List<String> tekstiLista = new LinkedList<>();
        tekstiLista.add("Pekka");
        tekstiLista.add("Maija");
        tekstiLista.add("Elina");
        tekstiLista.add("Pekka");
        System.out.println(laskeEsiintymat(tekstiLista));

    }

    /**
     * 
     * 
     * @param list
     * @return Metodi palauttaa Mapin, jossa on avaimena parametrina saadun Listan
     *         objekti ja keynä lukumäärä kuinka monta samaa objektia listassa oli.
     */
    private static Map<Object, Integer> laskeEsiintymat(List<?> list) {
        Map<Object, Integer> tulos = new HashMap<>();
        for (Object object : list) {
            if (tulos.containsKey(object)) {
                tulos.put(object, tulos.get(object) + 1);
            } else {
                tulos.put(object, 1);
            }
        }
        return tulos;
    }
}