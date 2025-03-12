### Fork the backend - option a) Docker - preferred  (Already done in task 1)

1. Go to the workspace folder 'Siba'
1. Fork/Copy there the backend project repo: https://github.com/haagahelia/Siba_be 
1. The .env files are not in repo, so create/copy the given file to backend repo root.
    - Backend needs all other info than the MARIADB_ROOT_PASSWORD but having that does not harm other than security a bit
1. You will not get the node_modules, so you will need to move to that folder and: ```npm install```
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

#### The .env file for the backend (Already done in task 1)

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

## Testing whether the database + backend combo works

There is one data fetching route that does not need login:   something like this, fix the details to match your port etc.  

http://localhost:1111/api/subject               (GET route to list all subjects from DB via backend. Here replace 1111 with your backend port)

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


(((**Note4:** to have data in Allocation related tables you'll need to run startAllocation test case. (Or if frontend web app running) Login as admin admin and "Program results" > "Reset calculation" and "Start calculation")))

(((**Note5:** to have data in the log tables, the logging setting in GlobalSetting table must be 1, and someone must have run the request\Allocation.rest "resetAllocation" and "startAllocation" test cases, after loggin in!. Well once someone has run it for that local database, or for that persisted **docker volume**, and there is data in log_event table, then no need to do again.)))