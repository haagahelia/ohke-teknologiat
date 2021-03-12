const { getUsers, getPosts } = require('./blog/api');


async function main() {
    let userPromise = getUsers();
    let postPromise = getPosts();

    let users = await userPromise;
    let posts = await postPromise;

    for (let user of users) {
        console.log(user.name);

        for (let post of posts) {
            if (post.userId === user.id) {
                console.log(`- ${post.title}`);
            }
        }

        console.log();
    }
}

main();