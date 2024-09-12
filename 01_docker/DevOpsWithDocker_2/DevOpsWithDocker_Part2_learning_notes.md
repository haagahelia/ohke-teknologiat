# DevOps with Docker - Summary of Part 2, sections 1-4

**NOTE:** Especially in these sections the material contains a lot of local installation commands,
but those are just for reading. No need to install any of the tools locally, finally all leads 
to dockerized version of the installation = docker should be only thing you install.


## "Migrating to Docker Compose"

https://devopswithdocker.com/part-2/section-1

- Docker Compose to orchestrate multi-container system:
  * services ~ running named containers
  * service startup order and other restart etc. policies
  * image build instructions as Dockerfiles
  * environment variables and/or .env files
  * port publications
  * volumes
  * networks

https://docs.docker.com/reference/compose-file/

---

## "Docker networking"

https://devopswithdocker.com/part-2/section-2

There are about 7 different Network types or "Drivers" in Docker:
1. **Bridge**: Normal idea of a network, like one 'bus' where you can connect those containers you want
1. **Host**: Joining the containers seemingly directly to host computer's network stack. Containers appear kind of an app running in host os without docker would.
1. **None**: Isolating the container from any networks
1. -7. (other types = drivers left for advanced studies)

https://docs.docker.com/reference/cli/docker/network/

https://docs.docker.com/reference/cli/docker/network/create/

https://docs.docker.com/reference/compose-file/networks/ 

Default network

- "By default Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by the service's name".

((
- "Docker Engine defines one default network with name:bridge and driver:bridge"    (Some sources say name:'docker0')
)) 

- BUT it's **better idea** to explicitly create your **own named network** with driver: **bridge**  
and also join the wanted containers to it by defining each of them the network
   * Then again, you could use the name of the service like name of the server computer, e.g. DB_HOST=my_mariadb_service

---

## "Volumes in action" (No tasks beyond this point)

https://devopswithdocker.com/part-2/section-3

- Multi-container example showing e.g. how database needs to persist its datafiles (contains metadata and data) using volumes
- Two containers could be given access to the volume/mount. E.g. one write-permissions and the other just ro (read-only)

https://docs.docker.com/reference/compose-file/volumes/

---

## "Containers in development"

https://devopswithdocker.com/part-2/section-4

- not much new, running docker compose to set up identical development environment for all developers
- CMD => command:    ENTRYPOINT => entrypoint: 
- using host volume allows container to modify defined host computer files/folders

---