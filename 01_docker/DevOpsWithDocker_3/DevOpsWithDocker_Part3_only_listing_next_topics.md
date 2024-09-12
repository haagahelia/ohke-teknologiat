# DevOps with Docker - Summary of Part 3, only listing next topics

**NOTE:** These topics still contain useful steps that you will most likely need in your first software projects. We most likely let you study them later on your own pace.

=============================================


## "Official Images and trust"

https://devopswithdocker.com/part-3/section-1


- official docker images
- how to study could there be security risks in images?
 

## "Deployment pipelines"

https://devopswithdocker.com/part-3/section-2 

- CI/CD pipeline (sometimes called deployment pipeline)
- GitHub Actions
- Builder container building an image, ...
- Publisher/Server container publishing/serving that image


## "Using a non-root user"

https://devopswithdocker.com/part-3/section-3

- Docker itself needs sudo rights ...
- ... but all operations do not need to **run** with sudo rights
- RUN useradd juhani   # to add normal user
- RUN chown .....      # to change that normal user to own files or folders
- USER juhani          # changing to act as that normal user


## "Optimizing the image size"

https://devopswithdocker.com/part-3/section-4

- many means for making images smaller
- multi-stage build Docker-files


## "Multi-host environments"

https://devopswithdocker.com/part-3/section-5

- Docker swarm mode
- Kubernetes (orchestrating your containers in large multi-host environments)
   * In school we have used e.g. Rahti2 of CSC (RedHat OKD), which is based on Kubernetes
