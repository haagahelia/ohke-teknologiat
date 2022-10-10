# Installing Kafka and making producer and consumer clients

## First install Docker to your computer

For Windows, install the Docker Desktop 

For Linux the installation is even less painful.

* While installing I selected the recommended "WSL2" instead of "Hyper-V something". Do that if it is offered to you.

* One had to log out from Windows and log back in to have the Docker installation finished

* **docker-compose** tool is part of the Docker installation.

## Then create your project (e.g. 'kafka-app-lastname') repo in GitHub, use Node as .gitignore template

Then clone it to local folder.

**Note:** git use is not instructed here. So feel free to select when make new commits and push own backups to remote.
```
git add -A
git commit -m "Xxxx xxxx xxxxxx"
git push
```

# Then add the docker-compose.yml file to the project root

[01 docker-compose.yml file](.\screenshots\01_docker-compose-yml.png)

You can use e.g. VS Code editor. After the file is ready, run this command e.g. in the VS code Terminal window

```
docker-compose up
```

It will download the defined two docker images 'zookeeper' and 'kafka' and configure and start a virtual machine out of each of those.

The terminal window will keep on showing messages from the (zookeeper service, and more importantly the) Kafka server. But you can split and narrow the Terminal window to the left of the bottom. 

Thus you get more Terminal windows to the right. In a new one run the following topic creation command script with its options.
[02 kafka_topic_creation_command file](.\screenshots\02_kafka_topic_creation_command.png)

## Create a Node project for both producer and client processes

# Do you want to install Node 18.x.x. even if it is latest and not LTS?
To use import/export without babel hazzle, you could install Node 18.x.x or newer from https://nodejs.org/en/ 
(Select: Automatically setup/install all tools)  

Then in any case in project root folder.
```
npm init
```

Now this folder becomes a node project. Administratively it's one node project with one package.json file and on node_modules folder. 

Run thes two, at least the first one is used in our project. It's library for registering as Node.js Kafka client. Second one is for de/seriliazation of objects for sending them over Kafka broker to another client.
```
npm i node-rdkafka --save
npm i avsc --save
```
Next we define two runnable index.js files. So two separate processes are born from this administratively single Node project.
[03 package.json file](.\screenshots\03_package_json_scripts_added.png)

### Time to write the Kafka producer client and then test it
[04 producer code file](.\screenshots\04_producer_code.png)

```
npm run start:producer
```
Later you can use Ctrl+C to stop it for editing and restart.

### Time to write the Kafka consumer client and then test it
[05 consumer code file](.\screenshots\05_consumer_code.png)

```
npm run start:consumer
```
Later you can use Ctrl+C to stop it for editing and restart.

**Does everything work? So far you have just read and rewritten same. But even there you learn to see structures etc.**

# Now would start your changes

You need to decide what will be your business case for your further Kafka app unless you want to use just mine which follows below:

## Proposed case if no own Business case in mind - Merely technical proof of concept
Make producer to be producer-consumer and consumer to be consumer-producer.

E.g. make the "producer" submit JSON formatted randomized addition calculations to "consumer" on topic/channel 'task'.

But then you could have another topic 'answer' (just a text like "1+2=2 is false", "1+1=2 is true"). So you would make the 'consumer' to be also producer but on topic 'answer' and the 'producer' to be also consumer but on same topic 'answer'. Thus they communicate one way with 'task' and 'answer' is used to give answer.

Setup the answer channel, and when you get one task to handle, make that code to initiate the response.

Might sound complicated, just read the instructions few times.

## What to submit?

Submit screenshots of working system's console, where messages are sent and received.

Then when you create your own code, or make any other changes, copy that code to Word doc and submit as PDF. If you copy-paste from VS code you get the colors and all, when select such paste option.

## Full points or extra points?

Find out how to secure the system with key files or such. Now there is nothing stopping anybody from posting the messages as long as they know IP address and correct port.

