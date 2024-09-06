# DOCKER VOLUME SUMMARY

https://docs.docker.com/engine/storage/volumes/

## There are three kinds of volumes available

All of them persist the data directory

1. **Host Volume**: host computer directory mapped to container directory

```/my_laptop/some_folder/:/home/node/app```

2. **Anonymous Volume**: only container directory referenced

```/home/node/app```

3. **Named Volume**: like anonymous, but given name allows for sharing the volume between containers. RECOMMENDED WAY

```my_volume:/home/node/app```        

---

(Of course containers could use some cloud service / database too, so 
then local data persistence with volume would not be needed.)





