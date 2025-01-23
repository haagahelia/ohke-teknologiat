# DevOps with Docker - Learning notes of Part 1a, sections 1-3

Example for learning notes that you could do to: 
1. stay awake/focus 
2. process the issues
3. organize your thoughts in manner meaningful to you 
3. possibly have something to go back to to recap the issues (but not necessarily)

Docker documentation! https://docs.docker.com/
Docker Desktop > Learning Center   
     - look at e.g. containers and then lower part of view
(https://www.docker.com/101-tutorial/)
https://docs.docker.com/guides/resources/
https://docs.docker.com/get-started/docker_cheatsheet.pdf
Course forums! (HYY)

Multiple Steps! Start early and reserve at least three sessions! 
================================================================
- Installation and troubleshooting takes time,
- Learning takes time and maybe you need to ask for help,
- Then doing task and related troubleshooting and asking help takes time!

* => Don't rush
* => Don't panic either. 
* => Understandable, but complicated new concepts and terms! 
* => Trust your slow and steady research work!

Write your own notes at all times. In docker usage you do only very
few new lines of scripts, but the key is to know and to understand the concepts
and meanings!

Part 1a
=======

- Create images (```docker build ... ```, Dockerfile)
- Run containerized applications (```docker run ... ```)
- Containerize applications 

## https://devopswithdocker.com/part-1/section-1


DevOps: release, configuring, and monitoring done by developers
(+testing, +deployment)

Container
=========

"Package of software" 

[often: Running Linux os + the libs/bin app needs (often parts of that Linux release) + the needed application starting in a way someone defined it, with your possible changes or configurations ]

"App and all its dependencies packed together"

Containerization benefits
=========================
1. Dependencies move together with the app, as container
2. Isolated environment, not mixing e.g. with lib versions or env variables
3. One developer develops the dev env and others just take into use from an image!
4. Scaling by running more and more containers (load balancing traffic)

Juhani thought these could be listed as benefits too, agree?

5. Scripts can be maintained and taken to next project, updated, improved, dev automated/integrated even more!
6. Version controlled Docker scripts that are easy to edit with editor
7. Size of storage, as all is in scripts, software binary images downloaded from docker hub, (or compiled from your source code) and only your scripts, sources and other assets need to be stored.
8. Latest version of someone else's work (e.g. MariaDB) pulled always if you so wish
9. Put more learning on generic DevOps skills instead of (possibly changing) installation and configuration procedures of (possibly changing) tools.


Virtual Machines vs Containers
==============================
- containers run almost as efficient as native apps
- containers/images are transferrable between environments 
(as long as 1. a docker version for that env exists 2. based on multi-images)
- virtual machines often use more RAM resources, as part of RAM dedicated for the VM
- containers run MANAGED/ISOLATED/CONNECTED by Docker Engine (docker daemon), but using normal resources of the OS 


Your files(src, env, assets...) + your Dockerfile   =build=>   Image

Image built by your, or Image pulled from Docker Hub    =run=>   Container

("Image recipe for food, Container one prepared meal (can be already spoiled, but recipe is a way to produce a new fresh one").

----

FROM <image>:<tag>
RUN <install dependencies>                    # here we build the image step by step
CMD <command executed on `docker container run`>   # setting the start procedure

docker container run => docker run
docker container ls => docker ls ?

docker system prune     => does it remove volumes?

50 commands
- only few needed by you
- those teach you more and more about docker
   => so try to enjoy learning each new needed command

### Ex 1.1

- How to find out how to "start 3 containers in detached mode"? Find out now?

### Ex 1.2

- no probs


## https://devopswithdocker.com/part-1/section-2

$ docker run ubuntu
  Unable to find image 'ubuntu:latest' locally
  latest: Pulling from library/ubuntu

 -t will create a tty.
 -i flag will instruct to pass the STDIN to the container
 => -it 

docker run -d -it =>  why not   docker run -dit  ?

docker run --rm -it     what's difference between -- and - ?

docker logs
https://docs.docker.com/engine/logging/

docker pause
https://docs.docker.com/reference/cli/docker/container/pause/

"looper"   Notice that you can name many things in docker, including images! Looper is just a name for a container that the course materials create based on Ubuntu.

### Ex 1.3

devopsdockeruh/simple-web-service:ubuntu   What is devopsdockeruh ?

                                    (Docker Hub user/organization =publisher)                                

Nonmatching host platform: M1/M2 Mac. "WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested" Docker Desktop for Mac employs a possibly slower emulator

### Ex 1.4

What is sh?       (The command interpreter in that Ubuntu image/container. For executing shell scripts. Similar to e.g. bash command. Can be either 1. called 
from another process or 2. is used to interprete your console commands)  

man sh   (in Linux/Unix console)
https://linux.die.net/man/1/sh
https://man7.org/linux/man-pages/man1/sh.1p.html
https://www.commandlinux.com/man-page/man1/sh.1.html
https://www.unix.com/man-page/linux/1/sh/

"If you're on Windows, you'll want to switch the ' and " around"

docker exec

## https://devopswithdocker.com/part-1/section-3

docker search hello-world
"Official images are curated and reviewed by Docker, Inc. and are usually actively maintained by the authors. "

"Auto image is automatically built from the source repository each time new sources pushed to your source provider"

https://hub.docker.com/_/mariadb
click on the version of the image to see the: Dockerfile,  where       FROM ubuntu:jammy

"other Docker registries competing with Docker Hub, such as Quay". By default, docker search will only search from Docker Hub, but to search a different registry, you can add the registry address before the search term, for example, docker search quay.io/hello. 

registry/organisation/image:tag
image   => registry will default to 'Docker hub', organisation to 'library' and tag to 'latest'

### Ex 1.5 - 1.6

- No probs, just need to remember or recap also previous part commands to get these done

"Dockerfile is simply a file that contains the build instructions for an image"

https://linux.die.net/man/1/chmod   for chmod +x filename

https://hub.docker.com/_/alpine

```
FROM scratch
ADD alpine-minirootfs-20240807-x86_64.tar.gz /
CMD ["/bin/sh"]
```

# Copy the hello.sh file from this directory (Means where Dockerfile, and where "docker build" run)
 to /usr/src/app/ creating /usr/src/app/hello.sh
```
COPY hello.sh .
```

```
docker diff container_a
docker logs container_a
docker image ls
docker container ls          -a
```

https://linux.die.net/man/1/touch

We will not use docker commit (we do not play directly with the image binaries, but want to keep our work always in scripts, Dockerfile for instance)

### Ex 1.7-1.8

- Entrypoint as a new issue
https://docs.docker.com/reference/dockerfile/#entrypoint

- You kind of need to know e.g. that:
  - ENTRYPOINT is "executed" first, then CMD
  - if no ENTRYPOINT given, default ENTRYPOINT runs the shell interpreter "/bin/sh -c"
  - docker run command later would have as last part, the command, or CMD

  ``` docker run hello-world pwd ```       =>   CMD ["pwd"]  => "bin/sh -c pwd"

Hint: Use the docs.docker.com references, e.g. CLI reference, docker container run, study the
command options parameters etc.  

===================== Linux command parameter flags =============

Teemu's example from the board, these are all the same:

```
docker run -i -t
docker run -it
docker run --interactive --tty
```

But this would be misinterpreted:    = WRONG
```
docker run --it             (as after -- the letters are interpreted as one word)
```

```
docker run --rm    (Checking learning: Is this now r and m, or one "word" rm?)
```
