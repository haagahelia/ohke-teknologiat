# Some commands for finding out which ports are open in the system and which processes are listening to those. And killing that process

One way to get your own IP address, it's for the WLAN or Ethernet network adapter
```shell
ifconfig
```

**Extra:** How to find out which ports are open and listened in your local system, you need the program nmap and the scanned IP address
```shell
sudo apt install nmap
sudo nmap 127.0.0.1         
```
**Note:** Be careful with address given to nmap, 
as it's illegal to scan other peoples' computers in Finland

Now you might have port numbers you are interested in. Or you might get that from a Node.js / create-react-app Node error messages. EADDRINUSE or so. 3000 or so.

The following commands might work without sudo. Distributions might vary, and user's access rights.
```shell
sudo netstat -a | more           // -a=all, -t=TCP -u=UDP, -l=listening,     

sudo netstat -l   // all listening ports
sudo netstat -lt  // listening TCP ports
netstat -s        // -s statistics
netstat -tp       // -p means processID,PID               
                  // -tp   all TCP ports with PID
netstat -tulpn    // all the above plus also paramter n=numerical ports/addresses 
```
You can add a filter that only greps the lines that contain certain data of interest. 

E.g. this might list the processes (with the PID) that are listening to TCP port 8787, if any such exist
```shell
netstat -tp | grep '8787'
```

Let's assume the line had something like 2344 or 963 in the beginning, indicating the process ID

Now, with the Process ID we can kill that process if needed. 9 means forcing the kill. "All nine lifes of the cat"
```shell
kill -9 2344
```


More info here, though most was already available in examples above: [https://www.tecmint.com/20-netstat-commands-for-linux-network-management/](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/)

Another very interested command is **lsof** that can do a lot of things: [https://www.tecmint.com/10-lsof-command-examples-in-linux/](https://www.tecmint.com/10-lsof-command-examples-in-linux/) 