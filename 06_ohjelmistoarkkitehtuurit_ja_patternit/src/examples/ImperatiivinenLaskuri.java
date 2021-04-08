import java.util.LinkedList;
import java.util.List;

/**
 * Lasketaan imperatiivisilla komennoilla lasku (1+(2*(3+2))) = 11. Tarkoitus on
 * havainnollistaa eri ohjelmointiparadigmojen eroja. Tämä imperatiivinen
 * toteutus on vain lista suoritettavia asioita tietokoneelle, ja toteutus
 * paljastaa enemmän "tietokoneen arkkitehtuurista" kuin itse ratkaistavan
 * ongelman arkkitehtuurista.
 * 
 * Vrt. FunktionaalinenLaskuri.js ja Oliolaskuri.java.
 * 
 * NOTE: Koodi on huonoa ja bugista.
 */

public class ImperatiivinenLaskuri {
    public static void main(final String[] args) {

        // Lähdetään allokoimaan tietokoneen muistista tarvittava tila ja sijoittamaan
        // sinne haluamamme asiat. Emme siis kuvaa ratkaisemaamme ongelmaa, vaan
        // kerromme tietokoneen ymmärtämällä tavalla mitä sen pitää tehdä.
        String[] luvutJaOperaatiot = { "3", "sum", "2", "mul", "2", "sum", "1" };

        int tulos = Integer.parseInt(luvutJaOperaatiot[0]);

        // Tämä for looppii siis käy muistiin sijoittamamme asiat yksi kerrallaan läpi
        // ja if lauseilla selvittää että mitä minkäkinlaiselle asialle pitää tehdä.
        // Tämä ei mallinna tai kuvaa varsinaista ongelmakenttäämme juuri
        // mitenkään vaan antaa vain tietokoneelle ohjeita meidän ongelmatapauksemme
        // ratkaisun laskemiseksi vaihe kerrallaan. Tämä koodin laajentaminen
        // tai hyödyntäminen samankaltaisten ongelmien ratkaisuun olisi vaikeaa.
        for (int i = 1; i < luvutJaOperaatiot.length; i++) {
            if (luvutJaOperaatiot[i].equals("sum") || luvutJaOperaatiot[i].equals("mul")) {
                if (luvutJaOperaatiot[i].equals("sum")) {
                    tulos = tulos + Integer.parseInt(luvutJaOperaatiot[i + 1]);
                } else {
                    tulos = tulos * Integer.parseInt(luvutJaOperaatiot[i + 1]);
                }
            }
        }

        System.out.println("Summa = " + tulos);
    }
}
