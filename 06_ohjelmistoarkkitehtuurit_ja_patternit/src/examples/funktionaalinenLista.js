/**
 * Tämän esimerkin tarkoituksena on havainnollistaa funktionaalista ohjelmointityyliä
 * ja vertailukohtaa olio-ohjelmoinnin vastaavaan toteutukseen. Funktionaalinen toteutus on tehty
 * kahdella tavalla, toinen hyödyntää javascriptin reduce-funktiota.
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

//Annetaan tämä javascriptin reduce-funktiolle
const laskeEsiintymatReduceVersio = (acc, val) => {
    if (acc[val]) {
        return { ...acc, [val]: acc[val] + 1 }
    }
    return { ...acc, [val]: 1 }
}

//Annetaan reduce-funktiolle myös curryttamalla vertailufunktio
const laskeEsiintymatReduceVersioAvainFunktiolla = (uniikkiAvainFunktio) => (acc, val) => {
    if (acc[uniikkiAvainFunktio(val)]) {
        return { ...acc, [uniikkiAvainFunktio(val)]: acc[uniikkiAvainFunktio(val)] + 1 }
    }
    return { ...acc, [uniikkiAvainFunktio(val)]: 1 }
}

const numeroLista = [1, 2, 3, 1];
console.log(laskeEsiintymat(numeroLista, (a) => a))

const reduceVersioNumeroLista = numeroLista.reduce(laskeEsiintymatReduceVersio, {})
console.log(`reduce versio numerolistasta: ${JSON.stringify(reduceVersioNumeroLista)}`)

const stringLista = ["Pekka", "Maija", "Elina", "Pekka"];
console.log(laskeEsiintymat(stringLista, (a) => a))

const reduceVersioStringLista = stringLista.reduce(laskeEsiintymatReduceVersio, {})
console.log(`reduce versio stringlistasta: ${JSON.stringify(reduceVersioStringLista)}`)

const autoLista = [{ id: 1, merkki: "Volvo" },
{ id: 2, merkki: "Mersu" }, { id: 3, merkki: "BMW" }, { id: 4, merkki: "Volvo" }];
console.log(laskeEsiintymat(autoLista, (a) => a.merkki))

const reduceVersioAutoLista = autoLista.reduce(laskeEsiintymatReduceVersioAvainFunktiolla((a) =>
    a.merkki), {})
console.log(`reduce versio autolistasta: ${JSON.stringify(reduceVersioAutoLista)}`)


