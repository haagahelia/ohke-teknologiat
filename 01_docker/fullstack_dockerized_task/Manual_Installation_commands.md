
# Commands and settings used in manual installation of a Full-stack system

* While dockerization / containerization of the system there are of course changes.

* Not all steps or users or installations are needed. 

* On the other hand, e.g. separation of backend and DB to different containers instead of same 
server machine means the backend container must somehow connected
with the DB container! Either inside docker engine, or outside, via the host computer.

* In the case of frontend browser connecting to the backend we have to even connect via internet.

* But certainly looking at the manual installation steps, commands and parameters help 

* The commands listed were run inside Ubuntu Linux and thus most likely run in your docker containers. Of course some commands might not be installed in certain docker image.

## Architecture picture

[New with local DB](https://github.com/valju/docs_backend_design/blob/master/BackendArchitecturePic_with_DrawIo_LocalDB_WithMoreDetails.drawio.png)

[Older with SSH tunnel](https://github.com/valju/docs_backend_design/blob/master/BackendArchitecturePic_with_DrawIo_WithMoreDetails.png)

## Concept picture of the dockerized architecture - Don't take this literally

[dockerize architecture ideas](https://github.com/valju/docs_backend_design/blob/master/BackendArchitecturePic_with_DrawIo_LocalDB_WithMoreDetails.drawio.png)

But no need to e.g. make this automatically build. Just by running your docker/docker-compose files

# Files and repositories needed

[Backend repository, with e.g. DB SQL scripts, run by normal DB user](https://github.com/haagahelia/Siba_be)

[Frontend repository](https://github.com/haagahelia/siba-fe)

[createSchemaAndUsers.sql, run by DB root](createSchemaAndUsers.sql)   Note: You'll need to change things, at least password

[.env (Backend) and .env.local (Frontend) templates](dot_env_files.zip)  Note: You'll need to change some things, possibly usernames, ports, passwords.

[default, an nginx conf file example](default)   Note: Not sure if this is needed at all. Possibly just copy html etc. to the default publication folder.

---

### 1. Initially e.g. firewall was set up, e.g. so that these ports are

* 22 - SSH    = if need to go ther to copy files, git pull, start services etc.

* 80 - http   = published version of frontend served from here

* 8888 - Backend REST API, frontend app from browser must be able access it, = via real Internet

* (3306 - MariaDB not outside of this computer. Unless you want. Backend needs to see this though)

* (8686 - Or so for frontend dev-time node server, not available outside this computer)

### 2. Then the Ubuntu was installed and updated to the latest

Extra: CSC cloud VM installation  (https://github.com/haagahelia/linux-servers-etc/blob/main/CSC_virtual_machine_and_user_creation.md)

```
sudo apt update
sudo apt upgrade
```

### 3. Then two users created one with sudo rights, one without.

* jyser1 sudo
* jyser2

### 4. This was how the MariaDB server was installed (when no docker used)

Write down the possible/probably root username and password

While using docker image find out the default password etc. from documentation

```
sudo apt update
sudo apt install mariadb-server
sudo systemctl start mariadb.service
sudo mysql_secure_installation
```

Extra: [MariaDB Ubuntu installation to cloud VM](https://github.com/haagahelia/linux-servers-etc/blob/main/mariadb_installation.md)

[MariaDB local installation (Windows)](https://github.com/haagahelia/linux-servers-etc/blob/main/mariadb_installation_local_pc.md)

### 5. This was apparently done to hide the sudo user's home directory from others

Probably not needed in docker version.

```
cd ~
pwd
chmod 700 .
ls -Falls
pwd
```

### 6. How to create the schema="database" in MariaDB, the backend user for DB, and give all rights to that user to that schema:

Here the root password was needed (-p means wait for password on next line)

```
nano ~/createSchemaAndUsers.sql
mysql -h localhost -u root -p < ~/createSchemaAndUsers.sql
```

### 7. How the root root folder Siba was created to home directory. Deleted if existed before

```
cd ~
ls -Falls
rm -rf Siba
mkdir Siba
cd Siba/
```

### 8. How the two repos were cloned

```
cd ~/Siba
git clone https://github.com/haagahelia/Siba_be.git
git clone https://github.com/haagahelia/siba-fe.git
```

### 9. How the case database tables, stored procedures and test data rows were created

```
mysql -h localhost -u jyser3 -p < ~/Siba/Siba_be/Database/SQL_Scripts/000__CreateALLdb.sql
```

### 10. How the backend .env file was written if pasted from copy paste text (not in repository)

```
nano ~/Siba/Siba_be/.env   
```

### 11. How the backend .env file was copied, if existed in home directory (not in repository)

```
cp ~/.env ~/Siba/Siba_be/
```

### 12. How the frontend .env.local file was written if pasted from copy paste text (not in repository)

```
nano ~/Siba/siba-fe/.env.local
```

### 13. How the backend .env file was copied, if existed in home directory (not in repository)

```
cp ~/.env.local ~/Siba/siba-fe/.env.local
```

### 14. How to find out what processes running, and how to kill with PID, process id, e.g. 4066

```
ps -a
ps -aux
ps -aux | grep 'node'
ps -aux | grep 'npm'
ps -aux | grep 'vite'
ps -aux | grep 'tsc'
sudo kill -9 4066
```

### 15. How is listening to port 8888?

```
lsof -i :8888 
```

### 16. Finding out what commands work in that Virtual machine

Equal to you finding docker images that support the needed Things. Though something you can also run in host machine, outside the container. E.g. you could git clone/pull in host machine and then copy files to container. OR git clone/pull from the container.

The selected docker image of course might have e.g. the support for Node already.

```
git --version           # often found in Linux distributions
node --version
docker --version        # Probably not needed inside container :D
tsc --version
python --version        # Python probably not needed in normal use of the app
python3 --version		# Python probably not needed in normal use of the app
py --version			# Python probably not needed in normal use of the app
```

This is most likely needed somewhere:

```
npm i -g typescript
```

### 17. How Node.js was installed manually. 

Not sure if this is still the correct way for installin Node.js . Sometimes direct ```sudo apt install node``` or so gives very old version and we need to add some other apt/Debian repository link to our computer to get the newer one, latest sub version of major version 20. World is not perfect.

```
cd ~
sudo apt-get update && sudo apt-get install -y ca-certificates curl gnupg
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=20
echo $NODE_MAJOR
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt-get update && sudo apt-get install nodejs -y
```

### 18. Checking which version of node in use now

```
node -v
npm -v
npx -v
```

### 19. Pulling/refreshing latest version of backend and starting it

```
cd ~/Siba/Siba_be/
git pull
npm install
less .env
npm start
```

```
sudo npm i -g pm2
nano package.json
```

### 20. Possibly add this line in the middle of package.json scripts, if missing. Remember JSON does not allow trailing commas!

```
"production2": "pm2 start dist/index.js",
```

```
nano .env         
npm run production2
### which means now same as:
pm2 start dist/index.js
```


### 21. Pulling/refreshing latest version of frontend and starting it. Note: Frontend app will be run in your Browser. Thus NOT on server. Not on the same computer as backend.

```
cd ~/Siba/siba-fe
git pull
npm install
less ~/Siba23/siba-fe/.env.local
nano ~/Siba23/siba-fe/.env.local
npm install
```

### 22. This would be how to start the development-time server, BUT...

```
nano .env.local
nano package.json 
npm install
npm start
npm start --host
npm host
npm run host
npm run host &
ps -a | grep node
ps -a | grep npm
```

```
git pull
npm run build
ls -Falls
cd dist/
ls
```

###  23. Installing the nginx web server / web proxy server

```
nginx -v
sudo apt install nginx-core
nginx -v
sudo systemctl status nginx
```

### 24. Just testing the web server from console, with console browser lynx

```
sudo apt install lynx
lynx http://localhost:80
```

### 25. Publishing the content of the dist folder to the nginx web server's default public folder

```
sudo cp -r ~/Siba23/siba-fe/dist/* /var/www/html/
lynx http://localhost:80
```

[What the deployed React app files might include (picture)](deployed_files_from_vite_react_app_after_npm_build.png)

### 26. POSSIBLY NEEDED: If the access rights for the public / www / others are not enough then possible to adjust them:

```
cd /var/www/html/
ls -Falls
sudo chmod 756 .
ls -Falls
```


### ----------------------------------------------------------------------

### 27. EXTRA: This would be the way to publish in certain user's home folder's public_html folder

That is not by default offered out from the computer by nginx

```
cp -r ~/Siba23/siba-fe/dist/*  ~/public_html/
```

EXTRA: But with this nginx configuration both the common folder and the user public_html folders would be offered (if public_html folder exists, and has correct access rights). This was defined in was it /etc/nginx/site_available or somewhere. Read the manuals

```
    # This is there usually without any config changes
	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	# Home directories - This you'd need to add if want public_html folders
	location ~ ^/~(.+?)(/.*)?$ {
  		alias /home/$1/public_html$2;
	}
```