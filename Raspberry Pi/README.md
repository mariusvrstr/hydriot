# Raspberry Pi Remote VS Code Environment #
Easily developer on your Raspberry Pi device from your desktop over wifi, no need to swap keyboard and mouse everytime you want to do some IoT dev.



## Raspberry Pi Dev Environment Setup ##
+ [Latest Raspian OS](https://www.raspberrypi.org/documentation/installation/installing-images) on your Raspberry Pi
+ Update the default (raspberry) password for the (pi) user 
  Should get prompted after first boot else you can manually start it with `$ sudo raspi-config`

+ Connected to local Wi-Fi (IoT devices is not known for being secure suggest subnetwork / VLAN isolation)
+ [Download](https://code.visualstudio.com/#alt-downloads) the latest VS Code for Debian (ARM .deb file) and install
    + Install Extentions: Python Extention, Pilint and Autopep8
+ Enable SSH (Disabled by default)
  Raspberry Icon > Preferences > Raspberry Pi Configuration > Interfaces > SSH enable > OK
  ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/EnableSSH.png)
+ Configure static IP (Else the IP will change from time to time)
    + Get current interface name and IP `$ ip r | grep default`
      via = DHCP IP, wlan0 = interface name, src IP = issued IP
    + Get the device Mac for interface  `$ cat /sys/class/net/{interface name}/address`
    + Configure a static reservation on the network DHCP
    
      ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/ReserveDHCP.png)
    + Restart the raspberry pi or renew the IP
    
    ```console
   	sudo dhclient -r
    sudo dhclient
    ```
+ Create a new Dev folder (/home/pi/Dev)


## Configure Desktop Environment ##
+ [Download](https://code.visualstudio.com/#alt-downloads) and install VS Code
    + Install the **Remote - SSH** extension
+ Connect to the Raspberry Pi VS Code
    + Open the remote explorer
      ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/RemoteVsCodeExplorer.png)
    + SSH Targets + Add (Use the Raspberry Pi IP set by DHCP)
    + Enter the SSH command `$ SSH [user]@[IP/fqdn] -A`
    
      ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/sshCommand.png)
    + Choose Linux OS and enter password as prompted (Updated pi user password)
      If you have issues here first check that SSH work with the same command from PowerShell






