# DOCKER NETWORKING SUMMARY

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

More e.g. on this [Youtube video "Docker Networking Tutorial"](https://www.youtube.com/watch?app=desktop&v=fBRgw5dyBd4) by Anton Putra




