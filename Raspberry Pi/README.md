# Raspberry Pi Remote VS Code Environment #
Easily developer on your Raspberry Pi device from your desktop over wifi, no need to swap keyboard and mouse everytime you want to do some IoT dev.

* Raspberry Pi Dev Environment Setup
* Configure Desktop Environment
* Configure SSH Key

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


## Configure SSH Key ##
This is optional but will allow you to connect seemlessly without needing to enter a password often during remote session. Note that this approach is not the most secure as your will have your SSH private key in cleartext file on your Desktop but good enough for dev.
+ Generate a SSH Key from PuttyGen
    + Copy public key into a **id_rsa.pub** file
  
      ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/PuTTyGen_publicKey.png)  
    + Save the private key (In Open SSH format) as **id_rsa** file

      ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/PuTTyGen_privateKey.png)  
    + Copy the above 2 files to C:\Users\{username}\.ssh\pi\
    
      ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/sshKeys.png)  
+ Add Key to Raspberry Pi (Can use remote PowerShell SSH connection - Makes copy paste easier)
    + Open SSH connection to PI e.g. `ssh pi@10.0.0.15`
    + Create SSH Folder (Will complain if already exist) `$ sudo mkdir ~/.ssh`
    + Edit the SSH Authorization file `$ sudo nano ~/.ssh/authorized_keys`
      Copy paste from **id_rsa.pub** (Public Key) file >> Cntr+O (Save) Cntr+X (Exit)
    + Protect the file properly
    
      ```console
      sudo chmod 700 ~/.ssh
      sudo chmod 700 ~/.ssh -R
      sudo chmod 600 ~/.ssh/authorized_keys
      sudo chmod 644 ~/.ssh/authorized_keys
      sudo chown pi:pi ~/.ssh/authorized_keys    
      ```
      
+ Configure the SSH Connection
    + Open the config file (Global SSH config file) in VS Code (Settings cog in remote window)
    + Add the IdentityFile reference pointing to the id_rsa file (Private Key)
    
    ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/sshConfigurationFile.png)    
    + Save and restart VS Code (Desktop)
+ Reconnect to remote VS Code environment (Should NOT prompt for pass)
