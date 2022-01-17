# How to use the ufw (Uncomplicated FireWall) command to setup the Linux firewall

**Note:** This document ***applies to Ubuntu/Xubuntu linux***. For other systems, like MacOS, things are different! Then just read, digest and act if needed.

**Note:** Ubuntu (or lighter: Xubuntu) does not have firewall enabled after installation! Thus the first action should be enabling the firewall.

Ubuntu/Xubuntu already has the ufw program, but in some other systems you might need to install it:

```shell 
sudo apt install ufw
```

Then, once the ufw tool installed, use it to enable the firewall with this command. The two other ones are already like that initiall, but it doesn't hurt to run them.
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
less /var/log/ufw.log   // OR with sudo if required
tail -n 15 /var/log/ufw.log
```

This page seems to have most of what you need:  (Most useful commands introduced already above though): [https://www.linuxbabe.com/security/ufw-firewall-debian-ubuntu-linux-mint-server](https://www.linuxbabe.com/security/ufw-firewall-debian-ubuntu-linux-mint-server)
