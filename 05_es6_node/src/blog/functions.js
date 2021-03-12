function getPostsByUser(user, posts) {
    return posts.filter(post => post.userId === user.id);
}

function combineUsersAndPosts(users, posts) {
    return users.map(user => {
        return { ...user, posts: getPostsByUser(user, posts) };
    });
}

module.exports = { combineUsersAndPosts, getPostsByUser };
