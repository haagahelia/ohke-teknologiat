# Installing Kafka and making producer and consumer clients

## First install Docker Engine and Docker Compose to your computer

For Linux or Linux VM in Windows install 1. Docker Engine and 2. Docker Compose (But NOT the Docker Desktop).

For Windows and Mac, install the Docker Desktop (Installs also the Docker Engine and Docker Compose) 

* Windows: While installing I selected the recommended "WSL 2" instead of "Hyper-V something". (Might spoil your other VMs though!).

* One had to log out from Windows and log back in to have the Docker installation finished. Also settings changes were required.

* **docker-compose / docker compose** tool is part of the needed installation.

## Then create your project (e.g. 'kafka-app-lastname') repo in GitHub, use Node as .gitignore template

Then clone it to local folder.

**Note:** git use is not instructed here. So feel free to select when you make new commits and push own backups to the remote.
```
git add -A
git commit -m "Xxxx xxxx xxxxxx"
git push
```

# Then add the docker-compose.yml file to the project root

[01 docker-compose.yml file](.\screenshots\)

You can use e.g. VS Code editor. After the file is ready, run this command e.g. in the VS code Terminal window

```
docker compose up
```

It will download the defined **two docker images** 'zookeeper' and 'kafka' and configure and start **two running containers** out of each of those.

The terminal window will keep on showing messages from the (zookeeper service, and more importantly the) Kafka server. But you can split and narrow the Terminal window to the left of the bottom. 

## Create a Node 'project' folders for both producer and client processes

# Install latest Node if you haven't for some months
(from https://nodejs.org/en/). The package.json now has the "type":"module" so we can use import/export without babel hazzle,  
(Select: Automatically setup/install all tools)  

Then in any case, in project root folder.

```
npm init
```

Now this folder becomes a node project. Administratively it's one node project with one package.json file and on node_modules folder. 

Run these two, at least the first one is used in our project. It's library for registering as Node.js Kafka client. Second one is for UUID creation.
```
npm i kafkajs --save
npm i uuid --save
```

Next we define two runnable index.js files. So two separate processes are born from this administratively single Node project.
[03 package.json file](.\screenshots\)



###Creating the Kafka topic(s) = message channels = event 'queues' ###

In Powershell or similar powerful console run the following topic creation command script.
[topic_creation_command.sh file](.\topic_creation_command.sh). For some reason the command did not work for 
me in GitBash console. 

**OR**: run the following commands (yes, twice! To see that they work)

```
node ./admin/deleteTopics.js
node ./admin/deleteTopics.js
node ./admin/createTopics.js
node ./admin/createTopics.js
```

### Time to write the Kafka producer client and then test it
[04 producer code file](.\screenshots\)

```
npm run start:producer
```
Later you can use Ctrl+C to stop it for editing and restart.

### Time to write the Kafka consumer client and then test it
[05 consumer code file](.\screenshots\)

```
npm run start:consumer
```
Later you can use Ctrl+C to stop it for editing and restart.

**Does everything work? So far you have just read and rewritten same. But even there you learn to see structures etc.**

# Now would start your own changes

The producer/client is currently sending some personal id:s to the consumer/server to be checked, using channel 'tobechecked'.

First make the server to check the personal id (minimum raw version= check that there are 11 characters and first one is a digit)

Then setup the response channel 'checkedresult', and when you get one id to check, make that code to initiate immediately the response by putting the response to the other channel.

Might sound complicated, but just read the instructions few times. 

**Hint 1:** You'll make consumer to be also producer in the other channel, 'checkedresult'. And producer to be also consumer in that second return channel.
**Hint 2:** Make the consumers and producers exist all the time.
**Hint 3:** But the consumer can behave as producer only in one specific place, right? Only when it has i) received a new id, and ii) checked it. Not before that, but immediately there.
**Hint 4:** Write more features incrementally. Test often with console.log. Have both client and server window open while testing. 

## What to submit?

**One PDF file**. Submit there screenshots of working system's console, where messages are sent and received. Then when you create your own code, or make any other changes, copy that code to Word doc and submit it finally as one PDF. If you copy-paste from VS code you'll get the colors and all, when select such paste option in Word.

## EXTRAS. More challenge? Make the id checking 'real'. 

First check all the rules and then check against some list (=fake database).

## EXTRAS. More challenge? Make the id checking 'real'. 

Complete the started DevOps scripting if you want. Automate everything that can be automated.
