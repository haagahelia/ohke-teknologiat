# How to use the ufw (Uncomplicated FireWall) command to setup the Linux firewall 
(same firewall that some might earlier have set up via iptables)

**Note 1:** This help ***applies to Ubuntu/Xubuntu linux***. For other systems, like MacOS, or for virtual machines, virtual boxes, cloud environments, etc. things might be different! Then just read this, digest the concepts and apply the skills using different commands where needed. 

**Note 2:** In some virtual or cloud environments you cannot set the firewall from inside the OS, but from the outside host environment.

**Note 3:** Ubuntu (or lighter: Xubuntu) does not have firewall enabled after installation! Thus, your first action should usually be enabling the firewall.

Ubuntu/Xubuntu already has the ufw program, but in some other systems you might need to install it:

```shell 
sudo apt install ufw
```

Then, once the ufw tool installed, use it to enable the Linux firewall with this command. The two other ones are already like that initially by default, but it doesn't hurt to run them explicitly.
```shell 
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Checking what is the status of the Linux firewall
```shell 
sudo ufw status verbose
sudo ufw status numbered
```

Here are some commands to set firewall to log blocked connection attempts. And to define the level of seriousness of the logged messages.
```shell
sudo ufw logging on
sudo ufw status verbose
sudo ufw logging medium
sudo ufw status verbose
```
How to see what communication has been blocked, use either of these commands
```shell
less /var/log/ufw.log          // OR with sudo if required
tail -n 15 /var/log/ufw.log    // add the -f if want to make e.g. updating secondary console window of the latest log
```

Manual: [https://wiki.ubuntu.com/UncomplicatedFirewall](https://wiki.ubuntu.com/UncomplicatedFirewall) 

This page seems to have most of what you need:  (Most useful commands introduced already above though): [https://www.linuxbabe.com/security/ufw-firewall-debian-ubuntu-linux-mint-server](https://www.linuxbabe.com/security/ufw-firewall-debian-ubuntu-linux-mint-server)
