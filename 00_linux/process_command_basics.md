# Linux process, port/socket and file handle commands
## Typically needed in our projects when multiple developers use the same server

## Examples of needs / use cases
1. Which ports are being listened to by our server?  *)
2. In which port is node running?
3. Which process is running in port :1234?
4. How to kill the running instance of node that someone else has started? (EADDRINUSE or so error)
5. Which files / file handles / resources is a certain process holding?

*) Remeber that e.g. the lsof command that we use is either 1. the original we got from installed Linux distro image, OR 2. an updated one from e.g. dpkg repositories OR 3. in the worst case, if our server hijacked, a fake version of the tool, possibly hiding the backdoor ports. Thus *only uncompromised servers* are to be trusted. After a security breech you cannot really fully trust any tool anymore.


## Some commands for finding out which ports are open in the system and which processes are listening to those. And killing that process

One way to get your own IP address, it's for the WLAN or Ethernet network adapter
```shell
ip addr show      // 1. in managed cloud might not know the correct mapped extrenal IP address 2. old tool: ifconfig
```

## The lsof command
The useful command you should learn is lsof. Name comes from 'list open files'. In Linux everything is modeled as a file. E.g. a printer is a "file", as are the harddrives, or streams/pipes, ports.
The **lsof** command can do a lot of things: [https://www.tecmint.com/10-lsof-command-examples-in-linux/](https://www.tecmint.com/10-lsof-command-examples-in-linux/) 

The following commands might work without sudo. Distributions might vary, and user's access rights. You might sometimes need sudo to see all processes.
```shell
sudo lsof -i                // List all processes listening to ports, e.g. ssh connections 
sudo lsof -i | grep node    // List all processes listening to ports, only show lines mentioning *node*
sudo lsof -i TCP:22         // List process listening to *TCP port 22*
sudo lsof -i TCP:8600-8888  // List all processes listening to a *port between 8600 and 8888*      
sudo lsof -p 1234           // List all resources that the *process 1234* has open
sudo lsof -i -u juuuser2    // List all resources used by *user juuuser2*

```
Let's assume the line had something like 2344 or 963 in the beginning, indicating the process ID

Now, with the Process ID we can kill that process if needed. 9 means forcing the kill. "All nine lifes of the cat"
```shell
kill -9 2344
```

<hr />
## What about Windows then? How to find out what process is running at port 8888? And lets assume process id found was again 2344
```
netstat -aof | findstr 8888
kill 2344
```

<hr />
**Extra:** How to find out which ports are open and listened in your local system, you need the program nmap and the scanned IP address

```shell
sudo apt install nmap
sudo nmap 127.0.0.1         
```

```
// Output example:
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000040s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 0.16 seconds
```

**Note:** Be careful with address given to nmap, 
as it's *illegal* to scan other peoples' computers in Finland
