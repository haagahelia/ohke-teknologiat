# DOCKER PORT SUMMARY

* "Exposing a container port" means telling Docker that the container listens to a certain port. This doesn't do much, except it helps humans with the configuration.

* "**Publishing a port**" means that Docker will map host ports to the container ports.
  -   -p 8080:80              &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; in docker run
  -   ports:  - '8080:80'         &nbsp; &nbsp; &nbsp; in docker-compose file

### More from Docker documentation:

https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/

https://docs.docker.com/reference/cli/docker/container/port/

https://docs.docker.com/reference/dockerfile/#expose    
(Dockerfile can only EXPOSE, not publish/map ports, as it's about building one image, not orchestration of many containers)

https://docs.docker.com/reference/compose-file/services/

https://docs.docker.com/reference/compose-file/services/#ports
(Docker Compose then is about inter-container orchestration, here publishing ports possible)



