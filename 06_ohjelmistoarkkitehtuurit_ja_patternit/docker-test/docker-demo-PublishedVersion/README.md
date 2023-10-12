# Kafka server & producer and consumer clients

## First install Docker Engine and Docker Compose to your computer

Some of the needed [Docker links and info](../Docker.pdf). 

1. For **Linux** or **Linux VM** in Windows install 1. Docker Engine and 2. Docker Compose (But NOT the Docker Desktop).

1. For **Windows** install the Docker Desktop (Installs also the Docker Engine and Docker Compose) 

1. For **Mac** install the Docker Desktop (Installs also the Docker Engine and Docker Compose) 

* Windows: While installing I selected the recommended "WSL 2" instead of "Hyper-V something". (Might spoil your other VMs though!).

* One had to log out from Windows and log back in to have the Docker installation finished. Also settings changes were required.

* **docker-compose / docker compose** tool is part of the needed installation.

## Then create your Node project repo in GitHub 

Private repo, name it e.g. 'kafka-app-lastname'. Use Node as .gitignore template. Then clone it to local folder.

**Note:** git use is not instructed here. So feel free to select when you make new commits and push own backups to the remote.
```
git add -A
git commit -m "Xxxx xxxx xxxxxx"
git push
```

# Then add the docker-compose.yml file to the project root

[01 docker-compose.yml file](./screenshots/). Read and type this to learn the YAML structure and docker compose files a bit.

You can use e.g. VS Code editor. After the file is ready, run this command e.g. in the VS code Terminal window

```
docker compose up
```

It will download the yaml-defined **docker images** 'zookeeper' and 'kafka' and configure and start **two running containers** out of each of those. Plus a network between them.

The terminal window will keep on showing messages from the (zookeeper service, and more importantly the) Kafka server. But you can split and narrow the Terminal window to the left of the bottom. 

## Create a Node 'project' folders for both producer and client processes
According to shared screenshots of the project. It's a bit confusing, but now the repo will have two Node projects or starting points, even if they share the package.json file and node_modules folder.

# Install the latest Node if you haven't for some months
(from https://nodejs.org/en/). The package.json now has the "type":"module" so we can use import/export without babel hazzle,  
(Selects while installing: Automatically setup/install all tools)  

Then in any case, in project root folder.

```
npm init
```

Now this folder becomes a node / npm module project. Administratively it's one node project with one package.json file and on node_modules folder. But will have two 'apps', producer and consumer

Run these two, at least the first one is used in our project. It's library for registering as Node.js Kafka client and communicationg with the Kafka server. Second one is for the UUID creation.
```
npm i kafkajs --save
npm i uuid --save
```

Next we define two runnable index.js files. So two separate processes are born from this administratively single Node project.
[03 package.json file](./screenshots/). Given also in the [.zip file](../docker-demo-PublishedVersion.zip).



###Creating the Kafka topic(s) = message channels = event 'queues' ###

In Powershell or similar powerful console run the following topic creation command script.
[topic_creation_command.sh file](./topic_creation_command.sh). Given also in the same [.zip file](../docker-demo-PublishedVersion.zip). For some reason the command did not work for 
me in GitBash console but worked from Powershell. 

**OR**: run the following commands (yes, twice! To see that they work). Given in the same [.zip file](../docker-demo-PublishedVersion.zip).

```
node ./admin/deleteTopics.js
node ./admin/deleteTopics.js
node ./admin/createTopics.js
node ./admin/createTopics.js
```

## The used Kafka client library: 
We are using the [kafkajs library](https://www.npmjs.com/package/kafkajs) to [write code](https://kafka.js.org/docs/getting-started) for the Kafka producer and Kafka consumer. And the admin as you already saw. 

### Time to write the Kafka producer client and then test it
[04 producer code file](./screenshots/). Read this carefully, try to understand as much as possible. Write it to learn the basics of the kafkajs Kafka producer client code.

```
npm run start:producer
```
Later you can use Ctrl+C to stop it for editing and restart. But for now leave it running on its own terminal window.

### Time to write the Kafka consumer client and then test it
[05 consumer code file](./screenshots/).  Read this carefully, try to understand as much as possible. Write it to learn the basics of the kafkajs Kafka consumer client code.

```
npm run start:consumer
```
Later you can use Ctrl+C to stop it for editing and restart. 

**Does everything work? So far you have just read and rewritten same code as given. But even then you learn to look at the structures etc.**

# Now would start your own changes

The producer/client is currently sending some personal id:s to the consumer/server to be checked, using channel 'tobechecked'.

Change or add code so that producer will randomize and send Fahrenheit degree number to the channel. 

Then create the response channel/topic 'convertedresult', and when you get one temperature to convert, make that code to initiate immediately the response by putting a response to the other channel. Response should have the Celcius degrees and the same UUID at least.

Might sound complicated, but just read the instructions few times. 

**Hint 1:** You'll make consumer to be also producer in the other channel, 'convertedresult'. And producer to be also consumer in that second return channel.
**Hint 2:** Make the consumers and producers exist all the time.
**Hint 3:** But the consumer can behave as producer only in one specific place/time in code, right? Only when it has i) received a new message, and ii) converted it. Not before that, but immediately then and there. Thus you can write this only inside an event-handler function.
**Hint 4:** Write more features incrementally. Test often with console.log. Have both client and server window open while testing. Also look at the docker containers, are they running?

## What to submit?

**One PDF file**. Submit there screenshots of working system's console, where messages are sent and received. Then when you create your own code, or make any other changes, copy that code to Word doc and submit it finally as one PDF. If you copy-paste from VS code you'll get the colors and all, when select such paste option in Word.


<!-- 
## Full points? Make the id checking 'real'. 

First check all the rules and then check against some list (=fake database). More about [how you could validate personal id:s](../MoreAboutCheckingFinnishPersonalIdNumbers.md). Is that in optimal order? Remember checking one number faster than string comparisons, checking without 'database server' a lot faster and optimized when database bothering can be avoided.

## EXTRAS. More challenge? DevOps and beyond. 

Complete the started DevOps scripting if you want. Automate everything that can be automated.

In real life you would also most likely have/create two separate Kafka servers or server instances. But one the way to create them is here already.

## EXTRAS. More challenge? Securing the Kafka server. 

How to make 1) only certain allowed clients able to connect to the Kafka server and topic, and 2) make the connection secured so that messages are encrypted. And 3) firewalls etc. settings. Now Kafka is used in basically 'everything goes' -settings.

-->