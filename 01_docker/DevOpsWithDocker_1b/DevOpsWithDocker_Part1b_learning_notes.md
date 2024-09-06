# DevOps with Docker - Summary of Part 1b, sections 4-6

**NOTE:** Especially in these sections the material contains a lot of local installation commands,
but those are just for reading. No need to install any of the tools locally, finally all leads 
to dockerized version of the installation = docker should be only thing you install.

https://devopswithdocker.com/part-1/section-4/
==============================================
 
- manual commands for testing first => **No need to run**, just read them!
- Dockerfile  (FROM, WORKDIR, COPY, RUN, RUN, RUN, EXPOSE, CMD/ENTRYPOINT)
- ENTRYPOINT + CMD
 
https://devopswithdocker.com/part-1/section-5
=============================================
 
- mounting volumes for persistence and sharing
- publishing ports to make container services available to others and/or host
 
 
https://devopswithdocker.com/part-1/section-6
=============================================
 
- dockerizing existing projects from e.g. github repos (hopefully with informative and up-to-date README files)
- publishing own images to Docker Hub.   Consisting of: 

   1. some other ready-made docker image as the first layer, like node:latest  or nginx 
   2. own source code + compilation 
   3. other assets
   4. Dockerfiles and other scripts
   5. e.g npm library installation "instructions" (npm i  + package.json)

### Remember e.g. these information sources:
https://docs.docker.com/reference/cli/docker/container/run/  Docker CLI reference, e.g.  docker container run
https://docs.docker.com/reference/dockerfile/     Dockerfile reference


### Random notes from the pages listed above: (in order of appearance)

- We go a bit 'backwards' to run manual commands first, then see how to do them in Dockerfile

- ... At some point, you may have noticed that sudo is not installed either, but since we are root (inside docker containers) we don't need it ...

- Most changing content later in Dockerfile to have more permanent layers to the top for faster caching.

- Remember RUN means RUNNING commands to build / while building the **image** i.e. 'docker build- ...

   - ... whereas CMD / ENTRYPOINT is the definition of the command(s) that WOULD BE run at 'docker run', later, while starting the **container**

- ENTRYPOINT vs CMD can be confusing:

   CMD represents an argument list for the ENTRYPOINT. By default, the entrypoint in Docker is set as /bin/sh -c and this is passed if no entrypoint is set. This is why giving the path to a script file as CMD works: you're giving the file as a parameter to /bin/sh -c.

   ```
   FROM python:3.11
   ENTRYPOINT ["python3"]
   CMD ["--help"]
   ```

   OR

   ```
   FROM python:3.11
   CMD ["python3","--help"]                 => "/bin/sh -c python3 --help"
   ```