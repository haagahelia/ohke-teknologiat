/**
 * Tässä esimerkissä on esitetty mongodb-tietokantaa potilastietoihin liittyen
 * päivittävä javascript-funktio, joka
 * havainnollistaa myös curryttamisen periaatetta käytännössä.
 * Vertailun vuoksi tämä on sama asia on toteutettu luokkana 
 * UserMeasurementsUpdaterClass.js-tiedostossa.
 */
export default function UserMeasurementsUpdater(userDataCollection) {
    const userExistsInCollection = async (userId) => {
        const cursor = await userDataCollection.find({ 'user.id': userId });
        return await cursor.hasNext();
    }

    const insertNewUser = async (userData) => {
        const result = await userDataCollection.insertOne(userData);
        return result.insertedCount === 1;
    }

    const updateUserOperationDate = async (userData) => {
        if (!userData.user.operationDate) {
            return false;
        }

        return await updateOperationDate(userData);
    }

    const updateOperationDate = async (userData) => {
        const query = { 'user.id': userData.user.id };
        const updateDocument = {
            $set: {
                'user.operationDate': userData.user.operationDate
            }
        };
        return await updateDocumentWithQuery(query, updateDocument);
    }

    const updateDocumentWithQuery = async (query, updateDocument) => {
        const result = await userDataCollection.updateOne(query, updateDocument);
        return result.modifiedCount >= 0;
    }

    /**
     * Palautetaan tästä funktiosta kolme funktiota joille on siis curryttamisen avulla
     * bindattu oikea mongodb-collection. Huomionarvoista on myös, että 
     * tämä funktio pystyy palauttamaan "fiksuna julkisena rajapintana" vain haluamansa
     * funktiot ja loput jäävät tämän funktion privaateiksi apufunktioiksi, joista
     * kutsuvan tahon ei tarvitse tietää mitään.
     */
    return {
        userExistsInCollection,
        insertNewUser,
        updateUserOperationDate
    }
}