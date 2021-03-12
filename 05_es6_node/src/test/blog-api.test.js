const assert = require('assert');
const { getUsers, getPosts } = require('../blog/api');

describe('Getting users', function () {
    it('Gets ten users from API', function (done) {
        getUsers().then(users => {
            assert.strictEqual(users.length, 10);
            done();
        });
    });

    it('Gets 100 posts from API', async function () {
        let posts = await getPosts();
        assert.strictEqual(posts.length, 100);
    });
});