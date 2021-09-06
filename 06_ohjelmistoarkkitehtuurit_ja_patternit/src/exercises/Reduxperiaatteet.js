/*Tässä tehtävässä on tarkoitus rakentaa pieni skripti 
rahasummien lisäämiseen ja poistamiseen säiliöstä Reduxin periaatteiden mukaisesti. 
Lopulta scriptin pitäisi siis tulostaa summa 50.
Muista ajaa ensin src-kansiossa komento "npm install"
Voit ajaa tämän tiedoston komennolla "node Reduxperiaatteet.js" tai "npm run build"
HUOM: Tämä nykyinen versio ilman korjauksia heittää Redux-kirjastolta virheen, eli se ei
suostu ajamaan sellaisenaan ilman muutoksia.
*/

//import Redux from 'redux' //ES6 syntaksilla voisi tehdä näin

const Redux = require('redux')

//Action 1
function removeMoney(value) {
    return {
        type: "", //FIXME
        amount: null //FIXME
    };
}

//Action 2
function addMoney(value) {
    return {
        type: "", //FIXME
        amount: null //FIXME
    };
}

/*
Pohja reducerille, ota edellinen tila ja Action ja palauta uusi tila.
Tämä reducer-funktio on siis "idealtaan samantapainen" kuin funktionaalisen ohjelmoinnin 
reduce-funktio eli Array.prototype.reduce(reducer, ?initialValue)
*/
function moneyReducer(state, action) {
    if (state == undefined) {
        state = 0
    }

    if (action.type === "ADD") {
        return state + action.amount;
    } else if (action.type === "REMOVE") {
        return 0 //FIXME
    } else {
        return state;
    }
}

//Luodaan redux-säiliö ja käytetään sitä
let store = Redux.createStore(/*reducerFunktio*/);//FIXME: createStorelle pitää antaa parametriksi reducer-funktio
store.dispatch(addMoney(50));
store.dispatch(addMoney(50));
store.dispatch(removeMoney(50));

console.log(store.getState()); //pitäisi tulla tuloste 50

