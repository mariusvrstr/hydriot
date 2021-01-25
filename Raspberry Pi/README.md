# Raspberry Pi Remote VS Code Environment #
Easily developer on your Raspberry Pi device from your desktop over wifi, no need to swap keyboard and mouse everytime you want to do some IoT dev.



## Raspberry Pi Dev Environment Setup ##
+ [Latest Raspian OS](https://www.raspberrypi.org/documentation/installation/installing-images) on your Raspberry Pi
+ Update the default (raspberry) password for the (pi) user 
  Should get prompted after first boot else you can manually start it with `$ sudo raspi-config`

+ Connected to local Wi-Fi (IoT devices is not known for being secure suggest subnetwork / VLAN isolation)
+ [Download](https://code.visualstudio.com/#alt-downloads) the latest VS Code for Debian (ARM .deb file) and install
+ Enable SSH (Disabled by default)
  Raspberry Icon > Preferences > Raspberry Pi Configuration > Interfaces > SSH enable > OK
  ![https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/EnableSSH.png]
+ Configure static IP (Else the IP will change from time to time)
    + Get current interface name and IP (`$ ip r | grep default`)
      via IP = DHCP, wlan0 = interface name, src IP = issued IP




