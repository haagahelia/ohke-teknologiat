/**
 * Lasketaan funktionaalisen ohjelmoinnin mukaan mallinnetulla laskurilla (1+(2*(3+2))) = 11.
 * Tarkoitus olisi havainnollistaa miten voimme funktionaalisen paradigman avulla vain
 * määritellä lopputuloksen funktioiden avulla ja laskenta tapahtuu kuin itsestään.
 * Vrt. Oliolaskuri.java
 */

const sum = (x1, x2) => x1 + x2;
const mul = (x1, x2) => x1 * x2;

/**
 * tulos-muuttujaan tuleva arvo on siis määritelty deklaratiivisesti, eikä tarvitse kutsua erikseen esim.
 * jotain laske()-funktiota, joka siis imperatiivisesti käskisi ohjelmaa tekemään jotain.
 * Funktioita ja muuttujia käsitellään samalla tavalla "first class citizens":einä, jolloin 
 * siis toinen funktio voi ottaa parametrikseen myös toisen funktion siinä missä esimerkiksi
 * int-arvon.
 */
const tulos = sum(1, mul(2, sum(3, 2)));

console.log(tulos);
