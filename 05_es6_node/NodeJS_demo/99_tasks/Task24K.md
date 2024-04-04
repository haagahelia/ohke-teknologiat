# Install the model backend - Siba and add few features to it

## Following given models

You will get a ready full-stack architecture, with Node.js backend written with TypeScript using MariaDB RDBMS. After setting all up you try to follow the model and implement few backend features have following benefits:

* include security in form of login request created JWT token that needs to be provided in future request
    * token based authentication and authorization, 
    * token expiration check
    * role-based method-level authorization
* include input parameter and data validation created in modular manner
* use Knex library to run DB operations (programmed with TypeScript)

Generic information about the case database and used technologies will be here: 

https://github.com/haagahelia/ohke-teknologiat/tree/master/05_es6_node/NodeJS_demo

## Needed tools

- Docker
- git
- VS Code 
    - with REST Client add-on
- Locally most likely: Nodejs, TypeScript, Nodemon, ...
- Possibly MariaDB RDBMS installed locally if:
    - Dockerized version will not work
    - Teacher has not given a remote database to be used with SSH tunnel

## Create the workspace folder

1. Create the root root folder ('Workspace folder') 'Siba'. Somewhere that is not under any git repo folder (repo folders cannot be under other repo folders)

### Install the backend

1. Go to the workspace folder 'Siba'
1. Clone there the backend project repo: https://github.com/haagahelia/Siba_be
1. You will not get the node_modules, so you will need to move to that folder and: ```npm install```
1. Also the .env files are not in repo, so create/copy the given files to backend repo root.
    - Backend needs all other info than the MARIADB_ROOT_PASSWORD but having that does not harm other than security a bit
1. You can also run the: ```npm audit fix```   , if there would be any recent vulnerabilities.
1. Now ```npm start``` should start the backend. But still without Database connection
1. See the backend logs in the 'logs' folder

#### The .env file for the backend

For simplicity and avoiding too many environment probs we only use one .env file. See Teams > Files for that.

After this weekly task you can create multiple .env files etc. using this info https://docs.docker.com/compose/environment-variables/set-environment-variables/ .  But now let's go a bit non-secure demo way.

## Database installation options

Either 

a) install MariaDB locally to your computer  (localhost), or 

b) use the dockerized version of DB without dockerizing backend (localhost still from backend point of view, need to expose the port from docker to host machine), or 

c) use the given remote database (if needed and teacher has created) via tunnel. In any case you'll need to pay attention to e.g. server host address, ports, usernames, passwords, database/schema names, ... see Teams and Files tab for possible 'secret info' that might be later given if needed.

- Setup database or tunnel to remote database(from Teacher)
    - Let's see if this needed for someone for whom dockerized DB did not work and too much time spent on this case otherwise.

### Database option a) Install latest 10.X (Not RC nor Beta version) version of MariaDB locally.

Write down all info about root user and passwords, ports etc. Run the ```createSchemaAndUsers.sql``` and then ```00__CreateAllDB.sql``` via e.g. DBeaver.

Make sure to use the "Run (whole) SQL Script" command and not e.g. run (one) SQL statement.

[Instructions on how to make a 'cold file installation' of MariaDB, Windows version, but Mac/Linux would be pretty similar, or even same?](https://github.com/haagahelia/linux-servers-etc/blob/main/mariadb_installation_local_pc.md)

### Database option b) Use the dockerized version of database (or backend and database)

Have the .env file correctly written and located in backend folder, and run the command ```docker-compose -f docker-compose-db.yaml up```

Currently the .env for local DB and dockerized DB might be exactly same? As long as the backend is NOT dockerized. Check from teacher for any doubts in env settings!

### Database option c) Tunnel creation (let's see if any need this time. Not created yet)

1. This console command in Windows would create a ssh tunnel / port forwarding if you will use remote database:
    - ```ssh -f juuser1@123.123.123.45 -L 3308:localhost:3306 -N```
    - The local port in your computer would thus be 3308, 
    - and in the remote computer we would target 3306 where MariaDB database typically exists. 
    - **Note**: all info here is incorrect as correct info cannot be published in the github repo. 
    - **See Teams for correct information = secrets**. 
    - If everything goes correctly this command does not return anything to see. 
    - You can run ```ps -a``` to see if ssh process exists, and kill it with ```kill -9 1234``` if the process id was 1234.

1. Backend .env file must match your database: 
    1. The database server (or tunnel) address, typically localhost, could be mariadb_service if connecting from dockerized backend service created also with docker compose
    1. The database server (or tunnel) port, typically 3306, 3308, 3315 or so
    1. The database user, in our case could be e.g. jyser3, but you have possibly created something different. Note this is almost never same as a Linux user connecting to the Linux computer
    1. The database user's password. Note it's not the Linux password, but database password
    1. The database/schema name, e.g. casedb, ideacasedb, must be correct too
    1. The MARIADB_ROOT_PASSWORD is used only while creating the dockerized MariaDB DB. No need to be same as local DB root password. Should be diffent.

So just calm down and think through and make sure you have all details correctly.

### Install DBeaver to ( 1. create DB, 2. insert and ) 3. read the data in the tables

More info about database connection set up and how to use DBeaver here:

https://github.com/haagahelia/ohke-teknologiat/tree/master/05_es6_node/NodeJS_demo

### Set up the VS Code REST client

1. Add the 'REST Client' add-on to VS Code
1. Create a '.vscode' settings folder to the Siba root root folder. (In file explorer, or e.g. in console/shell/terminal: ```mkdir .vscode```)
1. Copy to that folder the given settings.json file. The tokens there are fake/expired, but you get the structure correct
1. Go to backend 'request' folder, and run the requests in the 1_Logins.rest file. And copy the token you get by running e.g. admin-admin to the settings.json file, adminEnv token. And so on. You can copy the noroleuser token to the expiredEnv, and it will expire in maybe one hour.
1. Now, if you select the REST client environment from the bottom right of the VS Code window. It needs to be selected once, before going to next step
1. ...then you are ready to run other tests in request folder (forget files starting with _ they are in process of being removed)
1. Look at the ```request\GlobalSettings.rest``` as some kind of model. 
1. The nextId variable needs to be changed to the autogenerated id you get by running the POST.

**Note:** to have data in the log_event table, the logging setting in GlobalSetting table must be 1, and someone must have run the Program results Reset calculation and Start calculation. (Or someone has run the request\Allocation.rest reset and start allocation test cases, after loggin in!) 

Well once someone has, and there is data in log_event table, no need to do again.


### The additions to write and test in the backend code

You will be adding API end point and routing for most/some of these features: (learning makes faster soon)

* what are the database logged events there are all in all? (don't mix it with the logs file and e.g. app.log) Easy feature as it needs maybe login, but no input in the request for the query. Database: casedb, Table: log_event

* what rows there are about room id ```1025```? (hard-coded in the request) 

* what rows there are that are mentioning something you give in the request. = request should include, in body or URL 'searchText' and if the ```LIKE %``` matches, those rows are returned.

* what warnings there are that are from given date? Either use the date part of datetime and match it to given date OR use some time difference function

1. add a new file ```src/routes/logEvent.ts```
1. add routing ```'/logEvent'``` to that file, in file ```src/routes/index.ts```
1. following the models in e.g. in Subject related route and validation code...
1. add the suggested/required new log_event routes ONE by ONE.
    1. add the endpoint and routing to it
        1. the database operation should be always started by doing something easy that works, and then making it more specific. E.g. first list everything, and only after that works put there WHERE conditions.
    1. add the REST client test(s) for it
    1. add validation components to validationHandler folder, new file ```logEvent.ts``` IF needed by that endpoint (e.g. mere 'GET all' does not need any input, just URL = no input validation)
    1. if added validation, test it again. Try to make it fail and show the logs!

#### ---- EXPRESS VALIDATOR ----
Express-validator is a library that can be used to validate the data coming from the frontend or other client:
https://express-validator.github.io/docs/

New validation ideas could contain e.g. ```.isEmail()``` or ```.contains("-")``` 

## NOTE THESE

* Do NOT return anything straight from the routes. But use the ```successHandler```, ```dbErrorHandler```, ```requestErrorHandler``` etc.

* Do NOT do validations manually, look at the model and use the same model that was used before, e.g. ```validateNameObl,```
and ```[roleChecker, validate]```

* Also define what roles are able to run that feature so you can test role-based-authorization you define

* Possible needed new TypeScript types can go to the ```types\custom.ts```

* And most IMPORTANTLY use the ```logs\app.log``` from the beginning. Take screenshots when get interesting errors and fixed operation success messages there!

# ------------------------------------

### ((( Install the frontend  (Possible but not really needed for the task) Skip if no extra time!  )))

1. Go to the workspace folder 'Siba'
1. Clone there the frontend project repo: https://github.com/haagahelia/siba-fe
1. You will not get the node_modules, so you will need to move to that folder and: ```npm install```
1. Also the .env file is not in repo, so create/copy that given file contents to frontend repo root
1. You can also run the: ```npm audit fix```   , if there would be any recent vulnerabilities.
1. ```npm start``` would start the application 
1. and with logout/login you can use e.g. email: "admin", password: "admin" to log in.
1. 

(using the running frontend)
- http://localhost:8753/subject
- if want to login: http://localhost:8753/login
and admin   -   admin
- then go to Allocation, open e.g. 10004 and then
in the dialog press "Pick Allocation"
- http://localhost:8753/subject
- then to Program results and press "Reset allocation",
"Start allocation".
