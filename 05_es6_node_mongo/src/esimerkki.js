function helloAgent({ names }) {
    let { first, last } = names;
    console.log(`My name is ${last}, ${first} ${last}`);
}

// Miten kutsut yllä olevaa funktiota?
// > helloAgent({ names: { first: 'James', last: 'Bond' } })
// My name is Bond, James Bond


// Miten saat tämän funktion käyttöön muissa moduuleissa?
module.exports = helloAgent;
