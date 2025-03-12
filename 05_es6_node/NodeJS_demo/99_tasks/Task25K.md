# Learn and add few features to the model backend - Siba

## The principles and themes as a list first. After the list more details of each

1. **Follow given models** - All coding can be done by reading old code, and doing similar code! You don't have to invent
any new wheels. (Good way inboard a lot of new developers)
1. Think twice before adding new files. You only add new files at some steps. In other steps you just add lines to existing files.
1. Install the **Needed tools** (unless you already have everything installed)
1. **Fork** the working Siba backend repo (= create your own detached copy of the repo) (and then clone your own repo to laptop). Or copy the contents to a separate new repo without the .git folder. (Done in the task 1 already)
1. Make the **database** get **created and run** (you'll need to add the given .env file) by the docker files (no need to change them, they are ready) => Change the SQL scripts
1. Make the Siba **backend run** (needs that same .env file)
1. Install and make the **REST Client VS Code extension** work and **test the backend** with it (you'll need to add the given settings.json file)
1. When all ready-made seems to work, add the instructed **database table** with **scripts also** for the **test data** etc.
1. Add first **new route** to the backend routing and implement the code behind it. Basically easiest is always "GET all", e.g. GET /product/    = **L**  = List
1. Add **first API test case** for that route and test it
1. Add **more test cases**, failing ones and successful ones, still for that one new route.
1. Add **second route**, e.g. GET one by id,  or:   GET /product/:id     = **R**   = Read
1. Add **input data validators** and test them with your previous and now added new REST client test cases (ok and fail cases again!)

## Follow given models

You are given a **ready** full-stack architecture, with **Node.js & Express** backend written with **TypeScript** using MariaDB **RDBMS** with help of the **knex library**. After setting all up you try to follow the model and implement few backend features, finally having e.g. the **following benefits**:

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
- Locally for development and running local version of Node most likely: **Nodejs**, TypeScript, Nodemon, ...
- Possibly MariaDB RDBMS installed locally but **only IF**:
    - Dockerized version will not work
    - Teacher has not given a remote database to be used with SSH tunnel
- DBeaver Community edition. Zip downloaded and extracted to e.g. c:\users\joe\dbeaver folder. This to see whether the tables and data created.

### Fork, install and test the environment according to the earlier Node.js installation task (task 1)

# Real task starts here (task 3)

**Note2:** Running docker for database creation might ask for "File sharing permission". That is for the docker to access the 000_createAllDb.sql that is needed for creating the database container.

**Note3:** For someone running WSL the name property needed to be removed from the docker-compose file. It's the name for the project and not 100% necessary. Docker will use some other name for it then. Name cannot hava more than small letters and - and _

---

## NOTE THESE!

* Do NOT return anything straight from the routes. But use the ```successHandler```, ```dbErrorHandler```, ```requestErrorHandler``` etc.

* Do NOT write validations manually, look at the model and use the same model that was used before, e.g. ```validateNameObl,```
and ```[roleChecker, validate]```

* Also define what roles are able to run that feature so you can test role-based-authorization you define

* The possibly needed new TypeScript types should go to the ```types\custom.ts```

* And most IMPORTANTLY use the ```logs\app.log``` from the beginning. **Take screenshots of app.log** and the result window when you will get interesting errors and fixed operation success messages there!

---

# The additions to write and test in the backend code = real task

You will be adding a new table Sauna (id INTEGER, name VARCHAR(200), opened DATE, temperature DECIMAL(3,1), isPublic BOOLEAN). For simplicity add it to the existing database. So it will be an unrelated/unlinked table, no prob there. 

Add the table and its fake test data rows (10 rows or more) to the existing SQL script files. Take model from existing SQL script lines. **Notice** that the files 000__CreateALLdb.sql and 06__drop_tables_create_tables_insert_test_data.sql are generated by running ```sh a_concatenate_needed_db_scripts.sh``` console command in that folder. 

**Note:** Like mentioned above, just docker-compose down and up again will not work with SQL scripts that are source code in our original folder (not in the docker container!). Thus need to also delete the volume, possibly also the image while creating needed table and its test data.

Hint: You can always start with minimal version, e.g start with just few properties. Start with just one route. Only one view, and so on. Makes sense to minimize the re-work you might need to do.

### Features to implement (first feature is simple so that there your learn the end-point basics. Then features themselves get more non-trivial from validation and DB operation point of view)

* What are the Saunas there all in all? Easy feature as will later maybe need the login, but no input in the request for the query. Database: casedb, Table: Sauna

* What saunas have letter 's' in their name? (hard-code this in the end point) 

* What rows there are that have something you give in the request in their name. = request should include, in body JSON data **or** URL :name parameter. If the ```LIKE %``` matches, those rows are returned. Thus the complete name doesn't have to be given, partial is enough

* Which saunas are more recent than a date you give in the request? (Date given in POST JSON data or URL parameter)?

* How to add a new Sauna to the system (to DB via Backend REST end point)

* Extra: How to edit a Sauna (sauna that exists in DB already)

**See the given PDF example about analyzing one Program route in Teams**

See the Files tabs.

That should give an idea how much code is needed per one new route.

1. add a new file ```src/routes/sauna.ts```
1. add routing ```'/sauna'``` to that file, in file ```src/routes/index.ts```
1. following the models in e.g. in Program related route and validation code...
1. add the suggested/required new routes from above ONE by ONE.
    1. add the endpoint and routing to it
        1. the database operation development should be always started by doing something easy that works, and then making it more specific. E.g. first list everything, and only after that tested and works put there the WHERE conditions.
    1. add the REST client test(s) for it
        * Look at the ```request\GlobalSettings.rest``` or ```request\Program.rest``` as some kind of model how to implement your own test cases in the future. 
        * The 'nextId' local variable could be changed to the autogenerated id you get by running the POST. = what was the next auto-generated id going to be
    1. add validation components to validationHandler folder, new file ```sauna.ts``` IF needed by that endpoint (e.g. mere 'GET all' does not need any input, just URL = no input validation)
    1. if added validation, test it again. Try to make it fail and show the logs!


#### ---- EXPRESS-VALIDATOR validators for input data ----
Express-validator is a library that can be used to validate the data coming from the frontend or other client (like that REST Client extension):
https://express-validator.github.io/docs/

New express-validator validation ideas could contain e.g.: 
 - ```.isEmail()```   (currently the email allows test values: admin etc. But just for making dev testing faster)
 - ```.contains("-")```
 - ```.isDate()```
 - ```.isISO8601```


# --------------------END------------------------
# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------

### EXTRA: (Totally extra, just if feel like finding out what the Frontend does currently) 

## Install the frontend  (Possible but not really needed for the task) Skip if no extra time!  )))

### a) Docker option

Do pretty much same as with the dockerized backend
1. Go to the workspace folder 'Siba'
1. Fork there the frontend project repo: https://github.com/haagahelia/siba-fe
1. The .env file is not in repo, so create/copy that given file to frontend repo root
1. and with logout/login you can use e.g. email: "admin", password: "admin" to log in.
1. Run the correct docker-compose up with the correct docker-compose script file 

### b) Manual option
1. Go to the workspace folder 'Siba'
1. Fork there the frontend project repo: https://github.com/haagahelia/siba-fe
1. You will not get the node_modules, so you will need to move to that folder and: ```npm install```
1. Also the .env file is not in repo, so create/copy that given file to frontend repo root
1. You can also run the: ```npm audit fix```   , if there would be any recent vulnerabilities.
1. ```npm start``` would start the application 
1. and with logout/login you can use e.g. email: "admin", password: "admin" to log in.


(using the running frontend, again check the correct ports etc. from .env files and so on)
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