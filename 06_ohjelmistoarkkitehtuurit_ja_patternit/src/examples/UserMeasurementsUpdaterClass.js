/**
 * Tässä esimerkissä on esitetty mongodb-tietokantaa potilastietoihin liittyen
 * päivittävä javascript-luokka.
 * Tässä voi havaita mm. sen että privaattien luokkametodeiden tekeminen
 * javascriptillä ei onnistu.
 * Vertailun vuoksi tämä on sama asia on toteutettu funktiona
 * [UserMeasurementsUpdaterFunction.js-tiedostossa](UserMeasurementsUpdaterFunction.js).
 */
export default class UserMeasurementsUpdater {
    constructor(userDataCollection) {//Otetaan mongodb-collection parametrina.
        this.userDataCollection = userDataCollection;//tallennetaan luokkamuuttujaan
    }

    //luokan julkisia metodeita, 3 kpl
    async userExistsInCollection(userId) {
        const cursor = await this.userDataCollection.find({ 'user.id': userId });
        return await cursor.hasNext();
    }

    async insertNewUser(userData) {
        const result = await this.userDataCollection.insertOne(userData);
        return result.insertedCount === 1;
    }

    async updateUserOperationDate(userData) {

        if (!userData.user.operationDate) {
            return false;
        }

        return await this.updateOperationDate(userData);
    }

    //luokan "sisäisiä" metodeita 2 kpl
    async updateOperationDate(userData) {
        const query = { 'user.id': userData.user.id };
        const updateDocument = {
            $set: {
                'user.operationDate': userData.user.operationDate
            }
        };
        return await this.updateDocumentWithQuery(query, updateDocument);
    }

    async updateDocumentWithQuery(query, updateDocument) {
        const result = await this.userDataCollection.updateOne(query, updateDocument);
        return result.modifiedCount >= 0;
    }
}