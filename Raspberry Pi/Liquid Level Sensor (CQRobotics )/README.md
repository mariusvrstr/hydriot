# Liquid Level Sensor - CQRobotics #
Measure if the sensor is in contact with liquid

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/Liquid%20Level%20Sensor%20(CQRobotics%20)/resources/sensor.jpg)


## Resources ##

* [Buy from Amzon](https://www.amazon.com/CQRobot-Consumption-Resistance-Temperature-Properties/dp/B07ZMGW3QJ) (~R270)
* [Product Wiki](http://www.cqrobot.wiki/index.php/Liquid_Level_Sensor)

## Setup ##

- [X] A Raspberry Pi with VS Code and Python Environment 
- [ ] Connect the sensor with the Raspberry Pi
- [ ] Install WiringPI (CPP Library)
- [ ] Run the sample python script

### Connect the sensor with the Raspberry Pi ###

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/Liquid%20Level%20Sensor%20(CQRobotics%20)/resources/connection.jpg)

### Install WiringPI ###

Run the configuration once:

```console
sudo python3 CQRobot_ADS1115.py
```

Monitor the Voltage

```console
sudo python3 ADS1115_ReadVoltage.py
```

### Run the sample_python.py file ###

