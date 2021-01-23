# Total Desolvable Solids (TDS) Sensor - CQRobotics #
Measure what the solid counts is

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/TDS%20Sensor%20(CQRobotics)/resources/tds_sensor.jpg)
![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/TDS%20Sensor%20(CQRobotics)/resources/adc_module.jpg)

Important

## Resources ##

* TDS Sensor
** [Buy TDS Sensor from Amzon](https://www.amazon.com/CQRobot-Ocean-Compatible-Scientific-Laboratory/dp/B08KXRHK7H/ref=sr_1_4?crid=1KJNXUKV7RPCC&dchild=1&keywords=tds+meter+sensor&qid=1611391268&sprefix=TDS+Meter+Sensor%2Cdigital-text%2C1004&sr=8-4) (~R220)
** [Product Wiki](http://www.cqrobot.wiki/index.php/Liquid_Level_Sensor)
* ADC Module (Analog to Digital Signal Converter)
** [By ADC Module from Amazon](https://www.amazon.com/gp/product/B08KFZ3PVT/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) (~R240)
** [Product Wiki](http://www.cqrobot.wiki/index.php/ADS1115_16-Bit_ADC_Module)

## Setup ##

- [X] A Raspberry Pi with VS Code and Python Environment 
- [ ] Connect the sensor with the Raspberry Pi
- [ ] Enable I2C in Interfaces
- [ ] Check the I2C Switch
- [ ] Run the files

### Connect the sensor with the Raspberry Pi ###

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/TDS%20Sensor%20(CQRobotics)/resources/connection.jpg)
___<sup>Connect the Sensor to the ADC Module on the A2 channel (G,V,S)</sup>___


### Enable I2C in Interfaces ###

Enable I2C Interface in Raspberry Pi Config

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/TDS%20Sensor%20(CQRobotics)/resources/I2C_config.png)

### Check the I2C Switch ###

On the ADC Module there is a hardware switch on the circut board with one of two options (0X48 or 0X49)

Ensure that it is set to point to >> **0X48**

### Run the files ###

Run the configuration once:

```console
sudo python3 CQRobot_ADS1115.py
```

Monitor the Voltage

```console
sudo python3 ADS1115_ReadVoltage.py
```
