# PH Sensor
pH sensors usually read the voltage to an analog BNC adapter, as such they need a analog to digital converter to work with the Raspberry Pi.

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/pH%20Sensor%20(GAOHOU)/_resources/gaohou.jpg)
![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/pH%20Sensor%20(GAOHOU)/_resources/ph_sensor.jpg)
![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/pH%20Sensor%20(GAOHOU)/_resources/adc_module.jpg)

## Overview
* pH range from 0 (acid) to 14 (caustic) with pure water in the middle with pH 7

## Approach
* Short the BNC connector (Outside with inside), this must simualte a neutral pH of 7. Adjust the offset to calibrate.
* pH readings are neutroriously volitile use average to stabilize e.g. average 20 readings with 10 milisecond delay

## Connecting the Probe

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/pH%20Sensor%20(GAOHOU)/_resources/ph_connection.jpg)

+ BNC
    + Red (V+ VCC)
    + Black (GND G)
    + Blue (Po - pH Out)
+ Ocean ADS1115 (Channel A1)
    + Black (G)
    + Red (V)
    + Blue (S)
+ Raspberry Pi
    + Black (Pin 6)
    + Red (Pin 4)
    + Blue (Pin 5 GPIO3)
    + Green (Pin 3 GPIO2)

## Maintenance

+ pH readings needs to be calibrated to keep readings accurate
    + First calibrate to neutral by short circut the BNC connector and updating the OFFSET to get a consistant pH 7
    + Then calibrate the sensor by using pH solutions (Buffers) e.g. 4, 6.86, 9.18
+ pH probe need to be cleaned from time to time to keep readings accurate (DO NOT WIPE!!!)
    + Switl electrode gently in cleaning solutions
    + Rinse in deionized or distilled water
    + Store in storage solution
+ pH probes make use of chemicals and usually need to be replaced withing 3 years

## Resources
* [Manual](http://www.baaqii.net/promanage/BU0203%2BBU0481.pdf)
* [Files and scripts](www.baaqii.net/promanage/BU0203.zip)
 

