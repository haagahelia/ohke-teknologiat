/*Tässä tehtävässä on tarkoitus rakentaa pieni scripti 
värien lisäämiseen ja poistamiseen säiliöstä Reduxin periaatteiden mukaisesti. 
Lopulta scriptin pitäisi siis tulosta "keltainen", "vihreä"
Muista ajaa ensin src-kansiossa komento "npm install"
Voit ajaa tämän tiedoston komennolla "node Reduxperiaatteet.js" tai "npm run build"
*/

//import Redux from 'redux' //ES6 syntaksilla voisi tehdä näin

const Redux = require('redux')

//Action 1
function addColor(value){
    return{
        type: "", //FIXME
        color: null //FIXME
    };
}

//Action 2
function removeColor(value){
    return{
        type: "", //FIXME
        color: null //FIXME
    };
}

//Pohja reducerille, ota edellinen tila ja Action ja palauta uusi tila
function favoriteColors(state, action){ 
    //tämä reducer-funktio on siis "idealtaan samantapainen" kuin funktionaalisen ohjelmoinnin 
    //reduce-funktio, eli Array.prototype.reduce(reducer, ?initialValue)
    if(state == undefined){
        state = []
    }

    if(action.type === "ADD"){
        return state.concat(action.color);
    }else if(action.type === "REMOVE"){
        return state.filter(function(item){ 
            //selvitä tarvittaessa miten toimii funktionaalisen ohjelmoinnin filter-funktio
            return null //FIXME
        });
    }else{
        return state;
    }
}

//Luodaan redux-säiliö ja käytetään sitä
let store = Redux.createStore(favoriteColors);
store.dispatch(addColor("sininen"));
store.dispatch(addColor("keltainen"));
store.dispatch(addColor("vihreä"));
store.dispatch(removeColor("sininen"));

console.log(store.getState()); //pitäisi tulla tuloste ['keltainen', 'vihreä']

