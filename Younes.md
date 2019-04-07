Title
===

Der Zugriff auf Raspberry ist mit SSHFS. Es ermöglicht den zugriff von überall.

Das ist Zugriff auf Filssystem durch ssh tunnel :  

Command: 

```
sudo apt-get install sshfs
sudo groupadd fuse
sudo adduser $USER fuse
sudo chown root:fuse /dev/fuse
mkdir /home/you/raspberry2
sshfs pi@192.168.1.5:/home/pi /home/you/raspberry2
```

