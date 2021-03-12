const assert = require('assert');
let { getPostsByUser, combineUsersAndPosts } = require('../blog/functions.js');

describe('Getting posts for specific user', function () {
    it('Filters posts for given user', function () {
        let user = { id: 1 };
        let posts = [{ id: 1, userId: 1 }, { id: 2, userId: 1 }, { id: 3, userId: 2 }];

        let result = getPostsByUser(user, posts);

        assert.deepStrictEqual(result, [{ id: 1, userId: 1 }, { id: 2, userId: 1 }]);
    });
});

describe('Combining arrays of posts and users', function () {
    it('Adds a list of posts for each user', function () {
        let users = [{ id: 1 }, { id: 2 }];
        let posts = [{ id: 1, userId: 1 }, { id: 2, userId: 1 }];

        let result = combineUsersAndPosts(users, posts);

        assert.deepStrictEqual(result, [
            {
                id: 1,
                posts: [{ id: 1, userId: 1 }, { id: 2, userId: 1 }]
            },
            {
                id: 2,
                posts: []
            }
        ]);
    });
});
