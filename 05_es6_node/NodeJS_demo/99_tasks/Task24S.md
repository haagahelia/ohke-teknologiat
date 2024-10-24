# Learn and add few features to the model backend - Siba

## The steps as a list first. After the list more details of each

1. **Follow given models** - All coding can be done by reading old code, and doing similar code! You don't have to invent
any new wheels. (Good way inboard a lot of new developers)
1. Think twice before adding new files. You only add new files at some steps. In other steps you just add lines to existing files.
1. Install the **Needed tools** (unless you already have everything installed)
1. **Fork** the working Siba backend repo (= create your own detached copy of the repo). Or copy the contents to a separate new repo without the .git folder.
1. Make the **database created and run** (you'll need to add the given .env file)
1. Make the Siba **backend run** (needs that same .env file)
1. Install and make the **REST Client VS Code extension** work and **test the backend** with it (you'll need to add the given settings.json file)
1. When all ready-made seems to work, add the instructed **database table** with **scripts also** for the **test data** etc.
1. Add first **new route** to the backend routing and implement the code behind it. Basically easiest is always "GET all", e.g. GET /product/    = **L**  = List
1. Add **first API test case** for that route and test it
1. Add **more test cases**, failing ones and successful ones, still for that one new route.
1. Add **second route**, e.g. GET one by id,  or:   GET /product/:id     = **R**   = Read
1. Add **input data validators** and test them with your previous and now added new REST client test cases (ok and fail cases again!)
1. (NEXT WEEK!  Add authentication and role-based method level authorization)

## Follow given models

You are given a ready full-stack architecture, with **Node.js & Express** backend written with **TypeScript** using MariaDB **RDBMS** with help of the **knex library**. After setting all up you try to follow the model and implement few backend features, finally having e.g. the following benefits:

* include security in form of login request created JWT token that needs to be provided in future request
    * **token-based authentication** and **authorization**, 
    * **token expiration** check
    * **role-based method-level authorization**
* include input parameter and **data validation** created in a modular manner
* use the Knex library to **generate SQL and run DB operations based on your TypeScript code**

# Generic information

Generic information about the used technologies, architecture etc. will be here: 

https://github.com/haagahelia/ohke-teknologiat/tree/master/05_es6_node/NodeJS_demo

## Note that YOU need to keep track of e.g. port numbers

You can e.g. look at the architecture pic and write down what are e.g. backend, database and frontend dev server ports. Most likely changes needed in some given files. So be context and settings aware!

## Needed tools

- Docker
- git
- VS Code 
    - with REST Client extension
- Locally for development and running local version of Node most likely: Nodejs, TypeScript, Nodemon, ...
- Possibly MariaDB RDBMS installed locally but only IF:
    - Dockerized version will not work
    - Teacher has not given a remote database to be used with SSH tunnel
- DBeaver Community edition. Zip downloaded and extracted to e.g. c:\users\joe\dbeaver folder. This to see whether the tables and data created.

## Fork the Siba backend repo
### Create the workspace folder

1. Create the root root folder ('Workspace folder') 'Siba'. Somewhere that is not under any git repo folder (repo folders cannot be under other repo folders)

### Fork the backend - option a) Docker - preferred

1. Go to the workspace folder 'Siba'
1. Fork/Copy there the backend project repo: https://github.com/haagahelia/Siba_be 
1. The .env files are not in repo, so create/copy the given file to backend repo root.
    - Backend needs all other info than the MARIADB_ROOT_PASSWORD but having that does not harm other than security a bit
1. Look at the docker compose files
1. Run the command ```docker-compose -f <write here the correct file name> up```
1. Test the backend by opening localhost:1111 where you replace 1111 with the real backend port. Should give a very very short error page telling "Cannot get /" or "Hello world" something like that. That means backend runs and routing works.
1. See the backend logs in the 'logs' folder

### Fork the backend - option b) non-preferred "local" / manual option

1. Go to the workspace folder 'Siba'
1. Fork/Copy there the backend project repo: https://github.com/haagahelia/Siba_be 
1. You will not get the node_modules, so you will need to move to that folder and: ```npm install```
1. Also the .env files are not in repo, so create/copy the given file to backend repo root.
    - Backend needs all other info than the MARIADB_ROOT_PASSWORD but having that does not harm other than security a bit
1. You can also run the: ```npm audit fix```   , if there would be any recent vulnerabilities.
1. Now ```npm start``` should start the backend. But still without Database connection
1. Test the backend by opening localhost:1111 where you replace 1111 with the real backend port. Should give a very very short error page telling "Cannot get /" or "Hello world" something like that. That means backend runs and routing works.
1. See the backend logs in the 'logs' folder

#### The .env file for the backend

For simplicity and avoiding too many environment probs we only use one .env file. See Teams > Files for that. Docker also, despite the documentation of claiming to support multiple .env files, seems not to support them in reality (Based on Oct 1/2024 testings). So after this semester you can try to create multiple .env files etc. using this info https://docs.docker.com/compose/environment-variables/set-environment-variables/. No prob of course is that all the containers and the processes running in them could get all env variables. 

## Database installation options

Either 

a) use the dockerized version of DB without dockerizing backend (still 'localhost' from backend point of view, need to expose the port from docker to docker host machine), or 

b) install MariaDB locally to your computer  (localhost)

c) use the given remote database (if needed and teacher has created) via tunnel. In any case you'll need to pay attention to e.g. server host address, ports, usernames, passwords, database/schema names, ... see Teams and Files tab for possible 'secret info' that might be later given if needed.

- Setup database or tunnel to remote database(from Teacher)
    - Let's see if this needed for someone for whom dockerized DB did not work and too much time spent on this case otherwise.

### Database option a) Use the dockerized version of database (or backend and database) - Preffered and easiest option

Have the .env file correctly written and located in backend folder, and run the command ```docker-compose -f <write here the correct file name> up```

**Note!** Database is created based on SQL scripts = source code, thus the whole docker container has to be started again, if want to edit the starting point SQL while developing the test data.

=> ```docker-compose -f <write here the correct file name> down```

=> does not remove the volume => need to delete the volume too, either by command line tools, or Docker Desktop!

### Database option b) Install latest 10.X (Not RC nor Beta version) version of MariaDB locally.

Write down all info about root user and passwords, ports etc. 

[Instructions on how to make a 'cold file installation' of MariaDB, Windows version, but Mac/Linux would be pretty similar, or even same?](https://github.com/haagahelia/linux-servers-etc/blob/main/mariadb_installation_local_pc.md)

### Database option c) Tunnel creation (Ask teacher if a nor b work. Not created yet)

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

## Install DBeaver Community Edition to ( 1. create DB, 2. insert and ) 3. view the inserted or changed data in the tables

(Skip if no time and database seems to work and give data)

DBeaver allows nicely the 'cold-file installation'. Just download the **zip file** and extract to some folder. E.g. c/users/susanne/dbeaver. And start the .exe application. It still writes some settings to the OS registry if allowed. Like the connection settings.

[More info about database connection set up and how to use DBeaver for basic stuff, page 11 or so](https://github.com/haagahelia/ohke-teknologiat/blob/master/05_es6_node/NodeJS_demo/01_database/CreatingDatabase_for_IdeaCaseBackend.pdf)

(In manual installation you would run some ```createSchemaAndUsers.sql``` and then ```00__CreateAllDB.sql``` via e.g. DBeaver.

Make sure to use the "Run (whole) SQL Script" command and not e.g. run (one) SQL statement.

### Set up the VS Code extension called **REST client**

1. Add the 'REST Client' extension to VS Code
1. Create a '.vscode' settings folder to the Siba root root folder. (In file explorer, or e.g. in console/shell/terminal: ```mkdir .vscode```)
    - But then open that Siba root root folder as project in VS Code, and not the Siba_be backend project folder (Which has that .vscode folder where the settings.json will later go).
    - there might be also inner .vscode folders, but they would only affect if that folder opened as VS code project.
1. Copy the given settings.json file to that folder. The tokens there are fake/expired, but you'll get the structure correct
    - make sure the file is really settings.json and not e.g. settings.json.txt
1. Now, select the REST client environment from the bottom right of the VS Code window. It needs to be selected once, before going to next step
1. Go to backend 'request' folder, and run the requests in the **1_Logins.rest** file. Sending e.g. admin-admin login request, copy the token contents carefully and paste it to the settings.json file, adminEnv token. And so on. You can copy the noroleuser token to the expiredEnv, and it will expire in .env defined time. Leave the invalidtokenEnv token as is.
1. ...then you are ready to run other tests in request folder (forget files starting with _ they are in process of being removed). You should see database data coming through via some routes?
1. Look at the ```request\GlobalSettings.rest``` or ```request\Program.rest``` as some kind of model how to implement your own test cases in the future. 
1. The 'nextId' local variable could be changed to the autogenerated id you get by running the POST. = what was the next auto-generated id going to be

**Note:** to have data in Allocation related tables you'll need to run startAllocation test case. (Or if frontend web app running) Login as admin admin and "Program results" > "Reset calculation" and "Start calculation" 

**Note:** to have data in the log tables, the logging setting in GlobalSetting table must be 1, and someone must have run the request\Allocation.rest "resetAllocation" and "startAllocation" test cases, after loggin in!. Well once someone has run it for that local database, or for that persisted **docker volume**, and there is data in log_event table, then no need to do again.

---

## NOTE THESE!

* Do NOT return anything straight from the routes. But use the ```successHandler```, ```dbErrorHandler```, ```requestErrorHandler``` etc.

* Do NOT do validations manually, look at the model and use the same model that was used before, e.g. ```validateNameObl,```
and ```[roleChecker, validate]```

* Also define what roles are able to run that feature so you can test role-based-authorization you define

* The possibly needed new TypeScript types should go to the ```types\custom.ts```

* And most IMPORTANTLY use the ```logs\app.log``` from the beginning. **Take screenshots of app.log** and the result window when you will get interesting errors and fixed operation success messages there!

---

# The additions to write and test in the backend code = real task

You will be adding a new table City (id INTEGER, name VARCHAR(200), established DATE, averageTemp DECIMAL(3,1) ). For simplicity add it to existing database. So it will be an unrelated/unlinked table. 

Add the table and its fake test data rows (10 rows or more) to the existing SQL script files. Take model from existing lines. Notice that the files 000__CreateALLdb.sql and 06__drop_tables_create_tables_insert_test_data.sql are generated by running ```sh a_concatenate_needed_db_scripts.sh``` console command in that folder. 

**Note:** Like mentioned above, just docker-compose down and up again will not work with SQL scripts that are source code in our original folder (not in the docker container!). Thus need to also delete the volume, possibly also the image while creating perfect test data.

Hint: You can always start with minimal version, e.g start with just few properties. Start with just one route. Only one view, and so on. Makes sense to minimize the re-work you might need to do.

### Features to implement (first feature is simple so that there your learn the end-point basics. Then features themselves get more non-trivial from validation and DB operation point of view)

* What are the Cities are there all in all? Easy feature as it needs maybe login, but no input in the request for the query. Database: casedb, Table: City

* What cities have "burg" in their name? (hard-coded in the request) 

* What rows there are that are mentioning something you give in the request. = request should include, in body JSON data or URL :searchText parameter. If the ```LIKE %``` matches, those rows are returned.

* Which cities were established before the date you give in the request? (Date given in POST JSON data or URL parameter)?

**See the given PDF example about analyzing one Program route in Teams**

See the Files tabs.

That should give an idea how much code is needed per one new route.

1. add a new file ```src/routes/city.ts```
1. add routing ```'/city'``` to that file, in file ```src/routes/index.ts```
1. following the models in e.g. in Program related route and validation code...
1. add the suggested/required new routes from above ONE by ONE.
    1. add the endpoint and routing to it
        1. the database operation development should be always started by doing something easy that works, and then making it more specific. E.g. first list everything, and only after that tested and works put there the WHERE conditions.
    1. add the REST client test(s) for it
    1. add validation components to validationHandler folder, new file ```city.ts``` IF needed by that endpoint (e.g. mere 'GET all' does not need any input, just URL = no input validation)
    1. if added validation, test it again. Try to make it fail and show the logs!


#### ---- EXPRESS VALIDATOR ----
Express-validator is a library that can be used to validate the data coming from the frontend or other client (like that REST Client extension):
https://express-validator.github.io/docs/

New express-validator validation ideas could contain e.g.: 
 - ```.isEmail()```   (currently the email allows test values: admin etc. But just for making dev testing faster)
 - ```.contains("-")```
 - ```.isDate()```
 - ```.isISO8601```


# -------------------------------------------------

### EXTRA: (Totally extra, just if feel like finding out what the Frontend does currently) 

#### Install the frontend  (Possible but not really needed for the task) Skip if no extra time!  )))

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




<!-- 
# Old task about log tables

You will be adding an API end-point for most/some of these features: 

(first one is simple so that there your learn the end-point basics. Then
features themselves get more non-trivial from validation and DB operation point of view)

* What are the database logged events there are all in all? (Hope you won't confuse the logEvent concept with the logs file and e.g. app.log) Easy feature as it needs maybe login, but no input in the request for the query. Database: casedb, Table: log_event

* What rows there are about room id ```1025```? (hard-coded in the request) 

* What rows there are that are mentioning something you give in the request. = request should include, in body JSON data or URL :searchText parameter. If the ```LIKE %``` matches, those rows are returned.

* What warnings there are that are from given date (given in POST JSON data or URL parameter)? Either use the date part of datetime and match it to given date OR use some time difference function

**See the given PDF example about analyzing one Program route in Teams**

See the Files tabs.

That should give an idea how much code is needed per one new route.

1. add a new file ```src/routes/logEvent.ts```
1. add routing ```'/logEvent'``` to that file, in file ```src/routes/index.ts```
1. following the models in e.g. in Program related route and validation code...
1. add the suggested/required new log_event routes ONE by ONE.
    1. add the endpoint and routing to it
        1. the database operation development should be always started by doing something easy that works, and then making it more specific. E.g. first list everything, and only after that works put there WHERE conditions.
    1. add the REST client test(s) for it
    1. add validation components to validationHandler folder, new file ```logEvent.ts``` IF needed by that endpoint (e.g. mere 'GET all' does not need any input, just URL = no input validation)
    1. if added validation, test it again. Try to make it fail and show the logs!

-->