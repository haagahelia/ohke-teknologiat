/**
 * Tämän esimerkin tarkoituksena on havainnollistaa funktionaalista ohjelmointityyliä
 * ja vertailukohtaa olio-ohjelmoinnin vastaavaan toteutukseen.
 * Vrt. Listaesimerkki.java
 * */

const laskeEsiintymat = (lista, uniikkiAvainFunktio, esiintymaMap = {}) => {
    if (lista.length < 1) {
        return esiintymaMap
    }

    const avain = uniikkiAvainFunktio(lista[0])
    const uusiArvoAvaimelle = esiintymaMap[avain] ? (esiintymaMap[avain] + 1) : 1

    //Luodaan aina uusi map, hyödynnettään ES6 computed propertya avaimen kanssa.
    return laskeEsiintymat(lista.slice(1),
        uniikkiAvainFunktio, { ...esiintymaMap, [avain]: uusiArvoAvaimelle })
}


const numeroLista = [1, 2, 3, 1];
console.log(laskeEsiintymat(numeroLista, (a) => a))

const stringLista = ["Pekka", "Maija", "Elina", "Pekka"];
console.log(laskeEsiintymat(stringLista, (a) => a))

const autoLista = [{ id: 1, merkki: "Volvo" },
{ id: 2, merkki: "Mersu" }, { id: 3, merkki: "BMW" }, { id: 4, merkki: "Volvo" }];
console.log(laskeEsiintymat(autoLista, (a) => a.merkki))


