import java.util.LinkedList;
import java.util.List;

/**
 * Lasketaan proseduraalisilla komennoilla lasku (1+(2*(3+2))) = 11. Tarkoitus
 * on havainnollistaa eri ohjelmointiparadigmojen eroja. Vrt.
 * FunktionaalinenLaskuri.js ja Oliolaskuri.java. NOTE: Koodi on huonoa ja
 * bugista.
 */

public class ImperatiivinenLaskuri {
    public static void main(final String[] args) {
        List luvutJaOperaatiot = new LinkedList();

        luvutJaOperaatiot.add(3);
        luvutJaOperaatiot.add("sum");
        luvutJaOperaatiot.add(2);
        luvutJaOperaatiot.add("mul");
        luvutJaOperaatiot.add(2);
        luvutJaOperaatiot.add("sum");
        luvutJaOperaatiot.add(1);

        int tulos = (int) luvutJaOperaatiot.get(0);

        for (int i = 1; i < luvutJaOperaatiot.size(); i++) {
            if (luvutJaOperaatiot.get(i) instanceof String) {
                if (luvutJaOperaatiot.get(i).equals("sum")) {
                    tulos = tulos + (int) luvutJaOperaatiot.get(i + 1);
                } else {
                    tulos = tulos * (int) luvutJaOperaatiot.get(i + 1);
                }
            }
        }

        System.out.println("Summa = " + tulos);
    }
}
